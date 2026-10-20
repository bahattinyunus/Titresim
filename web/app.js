/**
 * Titreşim: Evrensel Ses, Kutsal Kelâm ve Frekans Terapisi Laboratuvarı v1.2
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
    time: "Akşam ile yatsı arası",
    element: "Su (Soğuk & Nemli) / Kova",
    organ: "Omurga, bel, kalça ve böbrekler",
    effects: ["Cesaret, ferahlık ve ulvi hisler uyandırır.", "Akıl hastalıklarında kötü düşünceleri kovar.", "Omurga ağrılarını hafifletir."],
    quote: "Farabi: 'Neva makamı insana lezzet ve ferahlık verir.'",
    ratios: [1.0, 1.125, 1.2, 1.333, 1.5, 1.687, 1.8, 2.0]
  }
];

const PLANETARY_DATA = [
  { id: "sun", name: "Güneş (Sun)", freq: 126.22, note: "B", chakra: "Solar Pleksus", cycle: "Güneş rotasyonu (32. oktav)", desc: "Yaşam enerjisi, canlılık ve benlik farkındalığı aşılar.", color: "#f59e0b" },
  { id: "mercury", name: "Merkür (Mercury)", freq: 141.27, note: "C#", chakra: "Boğaz", cycle: "Yörünge periyodu (30. oktav)", desc: "İletişim, mantıksal zeka ve zihinsel akıcılık sağlar.", color: "#94a3b8" },
  { id: "venus", name: "Venüs (Venus)", freq: 221.23, note: "A", chakra: "Kalp / Üçüncü Göz", cycle: "Yörünge periyodu (32. oktav)", desc: "Aşk, estetik, uyum ve şefkat rezonansı doğurur.", color: "#ec4899" },
  { id: "earth_day", name: "Dünya Günü", freq: 194.18, note: "G", chakra: "Kök Çakra", cycle: "24 saat eksenel dönüş (24. oktav)", desc: "Topraklanma, fiziksel dinamizm ve canlılık.", color: "#10b981" },
  { id: "om_year", name: "Dünya Yılı (Om)", freq: 136.10, note: "C#", chakra: "Kalp (Anahata)", cycle: "365.25 günlük döngü (32. oktav)", desc: "Evrensel denge, derin meditatif sükunet.", color: "#6366f1" },
  { id: "moon_synodic", name: "Sinodik Ay", freq: 210.42, note: "G#", chakra: "Sakral Çakra", cycle: "29.53 gün ay fazı (29. oktav)", desc: "Duygusal akışkanlık, sezgi ve lenfatik denge.", color: "#38bdf8" },
  { id: "mars", name: "Mars", freq: 144.72, note: "D", chakra: "Kök / Göbek", cycle: "Mars döngüsü (33. oktav)", desc: "Cesaret, motivasyon ve odaklanmış eylem kudreti.", color: "#ef4444" },
  { id: "jupiter", name: "Jüpiter", freq: 183.58, note: "F#", chakra: "Üçüncü Göz", cycle: "11.86 yıllık yörünge (36. oktav)", desc: "Genişleme, bilgelik ve yüksek idrak bereketi.", color: "#f97316" },
  { id: "saturn", name: "Satürn", freq: 147.85, note: "D", chakra: "Kök Çakra", cycle: "29.46 yıllık yörünge (37. oktav)", desc: "Disiplin, konsantrasyon ve kemik/yapı sağlığı.", color: "#64748b" },
  { id: "platonic_year", name: "Platonik Büyük Yıl", freq: 172.06, note: "F", chakra: "Taç Çakra", cycle: "25.920 yıllık presesyon (48. oktav)", desc: "Ruhsal neşe, aydınlanma ve evrensel kozmik bilinç.", color: "#8b5cf6" }
];

const TRADITIONS_DATA = [
  {
    tradition: "İslam Tasavvuf ve Tecvid Geleneği",
    practice: "Kur'an-ı Kerim Kıraati ve Zikir Rezonansı",
    principles: [
      "Tecvid kuralları (Med, Gunne, Kalkale, İhfa) ses yolunda mikro-harmonikler üretir.",
      "Gunne (geniz titreşimi): Sinüsleri uyararak nitrik oksit (NO) salınımını 15 kata kadar arttırır.",
      "Uzatma (Medd): Akciğer kapasitesini ve parasempatik vagal tonusu optimize eder."
    ],
    effects: "Frontal EEG'de belirgin Alfa/Teta artışı, kortizolde sert düşüş, kalp hızı değişkenliği (HRV) koheransı."
  },
  {
    tradition: "Vedik ve Hint Geleneği",
    practice: "Pranava Mantra (Om / Aum) & Nada Yoga",
    principles: [
      "A-U-M heceleri karından tepeye kadar dikey bir titreşim sütunu oluşturur.",
      "Sanskrit fonetik dil yapısı damağa temas ederek 84 meridyen noktasını uyarır.",
      "136.1 Hz (Dünya Yılı / Ciss) temel frekansı ile evrensel uyum."
    ],
    effects: "Amigdala uyarımını yatıştırır, Default Mode Network (gevezelik) aktivitesini durdurur."
  },
  {
    tradition: "Batı Gregoryen Manastır Geleneği",
    practice: "Gregoryen İlahileri (Gregorian Chants / Solfeggio)",
    principles: [
      "Monofonik saf entonasyon ve 4-8 saniyelik katedral rezonansı.",
      "Dr. Alfred Tomatis'in bulgularına göre koklea salyangozunu şarj eder ve korteksi uyanık tutar."
    ],
    effects: "Nefes ritmini dakikada 6 nefese düşürür, tansiyonu regüle eder."
  },
  {
    tradition: "Tibet ve Himalaya Şamanizmi",
    practice: "Tibet Ses Çanakları (Singing Bowls) & Çanlar",
    principles: [
      "7 kutsal metal alaşımından yayılan çok katmanlı mikrotonal çarpışmalar (Doğal Binaural vuruş).",
      "Beden dokularında ve hücreler arası sıvıda piezoelektrik titreşim masajı."
    ],
    effects: "Anksiyete ve zihinsel stresi saniyeler içinde kırarak derin gevşeme sağlar."
  }
];

const QUOTES_DATA = [
  {
    id: "tesla_energy_vibration",
    author: "Nikola Tesla",
    era: "1856 - 1943",
    work: "Kişisel Notlar ve Röportajlar",
    quote: "Evrenin sırrını bulmak istiyorsanız; enerji, frekans ve titreşim cinsinden düşünün.",
    category: "bilim_ve_fizik",
    freq: 432.0,
    reflection: "Madde sandığımız katılık, belirli frekanslarda kilitlenmiş yoğun enerjiden ibarettir."
  },
  {
    id: "tesla_369",
    author: "Nikola Tesla",
    era: "1856 - 1943",
    work: "Elektromanyetik Araştırmalar",
    quote: "3, 6 ve 9 sayılarının ihtişamını bilseydiniz, evrenin anahtarına sahip olurdunuz.",
    category: "bilim_ve_fizik",
    freq: 396.0,
    reflection: "Solfeggio frekanslarının tümü rakam kökü toplamında 3, 6 veya 9'a indirgenir."
  },
  {
    id: "einstein_future_medicine",
    author: "Albert Einstein",
    era: "1879 - 1955",
    work: "Bilimsel Aforizmalar",
    quote: "Geleceğin tıbbı, frekanslar tıbbı olacaktır.",
    category: "bilim_ve_fizik",
    freq: 528.0,
    reflection: "Biyokimyasal moleküller yerine dokuların doğal rezonans frekanslarıyla etkileşim kuran akustik şifa."
  },
  {
    id: "einstein_energy_match",
    author: "Albert Einstein",
    era: "1879 - 1955",
    work: "Görelilik ve Kuantum Mektupları",
    quote: "Her şey enerjidir ve her şey sadece bundan ibarettir. Sahip olmak istediğiniz gerçekliğin frekansına uyum sağladığınızda, artık o gerçeğe sahip olursunuz.",
    category: "bilim_ve_fizik",
    freq: 136.1,
    reflection: "İçsel durumunuzun frekansı, yaşamınızın rezonans alanını belirler."
  },
  {
    id: "mevlana_ney_dinle",
    author: "Mevlânâ Celâleddîn-i Rûmî",
    era: "1207 - 1273",
    work: "Mesnevî-i Mânevî (1. Beyit)",
    quote: "Dinle neyden kim hikâyet etmededir; ayrılıklardan şikâyet etmededir. Kamışlıktan kesildim kesile, feryadımdan kadın-erkek herkes inledi.",
    category: "tasavvuf",
    freq: 220.0,
    reflection: "Ney, içi boşaltılmış ve ilahi nefese ayna olmuş kamil insanın asıl vatanına duyduğu iştiyaktır."
  },
  {
    id: "mevlana_ney_dost",
    author: "Mevlânâ Celâleddîn-i Rûmî",
    era: "1207 - 1273",
    work: "Dîvân-ı Kebîr",
    quote: "Biz birer ney gibiyiz; bizdeki nağmeler Senden gelir ey Dost! Biz bir dağ gibiyiz; bizdeki seda Senin sesinin yankısıdır.",
    category: "tasavvuf",
    freq: 136.1,
    reflection: "Varlık, Hakk'ın nefesinin kozmik kamışta çıkardığı kesintisiz bir nağmeden ibarettir."
  },
  {
    id: "mevlana_sama",
    author: "Mevlânâ Celâleddîn-i Rûmî",
    era: "1207 - 1273",
    work: "Fîhi Mâ Fîh",
    quote: "Semâ, âşıkların gıdasıdır; zira onda cananın hayali ve vuslatın kokusu vardır. Ruhun perdesini aralayan ses, insanı ötelerle buluşturur.",
    category: "tasavvuf",
    freq: 432.0,
    reflection: "Ritmik dönüş ve musiki, zihni susturarak kalbi merkeze oturtan akustik bir ibadettir."
  },
  {
    id: "ibn_sina_musiki_sifasi",
    author: "İbn-i Sînâ (Avicenna)",
    era: "980 - 1037",
    work: "El-Kânûn fi't-Tıbb & Şifâ",
    quote: "Tedavinin en iyi ve en tesirli yollarından biri; hastanın aklî ve ruhî kuvvetlerini artırmak, ona güzel kokular ve hoşuna giden musiki ile şifa vermektir.",
    category: "islam_tibbi",
    freq: 220.0,
    reflection: "Hekim sadece bedeni değil, ruhun mizacını nağmelerle mizanına getiren kişidir."
  },
  {
    id: "ibn_sina_nabiz",
    author: "İbn-i Sînâ (Avicenna)",
    era: "980 - 1037",
    work: "Risâle fi'n-Nabz",
    quote: "Nabzın vuruşları ile musiki perdeleri arasında tam bir tenasüp (oran) vardır. Hekim, nabızdaki aksaklığı müziğin makamı ile teşhis edip tedavi edebilir.",
    category: "islam_tibbi",
    freq: 293.33,
    reflection: "Kalp atışı bir perküsyon, damarlar ise telli sazdır; makamlar nabzın bozulan veznini düzeltir."
  },
  {
    id: "farabi_makamlar",
    author: "Fârâbî (Alpharabius)",
    era: "872 - 950",
    work: "Kitâbü'l-Mûsîka'l-Kebîr",
    quote: "Rast makamı insana sefa (huzur ve neşe), Rehavi sonsuzluk hissi, Buselik kuvvet, Isfahan zeka ve güven verir.",
    category: "islam_tibbi",
    freq: 220.0,
    reflection: "Farabi, makamların insan psikolojisi ve hormonları üzerindeki tesirlerini ilk kez sistemleştirmiştir."
  },
  {
    id: "pythagoras_spheres",
    author: "Pisagor (Pythagoras)",
    era: "M.Ö. 570 - 495",
    work: "Kürelerin Müziği (Musica Universalis)",
    quote: "Gözler için gök kubbe ve yıldızlar ne ise, kulaklar için de ses ve armoni odur. Gezegenlerin her biri dönerken ilahi bir ses çıkarır.",
    category: "antik_felsefe",
    freq: 216.0,
    reflection: "Evren sayılardan örülmüştür; müzik ise sayıların işitilebilir suretidir."
  },
  {
    id: "pythagoras_geometry",
    author: "Pisagor (Pythagoras)",
    era: "M.Ö. 570 - 495",
    work: "Pisagoryen Fragmanlar",
    quote: "Geometri maddenin mekândaki nizamıdır; musiki ise zamanın nizamıdır.",
    category: "antik_felsefe",
    freq: 432.0,
    reflection: "Zaman içinde salınan her form müziktir, mekânda donan her müzik mimaridir."
  },
  {
    id: "plato_music",
    author: "Platon (Eflatun)",
    era: "M.Ö. 427 - 347",
    work: "Devlet (Respublica)",
    quote: "Müzik ruha kanat verir, zihne uçuş gücü aşılar, hayal gücünü tutuşturur, hüzün perdesini yırtar ve tüm varoluşa neşe ve hayat bahşeder.",
    category: "antik_felsefe",
    freq: 528.0,
    reflection: "Müzik eğitimi alan bir ruh, evrendeki uyumsuzlukları sezgisel olarak hemen hisseder."
  },
  {
    id: "confucius_music",
    author: "Konfüçyüs (Kongzi)",
    era: "M.Ö. 551 - 479",
    work: "Li Ji (Yue Ji - Müzik Kitabı)",
    quote: "Bir toplumun ahlakını ve ruhunu dönüştürmek, nizamını tesis etmek istiyorsanız; işe onların müziğini tanzim etmekle başlayın.",
    category: "antik_felsefe",
    freq: 136.1,
    reflection: "Bir medeniyetin müziğindeki armoni ve vakar, onun ahlaki seviyesinin aynasıdır."
  },
  {
    id: "hermes_vibration",
    author: "Hermes Trismegistus",
    era: "Antik İskenderiye Geleneği",
    work: "Kybalion (Titreşim Prensibi)",
    quote: "Hiçbir şey durmaz; her şey hareket eder; her şey titreşir. Saf Ruhtan en kaba maddeye kadar her varoluş hali, farklı titreşim dereceleridir.",
    category: "antik_felsefe",
    freq: 7.83,
    reflection: "Titreşim frekansını değiştiren simyacı, zihnin ve maddenin doğasını da dönüştürür."
  },
  {
    id: "kuran_kun",
    author: "Kur'ân-ı Kerîm",
    era: "Vahiy Geleneği",
    work: "Yâsîn Sûresi, 82. Âyet",
    quote: "O'nun emri, bir şeyi dilediği vakit sadece ona 'Kün!' (Ol!) demektir; o şey de hemen oluverir.",
    category: "tasavvuf",
    freq: 528.0,
    reflection: "Kozmik yaradılış ilahi kelâmın ve titreşimin tecelli etmesiyle başlamıştır."
  },
  {
    id: "ibrahim_hakki",
    author: "Erzurumlu İbrahim Hakkı",
    era: "1703 - 1780",
    work: "Mârifetnâme",
    quote: "Ses ve nefes, can mülkünün cananıdır; doğru nağme dertlilere dermandır.",
    category: "tasavvuf",
    freq: 220.0,
    reflection: "Marifetname, makamlar ile insan tabiatlarının dengelenmesini teferruatıyla açıklar."
  },
  {
    id: "suuri_hasan",
    author: "Şuûrî Hasan Efendi",
    era: "17. Yüzyıl",
    work: "Ta'dîl-i Emzice",
    quote: "Günün vakitlerinde hastaların hıltları değişir. Hekim; fecirde Rast, kuşlukta Buselik, öğlede Uşşak dinleterek bedenin kimyasını sesle dengeye getirir.",
    category: "islam_tibbi",
    freq: 247.5,
    reflection: "Osmanlı hekimleri, sirkadiyen biyolojik saati makamların frekanslarıyla senkronize etmiştir."
  },
  {
    id: "evliya_celebi",
    author: "Evliyâ Çelebi",
    era: "1611 - 1682",
    work: "Seyahatnâme (Edirne Darüşşifası)",
    quote: "Edirne Darüşşifası'nda hanendeler saz meclisi kurup on makam ile meşk ederler; hastalar bu nağmelerle mest olup feryatları kesilir, şifa bulurlar.",
    category: "islam_tibbi",
    freq: 220.0,
    reflection: "Avrupa'da akıl hastalarının zincire vurulduğu çağda, Osmanlı'da musikiyle terapi uygulanıyordu."
  },
  {
    id: "kepler_music",
    author: "Johannes Kepler",
    era: "1571 - 1630",
    work: "Harmonices Mundi (1619)",
    quote: "Göklerdeki gezegenler semavi bir polifoni icra ederler. Gezegenlerin hız oranları, tam müzikal gam aralıklarına karşılık gelir.",
    category: "bilim_ve_fizik",
    freq: 183.58,
    reflection: "Gezegenlerin hareket yasaları ile müzik harmonisi aynı ilahi geometrinin tezahürüdür."
  },
  {
    id: "chladni_cymatics",
    author: "Ernst Chladni",
    era: "1756 - 1827",
    work: "Entdeckungen über die Theorie des Klanges",
    quote: "Levhaya yayı sürttüğümde kum taneleri görünmeyen bir iradenin emrindeymiş gibi kusursuz geometrik mandalalara toplandı. Ses, maddeyi biçimlendiren mimardır.",
    category: "bilim_ve_fizik",
    freq: 432.0,
    reflection: "Sematik, ses dalgalarının görünmez gücünü gözle görülür somut maddeye dönüştürür."
  },
  {
    id: "masaru_emoto",
    author: "Dr. Masaru Emoto",
    era: "1943 - 2014",
    work: "Suyun Gizli Mesajı",
    quote: "Su dinler ve hisseder. Sevgi ve ahenkli müzik dinletilen su kusursuz altıgen kristaller oluşturur. Bedenimizin %70'i su olduğuna göre, her ses bizi yeniden inşa eder.",
    category: "mistik_akustik",
    freq: 528.0,
    reflection: "Beden suyu, zihnimizden ve çevremizden yayılan her frekansın canlı kütüphanesidir."
  },
  {
    id: "inayat_khan",
    author: "Hazrat Inayat Khan",
    era: "1882 - 1927",
    work: "The Mysticism of Sound and Music",
    quote: "Ses tüm tezahürün başlangıcı ve sonudur. Bilen kişi için tüm evren tek bir ilahi senfonidir. Bedeniniz bir enstrüman, ruhunuz virtüözdür.",
    category: "mistik_akustik",
    freq: 432.0,
    reflection: "Hastalık bedenin akordunun bozulması, şifa ise yeniden evrensel frekansa akortlanmasıdır."
  },
  {
    id: "yunus_emre",
    author: "Yûnus Emre",
    era: "1238 - 1328",
    work: "Dîvân-ı Yûnus Emre",
    quote: "Söz ola kese savaşı / Söz ola kestire başı / Söz ola ağulu aşı / Bal ile yağ ede bir söz.",
    category: "tasavvuf",
    freq: 432.0,
    reflection: "Ağızdan çıkan her harf bir titreşim yayar; şifalı kelâm zehirli halleri bala ve yağa dönüştürür."
  }
];

// ==========================================
// 2. GELİŞMİŞ SES MOTORU (WEB AUDIO API)
// ==========================================
class AudioEngine {
  constructor() {
    this.ctx = null;
    this.masterGain = null;
    this.analyser = null;
    this.destNode = null; // Kayıt için

    // Tekli ton
    this.singleOsc = null;
    this.singleGain = null;
    this.isPlayingSingle = false;

    // Binaural
    this.leftOsc = null;
    this.rightOsc = null;
    this.binauralGain = null;
    this.isPlayingBinaural = false;

    // İzokronik
    this.isoCarrierOsc = null;
    this.isoGain = null;
    this.isoInterval = null;
    this.isPlayingIso = false;

    // Gürültü
    this.noiseNode = null;
    this.noiseGain = null;
    this.isPlayingNoise = false;

    // Dem / Tanpura Drone
    this.droneOscs = [];
    this.droneGain = null;
    this.isPlayingDrone = false;

    // Makam
    this.makamTimeouts = [];

    // Kayıt Cihazı
    this.mediaRecorder = null;
    this.recordedChunks = [];
    this.isRecording = false;
  }

  init() {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioCtx();

      this.masterGain = this.ctx.createGain();
      this.masterGain.gain.setValueAtTime(0.5, this.ctx.currentTime);

      this.analyser = this.ctx.createAnalyser();
      this.analyser.fftSize = 512;

      this.destNode = this.ctx.createMediaStreamDestination();

      this.masterGain.connect(this.analyser);
      this.analyser.connect(this.ctx.destination);
      this.analyser.connect(this.destNode);
    }
    if (this.ctx.state === "suspended") {
      this.ctx.resume();
    }
  }

  playTone(freq, type = "sine") {
    this.init();
    this.stopTone();
    this.stopBinaural();
    this.stopIsochronic();

    this.singleOsc = this.ctx.createOscillator();
    this.singleGain = this.ctx.createGain();

    this.singleOsc.type = type;
    this.singleOsc.frequency.setValueAtTime(freq, this.ctx.currentTime);

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
        this.singleGain.gain.linearRampToValueAtTime(0.001, now + 0.08);
        setTimeout(() => {
          if (this.singleOsc) {
            this.singleOsc.stop();
            this.singleOsc.disconnect();
            this.singleOsc = null;
          }
        }, 90);
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
    this.stopIsochronic();

    const leftFreq = carrier - (beat / 2);
    const rightFreq = carrier + (beat / 2);

    this.leftOsc = this.ctx.createOscillator();
    this.rightOsc = this.ctx.createOscillator();

    this.leftOsc.frequency.setValueAtTime(leftFreq, this.ctx.currentTime);
    this.rightOsc.frequency.setValueAtTime(rightFreq, this.ctx.currentTime);

    const merger = this.ctx.createChannelMerger(2);
    this.binauralGain = this.ctx.createGain();

    this.leftOsc.connect(merger, 0, 0);  // Sol kanal
    this.rightOsc.connect(merger, 0, 1); // Sağ kanal

    merger.connect(this.binauralGain);
    this.binauralGain.gain.setValueAtTime(0, this.ctx.currentTime);
    this.binauralGain.gain.linearRampToValueAtTime(0.35, this.ctx.currentTime + 0.2);

    this.binauralGain.connect(this.masterGain);

    this.leftOsc.start();
    this.rightOsc.start();
    this.isPlayingBinaural = true;

    updateAudioStatus(true, `Binaural (${carrier} Hz / Beat: ${beat.toFixed(1)} Hz)`);
  }

  stopBinaural() {
    if (this.leftOsc && this.rightOsc) {
      try {
        const now = this.ctx.currentTime;
        this.binauralGain.gain.linearRampToValueAtTime(0.001, now + 0.1);
        setTimeout(() => {
          if (this.leftOsc) { this.leftOsc.stop(); this.leftOsc = null; }
          if (this.rightOsc) { this.rightOsc.stop(); this.rightOsc = null; }
        }, 110);
      } catch (e) {
        this.leftOsc = null;
        this.rightOsc = null;
      }
    }
    this.isPlayingBinaural = false;
    updateAudioStatus(false);
  }

  playIsochronic(carrierFreq, pulseRate) {
    this.init();
    this.stopTone();
    this.stopBinaural();
    this.stopIsochronic();

    this.isoCarrierOsc = this.ctx.createOscillator();
    this.isoCarrierOsc.type = "sine";
    this.isoCarrierOsc.frequency.setValueAtTime(carrierFreq, this.ctx.currentTime);

    this.isoGain = this.ctx.createGain();
    this.isoGain.gain.setValueAtTime(0.0, this.ctx.currentTime);

    this.isoCarrierOsc.connect(this.isoGain);
    this.isoGain.connect(this.masterGain);

    this.isoCarrierOsc.start();
    this.isPlayingIso = true;

    // Ritmik darbe modülasyonu
    const periodMs = 1000.0 / pulseRate;
    const onDuration = periodMs * 0.5;

    let isOn = false;
    this.isoInterval = setInterval(() => {
      if (!this.isPlayingIso || !this.ctx) return;
      isOn = !isOn;
      const now = this.ctx.currentTime;
      if (isOn) {
        this.isoGain.gain.cancelScheduledValues(now);
        this.isoGain.gain.linearRampToValueAtTime(0.4, now + 0.02);
      } else {
        this.isoGain.gain.cancelScheduledValues(now);
        this.isoGain.gain.linearRampToValueAtTime(0.001, now + 0.02);
      }
    }, onDuration);

    updateAudioStatus(true, `İzokronik: ${carrierFreq} Hz / Nabız: ${pulseRate.toFixed(1)} Hz`);
  }

  stopIsochronic() {
    if (this.isoInterval) {
      clearInterval(this.isoInterval);
      this.isoInterval = null;
    }
    if (this.isoCarrierOsc) {
      try {
        this.isoCarrierOsc.stop();
        this.isoCarrierOsc.disconnect();
      } catch (e) {}
      this.isoCarrierOsc = null;
    }
    this.isPlayingIso = false;
    updateAudioStatus(false);
  }

  playNoise(type = "pink", volume = 0.3) {
    this.init();
    this.stopNoise();

    const bufferSize = this.ctx.sampleRate * 3; // 3 saniyelik döngü
    const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
    const output = buffer.getChannelData(0);

    if (type === "white") {
      for (let i = 0; i < bufferSize; i++) {
        output[i] = Math.random() * 2 - 1;
      }
    } else if (type === "pink") {
      let b0 = 0, b1 = 0, b2 = 0, b3 = 0, b4 = 0, b5 = 0, b6 = 0;
      for (let i = 0; i < bufferSize; i++) {
        const white = Math.random() * 2 - 1;
        b0 = 0.99886 * b0 + white * 0.0555179;
        b1 = 0.99332 * b1 + white * 0.0750759;
        b2 = 0.96900 * b2 + white * 0.1538520;
        b3 = 0.86650 * b3 + white * 0.3104856;
        b4 = 0.55000 * b4 + white * 0.5329522;
        b5 = -0.7616 * b5 - white * 0.0168980;
        output[i] = (b0 + b1 + b2 + b3 + b4 + b5 + b6 + white * 0.5362) * 0.11;
        b6 = white * 0.115926;
      }
    } else if (type === "brown") {
      let lastOut = 0.0;
      for (let i = 0; i < bufferSize; i++) {
        const white = Math.random() * 2 - 1;
        output[i] = (lastOut + (0.02 * white)) / 1.02;
        lastOut = output[i];
        output[i] *= 3.5; // Güçlendir
      }
    }

    this.noiseNode = this.ctx.createBufferSource();
    this.noiseNode.buffer = buffer;
    this.noiseNode.loop = true;

    this.noiseGain = this.ctx.createGain();
    this.noiseGain.gain.setValueAtTime(volume, this.ctx.currentTime);

    this.noiseNode.connect(this.noiseGain);
    this.noiseGain.connect(this.masterGain);

    this.noiseNode.start();
    this.isPlayingNoise = true;
  }

  stopNoise() {
    if (this.noiseNode) {
      try {
        this.noiseNode.stop();
        this.noiseNode.disconnect();
      } catch (e) {}
      this.noiseNode = null;
    }
    this.isPlayingNoise = false;
  }

  toggleDrone(rootFreq = 136.1) {
    if (this.isPlayingDrone) {
      this.stopDrone();
      return false;
    } else {
      this.startDrone(rootFreq);
      return true;
    }
  }

  startDrone(rootFreq = 136.1) {
    this.init();
    this.stopDrone();

    this.droneGain = this.ctx.createGain();
    this.droneGain.gain.setValueAtTime(0, this.ctx.currentTime);
    this.droneGain.gain.linearRampToValueAtTime(0.25, this.ctx.currentTime + 1.5);

    // Düşük geçiren filtre (yumuşak mistik hava)
    const filter = this.ctx.createBiquadFilter();
    filter.type = "lowpass";
    filter.frequency.setValueAtTime(600, this.ctx.currentTime);

    const layers = [
      { freq: rootFreq, gain: 0.5 },
      { freq: rootFreq * 1.002, gain: 0.3 }, // Koro detuning
      { freq: rootFreq * 1.5, gain: 0.2 },   // 5'li
      { freq: rootFreq * 2.0, gain: 0.1 }    // Oktav
    ];

    layers.forEach(l => {
      const osc = this.ctx.createOscillator();
      const g = this.ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(l.freq, this.ctx.currentTime);
      g.gain.setValueAtTime(l.gain, this.ctx.currentTime);

      osc.connect(g);
      g.connect(filter);
      osc.start();
      this.droneOscs.push(osc);
    });

    filter.connect(this.droneGain);
    this.droneGain.connect(this.masterGain);
    this.isPlayingDrone = true;
  }

  stopDrone() {
    if (this.droneOscs.length > 0) {
      try {
        const now = this.ctx.currentTime;
        this.droneGain.gain.linearRampToValueAtTime(0.001, now + 1.0);
        setTimeout(() => {
          this.droneOscs.forEach(o => { try { o.stop(); o.disconnect(); } catch (e) {} });
          this.droneOscs = [];
        }, 1050);
      } catch (e) {
        this.droneOscs = [];
      }
    }
    this.isPlayingDrone = false;
  }

  playTibetanBowl(freq = 528.0) {
    this.init();
    const now = this.ctx.currentTime;

    const harmonics = [1.0, 2.0, 3.01, 4.2];
    const decays = [4.5, 3.0, 2.0, 1.2];

    harmonics.forEach((h, idx) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(freq * h, now);

      gain.gain.setValueAtTime(0.2 / (idx + 1), now);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + decays[idx]);

      osc.connect(gain);
      gain.connect(this.masterGain);

      osc.start(now);
      osc.stop(now + decays[idx]);
    });
  }

  playMakamScale(makam, baseFreq = 220.0) {
    this.init();
    this.stopTone();
    this.stopMakamScale();

    const noteDuration = 0.9;
    makam.ratios.forEach((ratio, index) => {
      const freq = baseFreq * ratio;
      const tid = setTimeout(() => {
        this.playMakamNote(freq, noteDuration);
        if (cymaticsSim) {
          cymaticsSim.setFrequency(freq);
        }
      }, index * noteDuration * 1000);
      this.makamTimeouts.push(tid);
    });

    updateAudioStatus(true, `${makam.name} Arpeji Çalıyor`);
  }

  playMakamNote(freq, duration) {
    const now = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();

    osc.type = "sine";
    osc.frequency.setValueAtTime(freq, now);

    gain.gain.setValueAtTime(0, now);
    gain.gain.linearRampToValueAtTime(0.35, now + 0.08);
    gain.gain.setValueAtTime(0.3, now + duration - 0.15);
    gain.gain.linearRampToValueAtTime(0.001, now + duration);

    osc.connect(gain);
    gain.connect(this.masterGain);

    osc.start(now);
    osc.stop(now + duration + 0.05);
  }

  stopMakamScale() {
    this.makamTimeouts.forEach(id => clearTimeout(id));
    this.makamTimeouts = [];
  }

  startRecording() {
    this.init();
    this.recordedChunks = [];
    const stream = this.destNode.stream;
    this.mediaRecorder = new MediaRecorder(stream);

    this.mediaRecorder.ondataavailable = (e) => {
      if (e.data.size > 0) {
        this.recordedChunks.push(e.data);
      }
    };

    this.mediaRecorder.onstop = () => {
      const blob = new Blob(this.recordedChunks, { type: "audio/webm" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `titresim_seans_${new Date().toISOString().slice(0, 19).replace(/[:T]/g, "-")}.webm`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    };

    this.mediaRecorder.start();
    this.isRecording = true;
  }

  stopRecording() {
    if (this.mediaRecorder && this.isRecording) {
      this.mediaRecorder.stop();
      this.isRecording = false;
    }
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

    this.plateType = "square"; // "square" veya "circular"
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
    for (let i = 0; i < this.numParticles; i++) {
      this.particles.push({
        x: (Math.random() - 0.5) * 0.94,
        y: (Math.random() - 0.5) * 0.94,
        vx: (Math.random() - 0.5) * 0.002,
        vy: (Math.random() - 0.5) * 0.002,
        size: Math.random() < 0.2 ? 1.8 : 1.2,
        colorHue: Math.random() < 0.15 ? 195 : 42
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
    if (this.plateType === "circular") {
      // Dairesel plaka / Su çanağı modu: J_m(k * r) * cos(m * theta)
      const r = Math.sqrt(x * x + y * y);
      if (r > 0.48) return 5.0; // Sınır dışı
      const theta = Math.atan2(y, x);
      const normR = r / 0.48;
      const k = pi * (this.n + (this.m / 2.0) - 0.25);
      const arg = k * normR;
      // Bessel J_m(arg) yaklaşımı
      const radial = Math.cos(arg - (this.m * pi / 2) - (pi / 4)) * Math.sqrt(2 / (pi * (arg + 0.1)));
      return radial * Math.cos(this.m * theta);
    } else {
      // Standart Kare Chladni Plakası
      const term1 = Math.cos(this.n * pi * x) * Math.cos(this.m * pi * y);
      const term2 = Math.cos(this.m * pi * x) * Math.cos(this.n * pi * y);
      return this.a * term1 - this.b * term2;
    }
  }

  animate() {
    const ctx = this.ctx;
    const w = this.canvas.width;
    const h = this.canvas.height;
    const halfW = w / 2;
    const halfH = h / 2;

    ctx.fillStyle = "rgba(6, 9, 17, 0.25)";
    ctx.fillRect(0, 0, w, h);

    // Dairesel plaka çeperi çizimi
    if (this.plateType === "circular") {
      ctx.strokeStyle = "rgba(56, 189, 248, 0.25)";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.arc(halfW, halfH, (w - 20) * 0.48, 0, Math.PI * 2);
      ctx.stroke();
    }

    const isAudioActive = audio.isPlayingSingle || audio.isPlayingBinaural || audio.isPlayingIso || audio.isPlayingDrone || audio.makamTimeouts.length > 0;
    const agitation = isAudioActive ? 0.0035 : 0.001;
    const forceFactor = isAudioActive ? 0.0006 : 0.0002;

    for (let i = 0; i < this.particles.length; i++) {
      const p = this.particles[i];

      const val = this.evaluateW(p.x, p.y);
      const absVal = Math.abs(val);

      const eps = 0.01;
      const gradX = (Math.abs(this.evaluateW(p.x + eps, p.y)) - absVal) / eps;
      const gradY = (Math.abs(this.evaluateW(p.x, p.y + eps)) - absVal) / eps;

      p.vx -= gradX * forceFactor;
      p.vy -= gradY * forceFactor;

      p.vx += (Math.random() - 0.5) * agitation * absVal;
      p.vy += (Math.random() - 0.5) * agitation * absVal;

      p.vx *= 0.94;
      p.vy *= 0.94;

      p.x += p.vx;
      p.y += p.vy;

      if (this.plateType === "circular") {
        const r = Math.sqrt(p.x * p.x + p.y * p.y);
        if (r > 0.47) {
          const angle = Math.atan2(p.y, p.x);
          p.x = Math.cos(angle) * 0.46;
          p.y = Math.sin(angle) * 0.46;
          p.vx *= -0.4;
          p.vy *= -0.4;
        }
      } else {
        if (p.x < -0.48) { p.x = -0.48; p.vx *= -0.5; }
        if (p.x > 0.48) { p.x = 0.48; p.vx *= -0.5; }
        if (p.y < -0.48) { p.y = -0.48; p.vy *= -0.5; }
        if (p.y > 0.48) { p.y = 0.48; p.vy *= -0.5; }
      }

      const scrX = halfW + p.x * (w - 20);
      const scrY = halfH + p.y * (h - 20);

      ctx.beginPath();
      ctx.arc(scrX, scrY, p.size, 0, Math.PI * 2);
      if (absVal < 0.16) {
        ctx.fillStyle = p.colorHue === 42 ? "#fbbf24" : "#38bdf8";
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

    const isActive = audio.analyser && (audio.isPlayingSingle || audio.isPlayingBinaural || audio.isPlayingIso || audio.isPlayingDrone || audio.isPlayingNoise || audio.makamTimeouts.length > 0);

    if (isActive) {
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
      ctx.lineTo(canvas.width, canvas.height / 2);
      ctx.stroke();
    } else {
      // Düz çizgi
      ctx.lineWidth = 1;
      ctx.strokeStyle = "rgba(148, 163, 184, 0.25)";
      ctx.beginPath();
      ctx.moveTo(0, canvas.height / 2);
      ctx.lineTo(canvas.width, canvas.height / 2);
      ctx.stroke();
    }
  }

  drawScope();
}

// Durum Rozeti Güncelleyici
function updateAudioStatus(isPlaying, text = "Hazır") {
  const badge = document.getElementById("audioStatusBadge");
  const overlay = document.getElementById("canvasOverlay");

  if (isPlaying) {
    badge.className = "status-badge playing";
    badge.innerText = `● ${text}`;
    if (overlay) overlay.style.opacity = "0";
  } else {
    badge.className = "status-badge ready";
    badge.innerText = "Ses Motoru: Hazır";
    if (overlay) overlay.style.opacity = "1";
  }
}

// ==========================================
// 5. ARAYÜZ GÖRSEL BİLEŞENLERİ (UI RENDERING)
// ==========================================
function renderSolfeggio() {
  const grid = document.getElementById("solfeggioGrid");
  grid.innerHTML = "";

  SOLFEGGIO_DATA.forEach(t => {
    const card = document.createElement("div");
    card.className = "solf-card";
    card.innerHTML = `
      <div class="solf-freq">${t.freq} Hz</div>
      <div class="solf-name">${t.name}</div>
      <div class="solf-chakra">Çakra: <span>${t.chakra}</span> (Nota: ${t.note})</div>
      <div class="solf-desc">${t.desc}</div>
      <button class="btn btn-sm btn-outline mt-2 play-solf-btn">Titreşimi Dinle</button>
    `;

    card.querySelector(".play-solf-btn").addEventListener("click", () => {
      document.querySelectorAll(".solf-card").forEach(c => c.classList.remove("playing"));
      card.classList.add("playing");
      audio.playTone(t.freq);
      cymaticsSim.setFrequency(t.freq);
    });

    grid.appendChild(card);
  });
}

function renderPlanetary() {
  const grid = document.getElementById("planetaryGrid");
  if (!grid) return;
  grid.innerHTML = "";

  PLANETARY_DATA.forEach(p => {
    const card = document.createElement("div");
    card.className = "planet-card";
    card.innerHTML = `
      <div class="planet-name">
        <span>${p.name}</span>
        <span class="planet-freq">${p.freq} Hz</span>
      </div>
      <div class="planet-cycle">🪐 ${p.cycle} (Nota: ${p.note} | ${p.chakra})</div>
      <p class="planet-effects">${p.desc}</p>
      <button class="btn btn-sm btn-outline mt-2 play-planet-btn">Kozmik Frekansı Çal</button>
    `;

    card.querySelector(".play-planet-btn").addEventListener("click", () => {
      document.querySelectorAll(".planet-card").forEach(c => c.classList.remove("playing"));
      card.classList.add("playing");
      audio.playTone(p.freq);
      cymaticsSim.setFrequency(p.freq);
    });

    grid.appendChild(card);
  });
}

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

// Kadim Bilgelik ve Alıntılar Kütüphanesini Render Et
let activeQuoteCategory = "all";
let currentQuoteSearch = "";
let currentBannerQuote = QUOTES_DATA[0];

function renderQuotes(category = "all", search = "") {
  const container = document.getElementById("quotesCardsList");
  if (!container) return;
  container.innerHTML = "";

  const normSearch = search.trim().toLowerCase();

  const filtered = QUOTES_DATA.filter(q => {
    const matchCat = category === "all" || q.category === category;
    const matchSearch = !normSearch || 
      q.author.toLowerCase().includes(normSearch) || 
      q.quote.toLowerCase().includes(normSearch) || 
      q.work.toLowerCase().includes(normSearch) || 
      q.reflection.toLowerCase().includes(normSearch);
    return matchCat && matchSearch;
  });

  if (filtered.length === 0) {
    container.innerHTML = `<p class="text-muted" style="text-align:center; padding: 24px;">Aradığınız kriterlere uygun alıntı bulunamadı.</p>`;
    return;
  }

  const catLabels = {
    tasavvuf: "Tasavvuf & İrfan",
    islam_tibbi: "İslam Müzikterapisi",
    antik_felsefe: "Antik Felsefe",
    bilim_ve_fizik: "Fizik & Akustik",
    mistik_akustik: "Mistik Akustik"
  };

  filtered.forEach(q => {
    const card = document.createElement("div");
    card.className = "wisdom-card";
    card.innerHTML = `
      <div class="wisdom-card-top">
        <div>
          <span class="wisdom-card-author">« ${q.author} »</span>
          <span class="wisdom-card-era">(${q.era})</span>
        </div>
        <span class="wisdom-card-cat-badge">${catLabels[q.category] || q.category}</span>
      </div>
      <div class="wisdom-card-work">Kaynak: <strong>${q.work}</strong></div>
      <div class="wisdom-card-quote">“${q.quote}”</div>
      <div class="wisdom-card-reflection">💡 <strong>Tefekkür:</strong> ${q.reflection}</div>
      <div class="wisdom-card-actions">
        <span class="wisdom-card-freq-tag">🎵 Uyumlu Ton: ${q.freq} Hz</span>
        <button class="btn btn-sm btn-outline-gold play-quote-btn">Rezonans Frekansını Dinle</button>
      </div>
    `;

    card.querySelector(".play-quote-btn").addEventListener("click", () => {
      audio.playTone(q.freq);
      if (cymaticsSim) {
        cymaticsSim.setFrequency(q.freq);
      }
    });

    container.appendChild(card);
  });
}

function setupWisdomBanner() {
  const quoteEl = document.getElementById("wisdomBannerQuote");
  const authorEl = document.getElementById("wisdomBannerAuthor");
  const workEl = document.getElementById("wisdomBannerWork");
  const reflEl = document.getElementById("wisdomBannerReflection");
  const freqValEl = document.getElementById("wisdomFreqVal");
  const nextBtn = document.getElementById("nextWisdomBtn");
  const playFreqBtn = document.getElementById("playWisdomFreqBtn");

  if (!quoteEl) return;

  function setQuote(q) {
    currentBannerQuote = q;
    quoteEl.innerText = `“${q.quote}”`;
    authorEl.innerText = `— ${q.author}`;
    workEl.innerText = `(${q.work})`;
    reflEl.innerText = `💡 ${q.reflection}`;
    freqValEl.innerText = q.freq;
  }

  // İlk rastgele alıntı
  setQuote(QUOTES_DATA[Math.floor(Math.random() * QUOTES_DATA.length)]);

  nextBtn.addEventListener("click", () => {
    let nextQ;
    do {
      nextQ = QUOTES_DATA[Math.floor(Math.random() * QUOTES_DATA.length)];
    } while (nextQ.id === currentBannerQuote.id && QUOTES_DATA.length > 1);
    setQuote(nextQ);
  });

  playFreqBtn.addEventListener("click", () => {
    audio.playTone(currentBannerQuote.freq);
    if (cymaticsSim) {
      cymaticsSim.setFrequency(currentBannerQuote.freq);
    }
  });
}

// Kalp Koheransı Nefes Rehberi (0.1 Hz)
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

// Seans Zamanlayıcısı
let sessionTimer = null;
let timerSecondsLeft = 0;

function setupSessionTimer() {
  const display = document.getElementById("timerCountdown");
  const cancelBtn = document.getElementById("cancelTimerBtn");

  document.querySelectorAll(".timer-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const minutes = parseInt(btn.getAttribute("data-minutes"), 10);
      startTimer(minutes * 60);
    });
  });

  cancelBtn.addEventListener("click", () => {
    stopTimer();
  });

  function startTimer(seconds) {
    stopTimer();
    timerSecondsLeft = seconds;
    cancelBtn.classList.remove("hidden");
    updateDisplay();

    sessionTimer = setInterval(() => {
      timerSecondsLeft--;
      if (timerSecondsLeft <= 0) {
        stopTimer();
        // Seans Tamamlandı - Tibet Çanağı Zili Çal
        audio.playTibetanBowl(528.0);
        alert("🧘 Meditasyon seansınız tamamlandı. Şifa olsun!");
      } else {
        updateDisplay();
      }
    }, 1000);
  }

  function stopTimer() {
    if (sessionTimer) {
      clearInterval(sessionTimer);
      sessionTimer = null;
    }
    cancelBtn.classList.add("hidden");
    display.innerText = "Sayaç: Kapalı";
  }

  function updateDisplay() {
    const mins = Math.floor(timerSecondsLeft / 60);
    const secs = timerSecondsLeft % 60;
    display.innerText = `Kalan: ${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  }
}

// ==========================================
// 6. BAŞLATICI (INITIALIZATION)
// ==========================================
document.addEventListener("DOMContentLoaded", () => {
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
      const targetContent = document.getElementById(targetId);
      if (targetContent) {
        targetContent.classList.add("active");
      }
    });
  });

  // Hızlı Frekans Butonları
  document.querySelectorAll(".quick-freq-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const freq = parseFloat(btn.getAttribute("data-freq"));
      audio.playTone(freq);
      cymaticsSim.setFrequency(freq);
    });
  });

  // Plaka Türü Değişimi (Kare vs Dairesel)
  const squareBtn = document.getElementById("squarePlateBtn");
  const circularBtn = document.getElementById("circularPlateBtn");
  const plateBadge = document.getElementById("plateTypeBadge");

  squareBtn.addEventListener("click", () => {
    squareBtn.classList.add("active");
    circularBtn.classList.remove("active");
    cymaticsSim.plateType = "square";
    plateBadge.innerText = "Kare Plaka";
    cymaticsSim.initParticles();
  });

  circularBtn.addEventListener("click", () => {
    circularBtn.classList.add("active");
    squareBtn.classList.remove("active");
    cymaticsSim.plateType = "circular";
    plateBadge.innerText = "Dairesel Çanak";
    cymaticsSim.initParticles();
  });

  // Chladni Slider Dinleyicileri
  const nSlider = document.getElementById("chladniN");
  const mSlider = document.getElementById("chladniM");

  nSlider.addEventListener("input", (e) => {
    cymaticsSim.setModes(parseInt(e.target.value, 10), parseInt(mSlider.value, 10));
  });

  mSlider.addEventListener("input", (e) => {
    cymaticsSim.setModes(parseInt(nSlider.value, 10), parseInt(e.target.value, 10));
  });

  // Parçacıkları Saç
  document.getElementById("scatterParticlesBtn").addEventListener("click", () => {
    cymaticsSim.initParticles();
  });

  // Ses Aç / Kapa
  document.getElementById("toggleAudioBtn").addEventListener("click", () => {
    if (audio.isPlayingSingle || audio.isPlayingBinaural || audio.isPlayingIso || audio.makamTimeouts.length > 0) {
      audio.stopTone();
      audio.stopBinaural();
      audio.stopIsochronic();
    } else {
      audio.playTone(cymaticsSim.currentFreq);
    }
  });

  // Dem / Tanpura Drone Butonu
  const toggleDroneBtn = document.getElementById("toggleDroneBtn");
  toggleDroneBtn.addEventListener("click", () => {
    const isNowPlaying = audio.toggleDrone(136.1);
    if (isNowPlaying) {
      toggleDroneBtn.innerText = "🕉️ Dem Tonu: Açık";
      toggleDroneBtn.classList.add("active");
    } else {
      toggleDroneBtn.innerText = "🕉️ Dem Tonu: Kapalı";
      toggleDroneBtn.classList.remove("active");
    }
  });

  // Canlı Ses Kayıt Butonu
  const recordBtn = document.getElementById("recordAudioBtn");
  recordBtn.addEventListener("click", () => {
    if (!audio.isRecording) {
      audio.startRecording();
      recordBtn.innerText = "⏹️ Kaydı Bitir & İndir";
      recordBtn.classList.add("recording");
    } else {
      audio.stopRecording();
      recordBtn.innerText = "⏺️ Seansı Kaydet";
      recordBtn.classList.remove("recording");
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

  // İzokronik Kontrolleri
  const isoCarrierSlider = document.getElementById("isoCarrierSlider");
  const isoPulseSlider = document.getElementById("isoPulseSlider");
  const isoCarrierVal = document.getElementById("isoCarrierVal");
  const isoPulseVal = document.getElementById("isoPulseVal");
  const isoBandName = document.getElementById("isoBandName");
  const toggleIsoBtn = document.getElementById("toggleIsoBtn");

  function getBandName(hz) {
    if (hz <= 4) return "Delta";
    if (hz <= 8) return "Teta";
    if (hz <= 13) return "Alfa";
    if (hz <= 30) return "Beta";
    return "Gama";
  }

  isoCarrierSlider.addEventListener("input", (e) => {
    isoCarrierVal.innerText = e.target.value;
    if (audio.isPlayingIso) {
      audio.playIsochronic(parseFloat(isoCarrierSlider.value), parseFloat(isoPulseSlider.value));
    }
  });

  isoPulseSlider.addEventListener("input", (e) => {
    const val = parseFloat(e.target.value);
    isoPulseVal.innerText = val.toFixed(1);
    isoBandName.innerText = getBandName(val);
    if (audio.isPlayingIso) {
      audio.playIsochronic(parseFloat(isoCarrierSlider.value), val);
    }
  });

  toggleIsoBtn.addEventListener("click", () => {
    if (audio.isPlayingIso) {
      audio.stopIsochronic();
      toggleIsoBtn.innerText = "⚡ İzokronik Nabzı Başlat";
    } else {
      const c = parseFloat(isoCarrierSlider.value);
      const p = parseFloat(isoPulseSlider.value);
      audio.playIsochronic(c, p);
      cymaticsSim.setFrequency(c);
      toggleIsoBtn.innerText = "⏹️ İzokronik Nabzı Durdur";
    }
  });

  // Akustik Gürültü Kontrolleri
  const noiseVolSlider = document.getElementById("noiseVolSlider");
  const noiseVolVal = document.getElementById("noiseVolVal");
  const stopNoiseBtn = document.getElementById("stopNoiseBtn");

  noiseVolSlider.addEventListener("input", (e) => {
    noiseVolVal.innerText = e.target.value;
    if (audio.noiseGain) {
      audio.noiseGain.gain.setValueAtTime(e.target.value / 100.0, audio.ctx.currentTime);
    }
  });

  document.querySelectorAll(".noise-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".noise-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      const type = btn.getAttribute("data-noise");
      const vol = parseFloat(noiseVolSlider.value) / 100.0;
      audio.playNoise(type, vol);
    });
  });

  stopNoiseBtn.addEventListener("click", () => {
    document.querySelectorAll(".noise-btn").forEach(b => b.classList.remove("active"));
    audio.stopNoise();
  });

  // Alıntılar Sekmesi Filtreleme ve Arama Dinleyicileri
  document.querySelectorAll(".quote-cat-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".quote-cat-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      activeQuoteCategory = btn.getAttribute("data-cat");
      renderQuotes(activeQuoteCategory, currentQuoteSearch);
    });
  });

  const quoteSearchInput = document.getElementById("quoteSearchInput");
  if (quoteSearchInput) {
    quoteSearchInput.addEventListener("input", (e) => {
      currentQuoteSearch = e.target.value;
      renderQuotes(activeQuoteCategory, currentQuoteSearch);
    });
  }

  // Verileri ve Alt Bileşenleri Başlat
  renderSolfeggio();
  renderPlanetary();
  renderMakamlar();
  renderTraditions();
  renderQuotes("all", "");
  setupBreathing();
  setupSessionTimer();
  setupWisdomBanner();
});
