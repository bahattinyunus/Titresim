"""
Akustik Akort Sistemleri & Mikrotonal Koma Hesaplayıcı Modülü.
Pisagor Doğal Akordu, 432 Hz (Verdi) / 440 Hz (ISO) / 444 Hz Dönüşümleri ve
Geleneksel Türk Sanat/Tasavvuf Müziği Arel-Ezgi-Uzdilek (53-TET / Holderian Koma) Sistemi.
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional
import math


@dataclass
class MicrotonalInterval:
    name: str
    symbol: str
    commas: int
    cents: float
    frequency_ratio: float
    description: str


class TuningSystem:
    """Akort sistemleri ve mikrotonal perde matematiği."""

    # 53 Eşit Bölümlü Tampere (53-TET / Holder Koması)
    # 1 Oktav = 53 Koma. 1 Koma = 1200 / 53 ≈ 22.6415 Cent.
    COMMA_CENTS = 1200.0 / 53.0
    COMMA_RATIO = 2.0 ** (1.0 / 53.0)  # ≈ 1.01316416

    # Arel-Ezgi-Uzdilek Temel Aralıkları
    INTERVALS_53TET = {
        "F": MicrotonalInterval("Fazla", "F", 1, COMMA_CENTS * 1, COMMA_RATIO ** 1, "En küçük mikrotonal koma aralığı"),
        "B": MicrotonalInterval("Bakiye", "B", 4, COMMA_CENTS * 4, COMMA_RATIO ** 4, "Küçük yarım ses (Segah ve Uşşak bemolleri)"),
        "S": MicrotonalInterval("Küçük Mücenneb", "S", 5, COMMA_CENTS * 5, COMMA_RATIO ** 5, "Orta yarım ses"),
        "K": MicrotonalInterval("Büyük Mücenneb", "K", 8, COMMA_CENTS * 8, COMMA_RATIO ** 8, "Büyük yarım ses (Hicaz ve Saba aralıkları)"),
        "T": MicrotonalInterval("Tanini", "T", 9, COMMA_CENTS * 9, COMMA_RATIO ** 9, "Tam ses (Rast, Dügah, Çargah arası)"),
        "A": MicrotonalInterval("Artık Mücenneb", "A", 12, COMMA_CENTS * 12, COMMA_RATIO ** 12, "Genişletilmiş ses (Hicaz 2-3 perde arası)"),
    }

    # Batı Standart Notalarının A4=440 Hz için Yarı-Ton Adımları (Semitones from A4)
    SEMITONE_OFFSETS = {
        "C": -9, "C#": -8, "Db": -8, "D": -7, "D#": -6, "Eb": -6,
        "E": -5, "F": -4, "F#": -3, "Gb": -3, "G": -2, "G#": -1, "Ab": -1,
        "A": 0, "A#": 1, "Bb": 1, "B": 2
    }

    @classmethod
    def convert_a4(cls, freq_at_source: float, source_a4: float = 440.0, target_a4: float = 432.0) -> float:
        """Verilen bir frekansı bir A4 referansından diğerine (örn: 440 Hz -> 432 Hz) dönüştürür."""
        ratio = target_a4 / source_a4
        return round(freq_at_source * ratio, 3)

    @classmethod
    def note_to_frequency(cls, note_name: str, octave: int = 4, a4_ref: float = 432.0) -> float:
        """Nota adını ve oktavını hedef A4 frekansına göre (Hz) hesaplar."""
        note_name = note_name.strip().capitalize()
        if note_name not in cls.SEMITONE_OFFSETS:
            raise ValueError(f"Geçersiz nota: {note_name}")

        semitone = cls.SEMITONE_OFFSETS[note_name]
        octave_shift = (octave - 4) * 12
        total_semitones = semitone + octave_shift

        freq = a4_ref * (2.0 ** (total_semitones / 12.0))
        return round(freq, 2)

    @classmethod
    def pythagorean_scale(cls, tonic_freq: float = 216.0) -> List[Tuple[str, float, float]]:
        """
        Pisagor 3:2 saf beşli zinciri üzerinden 7 temel perdeyi türetir.
        Döndürür: [(Perde Adı, Frekans Hz, Cent Değeri), ...]
        """
        # Saf Pisagor oranları (1, 9/8, 81/64, 4/3, 3/2, 27/16, 243/128, 2)
        ratios = [
            ("1 (Tonic)", 1.0),
            ("2 (Büyük İkili / Tanini)", 9.0 / 8.0),
            ("3 (Pisagor Üçlüsü)", 81.0 / 64.0),
            ("4 (Saf Dörtlü)", 4.0 / 3.0),
            ("5 (Saf Beşli)", 3.0 / 2.0),
            ("6 (Büyük Altılı)", 27.0 / 16.0),
            ("7 (Büyük Yedili)", 243.0 / 128.0),
            ("8 (Oktav)", 2.0),
        ]
        res = []
        for name, r in ratios:
            freq = round(tonic_freq * r, 2)
            cents = round(1200.0 * math.log2(r), 1)
            res.append((name, freq, cents))
        return res

    @classmethod
    def calculate_makam_53tet(cls, base_freq: float, comma_steps: List[int]) -> List[float]:
        """
        Arel-Ezgi 53-TET koma adımlarına göre tam dizi frekanslarını türetir.
        Örnek Rast Makamı (T - K - S - T - T - K - S): [0, 9, 17, 22, 31, 40, 48, 53]
        """
        freqs = []
        for step in comma_steps:
            ratio = cls.COMMA_RATIO ** step
            freqs.append(round(base_freq * ratio, 2))
        return freqs
