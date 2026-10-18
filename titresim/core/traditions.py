"""
Kutsal Ses Gelenekleri ve Nörobiyolojik Rezonans Modülü.
Kur'an-ı Kerim kıraati ve tecvid ilmi, Vedik mantralar, Gregoryen ilahileri,
Tibet ses çanakları ve Şamanik davul trans ritimlerinin akustik modelleri.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Dict, Any
import json

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


@dataclass
class SacredTradition:
    id: str
    tradition: str
    practice: str
    fundamental_frequencies: List[str]
    acoustic_principles: List[str]
    neurobiological_effects: List[str]
    historical_sources: str


class SacredTraditions:
    """Kutsal kelâm ve kadim ses gelenekleri bilgi motoru."""

    @classmethod
    def get_all(cls) -> List[SacredTradition]:
        json_path = DATA_DIR / "traditions.json"
        if json_path.exists():
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [
                    SacredTradition(
                        id=item["id"],
                        tradition=item["tradition"],
                        practice=item["practice"],
                        fundamental_frequencies=item["fundamental_frequencies"],
                        acoustic_principles=item["acoustic_principles"],
                        neurobiological_effects=item["neurobiological_effects"],
                        historical_sources=item["historical_sources"],
                    )
                    for item in data
                ]
        return []

    @classmethod
    def find_by_id(cls, tradition_id: str) -> Optional[SacredTradition]:
        tradition_id = tradition_id.strip().lower()
        for t in cls.get_all():
            if t.id.lower() == tradition_id or tradition_id in t.tradition.lower():
                return t
        return None

    @classmethod
    def search(cls, query: str) -> List[SacredTradition]:
        q = query.strip().lower()
        results = []
        for t in cls.get_all():
            text_corpus = f"{t.tradition} {t.practice} {' '.join(t.acoustic_principles)} {' '.join(t.neurobiological_effects)} {t.historical_sources}".lower()
            if q in text_corpus:
                results.append(t)
        return results
