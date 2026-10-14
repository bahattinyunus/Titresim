"""
Sematik (Cymatics) & Chladni Plaka Rezonans Modeli.
Ses dalgalarının maddede (kum, su, toz) meydana getirdiği geometrik mandalaların matematiksel simülasyonu.
"""

from dataclasses import dataclass
from typing import List, Tuple
import math


@dataclass
class CymaticsPattern:
    frequency: float
    n_mode: int
    m_mode: int
    geometry_name: str
    symbolism: str


class ChladniPlate:
    """
    Kare Chladni plakası üzerinde modal titreşim simülatörü.
    w(x, y) = a * cos(n * pi * x / L) * cos(m * pi * y / L) - b * cos(m * pi * x / L) * cos(n * pi * y / L)
    Titreşimsiz (düğüm / nodal) çizgiler w(x, y) ≈ 0 olan yerlerde kum taneleri toplanır.
    """

    def __init__(self, n: int = 3, m: int = 5, a: float = 1.0, b: float = 1.0):
        self.n = n
        self.m = m
        self.a = a
        self.b = b

    @classmethod
    def from_frequency(cls, freq: float) -> "ChladniPlate":
        """Frekans değerine göre uygun modal harmonikleri türetir."""
        # Frekans yükseldikçe modal sayılar ve karmaşıklık artar
        if freq < 100:
            return cls(n=1, m=2)
        elif freq < 200:
            return cls(n=2, m=3)
        elif freq < 350:
            return cls(n=3, m=4)
        elif freq < 500:
            return cls(n=3, m=5)
        elif freq < 650:
            return cls(n=4, m=6)
        elif freq < 800:
            return cls(n=5, m=7)
        else:
            return cls(n=6, m=8)

    def evaluate_point(self, x: float, y: float, L: float = 1.0) -> float:
        """[-L/2, L/2] aralığındaki (x, y) noktasında genliği hesaplar."""
        term1 = math.cos(self.n * math.pi * x / L) * math.cos(self.m * math.pi * y / L)
        term2 = math.cos(self.m * math.pi * x / L) * math.cos(self.n * math.pi * y / L)
        return self.a * term1 - self.b * term2

    def compute_grid(self, resolution: int = 41) -> List[List[float]]:
        """NxN matris üzerinde genlik değerlerini hesaplar."""
        grid = []
        step = 1.0 / (resolution - 1)
        for i in range(resolution):
            row = []
            y = -0.5 + i * step
            for j in range(resolution):
                x = -0.5 + j * step
                row.append(self.evaluate_point(x, y))
            grid.append(row)
        return grid

    def render_ascii(self, resolution: int = 35, threshold: float = 0.18) -> str:
        """Terminal için nodal çizgileri gösteren ASCII mandala deseni üretir."""
        grid = self.compute_grid(resolution)
        lines = []
        border = "+" + "-" * resolution + "+"
        lines.append(border)

        for row in grid:
            chars = []
            for val in row:
                if abs(val) < threshold:
                    chars.append("#")  # Kum tanesi / nodal çizgi
                elif abs(val) < threshold * 2:
                    chars.append("·")
                else:
                    chars.append(" ")
            lines.append("|" + "".join(chars) + "|")

        lines.append(border)
        return "\n".join(lines)

    def export_svg(self, filepath: str, size: int = 500, resolution: int = 80, threshold: float = 0.15) -> None:
        """Deseni saf vektörel SVG olarak kaydeder (Harici kütüphane gerektirmez)."""
        grid = self.compute_grid(resolution)
        step = size / resolution

        svg_parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}">',
            f'  <rect width="{size}" height="{size}" fill="#0b0f19" />',
            f'  <g fill="#f59e0b" opacity="0.85">',
        ]

        for i, row in enumerate(grid):
            y = i * step
            for j, val in enumerate(row):
                x = j * step
                if abs(val) < threshold:
                    r = step * 0.4
                    svg_parts.append(f'    <circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" />')
                elif abs(val) < threshold * 2:
                    r = step * 0.2
                    svg_parts.append(f'    <circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" opacity="0.4" fill="#38bdf8" />')

        svg_parts.append("  </g>")
        svg_parts.append(f'  <text x="20" y="30" fill="#94a3b8" font-family="monospace" font-size="14">Chladni Modes: n={self.n}, m={self.m}</text>')
        svg_parts.append("</svg>")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(svg_parts))
