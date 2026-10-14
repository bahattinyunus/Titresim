"""
Titresim CLI (Komut Satırı Arayüzü)
Kullanım: python -m titresim [komut] [seçenekler]
"""

import argparse
import sys
import os
import webbrowser
from http.server import SimpleHTTPRequestHandler
import socketserver
from pathlib import Path

# Windows konsolunda UTF-8 karakter desteği
try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

from .core.frequencies import Solfeggio, Brainwaves, CosmicOctave
from .core.makam import MakamTherapy
from .core.cymatics import ChladniPlate
from .core.generator import ToneGenerator
from .core.binaural import BinauralBeatGenerator


def handle_info(args):
    target = args.target.lower()
    if target in ("solfeggio", "solf"):
        print("\n" + "=" * 65)
        print("          SOLFEGGIO KUTSAL ŞİFA FREKANSLARI")
        print("=" * 65)
        for t in Solfeggio.get_all():
            print(f"🎵 {t.frequency} Hz | {t.name}")
            print(f"   Nota: {t.note} | Çakra: {t.chakra}")
            print(f"   Niyet: {t.intention}")
            print(f"   Açıklama: {t.description}\n")

    elif target in ("makam", "makamlar"):
        if args.name:
            m = MakamTherapy.find_by_id(args.name)
            if not m:
                print(f"❌ '{args.name}' makamı bulunamadı.")
                return
            print("\n" + "=" * 65)
            print(f"  {m.name.upper()} - ŞİFA VE REZONANS BİLGİSİ")
            print("=" * 65)
            print(f"• Temel Ton: {m.root_tone}")
            print(f"• Vakti: {m.time}")
            print(f"• Element & Burç: {m.element} / {m.zodiac}")
            print(f"• Tesirli Organlar: {m.organ}")
            print(f"• Terapötik Etkiler:")
            for eff in m.therapeutic_effects:
                print(f"   - {eff}")
            print(f"• Kadim Not: {m.scholar_notes}\n")
        else:
            print("\n" + "=" * 65)
            print("       OSMANLI DARÜŞŞİFA MAKAMLARI (FARABİ & İBN-İ SİNA)")
            print("=" * 65)
            for m in MakamTherapy.get_all():
                print(f"✨ {m.name} ({m.root_tone}) - Vakit: {m.time}")
                print(f"   Organ: {m.organ}")
                print(f"   Tıbbi Özellik: {m.therapeutic_effects[0]}\n")

    elif target in ("brain", "beyin"):
        print("\n" + "=" * 65)
        print("          BEYİN DALGASI BANTLARI VE BİLİNÇ HALLERİ")
        print("=" * 65)
        for b in Brainwaves.get_all():
            print(f"🧠 {b.band} | Aralık: {b.range_hz[0]}-{b.range_hz[1]} Hz (Merkez: {b.center_hz} Hz)")
            print(f"   Bilinç Durumu: {b.state}")
            print(f"   Biyolojik Etki: {b.effects}\n")

    elif target in ("cosmic", "kozmik", "schumann"):
        print("\n" + "=" * 65)
        print("       HANS COUSTO KOZMİK OKTAV & SCHUMANN REZONANSLARI")
        print("=" * 65)
        for c in CosmicOctave.get_all():
            print(f"🌍 {c.name} | {c.frequency} Hz")
            print(f"   Kaynak: {c.source}")
            print(f"   Açıklama: {c.description}\n")
    else:
        print(f"Bilinmeyen bilgi hedefi: {args.target}. Seçenekler: solfeggio, makam, brain, cosmic")


def handle_generate(args):
    gen = ToneGenerator()
    print(f"🎵 {args.freq} Hz tonu üretiliyor (Süre: {args.duration}s)...")
    samples = gen.generate_sine(args.freq, args.duration, volume=args.volume)
    out_path = args.output or f"tone_{int(args.freq)}hz.wav"
    gen.save_wav(out_path, samples)
    print(f"✅ WAV dosyası başarıyla kaydedildi: {out_path}")


def handle_binaural(args):
    gen = BinauralBeatGenerator()
    print(f"🧠 Taşıyıcı: {args.carrier} Hz, Beat: {args.beat} Hz üretiliyor (Süre: {args.duration}s)...")
    l_samples, r_samples = gen.generate(
        carrier_freq=args.carrier,
        beat_freq=args.beat,
        duration=args.duration,
        volume=args.volume,
    )
    out_path = args.output or f"binaural_{args.carrier}_{args.beat}hz.wav"
    gen.save_stereo_wav(out_path, l_samples, r_samples)
    print(f"✅ Stereo Binaural WAV kaydedildi: {out_path}")


def handle_makam_audio(args):
    m = MakamTherapy.find_by_id(args.id)
    if not m:
        print(f"❌ '{args.id}' makamı bulunamadı.")
        return
    gen = ToneGenerator()
    freqs = m.get_frequencies(base_freq=args.base)
    print(f"🎶 {m.name} dizisi sentezleniyor (Temel ton: {args.base} Hz)...")
    print(f"   Perdeler: {freqs}")
    samples = gen.generate_scale(freqs, note_duration=args.note_duration)
    out_path = args.output or f"makam_{m.id}.wav"
    gen.save_wav(out_path, samples)
    print(f"✅ Makam ses kaydı hazır: {out_path}")


def handle_cymatics(args):
    if args.modes:
        n, m = map(int, args.modes.split(","))
        plate = ChladniPlate(n=n, m=m)
    else:
        plate = ChladniPlate.from_frequency(args.freq)

    print(f"\n🔮 Sematik Chladni Deseni (Modlar: n={plate.n}, m={plate.m})")
    print(plate.render_ascii(resolution=args.res))

    if args.svg:
        plate.export_svg(args.svg)
        print(f"✅ SVG çizimi kaydedildi: {args.svg}")


def handle_serve(args):
    web_dir = Path(__file__).resolve().parent.parent / "web"
    os.chdir(web_dir)
    port = args.port

    class QuietHandler(SimpleHTTPRequestHandler):
        def log_message(self, format, *argv):
            pass

    with socketserver.TCPServer(("", port), QuietHandler) as httpd:
        url = f"http://localhost:{port}"
        print("\n" + "=" * 65)
        print(f"  🌌 Titreşim İnteraktif Frekans Laboratuvarı Başlatıldı!")
        print(f"  Tarayıcıda açın: {url}")
        print("  Durdurmak için Ctrl+C tuşlarına basın.")
        print("=" * 65 + "\n")
        if not args.no_browser:
            webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nSunucu kapatıldı.")


def main():
    parser = argparse.ArgumentParser(
        prog="titresim",
        description="Titresim: Evrensel Ses, Kutsal Kelâm ve Frekans Terapisi Laboratuvarı",
    )
    subparsers = parser.add_subparsers(dest="command", help="Alt komutlar")

    # info
    p_info = subparsers.add_parser("info", help="Kadim arşiv ve frekans veri setlerini gösterir")
    p_info.add_argument("target", help="solfeggio | makam | brain | cosmic")
    p_info.add_argument("--name", "-n", help="Makam adı aramak için (örn: rast, hicaz)")

    # generate
    p_gen = subparsers.add_parser("generate", help="Saf veya harmonikli frekans WAV tonu üretir")
    p_gen.add_argument("--freq", "-f", type=float, default=528.0, help="Frekans (Hz)")
    p_gen.add_argument("--duration", "-d", type=float, default=5.0, help="Süre (saniye)")
    p_gen.add_argument("--volume", "-v", type=float, default=0.5, help="Ses şiddeti (0.0 - 1.0)")
    p_gen.add_argument("--output", "-o", help="Çıktı WAV dosyası")

    # binaural
    p_bin = subparsers.add_parser("binaural", help="Stereo binaural beat beyin dalgası üretir")
    p_bin.add_argument("--carrier", "-c", type=float, default=200.0, help="Taşıyıcı frekans (Hz)")
    p_bin.add_argument("--beat", "-b", type=float, default=7.83, help="Beat frekansı (Hz)")
    p_bin.add_argument("--duration", "-d", type=float, default=10.0, help="Süre (saniye)")
    p_bin.add_argument("--volume", "-v", type=float, default=0.5, help="Ses seviyesi")
    p_bin.add_argument("--output", "-o", help="Çıktı WAV dosyası")

    # makam-audio
    p_makam = subparsers.add_parser("makam-audio", help="Osmanlı makam dizisini sentezler")
    p_makam.add_argument("--id", required=True, help="Makam ID (rast, nihavend, hicaz vb.)")
    p_makam.add_argument("--base", type=float, default=220.0, help="Temel ton frekansı")
    p_makam.add_argument("--note-duration", type=float, default=0.7, help="Nota süresi")
    p_makam.add_argument("--output", "-o", help="Çıktı WAV dosyası")

    # cymatics
    p_cym = subparsers.add_parser("cymatics", help="Chladni sematik mandala modeli üretir")
    p_cym.add_argument("--freq", "-f", type=float, default=432.0, help="Frekans (Hz)")
    p_cym.add_argument("--modes", "-m", help="Özel modlar örn: 3,5")
    p_cym.add_argument("--res", "-r", type=int, default=37, help="ASCII çözünürlük")
    p_cym.add_argument("--svg", help="SVG dosyası olarak kaydetme yolu")

    # serve
    p_srv = subparsers.add_parser("serve", help="İnteraktif web laboratuvarını yerel sunucuda başlatır")
    p_srv.add_argument("--port", "-p", type=int, default=8000, help="Port numarası")
    p_srv.add_argument("--no-browser", action="store_true", help="Tarayıcıyı otomatik açma")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "info":
        handle_info(args)
    elif args.command == "generate":
        handle_generate(args)
    elif args.command == "binaural":
        handle_binaural(args)
    elif args.command == "makam-audio":
        handle_makam_audio(args)
    elif args.command == "cymatics":
        handle_cymatics(args)
    elif args.command == "serve":
        handle_serve(args)


if __name__ == "__main__":
    main()
