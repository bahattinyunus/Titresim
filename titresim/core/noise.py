"""
Akustik Gürültü Sentezleyici Modülü (Noise Generator).
Beyaz (White), Pembe (Pink - 1/f) ve Kahverengi/Kırmızı (Brownian/Red - 1/f^2) gürültü üretir.
Tinnitus (kulak çınlaması) terapisi, derin uyku, odaklanma ve meditatif ses maskeleme için kullanılır.
"""

from typing import List
import math
import random


class NoiseGenerator:
    """Saf Python ile deterministik veya rassal akustik gürültü üreteci."""

    def __init__(self, sample_rate: int = 44100, seed: int = 42):
        self.sample_rate = sample_rate
        self.rng = random.Random(seed)

    def generate_white_noise(self, duration: float, volume: float = 0.5) -> List[float]:
        """Tüm frekanslarda eşit enerjiye sahip düz beyaz gürültü üretir."""
        total_samples = int(self.sample_rate * duration)
        samples = []
        for _ in range(total_samples):
            # Uniform dağılımdan [-1.0, 1.0] aralığında örnekleme
            val = (self.rng.random() * 2.0 - 1.0) * volume
            samples.append(val)
        return samples

    def generate_pink_noise(self, duration: float, volume: float = 0.5) -> List[float]:
        """
        Pembe Gürültü (1/f spektrumu - Pembe/Pink Noise).
        Oktav başına eşit enerji taşır; insan kulağına en doğal, huzur verici gelen gürültüdür.
        Paul Kellet'in optimize edilmiş çoklu kutup filtreleme algoritması kullanılır.
        """
        total_samples = int(self.sample_rate * duration)
        samples = []

        b0, b1, b2, b3, b4, b5, b6 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

        for _ in range(total_samples):
            white = self.rng.random() * 2.0 - 1.0

            b0 = 0.99886 * b0 + white * 0.0555179
            b1 = 0.99332 * b1 + white * 0.0750759
            b2 = 0.96900 * b2 + white * 0.1538520
            b3 = 0.86650 * b3 + white * 0.3104856
            b4 = 0.55000 * b4 + white * 0.5329522
            b5 = -0.7616 * b5 - white * 0.0168980

            pink = b0 + b1 + b2 + b3 + b4 + b5 + b6 + white * 0.5362
            b6 = white * 0.115926

            # Ölçeklendirme (~0.11 ile çarpılarak [-1.0, 1.0] dengelenir)
            val = pink * 0.11 * volume
            clamped = max(-1.0, min(1.0, val))
            samples.append(clamped)

        return samples

    def generate_brown_noise(self, duration: float, volume: float = 0.5) -> List[float]:
        """
        Kahverengi / Kırmızı Gürültü (Brownian / Red Noise - 1/f^2).
        Derin şelale, gök gürültüsü veya okyanus dalgaları gibi alt bas frekansların yoğun olduğu,
        derin uyku ve hiperaktiviteyi (DEHB) sakinleştirici akustik spektrum.
        Entegre edilmiş rassal yürüyüş (Leaky Random Walk) kullanır.
        """
        total_samples = int(self.sample_rate * duration)
        samples = []
        last_val = 0.0

        for _ in range(total_samples):
            white = self.rng.random() * 2.0 - 1.0
            # Sızıntılı integratör (DC kaymasını önler)
            last_val = (last_val * 0.98) + (white * 0.1)
            # Normalizasyon
            val = last_val * 0.5 * volume
            clamped = max(-1.0, min(1.0, val))
            samples.append(clamped)

        return samples
