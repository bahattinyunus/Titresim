# 〰️ Titreşim: Evrensel Ses, Kutsal Kelâm ve Frekans Terapisi

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.2.0-f59e0b?style=for-the-badge" alt="Version 1.2.0">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/License-MIT-amber?style=for-the-badge" alt="License MIT">
  <img src="https://img.shields.io/badge/Web%20Audio-Interactive%20Studio%20v1.2-38bdf8?style=for-the-badge&logo=html5&logoColor=white" alt="Web Studio">
  <img src="https://img.shields.io/badge/Tests-35%20Passed-10b981?style=for-the-badge" alt="Tests">
</p>

> *"Evrenin sırrını bulmak istiyorsanız; enerji, frekans ve titreşim cinsinden düşünün."* — **Nikola Tesla**
>
> *"Başlangıçta Söz vardı. Söz Allah ile birlikteydi ve Söz Allah'ıydı."* — **Yuhanna 1:1**
>
> *"O, 'Ol!' (Kün!) dedi ve her şey titreşerek var oldu."* — **Kutsal Metinler Muhtevası**
>
> *"Her şey enerjidir ve her şey sadece bundan ibarettir. Sahip olmak istediğiniz gerçekliğin frekansına uyum sağladığınızda, artık o gerçeğe sahip olursunuz."* — **Albert Einstein**

---

## 🌟 Proje Vizyonu ve Felsefesi

Bu repo; sesin yalnızca işitsel bir duyu uyarısı değil, evrenin temel yapı taşı, maddeye şekil veren kurucu bir enerji formu ve insanlık tarihinin en kadim şifa aracı olduğu gerçeğinden yola çıkılarak geliştirilmiş **kapsamlı bir akustik rezonans ve şifa ekosistemidir**.

Madde dediğimiz şeyin özü titreşimdir; kuantum altı parçacıklardan galaksilere kadar her varlık kendine has bir frekansta salınır. İnsanlık tarihi boyunca bilgelik gelenekleri, şifanın sesle (mantra, kıraat, ilahi, ezgi) mümkün olduğunu keşfetmiştir. Bu proje; **Kur'an-ı Kerim kıraatinin** biyoakustik ve nörolojik rezonansından, **Vedik mantralara**, **Gregoryen ilahilerinden** **Osmanlı darüşşifa müzikterapisi geleneklerine**, **53-TET Arel-Ezgi mikrotonal koma akort sisteminden**, **Chladni & Bessel Sematik (Cymatics)** fiziğine, **İzokronik nabız tonlarına**, **pembe/kahverengi akustik gürültü maskelemesine**, **Binaural Beats** ve **Hans Cousto Kozmik Gezegen Oktavı**'na kadar sesin evrensel şifa haritasını dijital dünyada modeller.

---

## 🚀 Proje Mimarisi ve Temel Bileşenler

```
Titresim/
├── data/                               # Yapılandırılmış Açık Veri Setleri (JSON)
│   ├── solfeggio.json                  # 9 Kutsal Solfeggio Frekansı & Niyetleri
│   ├── makamlar.json                   # 12 Osmanlı Şifa Makamı (Farabi & İbn-i Sina)
│   ├── traditions.json                 # Kutsal Ses Gelenekleri & Nörobiyolojik Etkileri
│   ├── brainwaves.json                 # Delta, Teta, Alfa, Beta, Gama Bantları
│   ├── cosmic_octave.json              # Schumann Rezonansı & Hans Cousto Kozmik Tonları
│   └── planetary.json                  # Hans Cousto 12 Gezegen Yörünge Frekansı
├── docs/                               # Kapsamlı Bilimsel ve Tarihsel Araştırma Metinleri
│   ├── KUTSAL_KELAM_VE_REZONANS.md     # Tecvid Kaideleri, Gunne, Nitrik Oksit, Vagus & EEG
│   ├── OSMANLI_MUZIKTERAPISI.md        # Ahlat-ı Erba'a (4 Mizaç), Edirne Darüşşifası & Makamlar
│   ├── MIKROTONAL_KOMA_VE_53_KOMALI_SISTEM.md # 53-TET Holderian Koma, Pisagor & Makam Perdeleri
│   ├── SEMATIK_VE_KUTSAL_GEOMETRI.md   # Chladni & Bessel Dalga Mekaniği & Beden Suyu Rezonansı
│   ├── BEYIN_DALGALARI_VE_BINAURAL.md  # 0.1 Hz Kardiyorespiratuar Koherans & FFR Mekanizması
│   ├── IZOKRONIK_TONLAR_VE_GURULTU_TERAPISI.md # Hoparlör Uyumlu Nabızlar, Pembe/Kahverengi Gürültü
│   └── SOLFEGGIO_VE_KOZMIK_OKTAV.md    # Guido d'Arezzo İlahisi & Hans Cousto Matematiksel Modeli
├── titresim/                           # Python 3 Ses Sentezleme & Hesaplama Çekirdeği
│   ├── __init__.py                     # Paket Girişi & Genel İhracatlar (v1.2.0)
│   ├── __main__.py                     # Modül Olarak Çalıştırma Desteği
│   ├── cli.py                          # Zengin CLI Komut Satırı Arayüzü
│   └── core/
│       ├── frequencies.py              # Solfeggio, Beyin Dalgaları, Kozmik & Gezegen Tonları
│       ├── makam.py                    # Makam Terapisi Arama Motoru & Dizi Frekans Hesaplayıcı
│       ├── cymatics.py                 # Kare & Dairesel Chladni/Bessel Plaka Simülatörü & SVG
│       ├── generator.py                # Saf Python PCM WAV Sentezleyici & Meditatif Dem/Drone
│       ├── binaural.py                 # 2 Kanallı Stereo Binaural Beat & Pembe Gürültü Katmanı
│       ├── isochronic.py               # Hoparlör Uyumlu İzokronik Darbe Sentezleyici
│       ├── noise.py                    # Pembe (1/f), Kahverengi (1/f²) ve Beyaz Gürültü Motoru
│       ├── traditions.py               # Kutsal Ses Gelenekleri Bilgi Motoru
│       └── tuning.py                   # 53-TET Koma, 432 Hz/440 Hz Dönüşümü & Pisagor Akordu
├── web/                                # İnteraktif Web Audio & Cymatics Laboratuvarı v1.2
│   ├── index.html                      # Modern Görsel Arayüz (HTML5 + Glassmorphism)
│   ├── style.css                       # Koyu & Mistik Tasarım (Glassmorphism + KaTeX stili)
│   └── app.js                          # Web Audio API + Canlı Sematik + WAV Kaydedici + Sayaç
├── tests/                              # Kapsamlı Birim Testleri (35 Test - %100 Başarılı)
│   ├── test_frequencies.py
│   ├── test_makam.py
│   ├── test_cymatics.py
│   ├── test_circular_cymatics.py
│   ├── test_generator.py
│   ├── test_binaural.py
│   ├── test_isochronic.py
│   ├── test_noise.py
│   ├── test_traditions.py
│   └── test_tuning.py
├── pyproject.toml                      # Modern Python Paketleme Yapılandırması
├── LICENSE                             # MIT Açık Kaynak Lisansı
└── README.md                           # Ana Dokümantasyon
```

---

## ⚡ Hızlı Başlangıç

### Gereksinimler
* Python 3.9 veya üzeri
* Herhangi bir harici Python kütüphanesine bağımlılık **yoktur** (Standart Python kütüphaneleri `math`, `wave`, `struct`, `json` kullanılmıştır).
* Web Laboratuvarı için modern bir internet tarayıcısı (Chrome, Edge, Firefox, Safari).

### Kurulum

Projeyi klonlayın veya paketi yerel geliştirme modunda kurun:
```bash
git clone https://github.com/arch-yunus/Titresim.git
cd Titresim

# İsteğe bağlı olarak doğrudan CLI komutu olarak sisteme kurmak için:
pip install -e .
```

---

## 🖥️ CLI (Komut Satırı) Kullanımı

Paketi doğrudan `python -m titresim` veya `titresim` komutuyla çalıştırabilirsiniz:

### 1. Kadim Frekans, Gezegen ve Gelenek Arşivini Sorgulama
```bash
# Solfeggio kutsal frekanslarını listele
python -m titresim info solfeggio

# Hans Cousto kozmik gezegen frekanslarını listele
python -m titresim info planetary

# Kutsal ses geleneklerini (Tecvid/Kıraat, Vedik, Gregoryen, Tibet) listele
python -m titresim info traditions

# Osmanlı darüşşifa makamlarını listele
python -m titresim info makam

# Belirli bir makamın tıbbi ve müzikal detaylarını getir
python -m titresim info makam -n rast
```

### 2. Akort Sistemleri & 53-TET Koma Hesaplayıcı
```bash
# 440 Hz'i 432 Hz Verdi akorduna çevir ve Pisagor 3:2 saf beşli dizisini göster
python -m titresim tuning --freq 440 --a4-from 440 --a4-to 432 --pythagorean 216
```

### 3. Saf ve Harmonikli Ses (WAV) Üretimi
```bash
# 528 Hz (Mi - DNA Onarım & Aşk) frekansında 5 saniyelik WAV üret
python -m titresim generate --freq 528 --duration 5 --output dna_528hz.wav
```

### 4. Stereo Binaural Beat & Pembe Gürültülü Beyin Dalgası Sentezi
```bash
# 200 Hz taşıyıcı ton ve 7.83 Hz Schumann rezonansı beat'i, yumuşak pembe gürültü zeminli
python -m titresim binaural --carrier 200 --beat 7.83 --noise 0.04 --duration 10 -o schumann.wav
```

### 5. İzokronik Tonlar (Hoparlör Uyumlu Kulaklıksız Beyin Dalgası)
```bash
# 432 Hz taşıyıcı üzerinde 10 Hz Alfa nabzı üret
python -m titresim isochronic --carrier 432 --pulse 10.0 --duration 10 -o isochronic_alpha.wav
```

### 6. Pembe, Kahverengi ve Beyaz Akustik Gürültü Sentezi
```bash
# Tinnitus ve derin uyku için 1/f pembe gürültü üret
python -m titresim noise --type pink --duration 15 -o pink_noise.wav

# DEHB ve sakinleşme için 1/f² kahverengi gürültü üret
python -m titresim noise --type brown --duration 15 -o brown_noise.wav
```

### 7. Sürekli Meditatif Dem / Tanpura Drone Tonu
```bash
# 136.1 Hz (Dünya Yılı / Om) karar tonunda rezonant sürekli Dem üret
python -m titresim drone --freq 136.1 --duration 20 -o om_drone.wav
```

### 8. Osmanlı Makam Şifa Dizisini Sentezleme
```bash
# Nihavend makamının arpej dizisini saf ney harmonikleriyle seslendir
python -m titresim makam-audio --id nihavend --base 220 --output nihavend.wav
```

### 9. Matematiksel Sematik (Cymatics) Mandala Modelleri
```bash
# 432 Hz için terminalde kare Chladni deseni çizdir ve SVG kaydet
python -m titresim cymatics --freq 432 --svg chladni_432.svg

# Dairesel Chladni / Su Çanağı Bessel desenini terminalde çizdir
python -m titresim cymatics --circular --freq 432 --res 25
```

### 10. İnteraktif Web Laboratuvarını Başlatma
```bash
python -m titresim serve --port 8000
```
Tarayıcınız otomatik olarak `http://localhost:8000` adresinde açılacaktır.

---

## 🌐 İnteraktif Web Audio & Cymatics Laboratuvarı v1.2

`web/` dizininde yer alan laboratuvar tamamen tarayıcı içinde çalışır:
* **Canlı Chladni & Dairesel Su Simülasyonu:** 2800 adet kum taneciğinin ses dalgalarının nodal çizgilerine aktığı gerçek zamanlı fizik motoru. Kare plaka ve Dairesel su çanağı modları arasında tek tıkla geçiş!
* **Web Audio API Osilatörleri:** Solfeggio tonları, 12 Osmanlı makamı, stereo binaural beats, izokronik vuruşlar ve canlı gezegen tonları.
* **Akustik Gürültü Mikseri:** Pembe (1/f), Kahverengi (1/f²) ve Beyaz gürültüyü canlı olarak seansın arkasına karıştırabilme.
* **Sürekli Dem (Drone) Modu:** Ney ve Tanpura benzeri 4 katmanlı rezonant dem tonu.
* **Canlı Seans Kaydedici:** Çalınan seansı Web Audio üzerinden doğrudan kaydedip anında WAV/WebM formatında indirebilme.
* **Meditasyon Seans Zamanlayıcısı:** 5, 10 ve 20 dakikalık geri sayım; seans bitiminde çalan saf 528 Hz Tibet kase çanı.
* **0.1 Hz Vagus Siniri Nefes Rehberi:** 5.5 saniye nefes alma, 5.5 saniye nefes verme animasyonuyla kalp hızı değişkenliği (HRV) eğitimi.

---

## 🐍 Python SDK Olarak Kullanım

Kendi Python projelerinizde kütüphaneyi içe aktararak kullanabilirsiniz:

```python
from titresim import (
    Solfeggio,
    MakamTherapy,
    ChladniPlate,
    CircularChladniPlate,
    ToneGenerator,
    BinauralBeatGenerator,
    IsochronicToneGenerator,
    NoiseGenerator,
    PlanetaryFrequencies,
    TuningSystem
)

# 1. Gezegen Frekansı & Çakra Sorgusu
sun = PlanetaryFrequencies.find_by_id("sun")
print(f"{sun.name}: {sun.frequency} Hz - Çakra: {sun.chakra}")

# 2. 53-TET Koma & 432 Hz Dönüşümü
freq_432 = TuningSystem.convert_a4(440.0, source_a4=440.0, target_a4=432.0)
print(f"440 Hz'in 432 Hz Karşılığı: {freq_432} Hz")

# 3. Dairesel Bessel Sematik Deseni Üretimi
circle_plate = CircularChladniPlate.from_frequency(432.0)
print(circle_plate.render_ascii(resolution=25))

# 4. Hoparlör Uyumlu İzokronik Nabız Tonu Üretimi
iso_gen = IsochronicToneGenerator()
samples = iso_gen.generate(carrier_freq=432.0, pulse_rate_hz=10.0, duration=5.0)

# 5. Pembe Gürültü Katmanlı Binaural Beat WAV Sentezleme
binaural = BinauralBeatGenerator()
left, right = binaural.generate(carrier_freq=200, beat_freq=7.83, duration=5.0, pink_noise_level=0.03)
binaural.save_stereo_wav("schumann_pink.wav", left, right)
```

---

## 🧪 Birim Testleri

Tüm modüller kapsamlı birim testleriyle doğrulanmıştır:
```bash
python -m unittest discover tests
```
Çıktı:
```text
Ran 35 tests in 0.091s
OK
```

---

## 📚 Kapsamlı Dokümantasyon Arşivi

Detaylı bilimsel ve tarihi araştırmalar için `docs/` dizinindeki kaynak metinleri inceleyebilirsiniz:
1. [**Kutsal Kelâm, Kıraat Rezonansı ve Zikir Akustiği**](docs/KUTSAL_KELAM_VE_REZONANS.md) — Tecvid, Gunne ve Nitrik Oksit, Vagus ve Kalp Koheransı, Kur'an tilavetinin EEG Alfa/Teta etkileri.
2. [**Osmanlı Darüşşifalarında Müzikterapi ve Makam Şifası**](docs/OSMANLI_MUZIKTERAPISI.md) — Farabi, İbn-i Sina, Evliya Çelebi, 4 Mizaç (Ahlat-ı Erba'a) ve 12 klasik makam cetveli.
3. [**53-TET Mikrotonal Koma ve Perde Akustiği**](docs/MIKROTONAL_KOMA_VE_53_KOMALI_SISTEM.md) — Arel-Ezgi-Uzdilek koma cetveli, Pisagor koması ve darüşşifalardaki mikrotonal şifa matematiği.
4. [**Sematik (Cymatics), Rezonans ve Kutsal Geometri**](docs/SEMATIK_VE_KUTSAL_GEOMETRI.md) — Kare ve dairesel Chladni plaka matematiği, Bessel fonksiyonları ve bedendeki suyun ses ile yapılaşması.
5. [**İzokronik Tonlar ve Spektral Gürültü Terapisi**](docs/IZOKRONIK_TONLAR_VE_GURULTU_TERAPISI.md) — FFR mekanizması, hoparlör uyumlu izokronik nabızlar ve Pembe (1/f) / Kahverengi (1/f²) gürültü maskelemesi.
6. [**Beyin Dalgaları, Binaural Beats ve Vagus Siniri**](docs/BEYIN_DALGALARI_VE_BINAURAL.md) — Delta/Teta/Alfa/Beta/Gama spektrumu, frekans sürüklenmesi (FFR) ve 0.1 Hz kardiyorespiratuar koherans.
7. [**Solfeggio Frekansları ve Hans Cousto Kozmik Oktavı**](docs/SOLFEGGIO_VE_KOZMIK_OKTAV.md) — Guido d'Arezzo ilahisi, 9 Solfeggio tonu, gezegen periyotları ve 432 Hz Verdi akordu.

---

## 🤝 Katkıda Bulunma

Bu depo; sesin evrensel enerjisine, kadim bilgelik geleneklerine ve ses akustiğine ilgi duyan herkesin katkısına açıktır:
* Yeni gelenekler ve müzikterapi araştırmaları ekleyebilir,
* Ses sentezleme veya sematik simülatörüne yeni algoritmalar dahil edebilir,
* Yeni makamlar veya frekans veri setleri önerebilirsiniz.

Katkı sağlamak için lütfen bir **Pull Request (PR)** açın ya da bir **Issue** oluşturun.

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) altında açık kaynaklı olarak sunulmuştur. Özgürce inceleyebilir, geliştirebilir ve paylaşabilirsiniz.