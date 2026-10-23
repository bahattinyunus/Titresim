/**
 * Titreşim: Evrensel Ses, Kutsal Kelâm ve Frekans Terapisi Laboratuvarı v2.0
 * Web Audio API & Canlı Chladni Cymatics Simülasyon Motoru
 */

// ==========================================
// 1. DAHİLİ VERİLER (DATASETS)
// ==========================================
const ORGANS_DATA = [
  {
    "id": "heart",
    "name": "Kalp & Kardiyovasküler Sistem",
    "frequency": 136.1,
    "alternative_freqs": [
      528.0,
      10.5,
      639.0
    ],
    "category": "dolasim",
    "element": "Hava / Yangın",
    "associated_chakra": "Anahata (Kalp Çakrası)",
    "description": "Kalp kası ritmi, koroner dolaşım ve kan basıncı dengesi. 0.1 Hz vagal kilitlenme ve 136.1 Hz OM tonu ile rezonansa girer.",
    "effects": "Tansiyon dengesi, kardiyak ritim düzeni, duygusal ferahlık ve göğüs sıkışmasının giderilmesi.",
    "healing_protocol": "136.1 Hz taşıyıcı ton üzerinde 0.10 Hz izokronik modülasyon ile günde 15 dakika."
  },
  {
    "id": "brain",
    "name": "Beyin & Serebral Korteks",
    "frequency": 727.0,
    "alternative_freqs": [
      7.83,
      10.0,
      40.0
    ],
    "category": "sinir_sistemi",
    "element": "Eter / Işık",
    "associated_chakra": "Ajna & Sahasrara",
    "description": "Nöronal sinaps iletimi, beyin omurilik sıvısı (BOS) sirkülasyonu ve hemisferik senkronizasyon.",
    "effects": "Zihinsel berraklık, hafıza kuvvetlenmesi, baş ağrısı ve migren yatışması, nöroplastisite.",
    "healing_protocol": "727 Hz Rife tonu ve 7.83 Hz Schumann teta dalgası zeminli akustik banyo."
  },
  {
    "id": "liver",
    "name": "Karaciğer & Safra Dolaşımı",
    "frequency": 317.83,
    "alternative_freqs": [
      528.0,
      741.0
    ],
    "category": "sindirim_detoks",
    "element": "Ağaç / Ateş (Ahlat-ı Erba'a: Safra)",
    "associated_chakra": "Manipura (Solar Pleksus)",
    "description": "Vücudun ana kimya fabrikası, toksin filtreleme, enzim sentezi ve safra salgısı.",
    "effects": "Toksin arınması, safra akışkanlığı, kronik yorgunluk ve öfke halinin teskini.",
    "healing_protocol": "317.83 Hz ve 741 Hz temizleyici harmonikleriyle yemeklerden 1 saat sonra 12 dakika."
  },
  {
    "id": "kidneys",
    "name": "Böbrekler & Boşaltım Sistemi",
    "frequency": 319.88,
    "alternative_freqs": [
      54.0,
      210.42
    ],
    "category": "bosaltim_su",
    "element": "Su (Ahlat-ı Erba'a: Balgam)",
    "associated_chakra": "Svadhisthana (Sakral Çakra)",
    "description": "Sıvı ve elektrolit dengesi, kan filtrasyonu, böbreküstü bezleri kortizol regülasyonu.",
    "effects": "Ödem atımı, böbrek kumu ve sancılarının yatışması, yaşama enerjisinin (Jing) korunması.",
    "healing_protocol": "319.88 Hz rezonans tonu ile bol su tüketilerek dinlenen akşam seansı."
  },
  {
    "id": "lungs",
    "name": "Akciğerler & Solunum Yolları",
    "frequency": 220.0,
    "alternative_freqs": [
      432.0,
      741.0
    ],
    "category": "solunum",
    "element": "Metal / Hava",
    "associated_chakra": "Anahata & Vishuddha",
    "description": "Oksijen-karbondioksit difüzyonu, bronşiyol esnekliği ve göğüs kafesi genişlemesi.",
    "effects": "Derin nefes kapasitesi, astım ve nefes darlığı teskini, hüzün ve kederin dağıtılması.",
    "healing_protocol": "220 Hz Rast tonu ve diyafram nefesi rehberliği eşliğinde 10 dakika."
  },
  {
    "id": "stomach",
    "name": "Mide & Bağırsaklar (İkinci Beyin)",
    "frequency": 110.0,
    "alternative_freqs": [
      528.0,
      126.22
    ],
    "category": "sindirim_detoks",
    "element": "Toprak / Ateş",
    "associated_chakra": "Manipura (Solar Pleksus)",
    "description": "Mide asidi dengesi, enterik sinir sistemi, serotonin üretimi ve bağırsak mikrobiyotası.",
    "effects": "Gastrit ve reflü yatışması, hazımsızlık giderimi, anksiyete kaynaklı karın krampları çözümü.",
    "healing_protocol": "110 Hz derin bas tonu ile karın bölgesine odaklanarak dinleme."
  },
  {
    "id": "pineal_gland",
    "name": "Epifiz Bezi (Pineal / Üçüncü Göz)",
    "frequency": 963.0,
    "alternative_freqs": [
      852.0,
      221.23
    ],
    "category": "endokrin",
    "element": "Işık / Saf Bilinç",
    "associated_chakra": "Ajna & Sahasrara",
    "description": "Melatonin ve DMT sentezi, sirkadiyen biyolojik saat ve manevi algı merkezi.",
    "effects": "Kireçlenmiş epifizin titreşimle uyarılması, derin rüya farkındalığı ve sirkadiyen uyum.",
    "healing_protocol": "963 Hz Solfeggio tonu ile karanlık ve sessiz ortamda gece meditasyonu."
  },
  {
    "id": "thyroid",
    "name": "Tiroid & Paratiroid Bezleri",
    "frequency": 741.0,
    "alternative_freqs": [
      141.27,
      293.33
    ],
    "category": "endokrin",
    "element": "Eter / Ses",
    "associated_chakra": "Vishuddha (Boğaz Çakrası)",
    "description": "Metabolizma hızı, T3/T4 hormon dengesi, kalsiyum regülasyonu ve vokal kordlar.",
    "effects": "Metabolik canlanma, boğaz tıkanıklığı hissinin dağılması ve ses berraklığı.",
    "healing_protocol": "741 Hz Solfeggio ve boğaz formantı rezonansı ile sabah seansı."
  },
  {
    "id": "bones_spine",
    "name": "Kemikler, Omurga & Eklemler",
    "frequency": 194.18,
    "alternative_freqs": [
      396.0,
      174.0
    ],
    "category": "iskelet_kas",
    "element": "Toprak (Prithvi)",
    "associated_chakra": "Muladhara (Kök Çakra)",
    "description": "Piezoelektrik kemik matriksi, kemik iliği hücresel üretimi ve omurga dikliği.",
    "effects": "Bel ve boyun ağrılarının yatışması, kemik yoğunluğu desteği, güçlü topraklanma.",
    "healing_protocol": "194.18 Hz (Dünya Günü) tonu ve 174 Hz fiziksel anestezi frekansı kombinasyonu."
  },
  {
    "id": "thymus",
    "name": "Timus Bezi (Bağışıklık & Şefkat)",
    "frequency": 639.0,
    "alternative_freqs": [
      528.0,
      352.0
    ],
    "category": "bagisiklik_endokrin",
    "element": "Hava (Vayu)",
    "associated_chakra": "Anahata (Kalp Çakrası)",
    "description": "T-lenfositlerinin olgunlaşması, hücresel bağışıklık ve sevgi/şefkat duygusunun nöral merkezi.",
    "effects": "Bağışıklık sisteminin uyarılması, timus vurusu (thymus tap) etkisi, kalp açılımı.",
    "healing_protocol": "639 Hz ve göğüs üzerine hafif mekanik vuruşlarla eşzamanlı dinleme."
  }
];

const PHONETICS_DATA = [
  {
    "id": "hu",
    "name": "HÛ (İlahi Öz ve Mutlak Gayb)",
    "tradition": "Tasavvuf / İrfan Geleneği",
    "formants": [
      300,
      800,
      2400
    ],
    "base_pitch_hz": 136.1,
    "mahref": "Cevf & Boğaz Kökü (Aksâ-i Halk)",
    "description": "Nefes verişin en saf hali. Dudakların yuvarlanmasıyla boğazın en derininden çıkan 'H' sesi ve derin 'U' uzatması.",
    "effects": "Egonun çözünmesi, kalp koheransı, parasempatik derin gevşeme ve zihinsel sükût.",
    "nitric_oxide_effect": "Vagus sinirinin göğüs dalını uyarır; diyaframı tamamen boşaltarak kan basıncını düşürür."
  },
  {
    "id": "hayy",
    "name": "HAYY (Ezeli ve Ebedi Canlılık)",
    "tradition": "Tasavvuf / İrfan Geleneği",
    "formants": [
      270,
      2200,
      2800
    ],
    "base_pitch_hz": 220.0,
    "mahref": "Boğaz Ortası (Vast-ı Halk) ve Dil Ortası (Cim/Şın/Ye)",
    "description": "Nefes alışın ve dirilişin sesi. 'Ha' harfinin boğazı yırtarcasına açılması ve 'Y' harfinin damağa yükselmesi.",
    "effects": "Hücresel canlanma, enerji kanallarının (Nadi/Meridyen) açılması, melankoli ve uyuşukluğun dağılması.",
    "nitric_oxide_effect": "Boğaz ve laringeal mukozayı uyararak sempatik/parasempatik dengeyi hızla kurar."
  },
  {
    "id": "hakk",
    "name": "HAKK (Mutlak Gerçeklik ve Adalet)",
    "tradition": "Tasavvuf / İrfan Geleneği",
    "formants": [
      350,
      1100,
      2600
    ],
    "base_pitch_hz": 196.0,
    "mahref": "Boğaz Kökü ve Dil Kökü (Kaf Harfi patlaması)",
    "description": "Kaf (Qaf) harfinin küçük dile vurarak patlamasıyla oluşan tok ve kararlı akustik rezonans.",
    "effects": "Zihinsel kararlılık, irade kuvveti, şüphe ve vesveselerin kökten kesilmesi.",
    "nitric_oxide_effect": "Kraniyal kemiklerde kemik iletimli (bone conduction) mikro-şok dalgası oluşturur."
  },
  {
    "id": "allah",
    "name": "ALLAH (Lafzatullah / İsmi Celâl)",
    "tradition": "İslam Vahiy Geleneği",
    "formants": [
      750,
      1200,
      2500
    ],
    "base_pitch_hz": 216.0,
    "mahref": "Boğaz Kökü (Hemze), Dil Yanı (Kalın Lâm) ve Boğaz (He)",
    "description": "Elif'ten Lâm'a ve Lâm'dan He'ye akan tam göğüs ve kalp rezonatörü. Açık vokal ile başlayan ve kalbe inen ses.",
    "effects": "Tüm endokrin ve sinir sisteminin bir anda senkronize olması; mutlak emniyet ve aşk hali.",
    "nitric_oxide_effect": "Tüm torasik kaviteyi titreştirerek kalp hızı değişkenliğinde (HRV) anında koherans sağlar."
  },
  {
    "id": "ghunnah_noon",
    "name": "GUNNE (Nazal Tını & Nûn/Mîm İdgamı)",
    "tradition": "Kur'ân-ı Kerîm Tecvid İlmi",
    "formants": [
      250,
      1800,
      2600
    ],
    "base_pitch_hz": 174.0,
    "mahref": "Hayşûm (Geniz ve Paranazal Sinüs Boşluğu)",
    "description": "Tecvidde iki hareke miktarı genizden gelen yumuşak çınlama sesi. Sesin burun kemiklerinde titreştirilmesi.",
    "effects": "Paranazal sinüslerde 15 kat artan Nitrik Oksit (NO) sentezi, kranial rahatlama, bronkodilatasyon.",
    "nitric_oxide_effect": "Dr. Weitzberg ve Lundberg araştırmaları: Nazal tını (humming/gunne) sinüslerdeki Nitrik Oksit (NO) üretimini 15 ila 20 kat artırır."
  },
  {
    "id": "aum_om",
    "name": "AUM / OM (Pranava Kozmik Hecesi)",
    "tradition": "Vedik ve Upanişad Geleneği",
    "formants": [
      300,
      850,
      2300
    ],
    "base_pitch_hz": 136.1,
    "mahref": "Boğazdan Dudaklara (A -> U -> M Üçlemesi)",
    "description": "Uyanıklık (A), rüya (U) ve derin uyku (M) hallerini birleştiren tam beden rezonans hecesi.",
    "effects": "Epifiz uyarımı, limbik sistem sakinleşmesi, zihinsel gürültünün susturulması.",
    "nitric_oxide_effect": "Dudakların kapanmasıyla 'M' sesinde sinüs rezonansı ve serebral kan akışında artış."
  },
  {
    "id": "shalom_selam",
    "name": "ŞALOM / SELÂM (Esenlik ve Barış)",
    "tradition": "Samî / İbrahîmî Gelenek",
    "formants": [
      400,
      1600,
      2500
    ],
    "base_pitch_hz": 432.0,
    "mahref": "Dil Ucu (Ş/S) ve Dudaklar (M)",
    "description": "Dudakların kapanışıyla sükûnete eren evrensel esenlik ve selâmet frekansı.",
    "effects": "Sosyal bağ kurma, amigdala korku refleksinin baskılanması, affedicilik.",
    "nitric_oxide_effect": "Yumuşak fısıltı ve dudak kapanışı ile vagal fren uyarımı."
  },
  {
    "id": "amen_amin",
    "name": "ÂMÎN / AMEN (Öyle Olsun ve Kabul Buyur)",
    "tradition": "Evrensel Dua Geleneği",
    "formants": [
      650,
      1300,
      2400
    ],
    "base_pitch_hz": 528.0,
    "mahref": "Açık Boğazdan (A) Nazal Dudaklara (M/N)",
    "description": "Duanın mührü. Açık bir yakarışla başlayıp teslimiyetle genizde yankılanan kapanış.",
    "effects": "Niyetin kilitlenmesi, nöral tamamlama ve rahatlama hissi.",
    "nitric_oxide_effect": "Akciğer alveollerinde relaksasyon ve derin soluk verme."
  }
];

const CHAKRAS_DATA = [
  {
    id: "muladhara",
    name: "Muladhara (Kök Çakra)",
    location: "Omurga tabanı, kuyruk sokumu",
    element: "Toprak (Prithvi)",
    solfeggio_freq: 396.0,
    planetary_freq: 194.18,
    bija_mantra: "LAM",
    color: "#ef4444",
    note: "C (Do)",
    organs: "Bağışıklık sistemi, kemikler, bacaklar, böbrek üstü bezleri",
    balance_effect: "Korkulardan arınma, dünyada güvende hissetme, güçlü topraklanma.",
    imbalance_symptoms: "Sürekli kaygı, maddi güvensizlik, bel ağrısı, panik atak."
  },
  {
    id: "svadhisthana",
    name: "Svadhisthana (Sakral Çakra)",
    location: "Göbeğin altı, pelvis bölgesi",
    element: "Su (Apas)",
    solfeggio_freq: 417.0,
    planetary_freq: 210.42,
    bija_mantra: "VAM",
    color: "#f97316",
    note: "D (Re)",
    organs: "Üreme organları, mesane, lenf dolaşımı, böbrekler",
    balance_effect: "Duygusal akışkanlık, yaratıcılık, yaşama sevinci ve travma çözümü.",
    imbalance_symptoms: "Duygusal donukluk, suçluluk hissi, yaratıcı tıkanıklık, bağımlılıklar."
  },
  {
    id: "manipura",
    name: "Manipura (Solar Pleksus)",
    location: "Mide boşluğu, diyafram altı",
    element: "Ateş (Agni)",
    solfeggio_freq: 528.0,
    planetary_freq: 126.22,
    bija_mantra: "RAM",
    color: "#eab308",
    note: "E (Mi)",
    organs: "Mide, karaciğer, safra kesesi, pankreas, sindirim sistemi",
    balance_effect: "Kişisel güç, irade, özgüven, DNA düzeyinde canlılık ve neşe.",
    imbalance_symptoms: "Özgüven eksikliği, kontrol takıntısı, mide ülseri, sindirim sorunları."
  },
  {
    id: "anahata",
    name: "Anahata (Kalp Çakrası)",
    location: "Göğüs kafesi merkezi",
    element: "Hava (Vayu)",
    solfeggio_freq: 639.0,
    planetary_freq: 136.10,
    bija_mantra: "YAM",
    color: "#22c55e",
    note: "F (Fa)",
    organs: "Kalp, akciğerler, timus bezi, kan dolaşımı",
    balance_effect: "Koşulsuz sevgi, şefkat, affedicilik, vagal kalp koheransı.",
    imbalance_symptoms: "Kırgınlık, kıskançlık, yalnızlık hissi, solunum darlığı, çarpıntı."
  },
  {
    id: "vishuddha",
    name: "Vishuddha (Boğaz Çakrası)",
    location: "Boğaz çukuru",
    element: "Eter (Akasha)",
    solfeggio_freq: 741.0,
    planetary_freq: 141.27,
    bija_mantra: "HAM",
    color: "#06b6d4",
    note: "G (Sol)",
    organs: "Boğaz, tiroid, ses telleri, boyun omurları",
    balance_effect: "Hakikati söyleme, duru ifade, sezgisel uyanış, hücresel detoks.",
    imbalance_symptoms: "Kendini ifade edememe, yalan söyleme, tiroid bozukluğu, boğaz enfeksiyonları."
  },
  {
    id: "ajna",
    name: "Ajna (Üçüncü Göz)",
    location: "İki kaşın ortası",
    element: "Işık / Saf Akıl",
    solfeggio_freq: 852.0,
    planetary_freq: 221.23,
    bija_mantra: "AUM",
    color: "#6366f1",
    note: "A (La)",
    organs: "Epifiz bezi, beyin yarıküreleri, gözler, sinir sistemi",
    balance_effect: "Ruhsal basiret, berrak sezgi, derin odak ve tefekkür gücü.",
    imbalance_symptoms: "Zihinsel bulanıklık, kabuslar, baş ağrısı, gerçeklikten kopukluk."
  },
  {
    id: "sahasrara",
    name: "Sahasrara (Taç Çakra)",
    location: "Başın tepe noktası (bıngıldak)",
    element: "Saf Bilinç / Kozmik Eter",
    solfeggio_freq: 963.0,
    planetary_freq: 172.06,
    bija_mantra: "OM",
    color: "#a855f7",
    note: "B (Si)",
    organs: "Serebral korteks, hipofiz bezi, merkezi sinir sistemi",
    balance_effect: "Birlik şuuru, aşkın huzur, kozmik aidiyet ve aydınlanma.",
    imbalance_symptoms: "Yabancılaşma, varoluşsal kriz, derin yalnızlık, manevi anlamsızlık."
  }
];

const PROTOCOLS_DATA = [
  {
    id: "deep_sleep_regeneration",
    title: "Derin Uyku & Hücresel Yenilenme Protokolü",
    subtitle: "Alfa'dan Delta'ya kademeli nöral yavaşlama ve hücre onarımı",
    target: "İnsomnia, uyku kalitesi düşüklüğü, kronik yorgunluk ve hücresel stres",
    total_recommended_minutes: 30,
    stages: [
      { stage: 1, name: "Zihinsel Sakinleşme & Günün Yükünü Bırakma", duration_percent: 25, carrier_freq: 432.0, beat_freq: 10.0, band: "Alfa", noise_type: "pink", noise_volume: 0.04, description: "Zihni meşgul eden düşünceleri yavaşlatır, parasempatik sisteme yumuşak geçiş sağlar." },
      { stage: 2, name: "Derin Gevşeme & Alacakaranlık Hali", duration_percent: 35, carrier_freq: 285.0, beat_freq: 5.5, band: "Teta", noise_type: "brown", noise_volume: 0.05, description: "Kas gerginliğini çözer, solunum ve kalp atışını gece ritmine senkronize eder." },
      { stage: 3, name: "Hücresel Onarım & Yavaş Dalga Uykusu", duration_percent: 40, carrier_freq: 174.0, beat_freq: 1.5, band: "Delta", noise_type: "brown", noise_volume: 0.06, description: "Büyüme hormonu salınımını tetikler, derin rüyasız uykuda doku yenilenmesini destekler." }
    ]
  },
  {
    id: "flow_state_focus",
    title: "Yüksek Odaklanma & Zihinsel Akış (Flow State)",
    subtitle: "Gama dalgası senkronizasyonu ile berrak kavrayış ve dikkat",
    target: "Çalışma, derin okuma, problem çözme ve dikkat dağınıklığını giderme",
    total_recommended_minutes: 25,
    stages: [
      { stage: 1, name: "Zihinsel Isınma & Odak Kilidi", duration_percent: 20, carrier_freq: 432.0, beat_freq: 14.0, band: "Düşük Beta", noise_type: "white", noise_volume: 0.02, description: "Dış dikkat dağıtıcıları maskeleyerek zihni çalışma masasına sabitler." },
      { stage: 2, name: "Derin Konsantrasyon & Bilişsel Hız", duration_percent: 50, carrier_freq: 528.0, beat_freq: 20.0, band: "Beta", noise_type: "pink", noise_volume: 0.03, description: "Sol ve sağ beyin küreleri arasında bilgi akışını hızlandırır." },
      { stage: 3, name: "Gama Akış Doruğu (Insight & Eureka)", duration_percent: 30, carrier_freq: 528.0, beat_freq: 40.0, band: "Gama", noise_type: "pink", noise_volume: 0.02, description: "Karmaşık kavramları sentezleme, yaratıcı kıvılcım ve yüksek farkındalık hali." }
    ]
  },
  {
    id: "darussifa_anxiety_relief",
    title: "Darüşşifa Anksiyete & Ruhî Sükun Protokolü",
    subtitle: "Nihavend & Rast makamları ve Schumann rezonansı ile panik yatıştırma",
    target: "Panik atak, yaygın anksiyete, kalp çarpıntısı ve zihinsel kuruntu",
    total_recommended_minutes: 20,
    stages: [
      { stage: 1, name: "Nihavend Teskini (Kan Basıncı & Nabız Dengesi)", duration_percent: 30, carrier_freq: 261.63, beat_freq: 7.83, band: "Schumann Teta", noise_type: "pink", noise_volume: 0.03, description: "Yüksek tansiyonu ve hızlı nabzı yatıştırır; darüşşifa hekimlerinin öğle reçetesi." },
      { stage: 2, name: "Rast Sefa & Göğüs Ferahlığı", duration_percent: 40, carrier_freq: 392.0, beat_freq: 6.0, band: "Teta", noise_type: "pink", noise_volume: 0.03, description: "Korku ve daralma hissini dağıtır, melankoli ve iç sıkıntısını sefaya çevirir." },
      { stage: 3, name: "Kozmik İtidal & Topraklanma (Om Tınısı)", duration_percent: 30, carrier_freq: 136.1, beat_freq: 4.5, band: "Derin Teta", noise_type: "brown", noise_volume: 0.04, description: "Yerçekimi ve dünya frekansıyla yeniden bağ kurarak emniyet hissini kalıcı kılar." }
    ]
  },
  {
    id: "heart_coherence_vagus",
    title: "Kalp Koheransı & Vagal Tonlama (0.1 Hz)",
    subtitle: "Solunum ve kalp hızı değişkenliği (HRV) senkronizasyonu",
    target: "Otonom sinir sistemi dengesizliği, tükenmişlik ve duygusal dalgalanmalar",
    total_recommended_minutes: 15,
    stages: [
      { stage: 1, name: "Diyafram Nefesi & Ritim Oturtma", duration_percent: 30, carrier_freq: 528.0, beat_freq: 10.0, band: "Alfa", noise_type: "pink", noise_volume: 0.02, description: "5 saniye nefes alış, 5 saniye veriş temposu için akustik zemin kurar." },
      { stage: 2, name: "Rezonans Frekansı Kilitlenmesi (0.1 Hz)", duration_percent: 50, carrier_freq: 639.0, beat_freq: 6.0, band: "Teta", noise_type: "pink", noise_volume: 0.03, description: "Baroreseptör refleksini tetikleyerek vagus sinirini güçlendirir." },
      { stage: 3, name: "Şefkat & Duygusal Denge", duration_percent: 20, carrier_freq: 432.0, beat_freq: 7.83, band: "Schumann", noise_type: "brown", noise_volume: 0.03, description: "Kalp manyetik alanını koherent hale getirir, içsel şefkat alanını genişletir." }
    ]
  },
  {
    id: "cellular_detox_solfeggio",
    title: "Hücresel Detoks & Enerji Meridyenleri Temizliği",
    subtitle: "Solfeggio 741 Hz, 528 Hz ve Karaciğer/Bağışıklık Rezonansı",
    target: "Bedensel toksin birikimi, halsizlik, lenf durgunluğu ve elektromanyetik sis",
    total_recommended_minutes: 25,
    stages: [
      { stage: 1, name: "Toksin Salımı & Arınma (741 Hz)", duration_percent: 35, carrier_freq: 741.0, beat_freq: 8.0, band: "Alfa", noise_type: "pink", noise_volume: 0.03, description: "Hücre zarından ağır metal ve metabolik atık salımını titreşimle destekler." },
      { stage: 2, name: "DNA & Matris Onarımı (528 Hz)", duration_percent: 40, carrier_freq: 528.0, beat_freq: 5.0, band: "Teta", noise_type: "brown", noise_volume: 0.03, description: "Su moleküler yapısını altıgen kümelere düzenleyerek hücre içi hidrasyonu artırır." },
      { stage: 3, name: "Canlılık & Yaşam Gücü Entegrasyonu", duration_percent: 25, carrier_freq: 285.0, beat_freq: 10.0, band: "Alfa", noise_type: "white", noise_volume: 0.02, description: "Doku yenilenmesini hızlandırır, meridyen hatlarını açık ve canlı tutar." }
    ]
  }
];

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
    "id": "tesla_energy_vibration",
    "author": "Nikola Tesla",
    "era": "19. - 20. Yüzyıl (1856 - 1943)",
    "work": "Kişisel Notlar ve Röportajlar",
    "quote": "Evrenin sırrını bulmak istiyorsanız; enerji, frekans ve titreşim cinsinden düşünün.",
    "category": "bilim_ve_fizik",
    "freq": 432.0,
    "reflection": "Madde sandığımız katılık, belirli frekanslarda kilitlenmiş yoğun enerjiden ibarettir."
  },
  {
    "id": "tesla_369",
    "author": "Nikola Tesla",
    "era": "19. - 20. Yüzyıl (1856 - 1943)",
    "work": "Elektromanyetik Araştırmalar",
    "quote": "3, 6 ve 9 sayılarının ihtişamını bilseydiniz, evrenin anahtarına sahip olurdunuz.",
    "category": "bilim_ve_fizik",
    "freq": 396.0,
    "reflection": "Solfeggio frekanslarının tümü (396, 417, 528, 639, 741, 852, 963) rakam kökü toplamında 3, 6 veya 9'a indirgenir."
  },
  {
    "id": "einstein_future_medicine",
    "author": "Albert Einstein",
    "era": "20. Yüzyıl (1879 - 1955)",
    "work": "Bilimsel Aforizmalar",
    "quote": "Geleceğin tıbbı, frekanslar tıbbı olacaktır.",
    "category": "bilim_ve_fizik",
    "freq": 528.0,
    "reflection": "Biyokimyasal moleküller yerine dokuların doğal rezonans frekanslarıyla etkileşim kuran akustik şifa."
  },
  {
    "id": "einstein_energy_match",
    "author": "Albert Einstein",
    "era": "20. Yüzyıl (1879 - 1955)",
    "work": "Görelilik ve Kuantum Mektupları",
    "quote": "Her şey enerjidir ve her şey sadece bundan ibarettir. Sahip olmak istediğiniz gerçekliğin frekansına uyum sağladığınızda, artık o gerçeğe sahip olursunuz. Bu bir felsefe değil, fiziktir.",
    "category": "bilim_ve_fizik",
    "freq": 136.1,
    "reflection": "İçsel durumunuzun frekansı, yaşamınızın rezonans alanını belirler."
  },
  {
    "id": "mevlana_ney_dinle",
    "author": "Mevlânâ Celâleddîn-i Rûmî",
    "era": "13. Yüzyıl (1207 - 1273)",
    "work": "Mesnevî-i Mânevî (1. Beyit)",
    "quote": "Bişnev in ney çün şikâyet mî-kuned / Ez cüdâyîhâ hikâyet mî-kuned: Dinle neyden kim hikâyet etmededir; ayrılıklardan şikâyet etmededir. Kamışlıktan kesildim kesile, feryadımdan kadın-erkek herkes inledi.",
    "category": "tasavvuf",
    "freq": 220.0,
    "reflection": "Ney, içi boşaltılmış ve ilahi nefese ayna olmuş kamil insanın; ayrıldığı asıl vatanına duyduğu iştiyakın sesidir."
  },
  {
    "id": "mevlana_ney_dost",
    "author": "Mevlânâ Celâleddîn-i Rûmî",
    "era": "13. Yüzyıl (1207 - 1273)",
    "work": "Dîvân-ı Kebîr",
    "quote": "Biz birer ney gibiyiz; bizdeki nağmeler Senden gelir ey Dost! Biz bir dağ gibiyiz; bizdeki seda Senin sesinin yankısıdır.",
    "category": "tasavvuf",
    "freq": 136.1,
    "reflection": "Varlık, Hakk'ın nefesinin kozmik kamışta çıkardığı kesintisiz bir nağmeden ibarettir."
  },
  {
    "id": "mevlana_sama_ruhun_gidasi",
    "author": "Mevlânâ Celâleddîn-i Rûmî",
    "era": "13. Yüzyıl (1207 - 1273)",
    "work": "Fîhi Mâ Fîh",
    "quote": "Semâ, âşıkların gıdasıdır; zira onda cananın hayali ve vuslatın kokusu vardır. Ruhun perdesini aralayan ses, insanı ötelerle buluşturur.",
    "category": "tasavvuf",
    "freq": 432.0,
    "reflection": "Ritmik dönüş ve musiki, zihni susturarak kalbi merkeze oturtan akustik bir ibadettir."
  },
  {
    "id": "ibn_sina_musiki_sifasi",
    "author": "İbn-i Sînâ (Avicenna)",
    "era": "10. - 11. Yüzyıl (980 - 1037)",
    "work": "El-Kânûn fi't-Tıbb (Tıbbın Kanunu) & Şifâ",
    "quote": "Tedavinin en iyi, en tesirli ve en zararsız yollarından biri; hastanın aklî ve ruhî kuvvetlerini artırmak, ona cesaret vermek, onu güzel kokular ve hoşuna giden musiki ile çevrelemektir.",
    "category": "islam_tibbi",
    "freq": 220.0,
    "reflection": "İbn-i Sina'ya göre hekim sadece bedeni değil, ruhun mizacını nağmelerle mizanına getiren kişidir."
  },
  {
    "id": "ibn_sina_nabiz_ve_makam",
    "author": "İbn-i Sînâ (Avicenna)",
    "era": "10. - 11. Yüzyıl (980 - 1037)",
    "work": "Risâle fi'n-Nabz (Nabız Risalesi)",
    "quote": "Nabzın vuruşları ile musiki perdeleri arasında tam bir tenasüp (oran) vardır. Hekim, hastanın nabzındaki aksaklığı müziğin usûlü ve makamı ile teşhis edip tedavi edebilir.",
    "category": "islam_tibbi",
    "freq": 293.33,
    "reflection": "Kalp atışı bir perküsyon, damarlar ise telli sazdır; makamlar nabzın bozulan veznini düzeltir."
  },
  {
    "id": "farabi_makamlarin_tesiri",
    "author": "Fârâbî (Alpharabius)",
    "era": "9. - 10. Yüzyıl (872 - 950)",
    "work": "Kitâbü'l-Mûsîka'l-Kebîr (Büyük Musiki Kitabı)",
    "quote": "Rast makamı insana sefa (huzur ve neşe), Rehavi makamı beka (sonsuzluk fikri), Kuçek makamı hüzün, Büzürk makamı havf (korkuyu giderme), Isfahan makamı itimat ve zeka, Buselik makamı kuvvet, Zirgüle makamı uyku verir.",
    "category": "islam_tibbi",
    "freq": 220.0,
    "reflection": "Farabi, makamların insan psikolojisi ve hormonları üzerindeki kesin tesirlerini ilk kez sistemleştiren bilgedir."
  },
  {
    "id": "farabi_ruh_ve_ahenk",
    "author": "Fârâbî (Alpharabius)",
    "era": "9. - 10. Yüzyıl (872 - 950)",
    "work": "İhsâü'l-Ulûm (İlimlerin Sayımı)",
    "quote": "Musiki öyle yüce bir ilimdir ki, ruhun kabalıklarını yontar, ahlakı güzelleştirir ve aklı ilahi nizama hazırlar.",
    "category": "islam_tibbi",
    "freq": 432.0,
    "reflection": "Ahenk, ruhun dağınıklığını toparlayan manevi bir mıknatıstır."
  },
  {
    "id": "pythagoras_musica_universalis",
    "author": "Pisagor (Pythagoras)",
    "era": "M.Ö. 6. Yüzyıl (M.Ö. 570 - 495)",
    "work": "Pisagoryen Sözlü Gelenek",
    "quote": "Gözler için gök kubbe ve yıldızlar ne ise, kulaklar için de ses ve armoni odur. Gezegenlerin her biri dönerken ilahi bir ses çıkarır; gökler kesintisiz bir 'Kürelerin Müziği' (Musica Universalis) icra eder.",
    "category": "antik_felsefe",
    "freq": 216.0,
    "reflection": "Pisagor'a göre evren sayı ve oranlardan örülmüştür; müzik ise sayıların işitilebilir suretidir."
  },
  {
    "id": "pythagoras_sayi_ve_armoni",
    "author": "Pisagor (Pythagoras)",
    "era": "M.Ö. 6. Yüzyıl (M.Ö. 570 - 495)",
    "work": "Pisagoryen Fragmanlar",
    "quote": "Geometri, maddenin mekândaki nizamıdır; musiki ise zamanın nizamıdır.",
    "category": "antik_felsefe",
    "freq": 432.0,
    "reflection": "Zaman içinde salınan her form müziktir, mekânda donan her müzik mimaridir."
  },
  {
    "id": "plato_music_soul",
    "author": "Platon (Eflatun)",
    "era": "M.Ö. 5. - 4. Yüzyıl (M.Ö. 427 - 347)",
    "work": "Devlet (Respublica)",
    "quote": "Müzik, ruha kanat verir, zihne uçuş gücü aşılar, hayal gücünü tutuşturur, hüzün perdesini yırtar ve tüm varoluşa neşe ve hayat bahşeder. O, düzenin ve erdemin en asil muallimidir.",
    "category": "antik_felsefe",
    "freq": 528.0,
    "reflection": "Müzik eğitimi alan bir ruh, evrendeki çirkinliği ve uyumsuzluğu sezgisel olarak hemen fark eder."
  },
  {
    "id": "confucius_music_state",
    "author": "Konfüçyüs (Kongzi)",
    "era": "M.Ö. 6. - 5. Yüzyıl (M.Ö. 551 - 479)",
    "work": "Li Ji (Ayinler Kitabı - Yue Ji)",
    "quote": "Bir toplumun ahlakını ve ruhunu dönüştürmek, nizamını tesis etmek istiyorsanız; işe onların müziğini tanzim etmekle başlayın. Asil müzik kalpleri birleştirir, yozlaşmış müzik ise cemiyeti çürütür.",
    "category": "antik_felsefe",
    "freq": 136.1,
    "reflection": "Bir medeniyetin müziğindeki armoni ve dinginlik, onun ahlaki seviyesinin doğrudan aynasıdır."
  },
  {
    "id": "hermes_vibration_principle",
    "author": "Hermes Trismegistus",
    "era": "Antik Mısır & İskenderiye Geleneği",
    "work": "Kybalion (Titreşim Prensibi)",
    "quote": "Hiçbir şey durmaz; her şey hareket eder; her şey titreşir. Saf Ruhtan en kaba maddeye kadar her varoluş hali, yalnızca farklı titreşim derecelerinden ibarettir.",
    "category": "antik_felsefe",
    "freq": 7.83,
    "reflection": "Titreşim hızını değiştiren simyacı, maddenin ve zihnin doğasını da dönüştürür."
  },
  {
    "id": "kuran_kun_fe_yekun",
    "author": "Kur'ân-ı Kerîm",
    "era": "Vahiy Geleneği",
    "work": "Yâsîn Sûresi, 82. Âyet",
    "quote": "İnnemâ emruhû izâ erâde şey'en en yekûle lehu kün fe-yekûn: O'nun emri, bir şeyi dilediği vakit sadece ona 'Kün!' (Ol!) demektir; o şey de hemen oluverir.",
    "category": "tasavvuf",
    "freq": 528.0,
    "reflection": "Kozmik yaradılış 'Kün' ilahi kelâmının, titreşim ve ses formunda tecelli etmesiyle başlamıştır."
  },
  {
    "id": "kuran_tertil",
    "author": "Kur'ân-ı Kerîm",
    "era": "Vahiy Geleneği",
    "work": "Müzzemmil Sûresi, 4. Âyet",
    "quote": "Ve rattili'l-Kur'âne tertîlâ: Ve Kur'ân'ı tertil ile (tane tane, harflerin hakkını vererek, derin bir ahenk ve huşu içinde) oku.",
    "category": "tasavvuf",
    "freq": 110.0,
    "reflection": "Tertil, harflerin mahreç titreşimlerini ve nefes ritmini kalp koheransı ile buluşturan rezonans disiplinidir."
  },
  {
    "id": "ibrahim_hakki_marifetname",
    "author": "Erzurumlu İbrahim Hakkı",
    "era": "18. Yüzyıl (1703 - 1780)",
    "work": "Mârifetnâme",
    "quote": "Hak şerleri hayr eyler / Zannetme ki gayr eyler / Ârif ânı seyr eyler / Mevlâ görelim neyler / Neylerse güzel eyler... Ses ve nefes, can mülkünün cananıdır; doğru nağme dertlilere dermandır.",
    "category": "tasavvuf",
    "freq": 220.0,
    "reflection": "İbrahim Hakkı, Marifetname'sinde makamların, burçların ve insan tabiatlarının sesle dengelenmesini teferruatıyla açıklar."
  },
  {
    "id": "suuri_hasan_efendi",
    "author": "Şuûrî Hasan Efendi",
    "era": "17. Yüzyıl",
    "work": "Ta'dîl-i Emzice (Mizaçların Düzenlenmesi)",
    "quote": "Günün muhtelif vakitlerinde hastaların hıltları (kan, balgam, safra, sevda) değişir. Hekim-i kâmil odur ki; fecirde Rast, kuşlukta Buselik, öğlede Uşşak, gurubda Hüseyni dinleterek bedenin kimyasını sesle dengeye getirir.",
    "category": "islam_tibbi",
    "freq": 247.5,
    "reflection": "Osmanlı hekimleri, sirkadiyen biyolojik saati makamların frekanslarıyla senkronize etmiştir."
  },
  {
    "id": "evliya_celebi_edirne",
    "author": "Evliyâ Çelebi",
    "era": "17. Yüzyıl (1611 - 1682)",
    "work": "Seyahatnâme (3. Cilt - Edirne Darüşşifası Bahsi)",
    "quote": "Sultan Bayezid-i Veli Darüşşifası'nda haftada üç gün akıl ve beden hastalarına şifa için musiki faslı icra olunur. On nefer hanende ve sazende meclis kurup Rast, Neva, Hicaz ve Saba ile meşk ederler; hastalar bu nağmelerle mest olup feryatları kesilir, şifa bulurlar.",
    "category": "islam_tibbi",
    "freq": 220.0,
    "reflection": "Avrupa'da akıl hastalarının zincire vurulduğu çağda, Osmanlı darüşşifalarında su sesi ve makamlarla terapi uygulanıyordu."
  },
  {
    "id": "kepler_harmonices_mundi",
    "author": "Johannes Kepler",
    "era": "17. Yüzyıl (1571 - 1630)",
    "work": "Harmonices Mundi (Dünyanın Uyumları, 1619)",
    "quote": "Göklerdeki gezegenler semavi bir polifoni (çok sesli koro) icra ederler. Gezegenlerin günöte ve günberi hızları arasındaki oranlar, tam müzikal gam aralıklarına (sekizli, beşli, dörtlü, üçlü) karşılık gelir.",
    "category": "bilim_ve_fizik",
    "freq": 183.58,
    "reflection": "Gezegenlerin hareket yasaları ile müzik harmonisi aynı ilahi geometrinin iki farklı tezahürüdür."
  },
  {
    "id": "chladni_matter_sound",
    "author": "Ernst Chladni",
    "era": "18. - 19. Yüzyıl (1756 - 1827)",
    "work": "Entdeckungen über die Theorie des Klanges (1787)",
    "quote": "Keman yayını metal levhaya sürttüğümde üzerindeki kum taneleri rastgele savrulmadı; görünmeyen bir iradenin emrindeymiş gibi kusursuz geometrik mandalalara ve simetrik düğüm çizgilerine toplandı. Ses, maddeyi biçimlendiren mimardır.",
    "category": "bilim_ve_fizik",
    "freq": 432.0,
    "reflection": "Cymatics (sematik), ses dalgalarının görünmez fiziksel gücünü gözle görülür somut maddeye dönüştürür."
  },
  {
    "id": "hans_cousto_cosmic_octave",
    "author": "Hans Cousto",
    "era": "20. Yüzyıl (1948 - Günümüz)",
    "work": "The Cosmic Octave: Tuning to the Greater Reality (1978)",
    "quote": "Kozmik Oktav kuralı uyarınca; gök cisimlerinin dönme ve dolanma periyotlarını ikinin katları ile (oktavlarla) işitilebilir frekans sahasına taşıdığımızda, evrenin mikrokozmik bedenimizle konuştuğu anahtarı buluruz.",
    "category": "bilim_ve_fizik",
    "freq": 136.1,
    "reflection": "Dünya Yılı'nın 32. oktavı 136.10 Hz (Om tonu), kadim bilgelerin sezgisel olarak keşfettiği kutsal akorttur."
  },
  {
    "id": "masaru_emoto_water",
    "author": "Dr. Masaru Emoto",
    "era": "20. - 21. Yüzyıl (1943 - 2014)",
    "work": "Suyun Gizli Mesajı (The Hidden Messages in Water)",
    "quote": "Su dinler, kaydeder ve hisseder. Sevgi, şükran ve ahenkli müzik dinletilen su dondurulduğunda kusursuz altıgen kar kristalleri oluştururken; öfke ve nefret sözleri söylenen suyun kristalleri paramparça ve kaotik olur. İnsan bedeninin %70'i su olduğuna göre, duyduğumuz her ses bedenimizi yeniden şekillendirir.",
    "category": "mistik_akustik",
    "freq": 528.0,
    "reflection": "Beden suyu, zihnimizden ve çevremizden yayılan her frekansın canlı kütüphanesidir."
  },
  {
    "id": "inayat_khan_sound_mysticism",
    "author": "Hazrat Inayat Khan",
    "era": "19. - 20. Yüzyıl (1882 - 1927)",
    "work": "The Mysticism of Sound and Music",
    "quote": "Ses, tüm tezahürün başlangıcı ve sonudur. Bilen kişi için tüm evren tek bir ilahi senfonidir. Bedeniniz bir enstrümandır; ruhunuz ise o enstrümanı çalan virtüözdür. Akordu bozuk bir enstrümandan güzel bir nağme çıkmaz.",
    "category": "mistik_akustik",
    "freq": 432.0,
    "reflection": "Hastalık bedenin akordunun bozulması, şifa ise yeniden evrensel frekansa akortlanmasıdır."
  },
  {
    "id": "gazzali_sama_ve_vecd",
    "author": "İmâm Gazzâlî",
    "era": "11. - 12. Yüzyıl (1058 - 1111)",
    "work": "İhyâ'u Ulûmi'd-Dîn (Âdâbü's-Semâ ve'l-Vecd)",
    "quote": "Kalpler ve sırlar hazinesinin kilitleri ancak ve ancak semâ ve nağmeler ile açılır. Çakmak taşındaki gizli ateş gibi, kalpteki ilahi muhabbet közü de hoş ve vezinli sesler ile alevlenir.",
    "category": "tasavvuf",
    "freq": 220.0,
    "reflection": "Musiki kalpte ne varsa onu ortaya çıkarır; kalbinde Hakk aşkı olanın aşkını ziyadeleştirir."
  },
  {
    "id": "alfred_tomatis_ear",
    "author": "Dr. Alfred Tomatis",
    "era": "20. Yüzyıl (1920 - 2001)",
    "work": "The Conscious Ear & Tomatis Etkisi",
    "quote": "Kulak yalnızca bir işitme organı değil; beyni şarj eden bir dinamodur. Yüksek frekanslı harmonikler (özellikle Mozart ve Gregoryen ilahileri) kortekse elektriksel enerji pompalar ve uyanıklık sağlar.",
    "category": "mistik_akustik",
    "freq": 432.0,
    "reflection": "Ses enerjisi, kulak salyangozundan vestibüler sisteme geçerek tüm beden omurgasını dikleştirir."
  },
  {
    "id": "max_planck_matrix",
    "author": "Max Planck",
    "era": "19. - 20. Yüzyıl (1858 - 1947)",
    "work": "Floransa Konferansı (1944)",
    "quote": "Bütün madde, ancak atom parçacıklarını bir arada tutan ve titreştiren bir kuvvet sayesinde var olur. Biz bu kuvvetin arkasında bilinçli ve akıllı bir Zihnin var olduğunu kabul etmek zorundayız. Bu Zihin, tüm maddenin ana matrisidir.",
    "category": "bilim_ve_fizik",
    "freq": 7.83,
    "reflection": "Kuantum fiziğinin babası Planck, maddenin temelinde yatan kozmik bilinci ve titreşimi böyle ifade etmiştir."
  },
  {
    "id": "walter_russell_light_wave",
    "author": "Walter Russell",
    "era": "19. - 20. Yüzyıl (1871 - 1963)",
    "work": "The Universal One & The Secret of Light",
    "quote": "Bu evrende ışıktan ve dalgadan başka hiçbir şey yoktur. Dalga, Yaratıcı'nın düşüncesinin ritmik hareketidir. Her element, ses oktavlarının farklı ritim ve eğriliklerde düğümlenmiş halleridir.",
    "category": "bilim_ve_fizik",
    "freq": 528.0,
    "reflection": "Periyodik tablodaki elementler, müzikal oktavların geometrik izdüşümleridir."
  },
  {
    "id": "yunus_emre_soz",
    "author": "Yûnus Emre",
    "era": "13. - 14. Yüzyıl (1238 - 1328)",
    "work": "Dîvân-ı Yûnus Emre",
    "quote": "Keleci bilen kişinin / Yüzünü ağ ede bir söz / Sözü pişirip diyenin / İşini sağ ede bir söz... Söz ola kese savaşı / Söz ola kestire başı / Söz ola ağulu aşı / Bal ile yağ ede bir söz.",
    "category": "tasavvuf",
    "freq": 432.0,
    "reflection": "Ağızdan çıkan her harf bir titreşim dalgası yayar; şifalı kelâm zehirli halleri bala ve yağa dönüştürür."
  },
  {
    "id": "niyazi_misri_soz",
    "author": "Niyâzî-i Mısrî",
    "era": "17. Yüzyıl (1618 - 1694)",
    "work": "Dîvân-ı Niyâzî-i Mısrî",
    "quote": "Derman arardım derdime / Derdim bana derman imiş / Bürhan sorardım aslıma / Aslım bana bürhan imiş... Savm u salât u hac ile sanma biter zâhid işin / İnsan-ı Kâmil olmaya lâzım olan irfân imiş.",
    "category": "tasavvuf",
    "freq": 220.0,
    "reflection": "Hastalığın frekansı ile şifanın frekansı aynı hakikatin iki kutbudur; dert doğru idrakle dermana döner."
  },
  {
    "id": "ibn_arabi_kun",
    "author": "Muhyiddîn İbnü'l-Arabî",
    "era": "12. - 13. Yüzyıl (1165 - 1240)",
    "work": "Fütûhât-ı Mekkiyye (Mekke Fetihleri)",
    "quote": "Kâinattaki bütün mevcudat, Hakk'ın 'Kün!' (Ol!) kelâmının harflerinden ve ilahi Nefes-i Rahmânî'nin fezadaki yayılımından ibarettir. Her varlık, ilahi nefesin belirli bir mertebede düğümlenmesiyle beliren bir ses harfidir.",
    "category": "tasavvuf",
    "freq": 432.0,
    "reflection": "Varlık statik bir madde yığını değil, ilahi nefesin sürekli üflendiği akışkan bir kelamlar okyanusudur."
  },
  {
    "id": "ibn_arabi_fusus_nefes",
    "author": "Muhyiddîn İbnü'l-Arabî",
    "era": "12. - 13. Yüzyıl (1165 - 1240)",
    "work": "Füsûsü'l-Hikem (Hikmetlerin Özleri)",
    "quote": "Nefes nasıl boğazdan, damaktan ve dudaklardan geçerken farklı seslere ve harflere bürünürse; Rahman'ın nefesi de ilahi isimlerin aynalarında tecelli ederek yıldızları, unsurları ve bedenleri var eder.",
    "category": "tasavvuf",
    "freq": 528.0,
    "reflection": "Harflerin mahreçleri gibi her mahluk ilahi nefesin çıktığı bir kozmik menfezdir."
  },
  {
    "id": "ihvan_safa_musiki",
    "author": "İhvân-ı Safâ",
    "era": "10. Yüzyıl (Bağdat & Basra)",
    "work": "Resâ'il İhvân es-Safâ (5. Mûsikî Risalesi)",
    "quote": "Bil ki ey kardeş; mûsikî aletlerinin tellerinden çıkan nağmeler, gök kürelerinin dönüşündeki nispetlere uygundur. Mûsikî, nefsi cismani alakanın ağırlığından sıyırarak feleki aleme ve ruhani saffete yükseltir; bedendeki dört hıltın fazlalıklarını törpüleyip itidale erdirir.",
    "category": "islam_tibbi",
    "freq": 220.0,
    "reflection": "Klasik Doğu felsefesinde müzik yalnızca estetik bir zevk değil, ruhun feleki menşeine dönüş vasıtasıdır."
  },
  {
    "id": "gazali_sema_adabi",
    "author": "İmâm Gazâlî",
    "era": "11. - 12. Yüzyıl (1058 - 1111)",
    "work": "İhyâü Ulûmi'd-Dîn (Kitâbu Âdâbi's-Semâ')",
    "quote": "Mûsikî ve güzel ses, çakmak taşının demire vurulduğunda kıvılcım saçması gibi kalbin derinliklerindeki gizli cevherleri uyandırır. Kalbinde Hakk sevgisi olanın aşkını taştırır, kalbinde vesvese olanın da vesvesesini depreştirir. Ses, kalpte saklı olan tohumun yağmurudur.",
    "category": "tasavvuf",
    "freq": 432.0,
    "reflection": "Akustik rezonans tarafsız bir kuvvettir; bireyin içsel frekansını açığa çıkarır ve büyütür."
  },
  {
    "id": "razi_tibbi_ruhani",
    "author": "Ebû Bekir er-Râzî (Rhazes)",
    "era": "9. - 10. Yüzyıl (865 - 925)",
    "work": "Et-Tıbbü'r-Rûhânî (Ruh Sağlığı Tıbbı)",
    "quote": "Gam, keder ve melankoliye duçar olan kimselere hoş kokulu bitkiler koklatılmalı, latif manzaralar seyrettirilmeli ve kulağına yumuşak nağmelerle çalınan tambur ve ud ezgileri dinletilmelidir. Bedenin mizacı düzelmeden evvel ruhun mizacı ses ile taranmalıdır.",
    "category": "islam_tibbi",
    "freq": 261.63,
    "reflection": "Psikosomatik tıp prensibi: Ruhun sesle dengelenmesi, somatik iyileşmenin ön şartıdır."
  },
  {
    "id": "suuri_hasan_vakit",
    "author": "Şuûrî Hasan Efendi",
    "era": "17. Yüzyıl",
    "work": "Ta'dîlü'l-Emzice (Mizaçların Düzenlenmesi)",
    "quote": "Günün yirmi dört saati feleğin burçlarıyla taksim edilmiştir. Seherde Rast, kuşlukta Buselik, öğlede Hicaz ve Nihavend, ikindide Uşşak, gün batarken Hüseyni ve yatsıda Zirgüle dinletildiğinde; kan, safra, balgam ve sevda mizaçları taşkınlık yapmaz, hasta sıhhate erer.",
    "category": "islam_tibbi",
    "freq": 392.0,
    "reflection": "Sirkadiyen biyolojik ritim ile makamların günün vakitleri arasındaki derin biyo-rezonans uyumu."
  },
  {
    "id": "gevrekzade_cocuk_ses",
    "author": "Gevrekzâde Hasan Efendi",
    "era": "18. Yüzyıl (1727 - 1801)",
    "work": "Emrâz-ı Atfâl (Çocuk Hastalıkları Risalesi)",
    "quote": "Beşikte ağlayan, havale ve humma geçiren masum sabi çocukların başucunda yumuşak sesle ninniler söylenmeli ve Rehavi makamı çalınmalıdır. Rehavi sabinin dimağını soğutur, başındaki harareti teskin eder ve onu derin bir uykuya sevk eder.",
    "category": "islam_tibbi",
    "freq": 174.0,
    "reflection": "Çocuk ve bebeklerin sinir sistemi gelişirken akustik şefkat ve makam melodilerinin koruyucu etkisi."
  },
  {
    "id": "evliya_edirne_fasli",
    "author": "Evliyâ Çelebi",
    "era": "17. Yüzyıl (1611 - 1682)",
    "work": "Seyahatnâme (3. Cilt - Edirne Darüşşifası)",
    "quote": "Darüşşifanın ortasındaki kubbe altında fıskiyeli büyük bir havuz vardır. Haftada üç gün usta hanende ve sazendeler gelip deli ve kederli hastalara fasıl eyler. Su şırıltısı ile ney sadası birbirine karıştığında nicelerin deliliği zail olur, hastaların yüzüne can gelir.",
    "category": "islam_tibbi",
    "freq": 200.0,
    "reflection": "Doğal su akustiği (pembe gürültü) ile enstrümantal melodinin birleştiği akustik şifa mimarisi."
  },
  {
    "id": "farabi_uc_tesir",
    "author": "Ebû Nasr el-Fârâbî",
    "era": "9. - 10. Yüzyıl (872 - 950)",
    "work": "Kitâbü'l-Mûsîka'l-Kebîr (Büyük Musiki Kitabı)",
    "quote": "Mûsikî nağmeleri üç nev'idir: Birincisi insana ferahlık, neşe ve dinçlik bağışlayan lezzet verici seslerdir. İkincisi zihne ve hayal gücüne suretler nakşeden ilham verici seslerdir. Üçüncüsü ise kalpteki gizli tutkuları coşturan veya dinlendiren ruhani seslerdir ki bu doğrudan tıbba dahildir.",
    "category": "islam_tibbi",
    "freq": 432.0,
    "reflection": "Müziğin nörolojik sınıflandırması: hedonik, bilişsel ve terapötik-duygusal etki alanları."
  },
  {
    "id": "mevlana_divan_ezel",
    "author": "Mevlânâ Celâleddîn-i Rûmî",
    "era": "13. Yüzyıl (1207 - 1273)",
    "work": "Dîvân-ı Kebîr (Külliyât-ı Şems)",
    "quote": "Biz hepimiz gök kubbenin dönmesinden çıkan nağmeleri dinlemiş ruhlarız; Adem'in cisminde o nağmelerin hatırası vardır. Ney ve tamburdan işittiğimiz sesler, cennetteki o ezelî meclisin yankısıdır; işte bu yüzden dinleyen her garip ruh o vatanı hatırlar da ağlar.",
    "category": "tasavvuf",
    "freq": 216.0,
    "reflection": "Platonik 'anamnesis' (hatırlama) kavramının tasavvuftaki tecellisi: Ses, ruhun ezelî hafızasını uyandırır."
  },
  {
    "id": "mevlana_fihi_mafih_nefes",
    "author": "Mevlânâ Celâleddîn-i Rûmî",
    "era": "13. Yüzyıl (1207 - 1273)",
    "work": "Fîhi Mâ Fîh (İçindekiler İçindedir)",
    "quote": "Nefes birdir, lakin çarptığı kaba göre ses verir: Bir kamışa üflersen ney olur, yanık feryat eder; bir boruya üflersen cenk borusu olur, dehşet saçar. İnsanoğlu da böyledir; içini dünya kirinden boşaltan kimseye ilahi nefes çarptığında ondan ancak hikmet nağmesi sadır olur.",
    "category": "tasavvuf",
    "freq": 528.0,
    "reflection": "Nöral arınma ve dinginlik: Zihin ne kadar sessiz ve arınmışsa, yansıttığı rezonans o kadar saftır."
  },
  {
    "id": "sems_tebrizi_kelam",
    "author": "Şems-i Tebrîzî",
    "era": "12. - 13. Yüzyıl (1185 - 1248)",
    "work": "Makâlât-ı Şems (Şems'in Sohbetleri)",
    "quote": "Ağızdan çıkan kelâm bir oktur, bir defa fırlatıldı mı hedefini bulur. Söz vardır can bağışlar, söz vardır can alır. Söz vardır yaraya merhem, söz vardır cihanı ateşe verir. Bir kimse konuşurken önce kalbinin kuyusuna inmeli, oradaki sesin saf suyunu çekip öyle konuşmalıdır.",
    "category": "tasavvuf",
    "freq": 432.0,
    "reflection": "Sözün biyoakustik ve niyet gücü: İletilen dalganın kalitesi kalpteki niyetin frekansıyla belirlenir."
  },
  {
    "id": "haci_bektas_nefes",
    "author": "Hacı Bektâş-ı Velî",
    "era": "13. Yüzyıl (1209 - 1271)",
    "work": "Makâlât (Sözler)",
    "quote": "Diliyle incitmeyen, sazıyla hakikati söyleyen meclis bulur. Mârifet nefesi haktan alıp halka hakça dağıtmaktır. Çalınan sazın teli gönül teliyle bir olmadıkça o ses taş üstüne dökülen sudan farksızdır.",
    "category": "tasavvuf",
    "freq": 432.0,
    "reflection": "Akustik samimiyet ve rezonans: Fiziksel tel ile zihinsel niyetin koheransı."
  },
  {
    "id": "attar_mantik_ses",
    "author": "Ferîdüddin Attâr",
    "era": "12. - 13. Yüzyıl (1145 - 1221)",
    "work": "Mantıku't-Tayr (Kuşların Dili)",
    "quote": "Simurg ezel meclisinde bir tüyünü Çin diyarına düşürdü; o tüyden binlerce renk ve ses dalgası saçıldı. Kuşların her biri kendi dilinde öttü amma hepsi o tek sesin arayışındaydı. Otuz kuş vadiyi aşıp aynaya baktığında, aradıkları Simurg'un kendi müşterek sesleri olduğunu gördüler.",
    "category": "tasavvuf",
    "freq": 963.0,
    "reflection": "Birlik şuuru ve polifonik koherans: Bütün frekansların kaynakta tek bir beyaz seste birleşmesi."
  },
  {
    "id": "hudayi_zikir_arsh",
    "author": "Azîz Mahmûd Hüdâyî",
    "era": "16. - 17. Yüzyıl (1541 - 1628)",
    "work": "Dîvân-ı İlâhiyyât",
    "quote": "Zikrin sadası gökleri tuttuğunda, kalbin pası çözülür; göğüs kafesi arş-ı a'lâya dönüşür. Hu nidası nefesten nefese ulaştığında ne gam kalır ne keder. Her hücre 'Allah' derken beden kendi aslına secde eyler.",
    "category": "tasavvuf",
    "freq": 136.1,
    "reflection": "Kutsal tekrarların (japa/zikir) hücresel vagal senkronizasyon ve derin gevşeme etkisi."
  },
  {
    "id": "pythagoras_spheres_deaf",
    "author": "Pisagor (Pythagoras)",
    "era": "M.Ö. 6. Yüzyıl (M.Ö. 570 - 495)",
    "work": "Kürelerin Musikisi ve Sayı Öğretisi",
    "quote": "Gök cisimleri uzayda dönerken öyle muazzam ve ilahi bir armoni (Musica Universalis) neşrederler ki, insan kulağı doğduğu andan itibaren bu sesin içinde yüzdüğü için onu duyamaz, sessizlik zanneder. Sessizlik dediğimiz şey, evrenin kesintisiz çalan senfonisidir.",
    "category": "antik_felsefe",
    "freq": 432.0,
    "reflection": "Kozmik dip gürültüsü ve temel armonikler: Duyularımızın alışkanlık eşiğinin ötesindeki ilahi ahenk."
  },
  {
    "id": "pythagoras_interval_medicine",
    "author": "Pisagor (Pythagoras)",
    "era": "M.Ö. 6. Yüzyıl (M.Ö. 570 - 495)",
    "work": "Monokord ve Ruh Terapisi",
    "quote": "Sayılar evrenin nizamıdır; müzik ise sayıların duyulabilir halidir. Uygun müzikal aralıklarla çalınan bir lirik ezgi, öfkeli bir adamı dinginleştirebilir, hüzünlü bir genci cesaretle doldurabilir. Tellerin oranını bilmeyen hekim, ruhun dikişlerini dikemez.",
    "category": "antik_felsefe",
    "freq": 528.0,
    "reflection": "Pisagor matematiği: 2:1 (oktav), 3:2 (tam beşli), 4:3 (tam dörtlü) sayısal oranlarının psiko-akustik tesiri."
  },
  {
    "id": "plato_republic_music",
    "author": "Platon (Eflatun)",
    "era": "M.Ö. 5. - 4. Yüzyıl (M.Ö. 428 - 348)",
    "work": "Devlet (Politeia, III. Kitap)",
    "quote": "Müzik eğitimi terbiyelerin en kuvvetlisidir. Çünkü ritim ve armoni ruhun ta derinliklerine kadar işler, oraya sımsıkı yerleşir ve ona asalet, zarafet ve dürüstlük bağışlar. Doğru terbiye edilmiş bir ruh, güzel olanı derhal tanır ve onu içine sindirerek beslenir.",
    "category": "antik_felsefe",
    "freq": 432.0,
    "reflection": "Müziğin nöroplastisite ve ahlaki karakter inşasındaki vazgeçilmez temel rolü."
  },
  {
    "id": "plato_timaeus_soul_ratios",
    "author": "Platon (Eflatun)",
    "era": "M.Ö. 4. Yüzyıl (M.Ö. 360 civarı)",
    "work": "Timaios (Timaeus)",
    "quote": "Evrenin Ruhu, Yaratıcı (Demiurgos) tarafından müzikal aralıklara, ses oktavlarına ve geometrik oranlara göre yoğrulmuştur. Bu sebeple kulaklarımızdaki işitme duyusu bize sadece geçici bir haz için değil, içimizdeki bozulmuş ruh ritmini evrenin ebedi ritmine yeniden akort etmek için ihsan edilmiştir.",
    "category": "antik_felsefe",
    "freq": 136.1,
    "reflection": "Akustik re-entrainment: Bireysel biyoritmi kozmik temel frekansa geri uyumlama."
  },
  {
    "id": "aristotle_politics_catharsis",
    "author": "Aristoteles (Aristo)",
    "era": "M.Ö. 4. Yüzyıl (M.Ö. 384 - 322)",
    "work": "Politika (VIII. Kitap) & Poetika",
    "quote": "Müzik doğrudan ruhun duygulanımlarına benzer modeller üretir: Öfke, yumuşaklık, cesaret ve itidal ezgilerde apaçık tezahür eder. Kutsal ezgileri dinleyen kimseler, sanki tıbbi bir arınma (katarsis) ve ilaç almışçasına ruhlarındaki aşırılıklardan arınır ve dinginleşirler.",
    "category": "antik_felsefe",
    "freq": 396.0,
    "reflection": "Akustik katarsis: Bastırılmış duyguların rezonant ses dalgalarıyla boşaltılması ve regülasyonu."
  },
  {
    "id": "hermes_kybalion_vibration",
    "author": "Hermes Trismegistus (Hermetik Külliyat)",
    "era": "Kadim İskenderiye Geleneği",
    "work": "Kybalion (Titreşim Prensibi / III. Hermetik Yasa)",
    "quote": "Hiçbir şey durmaz; her şey hareket eder; her şey titreşir. Saf Ruh'tan en kaba maddeye kadar evrendeki her varlık mertebesi yalnızca farklı bir titreşim derecesinden ibarettir. Titreşim prensibini anlayan kimse, zihinsel dönüşümün asasını elinde tutar.",
    "category": "antik_felsefe",
    "freq": 528.0,
    "reflection": "Modern kuantum dalga mekaniğinin binlerce yıl evvelki hermetik formülasyonu."
  },
  {
    "id": "boethius_three_musics",
    "author": "Anicius Manlius Severinus Boethius",
    "era": "5. - 6. Yüzyıl (477 - 524)",
    "work": "De Institutione Musica (Müzik Eğitimi Üzerine)",
    "quote": "Üç türlü mûsikî vardır: Birincisi gezegenlerin ve mevsimlerin ahengi olan Kozmik Müzik (Musica Mundana); ikincisi ruh ile bedenin eklemlerini bir arada tutan İnsan Müziği (Musica Humana); üçüncüsü ise telli ve nefesli aletlerden çıkan Enstrüman Müziği'dir (Musica Instrumentalis). Enstrüman, insana kendi iç müziğini hatırlatır.",
    "category": "antik_felsefe",
    "freq": 432.0,
    "reflection": "Orta Çağ ve Rönesans müziğinin omurgası: Makrokozmos, mikrokozmos ve enstrüman birliği."
  },
  {
    "id": "kepler_harmonices_polyphony",
    "author": "Johannes Kepler",
    "era": "16. - 17. Yüzyıl (1571 - 1630)",
    "work": "Harmonices Mundi (Dünyanın Uyumu, 1619)",
    "quote": "Göklerin hareketi, bir akıl tarafından kavranabilen ebedi bir polifonik konsere benzer. Gezegenler güneşe yaklaşıp uzaklaşırken hızları değişir ve bu hız oranları tam müzikal aralıklara denk düşer: Satürn ve Jüpiter bas söyler, Mars tenor, Dünya ve Venüs alto, Merkür ise tiz bir soprano gibi nağme eyler.",
    "category": "bilim_ve_fizik",
    "freq": 136.1,
    "reflection": "Kepler yasalarının müzik teorisiyle kusursuz kesişimi: Gezegen periyotlarının ses aralıkları."
  },
  {
    "id": "laozi_great_sound",
    "author": "Laozi (Lao Tzu)",
    "era": "M.Ö. 6. Yüzyıl (M.Ö. 571 - 471)",
    "work": "Tao Te Ching (Yol ve Erdem Kitabı, 41. Bölüm)",
    "quote": "Büyük karelerin köşeleri yoktur; büyük kaplar geç tamamlanır; büyük ses işitilmez; büyük suretin biçimi yoktur. Tao gizlidir ve isimsizdir; lakin her şeyi besleyen ve kemale erdiren yalnızca O'dur.",
    "category": "antik_felsefe",
    "freq": 7.83,
    "reflection": "Duyulabilir gürültünün ötesindeki derin sessizlik alanı (infrases ve kozmik dip dalgası)."
  },
  {
    "id": "mandukya_om_trinity",
    "author": "Mandukya Upanişad",
    "era": "M.Ö. 1. Binyıl (Vedik Dönem)",
    "work": "Mandukya Upanishad (1. Bölüm)",
    "quote": "OM hecesi bütün kainattır. Geçmiş, şimdi ve gelecek olan ne varsa hepsi OM'dur. Bu üç zaman diliminin ötesinde olan ebediyet de OM'dan başka bir şey değildir. Bu ses; uyanıklık (A), rüya (U) ve derin uykusuzluk (M) hallerini aşan dördüncü şuura (Turiya) açılan kapıdır.",
    "category": "kutsal_metin",
    "freq": 136.1,
    "reflection": "A-U-M formantlarının beyin dalgası spektrumunda Alfa, Teta ve Delta hallerini kucaklaması."
  },
  {
    "id": "chhandogya_sun_song",
    "author": "Chhandogya Upanişad",
    "era": "M.Ö. 8. - 6. Yüzyıl",
    "work": "Chhandogya Upanishad (III. Bölüm)",
    "quote": "Güneş gökyüzünde ışıldarken bir ilahi terennüm eyler. O, kainatın kalbindeki bal peteğidir; ışınları ise nehirler gibi akıp yeryüzündeki canlıların hücrelerini canlandıran ses telleridir. Güneşi dinleyen kimse ölümü tanımaz.",
    "category": "kutsal_metin",
    "freq": 126.22,
    "reflection": "Güneşin 126.22 Hz rezonant frekansı (Cousto oktavı) ve canlılar üzerindeki biyo-ritmik canlandırıcı etkisi."
  },
  {
    "id": "heart_sutra_emptiness_sound",
    "author": "Prajnaparamita Kalp Sutrası",
    "era": "M.S. 1. Yüzyıl (Budist Külliyat)",
    "work": "Maha Prajnaparamita Hridaya Sutra",
    "quote": "Biçim boşluktur, boşluk biçimdir; biçim boşluktan ayrı değildir, boşluk biçimden ayrı değildir. Duyum, algı, zihinsel oluşumlar ve bilinç de böyledir. Ses de böyledir; titreşir lakin özünde kalıcı bir töz barındırmaz; bu idrake eren kimse korkudan kurtulur.",
    "category": "kutsal_metin",
    "freq": 432.0,
    "reflection": "Kuantum dalga parçacık ikiliği ve sesin boşluktaki geçici dalgalanması: Zihinsel dinginlik anahtarı."
  },
  {
    "id": "mezmur_150_nefes",
    "author": "Kral Davud (Mezmurlar / Zebur)",
    "era": "M.Ö. 10. Yüzyıl (M.Ö. 1000 civarı)",
    "work": "Tevrat / Mezmurlar 150:1-6",
    "quote": "Rabb'e hamdedin! O'na boru sesiyle hamdedin; O'na lirik ve çenk ile hamdedin! O'na tefle, dansla hamdedin; O'na telli sazlarla ve neyle hamdedin! O'na çınlayan zillerle hamdedin! Bütün nefes alan canlılar Rabbe hamdetsin!",
    "category": "kutsal_metin",
    "freq": 528.0,
    "reflection": "Nefes ve ses ile kainatın varlık korosuna katılma: Şükran ve hücresel esenlik rezonansı."
  },
  {
    "id": "davud_lir_saul",
    "author": "I. Samuel (Tevrat)",
    "era": "M.Ö. 10. Yüzyıl",
    "work": "I. Samuel 16:23",
    "quote": "Kral Saul'ün üzerine kötü ve hırçın bir ruh (ağır anksiyete ve melankoli) çöktüğünde; Davud lirini alır, parmaklarıyla çalardı. Saul rahatlar, ferahlar ve o kötü ruh ondan uzaklaşıp giderdi.",
    "category": "kutsal_metin",
    "freq": 396.0,
    "reflection": "Tarihteki ilk kaydedilmiş psikiyatrik müzikterapi vakası: Telli sazla panik ve buhran teskini."
  },
  {
    "id": "yuhanna_soz_kelam",
    "author": "Yuhanna İncili",
    "era": "1. Yüzyıl",
    "work": "İncil / Yuhanna 1:1-3",
    "quote": "Başlangıçta Söz (Logos) vardı. Söz Tanrı ile birlikteydi ve Söz Tanrı idi. Başlangıçta O, Tanrı ile birlikteydi. Her şey O'nun aracılığıyla var oldu; var olan hiçbir şey O'nsuz var olmadı.",
    "category": "kutsal_metin",
    "freq": 528.0,
    "reflection": "Kozmik logos / frekans: Maddeden önce sesin, frekansın ve sözün önceliği ontolojisi."
  },
  {
    "id": "kuran_fussilet_gelin",
    "author": "Kur'ân-ı Kerîm",
    "era": "7. Yüzyıl",
    "work": "Fussilet Sûresi, 41:11",
    "quote": "Sonra duman (gaz bulutu) halinde bulunan göğe yöneldi; ona ve yeryüzüne: 'İsteyerek veya istemeyerek gelin!' buyurdu. İkisi de: 'İsteyerek ve itaat ederek geldik' dediler.",
    "category": "kutsal_metin",
    "freq": 7.83,
    "reflection": "Yaradılışın kozmik hitap ve icabet frekansı: Madde, ilahi emre titreşimsel rıza ile şekillenmiştir."
  },
  {
    "id": "kuran_kaf_sayha",
    "author": "Kur'ân-ı Kerîm",
    "era": "7. Yüzyıl",
    "work": "Kâf Sûresi, 50:41-42",
    "quote": "Çağırıcının yakın bir yerden sesleneceği güne kulak ver! O gün insanlar o dehşetli hak sayhayı (büyük akustik dalgayı) duyacaklardır. İşte o gün kabirlerden çıkış günüdür.",
    "category": "kutsal_metin",
    "freq": 174.0,
    "reflection": "Diriliş ve dönüşümün bir ses dalgası (Sayha / Sûr üflemesi) ile gerçekleşmesi gerçeği."
  },
  {
    "id": "kuran_isra_sifa",
    "author": "Kur'ân-ı Kerîm",
    "era": "7. Yüzyıl",
    "work": "İsrâ Sûresi, 17:82",
    "quote": "Biz Kur'an'dan, müminler için şifa ve rahmet olan şeyleri indiriyoruz; zalimlerin ise ancak ziyanını artırır.",
    "category": "kutsal_metin",
    "freq": 528.0,
    "reflection": "Kıraat sesinin nörobiyolojik, psikoakustik ve hücresel şifa frekansı boyutu."
  },
  {
    "id": "kuran_hasr_dag",
    "author": "Kur'ân-ı Kerîm",
    "era": "7. Yüzyıl",
    "work": "Haşr Sûresi, 59:21",
    "quote": "Eğer biz bu Kur'an'ı bir dağın üzerine indirseydik, muhakkak ki onu Allah korkusundan baş eğerek paramparça olmuş görürdün. Biz bu misalleri insanlara düşünsünler diye veriyoruz.",
    "category": "kutsal_metin",
    "freq": 432.0,
    "reflection": "Akustik rezonansın kütleleri sarsabilen ve taşlaşmış kalpleri yumuşatabilen kurucu kuvveti."
  },
  {
    "id": "hadis_kuran_tezyin",
    "author": "Hz. Muhammed (s.a.v.)",
    "era": "7. Yüzyıl",
    "work": "Sahîh-i Buhârî (Kitâbu't-Tevhîd, 52)",
    "quote": "Kur'ân'ı seslerinizle güzelleştirip süsleyiniz; zira güzel ses Kur'ân'ın güzelliğini ve kalplere nüfuzunu ziyadeleştirir.",
    "category": "kutsal_metin",
    "freq": 432.0,
    "reflection": "Akustik estetizm ve rezonans: Sözün hakikati sesin ahengiyle birleştiğinde zihinsel dirençler kırılır."
  },
  {
    "id": "hadis_sekine_kandil",
    "author": "Hz. Muhammed (s.a.v.)",
    "era": "7. Yüzyıl",
    "work": "Sahîh-i Müslim (Müsâfirîn, 240)",
    "quote": "Üseyd bin Hudayr gece vakti Kehf sûresini okurken atı şahlandı; göğe baktığında bir bulut içinde kandiller gibi parıldayan nurların indiğini gördü. Sabah Resûlullah'a haber verdiğinde Efendimiz şöyle buyurdu: 'Onlar meleklerdi; senin kıraatinin sesini dinlemek için yaklaştılar; okumaya devam etseydin sabahleyin herkes onları gözleriyle görecekti.'",
    "category": "kutsal_metin",
    "freq": 963.0,
    "reflection": "Ses dalgalarının metafizik ve elektromanyetik boyutu: Sekine ve koherans alanı doğuşu."
  },
  {
    "id": "hans_jenny_cymatics_matrix",
    "author": "Dr. Hans Jenny",
    "era": "20. Yüzyıl (1904 - 1972)",
    "work": "Cymatics: The Structure and Dynamics of Waves and Vibrations (1967)",
    "quote": "Sematik deneyleri göstermiştir ki ses; biçim yaratan, biçimi koruyan ve biçimi dönüştüren temel kuvvettir. Sıvı, gaz ve tozlar frekansın emriyle anında canlı doku morfolojisine benzer peteklere, sarmallara ve mandalalara dönüşür. Biyoloji, katılaşmış sematiktir.",
    "category": "bilim_ve_fizik",
    "freq": 528.0,
    "reflection": "Hücresel farklılaşma ve embriyolojik gelişim sürecindeki akustik mikro-dalgaların rolü."
  },
  {
    "id": "chladni_acoustic_geometry",
    "author": "Ernst Florens Friedrich Chladni",
    "era": "18. - 19. Yüzyıl (1756 - 1827)",
    "work": "Entdeckungen über die Theorie des Klanges (1787)",
    "quote": "Plakanın kenarına keman yayını sürttüğümde, üzerindeki kum taneleri gelişigüzel savrulmadı; görünmez bir nizamın emrine girerek kusursuz geometrik desenler (Chladni figürleri) çizdi. Ses, sessizliğin zeminine kendi imzasını kazımaktaydı.",
    "category": "bilim_ve_fizik",
    "freq": 432.0,
    "reflection": "Nodal çizgiler fiziği: Ses basıncının sıfır olduğu hatlarda toplanan maddenin geometrik nizamı."
  },
  {
    "id": "schrodinger_negentropy_harmony",
    "author": "Erwin Schrödinger",
    "era": "20. Yüzyıl (1887 - 1961)",
    "work": "What is Life? (Hayat Nedir?, 1944)",
    "quote": "Canlı bir organizma termodinamik dengeden (yani ölümden) nasıl kaçınır? Çevresinden sürekli 'negatif entropi' çekerek! Canlılık, dış dünyadaki kaotik dağınıklıktan bir düzen ve ritmik ahenk süzebilme kabiliyetidir.",
    "category": "bilim_ve_fizik",
    "freq": 7.83,
    "reflection": "Şifa frekansları bedenin entropik kaosunu düşürerek negatif entropi ve hücresel koherans sağlar."
  },
  {
    "id": "david_bohm_holomovement",
    "author": "David Bohm",
    "era": "20. Yüzyıl (1917 - 1992)",
    "work": "Wholeness and the Implicate Order (Bütünlük ve Saklı Düzen)",
    "quote": "Kainat statik şeylerin toplamı değil, kesintisiz bir 'Holo-hareket' (Holomovement) akışıdır. Nasıl bir ses kaydındaki her dalga diğer bütün enstrümanların bilgisini kendi içinde barındırıyorsa; evrendeki her atomaltı parçacık da tüm kainatın frekansını kendi saklı düzeninde katlanmış olarak taşır.",
    "category": "bilim_ve_fizik",
    "freq": 432.0,
    "reflection": "Holografik rezonans: Bireysel bilincin mikro dalgası, evrensel makro alanla sürekli temas halindedir."
  },
  {
    "id": "masaru_emoto_water_crystal",
    "author": "Dr. Masaru Emoto",
    "era": "20. - 21. Yüzyıl (1943 - 2014)",
    "work": "The Hidden Messages in Water (Sudaki Gizli Mesajlar, 2004)",
    "quote": "Su, sadece kimyasal bir bileşik değil; bilinci, sesi ve niyeti kaydeden kozmik bir teyptir. 'Sevgi ve Şükran' söylenen veya Mozart dinletilen su dondurulduğunda kusursuz altıgen pırlanta kristalleri oluştururken; öfke ve nefret yöneltilen suyun kristalleri paramparça olmaktadır. İnsan bedeninin yüzde yetmişi su olduğuna göre, duyduğumuz ve söylediğimiz sözlerin hücresel akıbetini varın siz düşünün.",
    "category": "mistik_akustik",
    "freq": 528.0,
    "reflection": "Beden sıvılarının akustik ve niyet bazlı yeniden yapılanması (su kristalizasyonu)."
  },
  {
    "id": "popp_biophoton_coherence",
    "author": "Dr. Fritz-Albert Popp",
    "era": "20. - 21. Yüzyıl (1938 - 2018)",
    "work": "Biyofotonik ve Hücresel İletişim Araştırmaları",
    "quote": "Sağlıklı bir hücre çekirdeği (DNA), lazer benzeri ultra zayıf koherent ışık ve akustik dalgalar yayar. Kanserli veya hastalıklı dokuda ise bu koherans bozulur ve sinyal kaotikleşir. Şifa, hücrenin koherent rezonans alanını yeniden tesis etmekten ibarettir.",
    "category": "bilim_ve_fizik",
    "freq": 528.0,
    "reflection": "528 Hz ve Solfeggio harmoniklerinin hücresel koherans ve biyofoton emisyonunu desteklemesi."
  },
  {
    "id": "rife_mortal_oscillatory",
    "author": "Royal Raymond Rife",
    "era": "20. Yüzyıl (1888 - 1971)",
    "work": "Evrensel Mikroskop ve Rezonans Frekans Terapisi",
    "quote": "Nasıl opera sanatçısının tutturduğu belirli bir tiz nota şarap kadehinin doğal frekansıyla eşleştiğinde kadehi paramparça ederse; her virüs ve bakterinin de kendine has bir 'Ölümcül Salınım Oranı' (Mortal Oscillatory Rate) vardır. O spesifik frekans gönderildiğinde çevre dokuya hiç zarar vermeden patojen imha olur.",
    "category": "bilim_ve_fizik",
    "freq": 741.0,
    "reflection": "Hedefe yönelik biyo-rezonans: Toksin ve patojenlerin frekansla etkisiz hale getirilmesi."
  },
  {
    "id": "cousto_cosmic_law",
    "author": "Hans Cousto",
    "era": "20. - 21. Yüzyıl (1948 - Günümüz)",
    "work": "Die Kosmische Oktave: Der Weg zum universellen Einklang (1984)",
    "quote": "Evrende hiçbir şey rasgele değildir. Gezegenlerin yörünge sürelerini oktav yasasıyla ses sahasına indirdiğimizde; Dünya'nın OM frekansı (136.1 Hz), Güneş'in Manipura tonu (126.22 Hz) ve Platonik Yılın Taç çakra rezonansı (172.06 Hz) matematiksel bir zorunlulukla açığa çıkar. İnsan, kainatın akort edilmiş mikro halidir.",
    "category": "mistik_akustik",
    "freq": 136.1,
    "reflection": "Kozmik oktav formülü $f = \frac{1}{T} \cdot 2^n$ ile makrokozmos ve insan biyofiziğinin tam örtüşmesi."
  },
  {
    "id": "beethoven_revelation",
    "author": "Ludwig van Beethoven",
    "era": "18. - 19. Yüzyıl (1770 - 1827)",
    "work": "Bettina von Arnim'e Mektuplar (1810)",
    "quote": "Müzik, insanın ruhunu tutuşturan bir kıvılcımdır; o, tüm bilgelik ve felsefeden daha yüksek bir ifşa ve vahiydir. Müziğimin derin anlamına nüfuz edebilen bir kimse, diğer insanların sürüklendiği bütün sefaletlerden ve dünyevi ıstıraplardan ebediyen azade olur.",
    "category": "mistik_akustik",
    "freq": 432.0,
    "reflection": "Müziğin aşkın ve kathartik gücü: Sanatın felsefeyi aşan doğrudan ontolojik şifası."
  },
  {
    "id": "goethe_frozen_music",
    "author": "Johann Wolfgang von Goethe",
    "era": "18. - 19. Yüzyıl (1749 - 1832)",
    "work": "Eckermann ile Konuşmalar (1829)",
    "quote": "Asil bir mimari eser gördüğümde aklıma daima şu fikir gelir: Mimari, taşların kalıbında donmuş mûsikîden başka bir şey değildir. Bir katedralin sütunları ve kubbeleri arasındaki nispetler, bir senfoninin ölçüleri ve akort aralıklarıdır.",
    "category": "mistik_akustik",
    "freq": 432.0,
    "reflection": "Sematik mimari: Üç boyutlu mekanların akustik harmonik oranlarla inşası."
  },
  {
    "id": "victor_hugo_music_ineffable",
    "author": "Victor Hugo",
    "era": "19. Yüzyıl (1802 - 1885)",
    "work": "William Shakespeare Üzerine Denemeler (1864)",
    "quote": "Müzik, kelimelerle ifade edilmesi imkansız olanı ve aynı zamanda sessiz kalınması asla kabil olmayanı haykırır.",
    "category": "mistik_akustik",
    "freq": 639.0,
    "reflection": "Duygusal sıkışmışlıkların çözümü: Dilin yetersiz kaldığı yerde kalbin sesle boşalması."
  },
  {
    "id": "inayat_khan_sound_creator",
    "author": "Hazrat Inayat Khan",
    "era": "19. - 20. Yüzyıl (1882 - 1927)",
    "work": "The Mysticism of Sound and Music (Sesin ve Müziğin Mistisizmi)",
    "quote": "Kainatın bütün yapısı sesten bina edilmiştir; insan bedeni ise ruhun elindeki yaşayan bir sazdır. Bedenin teli fazla gerildiğinde veya gevşediğinde hastalık ve ızdırap doğar. Şifacı hekim, hastanın beden sazını ilahi ezgiyle yeniden akort eden kimsedir.",
    "category": "tasavvuf",
    "freq": 432.0,
    "reflection": "Sufi müzikterapi felsefesi: İnsan bedenini yaşayan bir enstrüman olarak akort etme sanatı."
  },
  {
    "id": "nietzsche_life_without_music",
    "author": "Friedrich Nietzsche",
    "era": "19. Yüzyıl (1844 - 1900)",
    "work": "Putların Alacakaranlığı (Götzen-Dämmerung, 1888)",
    "quote": "Müziksiz bir hayat, bir hata, bir külfet, bir sürgün olurdu.",
    "category": "antik_felsefe",
    "freq": 432.0,
    "reflection": "Müziğin varoluşsal yaşama gücü (Wille zur Macht) ve trajik neşe aşılaması."
  },
  {
    "id": "kahlil_gibran_music_language",
    "author": "Halil Cibran (Kahlil Gibran)",
    "era": "19. - 20. Yüzyıl (1883 - 1931)",
    "work": "Müzik Üzerine (Al-Musiqa, 1905)",
    "quote": "Müzik, ruhun lisanıdır. Nağmeler göğsün tellerine vurduğunda, fani dünyanın kelimeleri eriyip gider; geriye sadece aşkın, hüznün ve ümidin berrak nehri kalır. Müzik, göklerin yeryüzündeki sürgün çocuklarına fısıldadığı ana dilidir.",
    "category": "mistik_akustik",
    "freq": 639.0,
    "reflection": "Evrensel duygusal rezonans: Kültürleri ve dilleri aşan ortak kalp tınısı."
  },
  {
    "id": "yehudi_menuhin_order",
    "author": "Yehudi Menuhin",
    "era": "20. Yüzyıl (1916 - 1999)",
    "work": "Unfinished Journey & Tema ve Çeşitlemeler",
    "quote": "Müzik, kaosun ortasındaki ruha düzen, karmaşanın içindeki zihne huzur, yalnız kalmış bir kalbe ise evrensel bir kardeşlik hissi bağışlar. Kemanın yayını tele dokundurduğumda, sadece bir enstrüman çalmam; insanlığın ortak yaralarını sarmaya çalışırım.",
    "category": "mistik_akustik",
    "freq": 432.0,
    "reflection": "Akustik koherans: Ritim ve armoninin beyin dalgalarındaki kaotik gürültüyü nizam ve sükuna çevirmesi."
  },
  {
    "id": "heisenberg_prob_waves",
    "author": "Werner Heisenberg",
    "era": "20. Yüzyıl (1901 - 1976)",
    "work": "Fizik ve Felsefe (Physics and Philosophy, 1958)",
    "quote": "Madde sandığımız en küçük atomaltı parçacıklar gerçekte birer 'şey' değildir; onlar titreşen olasılık dalgaları ve bağlantılar ağıdır. Evren nesnelerden değil, sürekli dans eden dinamik rezonans olaylarından dokunmuştur.",
    "category": "bilim_ve_fizik",
    "freq": 7.83,
    "reflection": "Kuantum belirsizliği ve potansiyeller alanı: Madde, gözlemcinin niyet ve frekansıyla somutlaşır."
  },
  {
    "id": "kindi_ud_dort_unsur",
    "author": "Ebû Yûsuf Ya'kûb b. İshâk el-Kindî (Alkindus)",
    "era": "9. Yüzyıl (801 - 873)",
    "work": "Risâle fî Hubri Te'lîfi'l-Elhân (Mûsikî Telifi Risalesi)",
    "quote": "Udun dört teli kâinatın dört unsuru ve bedenin dört hıltı ile tam bir tenasüp içindedir: En tiz tel olan Zîr ateşe ve sarı safraya; Mesnâ havaya ve kana; Mesles suya ve balgama; en kalın tel olan Bam ise toprağa ve kara safraya tekabül eder. Usta bir hekim, tellerin tınısıyla bedenin bozulan dört unsurunu mizanına getirir.",
    "category": "islam_tibbi",
    "freq": 220.0,
    "reflection": "İslam dünyasında ses terapisinin kurucusu el-Kindî'nin müzik teorisi ile hücresel mizaçları eşleştirmesi."
  },
  {
    "id": "urmevi_edvar_ruhaniyet",
    "author": "Safiyyüddîn el-Urmevî",
    "era": "13. Yüzyıl (1216 - 1294)",
    "work": "Kitâbü'l-Edvâr (Dönemler Kitabı)",
    "quote": "Her makam ve her aralık insan nefsinde bambaşka bir ruhani hal husule getirir: Kimi nağmeler nefse cesaret ve atılganlık aşılar, kimi nağmeler kalbe haşyet ve yakarış verir, kimi nağmeler ise dimağı tatlı bir rehavetle uykuya hazırlar. Perdelerin kemali, ruhun hallerine mutabık olmasıdır.",
    "category": "islam_tibbi",
    "freq": 293.33,
    "reflection": "17 perdeli sistemin mimarı Urmevî'nin makamların psikofizyolojik tesirlerini tahlili."
  },
  {
    "id": "meragi_camiul_elhan",
    "author": "Abdülkâdir-i Merâgî",
    "era": "14. - 15. Yüzyıl (1360 - 1435)",
    "work": "Câmi'u'l-Elhân (Ezgilerin Toplamı)",
    "quote": "Mûsikî fenni öyle bir cevherdir ki, onunla insan nefsi bedeni alakaların zindanından halas bulup letafet alemine uçar. Nağmelerin tertibi göklerin devranına denk düştüğünde, dinleyenin kalbinde kederden eser kalmaz; yerini ilahi bir huzur ve vecd kaplar.",
    "category": "islam_tibbi",
    "freq": 432.0,
    "reflection": "Klasik Doğu besteciliğinin zirvesi Merâgî'nin nağmelerin arındırıcı katharsis gücünü beyanı."
  },
  {
    "id": "kantemir_edvar_sır",
    "author": "Dimitrie Cantemir (Kantemiroğlu)",
    "era": "17. - 18. Yüzyıl (1673 - 1723)",
    "work": "Kitâb-ı İlmü'l-Mûsikî 'alâ Vechi'l-Edvâr",
    "quote": "Makamların her birinde gizli bir tılsım ve ruhani kuvvet saklıdır. Usta sazende bir makamdan diğerine geçerken adeta bir bahçeden diğerine su akıtır gibi dinleyicinin dimağındaki gamı yıkar, yerine asil bir tefekkür tohumu eker.",
    "category": "islam_tibbi",
    "freq": 220.0,
    "reflection": "Osmanlı makam seyrinin terapötik modülasyonu: Zihinsel blokajların makam geçişleriyle çözülmesi."
  },
  {
    "id": "ali_ufki_mezmur_nefes",
    "author": "Ali Ufkî Bey (Wojciech Bobowski)",
    "era": "17. Yüzyıl (1610 - 1675)",
    "work": "Mezmûrlar Tercümesi ve Mecmûa-i Sâz u Söz",
    "quote": "İlahi kelâmın güzelliği mûsikînin vezniyle birleştiğinde kulağa değil, doğrudan doğruya can kulağına hitap eder. Nefes ile tel birleştiğinde gök kubbenin altındaki bütün dertler eriyip gider.",
    "category": "tasavvuf",
    "freq": 432.0,
    "reflection": "Doğu ve Batı müzik geleneklerinin Osmanlı sarayında birleştiği evrensel nefes ahengi."
  },
  {
    "id": "ladikli_mehmed_muallim",
    "author": "Lâdikli Mehmed Çelebi",
    "era": "15. Yüzyıl",
    "work": "Zeynü'l-Elhân fî İlmi't-Te'lîf (Ezgilerin Süsü)",
    "quote": "İlahi hikmet mûsikîyi insan cismine şifa kılmıştır. Bedenin damarları tıpkı çalgının telleri gibidir; fazla gerilirse kopar, fazla gevşerse ses vermez. Hekim-i musikar, hastanın damarlarını nağmeyle mizanına getiren muallimdir.",
    "category": "islam_tibbi",
    "freq": 261.63,
    "reflection": "Damar elastikiyeti ve kan dolaşımının müzikal rezonansla akort edilmesi."
  },
  {
    "id": "haci_bayram_can",
    "author": "Hacı Bayrâm-ı Velî",
    "era": "14. - 15. Yüzyıl (1352 - 1430)",
    "work": "Divan ve Hikmetler",
    "quote": "Bilmek istersen seni / Can içre ara canı / Geç canından bul anı / Sen seni bil sen seni... Sazın telinden çıkan nida, can kafesindeki bülbülün asıl gülzarına duyduğu iştiyaktır; o sesi duyan uykudan uyanır.",
    "category": "tasavvuf",
    "freq": 432.0,
    "reflection": "İçsel uyanış ve farkındalık: Rezonansın bilinç perdelerini aralaması."
  },
  {
    "id": "esrefoglu_rumi_nefes",
    "author": "Eşrefoğlu Rûmî",
    "era": "15. Yüzyıl (1377 - 1469)",
    "work": "Müzekki'n-Nüfûs (Nefislerin Tezkiyesi)",
    "quote": "Nefes Hakk'ın emanetidir. Bir kimse her nefesinde Hakk'ı zikrederek sesini O'nun sevgisiyle tezyin eylerse, o nefes nefsani hevaları yakıp kül eden bir nura döner. O vakit o kimseden çıkan her seda çevresindekilere hayat bağışlar.",
    "category": "tasavvuf",
    "freq": 528.0,
    "reflection": "Farkındalıklı nefes (pranayama/habs-i nefes) ve sesin hücresel arındırma gücü."
  },
  {
    "id": "ismail_hakki_bursevi_ruh",
    "author": "İsmâil Hakkı Bursevî",
    "era": "17. - 18. Yüzyıl (1653 - 1725)",
    "work": "Rûhu'l-Beyân Tefsiri",
    "quote": "Arş-ı A'lâ'dan yere inen her ilahi emir bir ses ve nida suretinde tecelli eder. Melekler o nidayı tesbihlerle karşılarlar. İnsan kalbi de arşın bir numunesidir; oraya düşen ilahi ilhamlar ancak saf nağmeler ve temiz kelimelerle yankı bulur.",
    "category": "tasavvuf",
    "freq": 963.0,
    "reflection": "Kalbin bir akustik rezonatör olarak kozmik ilhamları alıcı (antenne) vazifesi görmesi."
  },
  {
    "id": "seyh_galib_ney_feryat",
    "author": "Şeyh Gâlib",
    "era": "18. Yüzyıl (1757 - 1799)",
    "work": "Hüsn ü Aşk (Güzellik ve Aşk)",
    "quote": "Hoşça bak zâtına kim zübde-i âlemsin sen / Merdüm-i dîde-i ekvân olan âdemsin sen... Neyin feryadını dinle; o kamış değil, senin kendi kalbinin hakikat denizine duyduğu hasretin iniltisidir.",
    "category": "tasavvuf",
    "freq": 432.0,
    "reflection": "Mikrokozmos olan insanın kendi içsel tınısını keşfetmesi: Bedenin evrenin özü olması."
  },
  {
    "id": "katip_celebi_musiki_sifa",
    "author": "Kâtip Çelebi",
    "era": "17. Yüzyıl (1609 - 1657)",
    "work": "Keşfü'z-Zunûn (İlimler Ansiklopedisi)",
    "quote": "İlm-i Mûsikî, riyaziye (matematik) ilimlerinin en şereflilerindendir ve tıpla ikiz kardeştir. Tıp bedenin uzuvlarını ilaçla tedavi ederse, mûsikî ruhun marazlarını nağmeyle tedavi eder. Ruha hitap etmeyen tıp eksiktir.",
    "category": "islam_tibbi",
    "freq": 220.0,
    "reflection": "Bütüncül (holistik) tıp: Matematik, müzik ve tıbbın ayrılmaz üçlü ittifakı."
  },
  {
    "id": "genesis_light_word",
    "author": "Tevrat / Yaratılış (Genesis)",
    "era": "M.Ö. 1. Binyıl",
    "work": "Tekvin (Genesis) 1:3",
    "quote": "Ve Tanrı dedi: 'Işık olsun!' Ve ışık oldu. Tanrı ışığın iyi olduğunu gördü ve ışığı karanlıktan ayırdı.",
    "category": "kutsal_metin",
    "freq": 528.0,
    "reflection": "Işığın yaratılışından önce 'Ve Tanrı dedi' (söz/kelâm/akustik titreşim) ifadesi yer alır; ses ışıktan öncedir."
  },
  {
    "id": "matthew_speak_word_healed",
    "author": "İncil / Matta",
    "era": "1. Yüzyıl",
    "work": "Matta 8:8",
    "quote": "Yüzbaşı cevap verdi: 'Ya Rab, evime girmene layık değilim; ancak yalnız bir söz söyle, kulum iyileşir.'",
    "category": "kutsal_metin",
    "freq": 528.0,
    "reflection": "Mekânı aşan akustik niyet ve şifa gücü: Tek bir şifalı kelâmın mesafeleri aşarak hücreyi onarması."
  },
  {
    "id": "kuran_neml_daglar",
    "author": "Kur'ân-ı Kerîm",
    "era": "7. Yüzyıl",
    "work": "Neml Sûresi, 27:88",
    "quote": "Sen dağları görürsün de onları hareketsiz ve donmuş sanırsın; oysa onlar bulutların akıp gitmesi gibi kesintisiz yürümektedir (dalgalanmaktadır). Bu, her şeyi sapasağlam ve ahenkle yapan Allah'ın sanatıdır.",
    "category": "kutsal_metin",
    "freq": 7.83,
    "reflection": "Maddenin statik katılığının bir yanılsama oluşu; yerkürenin ve dağların Schumann rezonansıyla akışı."
  },
  {
    "id": "kuran_ibrahim_kelime",
    "author": "Kur'ân-ı Kerîm",
    "era": "7. Yüzyıl",
    "work": "İbrâhîm Sûresi, 14:24-25",
    "quote": "Görmedin mi Allah güzel bir kelâmı neye benzetti? Kökü yerde sabit, dalları göğe yükselen güzel bir ağaç gibidir. O ağaç, Rabbinin izniyle her mevsim meyvesini verir.",
    "category": "kutsal_metin",
    "freq": 432.0,
    "reflection": "Güzel ve şifalı sözün fraktal morfolojisi: Köklenen, göğe uzanan ve kesintisiz şifa meyvesi veren kelâm."
  },
  {
    "id": "rig_veda_vac_sukta",
    "author": "Rig Veda (Vāc Sūkta)",
    "era": "M.Ö. 1500 civarı",
    "work": "Rig Veda Mandala 10, İlahi 125",
    "quote": "Ben Kutsal Söz'üm (Vāc)! Tanrıları ve evreni omuzlarımda taşırım. Rüzgar gibi serbestçe eserim; yeri, göğü ve ötesini kuşatırım. Dokunduğum insanı bir bilge, bir kâhin ve bir şifacı kılarım.",
    "category": "kutsal_metin",
    "freq": 528.0,
    "reflection": "Vedik gelenekte 'Vāc' (Kutsal Söz): Kâinatın yaratıcı ve dönüştürücü primal dişil enerjisi."
  },
  {
    "id": "bhartrhari_shabda_brahman",
    "author": "Bhartṛhari",
    "era": "5. Yüzyıl (Hindistan)",
    "work": "Vākyapadīya (Kelâm ve Dil Üzerine)",
    "quote": "Başlangıcı ve sonu olmayan, bölünmez ve ebedi hakikat Ses-Cevheridir (Shabda Brahman). Bütün evren ve varlık mertebeleri, bu aşkın sesin anlam formlarına bürünerek tezahür etmesinden başka bir şey değildir.",
    "category": "kutsal_metin",
    "freq": 432.0,
    "reflection": "Doğu dil felsefesinin zirvesi: Maddi evren, aşkın ses dalgasının mana aynasında donmasıdır."
  },
  {
    "id": "bardo_thodol_sound",
    "author": "Tibet Ölüler Kitabı (Bardo Thodol)",
    "era": "8. Yüzyıl (Padmasambhava)",
    "work": "Bardo Thodol (Geçiş Halleri Kılavuzu)",
    "quote": "Kulaklarında binlerce gök gürültüsü gibi çınlayan o muazzam kozmik sesleri duyduğunda korkma! Bil ki o sesler dışarıdan gelmiyor; onlar senin kendi öz bilincinin, kalbinin ve saf zihninin hakiki titreşimidir. O sesle bir ol, kurtuluşa er.",
    "category": "kutsal_metin",
    "freq": 963.0,
    "reflection": "İçsel nada (ses): Bireyin en derin trans hallerinde duyduğu hücresel ve nöronal rezonans sesleri."
  },
  {
    "id": "avesta_ahunwar_vibration",
    "author": "Zerdüşt Külliyatı (Zend Avesta)",
    "era": "M.Ö. 1. Binyıl",
    "work": "Yasna 27:13 (Ahunwar Mantrası)",
    "quote": "Ahura Mazda gökleri ve unsurları yaratmadan evvel 'Ahuna Vairya' kutsal kelâmını fısıldadı. O kutsal titreşim fezaya yayıldığında karanlığın kaosunu darmadağın etti ve nizamın ışığı parıldadı.",
    "category": "kutsal_metin",
    "freq": 432.0,
    "reflection": "Kadim Pers kozmolojisinde kelâmın kozmik kaosu kozmosa (düzene) dönüştüren gücü."
  },
  {
    "id": "hildegard_symphony_creation",
    "author": "Azize Hildegard von Bingen",
    "era": "12. Yüzyıl (1098 - 1179)",
    "work": "Scivias & Symphonia Armonie Celestium",
    "quote": "Tüm yaratılış tek bir ilahi senfonidir. Beden ise ruhun üzerine gerilmiş bir arp gibidir; doğru nefes, saf niyet ve kutsal ilahilerle çalındığında bedenin her hücresi cennetin armonisine katılır.",
    "category": "mistik_akustik",
    "freq": 528.0,
    "reflection": "Orta Çağ tıbbı ve mistisizminde kadın hekim ve bestecinin bedeni kutsal bir çalgı olarak görmesi."
  },
  {
    "id": "schopenhauer_music_will",
    "author": "Arthur Schopenhauer",
    "era": "18. - 19. Yüzyıl (1788 - 1860)",
    "work": "Die Welt als Wille und Vorstellung (İrade ve Tasavvur Olarak Dünya, 1819)",
    "quote": "Müzik, diğer sanatlar gibi fenomenlerin (görüntülerin) gölgesini değil; doğrudan doğruya İrade'nin (varoluşun gizli özünün) kendisini tasvir eder. İşte bu yüzden müziğin insan ruhuna tesiri diğer bütün sanatlardan katbekat derin, katbekat keskin ve katbekat şifalıdır.",
    "category": "antik_felsefe",
    "freq": 432.0,
    "reflection": "Müziğin ontolojik üstünlüğü: Temsili değil, doğrudan doğruya yaşam enerjisini seslendirmesi."
  },
  {
    "id": "bach_glory_refreshment",
    "author": "Johann Sebastian Bach",
    "era": "17. - 18. Yüzyıl (1685 - 1750)",
    "work": "Müzikal Otobiyografi ve İthaflar",
    "quote": "Mûsikînin tek ve nihai gayesi, Allah'ın celâlini yüceltmek ve insan ruhunu tazeleyip ferahlatmaktır. Bu yüce niyetin bulunmadığı yerde mûsikî yoktur; orada sadece şeytani bir kakofoni ve gürültü vardır.",
    "category": "mistik_akustik",
    "freq": 432.0,
    "reflection": "Barok matematiğinin ve kontrpuan nizamının zihinsel dinginlik ve huşu üretmesi."
  },
  {
    "id": "mozart_silence_between_notes",
    "author": "Wolfgang Amadeus Mozart",
    "era": "18. Yüzyıl (1756 - 1791)",
    "work": "Mektuplar ve Müzikal Düşünceler",
    "quote": "Müzik sadece notalarda değildir; asıl müzik, notaların arasındaki o esrarengiz sessizliktedir. İki ses arasındaki nefes aralığı, ruhun kanat çırptığı boşluktur.",
    "category": "mistik_akustik",
    "freq": 432.0,
    "reflection": "Es (sessizlik) ve rezonans dengesi: Terapötik müziğin zihinde açtığı dingin boşluk."
  },
  {
    "id": "debussy_sound_color",
    "author": "Claude Debussy",
    "era": "19. - 20. Yüzyıl (1862 - 1918)",
    "work": "Mösyö Krok ile Söyleşiler",
    "quote": "Müzik, doğanın görünmez güçlerinin renklerle ve ses dalgalarıyla zamanda akıp giden şiiridir. Rüzgarın sesini, denizin dalgalanışını ve gün batımının sükutunu ancak kuralların zincirini kıran saf nağmeler anlatabilir.",
    "category": "mistik_akustik",
    "freq": 528.0,
    "reflection": "Empresyonist akustik: Doğanın su ve rüzgar harmoniklerinin insan sinir sistemine dinginlik aşılaması."
  },
  {
    "id": "kandinsky_soul_piano",
    "author": "Wassily Kandinsky",
    "era": "19. - 20. Yüzyıl (1866 - 1944)",
    "work": "Sanatta Ruhsallık Üzerine (Über das Geistige in der Kunst, 1912)",
    "quote": "Renk bir tuş, göz bir çekiç, ruh ise telleri olan bir piyanodur. Sanatçı, insan ruhunu belirli frekanslarda titreştirmek için şu veya bu tuşa dokunan eldir.",
    "category": "mistik_akustik",
    "freq": 528.0,
    "reflection": "Sinestezi: Renk, ışık ve ses frekanslarının insan beyninde tek bir duyusal rezonans oluşturması."
  },
  {
    "id": "rilke_orpheus_song",
    "author": "Rainer Maria Rilke",
    "era": "19. - 20. Yüzyıl (1875 - 1926)",
    "work": "Orpheus'a Soneler (Die Sonette an Orpheus, 1922)",
    "quote": "Şarkı söylemek bir arzu değildir; şarkı söylemek varoluşun ta kendisidir! Bir Tanrı için bu kolaydır; lakin biz insanlar rüzgarın nefesinde kendi varlığımızın saf melodisini ne zaman duyacağız?",
    "category": "mistik_akustik",
    "freq": 432.0,
    "reflection": "Ses ve şarkının insan varoluşunun ontolojik derinliğini açığa çıkarması."
  },
  {
    "id": "oliver_sacks_musicophilia",
    "author": "Dr. Oliver Sacks",
    "era": "20. - 21. Yüzyıl (1933 - 2015)",
    "work": "Musicophilia: Tales of Music and the Brain (2007)",
    "quote": "Müzik, beynin diğer hiçbir uyarana tepki vermediği kadar geniş ağlarını aynı anda harekete geçirir: Motor korteks, amigdala, hipokampus ve temporal lob birlikte ateşlenir. Ağır demans ve Alzheimer hastaları konuşmayı ve sevdiklerinin adını unutsalar dahi, gençliklerinde dinledikleri bir ezgiyi kusursuzca mırıldanabilirler; çünkü müzik ruhun silinmez belleğidir.",
    "category": "bilim_ve_fizik",
    "freq": 432.0,
    "reflection": "Nöromüzikoloji: Ses terapisinin nörodejeneratif hastalıklarda derin nöral yolları canlı tutması."
  },
  {
    "id": "bruce_lipton_biology_belief",
    "author": "Dr. Bruce H. Lipton",
    "era": "20. - 21. Yüzyıl (1944 - Günümüz)",
    "work": "The Biology of Belief (İnancın Biyolojisi, 2005)",
    "quote": "Hücre zarlarımız, iç mekanizmayı yöneten katı genetik programlar değil; çevreden gelen titreşimsel, akustik ve elektromanyetik sinyalleri okuyan sıvı kristal çiplerdir. Bedeniniz bir frekans alıcısıdır; dinlediğiniz harmonikler ve beslediğiniz düşünceler genlerinizin ifadesini doğrudan değiştirir.",
    "category": "bilim_ve_fizik",
    "freq": 528.0,
    "reflection": "Epigenetik ve akustik biyoloji: Ses dalgalarının hücre zarı reseptörlerini aktive etmesi."
  },
  {
    "id": "candace_pert_molecules_emotion",
    "author": "Dr. Candace Pert",
    "era": "20. - 21. Yüzyıl (1946 - 2013)",
    "work": "Molecules of Emotion (Duygu Molekülleri, 1997)",
    "quote": "Bedenimiz ve zihnimiz ayrı iki yapı değildir; onlar neuropeptid moleküllerinin kesintisiz dans ettiği tek bir 'psikonöroimmünolojik' rezonatördür. Her duygu ve her müzik notası bu molekülleri belirli bir frekansta titreştirir. Doğru frekanstaki ses, kilitlenmiş travma reseptörlerini gevşeterek bedeni kimyasal krizden kurtarır.",
    "category": "bilim_ve_fizik",
    "freq": 639.0,
    "reflection": "Duyguların biyokimyasal rezonansı: Sesle hücresel travma çözünmesi ve vagal rahatlama."
  },
  {
    "id": "mitchell_gaynor_healing_sound",
    "author": "Dr. Mitchell L. Gaynor (Onkolog)",
    "era": "20. - 21. Yüzyıl (1956 - 2015)",
    "work": "The Healing Power of Sound (Sesin İyileştirici Gücü, 1999)",
    "quote": "Kanser hastalarımda Tibet kaseleri ve ses terapisi kullandığımda gördüm ki; ses dalgaları kemoterapinin asla ulaşamadığı derin hücre çekirdeğine, hücresel strese ve ruhsal buhrana dokunmaktadır. Ses, bağışıklık sisteminin uykudaki askerlerini uyandıran bir boru sesidir.",
    "category": "islam_tibbi",
    "freq": 528.0,
    "reflection": "Integratif onkoloji ve akustik terapi: Bağışıklık hücrelerinin frekans uyarımıyla güçlenmesi."
  },
  {
    "id": "john_stuart_reid_cymatics_water",
    "author": "John Stuart Reid",
    "era": "20. - 21. Yüzyıl (Akustik Bilimci)",
    "work": "CymaScope & Hücresel Ses Araştırmaları",
    "quote": "Ses sadece havadaki bir dalga değil; temas ettiği su moleküllerini anında organize eden küresel bir basınç mandalasıdır. İnsan hücreleri ses dalgalarıyla karşılaştığında, hücre zarı mikroskobik bir davul derisi gibi esner ve hücre içi toksin atılımı hızlanır. Bizler sudan dokunmuş şarkılarız.",
    "category": "bilim_ve_fizik",
    "freq": 432.0,
    "reflection": "CymaScope bulguları: Sesin küresel basınç geometrisi ve hücre hidrasyonunu desteklemesi."
  },
  {
    "id": "meg_jordan_vagus_sound",
    "author": "Dr. Meg Jordan",
    "era": "21. Yüzyıl",
    "work": "İntegratif Sağlık ve Vagus Siniri Terapisi",
    "quote": "Vagus siniri ses terapisinin bedendeki süper otoyoludur. Ağızdan çıkarılan uzun bir 'OM', 'HU' veya 'ÂMÎN' sesi vokal kordları titreştirerek vagusu aktive eder; saniyeler içinde kan basıncı düşer, kalp ritmi sakinleşir ve beden 'dinlen ve onar' moduna geçer.",
    "category": "islam_tibbi",
    "freq": 136.1,
    "reflection": "Vokal tonlama ve zikrin vagal tonus üzerindeki doğrudan nörobiyolojik regülasyonu."
  },
  {
    "id": "pythagoras_golden_verses",
    "author": "Pisagor (Pythagoras)",
    "era": "M.Ö. 6. Yüzyıl (M.Ö. 570 - 495)",
    "work": "Altın Dizeler (Aurea Carmina)",
    "quote": "Gözlerini gece uykusuna teslim etmeden evvel, o gün yaptığın bütün amelleri üç kez zihninden geçir. Zihnini yatıştırmak için parmaklarını lirin tellerinde gezdir ve ruhunu mûsikînin sularında yıka. O vakit rüyaların semavi hakikatlerle dolar.",
    "category": "antik_felsefe",
    "freq": 432.0,
    "reflection": "Akşam ritüeli ve sirkadiyen akustik: Uyku öncesi telli çalgı armonikleriyle zihinsel arınma."
  },
  {
    "id": "farabi_saray_efsanesi",
    "author": "Ebû Nasr el-Fârâbî",
    "era": "9. - 10. Yüzyıl (872 - 950)",
    "work": "Seyfullah Devle Sarayı Meclis Rivayeti",
    "quote": "Fârâbî Şam Emiri'nin sarayında udunu çıkarıp telleri bir türlü bağladı ve öyle bir ezgi çaldı ki meclisteki herkes kahkahalarla gülmeye başladı. Sonra telleri değiştirdi, öyle bir makam çaldı ki vezirlerden kölelere kadar herkes hıçkırıklarla ağladı. Sonra telleri bir daha değiştirdi, öyle bir tını üfledi ki nöbetçiler dahil bütün saray ahalisi tatlı ve derin bir uykuya daldı; Fârâbî ise oradan sessizce ayrıldı.",
    "category": "islam_tibbi",
    "freq": 220.0,
    "reflection": "Akustik modülasyon dehası: Müzikal aralıkların insan biyokimyasını ve duygu durumunu anında değiştirmesi."
  },
  {
    "id": "hz_ali_kelam_esir",
    "author": "Hz. Ali (k.v.)",
    "era": "7. Yüzyıl (599 - 661)",
    "work": "Nehcü'l-Belâga (Belâgat Yolu)",
    "quote": "Söz senin ağzında hapsedildikçe senin esirindir; lakin bir kere ağzından fırladı mı sen onun esiri olursun. Dilini koru, sesini tart; zira güzel kelâm hasta kalplere şifa, kötü söz ise sağlam göğüslere zehirdir.",
    "category": "tasavvuf",
    "freq": 432.0,
    "reflection": "Sözün niyet ve sorumluluk boyutu: Yaydığımız akustik frekansın kendi yaşam alanımızı mühürlemesi."
  },
  {
    "id": "cafer_sadik_harf_menzil",
    "author": "İmâm Ca'fer es-Sâdık",
    "era": "8. Yüzyıl (702 - 765)",
    "work": "İlm-i Hurûf ve Esrâr-ı Kelâm",
    "quote": "Ağızdan çıkan her harfin gökyüzünde bir yıldızı, yeryüzünde bir unsuru ve bedende bir organı titreştiren gizli bir menzili vardır. Ağzını temiz tutanın kelâmı hastaya dokunduğunda deva olur.",
    "category": "tasavvuf",
    "freq": 528.0,
    "reflection": "Harf formantları ve biyo-rezonans: Fonetik artikülasyonun hücresel organ yansımaları."
  },
  {
    "id": "ibn_tufeyl_hayy_ses",
    "author": "İbn Tufeyl",
    "era": "12. Yüzyıl (1105 - 1185)",
    "work": "Hayy bin Yakzân (Esrârü'l-Hikmeti'l-Meşrikiyye)",
    "quote": "Hayy ıssız adada büyürken tabiatın seslerini dinledi: Rüzgarın kamışlıktaki uğultusunu, suyun şırıltısını, kuşların terennümünü taklit etti. Gördü ki bütün bu sesler rastgele bir gürültü değil; tek bir Görünmez Musavvir'in kâinat kubbesinde terennüm ettiği aşkın bir senfonidir.",
    "category": "tasavvuf",
    "freq": 432.0,
    "reflection": "Biyo-akustik uyanış: Tabiatın seslerindeki fraktal harmoniklerin tevhidi fısıldaması."
  },
  {
    "id": "hafiz_sirazi_kubbe_sadasi",
    "author": "Hâfız-ı Şîrâzî",
    "era": "14. Yüzyıl (1315 - 1390)",
    "work": "Dîvân-ı Hâfız",
    "quote": "Ez-sedâ-yı sühen-i aşk nedîdem hoş-ter / Yâdgârî ki der-în günbed-i devvâr bimând: Şu dönen gök kubbenin altında aşk sözünden ve onun nağmesinden daha hoş, daha kalıcı bir yâdigâr görmedim.",
    "category": "tasavvuf",
    "freq": 432.0,
    "reflection": "Fani dünyada ebediyen yankılanan tek rezonansın sevgi ve şefkat frekansı olması."
  },
  {
    "id": "fuzuli_can_bahs_soz",
    "author": "Fuzûlî",
    "era": "16. Yüzyıl (1483 - 1556)",
    "work": "Dîvân Mukaddimesi",
    "quote": "Söz cevher-i cân-bahş-ı ten-i hastadır ey dil / Söz söyle ki söz derdine derman ola bilsin... Şair odur ki her sözü can bağışlayan bir iksir gibi dinleyenin kırık kalbine merhem olsun.",
    "category": "tasavvuf",
    "freq": 432.0,
    "reflection": "Kelâmın can bahşeden (biyo-rejeneratif) boyutu: Edebi ve akustik inceliğin hücresel teskini."
  },
  {
    "id": "baki_hos_sada",
    "author": "Bâkî (Sultânü'ş-Şuarâ)",
    "era": "16. Yüzyıl (1526 - 1600)",
    "work": "Dîvân-ı Bâkî",
    "quote": "Âvâzeyi bu âleme Dâvûd gibi sal / Bâkî kalan bu kubbede bir hoş sadâ imiş... Şöhret de biter, taht da geçer; gök kubbede ebediyen titreşen ancak Hakk uğruna söylenmiş bir hoş sadâdır.",
    "category": "tasavvuf",
    "freq": 432.0,
    "reflection": "Davudi nida ve ebedi yankı: Sesin zamanda sönmeyen dalga formları."
  },
  {
    "id": "itri_segah_tekbir",
    "author": "Itrî (Buhûrîzâde Mustafa Efendi)",
    "era": "17. - 18. Yüzyıl (1640 - 1712)",
    "work": "Segâh Salât-ı Ümmiyye ve Segâh Bayram Tekbîri",
    "quote": "Segâh Tekbir öyle bir nağmedir ki; milyonlarca insan aynı anda tek bir nefes ve tek bir perdeyle 'Allahu Ekber' dediğinde yeryüzü adeta semaya yükselir, bütün sinirler ve yürekler aynı kutsal ritimde erir.",
    "category": "tasavvuf",
    "freq": 396.0,
    "reflection": "Kolektif koro koheransı: Milyonların aynı frekansta rezonansa girerek oluşturduğu devasa manyetik alan."
  },
  {
    "id": "dede_efendi_ferahfeza",
    "author": "Hammâmîzâde İsmâil Dede Efendi",
    "era": "18. - 19. Yüzyıl (1778 - 1846)",
    "work": "Ferahfezâ Âyîn-i Şerîfi",
    "quote": "Makam bir yolculuktur; neyzenin nefesiyle neva perdesinde seher gibi doğar, meyan köşkünde kalbin en derin sırlarını ifşa eder ve karar perdesinde teslimiyetle Hakk'ın sükunetinde karar kılar.",
    "category": "islam_tibbi",
    "freq": 261.63,
    "reflection": "Makam seyrinin arketipsel psikolojik evreleri: Doğuş (giriş), fırtına (meyan) ve itidal (karar)."
  },
  {
    "id": "neyzen_tevfik_kamis",
    "author": "Neyzen Tevfik (Kolaylı)",
    "era": "19. - 20. Yüzyıl (1879 - 1953)",
    "work": "Azâb-ı Mukaddes & Ney Taksimleri",
    "quote": "Ney kuru bir kamıştan ibarettir; lakin o kamışın deliklerinden inleyen ses kamışın değil, ona üfleyen dertli bağrın ateşidir. Asıl marifet kamışı değil, ona o can nefesini bahşeden Sahib-i Nefes'i duyabilmektir.",
    "category": "tasavvuf",
    "freq": 220.0,
    "reflection": "Arınma ve boşalma: Ney gibi benlik kirini boşaltmadan hakiki sesin çıkamayacağı hakikati."
  },
  {
    "id": "tanpinar_huzur_musiki",
    "author": "Ahmet Hamdi Tanpınar",
    "era": "20. Yüzyıl (1901 - 1962)",
    "work": "Huzur Romanı (1949)",
    "quote": "Bizim klasik mûsikîmiz, bir medeniyetin kendi iç dünyasında kurduğu en muazzam metafizik katedraldir. Itrî'nin Neva Kâr'ını dinlerken zaman durur; insan kendi faniliğinden sıyrılıp ebedi bir itidal havuzuna dalar.",
    "category": "mistik_akustik",
    "freq": 432.0,
    "reflection": "Zamansızlık hissi (flow): Klasik nağmelerin zihinsel zaman algısını yavaşlatması."
  },
  {
    "id": "stravinsky_music_order",
    "author": "Igor Stravinsky",
    "era": "20. Yüzyıl (1882 - 1971)",
    "work": "Poetics of Music (Müziğin Poetikası, 1942)",
    "quote": "Müziğin tek varlık gayesi, insan ile zaman arasındaki nizamı ve ahengi tesis etmektir. Kaotik akan zamanı alır, onu ritim ve aralıklarla kutsal bir geometriye kavuşturur.",
    "category": "antik_felsefe",
    "freq": 432.0,
    "reflection": "Zamanın akustik geometrisi: Kronolojik zamanı (Chronos) niteliksel kutsal zamana (Kairos) dönüştürme."
  },
  {
    "id": "carl_jung_music_archetype",
    "author": "Carl Gustav Jung",
    "era": "19. - 20. Yüzyıl (1875 - 1961)",
    "work": "Kolektif Bilinçdışı ve Arketipler",
    "quote": "Müzik, doğrudan doğruya kolektif bilinçdışının en derin arketiplerine hitap eder. Kelimelerin ulaşamadığı bilinçaltı travmaları ve gölge yönler, sesin dönüştürücü simyasıyla serbest kalır ve benlik bütünleşir.",
    "category": "bilim_ve_fizik",
    "freq": 432.0,
    "reflection": "Analitik psikoloji ve ses: Bilinçdışı düğümlerin arketipsel tınılarla çözülmesi."
  },
  {
    "id": "wilhelm_reich_armor_sound",
    "author": "Dr. Wilhelm Reich",
    "era": "20. Yüzyıl (1897 - 1957)",
    "work": "Karakter Analizi ve Bedensel Zırh Teorisi",
    "quote": "Bastırılmış her çocukluk acısı ve korku bedende kronik bir kas spazmı ('bedensel zırh') olarak donup kalır. Doğru frekanslı ses titreşimleri, diyafram nefesi ve rezonans bu zırhı titreterek çözer ve yaşam enerjisinin (orgon) yeniden akmasını sağlar.",
    "category": "bilim_ve_fizik",
    "freq": 174.0,
    "reflection": "Somatik psikoterapi: Beden zırhının rezonant frekanslarla gevşetilmesi ve enerji akışı."
  },
  {
    "id": "tchaikovsky_words_stop_music",
    "author": "Pyotr Ilyich Tchaikovsky",
    "era": "19. Yüzyıl (1840 - 1893)",
    "work": "Nadezhda von Meck'e Mektuplar (1878)",
    "quote": "Kelimelerin tükendiği, dilin kifayetsiz kaldığı yerde müzik başlar. Kalbimin öyle derin yaraları ve feryatları vardır ki, onları hiçbir lisanda söyleyemem; ancak bir kemanın ağlayışında ifşa edebilirim.",
    "category": "mistik_akustik",
    "freq": 639.0,
    "reflection": "Duygusal katarsis: Dilin sınırlarını aşan saf müzikal sağaltım."
  },
  {
    "id": "mahler_tradition_fire",
    "author": "Gustav Mahler",
    "era": "19. - 20. Yüzyıl (1860 - 1911)",
    "work": "Senfonik Sohbetler ve Aforizmalar",
    "quote": "Müzikte gelenek küllere tapınmak değil, ateşi canlı tutmaktır! Bir senfoni inşa etmek, ses dalgalarıyla kainatı yeniden yaratmak demektir. Her nota bir gezegen, her aralık bir yerçekimidir.",
    "category": "mistik_akustik",
    "freq": 432.0,
    "reflection": "Kozmik senfoni inşası: Makrokozmosun müzikal mimaride yeniden doğuşu."
  },
  {
    "id": "munir_nurettin_saffet",
    "author": "Münir Nurettin Selçuk",
    "era": "20. Yüzyıl (1900 - 1981)",
    "work": "Klasik Türk Musikisi İcra Notları",
    "quote": "Bizim musikimiz gırtlak cambazlığı değildir; o, insanın kendi iç derinliğini dinleme sanatıdır. Makamı doğru icra eden hanendede kibir erir, benlik kaybolur; geriye sadece saf ve arı bir ruh kalır.",
    "category": "islam_tibbi",
    "freq": 220.0,
    "reflection": "İcra ahlakı ve vokal rezonans: Şarkıcının egosuzlaşarak ses kanalına dönüşmesi."
  },
  {
    "id": "averroes_de_anima_sound",
    "author": "İbn Rüşd (Averroes)",
    "era": "12. Yüzyıl (1126 - 1198)",
    "work": "Telhîsu Kitâbi'n-Nefs (De Anima Şerhi)",
    "quote": "Ses, havada titreşen maddi bir hareket olarak başlar; lakin kulak zarına ulaştığında ruh onu gayri maddi, saf bir anlam suretine dönüştürür. Ses duyusu, maddi dünya ile ruhani dünya arasındaki en asil köprüdür.",
    "category": "antik_felsefe",
    "freq": 432.0,
    "reflection": "Akustik epistemoloji: Mekanik hava dalgasının bilinçte manaya ve idrake dönüşümü."
  },
  {
    "id": "yahya_kemal_musiki_ruh",
    "author": "Yahya Kemal Beyatlı",
    "era": "19. - 20. Yüzyıl (1884 - 1958)",
    "work": "Kendi Gök Kubbemiz (Eski Mûsikî)",
    "quote": "Çok insan anlayamaz eski mûsikîmizden / Ve ondan anlamayan bir şey anlamaz bizden... O mûsikî ki, asırlarca ruhumuzun sığındığı liman, zaferlerimizin sevinci ve kederlerimizin en asil tesellisi olmuştur.",
    "category": "tasavvuf",
    "freq": 220.0,
    "reflection": "Kültürel ve kolektif akustik hafıza: Medeniyet ruhunun makamlarla taşınması."
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

  // Meditatif Makam Seyir Sentezleyici (Ney tınısı & yumuşak vibrato)
  playSeyir(makamId, onNoteChange, onComplete) {
    this.init();
    this.stopTone();
    this.stopBinaural();
    this.stopIsochronic();

    const makam = MAKAM_DATA.find(m => m.id === makamId) || MAKAM_DATA[0];
    const baseFreq = makam.ratios ? (makam.root.includes("G") ? 196.0 : 220.0) : 220.0;
    
    // Seyir nota akış şablonları
    const templates = {
      rast: [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0],
      nihavend: [4, 3, 2, 1, 0, 2, 4, 5, 7, 6, 5, 4, 3, 2, 1, 0],
      hicaz: [0, 1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 2, 1, 0],
      ussak: [0, 1, 2, 3, 4, 3, 2, 1, 0]
    };
    const seq = templates[makamId] || templates.rast;

    let idx = 0;
    const playNext = () => {
      if (idx >= seq.length) {
        if (onComplete) onComplete();
        return;
      }
      const noteIdx = seq[idx];
      const ratio = makam.ratios[noteIdx] || 1.0;
      const freq = baseFreq * ratio;
      const isKarar = (idx === seq.length - 1);
      const dur = isKarar ? 2400 : 700;

      // Yumuşak ney tonu üret
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime);

      const now = this.ctx.currentTime;
      gain.gain.setValueAtTime(0.001, now);
      gain.gain.linearRampToValueAtTime(0.25, now + 0.15);
      gain.gain.setValueAtTime(0.20, now + (dur / 1000) * 0.7);
      gain.gain.linearRampToValueAtTime(0.001, now + (dur / 1000));

      osc.connect(gain);
      gain.connect(this.masterGain);
      osc.start(now);
      osc.stop(now + (dur / 1000));

      if (onNoteChange) onNoteChange(freq, noteIdx);
      if (cymaticsSim) cymaticsSim.setFrequency(freq);

      idx++;
      setTimeout(playNext, dur + 40);
    };

    playNext();
  }

  // Protokol Seans Yürütücüsü
  startProtocol(protocol, onProgress, onComplete) {
    this.stopProtocol();
    this.init();

    this.activeProtocol = protocol;
    const totalDurationSeconds = 120; // Hızlı ve etkili web demosu için 2 dakika
    let elapsedSeconds = 0;

    const stages = protocol.stages;
    let currentStageIndex = 0;

    const applyStage = (sIdx) => {
      if (sIdx >= stages.length) return;
      const st = stages[sIdx];
      this.playBinaural(st.carrierFreq, st.beat_freq);
      this.playNoise(st.noise_type, st.noise_volume * 1.5);
      if (cymaticsSim) cymaticsSim.setFrequency(st.carrierFreq);
    };

    applyStage(0);

    this.protocolTimer = setInterval(() => {
      elapsedSeconds++;
      const progressPercent = (elapsedSeconds / totalDurationSeconds) * 100;

      // Mevcut aşamayı hesapla
      let accumTime = 0;
      let calculatedStage = 0;
      for (let i = 0; i < stages.length; i++) {
        const stageSec = (stages[i].duration_percent / 100) * totalDurationSeconds;
        accumTime += stageSec;
        if (elapsedSeconds <= accumTime) {
          calculatedStage = i;
          break;
        }
      }

      if (calculatedStage !== currentStageIndex) {
        currentStageIndex = calculatedStage;
        applyStage(currentStageIndex);
      }

      const remainingSec = Math.max(0, totalDurationSeconds - elapsedSeconds);
      if (onProgress) {
        onProgress({
          progressPercent,
          currentStage: stages[currentStageIndex],
          stageIndex: currentStageIndex + 1,
          totalStages: stages.length,
          remainingSeconds: remainingSec
        });
      }

      if (elapsedSeconds >= totalDurationSeconds) {
        this.stopProtocol();
        if (onComplete) onComplete();
      }
    }, 1000);
  }

  stopProtocol() {
    if (this.protocolTimer) {
      clearInterval(this.protocolTimer);
      this.protocolTimer = null;
    }
    this.activeProtocol = null;
    this.stopBinaural();
    this.stopNoise();
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
      <div class="makam-action mt-3" style="display: flex; gap: 10px; flex-wrap: wrap;">
        <button id="playMakamBtn" class="btn btn-primary">🎶 Makam Dizisini Dinle (Şifa Arpeji)</button>
        <button id="playMakamSeyirBtn" class="btn btn-outline-gold">🕌 Meditatif Ney Seyri (Taksim)</button>
      </div>
    `;

    document.getElementById("playMakamBtn").addEventListener("click", () => {
      audio.playMakamScale(makam);
    });

    document.getElementById("playMakamSeyirBtn").addEventListener("click", () => {
      audio.playSeyir(makam.id);
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
  renderProtocols();
  renderChakras();
  renderOrgans();
  setupBreathGuide();
  renderPhonetics();
  setupBreathing();
  setupSessionTimer();
  setupWisdomBanner();
});

// ==========================================
// 5. TITRESIM v2.0: PROTOKOL VE CAKRA RENDER
// ==========================================
function renderProtocols() {
  const container = document.getElementById("protocolsGrid");
  if (!container) return;
  container.innerHTML = "";

  const activeBox = document.getElementById("activeProtocolBox");
  const stopBtn = document.getElementById("stopProtocolBtn");
  const pBar = document.getElementById("protocolProgressBar");
  const pStage = document.getElementById("activeProtocolStage");
  const pTimer = document.getElementById("activeProtocolTimer");
  const pDesc = document.getElementById("activeProtocolDesc");
  const pTitle = document.getElementById("activeProtocolTitle");

  if (stopBtn) {
    stopBtn.onclick = () => {
      audio.stopProtocol();
      activeBox.classList.add("hidden");
    };
  }

  PROTOCOLS_DATA.forEach(p => {
    const card = document.createElement("div");
    card.className = "protocol-card";
    card.innerHTML = `
      <div class="protocol-card-header">
        <div class="protocol-card-title">${p.title}</div>
        <div class="protocol-card-duration">⏱️ ${p.total_recommended_minutes} Dk (Demo: 2 Dk)</div>
      </div>
      <div class="protocol-card-desc">${p.subtitle} • <em>Hedef: ${p.target}</em></div>
      <div class="protocol-stages-list">
        ${p.stages.map(s => `<span class="stage-pill">Aşama ${s.stage}: ${s.band} (${s.carrier_freq}Hz / ${s.beat_freq}Hz)</span>`).join("")}
      </div>
      <button class="btn btn-primary start-proto-btn">▶️ Protokol Seansını Başlat</button>
    `;

    card.querySelector(".start-proto-btn").addEventListener("click", () => {
      activeBox.classList.remove("hidden");
      pTitle.innerText = `Aktif Seans: ${p.title}`;
      pBar.style.width = "0%";

      audio.startProtocol(
        p,
        (progress) => {
          pBar.style.width = `${progress.progressPercent}%`;
          pStage.innerText = `Aşama: ${progress.stageIndex} / ${progress.totalStages} (${progress.currentStage.band})`;
          const mins = Math.floor(progress.remainingSeconds / 60);
          const secs = progress.remainingSeconds % 60;
          pTimer.innerText = `Kalan: ${mins.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`;
          pDesc.innerText = `"${progress.currentStage.name}": ${progress.currentStage.description}`;
        },
        () => {
          activeBox.classList.add("hidden");
          alert(`"${p.title}" seansı başarıyla tamamlandı. Şifa ve itidal olsun.`);
        }
      );
    });

    container.appendChild(card);
  });
}

function renderChakras() {
  const container = document.getElementById("chakrasList");
  if (!container) return;
  container.innerHTML = "";

  const getMode = () => {
    const checked = document.querySelector('input[name="chakraMode"]:checked');
    return checked ? checked.value : "solfeggio";
  };

  const rainbowBtn = document.getElementById("rainbowAlignmentBtn");
  if (rainbowBtn) {
    rainbowBtn.onclick = () => {
      let cIdx = 0;
      rainbowBtn.disabled = true;
      rainbowBtn.innerText = "🌈 Gökkuşağı Dengeleniyor...";

      const playNextChakra = () => {
        if (cIdx >= CHAKRAS_DATA.length) {
          rainbowBtn.disabled = false;
          rainbowBtn.innerText = "🌈 Gökkuşağı Dengeleme Dizisini Başlat (1 → 7)";
          audio.stopTone();
          return;
        }
        const ch = CHAKRAS_DATA[cIdx];
        const freq = ch.solfeggio_freq;
        audio.playTone(freq);
        if (cymaticsSim) cymaticsSim.setFrequency(freq);

        document.querySelectorAll(".chakra-card").forEach(c => c.classList.remove("playing"));
        const activeCard = document.querySelector(`[data-chakra-id="${ch.id}"]`);
        if (activeCard) activeCard.classList.add("playing");

        cIdx++;
        setTimeout(playNextChakra, 2500);
      };

      playNextChakra();
    };
  }

  CHAKRAS_DATA.forEach(ch => {
    const card = document.createElement("div");
    card.className = "chakra-card";
    card.setAttribute("data-chakra-id", ch.id);
    card.innerHTML = `
      <div class="chakra-color-strip" style="background: ${ch.color};"></div>
      <div class="chakra-card-top">
        <div class="chakra-title-group">
          <h3>${ch.name}</h3>
          <div class="chakra-subtitle">📍 ${ch.location} • Element: ${ch.element}</div>
        </div>
        <div class="bija-badge">${ch.bija_mantra}</div>
      </div>
      <div class="chakra-meta-row">
        <span>Solfeggio: <strong class="solf-val">${ch.solfeggio_freq} Hz</strong></span> •
        <span>Cousto Gezegen: <strong>${ch.planetary_freq} Hz</strong></span> •
        <span>Nota: <strong>${ch.note}</strong></span> •
        <span>Organlar: <em>${ch.organs}</em></span>
      </div>
      <div class="chakra-effects">
        ✨ <strong>Denge:</strong> ${ch.balance_effect}
      </div>
      <div class="chakra-card-actions">
        <span class="chakra-freq-label" style="color: ${ch.color};">● ${ch.color} Titreşimi</span>
        <button class="btn btn-sm btn-outline play-chakra-btn">Titreşimi Dinle</button>
      </div>
    `;

    card.querySelector(".play-chakra-btn").addEventListener("click", () => {
      const mode = getMode();
      const targetFreq = mode === "solfeggio" ? ch.solfeggio_freq : ch.planetary_freq;
      document.querySelectorAll(".chakra-card").forEach(c => c.classList.remove("playing"));
      card.classList.add("playing");
      audio.playTone(targetFreq);
      if (cymaticsSim) cymaticsSim.setFrequency(targetFreq);
    });

    container.appendChild(card);
  });
}

// ==========================================
// 6. TITRESIM v2.1: ORGAN, NEFES & VOKAL RENDER
// ==========================================
function renderOrgans() {
  const container = document.getElementById("organsGrid");
  if (!container) return;
  container.innerHTML = "";

  const scanBtn = document.getElementById("fullBodyScanBtn");
  if (scanBtn) {
    scanBtn.onclick = () => {
      scanBtn.disabled = true;
      scanBtn.innerText = "🧬 Tüm Beden Taranıyor (10 Organ)...";
      let oIdx = 0;

      const playNextOrgan = () => {
        if (oIdx >= ORGANS_DATA.length) {
          scanBtn.disabled = false;
          scanBtn.innerText = "Tam Beden Organ Taraması Başlat (10 Organ)";
          audio.stopTone();
          return;
        }
        const org = ORGANS_DATA[oIdx];
        audio.playTone(org.frequency);
        if (cymaticsSim) cymaticsSim.setFrequency(org.frequency);

        document.querySelectorAll(".organ-card").forEach(c => c.classList.remove("playing"));
        const activeCard = document.querySelector(`[data-organ-id="${org.id}"]`);
        if (activeCard) activeCard.classList.add("playing");

        oIdx++;
        setTimeout(playNextOrgan, 3000);
      };

      playNextOrgan();
    };
  }

  ORGANS_DATA.forEach(org => {
    const card = document.createElement("div");
    card.className = "organ-card";
    card.setAttribute("data-organ-id", org.id);
    card.innerHTML = `
      <div class="organ-header">
        <span class="organ-title">${org.name}</span>
        <span class="organ-freq-badge">${org.frequency} Hz</span>
      </div>
      <div class="organ-desc">${org.description}</div>
      <div class="organ-effects">✨ <strong>Şifa:</strong> ${org.effects} • <em>Çakra: ${org.associated_chakra}</em></div>
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <span style="font-size: 11px; color: #94a3b8;">Protokol: ${org.healing_protocol}</span>
        <button class="btn btn-sm btn-outline play-organ-btn">Frekansı Çal</button>
      </div>
    `;

    card.querySelector(".play-organ-btn").addEventListener("click", () => {
      document.querySelectorAll(".organ-card").forEach(c => c.classList.remove("playing"));
      card.classList.add("playing");
      audio.playTone(org.frequency);
      if (cymaticsSim) cymaticsSim.setFrequency(org.frequency);
    });

    container.appendChild(card);
  });
}

const BREATH_PATTERNS = {
  coherence: { title: "0.10 Hz Kardiyak Koherans Nefesi", desc: "5.5s Alış, 5.5s Veriş ile vagal fren uyarımı ve maksimum HRV.", inhale: 5.5, holdIn: 0, exhale: 5.5, holdOut: 0 },
  box: { title: "Kutu Nefesi (Box Breathing)", desc: "4s Alış, 4s Tutuş, 4s Veriş, 4s Boş Tutuş ile panik bastırma.", inhale: 4.0, holdIn: 4.0, exhale: 4.0, holdOut: 4.0 },
  "4-7-8": { title: "4-7-8 Dr. Weil Uyku Nefesi", desc: "4s Burundan Alış, 7s Tutuş, 8s Ağızdan Veriş ile derin uyku.", inhale: 4.0, holdIn: 7.0, exhale: 8.0, holdOut: 0 },
  relax: { title: "Yumuşak Gevşeme Nefesi (1:1.5)", desc: "4s Alış, 6s Yavaş Veriş ile kas gevşemesi ve tansiyon düşüşü.", inhale: 4.0, holdIn: 0, exhale: 6.0, holdOut: 0 }
};

let activeBreathPattern = "coherence";
let breathTimer = null;
let breathTimeLeft = 0;

function setupBreathGuide() {
  const pTitle = document.getElementById("breathPatternTitle");
  const pDesc = document.getElementById("breathPatternDesc");
  const cText = document.getElementById("breathCircleText");
  const cTimer = document.getElementById("breathCircleTimer");
  const circle = document.getElementById("breathCircle");
  const startBtn = document.getElementById("startBreathBtn");
  const stopBtn = document.getElementById("stopBreathBtn");

  document.querySelectorAll(".breath-mode-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".breath-mode-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      activeBreathPattern = btn.getAttribute("data-pattern");
      const p = BREATH_PATTERNS[activeBreathPattern];
      if (pTitle) pTitle.innerText = p.title;
      if (pDesc) pDesc.innerText = p.desc;
      stopBreathingSession();
    });
  });

  function stopBreathingSession() {
    if (breathTimer) {
      clearInterval(breathTimer);
      breathTimer = null;
    }
    if (circle) {
      circle.style.transform = "scale(1.0)";
      circle.className = "breath-circle";
    }
    if (cText) cText.innerText = "HAZIR";
    if (cTimer) cTimer.innerText = "0.0s";
    if (startBtn) startBtn.classList.remove("hidden");
    if (stopBtn) stopBtn.classList.add("hidden");
    audio.stopTone();
  }

  if (stopBtn) stopBtn.onclick = stopBreathingSession;

  if (startBtn) {
    startBtn.onclick = () => {
      startBtn.classList.add("hidden");
      stopBtn.classList.remove("hidden");

      const p = BREATH_PATTERNS[activeBreathPattern];
      let currentPhase = "inhale"; // inhale, holdIn, exhale, holdOut
      let phaseTime = p.inhale;

      audio.playTone(216.0);

      const runPhase = () => {
        circle.className = `breath-circle ${currentPhase}`;
        if (currentPhase === "inhale") {
          cText.innerText = "NEFES AL";
          circle.style.transform = "scale(1.35)";
          audio.playTone(260.0);
        } else if (currentPhase === "holdIn") {
          cText.innerText = "NEFESİ TUT";
          audio.playTone(280.0);
        } else if (currentPhase === "exhale") {
          cText.innerText = "NEFES VER";
          circle.style.transform = "scale(0.85)";
          audio.playTone(200.0);
        } else if (currentPhase === "holdOut") {
          cText.innerText = "DİNLEN / TUT";
          audio.playTone(180.0);
        }
      };

      runPhase();
      let stepCountdown = phaseTime;

      breathTimer = setInterval(() => {
        stepCountdown -= 0.1;
        cTimer.innerText = `${Math.max(0, stepCountdown).toFixed(1)}s`;

        if (stepCountdown <= 0) {
          // Sıradaki faza geç
          if (currentPhase === "inhale") {
            if (p.holdIn > 0) { currentPhase = "holdIn"; phaseTime = p.holdIn; }
            else { currentPhase = "exhale"; phaseTime = p.exhale; }
          } else if (currentPhase === "holdIn") {
            currentPhase = "exhale"; phaseTime = p.exhale;
          } else if (currentPhase === "exhale") {
            if (p.holdOut > 0) { currentPhase = "holdOut"; phaseTime = p.holdOut; }
            else { currentPhase = "inhale"; phaseTime = p.inhale; }
          } else if (currentPhase === "holdOut") {
            currentPhase = "inhale"; phaseTime = p.inhale;
          }
          stepCountdown = phaseTime;
          runPhase();
        }
      }, 100);
    };
  }
}

function renderPhonetics() {
  const container = document.getElementById("vocalChantsList");
  if (!container) return;
  container.innerHTML = "";

  PHONETICS_DATA.forEach(chant => {
    const card = document.createElement("div");
    card.className = "chant-card";
    card.innerHTML = `
      <div class="chant-header">
        <span class="chant-title">${chant.name}</span>
        <span class="organ-freq-badge">${chant.base_pitch_hz} Hz</span>
      </div>
      <div style="font-size: 12px; color: #fde68a;">Gelenek: ${chant.tradition} • Mahreç: ${chant.mahref}</div>
      <div class="organ-desc mt-1">${chant.description}</div>
      <div class="formants-row">
        ${chant.formants.map((f, i) => `<span class="formant-pill">F${i+1}: ${f} Hz</span>`).join("")}
      </div>
      <div class="chant-no-effect">🧪 <strong>Biyoakustik Etki:</strong> ${chant.nitric_oxide_effect}</div>
      <div style="display: flex; justify-content: flex-end;">
        <button class="btn btn-sm btn-outline-gold play-chant-btn">🕊️ Vokal Formantını Dinle</button>
      </div>
    `;

    card.querySelector(".play-chant-btn").addEventListener("click", () => {
      document.querySelectorAll(".chant-card").forEach(c => c.classList.remove("playing"));
      card.classList.add("playing");
      audio.playTone(chant.base_pitch_hz);
      if (cymaticsSim) cymaticsSim.setFrequency(chant.base_pitch_hz);
    });

    container.appendChild(card);
  });
}
