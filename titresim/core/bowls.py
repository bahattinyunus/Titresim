"""
titresim/core/bowls.py
Himalaya ve Tibet Ses Çanakları (Singing Bowls) & Gong Akustik Fiziği.
Dairesel asimetriden doğan vuruş nabzı (beating / chattering),
inharmonik radyal modlar, tokmak vuruşu (struck) ve dönen sürtünme (singing rim) sentezi.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import math
import random
import json
from pathlib import Path


@dataclass
class SingingBowl:
    id: str
    name: str
    fundamental_hz: float
    beating_hz: float
    modal_ratios: List[float]
    damping: float
    chakra: str
    alloy: str
    faraday_droplet_pattern: str
    traditional_use: str
    healing_effects: str


class SingingBowlAcoustics:
    """Tibet ses çanakları ve gongların fiziksel modal akustik motoru."""

    _DATA_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "bowls.json"
    _DATA: Optional[Dict[str, Any]] = None

    @classmethod
    def _load_data(cls) -> Dict[str, Any]:
        if cls._DATA is None:
            if cls._DATA_PATH.exists():
                with open(cls._DATA_PATH, "r", encoding="utf-8") as f:
                    cls._DATA = json.load(f)
            else:
                cls._DATA = {"singing_bowls": []}
        return cls._DATA

    @classmethod
    def list_bowls(cls) -> List[SingingBowl]:
        data = cls._load_data()
        bowls = []
        for item in data.get("singing_bowls", []):
            bowls.append(SingingBowl(
                id=item["id"],
                name=item["name"],
                fundamental_hz=float(item["fundamental_hz"]),
                beating_hz=float(item.get("beating_hz", 1.8)),
                modal_ratios=[float(r) for r in item.get("modal_ratios", [1.0, 2.71, 5.4])],
                damping=float(item.get("damping", 0.12)),
                chakra=item.get("chakra", ""),
                alloy=item.get("alloy", ""),
                faraday_droplet_pattern=item.get("faraday_droplet_pattern", ""),
                traditional_use=item.get("traditional_use", ""),
                healing_effects=item.get("healing_effects", "")
            ))
        return bowls

    @classmethod
    def get_bowl(cls, bowl_id: str) -> Optional[SingingBowl]:
        norm = bowl_id.lower().replace("-", "").replace("_", "")
        for b in cls.list_bowls():
            b_norm = b.id.lower().replace("-", "").replace("_", "")
            if b_norm == norm or norm in b_norm:
                return b
        return None

    @classmethod
    def synthesize_struck_bowl(
        cls,
        bowl_id: str = "full_moon_om",
        duration: float = 10.0,
        strike_force: float = 0.8,
        sample_rate: int = 44100
    ) -> List[float]:
        """
        Tokmak Vuruşu (Struck Mode) Simülasyonu.
        Vuruş anındaki sert temas şoku, ardından çanağın dairesel asimetrisinden kaynaklanan
        çift mod ayrışması (split doublets) ile 1-2 Hz'lik doğal akustik nabız (beating) ve
        üst inharmonik modların yumuşak sönümlenmesi.
        """
        bowl = cls.get_bowl(bowl_id)
        if not bowl:
            f0 = 136.1
            beat_hz = 1.5
            ratios = [1.0, 2.71, 5.42, 8.95]
            damping = 0.12
        else:
            f0 = bowl.fundamental_hz
            beat_hz = bowl.beating_hz
            ratios = bowl.modal_ratios
            damping = bowl.damping

        num_samples = int(sample_rate * duration)
        samples = [0.0] * num_samples

        # Temel zaman sabiti (tau)
        tau_base = (8.0 / (damping + 0.05)) * min(2.0, (200.0 / (f0 + 50.0)))
        tau_base = max(3.0, min(14.0, tau_base))

        # Tokmak temas gürültüsü süresi ~ 25 ms
        tau_strike = 0.025

        for i in range(num_samples):
            t = i / sample_rate

            # 1. Tokmak vuruş şoku (ilk milisaniyeler)
            transient = 0.0
            if t < 0.04:
                noise = (random.random() * 2.0 - 1.0) * strike_force * (1.0 - t / 0.04) ** 2
                transient = noise * 0.4

            # 2. Asimetrik Çift Mod (Split doublet -> Doğal akustik nabız/beating)
            # f0_a ve f0_b frekansları birbiriyle beat_hz farkla girişim yapar
            f0_a = f0 - (beat_hz * 0.5)
            f0_b = f0 + (beat_hz * 0.5)

            env_fund = math.exp(-t / tau_base)
            # Mikro yumuşak yükseliş (0 - 3 ms)
            if t < 0.003:
                env_fund *= (t / 0.003)

            val_fund = 0.55 * (
                math.sin(2.0 * math.pi * f0_a * t) +
                math.sin(2.0 * math.pi * f0_b * t + 0.2)
            ) * env_fund

            # 3. İnharmonik Üst Modlar (Faraday dalgaları üreten yüksek modlar)
            val_modes = 0.0
            for idx, r in enumerate(ratios[1:], start=1):
                m_freq = f0 * r
                if m_freq >= sample_rate * 0.48:
                    continue
                # Yüksek modlar katlanarak daha hızlı söner
                tau_m = tau_base / (idx * 2.2)
                env_m = math.exp(-t / max(0.5, tau_m))
                weight = 0.35 / (idx ** 1.3)
                # Üst modlarda da hafif genlik modülasyonu
                val_modes += math.sin(2.0 * math.pi * m_freq * t) * env_m * weight

            val = (val_fund + val_modes) * strike_force + transient
            samples[i] = val

        # Normalizasyon
        max_val = max(abs(s) for s in samples) or 1.0
        return [s / max_val * 0.85 for s in samples]

    @classmethod
    def synthesize_singing_rim(
        cls,
        bowl_id: str = "full_moon_om",
        duration: float = 12.0,
        rub_speed_hz: float = 1.6,
        sample_rate: int = 44100
    ) -> List[float]:
        """
        Dönen Tokmakla Sürtme (Singing / Rubbed Rim Mode) Simülasyonu.
        Tokmağın çanak kenarında dönmesiyle oluşan stick-slip rezonans birikimi.
        Sürekli ve derin bir uğultu, su yüzeyinde Faraday dalgalanması hissi veren
        dönen faz ve hafif vibrato üretir.
        """
        bowl = cls.get_bowl(bowl_id)
        if not bowl:
            f0 = 136.1
            beat_hz = 1.5
            ratios = [1.0, 2.71, 5.42]
        else:
            f0 = bowl.fundamental_hz
            beat_hz = bowl.beating_hz
            ratios = bowl.modal_ratios

        num_samples = int(sample_rate * duration)
        samples = [0.0] * num_samples

        # 3 saniyelik kademeli yükseliş (swell), 2 saniyelik kapanış (fade-out)
        attack_sec = 3.0
        release_sec = 2.5
        sustain_end = duration - release_sec

        for i in range(num_samples):
            t = i / sample_rate

            # Zarf (Envelope)
            if t < attack_sec:
                env = 0.5 * (1.0 - math.cos(math.pi * (t / attack_sec)))
            elif t < sustain_end:
                env = 1.0
            else:
                t_rel = t - sustain_end
                env = 0.5 * (1.0 + math.cos(math.pi * (t_rel / release_sec)))

            # Dönen tokmak modülasyonu (rotational friction swell)
            rot_mod = 0.85 + 0.15 * math.sin(2.0 * math.pi * rub_speed_hz * t)

            # Temel mod çifti (akustik nabız)
            f0_a = f0 - (beat_hz * 0.5)
            f0_b = f0 + (beat_hz * 0.5)

            val_fund = 0.6 * (
                math.sin(2.0 * math.pi * f0_a * t) +
                math.sin(2.0 * math.pi * f0_b * t + 0.3)
            )

            # Birinci ve ikinci inharmonik şan modu
            val_modes = 0.0
            for idx, r in enumerate(ratios[1:3], start=1):
                m_freq = f0 * r
                if m_freq < sample_rate * 0.45:
                    m_weight = 0.22 / idx
                    val_modes += math.sin(2.0 * math.pi * m_freq * t + idx) * m_weight

            # Tokmak ahşap/deri sürtünme dokusu (hafif pembe/hışırtı katmanı)
            friction_hiss = (random.random() * 2.0 - 1.0) * 0.04 * rot_mod

            samples[i] = (val_fund + val_modes + friction_hiss) * env * rot_mod * 0.75

        max_val = max(abs(s) for s in samples) or 1.0
        return [s / max_val * 0.82 for s in samples]
