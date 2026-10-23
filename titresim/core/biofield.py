"""
titresim/core/biofield.py
Biyoalan, Fiziksel Diyapazon (Tuning Fork) Akustiği,
Nikola Tesla 3-6-9 Vorteks Matematiği ve Fibonacci Altın Oran Harmonikleri.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import math
import random
import json
from pathlib import Path


@dataclass
class TuningFork:
    id: str
    name: str
    frequency: float
    category: str
    damping_factor: float
    target_tissue: str
    biofield_layer: str
    clinical_effects: str
    strike_harmonics: List[float] = field(default_factory=list)


@dataclass
class TeslaTriad:
    root: int
    name: str
    frequencies: List[float]
    digital_roots: List[int]
    effects: str


class BiofieldAcoustics:
    """Diyapazon fiziksel modelleme, Tesla 3-6-9 vorteks ve Fibonacci harmonik motoru."""

    _DATA_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "biofield.json"
    _DATA: Optional[Dict[str, Any]] = None

    @classmethod
    def _load_data(cls) -> Dict[str, Any]:
        if cls._DATA is None:
            if cls._DATA_PATH.exists():
                with open(cls._DATA_PATH, "r", encoding="utf-8") as f:
                    cls._DATA = json.load(f)
            else:
                cls._DATA = {"tuning_forks": [], "tesla_369_vortex": {"triads": []}, "fibonacci_series": {"phi": 1.61803398875}}
        return cls._DATA

    @classmethod
    def list_forks(cls) -> List[TuningFork]:
        data = cls._load_data()
        forks = []
        for item in data.get("tuning_forks", []):
            forks.append(TuningFork(
                id=item["id"],
                name=item["name"],
                frequency=float(item["frequency"]),
                category=item["category"],
                damping_factor=float(item.get("damping_factor", 0.4)),
                target_tissue=item.get("target_tissue", ""),
                biofield_layer=item.get("biofield_layer", ""),
                clinical_effects=item.get("clinical_effects", ""),
                strike_harmonics=[float(h) for h in item.get("strike_harmonics", [])]
            ))
        return forks

    @classmethod
    def get_fork(cls, fork_id: str) -> Optional[TuningFork]:
        fork_id_norm = fork_id.lower().replace("-", "").replace("_", "")
        for f in cls.list_forks():
            if f.id.lower() == fork_id_norm or fork_id_norm in f.id.lower():
                return f
        return None

    @classmethod
    def strike_fork(
        cls,
        fork_id: str,
        duration: float = 8.0,
        sample_rate: int = 44100,
        strike_intensity: float = 0.8
    ) -> List[float]:
        """
        Fiziksel diyapazon vuruş (strike) simülasyonu.
        Vuruş anındaki metalik yüksek harmoniklerin (inharmonic clack) hızla sönümlenmesi
        ve temel frekansın saf sinüs olarak $e^{-t/\\tau}$ zarfıyla uzun süre tınlaması.
        """
        fork = cls.get_fork(fork_id)
        if not fork:
            freq = 128.0
            damping = 0.35
            harmonics = [353.3, 691.2]
        else:
            freq = fork.frequency
            damping = fork.damping_factor
            harmonics = fork.strike_harmonics

        num_samples = int(sample_rate * duration)
        samples = [0.0] * num_samples

        # Temel frekansın sönümlenme zaman sabiti (tau)
        # Düşük frekanslar daha uzun tınlar, yüksekler daha hızlı söner
        tau_fund = (12.0 / (damping + 0.1)) * (100.0 / (freq + 50.0)) ** 0.3
        tau_fund = max(2.5, min(15.0, tau_fund))

        # Geçici vuruş (strike transient) zaman sabiti ~ 0.05 - 0.09 saniye
        tau_transient = 0.06

        for i in range(num_samples):
            t = i / sample_rate

            # 1. Temel Saf Frekans (Ana Tınlama)
            env_fund = math.exp(-t / tau_fund)
            # Mikro yumuşak açılış (0-2 ms)
            if t < 0.002:
                env_fund *= (t / 0.002)

            val = math.sin(2.0 * math.pi * freq * t) * env_fund

            # 2. Vuruş Anı Harmonikleri (Inharmonic strike overtones)
            env_trans = math.exp(-t / tau_transient) * strike_intensity * 0.35
            for h_idx, h_freq in enumerate(harmonics):
                h_weight = 0.5 / (h_idx + 1)
                val += math.sin(2.0 * math.pi * h_freq * t) * env_trans * h_weight

            # 3. Tokmak Vuruşu Mikrosaniyelik Akustik Şok (İlk 5 milisaniye)
            if t < 0.005:
                noise = (random.random() * 2.0 - 1.0) * strike_intensity * 0.25 * (1.0 - t / 0.005)
                val += noise

            samples[i] = val

        # Normalizasyon
        max_val = max(abs(s) for s in samples) or 1.0
        return [s / max_val * 0.85 for s in samples]

    @staticmethod
    def digital_root(n: int) -> int:
        """Nikola Tesla dijital kök indirgemesi (1..9)."""
        if n <= 0:
            return 0
        return 1 + ((int(round(n)) - 1) % 9)

    @classmethod
    def get_tesla_triad(cls, root: int) -> Optional[TeslaTriad]:
        data = cls._load_data()
        triads = data.get("tesla_369_vortex", {}).get("triads", [])
        for tr in triads:
            if tr["root"] == root:
                return TeslaTriad(
                    root=tr["root"],
                    name=tr["name"],
                    frequencies=[float(f) for f in tr["frequencies"]],
                    digital_roots=tr["digital_roots"],
                    effects=tr["effects"]
                )
        return None

    @classmethod
    def list_tesla_triads(cls) -> List[TeslaTriad]:
        data = cls._load_data()
        triads = []
        for tr in data.get("tesla_369_vortex", {}).get("triads", []):
            triads.append(TeslaTriad(
                root=tr["root"],
                name=tr["name"],
                frequencies=[float(f) for f in tr["frequencies"]],
                digital_roots=tr["digital_roots"],
                effects=tr["effects"]
            ))
        return triads

    @classmethod
    def synthesize_tesla_vortex(
        cls,
        triad_root: int = 9,
        duration: float = 10.0,
        sample_rate: int = 44100,
        vortex_speed_hz: float = 0.2
    ) -> List[float]:
        """
        Nikola Tesla 3-6-9 Vorteks Holografik Ses Alanı.
        Triadın 3 frekansı 120 derecelik faz farkı (2*pi/3) ve döngüsel vorteks
        genlik modülasyonu ile birleşir, 3 boyutlu dinamik akustik girdap oluşturur.
        """
        triad = cls.get_tesla_triad(triad_root)
        if not triad:
            triad = cls.get_tesla_triad(9)
        frequencies = triad.frequencies if triad else [396.0, 639.0, 963.0]

        num_samples = int(sample_rate * duration)
        samples = [0.0] * num_samples

        phase_offsets = [0.0, 2.0 * math.pi / 3.0, 4.0 * math.pi / 3.0]

        for i in range(num_samples):
            t = i / sample_rate
            # Zarflama (fade-in / fade-out)
            fade = 1.0
            if t < 1.0:
                fade = 0.5 * (1.0 - math.cos(math.pi * t))
            elif t > duration - 1.0:
                fade = 0.5 * (1.0 + math.cos(math.pi * (t - (duration - 1.0))))

            val = 0.0
            for k in range(3):
                freq = frequencies[k]
                p_offset = phase_offsets[k]
                # Vorteks dönme genliği (Her frekans sırayla yükselip alçalır)
                vortex_amp = 0.5 + 0.5 * math.sin(2.0 * math.pi * vortex_speed_hz * t + p_offset)
                val += math.sin(2.0 * math.pi * freq * t + p_offset) * vortex_amp

            samples[i] = (val / 3.0) * fade * 0.85

        return samples

    @classmethod
    def generate_fibonacci_sequence(
        cls,
        base_freq: float = 432.0,
        octaves: int = 5,
        duration: float = 8.0,
        sample_rate: int = 44100
    ) -> List[float]:
        """
        Fibonacci ve Altın Oran (Phi = 1.6180339887) fraktal frekans akordu.
        $f_n = f_0 \\cdot \\Phi^{(n - k) / 2}$ altın oran spirali oluşturur.
        """
        phi = 1.618033988749895
        num_samples = int(sample_rate * duration)
        samples = [0.0] * num_samples

        freqs = [base_freq * (phi ** (n - 2)) for n in range(octaves)]

        for i in range(num_samples):
            t = i / sample_rate
            fade = 1.0
            if t < 0.8:
                fade = t / 0.8
            elif t > duration - 0.8:
                fade = (duration - t) / 0.8

            val = 0.0
            for idx, f in enumerate(freqs):
                weight = 1.0 / (idx + 1.2)
                val += math.sin(2.0 * math.pi * f * t) * weight

            samples[i] = val * fade * 0.4

        max_val = max(abs(s) for s in samples) or 1.0
        return [s / max_val * 0.8 for s in samples]
