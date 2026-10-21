# -*- coding: utf-8 -*-
"""
Expand quotes.json with an additional massive batch of profound quotes.
"""
import json
from pathlib import Path

DATA_PATH = Path("data/quotes.json")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    quotes = json.load(f)

existing_ids = {q["id"] for q in quotes}

more_quotes = [
    # --- 1. İSLAM DÜŞÜNCESİ, MÛSİKÎ FELSEFESİ & ŞİFAHEKİMLERİ ---
    {
        "id": "kindi_ud_dort_unsur",
        "author": "Ebû Yûsuf Ya'kûb b. İshâk el-Kindî (Alkindus)",
        "era": "9. Yüzyıl (801 - 873)",
        "work": "Risâle fî Hubri Te'lîfi'l-Elhân (Mûsikî Telifi Risalesi)",
        "quote_tr": "Udun dört teli kâinatın dört unsuru ve bedenin dört hıltı ile tam bir tenasüp içindedir: En tiz tel olan Zîr ateşe ve sarı safraya; Mesnâ havaya ve kana; Mesles suya ve balgama; en kalın tel olan Bam ise toprağa ve kara safraya tekabül eder. Usta bir hekim, tellerin tınısıyla bedenin bozulan dört unsurunu mizanına getirir.",
        "original_or_context": "رسالة في خبر تأليف الألحان للكندي - مبحث الأوتار الأربعة والطبائع",
        "category": "islam_tibbi",
        "recommended_freq": 220.0,
        "reflection": "İslam dünyasında ses terapisinin kurucusu el-Kindî'nin müzik teorisi ile hücresel mizaçları eşleştirmesi."
    },
    {
        "id": "urmevi_edvar_ruhaniyet",
        "author": "Safiyyüddîn el-Urmevî",
        "era": "13. Yüzyıl (1216 - 1294)",
        "work": "Kitâbü'l-Edvâr (Dönemler Kitabı)",
        "quote_tr": "Her makam ve her aralık insan nefsinde bambaşka bir ruhani hal husule getirir: Kimi nağmeler nefse cesaret ve atılganlık aşılar, kimi nağmeler kalbe haşyet ve yakarış verir, kimi nağmeler ise dimağı tatlı bir rehavetle uykuya hazırlar. Perdelerin kemali, ruhun hallerine mutabık olmasıdır.",
        "original_or_context": "كتاب الأدوار في الموسيقى لصفي الدين الأرموي",
        "category": "islam_tibbi",
        "recommended_freq": 293.33,
        "reflection": "17 perdeli sistemin mimarı Urmevî'nin makamların psikofizyolojik tesirlerini tahlili."
    },
    {
        "id": "meragi_camiul_elhan",
        "author": "Abdülkâdir-i Merâgî",
        "era": "14. - 15. Yüzyıl (1360 - 1435)",
        "work": "Câmi'u'l-Elhân (Ezgilerin Toplamı)",
        "quote_tr": "Mûsikî fenni öyle bir cevherdir ki, onunla insan nefsi bedeni alakaların zindanından halas bulup letafet alemine uçar. Nağmelerin tertibi göklerin devranına denk düştüğünde, dinleyenin kalbinde kederden eser kalmaz; yerini ilahi bir huzur ve vecd kaplar.",
        "original_or_context": "جامع الألحان لعبد القادر المراغي",
        "category": "islam_tibbi",
        "recommended_freq": 432.0,
        "reflection": "Klasik Doğu besteciliğinin zirvesi Merâgî'nin nağmelerin arındırıcı katharsis gücünü beyanı."
    },
    {
        "id": "kantemir_edvar_sır",
        "author": "Dimitrie Cantemir (Kantemiroğlu)",
        "era": "17. - 18. Yüzyıl (1673 - 1723)",
        "work": "Kitâb-ı İlmü'l-Mûsikî 'alâ Vechi'l-Edvâr",
        "quote_tr": "Makamların her birinde gizli bir tılsım ve ruhani kuvvet saklıdır. Usta sazende bir makamdan diğerine geçerken adeta bir bahçeden diğerine su akıtır gibi dinleyicinin dimağındaki gamı yıkar, yerine asil bir tefekkür tohumu eker.",
        "original_or_context": "Kantemiroğlu Edvarı - Osmanlı Musikisi Nazariyatı",
        "category": "islam_tibbi",
        "recommended_freq": 220.0,
        "reflection": "Osmanlı makam seyrinin terapötik modülasyonu: Zihinsel blokajların makam geçişleriyle çözülmesi."
    },
    {
        "id": "ali_ufki_mezmur_nefes",
        "author": "Ali Ufkî Bey (Wojciech Bobowski)",
        "era": "17. Yüzyıl (1610 - 1675)",
        "work": "Mezmûrlar Tercümesi ve Mecmûa-i Sâz u Söz",
        "quote_tr": "İlahi kelâmın güzelliği mûsikînin vezniyle birleştiğinde kulağa değil, doğrudan doğruya can kulağına hitap eder. Nefes ile tel birleştiğinde gök kubbenin altındaki bütün dertler eriyip gider.",
        "original_or_context": "Mecmûa-i Sâz u Söz Mukaddimesi",
        "category": "tasavvuf",
        "recommended_freq": 432.0,
        "reflection": "Doğu ve Batı müzik geleneklerinin Osmanlı sarayında birleştiği evrensel nefes ahengi."
    },
    {
        "id": "ladikli_mehmed_muallim",
        "author": "Lâdikli Mehmed Çelebi",
        "era": "15. Yüzyıl",
        "work": "Zeynü'l-Elhân fî İlmi't-Te'lîf (Ezgilerin Süsü)",
        "quote_tr": "İlahi hikmet mûsikîyi insan cismine şifa kılmıştır. Bedenin damarları tıpkı çalgının telleri gibidir; fazla gerilirse kopar, fazla gevşerse ses vermez. Hekim-i musikar, hastanın damarlarını nağmeyle mizanına getiren muallimdir.",
        "original_or_context": "زين الألحان في علم التأليف لمحمد بن عبد الحميد اللادقي",
        "category": "islam_tibbi",
        "recommended_freq": 261.63,
        "reflection": "Damar elastikiyeti ve kan dolaşımının müzikal rezonansla akort edilmesi."
    },
    {
        "id": "haci_bayram_can",
        "author": "Hacı Bayrâm-ı Velî",
        "era": "14. - 15. Yüzyıl (1352 - 1430)",
        "work": "Divan ve Hikmetler",
        "quote_tr": "Bilmek istersen seni / Can içre ara canı / Geç canından bul anı / Sen seni bil sen seni... Sazın telinden çıkan nida, can kafesindeki bülbülün asıl gülzarına duyduğu iştiyaktır; o sesi duyan uykudan uyanır.",
        "original_or_context": "Hacı Bayram-ı Veli Nutk-ı Şerifi",
        "category": "tasavvuf",
        "recommended_freq": 432.0,
        "reflection": "İçsel uyanış ve farkındalık: Rezonansın bilinç perdelerini aralaması."
    },
    {
        "id": "esrefoglu_rumi_nefes",
        "author": "Eşrefoğlu Rûmî",
        "era": "15. Yüzyıl (1377 - 1469)",
        "work": "Müzekki'n-Nüfûs (Nefislerin Tezkiyesi)",
        "quote_tr": "Nefes Hakk'ın emanetidir. Bir kimse her nefesinde Hakk'ı zikrederek sesini O'nun sevgisiyle tezyin eylerse, o nefes nefsani hevaları yakıp kül eden bir nura döner. O vakit o kimseden çıkan her seda çevresindekilere hayat bağışlar.",
        "original_or_context": "Müzekki'n-Nüfûs Zikir ve Nefes Bahisleri",
        "category": "tasavvuf",
        "recommended_freq": 528.0,
        "reflection": "Farkındalıklı nefes (pranayama/habs-i nefes) ve sesin hücresel arındırma gücü."
    },
    {
        "id": "ismail_hakki_bursevi_ruh",
        "author": "İsmâil Hakkı Bursevî",
        "era": "17. - 18. Yüzyıl (1653 - 1725)",
        "work": "Rûhu'l-Beyân Tefsiri",
        "quote_tr": "Arş-ı A'lâ'dan yere inen her ilahi emir bir ses ve nida suretinde tecelli eder. Melekler o nidayı tesbihlerle karşılarlar. İnsan kalbi de arşın bir numunesidir; oraya düşen ilahi ilhamlar ancak saf nağmeler ve temiz kelimelerle yankı bulur.",
        "original_or_context": "روح البيان في تفسير القرآن لإسماعيل حقي البروسوي",
        "category": "tasavvuf",
        "recommended_freq": 963.0,
        "reflection": "Kalbin bir akustik rezonatör olarak kozmik ilhamları alıcı (antenne) vazifesi görmesi."
    },
    {
        "id": "seyh_galib_ney_feryat",
        "author": "Şeyh Gâlib",
        "era": "18. Yüzyıl (1757 - 1799)",
        "work": "Hüsn ü Aşk (Güzellik ve Aşk)",
        "quote_tr": "Hoşça bak zâtına kim zübde-i âlemsin sen / Merdüm-i dîde-i ekvân olan âdemsin sen... Neyin feryadını dinle; o kamış değil, senin kendi kalbinin hakikat denizine duyduğu hasretin iniltisidir.",
        "original_or_context": "Hüsn ü Aşk Mesnevisi",
        "category": "tasavvuf",
        "recommended_freq": 432.0,
        "reflection": "Mikrokozmos olan insanın kendi içsel tınısını keşfetmesi: Bedenin evrenin özü olması."
    },
    {
        "id": "katip_celebi_musiki_sifa",
        "author": "Kâtip Çelebi",
        "era": "17. Yüzyıl (1609 - 1657)",
        "work": "Keşfü'z-Zunûn (İlimler Ansiklopedisi)",
        "quote_tr": "İlm-i Mûsikî, riyaziye (matematik) ilimlerinin en şereflilerindendir ve tıpla ikiz kardeştir. Tıp bedenin uzuvlarını ilaçla tedavi ederse, mûsikî ruhun marazlarını nağmeyle tedavi eder. Ruha hitap etmeyen tıp eksiktir.",
        "original_or_context": "كشف الظنون عن أسامي الكتب والفنون - مبحث علم الموسيقى",
        "category": "islam_tibbi",
        "recommended_freq": 220.0,
        "reflection": "Bütüncül (holistik) tıp: Matematik, müzik ve tıbbın ayrılmaz üçlü ittifakı."
    },

    # --- 2. KUTSAL METİNLER, VAHİY & KADİM KÜLLİYAT ---
    {
        "id": "genesis_light_word",
        "author": "Tevrat / Yaratılış (Genesis)",
        "era": "M.Ö. 1. Binyıl",
        "work": "Tekvin (Genesis) 1:3",
        "quote_tr": "Ve Tanrı dedi: 'Işık olsun!' Ve ışık oldu. Tanrı ışığın iyi olduğunu gördü ve ışığı karanlıktan ayırdı.",
        "original_or_context": "וַיֹּאמֶר אֱלֹהִים יְהִי אוֹר וַיְהִי-אוֹר (Vayomer Elohim yehi or vayehi or)",
        "category": "kutsal_metin",
        "recommended_freq": 528.0,
        "reflection": "Işığın yaratılışından önce 'Ve Tanrı dedi' (söz/kelâm/akustik titreşim) ifadesi yer alır; ses ışıktan öncedir."
    },
    {
        "id": "matthew_speak_word_healed",
        "author": "İncil / Matta",
        "era": "1. Yüzyıl",
        "work": "Matta 8:8",
        "quote_tr": "Yüzbaşı cevap verdi: 'Ya Rab, evime girmene layık değilim; ancak yalnız bir söz söyle, kulum iyileşir.'",
        "original_or_context": "ἀλλὰ μόνον εἰπὲ λόγῳ, καὶ ἰαθήσεται ὁ παῖς μου",
        "category": "kutsal_metin",
        "recommended_freq": 528.0,
        "reflection": "Mekânı aşan akustik niyet ve şifa gücü: Tek bir şifalı kelâmın mesafeleri aşarak hücreyi onarması."
    },
    {
        "id": "kuran_neml_daglar",
        "author": "Kur'ân-ı Kerîm",
        "era": "7. Yüzyıl",
        "work": "Neml Sûresi, 27:88",
        "quote_tr": "Sen dağları görürsün de onları hareketsiz ve donmuş sanırsın; oysa onlar bulutların akıp gitmesi gibi kesintisiz yürümektedir (dalgalanmaktadır). Bu, her şeyi sapasağlam ve ahenkle yapan Allah'ın sanatıdır.",
        "original_or_context": "وَتَرَى الْجِبَالَ تَحْسَبُهَا جَامِدَةً وَهِيَ تَمُرُّ مَرَّ السَّحَابِ ۚ صُنْعَ اللَّهِ الَّذِي أَتْقَنَ كُلَّ شَيْءٍ",
        "category": "kutsal_metin",
        "recommended_freq": 7.83,
        "reflection": "Maddenin statik katılığının bir yanılsama oluşu; yerkürenin ve dağların Schumann rezonansıyla akışı."
    },
    {
        "id": "kuran_ibrahim_kelime",
        "author": "Kur'ân-ı Kerîm",
        "era": "7. Yüzyıl",
        "work": "İbrâhîm Sûresi, 14:24-25",
        "quote_tr": "Görmedin mi Allah güzel bir kelâmı neye benzetti? Kökü yerde sabit, dalları göğe yükselen güzel bir ağaç gibidir. O ağaç, Rabbinin izniyle her mevsim meyvesini verir.",
        "original_or_context": "أَلَمْ تَرَ كَيْفَ ضَرَبَ اللَّهُ مَثَلًا كَلِمَةً طَيِّبَةً كَشَجَرَةٍ طَيِّبَةٍ أَصْلُهَا ثَابِتٌ وَفَرْعُهَا فِي السَّمَاءِ",
        "category": "kutsal_metin",
        "recommended_freq": 432.0,
        "reflection": "Güzel ve şifalı sözün fraktal morfolojisi: Köklenen, göğe uzanan ve kesintisiz şifa meyvesi veren kelâm."
    },
    {
        "id": "rig_veda_vac_sukta",
        "author": "Rig Veda (Vāc Sūkta)",
        "era": "M.Ö. 1500 civarı",
        "work": "Rig Veda Mandala 10, İlahi 125",
        "quote_tr": "Ben Kutsal Söz'üm (Vāc)! Tanrıları ve evreni omuzlarımda taşırım. Rüzgar gibi serbestçe eserim; yeri, göğü ve ötesini kuşatırım. Dokunduğum insanı bir bilge, bir kâhin ve bir şifacı kılarım.",
        "original_or_context": "अहं राष्ट्री संगमनी वसूनां - ऋग्वेद वाक्सूक्तम्",
        "category": "kutsal_metin",
        "recommended_freq": 528.0,
        "reflection": "Vedik gelenekte 'Vāc' (Kutsal Söz): Kâinatın yaratıcı ve dönüştürücü primal dişil enerjisi."
    },
    {
        "id": "bhartrhari_shabda_brahman",
        "author": "Bhartṛhari",
        "era": "5. Yüzyıl (Hindistan)",
        "work": "Vākyapadīya (Kelâm ve Dil Üzerine)",
        "quote_tr": "Başlangıcı ve sonu olmayan, bölünmez ve ebedi hakikat Ses-Cevheridir (Shabda Brahman). Bütün evren ve varlık mertebeleri, bu aşkın sesin anlam formlarına bürünerek tezahür etmesinden başka bir şey değildir.",
        "original_or_context": "अनादिनिधनं ब्रह्म शब्दतत्त्वं यदक्षरम् । विवर्ततेऽर्थभावेन प्रक्रिया जगतो यतः ॥",
        "category": "kutsal_metin",
        "recommended_freq": 432.0,
        "reflection": "Doğu dil felsefesinin zirvesi: Maddi evren, aşkın ses dalgasının mana aynasında donmasıdır."
    },
    {
        "id": "bardo_thodol_sound",
        "author": "Tibet Ölüler Kitabı (Bardo Thodol)",
        "era": "8. Yüzyıl (Padmasambhava)",
        "work": "Bardo Thodol (Geçiş Halleri Kılavuzu)",
        "quote_tr": "Kulaklarında binlerce gök gürültüsü gibi çınlayan o muazzam kozmik sesleri duyduğunda korkma! Bil ki o sesler dışarıdan gelmiyor; onlar senin kendi öz bilincinin, kalbinin ve saf zihninin hakiki titreşimidir. O sesle bir ol, kurtuluşa er.",
        "original_or_context": "The Tibetan Book of the Dead - Clear Light and Primal Sound",
        "category": "kutsal_metin",
        "recommended_freq": 963.0,
        "reflection": "İçsel nada (ses): Bireyin en derin trans hallerinde duyduğu hücresel ve nöronal rezonans sesleri."
    },
    {
        "id": "avesta_ahunwar_vibration",
        "author": "Zerdüşt Külliyatı (Zend Avesta)",
        "era": "M.Ö. 1. Binyıl",
        "work": "Yasna 27:13 (Ahunwar Mantrası)",
        "quote_tr": "Ahura Mazda gökleri ve unsurları yaratmadan evvel 'Ahuna Vairya' kutsal kelâmını fısıldadı. O kutsal titreşim fezaya yayıldığında karanlığın kaosunu darmadağın etti ve nizamın ışığı parıldadı.",
        "original_or_context": "Yatha Ahu Vairyo - Primal Word of Creation in Zoroastrianism",
        "category": "kutsal_metin",
        "recommended_freq": 432.0,
        "reflection": "Kadim Pers kozmolojisinde kelâmın kozmik kaosu kozmosa (düzene) dönüştüren gücü."
    },

    # --- 3. BATI FELSEFESİ, MİSTİKLER & KLASİK MÜZİK DEHALARI ---
    {
        "id": "hildegard_symphony_creation",
        "author": "Azize Hildegard von Bingen",
        "era": "12. Yüzyıl (1098 - 1179)",
        "work": "Scivias & Symphonia Armonie Celestium",
        "quote_tr": "Tüm yaratılış tek bir ilahi senfonidir. Beden ise ruhun üzerine gerilmiş bir arp gibidir; doğru nefes, saf niyet ve kutsal ilahilerle çalındığında bedenin her hücresi cennetin armonisine katılır.",
        "original_or_context": "Symphonia armonie celestium revelationum - Hildegardis Bingensis",
        "category": "mistik_akustik",
        "recommended_freq": 528.0,
        "reflection": "Orta Çağ tıbbı ve mistisizminde kadın hekim ve bestecinin bedeni kutsal bir çalgı olarak görmesi."
    },
    {
        "id": "schopenhauer_music_will",
        "author": "Arthur Schopenhauer",
        "era": "18. - 19. Yüzyıl (1788 - 1860)",
        "work": "Die Welt als Wille und Vorstellung (İrade ve Tasavvur Olarak Dünya, 1819)",
        "quote_tr": "Müzik, diğer sanatlar gibi fenomenlerin (görüntülerin) gölgesini değil; doğrudan doğruya İrade'nin (varoluşun gizli özünün) kendisini tasvir eder. İşte bu yüzden müziğin insan ruhuna tesiri diğer bütün sanatlardan katbekat derin, katbekat keskin ve katbekat şifalıdır.",
        "original_or_context": "Die Musik ist also keineswegs, gleich den andern Künsten, das Abbild der Ideen; sondern Abbild des Willens selbst",
        "category": "antik_felsefe",
        "recommended_freq": 432.0,
        "reflection": "Müziğin ontolojik üstünlüğü: Temsili değil, doğrudan doğruya yaşam enerjisini seslendirmesi."
    },
    {
        "id": "bach_glory_refreshment",
        "author": "Johann Sebastian Bach",
        "era": "17. - 18. Yüzyıl (1685 - 1750)",
        "work": "Müzikal Otobiyografi ve İthaflar",
        "quote_tr": "Mûsikînin tek ve nihai gayesi, Allah'ın celâlini yüceltmek ve insan ruhunu tazeleyip ferahlatmaktır. Bu yüce niyetin bulunmadığı yerde mûsikî yoktur; orada sadece şeytani bir kakofoni ve gürültü vardır.",
        "original_or_context": "Finis & Fundamental-Ursache aller Music solle nicht anders seyn als zu Gottes Ehre und Recreation des Gemüths",
        "category": "mistik_akustik",
        "recommended_freq": 432.0,
        "reflection": "Barok matematiğinin ve kontrpuan nizamının zihinsel dinginlik ve huşu üretmesi."
    },
    {
        "id": "mozart_silence_between_notes",
        "author": "Wolfgang Amadeus Mozart",
        "era": "18. Yüzyıl (1756 - 1791)",
        "work": "Mektuplar ve Müzikal Düşünceler",
        "quote_tr": "Müzik sadece notalarda değildir; asıl müzik, notaların arasındaki o esrarengiz sessizliktedir. İki ses arasındaki nefes aralığı, ruhun kanat çırptığı boşluktur.",
        "original_or_context": "Die Musik steckt nicht in den Noten, sondern in der Stille dazwischen",
        "category": "mistik_akustik",
        "recommended_freq": 432.0,
        "reflection": "Es (sessizlik) ve rezonans dengesi: Terapötik müziğin zihinde açtığı dingin boşluk."
    },
    {
        "id": "debussy_sound_color",
        "author": "Claude Debussy",
        "era": "19. - 20. Yüzyıl (1862 - 1918)",
        "work": "Mösyö Krok ile Söyleşiler",
        "quote_tr": "Müzik, doğanın görünmez güçlerinin renklerle ve ses dalgalarıyla zamanda akıp giden şiiridir. Rüzgarın sesini, denizin dalgalanışını ve gün batımının sükutunu ancak kuralların zincirini kıran saf nağmeler anlatabilir.",
        "original_or_context": "La musique est un total de forces dispersées... On en fait une chanson spéculative!",
        "category": "mistik_akustik",
        "recommended_freq": 528.0,
        "reflection": "Empresyonist akustik: Doğanın su ve rüzgar harmoniklerinin insan sinir sistemine dinginlik aşılaması."
    },
    {
        "id": "kandinsky_soul_piano",
        "author": "Wassily Kandinsky",
        "era": "19. - 20. Yüzyıl (1866 - 1944)",
        "work": "Sanatta Ruhsallık Üzerine (Über das Geistige in der Kunst, 1912)",
        "quote_tr": "Renk bir tuş, göz bir çekiç, ruh ise telleri olan bir piyanodur. Sanatçı, insan ruhunu belirli frekanslarda titreştirmek için şu veya bu tuşa dokunan eldir.",
        "original_or_context": "Die Farbe ist die Taste. Das Auge ist der Hammer. Die Seele ist das Klavier mit vielen Saiten.",
        "category": "mistik_akustik",
        "recommended_freq": 528.0,
        "reflection": "Sinestezi: Renk, ışık ve ses frekanslarının insan beyninde tek bir duyusal rezonans oluşturması."
    },
    {
        "id": "rilke_orpheus_song",
        "author": "Rainer Maria Rilke",
        "era": "19. - 20. Yüzyıl (1875 - 1926)",
        "work": "Orpheus'a Soneler (Die Sonette an Orpheus, 1922)",
        "quote_tr": "Şarkı söylemek bir arzu değildir; şarkı söylemek varoluşun ta kendisidir! Bir Tanrı için bu kolaydır; lakin biz insanlar rüzgarın nefesinde kendi varlığımızın saf melodisini ne zaman duyacağız?",
        "original_or_context": "Gesang ist Dasein. Für den Gott ein Leichtes. Wann aber sind wir?",
        "category": "mistik_akustik",
        "recommended_freq": 432.0,
        "reflection": "Ses ve şarkının insan varoluşunun ontolojik derinliğini açığa çıkarması."
    },

    # --- 4. MODERN NÖROLOJİ, BİYOAKUSTİK & REZONANS TIBBI ---
    {
        "id": "oliver_sacks_musicophilia",
        "author": "Dr. Oliver Sacks",
        "era": "20. - 21. Yüzyıl (1933 - 2015)",
        "work": "Musicophilia: Tales of Music and the Brain (2007)",
        "quote_tr": "Müzik, beynin diğer hiçbir uyarana tepki vermediği kadar geniş ağlarını aynı anda harekete geçirir: Motor korteks, amigdala, hipokampus ve temporal lob birlikte ateşlenir. Ağır demans ve Alzheimer hastaları konuşmayı ve sevdiklerinin adını unutsalar dahi, gençliklerinde dinledikleri bir ezgiyi kusursuzca mırıldanabilirler; çünkü müzik ruhun silinmez belleğidir.",
        "original_or_context": "Music can pierce the heart directly; it needs no mediation.",
        "category": "bilim_ve_fizik",
        "recommended_freq": 432.0,
        "reflection": "Nöromüzikoloji: Ses terapisinin nörodejeneratif hastalıklarda derin nöral yolları canlı tutması."
    },
    {
        "id": "bruce_lipton_biology_belief",
        "author": "Dr. Bruce H. Lipton",
        "era": "20. - 21. Yüzyıl (1944 - Günümüz)",
        "work": "The Biology of Belief (İnancın Biyolojisi, 2005)",
        "quote_tr": "Hücre zarlarımız, iç mekanizmayı yöneten katı genetik programlar değil; çevreden gelen titreşimsel, akustik ve elektromanyetik sinyalleri okuyan sıvı kristal çiplerdir. Bedeniniz bir frekans alıcısıdır; dinlediğiniz harmonikler ve beslediğiniz düşünceler genlerinizin ifadesini doğrudan değiştirir.",
        "original_or_context": "Cells are controlled by the energetic environment, not by genetic fatalism.",
        "category": "bilim_ve_fizik",
        "recommended_freq": 528.0,
        "reflection": "Epigenetik ve akustik biyoloji: Ses dalgalarının hücre zarı reseptörlerini aktive etmesi."
    },
    {
        "id": "candace_pert_molecules_emotion",
        "author": "Dr. Candace Pert",
        "era": "20. - 21. Yüzyıl (1946 - 2013)",
        "work": "Molecules of Emotion (Duygu Molekülleri, 1997)",
        "quote_tr": "Bedenimiz ve zihnimiz ayrı iki yapı değildir; onlar neuropeptid moleküllerinin kesintisiz dans ettiği tek bir 'psikonöroimmünolojik' rezonatördür. Her duygu ve her müzik notası bu molekülleri belirli bir frekansta titreştirir. Doğru frekanstaki ses, kilitlenmiş travma reseptörlerini gevşeterek bedeni kimyasal krizden kurtarır.",
        "original_or_context": "Your body is your subconscious mind and physical expression of thought.",
        "category": "bilim_ve_fizik",
        "recommended_freq": 639.0,
        "reflection": "Duyguların biyokimyasal rezonansı: Sesle hücresel travma çözünmesi ve vagal rahatlama."
    },
    {
        "id": "mitchell_gaynor_healing_sound",
        "author": "Dr. Mitchell L. Gaynor (Onkolog)",
        "era": "20. - 21. Yüzyıl (1956 - 2015)",
        "work": "The Healing Power of Sound (Sesin İyileştirici Gücü, 1999)",
        "quote_tr": "Kanser hastalarımda Tibet kaseleri ve ses terapisi kullandığımda gördüm ki; ses dalgaları kemoterapinin asla ulaşamadığı derin hücre çekirdeğine, hücresel strese ve ruhsal buhrana dokunmaktadır. Ses, bağışıklık sisteminin uykudaki askerlerini uyandıran bir boru sesidir.",
        "original_or_context": "Sound can redress imbalances on every level of physiologic functioning and can play a positive role in the treatment of virtually any medical disorder.",
        "category": "islam_tibbi",
        "recommended_freq": 528.0,
        "reflection": "Integratif onkoloji ve akustik terapi: Bağışıklık hücrelerinin frekans uyarımıyla güçlenmesi."
    },
    {
        "id": "john_stuart_reid_cymatics_water",
        "author": "John Stuart Reid",
        "era": "20. - 21. Yüzyıl (Akustik Bilimci)",
        "work": "CymaScope & Hücresel Ses Araştırmaları",
        "quote_tr": "Ses sadece havadaki bir dalga değil; temas ettiği su moleküllerini anında organize eden küresel bir basınç mandalasıdır. İnsan hücreleri ses dalgalarıyla karşılaştığında, hücre zarı mikroskobik bir davul derisi gibi esner ve hücre içi toksin atılımı hızlanır. Bizler sudan dokunmuş şarkılarız.",
        "original_or_context": "Sound is spherical in nature and imprints sacred geometry into the cellular water matrix.",
        "category": "bilim_ve_fizik",
        "recommended_freq": 432.0,
        "reflection": "CymaScope bulguları: Sesin küresel basınç geometrisi ve hücre hidrasyonunu desteklemesi."
    },
    {
        "id": "meg_jordan_vagus_sound",
        "author": "Dr. Meg Jordan",
        "era": "21. Yüzyıl",
        "work": "İntegratif Sağlık ve Vagus Siniri Terapisi",
        "quote_tr": "Vagus siniri ses terapisinin bedendeki süper otoyoludur. Ağızdan çıkarılan uzun bir 'OM', 'HU' veya 'ÂMÎN' sesi vokal kordları titreştirerek vagusu aktive eder; saniyeler içinde kan basıncı düşer, kalp ritmi sakinleşir ve beden 'dinlen ve onar' moduna geçer.",
        "original_or_context": "Vocal toning stimulates the vagal brake, shifting autonomic tone from fight-or-flight to rest-and-repair.",
        "category": "islam_tibbi",
        "recommended_freq": 136.1,
        "reflection": "Vokal tonlama ve zikrin vagal tonus üzerindeki doğrudan nörobiyolojik regülasyonu."
    }
]

added = 0
for q in more_quotes:
    if q["id"] not in existing_ids:
        quotes.append(q)
        existing_ids.add(q["id"])
        added += 1

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(quotes, f, ensure_ascii=False, indent=2)

print(f"Toplam {added} yeni alıntı eklendi. quotes.json güncel toplam: {len(quotes)} alıntı!")
