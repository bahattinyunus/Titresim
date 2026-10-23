"""
titresim/core/architecture.py
Kutsal Mimari Akustiği, Mimar Sinan Kubbe Rezonatörleri (Helmholtz Küpleri),
Ħal Saflieni 110 Hz Kâhin Odası ve Schroeder Yankılanma (Reverberation) Simülatörü.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import math
import json
from pathlib import Path


@dataclass
class SacredSpace:
    id: str
    name: str
    architect: str
    volume_m3: float
    rt60_sec: float
    resonators_count: int
    resonator_type: str
    resonator_frequency_hz: float
    description: str
    predelay_ms: float
    decay_time_sec: float
    damping: float
    early_diffusion: float


class AcousticArchitecture:
    """Kutsal mekânların akustik fiziği ve Mimar Sinan rezonatör motoru."""

    _DATA_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "architecture.json"
    _DATA: Optional[Dict[str, Any]] = None

    @classmethod
    def _load_data(cls) -> Dict[str, Any]:
        if cls._DATA is None:
            if cls._DATA_PATH.exists():
                with open(cls._DATA_PATH, "r", encoding="utf-8") as f:
                    cls._DATA = json.load(f)
            else:
                cls._DATA = {"sacred_spaces": []}
        return cls._DATA

    @classmethod
    def list_spaces(cls) -> List[SacredSpace]:
        data = cls._load_data()
        spaces = []
        for s in data.get("sacred_spaces", []):
            sig = s.get("acoustic_signature", {})
            spaces.append(SacredSpace(
                id=s["id"],
                name=s["name"],
                architect=s.get("architect", ""),
                volume_m3=float(s.get("volume_m3", 1000.0)),
                rt60_sec=float(s.get("rt60_sec", 2.0)),
                resonators_count=int(s.get("resonators_count", 0)),
                resonator_type=s.get("resonator_type", ""),
                resonator_frequency_hz=float(s.get("resonator_frequency_hz", 200.0)),
                description=s.get("description", ""),
                predelay_ms=float(sig.get("predelay_ms", 30.0)),
                decay_time_sec=float(sig.get("decay_time_sec", 2.5)),
                damping=float(sig.get("damping", 0.3)),
                early_diffusion=float(sig.get("early_diffusion", 0.8))
            ))
        return spaces

    @classmethod
    def get_space(cls, space_id: str) -> Optional[SacredSpace]:
        norm = space_id.lower().replace("-", "").replace("_", "")
        for s in cls.list_spaces():
            if s.id.lower() == norm or norm in s.id.lower():
                return s
        return None

    @staticmethod
    def calculate_helmholtz_frequency(
        cavity_volume_liters: float,
        neck_radius_cm: float,
        neck_length_cm: float,
        speed_of_sound_ms: float = 343.0
    ) -> float:
        """
        Mimar Sinan'ın Süleymaniye kubbesindeki akustik küplerin teorik rezonans frekansı.
        f = (c / 2*pi) * sqrt(A / (V * L_eff))
        L_eff = L + 1.6 * r (akustik uç düzeltmesi)
        """
        v_m3 = cavity_volume_liters * 0.001
        r_m = neck_radius_cm * 0.01
        l_m = neck_length_cm * 0.01
        area_m2 = math.pi * (r_m ** 2)
        l_eff = l_m + 1.6 * r_m

        if v_m3 <= 0 or l_eff <= 0 or area_m2 <= 0:
            return 0.0

        freq = (speed_of_sound_ms / (2.0 * math.pi)) * math.sqrt(area_m2 / (v_m3 * l_eff))
        return round(freq, 2)

    @classmethod
    def apply_reverberation(
        cls,
        input_samples: List[float],
        space_id: str = "suleymaniye",
        sample_rate: int = 44100,
        wet_mix: float = 0.40
    ) -> List[float]:
        """
        Girdiye kutsal mekânın akustik yankılanma ve Helmholtz rezonansını uygular.
        Schroeder/Moorer tabanlı 4 paralel tarak filtre (comb) ve 2 kaskat tüm-geçiren (allpass) filtre.
        """
        space = cls.get_space(space_id) or cls.get_space("suleymaniye")
        rt60 = space.rt60_sec if space else 4.0
        damping = space.damping if space else 0.35
        predelay_sec = (space.predelay_ms if space else 40.0) / 1000.0
        predelay_samples = int(predelay_sec * sample_rate)

        # Schroeder Comb filtre gecikme süreleri (asal sayı örnekler)
        comb_delays = [
            int(sample_rate * 0.0297),
            int(sample_rate * 0.0371),
            int(sample_rate * 0.0411),
            int(sample_rate * 0.0437)
        ]

        comb_buffers = [[0.0] * d for d in comb_delays]
        comb_indices = [0] * 4
        comb_filter_stores = [0.0] * 4

        # Geri besleme katsayıları: g = 10^(-3 * delay / (RT60 * fs))
        comb_gains = [
            10.0 ** (-3.0 * (d / sample_rate) / rt60)
            for d in comb_delays
        ]

        # All-pass filtre parametreleri
        allpass_delays = [
            int(sample_rate * 0.005),
            int(sample_rate * 0.0017)
        ]
        allpass_buffers = [[0.0] * d for d in allpass_delays]
        allpass_indices = [0] * 2
        allpass_gain = 0.5

        # Predelay buffer
        predelay_buf = [0.0] * max(1, predelay_samples)
        predelay_idx = 0

        # Çıktı dizisi (yankılanma kuyruğu için biraz uzatılır)
        tail_samples = int(sample_rate * min(rt60 * 0.8, 3.0))
        total_len = len(input_samples) + tail_samples
        output = [0.0] * total_len

        # Mekânın Helmholtz küp rezonatör frekansı (Süleymaniye'de ~250 Hz bas uğultusu emici)
        res_freq = space.resonator_frequency_hz if space else 250.0
        w0 = 2.0 * math.pi * res_freq / sample_rate
        # Basit rezonans filtresi değişkenleri
        res_y1 = 0.0
        res_y2 = 0.0

        for i in range(total_len):
            x = input_samples[i] if i < len(input_samples) else 0.0

            # Predelay
            delayed_x = predelay_buf[predelay_idx]
            predelay_buf[predelay_idx] = x
            predelay_idx = (predelay_idx + 1) % len(predelay_buf)

            # 4 Paralel Comb Filtre
            comb_sum = 0.0
            for c in range(4):
                d = comb_delays[c]
                idx = comb_indices[c]
                buf = comb_buffers[c]

                out_val = buf[idx]
                # Damping (Alçak geçiren filtre)
                store = out_val * (1.0 - damping) + comb_filter_stores[c] * damping
                comb_filter_stores[c] = store

                buf[idx] = delayed_x + store * comb_gains[c]
                comb_indices[c] = (idx + 1) % d
                comb_sum += out_val

            comb_out = comb_sum * 0.25

            # 2 Seri Allpass Filtre
            ap_in = comb_out
            for a in range(2):
                d = allpass_delays[a]
                idx = allpass_indices[a]
                buf = allpass_buffers[a]

                buf_out = buf[idx]
                ap_out = -allpass_gain * ap_in + buf_out
                buf[idx] = ap_in + allpass_gain * ap_out
                allpass_indices[a] = (idx + 1) % d
                ap_in = ap_out

            reverb_wet = ap_in

            # Sinan'ın küpleri: 250 Hz civarındaki bas patlamasını absorbe ederken rezonans katar
            res_val = 0.08 * math.sin(w0) * reverb_wet + 0.85 * res_y1 - 0.2 * res_y2
            res_y2 = res_y1
            res_y1 = res_val
            reverb_wet += res_val

            dry = x
            output[i] = (1.0 - wet_mix) * dry + wet_mix * reverb_wet

        # Normalizasyon
        max_val = max(abs(s) for s in output) or 1.0
        return [s / max_val * 0.85 for s in output]

    @classmethod
    def generate_impulse_response(
        cls,
        space_id: str = "suleymaniye",
        duration: float = 4.0,
        sample_rate: int = 44100
    ) -> List[float]:
        """Bir mekânın akustik dürtü yanıtını (Impulse Response) sentezler."""
        num_samples = int(sample_rate * duration)
        impulse = [0.0] * num_samples
        impulse[0] = 1.0  # Birim dürtü
        return cls.apply_reverberation(impulse, space_id=space_id, sample_rate=sample_rate, wet_mix=1.0)
