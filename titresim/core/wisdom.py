"""
Kadim Bilgelik, Alıntılar ve Ses Felsefesi Arşivi (Wisdom & Quotes Engine).
Tesla, Mevlânâ, İbn-i Sina, Farabi, Pisagor, Einstein, Kepler, Chladni ve kadim bilgelerin
ses, frekans, kozmik armoni ve şifa üzerine özlü sözleri ve felsefi tahlilleri.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Dict, Any
import json
import random

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


@dataclass
class WisdomQuote:
    id: str
    author: str
    era: str
    work: str
    quote_tr: str
    original_or_context: str
    category: str
    recommended_freq: float
    reflection: str


def _normalize_text(text: str) -> str:
    """Türkçe ve şapkalı karakterleri (â, î, û vb.) basit harflere dönüştürür ve tireleri temizler."""
    replacements = {
        'â': 'a', 'î': 'i', 'û': 'u', 'Â': 'a', 'Î': 'i', 'Û': 'u',
        'ı': 'i', 'İ': 'i', 'ğ': 'g', 'Ğ': 'g', 'ü': 'u', 'Ü': 'u',
        'ş': 's', 'Ş': 's', 'ö': 'o', 'Ö': 'o', 'ç': 'c', 'Ç': 'c',
        '-': ' ',
    }
    res = text
    for k, v in replacements.items():
        res = res.replace(k, v)
    # Birden fazla boşluğu teke indir
    import re
    res = re.sub(r'\s+', ' ', res)
    return res.lower().strip()


class WisdomArchive:
    """Tarihsel ve bilimsel alıntılar kütüphanesi."""

    CATEGORIES = {
        "tasavvuf": "Tasavvuf ve İrfan Geleneği",
        "islam_tibbi": "Osmanlı ve İslam Müzikterapisi & Tıbbı",
        "antik_felsefe": "Antik Felsefe ve Pisagoryen Gelenek",
        "bilim_ve_fizik": "Modern Fizik, Rezonans ve Akustik",
        "mistik_akustik": "Mistik Akustik ve Biyo-rezonans",
        "kutsal_metin": "Kutsal Metinler, Vahiy ve İlahi Kelam"
    }

    @classmethod
    def get_all(cls) -> List[WisdomQuote]:
        json_path = DATA_DIR / "quotes.json"
        if json_path.exists():
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [
                    WisdomQuote(
                        id=item["id"],
                        author=item["author"],
                        era=item["era"],
                        work=item["work"],
                        quote_tr=item["quote_tr"],
                        original_or_context=item.get("original_or_context", ""),
                        category=item.get("category", "genel"),
                        recommended_freq=float(item.get("recommended_freq", 432.0)),
                        reflection=item.get("reflection", ""),
                    )
                    for item in data
                ]
        return []

    @classmethod
    def find_by_id(cls, quote_id: str) -> Optional[WisdomQuote]:
        qid = quote_id.strip().lower()
        for q in cls.get_all():
            if q.id.lower() == qid:
                return q
        return None

    @classmethod
    def get_by_category(cls, category: str) -> List[WisdomQuote]:
        cat = category.strip().lower()
        return [q for q in cls.get_all() if q.category.lower() == cat]

    @classmethod
    def get_by_author(cls, author_query: str) -> List[WisdomQuote]:
        aq = _normalize_text(author_query.strip())
        tokens = [t for t in aq.split() if len(t) > 1]
        results = []
        for q in cls.get_all():
            norm_author = _normalize_text(q.author)
            if aq in norm_author or (tokens and all(token in norm_author for token in tokens)):
                results.append(q)
        return results

    @classmethod
    def search(cls, query: str) -> List[WisdomQuote]:
        q = _normalize_text(query.strip())
        results = []
        for item in cls.get_all():
            corpus = _normalize_text(f"{item.author} {item.work} {item.quote_tr} {item.original_or_context} {item.reflection} {item.category}")
            if q in corpus:
                results.append(item)
        return results

    @classmethod
    def get_random(cls, category: Optional[str] = None) -> Optional[WisdomQuote]:
        quotes = cls.get_by_category(category) if category else cls.get_all()
        if not quotes:
            return None
        return random.choice(quotes)

    @classmethod
    def format_quote_card(cls, q: WisdomQuote) -> str:
        """Terminal için estetik alıntı kartı üretir."""
        cat_name = cls.CATEGORIES.get(q.category, q.category.upper())
        divider = "─" * 68
        lines = [
            f"┌{divider}┐",
            f"│  📜 BİLGELİK & SES REZONANSI ALINTISI: {cat_name[:32]:<32} │",
            f"├{divider}┤",
            f"│  « {q.author} » ({q.era})",
            f"│  Eser/Kaynak: {q.work}",
            f"├{divider}┤",
        ]

        # Alıntıyı satırlara böl
        words = q.quote_tr.split()
        curr_line = "│  “"
        for w in words:
            if len(curr_line) + len(w) + 1 > 64:
                lines.append(f"{curr_line:<68} │")
                curr_line = "│   " + w
            else:
                curr_line += (" " if curr_line != "│  “" else "") + w
        curr_line += "”"
        lines.append(f"{curr_line:<68} │")

        if q.reflection:
            lines.append(f"├{divider}┤")
            r_words = ("Tefekkür: " + q.reflection).split()
            r_line = "│  💡 "
            for rw in r_words:
                if len(r_line) + len(rw) + 1 > 64:
                    lines.append(f"{r_line:<68} │")
                    r_line = "│     " + rw
                else:
                    r_line += (" " if r_line != "│  💡 " else "") + rw
            lines.append(f"{r_line:<68} │")

        lines.append(f"├{divider}┤")
        lines.append(f"│  🎵 Uyumlu Şifa Frekansı: {q.recommended_freq} Hz{'':<37} │")
        lines.append(f"└{divider}┘")
        return "\n".join(lines)
