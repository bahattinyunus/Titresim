# -*- coding: utf-8 -*-
"""
Generate comprehensive, high-resolution SVG visual assets for Titresim repository.
"""
import math
from pathlib import Path

ASSETS_DIR = Path("assets")
ASSETS_DIR.mkdir(parents=True, exist_ok=True)


def generate_banner_svg():
    """TİTREŞİM v2.0 Ana Banner Görseli."""
    w, h = 1200, 480
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">')
    svg.append('<defs>')
    svg.append('  <radialGradient id="bgGrad" cx="50%" cy="45%" r="70%">')
    svg.append('    <stop offset="0%" stop-color="#0f172a" />')
    svg.append('    <stop offset="50%" stop-color="#090d16" />')
    svg.append('    <stop offset="100%" stop-color="#020408" />')
    svg.append('  </radialGradient>')
    svg.append('  <radialGradient id="goldGlow" cx="50%" cy="50%" r="50%">')
    svg.append('    <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.3" />')
    svg.append('    <stop offset="100%" stop-color="#f59e0b" stop-opacity="0" />')
    svg.append('  </radialGradient>')
    svg.append('  <radialGradient id="cyanGlow" cx="50%" cy="50%" r="50%">')
    svg.append('    <stop offset="0%" stop-color="#06b6d4" stop-opacity="0.35" />')
    svg.append('    <stop offset="100%" stop-color="#06b6d4" stop-opacity="0" />')
    svg.append('  </radialGradient>')
    svg.append('  <linearGradient id="textGold" x1="0%" y1="0%" x2="100%" y2="0%">')
    svg.append('    <stop offset="0%" stop-color="#fbbf24" />')
    svg.append('    <stop offset="50%" stop-color="#fef08a" />')
    svg.append('    <stop offset="100%" stop-color="#f59e0b" />')
    svg.append('  </linearGradient>')
    svg.append('</defs>')

    # Background
    svg.append(f'<rect width="{w}" height="{h}" fill="url(#bgGrad)" />')

    # Ambient glows
    svg.append('<circle cx="600" cy="220" r="280" fill="url(#goldGlow)" />')
    svg.append('<circle cx="300" cy="240" r="220" fill="url(#cyanGlow)" />')
    svg.append('<circle cx="900" cy="240" r="220" fill="url(#cyanGlow)" />')

    # Sine waves across banner
    for wave_i, (color, op, freq_mult, y_off) in enumerate([
        ("#06b6d4", "0.25", 0.015, 230),
        ("#f59e0b", "0.30", 0.022, 240),
        ("#6366f1", "0.20", 0.012, 250),
        ("#38bdf8", "0.35", 0.028, 235),
    ]):
        points = []
        for x in range(0, w + 1, 10):
            y = y_off + math.sin(x * freq_mult + wave_i * 1.2) * (25 + wave_i * 8)
            points.append(f"{x},{y:.1f}")
        svg.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{color}" stroke-opacity="{op}" stroke-width="1.8" />')

    # Central Cymatics Mandala (Geometric rings & petals)
    cx, cy = 600, 220
    for r in [40, 75, 110, 145, 180]:
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#f59e0b" stroke-opacity="0.18" stroke-width="1" stroke-dasharray="4,6" />')

    # Mandala Petals (12-fold symmetry)
    for i in range(12):
        angle = i * (2 * math.pi / 12)
        px1 = cx + math.cos(angle) * 115
        py1 = cy + math.sin(angle) * 115
        px2 = cx + math.cos(angle + math.pi / 12) * 60
        py2 = cy + math.sin(angle + math.pi / 12) * 60
        svg.append(f'<path d="M {cx} {cy} Q {px2} {py2} {px1} {py1}" fill="none" stroke="#38bdf8" stroke-opacity="0.25" stroke-width="1.2" />')

    # Main Typography
    svg.append(f'<text x="{cx}" y="200" text-anchor="middle" font-family="Cinzel, Georgia, serif" font-size="54" font-weight="700" letter-spacing="14" fill="url(#textGold)">TİTREŞİM</text>')
    svg.append(f'<text x="{cx}" y="240" text-anchor="middle" font-family="Plus Jakarta Sans, sans-serif" font-size="14" font-weight="600" letter-spacing="4" fill="#67e8f9">EVRENSEL SES, KUTSAL KELÂM &amp; FREKANS TERAPİSİ LABORATUVARI v2.0</text>')

    # Badges / Frequency tags at bottom
    badges = [
        ("432 Hz", "Doğal Akort & Pi"),
        ("528 Hz", "DNA & Solfeggio"),
        ("7.83 Hz", "Schumann Rezonansı"),
        ("0.10 Hz", "Kalp Koheransı"),
        ("12 Makam", "Darüşşifa Tıbbı"),
        ("7 Çakra", "Kozmik Oktav")
    ]
    badge_y = 390
    spacing = w / (len(badges) + 1)
    for idx, (hz, label) in enumerate(badges):
        bx = int((idx + 1) * spacing)
        svg.append(f'<rect x="{bx-65}" y="{badge_y-18}" width="130" height="42" rx="6" fill="#1e293b" fill-opacity="0.75" stroke="#334155" stroke-width="1" />')
        svg.append(f'<text x="{bx}" y="{badge_y}" text-anchor="middle" font-family="monospace" font-size="13" font-weight="700" fill="#fde68a">{hz}</text>')
        svg.append(f'<text x="{bx}" y="{badge_y+16}" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#94a3b8">{label}</text>')

    # Quote at bottom center
    svg.append(f'<text x="{cx}" y="455" text-anchor="middle" font-family="Georgia, serif" font-size="11" font-style="italic" fill="#cbd5e1">"Evrenin sırrını bulmak istiyorsanız; enerji, frekans ve titreşim cinsinden düşünün." — Nikola Tesla</text>')

    svg.append('</svg>')
    out_path = ASSETS_DIR / "titresim_banner.svg"
    out_path.write_text("\n".join(svg), encoding="utf-8")
    print(f"Created: {out_path}")


def generate_cymatics_patterns_svg():
    """6 Modal Chladni ve Sematik Desenleri İnfografiği."""
    w, h = 1000, 680
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">')
    svg.append('<rect width="100%" height="100%" fill="#0a0f1d" />')

    # Title
    svg.append('<text x="500" y="45" text-anchor="middle" font-family="Cinzel, serif" font-size="24" font-weight="700" fill="#fde68a" letter-spacing="3">SEMATİK (CYMATICS) VE CHLADNI MODAL REZONANS DESENLERİ</text>')
    svg.append('<text x="500" y="70" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#94a3b8">Akustik frekansların nodal çizgilerde maddeye (kum ve su) kazıdığı kutsal geometri</text>')

    # 6 Panels: (n, m, freq, name, chakra)
    patterns = [
        (1, 2, "174 Hz", "Doğal Anestezi", "Temel Mod"),
        (2, 3, "396 Hz", "Kök (Muladhara)", "Korkudan Özgürleşme"),
        (3, 4, "432 Hz", "Evrensel A4 Akordu", "Doğal Pisagor Uyumu"),
        (3, 5, "528 Hz", "Solar Pleksus (Mi)", "Dönüşüm & DNA Onarımı"),
        (4, 5, "639 Hz", "Kalp (Anahata)", "İlişkiler & Bağ Kurma"),
        (5, 7, "852 Hz", "Üçüncü Göz (Ajna)", "Ruhsal Uyanış & Sezgi")
    ]

    card_w, card_h = 280, 260
    cols = 3
    for idx, (n, m, freq, title, sub) in enumerate(patterns):
        row = idx // cols
        col = idx % cols
        bx = 40 + col * 320
        by = 100 + row * 280

        # Card box
        svg.append(f'<rect x="{bx}" y="{by}" width="{card_w}" height="{card_h}" rx="8" fill="#131c2e" stroke="#1e293b" stroke-width="1.5" />')

        # Card header
        svg.append(f'<text x="{bx+15}" y="{by+28}" font-family="monospace" font-size="15" font-weight="700" fill="#38bdf8">{freq}</text>')
        svg.append(f'<text x="{bx+card_w-15}" y="{by+28}" text-anchor="end" font-family="monospace" font-size="11" fill="#94a3b8">n={n}, m={m}</text>')
        svg.append(f'<text x="{bx+15}" y="{by+46}" font-family="sans-serif" font-size="12" font-weight="600" fill="#f8fafc">{title}</text>')

        # Plate area inside card
        plate_cx = bx + card_w / 2
        plate_cy = by + 135
        plate_size = 140
        svg.append(f'<rect x="{plate_cx-plate_size/2}" y="{plate_cy-plate_size/2}" width="{plate_size}" height="{plate_size}" fill="#05080e" rx="4" stroke="#334155" />')

        # Generate Chladni nodal curve approximations
        # w(x,y) = a*sin(n*pi*x/L)*sin(m*pi*y/L) - b*sin(m*pi*x/L)*sin(n*pi*y/L) ~ 0
        grid_res = 35
        step = plate_size / grid_res
        for gi in range(grid_res):
            for gj in range(grid_res):
                nx = (gi / grid_res) - 0.5
                ny = (gj / grid_res) - 0.5
                val = math.cos(n * math.pi * nx) * math.cos(m * math.pi * ny) - math.cos(m * math.pi * nx) * math.cos(n * math.pi * ny)
                if abs(val) < 0.15:
                    px = plate_cx - plate_size / 2 + gi * step
                    py = plate_cy - plate_size / 2 + gj * step
                    svg.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="1.1" fill="#fde68a" fill-opacity="0.8" />')

        # Subtitle
        svg.append(f'<text x="{plate_cx}" y="{by+card_h-14}" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#94a3b8">{sub}</text>')

    svg.append('</svg>')
    out_path = ASSETS_DIR / "cymatics_chladni_patterns.svg"
    out_path.write_text("\n".join(svg), encoding="utf-8")
    print(f"Created: {out_path}")


def generate_chakra_spectrum_svg():
    """7 Çakra Akustiği ve Biyo-Rezonans İnfografiği."""
    w, h = 1050, 560
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">')
    svg.append('<rect width="100%" height="100%" fill="#090d16" />')

    # Title
    svg.append('<text x="525" y="45" text-anchor="middle" font-family="Cinzel, serif" font-size="22" font-weight="700" fill="#fde68a" letter-spacing="3">7 ÇAKRA AKUSTİK VE BİYO-REZONANS SPEKTRUMU</text>')
    svg.append('<text x="525" y="68" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#94a3b8">Kutsal Solfeggio Ölçeği, Hans Cousto Gezegen Tonları ve Bija Tohum Mantraları</text>')

    chakras = [
        ("Kök (Muladhara)", "#ef4444", "396 Hz", "194.18 Hz (Dünya)", "LAM", "C (Do)", "Topraklanma & Güven"),
        ("Sakral (Svadhisthana)", "#f97316", "417 Hz", "210.42 Hz (Ay)", "VAM", "D (Re)", "Akışkanlık & Yaşama Sevinci"),
        ("Solar Pleksus (Manipura)", "#eab308", "528 Hz", "126.22 Hz (Güneş)", "RAM", "E (Mi)", "İrade, Güç & DNA Onarımı"),
        ("Kalp (Anahata)", "#22c55e", "639 Hz", "136.10 Hz (OM / Yıl)", "YAM", "F (Fa)", "Koşulsuz Sevgi & Koherans"),
        ("Boğaz (Vishuddha)", "#06b6d4", "741 Hz", "141.27 Hz (Merkür)", "HAM", "G (Sol)", "Duru İfade & Sezgi"),
        ("Üçüncü Göz (Ajna)", "#6366f1", "852 Hz", "221.23 Hz (Venüs)", "AUM", "A (La)", "Ruhsal Düzen & Basiret"),
        ("Taç (Sahasrara)", "#a855f7", "963 Hz", "172.06 Hz (Platonik)", "OM", "B (Si)", "İlahi Birlik & Kozmik İdrak")
    ]

    card_h = 56
    start_y = 100
    for i, (name, color, solf, planet, bija, note, effect) in enumerate(chakras):
        y = start_y + i * 62
        # Row card
        svg.append(f'<rect x="40" y="{y}" width="970" height="{card_h}" rx="6" fill="#131c2e" stroke="{color}" stroke-opacity="0.35" stroke-width="1.2" />')
        # Color indicator strip
        svg.append(f'<rect x="40" y="{y}" width="8" height="{card_h}" rx="3" fill="{color}" />')

        # Chakra Number & Bija
        svg.append(f'<circle cx="85" cy="{y+card_h/2}" r="18" fill="{color}" fill-opacity="0.2" stroke="{color}" stroke-width="1" />')
        svg.append(f'<text x="85" y="{y+card_h/2+4}" text-anchor="middle" font-family="monospace" font-size="12" font-weight="700" fill="#f8fafc">{i+1}</text>')

        # Bija Mantra Badge
        svg.append(f'<rect x="120" y="{y+14}" width="55" height="28" rx="14" fill="#0b1120" stroke="#334155" />')
        svg.append(f'<text x="147" y="{y+32}" text-anchor="middle" font-family="monospace" font-size="11" font-weight="700" fill="#fde68a">{bija}</text>')

        # Chakra Name
        svg.append(f'<text x="195" y="{y+26}" font-family="sans-serif" font-size="14" font-weight="700" fill="#f8fafc">{name}</text>')
        svg.append(f'<text x="195" y="{y+44}" font-family="sans-serif" font-size="11" fill="#94a3b8">Nota: {note} • Tesir: {effect}</text>')

        # Solfeggio freq
        svg.append(f'<rect x="620" y="{y+14}" width="130" height="28" rx="4" fill="#0f172a" stroke="#1e293b" />')
        svg.append(f'<text x="685" y="{y+32}" text-anchor="middle" font-family="monospace" font-size="12" font-weight="700" fill="{color}">Solf: {solf}</text>')

        # Cousto freq
        svg.append(f'<rect x="765" y="{y+14}" width="230" height="28" rx="4" fill="#0f172a" stroke="#1e293b" />')
        svg.append(f'<text x="880" y="{y+32}" text-anchor="middle" font-family="monospace" font-size="11" font-weight="600" fill="#cbd5e1">Cousto: {planet}</text>')

    svg.append('</svg>')
    out_path = ASSETS_DIR / "chakra_acoustic_spectrum.svg"
    out_path.write_text("\n".join(svg), encoding="utf-8")
    print(f"Created: {out_path}")


def generate_brainwaves_svg():
    """Beyin Dalgaları & Binaural Beat Sürükleme İnfografiği."""
    w, h = 1000, 520
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">')
    svg.append('<rect width="100%" height="100%" fill="#0a0e1a" />')

    svg.append('<text x="500" y="42" text-anchor="middle" font-family="Cinzel, serif" font-size="22" font-weight="700" fill="#67e8f9" letter-spacing="3">EEG BEYİN DALGALARI &amp; BİNAURAL SÜRÜKLEME MEKANİZMASI</text>')
    svg.append('<text x="500" y="65" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#94a3b8">Superior Olivary Complex üzerinde iki kulak arasındaki faz farkının beyin dalgasını senkronize etmesi</text>')

    bands = [
        ("GAMA (30 - 100 Hz)", "#ec4899", 0.08, "Aşkın kavrayış, yüksek odak, Eureka kıvılcımı ve hızlı bilgi sentezi"),
        ("BETA (13 - 30 Hz)", "#f59e0b", 0.05, "Aktif uyanıklık, mantıksal problem çözme, dış dünyaya odaklanma"),
        ("ALFA (8 - 13 Hz)", "#10b981", 0.03, "Dingin farkındalık, rahatlamış uyanıklık, hafif meditasyon & 10 Hz"),
        ("TETA (4 - 8 Hz)", "#06b6d4", 0.018, "Derin meditasyon, REM rüyası, sezgisel yaratıcılık & 7.83 Hz Schumann"),
        ("DELTA (0.5 - 4 Hz)", "#8b5cf6", 0.009, "Rüyasız derin uyku, hücresel doku onarımı, büyüme hormonu (HGH)")
    ]

    for idx, (bname, bcolor, bfreq, bdesc) in enumerate(bands):
        by = 95 + idx * 80
        # Box
        svg.append(f'<rect x="40" y="{by}" width="920" height="70" rx="6" fill="#111827" stroke="#1f2937" />')
        # Left wave animation representation
        points = []
        for x in range(50, 320, 4):
            y = by + 35 + math.sin((x - 50) * bfreq * 12) * 16
            points.append(f"{x},{y:.1f}")
        svg.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{bcolor}" stroke-width="2" />')

        # Title & Info
        svg.append(f'<text x="340" y="{by+28}" font-family="sans-serif" font-size="15" font-weight="700" fill="{bcolor}">{bname}</text>')
        svg.append(f'<text x="340" y="{by+50}" font-family="sans-serif" font-size="12" fill="#94a3b8">{bdesc}</text>')

    svg.append('</svg>')
    out_path = ASSETS_DIR / "brainwave_entrainment_spectrum.svg"
    out_path.write_text("\n".join(svg), encoding="utf-8")
    print(f"Created: {out_path}")


def generate_makam_wheel_svg():
    """Osmanlı Darüşşifası 12 Şifa Makamı Dairesel Çarkı."""
    w, h = 800, 800
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">')
    svg.append('<rect width="100%" height="100%" fill="#0a0d14" />')

    cx, cy = 400, 410
    svg.append('<text x="400" y="45" text-anchor="middle" font-family="Cinzel, serif" font-size="22" font-weight="700" fill="#fde68a" letter-spacing="3">OSMANLI DARÜŞŞİFASI ŞİFA MAKAMLARI ÇARKI</text>')
    svg.append('<text x="400" y="68" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#94a3b8">Fârâbî, İbn Sînâ ve Şuûrî Hasan Efendi Mizaç ve Vakit Eşleşmesi</text>')

    makamlar = [
        ("Rast", "Seher Vakti", "Ateş / Safra", "#ef4444"),
        ("Rehavi", "Fecir Doğuşu", "Su / Balgam", "#06b6d4"),
        ("Küçek", "Kuşluk Öncesi", "Hava / Kan", "#10b981"),
        ("Büzürk", "Kuşluk Vakti", "Ateş / Safra", "#f59e0b"),
        ("Isfahan", "Öğle Vakti", "Toprak / Sevda", "#8b5cf6"),
        ("Neva", "Öğle Sonrası", "Su / Balgam", "#3b82f6"),
        ("Uşşak", "İkindi Vakti", "Ateş / Safra", "#f97316"),
        ("Zirgüle", "İkindi Sonu", "Hava / Kan", "#22c55e"),
        ("Saba", "Gün Batımı", "Hava / Kan", "#eab308"),
        ("Buselik", "Akşam Vakti", "Toprak / Sevda", "#a855f7"),
        ("Hüseyni", "Yatsı Öncesi", "Toprak / Sevda", "#6366f1"),
        ("Hicaz", "Yatsı & Gece", "Ateş / Safra", "#ec4899")
    ]

    r_outer = 290
    r_inner = 170

    for i, (mname, vkt, mzc, color) in enumerate(makamlar):
        ang1 = (i * 30 - 15) * math.pi / 180
        ang2 = (i * 30 + 15) * math.pi / 180
        ang_mid = i * 30 * math.pi / 180

        # Segment arc
        x1_out = cx + math.cos(ang1) * r_outer
        y1_out = cy + math.sin(ang1) * r_outer
        x2_out = cx + math.cos(ang2) * r_outer
        y2_out = cy + math.sin(ang2) * r_outer
        x1_in = cx + math.cos(ang2) * r_inner
        y1_in = cy + math.sin(ang2) * r_inner
        x2_in = cx + math.cos(ang1) * r_inner
        y2_in = cy + math.sin(ang1) * r_inner

        path_d = f"M {x1_out} {y1_out} A {r_outer} {r_outer} 0 0 1 {x2_out} {y2_out} L {x1_in} {y1_in} A {r_inner} {r_inner} 0 0 0 {x2_in} {y2_in} Z"
        svg.append(f'<path d="{path_d}" fill="{color}" fill-opacity="0.15" stroke="{color}" stroke-width="1.2" />')

        # Text in segment
        r_text = (r_outer + r_inner) / 2
        tx = cx + math.cos(ang_mid) * r_text
        ty = cy + math.sin(ang_mid) * r_text
        svg.append(f'<text x="{tx}" y="{ty}" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="700" fill="#f8fafc">{mname}</text>')
        svg.append(f'<text x="{tx}" y="{ty+13}" text-anchor="middle" font-family="sans-serif" font-size="9" fill="{color}">{vkt}</text>')

    # Center circle: Ney & Darüşşifa Symbol
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r_inner-10}" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5" />')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="50" fill="none" stroke="#67e8f9" stroke-opacity="0.4" stroke-width="1" stroke-dasharray="3,3" />')
    svg.append(f'<text x="{cx}" y="{cy-20}" text-anchor="middle" font-family="Cinzel, serif" font-size="18" font-weight="700" fill="#fbbf24">DARÜŞŞİFA</text>')
    svg.append(f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#94a3b8">Ahlat-ı Erba\'a</text>')
    svg.append(f'<text x="{cx}" y="{cy+24}" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#67e8f9">4 Mizaç &amp; 12 Makam</text>')

    svg.append('</svg>')
    out_path = ASSETS_DIR / "makam_therapy_darussifa.svg"
    out_path.write_text("\n".join(svg), encoding="utf-8")
    print(f"Created: {out_path}")


def generate_heart_coherence_svg():
    """0.1 Hz Kalp Hızı Değişkenliği (HRV) ve Vagal Tonlama İnfografiği."""
    w, h = 900, 420
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">')
    svg.append('<rect width="100%" height="100%" fill="#0a0e17" />')

    svg.append('<text x="450" y="40" text-anchor="middle" font-family="Cinzel, serif" font-size="20" font-weight="700" fill="#f43f5e" letter-spacing="2">0.1 Hz KALP HIZI DEĞİŞKENLİĞİ (HRV) &amp; VAGAL SENKRONİZASYON</text>')
    svg.append('<text x="450" y="62" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#94a3b8">Kaotik Sempatik Aktivasyon vs 0.1 Hz Rezonant Parasempatik Koherans</text>')

    # Top Graph: Chaotic HRV (Stress)
    svg.append('<rect x="50" y="90" width="800" height="130" rx="6" fill="#111827" stroke="#ef4444" stroke-opacity="0.3" />')
    svg.append('<text x="70" y="115" font-family="sans-serif" font-size="13" font-weight="700" fill="#ef4444">1. KAOTİK HRV (Stres, Kaygı, Sempatik Baskınlık)</text>')
    svg.append('<text x="70" y="132" font-family="sans-serif" font-size="11" fill="#94a3b8">Düzensiz atımlar, düşük vagal tonus, amigdala ajitasyonu</text>')

    chaotic_points = []
    for x in range(70, 830, 4):
        # Irregular noise wave
        y = 175 + math.sin(x * 0.05) * 18 + math.sin(x * 0.12) * 12 + math.sin(x * 0.28) * 8
        chaotic_points.append(f"{x},{y:.1f}")
    svg.append(f'<polyline points="{" ".join(chaotic_points)}" fill="none" stroke="#ef4444" stroke-width="1.8" />')

    # Bottom Graph: Coherent Sinusoid 0.1 Hz (Vagus & Meditation)
    svg.append('<rect x="50" y="240" width="800" height="130" rx="6" fill="#111827" stroke="#10b981" stroke-opacity="0.3" />')
    svg.append('<text x="70" y="265" font-family="sans-serif" font-size="13" font-weight="700" fill="#10b981">2. KOHERENT SİNÜZOİDAL HRV (0.10 Hz / Vagal Kilitlenme)</text>')
    svg.append('<text x="70" y="282" font-family="sans-serif" font-size="11" fill="#94a3b8">5.5s nefes alış, 5.5s veriş ritmi ile baroreseptör ve kalp atışının tam rezonansı</text>')

    coherent_points = []
    for x in range(70, 830, 4):
        # Smooth coherent 0.1 Hz sine wave
        y = 325 + math.sin(x * 0.025) * 28
        coherent_points.append(f"{x},{y:.1f}")
    svg.append(f'<polyline points="{" ".join(coherent_points)}" fill="none" stroke="#10b981" stroke-width="2.5" />')

    svg.append('<text x="450" y="395" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#94a3b8">Titresim v2.0 Kalp Koheransı Protokolü, 0.10 Hz izokronik modülasyon ile vagal freni devreye sokar.</text>')

    svg.append('</svg>')
    out_path = ASSETS_DIR / "heart_coherence_01hz.svg"
    out_path.write_text("\n".join(svg), encoding="utf-8")
    print(f"Created: {out_path}")


if __name__ == "__main__":
    generate_banner_svg()
    generate_cymatics_patterns_svg()
    generate_chakra_spectrum_svg()
    generate_brainwaves_svg()
    generate_makam_wheel_svg()
    generate_heart_coherence_svg()
