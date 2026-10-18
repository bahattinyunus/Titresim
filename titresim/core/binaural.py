"""
Stereo Binaural Beat & Beyin Dalgası Sentezleyici Modülü.
Sol ve sağ kulaklık kanallarına farklı frekanslar göndererek beyinde aradaki fark kadar
ritmik dalga (Delta, Teta, Alfa, Gama) algısı oluşturur.
Pembe gürültü (Pink Noise) zemin desteği ve frekans takibi yeteneklerine sahiptir.
"""

from typing import List, Tuple, Optional
import math
import struct
import wave
from .generator import ADSR
from .noise import NoiseGenerator


class BinauralBeatGenerator:
    """Stereo 2-kanal binaural dalga ve nöroakustik üreteç."""

    def __init__(self, sample_rate: int = 44100):
        self.sample_rate = sample_rate

    def generate(
        self,
        carrier_freq: float = 200.0,
        beat_freq: float = 7.83,
        duration: float = 10.0,
        volume: float = 0.5,
        pink_noise_level: float = 0.05,
    ) -> Tuple[List[float], List[float]]:
        """
        Sol ve sağ kanal için örnek dizileri döndürür.
        carrier_freq: Taşıyıcı ton (örn. 200 Hz)
        beat_freq: Hedef beyin dalgası (örn. 7.83 Hz Schumann)
        Sol: carrier - beat/2
        Sağ: carrier + beat/2
        pink_noise_level: Arkaya yumuşakça harmanlanan pembe gürültü genlik katsayısı
        """
        left_freq = carrier_freq - (beat_freq / 2.0)
        right_freq = carrier_freq + (beat_freq / 2.0)

        total_samples = int(self.sample_rate * duration)
        left_samples = []
        right_samples = []

        two_pi = 2.0 * math.pi
        left_step = two_pi * left_freq / self.sample_rate
        right_step = two_pi * right_freq / self.sample_rate

        # Yumuşak giriş ve çıkış
        adsr = ADSR(attack=1.0, decay=0.0, sustain_level=1.0, release=1.5)

        # Pembe gürültü üretimi
        pink_samples: Optional[List[float]] = None
        if pink_noise_level > 0.001:
            noise_gen = NoiseGenerator(sample_rate=self.sample_rate)
            pink_samples = noise_gen.generate_pink_noise(duration=duration, volume=pink_noise_level)

        for i in range(total_samples):
            t = i / self.sample_rate
            env = adsr.get_amplitude(t, duration)

            s_left = math.sin(left_step * i) * volume * env
            s_right = math.sin(right_step * i) * volume * env

            if pink_samples and i < len(pink_samples):
                p_noise = pink_samples[i] * env
                s_left += p_noise
                s_right += p_noise

            left_samples.append(s_left)
            right_samples.append(s_right)

        return left_samples, right_samples

    def save_stereo_wav(
        self,
        filepath: str,
        left_samples: List[float],
        right_samples: List[float],
    ) -> None:
        """İki kanallı stereo 16-bit PCM WAV olarak kaydeder."""
        if len(left_samples) != len(right_samples):
            raise ValueError("Sol ve sağ kanal örnek sayıları eşit olmalıdır.")

        with wave.open(filepath, "w") as wav_file:
            n_channels = 2
            sampwidth = 2  # 16-bit
            framerate = self.sample_rate
            n_frames = len(left_samples)

            wav_file.setparams((n_channels, sampwidth, framerate, n_frames, "NONE", "not compressed"))

            packed_frames = bytearray()
            for l, r in zip(left_samples, right_samples):
                clamped_l = max(-1.0, min(1.0, l))
                clamped_r = max(-1.0, min(1.0, r))

                int_l = int(clamped_l * 32767.0)
                int_r = int(clamped_r * 32767.0)

                packed_frames.extend(struct.pack("<hh", int_l, int_r))

            wav_file.writeframes(packed_frames)
