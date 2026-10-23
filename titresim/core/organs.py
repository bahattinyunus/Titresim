"""
titresim/core/organs.py
Organ Rezonansı ve Biyofiziksel Frekans Terapisi Motoru (Vibroacoustic Organ Resonance).
Kalp, beyin, karaciğer, böbrekler, akciğerler, mide ve endokrin bezlerinin
biyofiziksel rezonans frekanslarını modeller ve şifa tonları sentezler.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional
import json
import math
from .generator import ToneGenerator, ADSR

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


@dataclass
class OrganInfo:
    id: str
    name: str
    frequency: float
    alternative_freqs: List[float]
    category: str
    element: str
    associated_chakra: str
    description: str
    effects: str
    healing_protocol: str


def _normalize(text: str) -> str:
    t = text.lower().strip()
    replacements = [
        ("ı", "i"), ("ğ", "g"), ("ü", "u"), ("ş", "s"), ("ö", "o"), ("ç", "c"),
        ("â", "a"), ("î", "i"), ("û", "u"), ("-", " "), ("_", " ")
    ]
    for s, d in replacements:
        t = t.replace(s, d)
    return " ".join(t.split())


class OrganResonance:
    """Organ ve doku rezonansı yönetim ve ses sentezleme sınıfı."""

    @classmethod
    def get_all(cls) -> List[OrganInfo]:
        path = DATA_DIR / "organs.json"
        if not path.exists():
            return []
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [
                OrganInfo(
                    id=item["id"],
                    name=item["name"],
                    frequency=float(item["frequency"]),
                    alternative_freqs=[float(f) for f in item.get("alternative_freqs", [])],
                    category=item.get("category", "genel"),
                    element=item.get("element", ""),
                    associated_chakra=item.get("associated_chakra", ""),
                    description=item.get("description", ""),
                    effects=item.get("effects", ""),
                    healing_protocol=item.get("healing_protocol", "")
                )
                for item in data
            ]

    @classmethod
    def find_by_id(cls, query: str) -> Optional[OrganInfo]:
        q = _normalize(query)
        for organ in cls.get_all():
            norm_id = _normalize(organ.id)
            norm_name = _normalize(organ.name)
            if q == norm_id or q in norm_name or norm_id in q:
                return organ
        return None

    @classmethod
    def generate_organ_tone(
        cls,
        organ_id: str,
        duration: float = 6.0,
        volume: float = 0.5,
        sample_rate: int = 44100,
        include_harmonics: bool = True
    ) -> List[float]:
        """Belirtilen organın doğal rezonans tonunu yumuşak harmoniklerle sentezler."""
        organ = cls.find_by_id(organ_id)
        if not organ:
            raise ValueError(f"Organ bulunamadı: {organ_id}")

        gen = ToneGenerator(sample_rate=sample_rate)
        harmonics = [(2, 0.20), (3, 0.08)] if include_harmonics else []
        adsr = ADSR(attack=0.8, decay=0.2, sustain_level=0.85, release=1.2)

        return gen.generate_sine(
            frequency=organ.frequency,
            duration=duration,
            volume=volume,
            adsr=adsr,
            harmonics=harmonics
        )

    @classmethod
    def generate_full_body_scan(
        cls,
        duration_per_organ: float = 3.0,
        volume: float = 0.45,
        sample_rate: int = 44100
    ) -> List[float]:
        """Tüm organ sistemlerini baştan ayağa tarayan bütüncül biyo-akustik tarama seansı."""
        organs = cls.get_all()
        all_samples: List[float] = []
        gen = ToneGenerator(sample_rate=sample_rate)
        adsr = ADSR(attack=0.4, decay=0.1, sustain_level=0.85, release=0.5)

        for org in organs:
            samples = gen.generate_sine(
                frequency=org.frequency,
                duration=duration_per_organ,
                volume=volume,
                adsr=adsr,
                harmonics=[(2, 0.15)]
            )
            all_samples.extend(samples)

        return all_samples
