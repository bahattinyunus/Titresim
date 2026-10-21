"""
Terapötik Ses Seansı ve Protokol Motoru (Therapy Protocols Engine).
Çok aşamalı klinik ve meditatif ses protokolleri (Uyku, Odaklanma, Osmanlı Darüşşifası, Kalp Koheransı)
üretir, aşamalar arası yumuşak geçişler (cross-fade) ile stereo seans WAV dosyaları sentezler.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple, Optional, Dict, Any
import json
import math
from .binaural import BinauralBeatGenerator
from .generator import ToneGenerator, ADSR
from .noise import NoiseGenerator

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


@dataclass
class TherapyStage:
    stage: int
    name: str
    duration_percent: float
    carrier_freq: float
    beat_freq: float
    band: str
    noise_type: str
    noise_volume: float
    description: str


@dataclass
class TherapyProtocol:
    id: str
    title: str
    subtitle: str
    target: str
    total_recommended_minutes: int
    stages: List[TherapyStage]


class TherapySessionEngine:
    """Terapötik seans yönetimi ve sentez motoru."""

    def __init__(self, sample_rate: int = 44100):
        self.sample_rate = sample_rate
        self.binaural_gen = BinauralBeatGenerator(sample_rate=sample_rate)
        self.noise_gen = NoiseGenerator(sample_rate=sample_rate)

    @classmethod
    def get_all_protocols(cls) -> List[TherapyProtocol]:
        json_path = DATA_DIR / "protocols.json"
        if not json_path.exists():
            return []
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            protocols = []
            for p in data:
                stages = [
                    TherapyStage(
                        stage=s["stage"],
                        name=s["name"],
                        duration_percent=float(s["duration_percent"]),
                        carrier_freq=float(s["carrier_freq"]),
                        beat_freq=float(s["beat_freq"]),
                        band=s["band"],
                        noise_type=s["noise_type"],
                        noise_volume=float(s["noise_volume"]),
                        description=s["description"]
                    )
                    for s in p["stages"]
                ]
                protocols.append(TherapyProtocol(
                    id=p["id"],
                    title=p["title"],
                    subtitle=p["subtitle"],
                    target=p["target"],
                    total_recommended_minutes=int(p["total_recommended_minutes"]),
                    stages=stages
                ))
            return protocols

    @classmethod
    def find_protocol(cls, protocol_id: str) -> Optional[TherapyProtocol]:
        pid = protocol_id.strip().lower()
        for p in cls.get_all_protocols():
            if p.id.lower() == pid or pid in p.id.lower() or pid in p.title.lower():
                return p
        return None

    def synthesize_protocol_session(
        self,
        protocol: TherapyProtocol,
        total_duration_seconds: float = 60.0,
        volume: float = 0.5
    ) -> Tuple[List[float], List[float]]:
        """
        Protokolün tüm aşamalarını birleştirip kesintisiz stereo seans dalgası üretir.
        Döndürür: (left_channel_samples, right_channel_samples)
        """
        all_left: List[float] = []
        all_right: List[float] = []

        fade_time = 1.5  # Aşamalar arası yumuşak geçiş saniyesi

        for stage in protocol.stages:
            stage_duration = (stage.duration_percent / 100.0) * total_duration_seconds
            if stage_duration <= 0.1:
                continue

            # Binaural ton üret
            l_samples, r_samples = self.binaural_gen.generate(
                carrier_freq=stage.carrier_freq,
                beat_freq=stage.beat_freq,
                duration=stage_duration,
                volume=volume,
                pink_noise_level=0.0  # Gürültüyü ayrı sentezleyeceğiz
            )

            # Aşama gürültüsü üret
            if stage.noise_volume > 0.001:
                if stage.noise_type == "brown":
                    noise_samples = self.noise_gen.generate_brown_noise(stage_duration, stage.noise_volume)
                elif stage.noise_type == "white":
                    noise_samples = self.noise_gen.generate_white_noise(stage_duration, stage.noise_volume)
                else:
                    noise_samples = self.noise_gen.generate_pink_noise(stage_duration, stage.noise_volume)

                for i in range(len(l_samples)):
                    if i < len(noise_samples):
                        l_samples[i] += noise_samples[i]
                        r_samples[i] += noise_samples[i]

            all_left.extend(l_samples)
            all_right.extend(r_samples)

        return all_left, all_right

    def export_session_wav(
        self,
        filepath: str,
        protocol_id: str,
        duration_seconds: float = 60.0,
        volume: float = 0.5
    ) -> TherapyProtocol:
        """Belirtilen protokolü sentezler ve WAV olarak kaydeder."""
        prot = self.find_protocol(protocol_id)
        if not prot:
            raise ValueError(f"Protokol bulunamadı: {protocol_id}")

        left, right = self.synthesize_protocol_session(prot, duration_seconds, volume)
        self.binaural_gen.save_stereo_wav(filepath, left, right)
        return prot
