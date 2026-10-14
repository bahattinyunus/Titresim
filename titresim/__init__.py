"""
Titresim: Evrensel Ses, Kutsal Kelâm ve Frekans Terapisi Kütüphanesi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kadim şifa gelenekleri, Osmanlı darüşşifa müzikterapisi, kutsal metin kıraat rezonansı,
Solfeggio frekansları, Chladni sematik (cymatics) hesaplamaları ve binaural ses sentezleme motoru.
"""

__version__ = "1.0.0"
__author__ = "Bahattin Yunus Çetin"
__license__ = "MIT"

from .core.frequencies import Solfeggio, Brainwaves, CosmicOctave
from .core.makam import MakamTherapy, Makam
from .core.cymatics import ChladniPlate, CymaticsPattern
from .core.generator import ToneGenerator, ADSR
from .core.binaural import BinauralBeatGenerator

__all__ = [
    "Solfeggio",
    "Brainwaves",
    "CosmicOctave",
    "MakamTherapy",
    "Makam",
    "ChladniPlate",
    "CymaticsPattern",
    "ToneGenerator",
    "ADSR",
    "BinauralBeatGenerator",
]
