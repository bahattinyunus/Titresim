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

from .core.frequencies import Solfeggio, Brainwaves, CosmicOctave, PlanetaryFrequencies, fibonacci_tuning
from .core.makam import MakamTherapy
from .core.cymatics import ChladniPlate, CircularChladniPlate
from .core.generator import ToneGenerator
from .core.binaural import BinauralBeatGenerator
from .core.noise import NoiseGenerator
from .core.isochronic import IsochronicToneGenerator
from .core.traditions import SacredTraditions
from .core.tuning import TuningSystem
from .core.wisdom import WisdomArchive
from .core.session import TherapySessionEngine
from .core.chakra import ChakraResonance
from .core.seyir import MakamSeyirGenerator
from .core.organs import OrganResonance
from .core.phonetics import SacredPhonetics
from .core.breath import CoherenceBreathGuide


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

    elif target in ("planetary", "gezegen", "gezegenler"):
        print("\n" + "=" * 65)
        print("       HANS COUSTO GEZEGEN FREKANSLARI (PLANETARY TONES)")
        print("=" * 65)
        for p in PlanetaryFrequencies.get_all():
            print(f"🪐 {p.name} | {p.frequency} Hz ({p.note})")
            print(f"   Çakra: {p.chakra} | Döngü: {p.cycle}")
            print(f"   Etki: {p.effects}\n")

    elif target in ("traditions", "tradition", "gelenek", "gelenekler"):
        print("\n" + "=" * 65)
        print("       KUTSAL SES GELENEKLERİ & AKUSTİK ŞİFA DİSİPLİNLERİ")
        print("=" * 65)
        for tr in SacredTraditions.get_all():
            print(f"📜 {tr.tradition}")
            print(f"   Uygulama: {tr.practice}")
            print(f"   Temel Frekanslar: {', '.join(tr.fundamental_frequencies)}")
            print("   Akustik İlkeler:")
            for p in tr.acoustic_principles:
                print(f"     • {p}")
            print("   Nörobiyolojik Etkiler:")
            for e in tr.neurobiological_effects:
                print(f"     ✓ {e}")
            print(f"   Kaynaklar: {tr.historical_sources}\n")

    elif target in ("wisdom", "quotes", "sozler", "alintilar"):
        print("\n" + "=" * 68)
        print("     KADİM BİLGELİK, FREKANS VE REZONANS ALINTILARI ARŞİVİ")
        print("=" * 68)
        for q in WisdomArchive.get_all():
            print(f"\n« {q.author} » ({q.era}) - [{q.work}]")
            print(f"  “{q.quote_tr}”")
            if q.reflection:
                print(f"  💡 Tefekkür: {q.reflection}")
            print(f"  🎵 Frekans: {q.recommended_freq} Hz")
        print()

    elif target in ("chakra", "chakras", "cakra", "cakralar"):
        print("\n" + "=" * 68)
        print("        7 TEMEL ÇAKRA VE MERİDYEN AKUSTİK REZONANSI")
        print("=" * 68)
        for ch in ChakraResonance.get_all():
            print(f"🌈 {ch.name} ({ch.note})")
            print(f"   Konum: {ch.location} | Element: {ch.element}")
            print(f"   Solfeggio: {ch.solfeggio_freq} Hz | Gezegen (Cousto): {ch.planetary_freq} Hz | Tohum Bija: '{ch.bija_mantra}'")
            print(f"   Şifa Alanı: {ch.balance_effect}")
            print(f"   Dengesizlik: {ch.imbalance_symptoms}\n")

    elif target in ("protocol", "protocols", "protokol", "protokoller"):
        print("\n" + "=" * 68)
        print("          KLİNİK VE MEDİTATİF SES SEANSI PROTOKOLLERİ")
        print("=" * 68)
        for p in TherapySessionEngine.get_all_protocols():
            print(f"✨ [{p.id}] {p.title}")
            print(f"   Alt Başlık: {p.subtitle}")
            print(f"   Hedef Endikasyon: {p.target}")
            print(f"   Tavsiye Edilen Süre: {p.total_recommended_minutes} dakika | Aşama Sayısı: {len(p.stages)}")
            for st in p.stages:
                print(f"     Aşama {st.stage}: {st.name} ({st.duration_percent:.0f}%) -> {st.carrier_freq} Hz (Beat: {st.beat_freq} Hz - {st.band}) + {st.noise_type} gürültü")
            print()
    else:
        print(f"Bilinmeyen bilgi hedefi: {args.target}. Seçenekler: solfeggio, makam, brain, cosmic, planetary, traditions, wisdom, chakra, protocol")


def handle_quote(args):
    if args.id:
        q = WisdomArchive.find_by_id(args.id)
        if q:
            print("\n" + WisdomArchive.format_quote_card(q) + "\n")
        else:
            print(f"❌ '{args.id}' kimlikli alıntı bulunamadı.")
    elif args.search:
        results = WisdomArchive.search(args.search)
        if not results:
            print(f"🔍 '{args.search}' terimiyle eşleşen alıntı bulunamadı.")
            return
        print(f"\n🔍 '{args.search}' ile eşleşen {len(results)} bilgelik alıntısı:\n")
        for q in results:
            print(WisdomArchive.format_quote_card(q))
            print()
    elif args.category:
        results = WisdomArchive.get_by_category(args.category)
        if not results:
            print(f"❌ '{args.category}' kategorisi bulunamadı. Seçenekler: {', '.join(WisdomArchive.CATEGORIES.keys())}")
            return
        print(f"\n📚 {WisdomArchive.CATEGORIES.get(args.category, args.category)} Kategorisindeki Alıntılar ({len(results)} adet):\n")
        for q in results:
            print(WisdomArchive.format_quote_card(q))
            print()
    elif args.author:
        results = WisdomArchive.get_by_author(args.author)
        if not results:
            print(f"🔍 '{args.author}' ile eşleşen müellif bulunamadı.")
            return
        print(f"\n✒️ {args.author.title()} Alıntıları ({len(results)} adet):\n")
        for q in results:
            print(WisdomArchive.format_quote_card(q))
            print()
    elif args.all:
        quotes = WisdomArchive.get_all()
        print(f"\n🏛️ KADİM BİLGELİK & SES FELSEFESİ KÜLLİYATI ({len(quotes)} Alıntı)\n")
        for q in quotes:
            print(WisdomArchive.format_quote_card(q))
            print()
    else:
        # Varsayılan: Rastgele ilham verici bir bilgelik sözü
        q = WisdomArchive.get_random()
        if q:
            print("\n" + WisdomArchive.format_quote_card(q) + "\n")


def handle_generate(args):
    gen = ToneGenerator()
    print(f"🎵 {args.freq} Hz tonu üretiliyor (Süre: {args.duration}s)...")
    samples = gen.generate_sine(args.freq, args.duration, volume=args.volume)
    out_path = args.output or f"tone_{int(args.freq)}hz.wav"
    gen.save_wav(out_path, samples)
    print(f"✅ WAV dosyası başarıyla kaydedildi: {out_path}")


def handle_binaural(args):
    gen = BinauralBeatGenerator()
    print(f"🧠 Taşıyıcı: {args.carrier} Hz, Beat: {args.beat} Hz (Pembe Gürültü: {args.noise}) üretiliyor (Süre: {args.duration}s)...")
    l_samples, r_samples = gen.generate(
        carrier_freq=args.carrier,
        beat_freq=args.beat,
        duration=args.duration,
        volume=args.volume,
        pink_noise_level=args.noise,
    )
    out_path = args.output or f"binaural_{args.carrier}_{args.beat}hz.wav"
    gen.save_stereo_wav(out_path, l_samples, r_samples)
    print(f"✅ Stereo Binaural WAV kaydedildi: {out_path}")


def handle_isochronic(args):
    gen = IsochronicToneGenerator()
    print(f"⚡ İzokronik Ton: Taşıyıcı {args.carrier} Hz, Nabız {args.pulse} Hz üretiliyor (Süre: {args.duration}s)...")
    samples = gen.generate(
        carrier_freq=args.carrier,
        pulse_rate_hz=args.pulse,
        duration=args.duration,
        volume=args.volume,
        duty_cycle=args.duty,
    )
    tone_gen = ToneGenerator()
    out_path = args.output or f"isochronic_{int(args.carrier)}hz_{args.pulse}hz.wav"
    tone_gen.save_wav(out_path, samples)
    print(f"✅ İzokronik WAV kaydedildi: {out_path}")


def handle_noise(args):
    gen = NoiseGenerator()
    ntype = args.type.lower()
    print(f"🌊 {ntype.capitalize()} gürültü üretiliyor (Süre: {args.duration}s)...")
    if ntype in ("pink", "pembe"):
        samples = gen.generate_pink_noise(args.duration, volume=args.volume)
    elif ntype in ("brown", "red", "kahverengi"):
        samples = gen.generate_brown_noise(args.duration, volume=args.volume)
    else:
        samples = gen.generate_white_noise(args.duration, volume=args.volume)

    tone_gen = ToneGenerator()
    out_path = args.output or f"noise_{ntype}.wav"
    tone_gen.save_wav(out_path, samples)
    print(f"✅ Gürültü WAV kaydedildi: {out_path}")


def handle_drone(args):
    gen = ToneGenerator()
    print(f"🕉️ Meditatif Dem / Tanpura Drone: {args.freq} Hz (Süre: {args.duration}s)...")
    samples = gen.generate_drone(
        root_frequency=args.freq,
        duration=args.duration,
        volume=args.volume,
    )
    out_path = args.output or f"drone_{int(args.freq)}hz.wav"
    gen.save_wav(out_path, samples)
    print(f"✅ Meditatif Dem WAV kaydedildi: {out_path}")


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


def handle_tuning(args):
    print("\n" + "=" * 65)
    print("      AKUSTİK AKORT VE 53-TET MİKROTONAL KOMA CETVELİ")
    print("=" * 65)
    print("• 53-TET (Holderian Koma) Birim Değerleri:")
    for k, v in TuningSystem.INTERVALS_53TET.items():
        print(f"  [{v.symbol}] {v.name:16} : {v.commas:2} Koma ({v.cents:6.2f} cent) - {v.description}")

    if args.a4_from and args.a4_to and args.freq:
        converted = TuningSystem.convert_a4(args.freq, args.a4_from, args.a4_to)
        print(f"\n🔄 Frekans Dönüşümü ({args.a4_from} Hz -> {args.a4_to} Hz):")
        print(f"   {args.freq} Hz ==> {converted} Hz")

    if args.pythagorean:
        print(f"\n📐 Pisagor Doğal 3:2 Saf Beşli Dizisi (Tonic: {args.pythagorean} Hz):")
        for step, freq, cents in TuningSystem.pythagorean_scale(args.pythagorean):
            print(f"   {step:28} : {freq:7.2f} Hz ({cents:6.1f} cent)")


def handle_cymatics(args):
    if args.circular:
        if args.modes:
            n, m = map(int, args.modes.split(","))
            plate = CircularChladniPlate(n=n, m=m)
        else:
            plate = CircularChladniPlate.from_frequency(args.freq)

        print(f"\n🔮 Dairesel Sematik / Su Çanağı Deseni (Modlar: n={plate.n}, m={plate.m})")
        print(plate.render_ascii(resolution=args.res))
    else:
        if args.modes:
            n, m = map(int, args.modes.split(","))
            plate = ChladniPlate(n=n, m=m)
        else:
            plate = ChladniPlate.from_frequency(args.freq)

        print(f"\n🔮 Kare Sematik Chladni Deseni (Modlar: n={plate.n}, m={plate.m})")
        print(plate.render_ascii(resolution=args.res))

    if args.svg:
        plate.export_svg(args.svg)
        print(f"✅ SVG çizimi kaydedildi: {args.svg}")


def handle_protocol(args):
    protocols = TherapySessionEngine.get_all_protocols()
    if args.id:
        p = TherapySessionEngine.find_protocol(args.id)
        if not p:
            print(f"❌ '{args.id}' kimlikli seans protokolü bulunamadı.")
            return
        print("\n" + "=" * 68)
        print(f"  KLİNİK SEANS PROTOKOLÜ: {p.title.upper()}")
        print("=" * 68)
        print(f"• Alt Başlık: {p.subtitle}")
        print(f"• Hedef Endikasyon: {p.target}")
        print(f"• Tavsiye Edilen Süre: {p.total_recommended_minutes} Dakika")
        print("• Aşamalar:")
        for st in p.stages:
            print(f"   [{st.stage}] {st.name} ({st.duration_percent:.0f}%)")
            print(f"       Taşıyıcı: {st.carrier_freq} Hz | Beat: {st.beat_freq} Hz ({st.band})")
            print(f"       Zemin Gürültüsü: {st.noise_type.capitalize()} (Seviye: {st.noise_volume})")
            print(f"       Etki: {st.description}")
        print()
    else:
        print("\n" + "=" * 68)
        print("       KLİNİK VE MEDİTATİF TERAPÖTİK SEANS PROTOKOLLERİ")
        print("=" * 68)
        for p in protocols:
            print(f"✨ [{p.id}] {p.title} ({p.total_recommended_minutes} Dk)")
            print(f"   Hedef: {p.target}")
            print(f"   Aşama Sayısı: {len(p.stages)}\n")


def handle_session(args):
    engine = TherapySessionEngine()
    out_path = args.output or f"session_{args.id}.wav"
    duration_sec = args.duration * 60.0 if args.minutes else args.duration
    print(f"🧘 '{args.id}' seansı sentezleniyor (Süre: {duration_sec:.1f} saniye)...")
    try:
        prot = engine.export_session_wav(
            filepath=out_path,
            protocol_id=args.id,
            duration_seconds=duration_sec,
            volume=args.volume
        )
        print(f"✅ Seans başarıyla sentezlendi ve kaydedildi: {out_path}")
        print(f"   Protokol: {prot.title}")
    except Exception as e:
        print(f"❌ Hata: {e}")


def handle_chakra(args):
    if args.align:
        gen = ToneGenerator()
        print(f"🌈 7 Çakra Gökkuşağı Akordu (Rainbow Alignment) üretiliyor...")
        samples = ChakraResonance.generate_rainbow_alignment(duration_per_chakra=args.duration)
        out_path = args.output or "chakra_rainbow_alignment.wav"
        gen.save_wav(out_path, samples)
        print(f"✅ Çakra dengeleme WAV dosyası kaydedildi: {out_path}")
    elif args.id:
        ch = ChakraResonance.find_by_id(args.id)
        if not ch:
            print(f"❌ '{args.id}' çakrası bulunamadı.")
            return
        freq = ch.solfeggio_freq if args.mode == "solfeggio" else ch.planetary_freq
        print(f"✨ {ch.name} ({ch.note}) - {args.mode.capitalize()} Tonu: {freq} Hz üretiliyor...")
        samples = ChakraResonance.generate_chakra_tone(ch.id, mode=args.mode, duration=args.duration)
        out_path = args.output or f"chakra_{ch.id}_{args.mode}.wav"
        gen = ToneGenerator()
        gen.save_wav(out_path, samples)
        print(f"✅ Çakra tonu kaydedildi: {out_path}")
    else:
        print("\n" + "=" * 68)
        print("        7 TEMEL ÇAKRA VE MERİDYEN REZONANS CETVELİ")
        print("=" * 68)
        for ch in ChakraResonance.get_all():
            print(f"🌈 [{ch.id}] {ch.name} ({ch.note}) - Tohum Mantra: '{ch.bija_mantra}'")
            print(f"   Solfeggio: {ch.solfeggio_freq} Hz | Gezegen Tonu: {ch.planetary_freq} Hz")
            print(f"   Şifa: {ch.balance_effect}\n")


def handle_seyir(args):
    gen = MakamSeyirGenerator()
    out_path = args.output or f"seyir_{args.makam}.wav"
    print(f"🎶 {args.makam.upper()} makam seyri ve meditatif taksim ezgisi sentezleniyor...")
    samples = gen.generate_seyir_melody(
        makam_id=args.makam,
        base_freq=args.base,
        unit_note_duration=args.unit_duration
    )
    tone_gen = ToneGenerator()
    tone_gen.save_wav(out_path, samples)
    print(f"✅ Meditatif makam seyri kaydedildi: {out_path}")


def handle_organ(args):
    if args.list:
        print("\n" + "=" * 65)
        print("     İNSAN BEDENİ VE ORGAN REZONANS FREKANSLARI")
        print("=" * 65)
        for org in OrganResonance.get_all():
            print(f"🫀 {org.name} | {org.frequency} Hz")
            print(f"   Kategori: {org.category.upper()} | Çakra: {org.associated_chakra}")
            print(f"   Açıklama: {org.description}")
            print(f"   Şifa Tesiri: {org.effects}\n")
        return

    if args.scan:
        out_path = args.output or "organ_tam_beden_taramasi.wav"
        print(f"🧬 Tüm organ sistemlerini tarayan akustik frekans banyosu sentezleniyor...")
        samples = OrganResonance.generate_full_body_scan(duration_per_organ=args.duration_per_organ)
        tone_gen = ToneGenerator()
        tone_gen.save_wav(out_path, samples)
        print(f"✅ Tam beden organ tarama seansı kaydedildi: {out_path}")
        return

    if args.id:
        org = OrganResonance.find_by_id(args.id)
        if not org:
            print(f"❌ Organ bulunamadı: {args.id}")
            return
        out_path = args.output or f"organ_{org.id}.wav"
        print(f"🫀 {org.name} ({org.frequency} Hz) rezonans tonu sentezleniyor...")
        samples = OrganResonance.generate_organ_tone(org.id, duration=args.duration)
        tone_gen = ToneGenerator()
        tone_gen.save_wav(out_path, samples)
        print(f"✅ Organ şifa tonu kaydedildi: {out_path}")
    else:
        print("Lütfen bir seçenek belirtin: --list, --id <organ_adi> veya --scan")


def handle_vocal(args):
    if args.list:
        print("\n" + "=" * 65)
        print("   KUTSAL KELÂM, VOKAL FORMANT VE GUNNE REZONANSLARI")
        print("=" * 65)
        for c in SacredPhonetics.get_all():
            print(f"🕊️ {c.name} | Temel: {c.base_pitch_hz} Hz | Formantlar: {c.formants}")
            print(f"   Gelenek: {c.tradition} | Mahreç: {c.mahref}")
            print(f"   Nitrik Oksit & Biyo-etki: {c.nitric_oxide_effect}\n")
        return

    if args.id:
        c = SacredPhonetics.find_by_id(args.id)
        if not c:
            print(f"❌ Kutsal kelâm bulunamadı: {args.id}")
            return
        out_path = args.output or f"vocal_{c.id}.wav"
        print(f"🕊️ {c.name} vokal formant rezonansı sentezleniyor...")
        samples = SacredPhonetics.synthesize_chant(c.id, duration=args.duration, base_pitch=args.pitch)
        tone_gen = ToneGenerator()
        tone_gen.save_wav(out_path, samples)
        print(f"✅ Vokal formant sesi kaydedildi: {out_path}")
    else:
        print("Lütfen bir seçenek belirtin: --list veya --id <hu|hayy|allah|ghunnah|aum>")


def handle_breath(args):
    if getattr(args, "list", False):
        print("\n" + "=" * 65)
        print("   KLİNİK VE MEDİTATİF SOLUNUM / KOHERANS MODELLERİ")
        print("=" * 65)
        for p in CoherenceBreathGuide.PATTERNS.values():
            print(f"🌬️ {p.name} ({p.id.upper()}) | Döngü: {p.total_cycle_sec:.1f}sn")
            print(f"   Aşamalar: Nefes Al: {p.inhale_sec}s | Tut: {p.hold_in_sec}s | Nefes Ver: {p.exhale_sec}s | Bekle: {p.hold_out_sec}s")
            print(f"   Etki: {p.clinical_effect}")
            print(f"   Açıklama: {p.description}\n")
        return

    pattern = CoherenceBreathGuide.get_pattern(args.pattern)
    out_path = args.output or f"nefes_{pattern.id}.wav"
    print(f"🌬️ {pattern.name} akustik rehber seansı sentezleniyor...")
    print(f"   Detay: {pattern.description} ({pattern.clinical_effect})")
    samples = CoherenceBreathGuide.generate_guided_session(
        pattern_id=pattern.id,
        total_duration_sec=args.duration,
        base_freq=args.base
    )
    tone_gen = ToneGenerator()
    tone_gen.save_wav(out_path, samples)
    print(f"✅ Solunum rehberi seansı kaydedildi: {out_path}")


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
    p_info.add_argument("target", help="solfeggio | makam | brain | cosmic | planetary | traditions")
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
    p_bin.add_argument("--noise", type=float, default=0.03, help="Arka plan pembe gürültü seviyesi (0.0-1.0)")
    p_bin.add_argument("--duration", "-d", type=float, default=10.0, help="Süre (saniye)")
    p_bin.add_argument("--volume", "-v", type=float, default=0.5, help="Ses seviyesi")
    p_bin.add_argument("--output", "-o", help="Çıktı WAV dosyası")

    # isochronic
    p_iso = subparsers.add_parser("isochronic", help="İzokronik nabız tonu üretir (Hoparlör uyumlu)")
    p_iso.add_argument("--carrier", "-c", type=float, default=432.0, help="Taşıyıcı ton (Hz)")
    p_iso.add_argument("--pulse", "-p", type=float, default=10.0, help="Vuruş/nabız frekansı (Hz)")
    p_iso.add_argument("--duty", type=float, default=0.5, help="Açık kalma oranı (0.1 - 0.9)")
    p_iso.add_argument("--duration", "-d", type=float, default=10.0, help="Süre (saniye)")
    p_iso.add_argument("--volume", "-v", type=float, default=0.5, help="Ses seviyesi")
    p_iso.add_argument("--output", "-o", help="Çıktı WAV dosyası")

    # noise
    p_noi = subparsers.add_parser("noise", help="Pembe, kahverengi veya beyaz akustik gürültü üretir")
    p_noi.add_argument("--type", "-t", default="pink", choices=["pink", "brown", "white", "pembe", "kahverengi"], help="Gürültü türü")
    p_noi.add_argument("--duration", "-d", type=float, default=10.0, help="Süre (saniye)")
    p_noi.add_argument("--volume", "-v", type=float, default=0.4, help="Ses seviyesi")
    p_noi.add_argument("--output", "-o", help="Çıktı WAV dosyası")

    # drone
    p_dro = subparsers.add_parser("drone", help="Meditatif sürekli Tanpura / Dem tonu üretir")
    p_dro.add_argument("--freq", "-f", type=float, default=136.1, help="Temel ton frekansı (Hz)")
    p_dro.add_argument("--duration", "-d", type=float, default=15.0, help="Süre (saniye)")
    p_dro.add_argument("--volume", "-v", type=float, default=0.5, help="Ses seviyesi")
    p_dro.add_argument("--output", "-o", help="Çıktı WAV dosyası")

    # makam-audio
    p_makam = subparsers.add_parser("makam-audio", help="Osmanlı makam dizisini sentezler")
    p_makam.add_argument("--id", required=True, help="Makam ID (rast, nihavend, hicaz vb.)")
    p_makam.add_argument("--base", type=float, default=220.0, help="Temel ton frekansı")
    p_makam.add_argument("--note-duration", type=float, default=0.7, help="Nota süresi")
    p_makam.add_argument("--output", "-o", help="Çıktı WAV dosyası")

    # tuning
    p_tun = subparsers.add_parser("tuning", help="Akort, 432 Hz / 440 Hz dönüşümü ve 53-TET koma bilgisi")
    p_tun.add_argument("--freq", "-f", type=float, help="Dönüştürülecek frekans")
    p_tun.add_argument("--a4-from", type=float, default=440.0, help="Kaynak A4 referansı")
    p_tun.add_argument("--a4-to", type=float, default=432.0, help="Hedef A4 referansı")
    p_tun.add_argument("--pythagorean", type=float, help="Pisagor skalası için temel frekans (Hz)")

    # cymatics
    p_cym = subparsers.add_parser("cymatics", help="Chladni sematik mandala modeli üretir")
    p_cym.add_argument("--freq", "-f", type=float, default=432.0, help="Frekans (Hz)")
    p_cym.add_argument("--modes", "-m", help="Özel modlar örn: 3,5")
    p_cym.add_argument("--circular", "-c", action="store_true", help="Dairesel plaka / su çanağı modülü")
    p_cym.add_argument("--res", "-r", type=int, default=37, help="ASCII çözünürlük")
    p_cym.add_argument("--svg", help="SVG dosyası olarak kaydetme yolu")

    # serve
    p_srv = subparsers.add_parser("serve", help="İnteraktif web laboratuvarını yerel sunucuda başlatır")
    p_srv.add_argument("--port", "-p", type=int, default=8000, help="Port numarası")
    p_srv.add_argument("--no-browser", action="store_true", help="Tarayıcıyı otomatik açma")

    # quote
    p_quo = subparsers.add_parser("quote", help="Kadim bilgelik, rezonans ve ses felsefesi alıntılarını getirir")
    p_quo.add_argument("--random", "-r", action="store_true", help="Rastgele bir bilgelik sözü getirir (varsayılan)")
    p_quo.add_argument("--category", "-c", choices=list(WisdomArchive.CATEGORIES.keys()), help="Kategoriye göre filtrele (tasavvuf, islam_tibbi, antik_felsefe, bilim_ve_fizik, mistik_akustik)")
    p_quo.add_argument("--author", "-a", help="Yazara göre ara (örn: tesla, mevlana, ibn sina, pisagor)")
    p_quo.add_argument("--search", "-s", help="Alıntı metinlerinde anahtar kelime ara")
    p_quo.add_argument("--id", help="Belirli bir alıntı ID'si")
    p_quo.add_argument("--all", action="store_true", help="Tüm bilgelik külliyatını listele")

    # protocol
    p_pro = subparsers.add_parser("protocol", help="Klinik ve meditatif seans protokollerini listeler veya inceler")
    p_pro.add_argument("--id", help="Protokol ID (sleep, focus, anxiety, heart, detox)")

    # session
    p_ses = subparsers.add_parser("session", help="Çok aşamalı terapötik seans WAV dosyası sentezler")
    p_ses.add_argument("--id", required=True, help="Protokol ID (sleep, focus, anxiety, heart, detox)")
    p_ses.add_argument("--duration", "-d", type=float, default=60.0, help="Seans süresi (varsayılan 60 saniye)")
    p_ses.add_argument("--minutes", "-m", action="store_true", help="Süreyi dakika olarak yorumlar")
    p_ses.add_argument("--volume", "-v", type=float, default=0.5, help="Ses seviyesi")
    p_ses.add_argument("--output", "-o", help="Çıktı WAV dosyası")

    # chakra
    p_cha = subparsers.add_parser("chakra", help="7 temel çakra rezonans tonu veya gökkuşağı akordu üretir")
    p_cha.add_argument("--id", help="Çakra ID (muladhara, svadhisthana, manipura, anahata, vishuddha, ajna, sahasrara)")
    p_cha.add_argument("--mode", choices=["solfeggio", "planetary"], default="solfeggio", help="Frekans modu")
    p_cha.add_argument("--duration", "-d", type=float, default=8.0, help="Ton süresi")
    p_cha.add_argument("--align", action="store_true", help="1'den 7'ye tam gökkuşağı çakra dengeleme dizisi üretir")
    p_cha.add_argument("--output", "-o", help="Çıktı WAV dosyası")

    # seyir
    p_sey = subparsers.add_parser("seyir", help="Geleneksel Osmanlı makam seyri ve meditatif taksim sentezler")
    p_sey.add_argument("--makam", "-m", default="rast", choices=["rast", "nihavend", "hicaz", "ussak"], help="Makam adı")
    p_sey.add_argument("--base", "-b", type=float, default=220.0, help="Karar perdesi frekansı (Hz)")
    p_sey.add_argument("--unit-duration", "-u", type=float, default=0.8, help="Birim nota süresi (sn)")
    p_sey.add_argument("--output", "-o", help="Çıktı WAV dosyası")

    # organ
    p_org = subparsers.add_parser("organ", help="İnsan organ ve dokularının biyofiziksel rezonans frekanslarını sentezler")
    p_org.add_argument("--list", "-l", action="store_true", help="Organ frekanslarını listele")
    p_org.add_argument("--id", help="Organ ID (heart, brain, liver, kidneys, lungs, stomach, pineal, thyroid, bones, thymus)")
    p_org.add_argument("--duration", "-d", type=float, default=6.0, help="Ton süresi (saniye)")
    p_org.add_argument("--scan", action="store_true", help="Tüm organları baştan ayağa tarayan tam akustik banyo")
    p_org.add_argument("--duration-per-organ", type=float, default=3.0, help="Organ başına tarama süresi")
    p_org.add_argument("--output", "-o", help="Çıktı WAV dosyası")

    # vocal
    p_voc = subparsers.add_parser("vocal", help="Kutsal kelâm ve tecvid gunne vokal formant rezonansı üretir")
    p_voc.add_argument("--list", "-l", action="store_true", help="Kutsal kelâm ve formantları listele")
    p_voc.add_argument("--id", help="Kelâm ID (hu, hayy, hakk, allah, ghunnah, aum, shalom, amen)")
    p_voc.add_argument("--pitch", "-p", type=float, help="Özel temel taşıyıcı frekans (Hz)")
    p_voc.add_argument("--duration", "-d", type=float, default=5.0, help="Formant tını süresi (sn)")
    p_voc.add_argument("--output", "-o", help="Çıktı WAV dosyası")

    # breath
    p_brt = subparsers.add_parser("breath", help="Akustik biyogeribildirim solunum ve koherans rehberi üretir")
    p_brt.add_argument("--list", "-l", action="store_true", help="Solunum modellerini ve sürelerini listele")
    p_brt.add_argument("--pattern", "-p", default="coherence", choices=["coherence", "box", "4-7-8", "relax"], help="Nefes tekniği")
    p_brt.add_argument("--duration", "-d", type=float, default=60.0, help="Toplam seans süresi (saniye)")
    p_brt.add_argument("--base", "-b", type=float, default=216.0, help="Taban taşıyıcı frekans (Hz)")
    p_brt.add_argument("--output", "-o", help="Çıktı WAV dosyası")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "info":
        handle_info(args)
    elif args.command == "quote":
        handle_quote(args)
    elif args.command == "protocol":
        handle_protocol(args)
    elif args.command == "session":
        handle_session(args)
    elif args.command == "chakra":
        handle_chakra(args)
    elif args.command == "seyir":
        handle_seyir(args)
    elif args.command == "organ":
        handle_organ(args)
    elif args.command == "vocal":
        handle_vocal(args)
    elif args.command == "breath":
        handle_breath(args)
    elif args.command == "generate":
        handle_generate(args)
    elif args.command == "binaural":
        handle_binaural(args)
    elif args.command == "isochronic":
        handle_isochronic(args)
    elif args.command == "noise":
        handle_noise(args)
    elif args.command == "drone":
        handle_drone(args)
    elif args.command == "makam-audio":
        handle_makam_audio(args)
    elif args.command == "tuning":
        handle_tuning(args)
    elif args.command == "cymatics":
        handle_cymatics(args)
    elif args.command == "serve":
        handle_serve(args)


if __name__ == "__main__":
    main()
