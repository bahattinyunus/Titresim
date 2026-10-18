"""
İzokronik Ton (Isochronic Pulse) Sentezleyici Modülü.
Kulaklık gerektirmeden hoparlör üzerinden doğrudan beyin dalgası senkronizasyonu (FFR) sağlayan
düzenli aralıklarla açılıp kapanan (pulsed) ritmik akustik vuru üreteci.
"""

from typing import List, Tuple
import math
from .generator import ADSR


class IsochronicToneGenerator:
    """İzokronik nabız ve beyin dalgası frekans modülatörü."""

    def __init__(self, sample_rate: int = 44100):
        self.sample_rate = sample_rate

    def generate(
        self,
        carrier_freq: float = 432.0,
        pulse_rate_hz: float = 10.0,
        duration: float = 10.0,
        volume: float = 0.5,
        duty_cycle: float = 0.5,
        smoothness: float = 0.3,
    ) -> List[float]:
        """
        İzokronik dalga dizisi üretir.
        carrier_freq: Taşıyıcı ton (örn: 432 Hz veya 528 Hz)
        pulse_rate_hz: Vuruş / beyin dalgası frekansı (örn: 10 Hz Alfa, 7.83 Hz Schumann, 40 Hz Gama)
        duty_cycle: Her periyotta sesin açık kalma oranı (0.1 - 0.9, varsayılan 0.5)
        smoothness: Tıklama sesini (click/pop) önleyen kenar yumuşatma katsayısı (Raised Cosine)
        """
        total_samples = int(self.sample_rate * duration)
        samples = []

        two_pi = 2.0 * math.pi
        carrier_step = two_pi * carrier_freq / self.sample_rate
        pulse_period_samples = self.sample_rate / pulse_rate_hz if pulse_rate_hz > 0 else self.sample_rate

        adsr = ADSR(attack=0.5, decay=0.0, sustain_level=1.0, release=0.8)

        for i in range(total_samples):
            t = i / self.sample_rate
            global_env = adsr.get_amplitude(t, duration)

            # Periyot içi konum [0.0, 1.0)
            phase = (i % pulse_period_samples) / pulse_period_samples

            # Raised cosine veya yumuşak nabız modülasyonu
            if phase < duty_cycle:
                # Açık faz
                norm_phase = phase / duty_cycle
                # Sinüzoidal yumuşak pencere
                pulse_amp = math.sin(math.pi * norm_phase) ** smoothness
            else:
                pulse_amp = 0.0

            # Taşıyıcı dalga
            carrier_sample = math.sin(carrier_step * i)

            sample = carrier_sample * pulse_amp * volume * global_env
            samples.append(sample)

        return samples
