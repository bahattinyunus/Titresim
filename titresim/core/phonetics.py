"""
titresim/core/phonetics.py
Kutsal Kelâm ve Biyoakustik Fonetik Formant Motoru (Sacred Phonetics & Formant Synthesizer).
Tecvid ilmindeki Gunne (Ghunnah / Nazal Rezonans), Hayşûm ve Mahreç formantlarını ($F_1, F_2, F_3$)
modeller ve zikir/dua akustik rezonans dalgaları sentezler.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple
import json
import math
from .generator import ToneGenerator, ADSR

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


@dataclass
class SacredChant:
    id: str
    name: str
    tradition: str
    formants: List[float]
    base_pitch_hz: float
    mahref: str
    description: str
    effects: str
    nitric_oxide_effect: str


def _normalize(text: str) -> str:
    t = text.lower().strip()
    replacements = [
        ("ı", "i"), ("ğ", "g"), ("ü", "u"), ("ş", "s"), ("ö", "o"), ("ç", "c"),
        ("â", "a"), ("î", "i"), ("û", "u"), ("-", " "), ("_", " ")
    ]
    for s, d in replacements:
        t = t.replace(s, d)
    return " ".join(t.split())


class SacredPhonetics:
    """Kutsal kelam ve vokal formant ses motoru."""

    @classmethod
    def get_all(cls) -> List[SacredChant]:
        path = DATA_DIR / "phonetics.json"
        if not path.exists():
            return []
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [
                SacredChant(
                    id=item["id"],
                    name=item["name"],
                    tradition=item.get("tradition", ""),
                    formants=[float(x) for x in item.get("formants", [400, 1200, 2500])],
                    base_pitch_hz=float(item.get("base_pitch_hz", 220.0)),
                    mahref=item.get("mahref", ""),
                    description=item.get("description", ""),
                    effects=item.get("effects", ""),
                    nitric_oxide_effect=item.get("nitric_oxide_effect", "")
                )
                for item in data
            ]

    @classmethod
    def find_by_id(cls, query: str) -> Optional[SacredChant]:
        q = _normalize(query)
        for chant in cls.get_all():
            norm_id = _normalize(chant.id)
            norm_name = _normalize(chant.name)
            if q == norm_id or q in norm_name or norm_id in q:
                return chant
        return None

    @classmethod
    def synthesize_chant(
        cls,
        chant_id: str,
        duration: float = 5.0,
        base_pitch: Optional[float] = None,
        volume: float = 0.5,
        sample_rate: int = 44100
    ) -> List[float]:
        """
        Belirtilen kutsal zikrin formant rezonanslarını vokal nefes hissiyle sentezler.
        F1, F2, F3 formant frekansları ve temel taşıyıcı ton birleştirilir.
        """
        chant = cls.find_by_id(chant_id)
        if not chant:
            raise ValueError(f"Kutsal kelâm bulunamadı: {chant_id}")

        pitch = base_pitch if base_pitch else chant.base_pitch_hz
        formants = chant.formants  # [F1, F2, F3]

        total_samples = int(sample_rate * duration)
        samples = [0.0] * total_samples
        two_pi = 2.0 * math.pi

        # Vokal nefes zarfı (uzun yumuşak giriş ve sönüm)
        adsr = ADSR(attack=1.2, decay=0.3, sustain_level=0.85, release=1.5)

        # Temel tını + 3 Formant rezonatörü
        # Ağırlıklar: Temel ton (0.4), F1 (0.3), F2 (0.2), F3 (0.1)
        layers = [
            (pitch, 0.45),
            (formants[0], 0.25),
            (formants[1], 0.18),
            (formants[2], 0.08) if len(formants) > 2 else (pitch * 3, 0.05)
        ]

        for freq, weight in layers:
            phase = 0.0
            step = two_pi * freq / sample_rate
            for i in range(total_samples):
                t = i / sample_rate
                env = adsr.get_amplitude(t, duration)
                # Hafif vibrato
                vib = 1.0 + 0.005 * math.sin(two_pi * 4.5 * t)
                samples[i] += math.sin(phase) * weight * env * volume
                phase += step * vib
                if phase > two_pi:
                    phase -= two_pi

        return samples
