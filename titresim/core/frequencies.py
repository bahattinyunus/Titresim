"""
Frekans hesaplama, Solfeggio cetveli, Beyin dalgaları ve Kozmik Oktav modülü.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Dict, Any
import json

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


@dataclass
class SolfeggioTone:
    frequency: float
    name: str
    note: str
    chakra: str
    description: str
    intention: str


@dataclass
class BrainwaveBand:
    band: str
    range_hz: tuple[float, float]
    center_hz: float
    state: str
    carrier_recommendation: float
    effects: str


@dataclass
class CosmicTone:
    name: str
    frequency: float
    source: str
    description: str


class Solfeggio:
    """Solfeggio frekansları yönetimi ve sorgulama sınıfı."""

    DEFAULT_TONES = [
        SolfeggioTone(174, "Temel / Doğal Anestezi", "F", "Kök (Alt)", "Ağrı dindirme ve güvenlik.", "Ağrı kesici"),
        SolfeggioTone(285, "Hücresel Yenilenme", "C#", "Kök", "Doku ve hücre onarımı.", "Rejenerasyon"),
        SolfeggioTone(396, "Ut - Korkudan Özgürleşme", "G", "Kök", "Korku ve suçluluktan arınma.", "Kurtuluş"),
        SolfeggioTone(417, "Re - Travma Çözümü", "G#", "Sakral", "Geçmiş travmaları temizleme ve değişim.", "Dönüşüm"),
        SolfeggioTone(528, "Mi - Aşk Frekansı & DNA", "C", "Solar Pleksus", "DNA onarımı, sevgi ve mucizeler.", "DNA onarımı"),
        SolfeggioTone(639, "Fa - Bağ Kurma", "D#", "Kalp", "İlişkiler, şefkat ve empati.", "Kalp uyumu"),
        SolfeggioTone(741, "Sol - Sezgi & Arınma", "F#", "Boğaz", "Detoks, toksin temizliği ve sezgi.", "Arınma"),
        SolfeggioTone(852, "La - Ruhsal Düzen", "G#", "Üçüncü Göz", "Manevi uyanış ve içgörü.", "İçgörü"),
        SolfeggioTone(963, "Si - İlahi Birlik", "B", "Taç", "Birlik bilinci ve epifiz bezi uyarımı.", "Aydınlanma"),
    ]

    @classmethod
    def get_all(cls) -> List[SolfeggioTone]:
        json_path = DATA_DIR / "solfeggio.json"
        if json_path.exists():
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [
                    SolfeggioTone(
                        frequency=item["frequency"],
                        name=item["name"],
                        note=item["note"],
                        chakra=item["chakra"],
                        description=item["description"],
                        intention=item["intention"],
                    )
                    for item in data
                ]
        return cls.DEFAULT_TONES

    @classmethod
    def find_by_frequency(cls, freq: float, tolerance: float = 2.0) -> Optional[SolfeggioTone]:
        for tone in cls.get_all():
            if abs(tone.frequency - freq) <= tolerance:
                return tone
        return None


class Brainwaves:
    """Beyin dalgaları (Delta, Teta, Alfa, Beta, Gama) yönetimi."""

    @classmethod
    def get_all(cls) -> List[BrainwaveBand]:
        json_path = DATA_DIR / "brainwaves.json"
        if json_path.exists():
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [
                    BrainwaveBand(
                        band=item["band"],
                        range_hz=tuple(item["range_hz"]),
                        center_hz=item["center_hz"],
                        state=item["state"],
                        carrier_recommendation=item["carrier_recommendation"],
                        effects=item["effects"],
                    )
                    for item in data
                ]
        return [
            BrainwaveBand("Delta", (0.5, 4.0), 2.5, "Derin uyku", 100, "Bedensel onarım"),
            BrainwaveBand("Theta (Teta)", (4.0, 8.0), 6.0, "Derin meditasyon", 150, "Yaratıcılık"),
            BrainwaveBand("Alpha (Alfa)", (8.0, 13.0), 10.0, "Sakin uyanıklık", 200, "Dingin odaklanma"),
            BrainwaveBand("Beta", (13.0, 30.0), 18.0, "Aktif zihin", 250, "Problem çözme"),
            BrainwaveBand("Gamma (Gama)", (30.0, 50.0), 40.0, "Aşkın kavrayış", 300, "Zihinsel senkronizasyon"),
        ]

    @classmethod
    def classify(cls, freq: float) -> Optional[str]:
        for b in cls.get_all():
            if b.range_hz[0] <= freq <= b.range_hz[1]:
                return b.band
        return None


class CosmicOctave:
    """Hans Cousto Kozmik Oktav ve Schumann Rezonansı tonları."""

    SCHUMANN_FUNDAMENTAL = 7.83

    @classmethod
    def get_all(cls) -> List[CosmicTone]:
        json_path = DATA_DIR / "cosmic_octave.json"
        if json_path.exists():
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [
                    CosmicTone(
                        name=item["name"],
                        frequency=item["frequency"],
                        source=item["source"],
                        description=item["description"],
                    )
                    for item in data
                ]
        return [
            CosmicTone("Schumann Rezonansı", 7.83, "İyonosfer rezonansı", "Dünyanın kalp atışı"),
            CosmicTone("Dünya Yılı (Om)", 136.1, "Yıllık döngü 32. oktav", "Meditatif kalp uyumu"),
            CosmicTone("Verdi Akordu", 432.0, "Doğal akustik standart", "Organik Pisagor akordu"),
        ]
