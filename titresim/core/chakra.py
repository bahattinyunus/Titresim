"""
Çakra ve Meridyen Akustik Rezonans Modülü (Chakra Resonance Engine).
7 Temel Çakra ve Meridyen sisteminin Solfeggio, Gezegen (Cousto),
Bija Tohum Mantraları ve Renk Spektrumu Akustik Eşleşmeleri.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple
import json
from .generator import ToneGenerator, ADSR

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


@dataclass
class ChakraAcoustics:
    id: str
    name: str
    location: str
    element: str
    solfeggio_freq: float
    planetary_freq: float
    bija_mantra: str
    color: str
    note: str
    organs: str
    balance_effect: str
    imbalance_symptoms: str


class ChakraResonance:
    """Çakra akustiği ve rezonant frekans yönetim sınıfı."""

    @classmethod
    def get_all(cls) -> List[ChakraAcoustics]:
        json_path = DATA_DIR / "chakras.json"
        if not json_path.exists():
            return []
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [
                ChakraAcoustics(
                    id=item["id"],
                    name=item["name"],
                    location=item["location"],
                    element=item["element"],
                    solfeggio_freq=float(item["solfeggio_freq"]),
                    planetary_freq=float(item["planetary_freq"]),
                    bija_mantra=item["bija_mantra"],
                    color=item["color"],
                    note=item["note"],
                    organs=item["organs"],
                    balance_effect=item["balance_effect"],
                    imbalance_symptoms=item["imbalance_symptoms"]
                )
                for item in data
            ]

    @classmethod
    def _normalize(cls, text: str) -> str:
        t = text.lower().strip()
        replacements = [
            ("ı", "i"), ("ğ", "g"), ("ü", "u"), ("ş", "s"), ("ö", "o"), ("ç", "c"),
            ("â", "a"), ("î", "i"), ("û", "u")
        ]
        for src, dest in replacements:
            t = t.replace(src, dest)
        return t

    @classmethod
    def find_by_id(cls, chakra_id: str) -> Optional[ChakraAcoustics]:
        query = cls._normalize(chakra_id)
        for ch in cls.get_all():
            norm_id = cls._normalize(ch.id)
            norm_name = cls._normalize(ch.name)
            if query == norm_id or query in norm_name or norm_id in query:
                return ch
        return None

    @classmethod
    def generate_chakra_tone(
        cls,
        chakra_id: str,
        mode: str = "solfeggio",
        duration: float = 8.0,
        volume: float = 0.5,
        sample_rate: int = 44100
    ) -> List[float]:
        """
        Belirtilen çakra için yumuşak harmonikli rezonant ton üretir.
        mode: 'solfeggio' veya 'planetary'
        """
        ch = cls.find_by_id(chakra_id)
        if not ch:
            raise ValueError(f"Çakra bulunamadı: {chakra_id}")

        freq = ch.solfeggio_freq if mode == "solfeggio" else ch.planetary_freq
        gen = ToneGenerator(sample_rate=sample_rate)

        # Çakranın tohum sesini yansıtan harmonikler (2. ve 3. oktav hafif tınılar)
        harmonics = [(2, 0.20), (3, 0.08)]
        adsr = ADSR(attack=1.0, decay=0.2, sustain_level=0.8, release=1.5)

        return gen.generate_sine(
            frequency=freq,
            duration=duration,
            volume=volume,
            adsr=adsr,
            harmonics=harmonics
        )

    @classmethod
    def generate_rainbow_alignment(
        cls,
        duration_per_chakra: float = 4.0,
        volume: float = 0.5,
        sample_rate: int = 44100
    ) -> List[float]:
        """
        Kök çakradan Taç çakraya (1'den 7'ye) yükselen tam çakra dengeleme dizisi sentezler.
        """
        chakras = cls.get_all()
        all_samples = []
        gen = ToneGenerator(sample_rate=sample_rate)
        adsr = ADSR(attack=0.6, decay=0.1, sustain_level=0.85, release=0.8)

        for ch in chakras:
            samples = gen.generate_sine(
                frequency=ch.solfeggio_freq,
                duration=duration_per_chakra,
                volume=volume,
                adsr=adsr,
                harmonics=[(2, 0.15)]
            )
            all_samples.extend(samples)

        return all_samples
