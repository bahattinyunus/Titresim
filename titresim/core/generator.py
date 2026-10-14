"""
Akustik Ton Sentezleyici & WAV Üretim Modülü.
Saf Python (math, wave, struct) ile harici bağımlılık gerektirmeden 16-bit PCM WAV dosyaları üretir.
"""

from dataclasses import dataclass
from typing import List, Tuple, Callable
import math
import struct
import wave


@dataclass
class ADSR:
    """Zarf (Envelope) parametreleri saniye cinsinden."""
    attack: float = 0.05
    decay: float = 0.05
    sustain_level: float = 0.8
    release: float = 0.1

    def get_amplitude(self, t: float, total_duration: float) -> float:
        """Verilen t anındaki genlik katsayısını [0.0, 1.0] döndürür."""
        if t < 0:
            return 0.0
        if t < self.attack:
            return t / self.attack if self.attack > 0 else 1.0
        elif t < (self.attack + self.decay):
            dt = t - self.attack
            ratio = dt / self.decay if self.decay > 0 else 1.0
            return 1.0 - (1.0 - self.sustain_level) * ratio
        elif t < (total_duration - self.release):
            return self.sustain_level
        elif t < total_duration:
            dt = t - (total_duration - self.release)
            ratio = dt / self.release if self.release > 0 else 1.0
            val = self.sustain_level * (1.0 - ratio)
            return max(0.0, val) if val > 1e-9 else 0.0
        return 0.0


class ToneGenerator:
    """Tekli ve çoklu frekanslar için PCM ses üreteci."""

    def __init__(self, sample_rate: int = 44100):
        self.sample_rate = sample_rate

    def generate_sine(
        self,
        frequency: float,
        duration: float,
        volume: float = 0.5,
        adsr: ADSR = None,
        harmonics: List[Tuple[int, float]] = None,
    ) -> List[float]:
        """
        Saf sinüs dalgası veya harmonik katmanlı dalga dizisi üretir.
        harmonics: [(harmonik_katı, nispi_genlik), ...] Örn: [(2, 0.3), (3, 0.15)]
        """
        if adsr is None:
            adsr = ADSR(attack=0.1, decay=0.1, sustain_level=0.8, release=0.2)

        total_samples = int(self.sample_rate * duration)
        samples = []

        two_pi = 2.0 * math.pi
        base_step = two_pi * frequency / self.sample_rate

        for i in range(total_samples):
            t = i / self.sample_rate
            env = adsr.get_amplitude(t, duration)

            # Temel dalga
            sample = math.sin(base_step * i)

            # Harmonikler ekle
            if harmonics:
                for h_mult, h_amp in harmonics:
                    sample += h_amp * math.sin(base_step * h_mult * i)

            # Normalize ve ses seviyesi
            sample = sample * volume * env
            samples.append(sample)

        return samples

    def generate_scale(
        self,
        frequencies: List[float],
        note_duration: float = 0.8,
        volume: float = 0.5,
    ) -> List[float]:
        """Makam dizisi gibi ardışık notalardan oluşan ses serisi üretir."""
        all_samples = []
        adsr = ADSR(attack=0.08, decay=0.08, sustain_level=0.75, release=0.15)
        harmonics = [(2, 0.25), (3, 0.1)]  # Yumuşak ney benzeri zenginlik

        for freq in frequencies:
            note_samples = self.generate_sine(
                frequency=freq,
                duration=note_duration,
                volume=volume,
                adsr=adsr,
                harmonics=harmonics,
            )
            all_samples.extend(note_samples)

        return all_samples

    def save_wav(self, filepath: str, samples: List[float]) -> None:
        """Mono örnekleri 16-bit PCM WAV olarak kaydeder."""
        with wave.open(filepath, "w") as wav_file:
            n_channels = 1
            sampwidth = 2  # 16-bit (2 bytes)
            framerate = self.sample_rate
            n_frames = len(samples)

            wav_file.setparams((n_channels, sampwidth, framerate, n_frames, "NONE", "not compressed"))

            # Sıkıştırılmış ikili veri paketleme
            packed_frames = bytearray()
            for s in samples:
                # Kırpma (Clamping) [-1.0, 1.0]
                clamped = max(-1.0, min(1.0, s))
                int_sample = int(clamped * 32767.0)
                packed_frames.extend(struct.pack("<h", int_sample))

            wav_file.writeframes(packed_frames)
