"""
Titresim: Evrensel Ses, Kutsal Kelâm ve Frekans Terapisi Kütüphanesi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kadim şifa gelenekleri, Osmanlı darüşşifa müzikterapisi, kutsal metin kıraat rezonansı,
Solfeggio frekansları, Hans Cousto Gezegen Tonları, Chladni sematik (kare & dairesel),
izokronik tonlar (isochronic), akustik gürültü terapisi (pembe, kahverengi, beyaz),
53-TET mikrotonal koma akort sistemi ve iki kanallı binaural ses sentezleme motoru.
"""

__version__ = "1.3.0"
__author__ = "Bahattin Yunus Çetin"
__license__ = "MIT"

from .core.frequencies import (
    Solfeggio,
    SolfeggioTone,
    Brainwaves,
    BrainwaveBand,
    CosmicOctave,
    CosmicTone,
    PlanetaryFrequencies,
    PlanetaryTone,
    fibonacci_tuning,
)
from .core.makam import MakamTherapy, Makam
from .core.cymatics import ChladniPlate, CircularChladniPlate, CymaticsPattern
from .core.generator import ToneGenerator, ADSR
from .core.binaural import BinauralBeatGenerator
from .core.noise import NoiseGenerator
from .core.isochronic import IsochronicToneGenerator
from .core.traditions import SacredTraditions, SacredTradition
from .core.tuning import TuningSystem, MicrotonalInterval
from .core.wisdom import WisdomArchive, WisdomQuote

__all__ = [
    "Solfeggio",
    "SolfeggioTone",
    "Brainwaves",
    "BrainwaveBand",
    "CosmicOctave",
    "CosmicTone",
    "PlanetaryFrequencies",
    "PlanetaryTone",
    "fibonacci_tuning",
    "MakamTherapy",
    "Makam",
    "ChladniPlate",
    "CircularChladniPlate",
    "CymaticsPattern",
    "ToneGenerator",
    "ADSR",
    "BinauralBeatGenerator",
    "NoiseGenerator",
    "IsochronicToneGenerator",
    "SacredTraditions",
    "SacredTradition",
    "TuningSystem",
    "MicrotonalInterval",
    "WisdomArchive",
    "WisdomQuote",
]
