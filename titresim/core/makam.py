"""
Osmanlı Darüşşifaları Makam Terapisi Modülü.
Farabi, İbn-i Sina, Evliya Çelebi ve Şuuri Hasan Efendi'nin tıp risalelerine dayalı makam ve şifa sistemi.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Dict, Any
import json

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


@dataclass
class Makam:
    id: str
    name: str
    root_tone: str
    time: str
    element: str
    zodiac: str
    organ: str
    therapeutic_effects: List[str]
    scholar_notes: str
    scale_ratios: List[float]

    def get_frequencies(self, base_freq: float = 220.0) -> List[float]:
        """Verilen temel frekansa (Dügah/Rast temel tonuna) göre makamın dizi frekanslarını hesaplar."""
        return [round(base_freq * ratio, 2) for ratio in self.scale_ratios]


class MakamTherapy:
    """Makam terapisi arşivi ve arama motoru."""

    @classmethod
    def get_all(cls) -> List[Makam]:
        json_path = DATA_DIR / "makamlar.json"
        if json_path.exists():
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [
                    Makam(
                        id=item["id"],
                        name=item["name"],
                        root_tone=item["root_tone"],
                        time=item["time"],
                        element=item["element"],
                        zodiac=item["zodiac"],
                        organ=item["organ"],
                        therapeutic_effects=item["therapeutic_effects"],
                        scholar_notes=item["scholar_notes"],
                        scale_ratios=item["scale_ratios"],
                    )
                    for item in data
                ]
        return []

    @classmethod
    def find_by_id(cls, makam_id: str) -> Optional[Makam]:
        makam_id = makam_id.strip().lower()
        for m in cls.get_all():
            if m.id.lower() == makam_id or m.name.lower().startswith(makam_id):
                return m
        return None

    @classmethod
    def search_by_organ(cls, organ_name: str) -> List[Makam]:
        organ_name = organ_name.lower()
        results = []
        for m in cls.get_all():
            if organ_name in m.organ.lower():
                results.append(m)
        return results

    @classmethod
    def search_by_time(cls, time_query: str) -> List[Makam]:
        time_query = time_query.lower()
        results = []
        for m in cls.get_all():
            if time_query in m.time.lower():
                results.append(m)
        return results
