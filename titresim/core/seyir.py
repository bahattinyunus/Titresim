"""
Geleneksel Makam Seyir ve Meditatif Taksim Sentezleyici (Makam Improviser).
Farabi ve Osmanlı darüşşifalarının şifa makamları için (Rast, Nihavend, Hicaz, Uşşak)
geleneksel melodik seyir (Giriş -> Zemin -> Meyan -> Karar) dizilimi üretir.
Saf Python ile ney benzeri yumuşak üfleme, vibrato ve karar uzatmaları içerir.
"""

from typing import List, Tuple, Dict
import math
from .generator import ToneGenerator, ADSR
from .makam import MakamTherapy, Makam


class MakamSeyirGenerator:
    """Makam seyri ve meditatif taksim ezgisi üreteci."""

    # Makamların geleneksel seyir nota indeksleri (0 = Karar / Temel ton)
    # [ (nota_indeksi, sure_katsayisi, nefes_vurgusu) ]
    SEYIR_TEMPLATES: Dict[str, List[Tuple[int, float, float]]] = {
        "rast": [
            # Rast Seyri: Çıkıcı-inici (Rast -> Dügah -> Segah -> Çargah -> Neva -> Gerdaniye -> Karar)
            (0, 1.2, 0.45), (1, 0.8, 0.40), (2, 1.0, 0.45), (3, 0.9, 0.42),
            (4, 1.4, 0.50), # Neva asma karar
            (5, 0.8, 0.40), (6, 0.9, 0.45), (7, 1.5, 0.50), # Gerdaniye tizi
            (6, 0.8, 0.40), (5, 0.8, 0.38), (4, 1.1, 0.42),
            (3, 0.9, 0.40), (2, 1.0, 0.42), (1, 1.2, 0.45),
            (0, 2.8, 0.50)  # Rast karar perdesi (uzun sönüm)
        ],
        "nihavend": [
            # Nihavend Seyri: İnici-çıkıcı, hüzünlü ve asil (Neva'dan başlar, Çargah/Kürdi gezinir, Rast'a iner)
            (4, 1.3, 0.48), (3, 0.9, 0.40), (2, 1.0, 0.42), (1, 0.9, 0.38),
            (0, 1.4, 0.45), # Rast taban
            (2, 0.8, 0.38), (4, 1.1, 0.45), (5, 0.9, 0.42), (7, 1.6, 0.50), # Meyan
            (6, 0.9, 0.40), (5, 0.8, 0.38), (4, 1.2, 0.42),
            (3, 0.9, 0.38), (2, 1.0, 0.40), (1, 1.1, 0.42),
            (0, 3.0, 0.50)  # Karar
        ],
        "hicaz": [
            # Hicaz Seyri: Karakteristik Artık 2'li aralığı (Dügah -> Hicaz -> Neva -> Hüseyni -> Eviç -> Gerdaniye)
            (0, 1.2, 0.45), (1, 1.4, 0.48), (2, 1.0, 0.40), (3, 1.2, 0.45), # Hicaz dörtlüsü
            (4, 1.5, 0.50), # Neva asma karar
            (5, 0.9, 0.42), (6, 0.8, 0.40), (7, 1.6, 0.50), # Meyan doruk
            (5, 0.9, 0.40), (4, 1.1, 0.42), (3, 0.9, 0.40),
            (2, 1.2, 0.45), (1, 1.4, 0.48),
            (0, 3.2, 0.50)  # Dügah karar
        ],
        "ussak": [
            # Uşşak Seyri: Segah perdesi esnekliği ile kalbi titreten hüzünlü ve aşıkane seyir
            (0, 1.0, 0.40), (1, 1.4, 0.48), (2, 0.9, 0.42), (3, 1.1, 0.45),
            (4, 1.5, 0.50),
            (3, 0.8, 0.40), (2, 1.0, 0.42), (1, 1.3, 0.45),
            (0, 3.0, 0.50)
        ]
    }

    def __init__(self, sample_rate: int = 44100):
        self.sample_rate = sample_rate

    def generate_seyir_melody(
        self,
        makam_id: str,
        base_freq: float = 220.0,
        unit_note_duration: float = 0.8,
        vibrato_depth_cents: float = 12.0,
        vibrato_rate_hz: float = 4.5
    ) -> List[float]:
        """
        Belirtilen makamın geleneksel seyir dizisini ney tınısı ve yumuşak vibrato ile sentezler.
        """
        makam = MakamTherapy.find_by_id(makam_id)
        if not makam:
            makam = MakamTherapy.get_all()[0]

        makam_key = makam.id.lower()
        template = self.SEYIR_TEMPLATES.get(makam_key, self.SEYIR_TEMPLATES["rast"])
        scale_freqs = makam.get_frequencies(base_freq=base_freq)

        all_samples: List[float] = []
        two_pi = 2.0 * math.pi

        for note_idx, dur_mult, note_vol in template:
            # Dizi dışına taşmayı sınırla
            safe_idx = min(note_idx, len(scale_freqs) - 1)
            target_freq = scale_freqs[safe_idx]
            duration = unit_note_duration * dur_mult

            total_samples = int(self.sample_rate * duration)
            adsr = ADSR(attack=0.15, decay=0.1, sustain_level=0.8, release=0.25)

            for i in range(total_samples):
                t = i / self.sample_rate
                env = adsr.get_amplitude(t, duration)

                # Hafif ney vibratosu (özellikle notanın ikinci yarısında başlar)
                vib_factor = 0.0
                if t > (duration * 0.3):
                    vib_factor = math.sin(two_pi * vibrato_rate_hz * t) * (vibrato_depth_cents / 1200.0)

                inst_freq = target_freq * (2.0 ** vib_factor)
                step = two_pi * inst_freq / self.sample_rate

                # Temel sinüs + Yumuşak 2. ve 3. harmonik (Ney nefes sıcaklığı)
                sample = math.sin(step * i)
                sample += 0.22 * math.sin(step * 2.0 * i)
                sample += 0.08 * math.sin(step * 3.0 * i)

                all_samples.append(sample * note_vol * env)

        return all_samples
