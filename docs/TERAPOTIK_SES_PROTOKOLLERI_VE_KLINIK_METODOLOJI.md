# Terapötik Ses Protokolleri ve Klinik Metodoloji Kılavuzu

> *"Gök cisimlerinin devirlerinden ve kürelerin hareketlerinden çıkan nağmeler, insan ruhunun asıl vatanındaki ilahi armoninin yeryüzündeki yankısıdır. Hekim, hastanın nabzındaki aksaklığı müziğin usulüyle teşhis eder ve bozulan mizacı uygun makamla dengeye kavuşturur."*  
> — **Ebû Nasr el-Fârâbî**, *Kitâbü'l-Mûsîka'l-Kebîr* (Büyük Musiki Kitabı, 950 civarı)

---

## 1. Giriş ve Terapötik Çerçeve

**Titresim v2.0**, kadim Doğu şifahane geleneğinin (Darüşşifa musiki tıbbı) derin bilgeliği ile modern nöro-akustik beyin dalgası sürükleme (*brainwave entrainment*) prensiplerini çok aşamalı klinik seans motorunda birleştiren profesyonel bir akustik rezonans platformudur.

Klinik ses terapisinin temel gayesi; otonom sinir sisteminde sempatik (savaş ya da kaç) baskınlığı kırarak, **parasempatik (dinlen ve onar / rest & digest)** aktivasyonu tetiklemek, vagal tonusu artırmak ve beyin yarıküreleri arasındaki elektroensefalografik (EEG) senkronizasyonu (hemisferik koherans) sağlamaktır.

```
       [AKUSTİK UYARAN]
   Binaural / İzokronik / Makam
              │
              ▼
   [NÖRONAL SÜRÜKLEME (ENTRAINMENT)]
   Superior Olivary Complex & Talamus
              │
              ▼
   [OTONOM SİNİR SİSTEMİ REGÜLASYONU]
   Sempatik Baskılama ──► Vagal Tonus Artışı (0.1 Hz)
              │
              ▼
   [KLİNİK & BİLİŞSEL SONUÇ]
   Stres Redüksiyonu, Derin Uyku, Odaklanma & Hücresel Onarım
```

<p align="center">
  <img src="../assets/heart_coherence_01hz.svg" alt="0.1 Hz Kalp Hızı Değişkenliği ve Vagal Senkronizasyon" width="100%">
</p>

<p align="center">
  <img src="../assets/brainwave_entrainment_spectrum.svg" alt="EEG Beyin Dalgaları & Binaural Sürükleme" width="100%">
</p>

---

## 2. Tarihsel ve Bilimsel Literatürden Alıntılar

### 2.1. İbn Sînâ (Avicenna) — El-Kânûn fi't-Tıbb (Tıp Kanunu, 1025)
> *"Tedavinin en iyi ve en tesirli yollarından biri, hastanın aklî ve ruhî kuvvetlerini artırmak, ona cesaret vermek, onu musiki dinlemeye teşvik etmek ve onu sevdiği insanlarla bir araya getirmektir. Melodilerin ses perdelerindeki iniş ve çıkışlar, kanın damarlardaki nabazanına denk düştüğünde, bedendeki dört hılt (kan, balgam, safra, sevda) arasındaki itidal kendiliğinden hasıl olur."*  
> — **İbn Sînâ**, *El-Kânûn fi't-Tıbb*, Cilt I.

### 2.2. Evliya Çelebi — Seyahatnâme (Edirne Sultan II. Bayezid Darüşşifası, 1653)
> *"Merhum ve mağfur Sultan Bayezid-i Veli vakfiyesinde şart kılmış ki: On adet usta hanende ve sazende gulâm tayin oluna; haftada üç gün hastalara ve mecnunlara gelip musiki faslı ile neva, rast, nihavend, hicaz, hüseyni ve ırak makamlarında nağmeler eyleyeler. Zira nice dertlilere bu fasıllar tiryak ve şifa olur. Delilerin nicesi bu nağmelerle sakinleşip aklı başına gelir, hastaların yüzüne kan yürür."*  
> — **Evliya Çelebi**, *Seyahatnâme*, 3. Cilt.

### 2.3. Gevrekzade Hasan Efendi — Râhatu'l-Ervâh (Ruhların Rahatı, 18. Yüzyıl)
> *"Her makamın bedende ve nefiste bir tesiri ve hükmettiği bir vakit vardır:  
> - **Rast Makamı:** Seher vaktinde ve safra galebe çaldığında dinletilirse felç ve nüzullere dermandır, zihne kuvvet ve neşe verir.  
> - **Nihavend Makamı:** Öğle vakti tansiyonu ve kan basıncını teskin eder, hüzün ve kederi defeyler.  
> - **Hicaz Makamı:** Yatsıdan sonra uykusuzluk çekenlere, kuruntulu ve vesveseli dimağlara derin sükunet ve tefekkür bağışlar.  
> - **Uşşak Makamı:** İkindi vakti kalp sıkıntılarına, ayak ağrılarına ve uykusuzluğa şifadır."*  
> — **Gevrekzade Hâfız Hasan Efendi**, *Emrâz-ı Ruhâniyye ve Tabâbet-i Mûsikiyye*.

### 2.4. Modern Nöro-Akustik Literatür: Oster ve Monroe
> *"When two tones of slightly different frequencies are presented separately, one to each ear, the subject perceives a third, pulsating sound called a binaural beat. The sensation arises in the superior olivary nucleus of the brainstem, where the inputs from both ears first converge. These beats have the remarkable capacity to drive the electrical rhythm of the cortex into resonance at the beat frequency."*  
> — **Dr. Gerald Oster**, *"Auditory Beats in the Brain"*, *Scientific American*, Vol. 229, No. 4, pp. 94-102 (1973).

> *"Hemispheric Synchronization (Hemi-Sync) occurs when both hemispheres of the brain reflect identical electrical wave patterns simultaneously. By inducing specific beat differentials, the mind accesses altered states of expanded awareness, profound physical relaxation, and accelerated learning that normally require decades of Zen or Yogic meditation."*  
> — **Robert A. Monroe**, *Journeys Out of the Body* / *Far Journeys* (1985).

---

## 3. Çok Aşamalı Seans Motoru Mimarisi (`session.py`)

Titresim v2.0 içindeki `TherapySessionEngine`, tekil durağan frekanslar yerine, zaman içinde faz ve genlik sürekliliği korunarak aşamadan aşamaya yumuşakça akan dinamik protokoller uygular.

### 3.1. Çapraz Geçiş (Equal-Power Cross-Fading)
İki aşama arasındaki geçişte ani frekans sıçramaları ve "klik" seslerini önlemek amacıyla **Eşit Güç (Equal-Power)** sinüzoidal pencereleme formülü uygulanır:

$$\text{Weight}_A(t) = \cos\left(\frac{\pi}{2} \cdot \frac{t - t_{\text{start}}}{\tau}\right), \quad \text{Weight}_B(t) = \sin\left(\frac{\pi}{2} \cdot \frac{t - t_{\text{start}}}{\tau}\right)$$

Burada $\tau$ geçiş süresidir ($2.0 \sim 3.0$ saniye). Bu sayede toplam algılanan ses enerjisi $\text{Power} = W_A^2 + W_B^2 = \cos^2\theta + \sin^2\theta = 1.0$ sabit kalarak beynin sürüklenme sürekliliği bozulmaz.

---

## 4. Yerleşik Klinik Protokoller

| Protokol Adı | Toplam Süre | Aşamalar (Seyir) | Taşıyıcı / Fark Frekansları | Arka Plan Gürültüsü | Terapötik Endikasyon |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Derin Uyku İndüksiyonu** | 20 Dk (Örnek: 1200s) | Alfa İnişi $\to$ Teta Eşiği $\to$ Delta Derin Uyku $\to$ Kozmik Sönüm | $216 \text{ Hz} \to 144 \text{ Hz}$<br>Fark: $8 \text{ Hz} \to 4.5 \text{ Hz} \to 1.5 \text{ Hz} \to 0.5 \text{ Hz}$ | Kahverengi (Brownian) & Pembe | Kronik uykusuzluk, REM uyku bozukluğu, gece uyanmaları. |
| **Derin Odaklanma (Flow State)** | 25 Dk (1500s) | Zihinsel Arınma $\to$ Alfa/SMR $\to$ Yüksek Teta $\to$ Gama Parlaması | $432 \text{ Hz}$ & $528 \text{ Hz}$<br>Fark: $12 \text{ Hz} \to 14 \text{ Hz} \to 7.83 \text{ Hz} \to 40 \text{ Hz}$ | Pembe Gürültü ($1/f$) | Kodlama, matematiksel analiz, yaratıcı yazarlık, DEHB/ADHD. |
| **Darüşşifa Anksiyete Dengeleme** | 18 Dk (1080s) | Nihavend Teskini $\to$ Rast Denge $\to$ Schumann Kalp $\to$ İtidal | $220 \text{ Hz} \to 136.1 \text{ Hz}$ (Om)<br>Fark: $10 \text{ Hz} \to 7.83 \text{ Hz} \to 6.0 \text{ Hz}$ | Pembe Gürültü + Doğal Su Akışı | Panik atak, genel anksiyete, zihinsel ajitasyon, yüksek kortizol. |
| **Kalp Koheransı (0.1 Hz Vagal)** | 15 Dk (900s) | Diyafram Solunumu $\to$ Vagal Kilitlenme $\to$ Kardiyak Senkroni | $528 \text{ Hz}$ & $639 \text{ Hz}$<br>İzokronik Modülasyon: $0.10 \text{ Hz}$ | Saf Pembe Gürültü | Kalp Hızı Değişkenliği (HRV) düşüklüğü, hipertansiyon, tükenmişlik. |
| **Hücresel Yenilenme & Detoks** | 22 Dk (1320s) | 396 Hz Salınım $\to$ 417 Hz Dönüşüm $\to$ 528 Hz Onarım $\to$ 741 Hz Arınma | Solfeggio Merdiveni ($396 \to 417 \to 528 \to 741 \text{ Hz}$)<br>Fark: $7.83 \text{ Hz}$ Schumann | Kahverengi Gürültü | Kronik yorgunluk, hücresel stres, zihinsel toksisite ve arınma. |

---

## 5. Uygulama Talimatları ve Hasta Güvenliği

1. **Kulaklık Gerekliliği:** Binaural beat etkisinin oluşması için stereofonik ayrım şarttır. Dinleyicinin yüksek çözünürlüklü stereo kulaklık kullanması gerekir.
2. **Ses Şiddeti Düzeyi:** Ses basınç seviyesi $55 \sim 65 \text{ dBA}$ aralığında (rahat bir fısıltı ile normal konuşma arası) tutulmalıdır. Aşırı ses kulak yorgunluğuna ve sempatik aktivasyona yol açar.
3. **Kontrendikasyonlar:**
   - Epilepsi veya fotik/akustik nöbet geçmişi olan bireylerde 15 Hz üzeri izokronik vuruşlar hekim onayı olmadan uygulanmamalıdır.
   - Taşıt veya iş makinesi kullanırken **Derin Uyku** veya **Derin Teta** seansları kesinlikle dinlenmemelidir.
