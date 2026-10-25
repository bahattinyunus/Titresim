"""
titresim/core/water.py
Suyun Hafızası, Dördüncü Faz (EZ Suyu - Exclusion Zone H3O2),
QED Koherans Alanları ve Sematik Hekzagonal Kristalizasyon Akustik Motoru.
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional, Union
import math
import random
import json
from pathlib import Path


@dataclass
class WaterFrequency:
    id: str
    name: str
    frequency_hz: float
    effect_category: str
    coherence_rating: float
    molecular_effect: str
    faraday_wave_symmetry: str
    biological_benefit: str


@dataclass
class WaterMemoryTheory:
    name: str
    pioneer: str
    formula: str
    description: str


@dataclass
class EmotoCrystal:
    id: str
    name: str
    frequency_equivalent: float
    crystal_structure: str
    coherence_score: float
    scientific_note: str


class WaterAcoustics:
    """Suyun hafızası, hekzagonal kümelenme ve akustik kavitasyon motoru."""

    _DATA_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "water.json"
    _DATA: Optional[Dict[str, Any]] = None

    @classmethod
    def _load_data(cls) -> Dict[str, Any]:
        if cls._DATA is None:
            if cls._DATA_PATH.exists():
                with open(cls._DATA_PATH, "r", encoding="utf-8") as f:
                    cls._DATA = json.load(f)
            else:
                cls._DATA = {"acoustic_water_frequencies": [], "emoto_crystal_gallery": [], "water_memory_science": {}}
        return cls._DATA

    @classmethod
    def list_frequencies(cls) -> List[WaterFrequency]:
        data = cls._load_data()
        freqs = []
        for item in data.get("acoustic_water_frequencies", []):
            freqs.append(WaterFrequency(
                id=item["id"],
                name=item["name"],
                frequency_hz=float(item["frequency_hz"]),
                effect_category=item.get("effect_category", ""),
                coherence_rating=float(item.get("coherence_rating", 0.9)),
                molecular_effect=item.get("molecular_effect", ""),
                faraday_wave_symmetry=item.get("faraday_wave_symmetry", ""),
                biological_benefit=item.get("biological_benefit", "")
            ))
        return freqs

    @classmethod
    def get_frequency(cls, freq_id: str) -> Optional[WaterFrequency]:
        norm = freq_id.lower().replace("-", "").replace("_", "")
        for wf in cls.list_frequencies():
            wf_norm = wf.id.lower().replace("-", "").replace("_", "")
            if wf_norm == norm or norm in wf_norm:
                return wf
        return None

    @classmethod
    def list_theories(cls) -> List[WaterMemoryTheory]:
        data = cls._load_data()
        theories = []
        for th in data.get("water_memory_science", {}).get("theories", []):
            theories.append(WaterMemoryTheory(
                name=th["name"],
                pioneer=th["pioneer"],
                formula=th["formula"],
                description=th["description"]
            ))
        return theories

    @classmethod
    def list_crystals(cls) -> List[EmotoCrystal]:
        data = cls._load_data()
        crystals = []
        for cr in data.get("emoto_crystal_gallery", []):
            crystals.append(EmotoCrystal(
                id=cr["id"],
                name=cr["name"],
                frequency_equivalent=float(cr.get("frequency_equivalent", 0.0)),
                crystal_structure=cr.get("crystal_structure", ""),
                coherence_score=float(cr.get("coherence_score", 0.5)),
                scientific_note=cr.get("scientific_note", "")
            ))
        return crystals

    @staticmethod
    def calculate_coherence_index(freq_hz: float) -> float:
        """
        Herhangi bir frekansın su molekülleri üzerinde ürettiği teorik koherans endeksini hesaplar (0.0 - 1.0).
        Altın Oran harmonikleri, 528 Hz (DNA/su), 432 Hz ve Schumann 7.83 Hz için maksimum verir.
        """
        if freq_hz <= 0:
            return 0.0

        key_resonances = [7.83, 136.1, 432.0, 528.0, 741.0, 963.0]
        max_proximity = 0.0

        for kr in key_resonances:
            ratio = freq_hz / kr
            octave_fold = ratio
            while octave_fold >= 2.0:
                octave_fold /= 2.0
            while octave_fold < 1.0 and octave_fold > 0.0:
                octave_fold *= 2.0

            # 1.0 (unison) veya 1.5 (saf beşli) veya 1.618 (phi) yakınlığı
            diff_unison = abs(octave_fold - 1.0)
            diff_fifth = abs(octave_fold - 1.5)
            diff_phi = abs(octave_fold - 1.618)
            min_diff = min(diff_unison, diff_fifth, diff_phi)

            prox = math.exp(-min_diff * 4.0)
            if prox > max_proximity:
                max_proximity = prox

        base_index = 0.5 + 0.48 * max_proximity
        return round(min(1.0, max(0.1, base_index)), 3)

    @classmethod
    def synthesize_water_structuring_tone(
        cls,
        target: Union[str, float] = "dna_hexagonal_528",
        duration: float = 10.0,
        add_vortex_cavitation: bool = True,
        sample_rate: int = 44100
    ) -> List[float]:
        """
        Hekzagonal su yapılandırma tonu sentezi.
        Belirlenen frekansı, mikroskopik su vorteksi ve hidro-akustik kavitasyon
        baloncukları (subtle bubble cavitation flutter) hissiyle zenginleştirir.
        """
        if isinstance(target, (int, float)):
            freq = float(target)
            title = f"{freq:.1f} Hz"
        else:
            wf = cls.get_frequency(str(target))
            freq = wf.frequency_hz if wf else 528.0
            title = wf.name if wf else "528 Hz"

        num_samples = int(sample_rate * duration)
        samples = [0.0] * num_samples

        # Sıvı dalga modülasyonu hızı (0.12 Hz çok yavaş nefes alış)
        vortex_speed = 0.12

        for i in range(num_samples):
            t = i / sample_rate

            # Zarf (fade in/out)
            fade = 1.0
            if t < 1.2:
                fade = 0.5 * (1.0 - math.cos(math.pi * (t / 1.2)))
            elif t > duration - 1.2:
                fade = 0.5 * (1.0 + math.cos(math.pi * ((t - (duration - 1.2)) / 1.2)))

            # Ana saf ton
            main_tone = math.sin(2.0 * math.pi * freq * t)

            # Bir oktav alt sıvı gövdesi (sub-liquid bass)
            sub_liquid = math.sin(math.pi * freq * t) * 0.25

            # Su yüzeyi akışkan dalgalanma (liquid surface swell)
            swell = 0.88 + 0.12 * math.sin(2.0 * math.pi * vortex_speed * t)

            val = (main_tone * 0.75 + sub_liquid) * swell

            # Akustik mikro-kavitasyon (su kabarcığı pıtırtısı / micro-cavitation effervescence)
            if add_vortex_cavitation and random.random() < 0.03:
                bubble_pop = (random.random() * 2.0 - 1.0) * 0.08
                val += bubble_pop

            samples[i] = val * fade * 0.85

        max_val = max(abs(s) for s in samples) or 1.0
        return [s / max_val * 0.85 for s in samples]
