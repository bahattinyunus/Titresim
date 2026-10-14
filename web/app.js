/**
 * Titreşim: Evrensel Ses, Kutsal Kelâm ve Frekans Terapisi Laboratuvarı
 * Web Audio API & Canlı Chladni Cymatics Simülasyon Motoru
 */

// ==========================================
// 1. DAHİLİ VERİLER (DATASETS)
// ==========================================
const SOLFEGGIO_DATA = [
  { freq: 174, name: "Doğal Anestezi & Güven", note: "F", chakra: "Kök (Alt)", desc: "Fiziksel bedendeki ağrı ve gerginliği yatıştırır, organlara rahatlama aşılar." },
  { freq: 285, name: "Hücresel Yenilenme", note: "C#", chakra: "Kök Çakra", desc: "Hasarlı doku ve hücrelerin orijinal frekans koduna dönmesini destekler." },
  { freq: 396, name: "Ut - Korkudan Özgürleşme", note: "G", chakra: "Kök (Muladhara)", desc: "Bilinçaltındaki suçluluk, keder ve korku blokajlarını toprağa aktarır." },
  { freq: 417, name: "Re - Değişim & Travma Şifası", note: "G#", chakra: "Sakral (Svadhisthana)", desc: "Geçmiş travmaları temizler, yeni başlangıçlar için alan açar." },
  { freq: 528, name: "Mi - Aşk Frekansı & DNA", note: "C", chakra: "Solar Pleksus", desc: "Doğanın ve biyolojinin temel şifa tonu; su moleküllerini altıgen dizer." },
  { freq: 639, name: "Fa - Bağ Kurma & Kalp", note: "D#", chakra: "Kalp (Anahata)", desc: "Empati, hoşgörü, ailevi ve toplumsal bağları pekiştirir." },
  { freq: 741, name: "Sol - Sezgi & Arınma", note: "F#", chakra: "Boğaz (Vishuddha)", desc: "Beden ve zihni toksinlerden arındırır, ifade gücünü ve sezgileri açar." },
  { freq: 852, name: "La - Ruhsal Düzen", note: "G#", chakra: "Üçüncü Göz (Ajna)", desc: "İçgörü, basiret ve ruhsal uyanışı keskinleştirir." },
  { freq: 963, name: "Si - İlahi Birlik", note: "B", chakra: "Taç (Sahasrara)", desc: "Epifiz bezini uyararak mutlak birlik ve tefekkür halleri doğurur." }
];

const MAKAM_DATA = [
  {
    id: "rast",
    name: "Rast Makamı",
    root: "G (Sol - Rast)",
    time: "Gece sonu ile seher vakti arası, güneş doğarken",
    element: "Ateş (Sıcak & Kuru) / Koç",
    organ: "Baş, beyin, gözler ve kemikler",
    effects: ["İnsana sefa, neşe, iç huzuru ve canlılık verir.", "Felç, kas seğirmeleri ve sara illetine şifadır.", "Zihni berraklaştırır."],
    quote: "Farabi: 'Rast makamı insana sefa (huzur ve neşe) bağışlar.'",
    ratios: [1.0, 1.125, 1.25, 1.333, 1.5, 1.687, 1.875, 2.0]
  },
  {
    id: "rehavi",
    name: "Rehavi Makamı",
    root: "G (Sol)",
    time: "Seher vakti (fecir doğuşu)",
    element: "Su (Soğuk & Nemli) / Balık",
    organ: "Burun, boğaz, göğüs ve mide",
    effects: ["İnsana sonsuzluk ve azamet hissi verir.", "Şiddetli baş ağrısı (migren) ve burun kanamasına devadır.", "Ağlayan çocukları sakinleştirir."],
    quote: "Farabi: 'Rehavi makamı insana beka (sonsuzluk) fikri telkin eder.'",
    ratios: [1.0, 1.066, 1.25, 1.333, 1.5, 1.6, 1.875, 2.0]
  },
  {
    id: "nihavend",
    name: "Nihavend Makamı",
    root: "G (Sol) / C (Do)",
    time: "Öğle ile ikindi arası",
    element: "Toprak (Kuru & Soğuk) / Oğlak",
    organ: "Kalp, kan dolaşımı, tansiyon dengesi",
    effects: ["Huzur, dinginlik ve derin sevgi duyguları uyandırır.", "Yüksek tansiyonu düşürür, hızlı nabzı yatıştırır.", "Böbrek sancılarını dindirir."],
    quote: "Darüşşifalarda nabzı hızlı hastalara dinletilerek kalp atışı dengelenirdi.",
    ratios: [1.0, 1.125, 1.2, 1.333, 1.5, 1.6, 1.875, 2.0]
  },
  {
    id: "hicaz",
    name: "Hicaz Makamı",
    root: "A (La - Dügah)",
    time: "Yatsı vakti ile gece yarısı",
    element: "Ateş (Sıcak & Kuru) / Yay",
    organ: "Karaciğer, böbrekler ve idrar yolları",
    effects: ["İnsana tevazu ve derin manevi duyarlılık verir.", "Böbrek taşlarının dökülmesine ve sancıların dinmesine yardım eder.", "Ateşi düşürür."],
    quote: "Farabi: 'Hicaz makamı dinleyene tevazu ve huşu telkin eder.'",
    ratios: [1.0, 1.053, 1.265, 1.333, 1.5, 1.58, 1.875, 2.0]
  },
  {
    id: "buselik",
    name: "Buselik Makamı",
    root: "A (La - Dügah)",
    time: "Kuşluk vakti (öğleden önce)",
    element: "Hava (Sıcak & Nemli) / İkizler",
    organ: "Kalp, göğüs, boyun ve kaslar",
    effects: ["Kuvvet, cesaret ve dirayet aşılar.", "Boyun ve kas tutulmalarını çözer, kan dolaşımını canlandırır.", "Zihinsel yorgunluğu giderir."],
    quote: "Farabi: 'Buselik insana kuvvet ve dirayet hissi kazandırır.'",
    ratios: [1.0, 1.125, 1.2, 1.333, 1.5, 1.6, 1.777, 2.0]
  },
  {
    id: "huseyni",
    name: "Hüseyni Makamı",
    root: "A (La - Dügah)",
    time: "Sabah vakti ve gün batımı",
    element: "Toprak (Soğuk & Kuru) / Boğa",
    organ: "Karaciğer, safra kesesi ve mide",
    effects: ["Sükunet ve içsel emniyet telkin eder.", "Karaciğer hararetini ve mide yanmasını yatıştırır.", "Öfke patlamalarını dindirir."],
    quote: "Farabi: 'Hüseyni makamı insana sükun ve vakar bahşeder.'",
    ratios: [1.0, 1.125, 1.22, 1.333, 1.5, 1.6, 1.777, 2.0]
  },
  {
    id: "ussak",
    name: "Uşşak Makamı",
    root: "A (La - Dügah)",
    time: "Öğle vakti ve ikindi sonu",
    element: "Ateş (Sıcak & Nemli) / Terazi",
    organ: "Ayaklar, eklemler, gut ve romatizma",
    effects: ["Gülme, sevinç ve aşk duyguları doğurur.", "Ayak ağrılarına ve mafsal sızılarına iyi gelir.", "Derin uyku isteği uyandırır."],
    quote: "Farabi: 'Uşşak makamı insana gülme (neşelenme) hali aşılar.'",
    ratios: [1.0, 1.11, 1.23, 1.333, 1.5, 1.62, 1.777, 2.0]
  },
  {
    id: "neva",
    name: "Neva Makamı",
    root: "D (Re - Neva)",
    time: "Akşam vakti",
    element: "Hava / Kova",
    organ: "Kalça, omurilik ve zihin",
    effects: ["Cesaret ve ferahlık hissi verir.", "Siyatik ağrılarını dindirir, taşkın delilik hallerini yatıştırır.", "Ruhsal gerilimi boşaltır."],
    quote: "Evliya Çelebi: 'Edirne Darüşşifası'nda akıl hastaları bu makamla sükuna ererdi.'",
    ratios: [1.0, 1.125, 1.25, 1.333, 1.5, 1.687, 1.777, 2.0]
  }
];

const TRADITIONS_DATA = [
  {
    tradition: "İslam Kıraat ve Zikir Geleneği",
    practice: "Kur'an Tecvidi, Gunne & Esma Zikri",
    principles: [
      "Gunne (geniz sesi) burun sinüslerinde rezonans oluşturarak nitrik oksit (NO) salınımını 15 kata kadar arttırır.",
      "Kalkale (patlamalı harfler) beyinde mikro-akustik uyanış şokları üretir.",
      "Medd (sesi uzatma) parasempatik vagal tonusu optimize ederek solunumu 0.1 Hz ritmine kilitler."
    ],
    effects: "Frontal EEG'de belirgin Alfa (8-12 Hz) ve Teta (4-7 Hz) yükselişi; kortizol düşüşü ve kalp koheransı."
  },
  {
    tradition: "Vedik ve Hint Geleneği",
    practice: "Pranava Mantra (Om / Aum)",
    principles: [
      "A-U-M heceleri karnın altından başın tepesine kadar dikey bir titreşim sütunu kurar.",
      "136.1 Hz frekansı Dünya Yılı döngüsünün 32. oktavıdır.",
      "Vagus sinirini uyararak limbik sistemdeki amigdala alarmını kapatır."
    ],
    effects: "Default Mode Network (DMN) gevezeliğini susturur; derin meditatif sükunet (Dhyana)."
  },
  {
    tradition: "Batı Manastır Geleneği",
    practice: "Gregoryen İlahileri (Gregorian Chants)",
    principles: [
      "Monofonik (tek sesli) yapı ve Gotik katedrallerin 5-7 saniyelik yankılanma kubbesi.",
      "Solfeggio serisindeki kutsal oranlar ve saf akort (Just Intonation)."
    ],
    effects: "Dr. Alfred Tomatis'e göre kulak salyangozunu doğrudan şarj ederek korteksi uyanık tutar."
  },
  {
    tradition: "Tibet & Şamanik Gelenek",
    practice: "Tibet Çanakları & Ritmik Şaman Davulu",
    principles: [
      "Alaşım çanakların mikrotonal vuruşları doğal binaural beat dalgaları oluşturur.",
      "Şaman davulunun 4-7 Hz (dakikada 240-300 vuruş) ritmi beyni Teta bandına sürükler."
    ],
    effects: "Anlık bilişsel stres çözülmesi, vizyoner rüya bilinci ve derin hücresel masaj."
  }
];

// ==========================================
// 2. SES MOTORU (WEB AUDIO API)
// ==========================================
class AudioEngine {
  constructor() {
    this.ctx = null;
    this.masterGain = null;
    this.analyser = null;

    // Tekli ton osilatörü
    this.singleOsc = null;
    this.singleGain = null;
    this.isPlayingSingle = false;

    // Binaural osilatörleri
    this.leftOsc = null;
    this.rightOsc = null;
    this.binauralGain = null;
    this.isPlayingBinaural = false;

    // Makam sekans durumu
    this.makamTimeouts = [];
  }

  init() {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioCtx();

      this.masterGain = this.ctx.createGain();
      this.masterGain.gain.setValueAtTime(0.5, this.ctx.currentTime);

      this.analyser = this.ctx.createAnalyser();
      this.analyser.fftSize = 512;

      this.masterGain.connect(this.analyser);
      this.analyser.connect(this.ctx.destination);
    }
    if (this.ctx.state === "suspended") {
      this.ctx.resume();
    }
  }

  playTone(freq, type = "sine") {
    this.init();
    this.stopTone();
    this.stopBinaural();

    this.singleOsc = this.ctx.createOscillator();
    this.singleGain = this.ctx.createGain();

    this.singleOsc.type = type;
    this.singleOsc.frequency.setValueAtTime(freq, this.ctx.currentTime);

    // Zarf (Fade in)
    this.singleGain.gain.setValueAtTime(0, this.ctx.currentTime);
    this.singleGain.gain.linearRampToValueAtTime(0.4, this.ctx.currentTime + 0.1);

    this.singleOsc.connect(this.singleGain);
    this.singleGain.connect(this.masterGain);

    this.singleOsc.start();
    this.isPlayingSingle = true;

    updateAudioStatus(true, `${freq.toFixed(1)} Hz Ton Çalıyor`);
  }

  stopTone() {
    if (this.singleOsc) {
      try {
        const now = this.ctx.currentTime;
        this.singleGain.gain.linearRampToValueAtTime(0.001, now + 0.1);
        setTimeout(() => {
          if (this.singleOsc) {
            this.singleOsc.stop();
            this.singleOsc.disconnect();
            this.singleOsc = null;
          }
        }, 110);
      } catch (e) {
        this.singleOsc = null;
      }
    }
    this.isPlayingSingle = false;
    this.stopMakamScale();
    updateAudioStatus(false);
  }

  playBinaural(carrier, beat) {
    this.init();
    this.stopTone();
    this.stopBinaural();

    const leftFreq = carrier - (beat / 2);
    const rightFreq = carrier + (beat / 2);

    this.leftOsc = this.ctx.createOscillator();
    this.rightOsc = this.ctx.createOscillator();
    this.binauralGain = this.ctx.createGain();

    this.leftOsc.frequency.setValueAtTime(leftFreq, this.ctx.currentTime);
    this.rightOsc.frequency.setValueAtTime(rightFreq, this.ctx.currentTime);

    // Stereo Kanal Birleştirici
    const merger = this.ctx.createChannelMerger(2);
    this.leftOsc.connect(merger, 0, 0); // Sol kanal
    this.rightOsc.connect(merger, 0, 1); // Sağ kanal

    this.binauralGain.gain.setValueAtTime(0, this.ctx.currentTime);
    this.binauralGain.gain.linearRampToValueAtTime(0.35, this.ctx.currentTime + 0.3);

    merger.connect(this.binauralGain);
    this.binauralGain.connect(this.masterGain);

    this.leftOsc.start();
    this.rightOsc.start();
    this.isPlayingBinaural = true;

    updateAudioStatus(true, `Binaural: ${beat.toFixed(1)} Hz (Taşıyıcı: ${carrier} Hz)`);
  }

  stopBinaural() {
    if (this.leftOsc && this.rightOsc) {
      try {
        const now = this.ctx.currentTime;
        this.binauralGain.gain.linearRampToValueAtTime(0.001, now + 0.15);
        setTimeout(() => {
          if (this.leftOsc) {
            this.leftOsc.stop();
            this.leftOsc.disconnect();
            this.leftOsc = null;
          }
          if (this.rightOsc) {
            this.rightOsc.stop();
            this.rightOsc.disconnect();
            this.rightOsc = null;
          }
        }, 160);
      } catch (e) {
        this.leftOsc = null;
        this.rightOsc = null;
      }
    }
    this.isPlayingBinaural = false;
    updateAudioStatus(false);
  }

  playMakamScale(makam, baseFreq = 220) {
    this.init();
    this.stopTone();
    this.stopBinaural();
    this.stopMakamScale();

    const freqs = makam.ratios.map(r => baseFreq * r);
    const noteDuration = 0.8; // saniye

    freqs.forEach((freq, idx) => {
      const timeoutId = setTimeout(() => {
        this.playPluckNote(freq, noteDuration * 0.95);
        // Cymatics simülatörünü güncelle
        cymaticsSim.setFrequency(freq);
      }, idx * noteDuration * 1000);
      this.makamTimeouts.push(timeoutId);
    });

    // Bitişte durumu sıfırla
    const finalTimeout = setTimeout(() => {
      updateAudioStatus(false);
    }, freqs.length * noteDuration * 1000);
    this.makamTimeouts.push(finalTimeout);

    updateAudioStatus(true, `${makam.name} İcra Ediliyor...`);
  }

  playPluckNote(freq, duration) {
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();

    osc.type = "sine";
    osc.frequency.setValueAtTime(freq, this.ctx.currentTime);

    // Ney / tambur benzeri yumuşak zarf
    const now = this.ctx.currentTime;
    gain.gain.setValueAtTime(0, now);
    gain.gain.linearRampToValueAtTime(0.4, now + 0.05);
    gain.gain.exponentialRampToValueAtTime(0.001, now + duration);

    osc.connect(gain);
    gain.connect(this.masterGain);

    osc.start(now);
    osc.stop(now + duration + 0.05);
  }

  stopMakamScale() {
    this.makamTimeouts.forEach(id => clearTimeout(id));
    this.makamTimeouts = [];
  }
}

const audio = new AudioEngine();

// ==========================================
// 3. CANLI CHLADNI SEMATİK (CYMATICS) MOTORU
// ==========================================
class CymaticsSimulation {
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext("2d");
    this.numParticles = 2800;
    this.particles = [];

    this.n = 3;
    this.m = 5;
    this.a = 1.0;
    this.b = 1.0;
    this.currentFreq = 432.0;

    this.initParticles();
    this.animate = this.animate.bind(this);
    requestAnimationFrame(this.animate);
  }

  initParticles() {
    this.particles = [];
    const w = this.canvas.width;
    const h = this.canvas.height;
    for (let i = 0; i < this.numParticles; i++) {
      this.particles.push({
        x: (Math.random() - 0.5) * 0.96, // [-0.48, 0.48]
        y: (Math.random() - 0.5) * 0.96,
        vx: (Math.random() - 0.5) * 0.002,
        vy: (Math.random() - 0.5) * 0.002,
        size: Math.random() < 0.2 ? 1.8 : 1.2,
        colorHue: Math.random() < 0.15 ? 195 : 42 // Altın & Turkuaz
      });
    }
  }

  setModes(n, m) {
    this.n = n;
    this.m = m;
    document.getElementById("modeBadge").innerText = `Mod: n=${n}, m=${m}`;
    document.getElementById("nVal").innerText = n;
    document.getElementById("mVal").innerText = m;
  }

  setFrequency(freq) {
    this.currentFreq = freq;
    document.getElementById("currentFreqBadge").innerText = `${freq.toFixed(1)} Hz`;

    // Frekansa göre dinamik modal harmonikler hesapla
    let newN = 3, newM = 5;
    if (freq < 150) { newN = 1; newM = 2; }
    else if (freq < 250) { newN = 2; newM = 3; }
    else if (freq < 380) { newN = 3; newM = 4; }
    else if (freq < 500) { newN = 3; newM = 5; }
    else if (freq < 650) { newN = 4; newM = 6; }
    else if (freq < 800) { newN = 5; newM = 7; }
    else { newN = 6; newM = 8; }

    this.setModes(newN, newM);
    document.getElementById("chladniN").value = newN;
    document.getElementById("chladniM").value = newM;
  }

  // Chladni modal genlik fonksiyonu w(x, y)
  evaluateW(x, y) {
    const pi = Math.PI;
    const term1 = Math.cos(this.n * pi * x) * Math.cos(this.m * pi * y);
    const term2 = Math.cos(this.m * pi * x) * Math.cos(this.n * pi * y);
    return this.a * term1 - this.b * term2;
  }

  animate() {
    const ctx = this.ctx;
    const w = this.canvas.width;
    const h = this.canvas.height;
    const halfW = w / 2;
    const halfH = h / 2;

    // Arka planı hafif silme (Motion blur efekti)
    ctx.fillStyle = "rgba(6, 9, 17, 0.25)";
    ctx.fillRect(0, 0, w, h);

    const isAudioActive = audio.isPlayingSingle || audio.isPlayingBinaural || audio.makamTimeouts.length > 0;
    const agitation = isAudioActive ? 0.0035 : 0.001;
    const forceFactor = isAudioActive ? 0.0006 : 0.0002;

    // Parçacıkları güncelle ve çiz
    for (let i = 0; i < this.particles.length; i++) {
      const p = this.particles[i];

      // Genlik ve gradyan hesapla
      const val = this.evaluateW(p.x, p.y);
      const absVal = Math.abs(val);

      // Sayısal türevle gradyan bul
      const eps = 0.01;
      const gradX = (Math.abs(this.evaluateW(p.x + eps, p.y)) - absVal) / eps;
      const gradY = (Math.abs(this.evaluateW(p.x, p.y + eps)) - absVal) / eps;

      // Parçacıklar genliğin sıfır olduğu (düğüm) çizgilere doğru itilir
      p.vx -= gradX * forceFactor;
      p.vy -= gradY * forceFactor;

      // Rastgele akustik titreşim (termal Brownian hareketi)
      p.vx += (Math.random() - 0.5) * agitation * absVal;
      p.vy += (Math.random() - 0.5) * agitation * absVal;

      // Sürtünme
      p.vx *= 0.94;
      p.vy *= 0.94;

      p.x += p.vx;
      p.y += p.vy;

      // Sınırlar
      if (p.x < -0.48) { p.x = -0.48; p.vx *= -0.5; }
      if (p.x > 0.48) { p.x = 0.48; p.vx *= -0.5; }
      if (p.y < -0.48) { p.y = -0.48; p.vy *= -0.5; }
      if (p.y > 0.48) { p.y = 0.48; p.vy *= -0.5; }

      // Ekrana yansıt
      const scrX = halfW + p.x * (w - 20);
      const scrY = halfH + p.y * (h - 20);

      // Renk ve parlaklık: Düğüm çizgisine yaklaştıkça parlar
      ctx.beginPath();
      ctx.arc(scrX, scrY, p.size, 0, Math.PI * 2);
      if (absVal < 0.15) {
        ctx.fillStyle = p.colorHue === 42 ? "#fbbf24" : "#38bdf8"; // Tam rezonans
      } else {
        ctx.fillStyle = "rgba(148, 163, 184, 0.4)";
      }
      ctx.fill();
    }

    requestAnimationFrame(this.animate);
  }
}

let cymaticsSim = null;

// ==========================================
// 4. OSİLOSKOP / DALGA ANALİZÖRÜ
// ==========================================
function startOscilloscope() {
  const canvas = document.getElementById("scopeCanvas");
  const ctx = canvas.getContext("2d");
  const bufferLength = 256;
  const dataArray = new Uint8Array(bufferLength);

  function drawScope() {
    requestAnimationFrame(drawScope);

    ctx.fillStyle = "#05080e";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    if (audio.analyser && (audio.isPlayingSingle || audio.isPlayingBinaural || audio.makamTimeouts.length > 0)) {
      audio.analyser.getByteTimeDomainData(dataArray);

      ctx.lineWidth = 2;
      ctx.strokeStyle = "#f59e0b";
      ctx.beginPath();

      const sliceWidth = canvas.width / bufferLength;
      let x = 0;

      for (let i = 0; i < bufferLength; i++) {
        const v = dataArray[i] / 128.0;
        const y = (v * canvas.height) / 2;

        if (i === 0) {
          ctx.moveTo(x, y);
        } else {
          ctx.lineTo(x, y);
        }
        x += sliceWidth;
      }
      ctx.stroke();
    } else {
      // Düz çizgi (hazırda bekleme)
      ctx.strokeStyle = "rgba(148, 163, 184, 0.25)";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(0, canvas.height / 2);
      ctx.lineTo(canvas.width, canvas.height / 2);
      ctx.stroke();
    }
  }

  drawScope();
}

// ==========================================
// 5. ARAYÜZ (UI) BAĞLANTILARI
// ==========================================
function updateAudioStatus(isPlaying, text = "Ton Çalıyor") {
  const badge = document.getElementById("audioStatusBadge");
  const toggleBtn = document.getElementById("toggleAudioBtn");

  if (isPlaying) {
    badge.className = "status-badge active";
    badge.innerText = `● ${text}`;
    toggleBtn.innerText = "Sesi Durdur";
    toggleBtn.classList.replace("btn-primary", "btn-secondary");
  } else {
    badge.className = "status-badge ready";
    badge.innerText = "Ses Motoru: Hazır";
    toggleBtn.innerText = "Tonu Başlat / Durdur";
    toggleBtn.classList.replace("btn-secondary", "btn-primary");
  }
}

// Solfeggio Kartlarını Render Et
function renderSolfeggio() {
  const grid = document.getElementById("solfeggioGrid");
  grid.innerHTML = "";

  SOLFEGGIO_DATA.forEach(item => {
    const card = document.createElement("div");
    card.className = "solf-card";
    card.innerHTML = `
      <div class="solf-card-top">
        <span class="solf-freq">${item.freq} Hz</span>
        <span class="solf-note">${item.note}</span>
      </div>
      <div class="solf-name">${item.name}</div>
      <div class="solf-chakra">🔹 ${item.chakra}</div>
      <div class="solf-desc">${item.desc}</div>
    `;

    card.addEventListener("click", () => {
      document.querySelectorAll(".solf-card").forEach(c => c.classList.remove("playing"));
      if (audio.isPlayingSingle && cymaticsSim.currentFreq === item.freq) {
        audio.stopTone();
      } else {
        card.classList.add("playing");
        audio.playTone(item.freq);
        cymaticsSim.setFrequency(item.freq);
      }
    });

    grid.appendChild(card);
  });
}

// Makamları Render Et
function renderMakamlar() {
  const select = document.getElementById("makamSelect");
  select.innerHTML = "";

  MAKAM_DATA.forEach(m => {
    const opt = document.createElement("option");
    opt.value = m.id;
    opt.innerText = `${m.name} (${m.root})`;
    select.appendChild(opt);
  });

  function updateMakamDetail(id) {
    const makam = MAKAM_DATA.find(m => m.id === id) || MAKAM_DATA[0];
    const container = document.getElementById("makamDetailCard");
    container.innerHTML = `
      <div class="makam-detail-header">
        <h3>${makam.name}</h3>
        <p class="subtitle">Temel Karar Perdesi: <strong>${makam.root}</strong></p>
      </div>
      <div class="makam-info-grid">
        <div class="makam-tag"><strong>Vakti:</strong> ${makam.time}</div>
        <div class="makam-tag"><strong>Element & Burç:</strong> ${makam.element}</div>
        <div class="makam-tag" style="grid-column: span 2;"><strong>Şifa Organı:</strong> ${makam.organ}</div>
      </div>
      <div class="makam-effects-title"><strong>Terapötik Tesirleri:</strong></div>
      <ul class="makam-effects-list">
        ${makam.effects.map(e => `<li>${e}</li>`).join("")}
      </ul>
      <div class="makam-notes-quote">${makam.quote}</div>
      <div class="makam-action mt-3">
        <button id="playMakamBtn" class="btn btn-primary">🎶 Makam Dizisini Dinle (Şifa Arpeji)</button>
      </div>
    `;

    document.getElementById("playMakamBtn").addEventListener("click", () => {
      audio.playMakamScale(makam);
    });
  }

  select.addEventListener("change", (e) => updateMakamDetail(e.target.value));
  updateMakamDetail(MAKAM_DATA[0].id);
}

// Kutsal Gelenekleri Render Et
function renderTraditions() {
  const list = document.getElementById("traditionsList");
  list.innerHTML = "";

  TRADITIONS_DATA.forEach(t => {
    const div = document.createElement("div");
    div.className = "tradition-card";
    div.innerHTML = `
      <h3>${t.tradition}</h3>
      <div class="tradition-practice">📿 Pratik: <strong>${t.practice}</strong></div>
      <ul class="tradition-list">
        ${t.principles.map(p => `<li>${p}</li>`).join("")}
      </ul>
      <p class="mt-2" style="font-size: 12px; color: #a5f3fc;">🧠 <strong>Nörobiyolojik Etki:</strong> ${t.effects}</p>
    `;
    list.appendChild(div);
  });
}

// Nefes Rehberi Mantığı (0.1 Hz / Coherent Breathing)
let breathInterval = null;
let isBreathingActive = false;

function setupBreathing() {
  const circle = document.getElementById("breathingCircle");
  const text = document.getElementById("breathText");
  const btn = document.getElementById("toggleBreathBtn");

  btn.addEventListener("click", () => {
    if (isBreathingActive) {
      clearInterval(breathInterval);
      circle.className = "breathing-circle";
      text.innerText = "Hazır";
      btn.innerText = "Nefes Rehberini Başlat";
      isBreathingActive = false;
    } else {
      isBreathingActive = true;
      btn.innerText = "Nefes Rehberini Durdur";

      let isInhaling = true;
      circle.className = "breathing-circle inhale";
      text.innerText = "Nefes Al (5.5s)";

      breathInterval = setInterval(() => {
        isInhaling = !isInhaling;
        if (isInhaling) {
          circle.className = "breathing-circle inhale";
          text.innerText = "Nefes Al (5.5s)";
        } else {
          circle.className = "breathing-circle exhale";
          text.innerText = "Nefes Ver (5.5s)";
        }
      }, 5500);
    }
  });
}

// ==========================================
// 6. BAŞLATICI (INITIALIZATION)
// ==========================================
document.addEventListener("DOMContentLoaded", () => {
  // Canvas ve Simülatör Kurulumu
  const canvas = document.getElementById("cymaticsCanvas");
  cymaticsSim = new CymaticsSimulation(canvas);
  startOscilloscope();

  // Tab Geçişleri
  document.querySelectorAll(".tab-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
      document.querySelectorAll(".tab-content").forEach(c => c.classList.remove("active"));

      btn.classList.add("active");
      const targetId = btn.getAttribute("data-tab");
      document.getElementById(targetId).classList.add("active");
    });
  });

  // Hızlı Frekans Butonları (Schumann, Om, 432 Hz)
  document.querySelectorAll(".quick-freq-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const freq = parseFloat(btn.getAttribute("data-freq"));
      audio.playTone(freq);
      cymaticsSim.setFrequency(freq);
    });
  });

  // Chladni Slider Dinleyicileri
  const nSlider = document.getElementById("chladniN");
  const mSlider = document.getElementById("chladniM");

  nSlider.addEventListener("input", (e) => {
    cymaticsSim.setModes(parseInt(e.target.value), parseInt(mSlider.value));
  });

  mSlider.addEventListener("input", (e) => {
    cymaticsSim.setModes(parseInt(nSlider.value), parseInt(e.target.value));
  });

  // Parçacıkları Saç
  document.getElementById("scatterParticlesBtn").addEventListener("click", () => {
    cymaticsSim.initParticles();
  });

  // Ses Aç / Kapa
  document.getElementById("toggleAudioBtn").addEventListener("click", () => {
    if (audio.isPlayingSingle || audio.isPlayingBinaural || audio.makamTimeouts.length > 0) {
      audio.stopTone();
    } else {
      audio.playTone(cymaticsSim.currentFreq);
    }
  });

  // Binaural Kontrolleri
  const carrierSlider = document.getElementById("carrierSlider");
  const beatSlider = document.getElementById("beatSlider");
  const carrierVal = document.getElementById("carrierVal");
  const beatVal = document.getElementById("beatVal");
  const toggleBinauralBtn = document.getElementById("toggleBinauralBtn");

  carrierSlider.addEventListener("input", (e) => {
    carrierVal.innerText = e.target.value;
    if (audio.isPlayingBinaural) {
      audio.playBinaural(parseFloat(carrierSlider.value), parseFloat(beatSlider.value));
    }
  });

  beatSlider.addEventListener("input", (e) => {
    beatVal.innerText = parseFloat(e.target.value).toFixed(1);
    if (audio.isPlayingBinaural) {
      audio.playBinaural(parseFloat(carrierSlider.value), parseFloat(beatSlider.value));
    }
  });

  document.querySelectorAll(".wave-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".wave-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      const carrier = parseFloat(btn.getAttribute("data-carrier"));
      const beat = parseFloat(btn.getAttribute("data-beat"));

      carrierSlider.value = carrier;
      carrierVal.innerText = carrier;
      beatSlider.value = beat;
      beatVal.innerText = beat.toFixed(1);

      if (audio.isPlayingBinaural) {
        audio.playBinaural(carrier, beat);
      }
    });
  });

  toggleBinauralBtn.addEventListener("click", () => {
    if (audio.isPlayingBinaural) {
      audio.stopBinaural();
      toggleBinauralBtn.innerText = "🎧 Binaural Sesi Başlat";
    } else {
      const carrier = parseFloat(carrierSlider.value);
      const beat = parseFloat(beatSlider.value);
      audio.playBinaural(carrier, beat);
      cymaticsSim.setFrequency(carrier);
      toggleBinauralBtn.innerText = "⏹️ Binaural Sesi Durdur";
    }
  });

  // Verileri ve Alt Bileşenleri Başlat
  renderSolfeggio();
  renderMakamlar();
  renderTraditions();
  setupBreathing();
});
