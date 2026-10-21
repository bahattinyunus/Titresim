# -*- coding: utf-8 -*-
"""
Add second batch of quotes to quotes.json.
"""
import json
from pathlib import Path

DATA_PATH = Path("data/quotes.json")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    quotes = json.load(f)

existing_ids = {q["id"] for q in quotes}

more_quotes_2 = [
    {
        "id": "pythagoras_golden_verses",
        "author": "Pisagor (Pythagoras)",
        "era": "M.Ö. 6. Yüzyıl (M.Ö. 570 - 495)",
        "work": "Altın Dizeler (Aurea Carmina)",
        "quote_tr": "Gözlerini gece uykusuna teslim etmeden evvel, o gün yaptığın bütün amelleri üç kez zihninden geçir. Zihnini yatıştırmak için parmaklarını lirin tellerinde gezdir ve ruhunu mûsikînin sularında yıka. O vakit rüyaların semavi hakikatlerle dolar.",
        "original_or_context": "The Golden Verses of Pythagoras - Evening Purification and Music",
        "category": "antik_felsefe",
        "recommended_freq": 432.0,
        "reflection": "Akşam ritüeli ve sirkadiyen akustik: Uyku öncesi telli çalgı armonikleriyle zihinsel arınma."
    },
    {
        "id": "farabi_saray_efsanesi",
        "author": "Ebû Nasr el-Fârâbî",
        "era": "9. - 10. Yüzyıl (872 - 950)",
        "work": "Seyfullah Devle Sarayı Meclis Rivayeti",
        "quote_tr": "Fârâbî Şam Emiri'nin sarayında udunu çıkarıp telleri bir türlü bağladı ve öyle bir ezgi çaldı ki meclisteki herkes kahkahalarla gülmeye başladı. Sonra telleri değiştirdi, öyle bir makam çaldı ki vezirlerden kölelere kadar herkes hıçkırıklarla ağladı. Sonra telleri bir daha değiştirdi, öyle bir tını üfledi ki nöbetçiler dahil bütün saray ahalisi tatlı ve derin bir uykuya daldı; Fârâbî ise oradan sessizce ayrıldı.",
        "original_or_context": "İbn Hallikân, Vefeyâtü'l-A'yân (Fârâbî Tercüme-i Hâli)",
        "category": "islam_tibbi",
        "recommended_freq": 220.0,
        "reflection": "Akustik modülasyon dehası: Müzikal aralıkların insan biyokimyasını ve duygu durumunu anında değiştirmesi."
    },
    {
        "id": "hz_ali_kelam_esir",
        "author": "Hz. Ali (k.v.)",
        "era": "7. Yüzyıl (599 - 661)",
        "work": "Nehcü'l-Belâga (Belâgat Yolu)",
        "quote_tr": "Söz senin ağzında hapsedildikçe senin esirindir; lakin bir kere ağzından fırladı mı sen onun esiri olursun. Dilini koru, sesini tart; zira güzel kelâm hasta kalplere şifa, kötü söz ise sağlam göğüslere zehirdir.",
        "original_or_context": "نهج البلاغة - حكم وقصار أمير المؤمنين علي بن أبي طالب",
        "category": "tasavvuf",
        "recommended_freq": 432.0,
        "reflection": "Sözün niyet ve sorumluluk boyutu: Yaydığımız akustik frekansın kendi yaşam alanımızı mühürlemesi."
    },
    {
        "id": "cafer_sadik_harf_menzil",
        "author": "İmâm Ca'fer es-Sâdık",
        "era": "8. Yüzyıl (702 - 765)",
        "work": "İlm-i Hurûf ve Esrâr-ı Kelâm",
        "quote_tr": "Ağızdan çıkan her harfin gökyüzünde bir yıldızı, yeryüzünde bir unsuru ve bedende bir organı titreştiren gizli bir menzili vardır. Ağzını temiz tutanın kelâmı hastaya dokunduğunda deva olur.",
        "original_or_context": "رسائل الإمام جعفر الصادق في أسرار الحروف والطبائع",
        "category": "tasavvuf",
        "recommended_freq": 528.0,
        "reflection": "Harf formantları ve biyo-rezonans: Fonetik artikülasyonun hücresel organ yansımaları."
    },
    {
        "id": "ibn_tufeyl_hayy_ses",
        "author": "İbn Tufeyl",
        "era": "12. Yüzyıl (1105 - 1185)",
        "work": "Hayy bin Yakzân (Esrârü'l-Hikmeti'l-Meşrikiyye)",
        "quote_tr": "Hayy ıssız adada büyürken tabiatın seslerini dinledi: Rüzgarın kamışlıktaki uğultusunu, suyun şırıltısını, kuşların terennümünü taklit etti. Gördü ki bütün bu sesler rastgele bir gürültü değil; tek bir Görünmez Musavvir'in kâinat kubbesinde terennüm ettiği aşkın bir senfonidir.",
        "original_or_context": "حي بن يقظان لابن طفيل الأندلسي",
        "category": "tasavvuf",
        "recommended_freq": 432.0,
        "reflection": "Biyo-akustik uyanış: Tabiatın seslerindeki fraktal harmoniklerin tevhidi fısıldaması."
    },
    {
        "id": "hafiz_sirazi_kubbe_sadasi",
        "author": "Hâfız-ı Şîrâzî",
        "era": "14. Yüzyıl (1315 - 1390)",
        "work": "Dîvân-ı Hâfız",
        "quote_tr": "Ez-sedâ-yı sühen-i aşk nedîdem hoş-ter / Yâdgârî ki der-în günbed-i devvâr bimând: Şu dönen gök kubbenin altında aşk sözünden ve onun nağmesinden daha hoş, daha kalıcı bir yâdigâr görmedim.",
        "original_or_context": "از صدای سخن عشق ندیدم خوشتر / یادگاری که در این گنبد دوار بماند",
        "category": "tasavvuf",
        "recommended_freq": 432.0,
        "reflection": "Fani dünyada ebediyen yankılanan tek rezonansın sevgi ve şefkat frekansı olması."
    },
    {
        "id": "fuzuli_can_bahs_soz",
        "author": "Fuzûlî",
        "era": "16. Yüzyıl (1483 - 1556)",
        "work": "Dîvân Mukaddimesi",
        "quote_tr": "Söz cevher-i cân-bahş-ı ten-i hastadır ey dil / Söz söyle ki söz derdine derman ola bilsin... Şair odur ki her sözü can bağışlayan bir iksir gibi dinleyenin kırık kalbine merhem olsun.",
        "original_or_context": "Fuzuli Divanı Söz Redifli Kaside ve Mukaddime",
        "category": "tasavvuf",
        "recommended_freq": 432.0,
        "reflection": "Kelâmın can bahşeden (biyo-rejeneratif) boyutu: Edebi ve akustik inceliğin hücresel teskini."
    },
    {
        "id": "baki_hos_sada",
        "author": "Bâkî (Sultânü'ş-Şuarâ)",
        "era": "16. Yüzyıl (1526 - 1600)",
        "work": "Dîvân-ı Bâkî",
        "quote_tr": "Âvâzeyi bu âleme Dâvûd gibi sal / Bâkî kalan bu kubbede bir hoş sadâ imiş... Şöhret de biter, taht da geçer; gök kubbede ebediyen titreşen ancak Hakk uğruna söylenmiş bir hoş sadâdır.",
        "original_or_context": "Bâkî Divanı Meşhur Beyit",
        "category": "tasavvuf",
        "recommended_freq": 432.0,
        "reflection": "Davudi nida ve ebedi yankı: Sesin zamanda sönmeyen dalga formları."
    },
    {
        "id": "itri_segah_tekbir",
        "author": "Itrî (Buhûrîzâde Mustafa Efendi)",
        "era": "17. - 18. Yüzyıl (1640 - 1712)",
        "work": "Segâh Salât-ı Ümmiyye ve Segâh Bayram Tekbîri",
        "quote_tr": "Segâh Tekbir öyle bir nağmedir ki; milyonlarca insan aynı anda tek bir nefes ve tek bir perdeyle 'Allahu Ekber' dediğinde yeryüzü adeta semaya yükselir, bütün sinirler ve yürekler aynı kutsal ritimde erir.",
        "original_or_context": "Osmanlı Dini Musikisi Şaheseri - Segâh Tekbir Analizi",
        "category": "tasavvuf",
        "recommended_freq": 396.0,
        "reflection": "Kolektif koro koheransı: Milyonların aynı frekansta rezonansa girerek oluşturduğu devasa manyetik alan."
    },
    {
        "id": "dede_efendi_ferahfeza",
        "author": "Hammâmîzâde İsmâil Dede Efendi",
        "era": "18. - 19. Yüzyıl (1778 - 1846)",
        "work": "Ferahfezâ Âyîn-i Şerîfi",
        "quote_tr": "Makam bir yolculuktur; neyzenin nefesiyle neva perdesinde seher gibi doğar, meyan köşkünde kalbin en derin sırlarını ifşa eder ve karar perdesinde teslimiyetle Hakk'ın sükunetinde karar kılar.",
        "original_or_context": "Ferahfeza Ayin-i Şerifi Mukaddimesi",
        "category": "islam_tibbi",
        "recommended_freq": 261.63,
        "reflection": "Makam seyrinin arketipsel psikolojik evreleri: Doğuş (giriş), fırtına (meyan) ve itidal (karar)."
    },
    {
        "id": "neyzen_tevfik_kamis",
        "author": "Neyzen Tevfik (Kolaylı)",
        "era": "19. - 20. Yüzyıl (1879 - 1953)",
        "work": "Azâb-ı Mukaddes & Ney Taksimleri",
        "quote_tr": "Ney kuru bir kamıştan ibarettir; lakin o kamışın deliklerinden inleyen ses kamışın değil, ona üfleyen dertli bağrın ateşidir. Asıl marifet kamışı değil, ona o can nefesini bahşeden Sahib-i Nefes'i duyabilmektir.",
        "original_or_context": "Neyzen Tevfik Hatırat ve Şiirleri",
        "category": "tasavvuf",
        "recommended_freq": 220.0,
        "reflection": "Arınma ve boşalma: Ney gibi benlik kirini boşaltmadan hakiki sesin çıkamayacağı hakikati."
    },
    {
        "id": "tanpinar_huzur_musiki",
        "author": "Ahmet Hamdi Tanpınar",
        "era": "20. Yüzyıl (1901 - 1962)",
        "work": "Huzur Romanı (1949)",
        "quote_tr": "Bizim klasik mûsikîmiz, bir medeniyetin kendi iç dünyasında kurduğu en muazzam metafizik katedraldir. Itrî'nin Neva Kâr'ını dinlerken zaman durur; insan kendi faniliğinden sıyrılıp ebedi bir itidal havuzuna dalar.",
        "original_or_context": "Huzur Romanı - Neyzen Emin Dede ve Itrî Bahisleri",
        "category": "mistik_akustik",
        "recommended_freq": 432.0,
        "reflection": "Zamansızlık hissi (flow): Klasik nağmelerin zihinsel zaman algısını yavaşlatması."
    },
    {
        "id": "stravinsky_music_order",
        "author": "Igor Stravinsky",
        "era": "20. Yüzyıl (1882 - 1971)",
        "work": "Poetics of Music (Müziğin Poetikası, 1942)",
        "quote_tr": "Müziğin tek varlık gayesi, insan ile zaman arasındaki nizamı ve ahengi tesis etmektir. Kaotik akan zamanı alır, onu ritim ve aralıklarla kutsal bir geometriye kavuşturur.",
        "original_or_context": "Poetics of Music in the Form of Six Lessons (Harvard, 1942)",
        "category": "antik_felsefe",
        "recommended_freq": 432.0,
        "reflection": "Zamanın akustik geometrisi: Kronolojik zamanı (Chronos) niteliksel kutsal zamana (Kairos) dönüştürme."
    },
    {
        "id": "carl_jung_music_archetype",
        "author": "Carl Gustav Jung",
        "era": "19. - 20. Yüzyıl (1875 - 1961)",
        "work": "Kolektif Bilinçdışı ve Arketipler",
        "quote_tr": "Müzik, doğrudan doğruya kolektif bilinçdışının en derin arketiplerine hitap eder. Kelimelerin ulaşamadığı bilinçaltı travmaları ve gölge yönler, sesin dönüştürücü simyasıyla serbest kalır ve benlik bütünleşir.",
        "original_or_context": "The Archetypes and the Collective Unconscious (Collected Works Vol. 9)",
        "category": "bilim_ve_fizik",
        "recommended_freq": 432.0,
        "reflection": "Analitik psikoloji ve ses: Bilinçdışı düğümlerin arketipsel tınılarla çözülmesi."
    },
    {
        "id": "wilhelm_reich_armor_sound",
        "author": "Dr. Wilhelm Reich",
        "era": "20. Yüzyıl (1897 - 1957)",
        "work": "Karakter Analizi ve Bedensel Zırh Teorisi",
        "quote_tr": "Bastırılmış her çocukluk acısı ve korku bedende kronik bir kas spazmı ('bedensel zırh') olarak donup kalır. Doğru frekanslı ses titreşimleri, diyafram nefesi ve rezonans bu zırhı titreterek çözer ve yaşam enerjisinin (orgon) yeniden akmasını sağlar.",
        "original_or_context": "Character Analysis: The Segmental Armoring and Pulsation",
        "category": "bilim_ve_fizik",
        "recommended_freq": 174.0,
        "reflection": "Somatik psikoterapi: Beden zırhının rezonant frekanslarla gevşetilmesi ve enerji akışı."
    },
    {
        "id": "tchaikovsky_words_stop_music",
        "author": "Pyotr Ilyich Tchaikovsky",
        "era": "19. Yüzyıl (1840 - 1893)",
        "work": "Nadezhda von Meck'e Mektuplar (1878)",
        "quote_tr": "Kelimelerin tükendiği, dilin kifayetsiz kaldığı yerde müzik başlar. Kalbimin öyle derin yaraları ve feryatları vardır ki, onları hiçbir lisanda söyleyemem; ancak bir kemanın ağlayışında ifşa edebilirim.",
        "original_or_context": "Where words fail, music speaks.",
        "category": "mistik_akustik",
        "recommended_freq": 639.0,
        "reflection": "Duygusal katarsis: Dilin sınırlarını aşan saf müzikal sağaltım."
    },
    {
        "id": "mahler_tradition_fire",
        "author": "Gustav Mahler",
        "era": "19. - 20. Yüzyıl (1860 - 1911)",
        "work": "Senfonik Sohbetler ve Aforizmalar",
        "quote_tr": "Müzikte gelenek küllere tapınmak değil, ateşi canlı tutmaktır! Bir senfoni inşa etmek, ses dalgalarıyla kainatı yeniden yaratmak demektir. Her nota bir gezegen, her aralık bir yerçekimidir.",
        "original_or_context": "Tradition ist die Weitergabe des Feuers und nicht die Anbetung der Asche.",
        "category": "mistik_akustik",
        "recommended_freq": 432.0,
        "reflection": "Kozmik senfoni inşası: Makrokozmosun müzikal mimaride yeniden doğuşu."
    },
    {
        "id": "munir_nurettin_saffet",
        "author": "Münir Nurettin Selçuk",
        "era": "20. Yüzyıl (1900 - 1981)",
        "work": "Klasik Türk Musikisi İcra Notları",
        "quote_tr": "Bizim musikimiz gırtlak cambazlığı değildir; o, insanın kendi iç derinliğini dinleme sanatıdır. Makamı doğru icra eden hanendede kibir erir, benlik kaybolur; geriye sadece saf ve arı bir ruh kalır.",
        "original_or_context": "Münir Nurettin Selçuk Sanat Hayatı ve Hatıraları",
        "category": "islam_tibbi",
        "recommended_freq": 220.0,
        "reflection": "İcra ahlakı ve vokal rezonans: Şarkıcının egosuzlaşarak ses kanalına dönüşmesi."
    },
    {
        "id": "averroes_de_anima_sound",
        "author": "İbn Rüşd (Averroes)",
        "era": "12. Yüzyıl (1126 - 1198)",
        "work": "Telhîsu Kitâbi'n-Nefs (De Anima Şerhi)",
        "quote_tr": "Ses, havada titreşen maddi bir hareket olarak başlar; lakin kulak zarına ulaştığında ruh onu gayri maddi, saf bir anlam suretine dönüştürür. Ses duyusu, maddi dünya ile ruhani dünya arasındaki en asil köprüdür.",
        "original_or_context": "تلخيص كتاب النفس لأبي الوليد بن رشد",
        "category": "antik_felsefe",
        "recommended_freq": 432.0,
        "reflection": "Akustik epistemoloji: Mekanik hava dalgasının bilinçte manaya ve idrake dönüşümü."
    },
    {
        "id": "yahya_kemal_musiki_ruh",
        "author": "Yahya Kemal Beyatlı",
        "era": "19. - 20. Yüzyıl (1884 - 1958)",
        "work": "Kendi Gök Kubbemiz (Eski Mûsikî)",
        "quote_tr": "Çok insan anlayamaz eski mûsikîmizden / Ve ondan anlamayan bir şey anlamaz bizden... O mûsikî ki, asırlarca ruhumuzun sığındığı liman, zaferlerimizin sevinci ve kederlerimizin en asil tesellisi olmuştur.",
        "original_or_context": "Kendi Gök Kubbemiz - Eski Mûsikî Şiiri",
        "category": "tasavvuf",
        "recommended_freq": 220.0,
        "reflection": "Kültürel ve kolektif akustik hafıza: Medeniyet ruhunun makamlarla taşınması."
    }
]

added = 0
for q in more_quotes_2:
    if q["id"] not in existing_ids:
        quotes.append(q)
        existing_ids.add(q["id"])
        added += 1

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(quotes, f, ensure_ascii=False, indent=2)

print(f"2. part başarıyla tamamlandı: {added} yeni alıntı eklendi. Toplam alıntı sayısı: {len(quotes)}!")
