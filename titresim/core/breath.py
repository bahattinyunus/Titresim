"""
titresim/core/breath.py
Biyogeribildirim & Terapötik Solunum Akustik Rehber Motoru (Coherence Breath Guide).
0.1 Hz Kalp Koheransı, Kutu Nefesi (Box Breathing), 4-7-8 Uyku Nefesi ve Pranayama
için dinamik ses frekansı modülasyonu ile nefes alış, tutuş ve veriş fazlarını yönlendirir.
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Tuple
import math
from .generator import ADSR


@dataclass
class BreathPattern:
    id: str
    name: str
    inhale_sec: float
    hold_in_sec: float
    exhale_sec: float
    hold_out_sec: float
    target_bpm: float
    target_hz: float
    description: str
    clinical_effect: str

    @property
    def total_cycle_sec(self) -> float:
        return self.inhale_sec + self.hold_in_sec + self.exhale_sec + self.hold_out_sec


class CoherenceBreathGuide:
    """Akustik solunum koheransı ve nefes seansı sentezleyici."""

    PATTERNS: Dict[str, BreathPattern] = {
        "coherence": BreathPattern(
            id="coherence",
            name="0.10 Hz Kardiyak Koherans Nefesi",
            inhale_sec=5.5,
            hold_in_sec=0.0,
            exhale_sec=5.5,
            hold_out_sec=0.0,
            target_bpm=5.5,
            target_hz=0.091,
            description="5.5 saniye nefes alış, 5.5 saniye nefes veriş.",
            clinical_effect="Baroreseptör refleksi kilitlenmesi, maksimum Kalp Hızı Değişkenliği (HRV) ve vagal tonus artışı."
        ),
        "box": BreathPattern(
            id="box",
            name="Kutu Nefesi (Box Breathing / Donanma Odak Nefesi)",
            inhale_sec=4.0,
            hold_in_sec=4.0,
            exhale_sec=4.0,
            hold_out_sec=4.0,
            target_bpm=3.75,
            target_hz=0.0625,
            description="4s Alış, 4s Tutuş, 4s Veriş, 4s Boş Tutuş.",
            clinical_effect="Akut stres baskılama, zihinsel panik yatıştırma, yüksek odak ve berraklık."
        ),
        "4-7-8": BreathPattern(
            id="4-7-8",
            name="4-7-8 Dr. Andrew Weil Uyku & Anksiyete Nefesi",
            inhale_sec=4.0,
            hold_in_sec=7.0,
            exhale_sec=8.0,
            hold_out_sec=0.0,
            target_bpm=3.15,
            target_hz=0.052,
            description="4s Burundan Alış, 7s Tutuş, 8s Ağızdan Veriş.",
            clinical_effect="Kanda karbondioksit dengesi, hızlı parasempatik kilitlenme ve uykuya dalış."
        ),
        "relax": BreathPattern(
            id="relax",
            name="Yumuşak Gevşeme Nefesi (1:1.5 Oranı)",
            inhale_sec=4.0,
            hold_in_sec=0.0,
            exhale_sec=6.0,
            hold_out_sec=0.0,
            target_bpm=6.0,
            target_hz=0.10,
            description="4s Alış, 6s Yavaş Veriş.",
            clinical_effect="Uzamış nefes veriş ile vagal fren uyarımı ve kas gevşemesi."
        )
    }

    @classmethod
    def get_pattern(cls, pattern_id: str) -> BreathPattern:
        pid = pattern_id.strip().lower()
        if pid in cls.PATTERNS:
            return cls.PATTERNS[pid]
        for k, p in cls.PATTERNS.items():
            if pid in k or pid in p.name.lower():
                return p
        return cls.PATTERNS["coherence"]

    @classmethod
    def generate_guided_session(
        cls,
        pattern_id: str = "coherence",
        total_duration_sec: float = 60.0,
        base_freq: float = 216.0,
        volume: float = 0.5,
        sample_rate: int = 44100
    ) -> List[float]:
        """
        Nefes alış (yükselen frekans), tutuş (sabit tını) ve veriş (alçalan frekans)
        akustik kılavuz seansı sentezler.
        """
        pattern = cls.get_pattern(pattern_id)
        cycle_len = pattern.inhale_sec + pattern.hold_in_sec + pattern.exhale_sec + pattern.hold_out_sec
        if cycle_len <= 0:
            cycle_len = 11.0

        num_cycles = max(1, int(math.ceil(total_duration_sec / cycle_len)))
        all_samples: List[float] = []
        two_pi = 2.0 * math.pi

        for _ in range(num_cycles):
            # 1. FAZ: NEFES ALIŞ (Glissando: base_freq -> base_freq * 1.33)
            inhale_samples = int(pattern.inhale_sec * sample_rate)
            f_start = base_freq
            f_end = base_freq * 1.333
            for i in range(inhale_samples):
                t = i / inhale_samples
                cur_f = f_start + (f_end - f_start) * t
                env = math.sin(math.pi * t)  # yumuşak kubbe zarfı
                sample = math.sin(two_pi * cur_f * (i / sample_rate)) * volume * (0.3 + 0.7 * t)
                all_samples.append(sample)

            # 2. FAZ: NEFES TUTUŞ (Sabit yüksek ton)
            if pattern.hold_in_sec > 0:
                hold_samples = int(pattern.hold_in_sec * sample_rate)
                for i in range(hold_samples):
                    sample = math.sin(two_pi * f_end * (i / sample_rate)) * (volume * 0.4)
                    all_samples.append(sample)

            # 3. FAZ: NEFES VERİŞ (Glissando: f_end -> base_freq)
            exhale_samples = int(pattern.exhale_sec * sample_rate)
            for i in range(exhale_samples):
                t = i / exhale_samples
                cur_f = f_end - (f_end - f_start) * t
                sample = math.sin(two_pi * cur_f * (i / sample_rate)) * volume * (1.0 - 0.6 * t)
                all_samples.append(sample)

            # 4. FAZ: BOŞ TUTUŞ (Sabit alçak ton)
            if pattern.hold_out_sec > 0:
                hold_out_samples = int(pattern.hold_out_sec * sample_rate)
                for i in range(hold_out_samples):
                    sample = math.sin(two_pi * f_start * (i / sample_rate)) * (volume * 0.25)
                    all_samples.append(sample)

            if len(all_samples) >= int(total_duration_sec * sample_rate):
                break

        # Süreyi sınırla
        max_len = int(total_duration_sec * sample_rate)
        return all_samples[:max_len]
