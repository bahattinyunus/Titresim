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


def bessel_j(m: int, x: float, max_terms: int = 15) -> float:
    """Saf Python 1. tür Bessel fonksiyonu J_m(x) seri açılımı."""
    if x < 0:
        return ((-1) ** m) * bessel_j(m, -x, max_terms)
    val = 0.0
    half_x = x / 2.0
    for k in range(max_terms):
        denom = math.factorial(k) * math.factorial(m + k)
        term = (((-1) ** k) / denom) * (half_x ** (2 * k + m))
        val += term
    return val


class CircularChladniPlate:
    """
    Dairesel Chladni plakası / Tibet çanağı / Su yüzeyi dalga simülatörü.
    w(r, theta) = J_m(k * r) * cos(m * theta)
    n: Radyal eşmerkezli düğüm çemberi sayısı
    m: Açısal (çap) nodal çizgi sayısı
    """

    def __init__(self, n: int = 2, m: int = 3):
        self.n = max(1, n)
        self.m = max(0, m)
        # k_nm yaklaşık kök ölçeği
        self.k = math.pi * (self.n + (self.m / 2.0) - 0.25)

    @classmethod
    def from_frequency(cls, freq: float) -> "CircularChladniPlate":
        """Frekansa göre dairesel modları belirler."""
        if freq < 150:
            return cls(n=1, m=2)
        elif freq < 300:
            return cls(n=2, m=2)
        elif freq < 500:
            return cls(n=2, m=4)
        elif freq < 750:
            return cls(n=3, m=4)
        elif freq < 1000:
            return cls(n=3, m=6)
        else:
            return cls(n=4, m=8)

    def evaluate_polar(self, r: float, theta: float, R: float = 0.5) -> float:
        """Kutupsal koordinatta genliği hesaplar. r in [0, R]"""
        if r > R:
            return 0.0
        norm_r = r / R
        x_arg = self.k * norm_r
        radial = bessel_j(self.m, x_arg)
        angular = math.cos(self.m * theta)
        return radial * angular

    def compute_grid(self, resolution: int = 41) -> List[List[float]]:
        """Kare alan içerisindeki dairesel ızgarada genlikleri hesaplar."""
        grid = []
        step = 1.0 / (resolution - 1)
        for i in range(resolution):
            row = []
            y = -0.5 + i * step
            for j in range(resolution):
                x = -0.5 + j * step
                r = math.sqrt(x * x + y * y)
                if r <= 0.5:
                    theta = math.atan2(y, x)
                    row.append(self.evaluate_polar(r, theta, 0.5))
                else:
                    row.append(999.0)  # Çember dışı
            grid.append(row)
        return grid

    def render_ascii(self, resolution: int = 35, threshold: float = 0.14) -> str:
        """Terminal için dairesel Chladni mandala deseni."""
        grid = self.compute_grid(resolution)
        lines = []
        border = "+" + "-" * resolution + "+"
        lines.append(border)

        for row in grid:
            chars = []
            for val in row:
                if val == 999.0:
                    chars.append(" ")
                elif abs(val) < threshold:
                    chars.append("#")
                elif abs(val) < threshold * 2:
                    chars.append("·")
                else:
                    chars.append(" ")
            lines.append("|" + "".join(chars) + "|")

        lines.append(border)
        return "\n".join(lines)

    def export_svg(self, filepath: str, size: int = 500, resolution: int = 80, threshold: float = 0.12) -> None:
        """Dairesel sematik desenini SVG vektör dosyası olarak kaydeder."""
        grid = self.compute_grid(resolution)
        step = size / resolution

        svg_parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}">',
            f'  <rect width="{size}" height="{size}" fill="#0b0f19" />',
            f'  <circle cx="{size/2}" cy="{size/2}" r="{size*0.48}" stroke="#334155" stroke-width="2" fill="none" />',
            f'  <g fill="#38bdf8" opacity="0.9">',
        ]

        for i, row in enumerate(grid):
            y = i * step
            for j, val in enumerate(row):
                x = j * step
                if val != 999.0 and abs(val) < threshold:
                    r = step * 0.4
                    svg_parts.append(f'    <circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" />')
                elif val != 999.0 and abs(val) < threshold * 2:
                    r = step * 0.2
                    svg_parts.append(f'    <circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" opacity="0.3" fill="#f59e0b" />')

        svg_parts.append("  </g>")
        svg_parts.append(f'  <text x="20" y="30" fill="#94a3b8" font-family="monospace" font-size="14">Circular Chladni: n={self.n}, m={self.m}</text>')
        svg_parts.append("</svg>")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(svg_parts))

