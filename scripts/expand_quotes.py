# -*- coding: utf-8 -*-
"""
Generate and update data/quotes.json with an expansive collection of wisdom quotes.
"""
import json
from pathlib import Path

DATA_PATH = Path("data/quotes.json")

# Mevcut quotes oku
existing_quotes = []
if DATA_PATH.exists():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        existing_quotes = json.load(f)

existing_ids = {q["id"] for q in existing_quotes}

new_quotes = [
    {
        "id": "ibn_arabi_kun",
        "author": "Muhyiddîn İbnü'l-Arabî",
        "era": "12. - 13. Yüzyıl (1165 - 1240)",
        "work": "Fütûhât-ı Mekkiyye (Mekke Fetihleri)",
        "quote_tr": "Kâinattaki bütün mevcudat, Hakk'ın 'Kün!' (Ol!) kelâmının harflerinden ve ilahi Nefes-i Rahmânî'nin fezadaki yayılımından ibarettir. Her varlık, ilahi nefesin belirli bir mertebede düğümlenmesiyle beliren bir ses harfidir.",
        "original_or_context": "فالعالم كله كلمات الله التي لا تنفد، والنفس الرحماني هو أصل الهيولى",
        "category": "tasavvuf",
        "recommended_freq": 432.0,
        "reflection": "Varlık statik bir madde yığını değil, ilahi nefesin sürekli üflendiği akışkan bir kelamlar okyanusudur."
    },
    {
        "id": "ibn_arabi_fusus_nefes",
        "author": "Muhyiddîn İbnü'l-Arabî",
        "era": "12. - 13. Yüzyıl (1165 - 1240)",
        "work": "Füsûsü'l-Hikem (Hikmetlerin Özleri)",
        "quote_tr": "Nefes nasıl boğazdan, damaktan ve dudaklardan geçerken farklı seslere ve harflere bürünürse; Rahman'ın nefesi de ilahi isimlerin aynalarında tecelli ederek yıldızları, unsurları ve bedenleri var eder.",
        "original_or_context": "النفس الإلهي هو الذي به ظهرت أعيان الحروف",
        "category": "tasavvuf",
        "recommended_freq": 528.0,
        "reflection": "Harflerin mahreçleri gibi her mahluk ilahi nefesin çıktığı bir kozmik menfezdir."
    },
    {
        "id": "ihvan_safa_musiki",
        "author": "İhvân-ı Safâ",
        "era": "10. Yüzyıl (Bağdat & Basra)",
        "work": "Resâ'il İhvân es-Safâ (5. Mûsikî Risalesi)",
        "quote_tr": "Bil ki ey kardeş; mûsikî aletlerinin tellerinden çıkan nağmeler, gök kürelerinin dönüşündeki nispetlere uygundur. Mûsikî, nefsi cismani alakanın ağırlığından sıyırarak feleki aleme ve ruhani saffete yükseltir; bedendeki dört hıltın fazlalıklarını törpüleyip itidale erdirir.",
        "original_or_context": "الرسالة الخامسة في الموسيقى - رسائل إخوان الصفا",
        "category": "islam_tibbi",
        "recommended_freq": 220.0,
        "reflection": "Klasik Doğu felsefesinde müzik yalnızca estetik bir zevk değil, ruhun feleki menşeine dönüş vasıtasıdır."
    },
    {
        "id": "gazali_sema_adabi",
        "author": "İmâm Gazâlî",
        "era": "11. - 12. Yüzyıl (1058 - 1111)",
        "work": "İhyâü Ulûmi'd-Dîn (Kitâbu Âdâbi's-Semâ')",
        "quote_tr": "Mûsikî ve güzel ses, çakmak taşının demire vurulduğunda kıvılcım saçması gibi kalbin derinliklerindeki gizli cevherleri uyandırır. Kalbinde Hakk sevgisi olanın aşkını taştırır, kalbinde vesvese olanın da vesvesesini depreştirir. Ses, kalpte saklı olan tohumun yağmurudur.",
        "original_or_context": "السماع لا يثبت في القلب ما ليس فيه، وإنما يحرك ما هو فيه",
        "category": "tasavvuf",
        "recommended_freq": 432.0,
        "reflection": "Akustik rezonans tarafsız bir kuvvettir; bireyin içsel frekansını açığa çıkarır ve büyütür."
    },
    {
        "id": "razi_tibbi_ruhani",
        "author": "Ebû Bekir er-Râzî (Rhazes)",
        "era": "9. - 10. Yüzyıl (865 - 925)",
        "work": "Et-Tıbbü'r-Rûhânî (Ruh Sağlığı Tıbbı)",
        "quote_tr": "Gam, keder ve melankoliye duçar olan kimselere hoş kokulu bitkiler koklatılmalı, latif manzaralar seyrettirilmeli ve kulağına yumuşak nağmelerle çalınan tambur ve ud ezgileri dinletilmelidir. Bedenin mizacı düzelmeden evvel ruhun mizacı ses ile taranmalıdır.",
        "original_or_context": "كتاب الطب الروحاني في علاج أمراض النفس",
        "category": "islam_tibbi",
        "recommended_freq": 261.63,
        "reflection": "Psikosomatik tıp prensibi: Ruhun sesle dengelenmesi, somatik iyileşmenin ön şartıdır."
    },
    {
        "id": "suuri_hasan_vakit",
        "author": "Şuûrî Hasan Efendi",
        "era": "17. Yüzyıl",
        "work": "Ta'dîlü'l-Emzice (Mizaçların Düzenlenmesi)",
        "quote_tr": "Günün yirmi dört saati feleğin burçlarıyla taksim edilmiştir. Seherde Rast, kuşlukta Buselik, öğlede Hicaz ve Nihavend, ikindide Uşşak, gün batarken Hüseyni ve yatsıda Zirgüle dinletildiğinde; kan, safra, balgam ve sevda mizaçları taşkınlık yapmaz, hasta sıhhate erer.",
        "original_or_context": "تعديل الأمزجة في علم الطب والموسيقى",
        "category": "islam_tibbi",
        "recommended_freq": 392.0,
        "reflection": "Sirkadiyen biyolojik ritim ile makamların günün vakitleri arasındaki derin biyo-rezonans uyumu."
    },
    {
        "id": "gevrekzade_cocuk_ses",
        "author": "Gevrekzâde Hasan Efendi",
        "era": "18. Yüzyıl (1727 - 1801)",
        "work": "Emrâz-ı Atfâl (Çocuk Hastalıkları Risalesi)",
        "quote_tr": "Beşikte ağlayan, havale ve humma geçiren masum sabi çocukların başucunda yumuşak sesle ninniler söylenmeli ve Rehavi makamı çalınmalıdır. Rehavi sabinin dimağını soğutur, başındaki harareti teskin eder ve onu derin bir uykuya sevk eder.",
        "original_or_context": "رسالة في علاج أمراض الأطفال بالنغمات الموسيقية",
        "category": "islam_tibbi",
        "recommended_freq": 174.0,
        "reflection": "Çocuk ve bebeklerin sinir sistemi gelişirken akustik şefkat ve makam melodilerinin koruyucu etkisi."
    },
    {
        "id": "evliya_edirne_fasli",
        "author": "Evliyâ Çelebi",
        "era": "17. Yüzyıl (1611 - 1682)",
        "work": "Seyahatnâme (3. Cilt - Edirne Darüşşifası)",
        "quote_tr": "Darüşşifanın ortasındaki kubbe altında fıskiyeli büyük bir havuz vardır. Haftada üç gün usta hanende ve sazendeler gelip deli ve kederli hastalara fasıl eyler. Su şırıltısı ile ney sadası birbirine karıştığında nicelerin deliliği zail olur, hastaların yüzüne can gelir.",
        "original_or_context": "Evliya Çelebi Seyahatnamesi Edirne Sultan Bayezid Bimarhanesi Bahsi",
        "category": "islam_tibbi",
        "recommended_freq": 200.0,
        "reflection": "Doğal su akustiği (pembe gürültü) ile enstrümantal melodinin birleştiği akustik şifa mimarisi."
    },
    {
        "id": "farabi_uc_tesir",
        "author": "Ebû Nasr el-Fârâbî",
        "era": "9. - 10. Yüzyıl (872 - 950)",
        "work": "Kitâbü'l-Mûsîka'l-Kebîr (Büyük Musiki Kitabı)",
        "quote_tr": "Mûsikî nağmeleri üç nev'idir: Birincisi insana ferahlık, neşe ve dinçlik bağışlayan lezzet verici seslerdir. İkincisi zihne ve hayal gücüne suretler nakşeden ilham verici seslerdir. Üçüncüsü ise kalpteki gizli tutkuları coşturan veya dinlendiren ruhani seslerdir ki bu doğrudan tıbba dahildir.",
        "original_or_context": "كتاب الموسيقى الكبير لأبي نصر الفارابي",
        "category": "islam_tibbi",
        "recommended_freq": 432.0,
        "reflection": "Müziğin nörolojik sınıflandırması: hedonik, bilişsel ve terapötik-duygusal etki alanları."
    },
    {
        "id": "mevlana_divan_ezel",
        "author": "Mevlânâ Celâleddîn-i Rûmî",
        "era": "13. Yüzyıl (1207 - 1273)",
        "work": "Dîvân-ı Kebîr (Külliyât-ı Şems)",
        "quote_tr": "Biz hepimiz gök kubbenin dönmesinden çıkan nağmeleri dinlemiş ruhlarız; Adem'in cisminde o nağmelerin hatırası vardır. Ney ve tamburdan işittiğimiz sesler, cennetteki o ezelî meclisin yankısıdır; işte bu yüzden dinleyen her garip ruh o vatanı hatırlar da ağlar.",
        "original_or_context": "ما همه اجزای آدم بوده‌ایم / در بهشت آن لحن‌ها بشنوده‌ایم",
        "category": "tasavvuf",
        "recommended_freq": 216.0,
        "reflection": "Platonik 'anamnesis' (hatırlama) kavramının tasavvuftaki tecellisi: Ses, ruhun ezelî hafızasını uyandırır."
    },
    {
        "id": "mevlana_fihi_mafih_nefes",
        "author": "Mevlânâ Celâleddîn-i Rûmî",
        "era": "13. Yüzyıl (1207 - 1273)",
        "work": "Fîhi Mâ Fîh (İçindekiler İçindedir)",
        "quote_tr": "Nefes birdir, lakin çarptığı kaba göre ses verir: Bir kamışa üflersen ney olur, yanık feryat eder; bir boruya üflersen cenk borusu olur, dehşet saçar. İnsanoğlu da böyledir; içini dünya kirinden boşaltan kimseye ilahi nefes çarptığında ondan ancak hikmet nağmesi sadır olur.",
        "original_or_context": "فیه ما فیه - مجالس مولانا جلال الدین رومی",
        "category": "tasavvuf",
        "recommended_freq": 528.0,
        "reflection": "Nöral arınma ve dinginlik: Zihin ne kadar sessiz ve arınmışsa, yansıttığı rezonans o kadar saftır."
    },
    {
        "id": "sems_tebrizi_kelam",
        "author": "Şems-i Tebrîzî",
        "era": "12. - 13. Yüzyıl (1185 - 1248)",
        "work": "Makâlât-ı Şems (Şems'in Sohbetleri)",
        "quote_tr": "Ağızdan çıkan kelâm bir oktur, bir defa fırlatıldı mı hedefini bulur. Söz vardır can bağışlar, söz vardır can alır. Söz vardır yaraya merhem, söz vardır cihanı ateşe verir. Bir kimse konuşurken önce kalbinin kuyusuna inmeli, oradaki sesin saf suyunu çekip öyle konuşmalıdır.",
        "original_or_context": "مقالات شمس تبریزی",
        "category": "tasavvuf",
        "recommended_freq": 432.0,
        "reflection": "Sözün biyoakustik ve niyet gücü: İletilen dalganın kalitesi kalpteki niyetin frekansıyla belirlenir."
    },
    {
        "id": "haci_bektas_nefes",
        "author": "Hacı Bektâş-ı Velî",
        "era": "13. Yüzyıl (1209 - 1271)",
        "work": "Makâlât (Sözler)",
        "quote_tr": "Diliyle incitmeyen, sazıyla hakikati söyleyen meclis bulur. Mârifet nefesi haktan alıp halka hakça dağıtmaktır. Çalınan sazın teli gönül teliyle bir olmadıkça o ses taş üstüne dökülen sudan farksızdır.",
        "original_or_context": "Makâlât-ı Hacı Bektâş-ı Velî",
        "category": "tasavvuf",
        "recommended_freq": 432.0,
        "reflection": "Akustik samimiyet ve rezonans: Fiziksel tel ile zihinsel niyetin koheransı."
    },
    {
        "id": "attar_mantik_ses",
        "author": "Ferîdüddin Attâr",
        "era": "12. - 13. Yüzyıl (1145 - 1221)",
        "work": "Mantıku't-Tayr (Kuşların Dili)",
        "quote_tr": "Simurg ezel meclisinde bir tüyünü Çin diyarına düşürdü; o tüyden binlerce renk ve ses dalgası saçıldı. Kuşların her biri kendi dilinde öttü amma hepsi o tek sesin arayışındaydı. Otuz kuş vadiyi aşıp aynaya baktığında, aradıkları Simurg'un kendi müşterek sesleri olduğunu gördüler.",
        "original_or_context": "منطق الطیر - فرید الدین عطار نیشابوری",
        "category": "tasavvuf",
        "recommended_freq": 963.0,
        "reflection": "Birlik şuuru ve polifonik koherans: Bütün frekansların kaynakta tek bir beyaz seste birleşmesi."
    },
    {
        "id": "hudayi_zikir_arsh",
        "author": "Azîz Mahmûd Hüdâyî",
        "era": "16. - 17. Yüzyıl (1541 - 1628)",
        "work": "Dîvân-ı İlâhiyyât",
        "quote_tr": "Zikrin sadası gökleri tuttuğunda, kalbin pası çözülür; göğüs kafesi arş-ı a'lâya dönüşür. Hu nidası nefesten nefese ulaştığında ne gam kalır ne keder. Her hücre 'Allah' derken beden kendi aslına secde eyler.",
        "original_or_context": "Divan-ı Aziz Mahmud Hüdayi - Zikir ve Vird Bahisleri",
        "category": "tasavvuf",
        "recommended_freq": 136.1,
        "reflection": "Kutsal tekrarların (japa/zikir) hücresel vagal senkronizasyon ve derin gevşeme etkisi."
    },
    {
        "id": "pythagoras_spheres_deaf",
        "author": "Pisagor (Pythagoras)",
        "era": "M.Ö. 6. Yüzyıl (M.Ö. 570 - 495)",
        "work": "Kürelerin Musikisi ve Sayı Öğretisi",
        "quote_tr": "Gök cisimleri uzayda dönerken öyle muazzam ve ilahi bir armoni (Musica Universalis) neşrederler ki, insan kulağı doğduğu andan itibaren bu sesin içinde yüzdüğü için onu duyamaz, sessizlik zanneder. Sessizlik dediğimiz şey, evrenin kesintisiz çalan senfonisidir.",
        "original_or_context": "Musica Universalis (Harmony of the Spheres) fragments via Porphyry & Iamblichus",
        "category": "antik_felsefe",
        "recommended_freq": 432.0,
        "reflection": "Kozmik dip gürültüsü ve temel armonikler: Duyularımızın alışkanlık eşiğinin ötesindeki ilahi ahenk."
    },
    {
        "id": "pythagoras_interval_medicine",
        "author": "Pisagor (Pythagoras)",
        "era": "M.Ö. 6. Yüzyıl (M.Ö. 570 - 495)",
        "work": "Monokord ve Ruh Terapisi",
        "quote_tr": "Sayılar evrenin nizamıdır; müzik ise sayıların duyulabilir halidir. Uygun müzikal aralıklarla çalınan bir lirik ezgi, öfkeli bir adamı dinginleştirebilir, hüzünlü bir genci cesaretle doldurabilir. Tellerin oranını bilmeyen hekim, ruhun dikişlerini dikemez.",
        "original_or_context": "Fragments on Music and Medicine from the Pythagorean School",
        "category": "antik_felsefe",
        "recommended_freq": 528.0,
        "reflection": "Pisagor matematiği: 2:1 (oktav), 3:2 (tam beşli), 4:3 (tam dörtlü) sayısal oranlarının psiko-akustik tesiri."
    },
    {
        "id": "plato_republic_music",
        "author": "Platon (Eflatun)",
        "era": "M.Ö. 5. - 4. Yüzyıl (M.Ö. 428 - 348)",
        "work": "Devlet (Politeia, III. Kitap)",
        "quote_tr": "Müzik eğitimi terbiyelerin en kuvvetlisidir. Çünkü ritim ve armoni ruhun ta derinliklerine kadar işler, oraya sımsıkı yerleşir ve ona asalet, zarafet ve dürüstlük bağışlar. Doğru terbiye edilmiş bir ruh, güzel olanı derhal tanır ve onu içine sindirerek beslenir.",
        "original_or_context": "Πολιτεία (Republic) Book III, 401d",
        "category": "antik_felsefe",
        "recommended_freq": 432.0,
        "reflection": "Müziğin nöroplastisite ve ahlaki karakter inşasındaki vazgeçilmez temel rolü."
    },
    {
        "id": "plato_timaeus_soul_ratios",
        "author": "Platon (Eflatun)",
        "era": "M.Ö. 4. Yüzyıl (M.Ö. 360 civarı)",
        "work": "Timaios (Timaeus)",
        "quote_tr": "Evrenin Ruhu, Yaratıcı (Demiurgos) tarafından müzikal aralıklara, ses oktavlarına ve geometrik oranlara göre yoğrulmuştur. Bu sebeple kulaklarımızdaki işitme duyusu bize sadece geçici bir haz için değil, içimizdeki bozulmuş ruh ritmini evrenin ebedi ritmine yeniden akort etmek için ihsan edilmiştir.",
        "original_or_context": "Τίμαιος (Timaeus) 47b-d",
        "category": "antik_felsefe",
        "recommended_freq": 136.1,
        "reflection": "Akustik re-entrainment: Bireysel biyoritmi kozmik temel frekansa geri uyumlama."
    },
    {
        "id": "aristotle_politics_catharsis",
        "author": "Aristoteles (Aristo)",
        "era": "M.Ö. 4. Yüzyıl (M.Ö. 384 - 322)",
        "work": "Politika (VIII. Kitap) & Poetika",
        "quote_tr": "Müzik doğrudan ruhun duygulanımlarına benzer modeller üretir: Öfke, yumuşaklık, cesaret ve itidal ezgilerde apaçık tezahür eder. Kutsal ezgileri dinleyen kimseler, sanki tıbbi bir arınma (katarsis) ve ilaç almışçasına ruhlarındaki aşırılıklardan arınır ve dinginleşirler.",
        "original_or_context": "Πολιτικά (Politics) Book VIII, 1340a-1342a",
        "category": "antik_felsefe",
        "recommended_freq": 396.0,
        "reflection": "Akustik katarsis: Bastırılmış duyguların rezonant ses dalgalarıyla boşaltılması ve regülasyonu."
    },
    {
        "id": "hermes_kybalion_vibration",
        "author": "Hermes Trismegistus (Hermetik Külliyat)",
        "era": "Kadim İskenderiye Geleneği",
        "work": "Kybalion (Titreşim Prensibi / III. Hermetik Yasa)",
        "quote_tr": "Hiçbir şey durmaz; her şey hareket eder; her şey titreşir. Saf Ruh'tan en kaba maddeye kadar evrendeki her varlık mertebesi yalnızca farklı bir titreşim derecesinden ibarettir. Titreşim prensibini anlayan kimse, zihinsel dönüşümün asasını elinde tutar.",
        "original_or_context": "The Kybalion: 'Nothing rests; everything moves; everything vibrates.'",
        "category": "antik_felsefe",
        "recommended_freq": 528.0,
        "reflection": "Modern kuantum dalga mekaniğinin binlerce yıl evvelki hermetik formülasyonu."
    },
    {
        "id": "boethius_three_musics",
        "author": "Anicius Manlius Severinus Boethius",
        "era": "5. - 6. Yüzyıl (477 - 524)",
        "work": "De Institutione Musica (Müzik Eğitimi Üzerine)",
        "quote_tr": "Üç türlü mûsikî vardır: Birincisi gezegenlerin ve mevsimlerin ahengi olan Kozmik Müzik (Musica Mundana); ikincisi ruh ile bedenin eklemlerini bir arada tutan İnsan Müziği (Musica Humana); üçüncüsü ise telli ve nefesli aletlerden çıkan Enstrüman Müziği'dir (Musica Instrumentalis). Enstrüman, insana kendi iç müziğini hatırlatır.",
        "original_or_context": "De Institutione Musica, Liber I",
        "category": "antik_felsefe",
        "recommended_freq": 432.0,
        "reflection": "Orta Çağ ve Rönesans müziğinin omurgası: Makrokozmos, mikrokozmos ve enstrüman birliği."
    },
    {
        "id": "kepler_harmonices_polyphony",
        "author": "Johannes Kepler",
        "era": "16. - 17. Yüzyıl (1571 - 1630)",
        "work": "Harmonices Mundi (Dünyanın Uyumu, 1619)",
        "quote_tr": "Göklerin hareketi, bir akıl tarafından kavranabilen ebedi bir polifonik konsere benzer. Gezegenler güneşe yaklaşıp uzaklaşırken hızları değişir ve bu hız oranları tam müzikal aralıklara denk düşer: Satürn ve Jüpiter bas söyler, Mars tenor, Dünya ve Venüs alto, Merkür ise tiz bir soprano gibi nağme eyler.",
        "original_or_context": "Harmonices Mundi (The Harmony of the World), Libri V",
        "category": "bilim_ve_fizik",
        "recommended_freq": 136.1,
        "reflection": "Kepler yasalarının müzik teorisiyle kusursuz kesişimi: Gezegen periyotlarının ses aralıkları."
    },
    {
        "id": "laozi_great_sound",
        "author": "Laozi (Lao Tzu)",
        "era": "M.Ö. 6. Yüzyıl (M.Ö. 571 - 471)",
        "work": "Tao Te Ching (Yol ve Erdem Kitabı, 41. Bölüm)",
        "quote_tr": "Büyük karelerin köşeleri yoktur; büyük kaplar geç tamamlanır; büyük ses işitilmez; büyük suretin biçimi yoktur. Tao gizlidir ve isimsizdir; lakin her şeyi besleyen ve kemale erdiren yalnızca O'dur.",
        "original_or_context": "大音希声，大象无形 - 道德经 第四十一章",
        "category": "antik_felsefe",
        "recommended_freq": 7.83,
        "reflection": "Duyulabilir gürültünün ötesindeki derin sessizlik alanı (infrases ve kozmik dip dalgası)."
    },
    {
        "id": "mandukya_om_trinity",
        "author": "Mandukya Upanişad",
        "era": "M.Ö. 1. Binyıl (Vedik Dönem)",
        "work": "Mandukya Upanishad (1. Bölüm)",
        "quote_tr": "OM hecesi bütün kainattır. Geçmiş, şimdi ve gelecek olan ne varsa hepsi OM'dur. Bu üç zaman diliminin ötesinde olan ebediyet de OM'dan başka bir şey değildir. Bu ses; uyanıklık (A), rüya (U) ve derin uykusuzluk (M) hallerini aşan dördüncü şuura (Turiya) açılan kapıdır.",
        "original_or_context": "ओमित्येेतदक्षरमिदँ सर्वं तस्योपव्याख्यानं - माण्डूक्योपनिषत्",
        "category": "kutsal_metin",
        "recommended_freq": 136.1,
        "reflection": "A-U-M formantlarının beyin dalgası spektrumunda Alfa, Teta ve Delta hallerini kucaklaması."
    },
    {
        "id": "chhandogya_sun_song",
        "author": "Chhandogya Upanişad",
        "era": "M.Ö. 8. - 6. Yüzyıl",
        "work": "Chhandogya Upanishad (III. Bölüm)",
        "quote_tr": "Güneş gökyüzünde ışıldarken bir ilahi terennüm eyler. O, kainatın kalbindeki bal peteğidir; ışınları ise nehirler gibi akıp yeryüzündeki canlıların hücrelerini canlandıran ses telleridir. Güneşi dinleyen kimse ölümü tanımaz.",
        "original_or_context": "छान्दोग्योपनिषत् - तृतीयोध्यायः",
        "category": "kutsal_metin",
        "recommended_freq": 126.22,
        "reflection": "Güneşin 126.22 Hz rezonant frekansı (Cousto oktavı) ve canlılar üzerindeki biyo-ritmik canlandırıcı etkisi."
    },
    {
        "id": "heart_sutra_emptiness_sound",
        "author": "Prajnaparamita Kalp Sutrası",
        "era": "M.S. 1. Yüzyıl (Budist Külliyat)",
        "work": "Maha Prajnaparamita Hridaya Sutra",
        "quote_tr": "Biçim boşluktur, boşluk biçimdir; biçim boşluktan ayrı değildir, boşluk biçimden ayrı değildir. Duyum, algı, zihinsel oluşumlar ve bilinç de böyledir. Ses de böyledir; titreşir lakin özünde kalıcı bir töz barındırmaz; bu idrake eren kimse korkudan kurtulur.",
        "original_or_context": "色即是空，空即是色，受想行识亦复如是 - 般若波罗蜜多心经",
        "category": "kutsal_metin",
        "recommended_freq": 432.0,
        "reflection": "Kuantum dalga parçacık ikiliği ve sesin boşluktaki geçici dalgalanması: Zihinsel dinginlik anahtarı."
    },
    {
        "id": "mezmur_150_nefes",
        "author": "Kral Davud (Mezmurlar / Zebur)",
        "era": "M.Ö. 10. Yüzyıl (M.Ö. 1000 civarı)",
        "work": "Tevrat / Mezmurlar 150:1-6",
        "quote_tr": "Rabb'e hamdedin! O'na boru sesiyle hamdedin; O'na lirik ve çenk ile hamdedin! O'na tefle, dansla hamdedin; O'na telli sazlarla ve neyle hamdedin! O'na çınlayan zillerle hamdedin! Bütün nefes alan canlılar Rabbe hamdetsin!",
        "original_or_context": "כֹּל הַנְּשָׁמָה תְּהַלֵּל יָהּ הַלְלוּ-יָהּ (Kol haneshamah tehallel Yah)",
        "category": "kutsal_metin",
        "recommended_freq": 528.0,
        "reflection": "Nefes ve ses ile kainatın varlık korosuna katılma: Şükran ve hücresel esenlik rezonansı."
    },
    {
        "id": "davud_lir_saul",
        "author": "I. Samuel (Tevrat)",
        "era": "M.Ö. 10. Yüzyıl",
        "work": "I. Samuel 16:23",
        "quote_tr": "Kral Saul'ün üzerine kötü ve hırçın bir ruh (ağır anksiyete ve melankoli) çöktüğünde; Davud lirini alır, parmaklarıyla çalardı. Saul rahatlar, ferahlar ve o kötü ruh ondan uzaklaşıp giderdi.",
        "original_or_context": "וְלָקַח דָּוִד אֶת-הַכִּנּוֹר וְנִגֵּן בְּיָדוֹ וְרָוַח לְשָׁאוּל וְטוֹב לוֹ",
        "category": "kutsal_metin",
        "recommended_freq": 396.0,
        "reflection": "Tarihteki ilk kaydedilmiş psikiyatrik müzikterapi vakası: Telli sazla panik ve buhran teskini."
    },
    {
        "id": "yuhanna_soz_kelam",
        "author": "Yuhanna İncili",
        "era": "1. Yüzyıl",
        "work": "İncil / Yuhanna 1:1-3",
        "quote_tr": "Başlangıçta Söz (Logos) vardı. Söz Tanrı ile birlikteydi ve Söz Tanrı idi. Başlangıçta O, Tanrı ile birlikteydi. Her şey O'nun aracılığıyla var oldu; var olan hiçbir şey O'nsuz var olmadı.",
        "original_or_context": "Ἐν ἀρχῇ ἦν ὁ λόγος, καὶ ὁ λόγος ἦν πρὸς τὸν θεόν, καὶ θεὸς ἦν ὁ λόγος",
        "category": "kutsal_metin",
        "recommended_freq": 528.0,
        "reflection": "Kozmik logos / frekans: Maddeden önce sesin, frekansın ve sözün önceliği ontolojisi."
    },
    {
        "id": "kuran_fussilet_gelin",
        "author": "Kur'ân-ı Kerîm",
        "era": "7. Yüzyıl",
        "work": "Fussilet Sûresi, 41:11",
        "quote_tr": "Sonra duman (gaz bulutu) halinde bulunan göğe yöneldi; ona ve yeryüzüne: 'İsteyerek veya istemeyerek gelin!' buyurdu. İkisi de: 'İsteyerek ve itaat ederek geldik' dediler.",
        "original_or_context": "ثُمَّ اسْتَوَىٰ إِلَى السَّمَاءِ وَهِيَ دُخَانٌ فَقَالَ لَهَا وَلِلْأَرْضِ ائْتِيَا طَوْعًا أَوْ كَرْهًا قَالَتَا أَتَيْنَا طَائِعِينَ",
        "category": "kutsal_metin",
        "recommended_freq": 7.83,
        "reflection": "Yaradılışın kozmik hitap ve icabet frekansı: Madde, ilahi emre titreşimsel rıza ile şekillenmiştir."
    },
    {
        "id": "kuran_kaf_sayha",
        "author": "Kur'ân-ı Kerîm",
        "era": "7. Yüzyıl",
        "work": "Kâf Sûresi, 50:41-42",
        "quote_tr": "Çağırıcının yakın bir yerden sesleneceği güne kulak ver! O gün insanlar o dehşetli hak sayhayı (büyük akustik dalgayı) duyacaklardır. İşte o gün kabirlerden çıkış günüdür.",
        "original_or_context": "وَاسْتَمِعْ يَوْمَ يُنَادِ الْمُنَادِ مِن مَّكَانٍ قَرِيبٍ * يَوْمَ يَسْمَعُونَ الصَّيْحَةَ بِالْحَقِّ",
        "category": "kutsal_metin",
        "recommended_freq": 174.0,
        "reflection": "Diriliş ve dönüşümün bir ses dalgası (Sayha / Sûr üflemesi) ile gerçekleşmesi gerçeği."
    },
    {
        "id": "kuran_isra_sifa",
        "author": "Kur'ân-ı Kerîm",
        "era": "7. Yüzyıl",
        "work": "İsrâ Sûresi, 17:82",
        "quote_tr": "Biz Kur'an'dan, müminler için şifa ve rahmet olan şeyleri indiriyoruz; zalimlerin ise ancak ziyanını artırır.",
        "original_or_context": "وَنُنَزِّلُ مِنَ الْقُرْآنِ مَا هُوَ شِفَاءٌ وَرَحْمَةٌ لِّلْمُؤْمِنِينَ",
        "category": "kutsal_metin",
        "recommended_freq": 528.0,
        "reflection": "Kıraat sesinin nörobiyolojik, psikoakustik ve hücresel şifa frekansı boyutu."
    },
    {
        "id": "kuran_hasr_dag",
        "author": "Kur'ân-ı Kerîm",
        "era": "7. Yüzyıl",
        "work": "Haşr Sûresi, 59:21",
        "quote_tr": "Eğer biz bu Kur'an'ı bir dağın üzerine indirseydik, muhakkak ki onu Allah korkusundan baş eğerek paramparça olmuş görürdün. Biz bu misalleri insanlara düşünsünler diye veriyoruz.",
        "original_or_context": "لَوْ أَنزَلْنَا هَٰذَا الْقُرْآنَ عَلَىٰ جَبَلٍ لَّرَأَيْتَهُ خَاشِعًا مُّتَصَدِّعًا مِّنْ خَشْيَةِ اللَّهِ",
        "category": "kutsal_metin",
        "recommended_freq": 432.0,
        "reflection": "Akustik rezonansın kütleleri sarsabilen ve taşlaşmış kalpleri yumuşatabilen kurucu kuvveti."
    },
    {
        "id": "hadis_kuran_tezyin",
        "author": "Hz. Muhammed (s.a.v.)",
        "era": "7. Yüzyıl",
        "work": "Sahîh-i Buhârî (Kitâbu't-Tevhîd, 52)",
        "quote_tr": "Kur'ân'ı seslerinizle güzelleştirip süsleyiniz; zira güzel ses Kur'ân'ın güzelliğini ve kalplere nüfuzunu ziyadeleştirir.",
        "original_or_context": "زَيِّنُوا الْقُرْآنَ بِأَصْوَاتِكُمْ فَإِنَّ الصَّوْتَ الْحَسَنَ يَزِيدُ الْقُرْآنَ حُسْنًا",
        "category": "kutsal_metin",
        "recommended_freq": 432.0,
        "reflection": "Akustik estetizm ve rezonans: Sözün hakikati sesin ahengiyle birleştiğinde zihinsel dirençler kırılır."
    },
    {
        "id": "hadis_sekine_kandil",
        "author": "Hz. Muhammed (s.a.v.)",
        "era": "7. Yüzyıl",
        "work": "Sahîh-i Müslim (Müsâfirîn, 240)",
        "quote_tr": "Üseyd bin Hudayr gece vakti Kehf sûresini okurken atı şahlandı; göğe baktığında bir bulut içinde kandiller gibi parıldayan nurların indiğini gördü. Sabah Resûlullah'a haber verdiğinde Efendimiz şöyle buyurdu: 'Onlar meleklerdi; senin kıraatinin sesini dinlemek için yaklaştılar; okumaya devam etseydin sabahleyin herkes onları gözleriyle görecekti.'",
        "original_or_context": "تِلْكَ السَّكِينَةُ نَزَلَتْ لِلْقُرْآنِ",
        "category": "kutsal_metin",
        "recommended_freq": 963.0,
        "reflection": "Ses dalgalarının metafizik ve elektromanyetik boyutu: Sekine ve koherans alanı doğuşu."
    },
    {
        "id": "hans_jenny_cymatics_matrix",
        "author": "Dr. Hans Jenny",
        "era": "20. Yüzyıl (1904 - 1972)",
        "work": "Cymatics: The Structure and Dynamics of Waves and Vibrations (1967)",
        "quote_tr": "Sematik deneyleri göstermiştir ki ses; biçim yaratan, biçimi koruyan ve biçimi dönüştüren temel kuvvettir. Sıvı, gaz ve tozlar frekansın emriyle anında canlı doku morfolojisine benzer peteklere, sarmallara ve mandalalara dönüşür. Biyoloji, katılaşmış sematiktir.",
        "original_or_context": "Cymatics demonstrates the generative power of wave phenomena in matter.",
        "category": "bilim_ve_fizik",
        "recommended_freq": 528.0,
        "reflection": "Hücresel farklılaşma ve embriyolojik gelişim sürecindeki akustik mikro-dalgaların rolü."
    },
    {
        "id": "chladni_acoustic_geometry",
        "author": "Ernst Florens Friedrich Chladni",
        "era": "18. - 19. Yüzyıl (1756 - 1827)",
        "work": "Entdeckungen über die Theorie des Klanges (1787)",
        "quote_tr": "Plakanın kenarına keman yayını sürttüğümde, üzerindeki kum taneleri gelişigüzel savrulmadı; görünmez bir nizamın emrine girerek kusursuz geometrik desenler (Chladni figürleri) çizdi. Ses, sessizliğin zeminine kendi imzasını kazımaktaydı.",
        "original_or_context": "Discoveries in the Theory of Sound (Leipzig, 1787)",
        "category": "bilim_ve_fizik",
        "recommended_freq": 432.0,
        "reflection": "Nodal çizgiler fiziği: Ses basıncının sıfır olduğu hatlarda toplanan maddenin geometrik nizamı."
    },
    {
        "id": "schrodinger_negentropy_harmony",
        "author": "Erwin Schrödinger",
        "era": "20. Yüzyıl (1887 - 1961)",
        "work": "What is Life? (Hayat Nedir?, 1944)",
        "quote_tr": "Canlı bir organizma termodinamik dengeden (yani ölümden) nasıl kaçınır? Çevresinden sürekli 'negatif entropi' çekerek! Canlılık, dış dünyadaki kaotik dağınıklıktan bir düzen ve ritmik ahenk süzebilme kabiliyetidir.",
        "original_or_context": "What is Life? The Physical Aspect of the Living Cell (Cambridge, 1944)",
        "category": "bilim_ve_fizik",
        "recommended_freq": 7.83,
        "reflection": "Şifa frekansları bedenin entropik kaosunu düşürerek negatif entropi ve hücresel koherans sağlar."
    },
    {
        "id": "david_bohm_holomovement",
        "author": "David Bohm",
        "era": "20. Yüzyıl (1917 - 1992)",
        "work": "Wholeness and the Implicate Order (Bütünlük ve Saklı Düzen)",
        "quote_tr": "Kainat statik şeylerin toplamı değil, kesintisiz bir 'Holo-hareket' (Holomovement) akışıdır. Nasıl bir ses kaydındaki her dalga diğer bütün enstrümanların bilgisini kendi içinde barındırıyorsa; evrendeki her atomaltı parçacık da tüm kainatın frekansını kendi saklı düzeninde katlanmış olarak taşır.",
        "original_or_context": "Wholeness and the Implicate Order (Routledge, 1980)",
        "category": "bilim_ve_fizik",
        "recommended_freq": 432.0,
        "reflection": "Holografik rezonans: Bireysel bilincin mikro dalgası, evrensel makro alanla sürekli temas halindedir."
    },
    {
        "id": "masaru_emoto_water_crystal",
        "author": "Dr. Masaru Emoto",
        "era": "20. - 21. Yüzyıl (1943 - 2014)",
        "work": "The Hidden Messages in Water (Sudaki Gizli Mesajlar, 2004)",
        "quote_tr": "Su, sadece kimyasal bir bileşik değil; bilinci, sesi ve niyeti kaydeden kozmik bir teyptir. 'Sevgi ve Şükran' söylenen veya Mozart dinletilen su dondurulduğunda kusursuz altıgen pırlanta kristalleri oluştururken; öfke ve nefret yöneltilen suyun kristalleri paramparça olmaktadır. İnsan bedeninin yüzde yetmişi su olduğuna göre, duyduğumuz ve söylediğimiz sözlerin hücresel akıbetini varın siz düşünün.",
        "original_or_context": "The Hidden Messages in Water (Beyond Words, 2004)",
        "category": "mistik_akustik",
        "recommended_freq": 528.0,
        "reflection": "Beden sıvılarının akustik ve niyet bazlı yeniden yapılanması (su kristalizasyonu)."
    },
    {
        "id": "popp_biophoton_coherence",
        "author": "Dr. Fritz-Albert Popp",
        "era": "20. - 21. Yüzyıl (1938 - 2018)",
        "work": "Biyofotonik ve Hücresel İletişim Araştırmaları",
        "quote_tr": "Sağlıklı bir hücre çekirdeği (DNA), lazer benzeri ultra zayıf koherent ışık ve akustik dalgalar yayar. Kanserli veya hastalıklı dokuda ise bu koherans bozulur ve sinyal kaotikleşir. Şifa, hücrenin koherent rezonans alanını yeniden tesis etmekten ibarettir.",
        "original_or_context": "Biophotonics and Coherent Electromagnetic Fields in Living Cells",
        "category": "bilim_ve_fizik",
        "recommended_freq": 528.0,
        "reflection": "528 Hz ve Solfeggio harmoniklerinin hücresel koherans ve biyofoton emisyonunu desteklemesi."
    },
    {
        "id": "rife_mortal_oscillatory",
        "author": "Royal Raymond Rife",
        "era": "20. Yüzyıl (1888 - 1971)",
        "work": "Evrensel Mikroskop ve Rezonans Frekans Terapisi",
        "quote_tr": "Nasıl opera sanatçısının tutturduğu belirli bir tiz nota şarap kadehinin doğal frekansıyla eşleştiğinde kadehi paramparça ederse; her virüs ve bakterinin de kendine has bir 'Ölümcül Salınım Oranı' (Mortal Oscillatory Rate) vardır. O spesifik frekans gönderildiğinde çevre dokuya hiç zarar vermeden patojen imha olur.",
        "original_or_context": "Mortal Oscillatory Rate (MOR) Principles and High-Frequency Resonators",
        "category": "bilim_ve_fizik",
        "recommended_freq": 741.0,
        "reflection": "Hedefe yönelik biyo-rezonans: Toksin ve patojenlerin frekansla etkisiz hale getirilmesi."
    },
    {
        "id": "cousto_cosmic_law",
        "author": "Hans Cousto",
        "era": "20. - 21. Yüzyıl (1948 - Günümüz)",
        "work": "Die Kosmische Oktave: Der Weg zum universellen Einklang (1984)",
        "quote_tr": "Evrende hiçbir şey rasgele değildir. Gezegenlerin yörünge sürelerini oktav yasasıyla ses sahasına indirdiğimizde; Dünya'nın OM frekansı (136.1 Hz), Güneş'in Manipura tonu (126.22 Hz) ve Platonik Yılın Taç çakra rezonansı (172.06 Hz) matematiksel bir zorunlulukla açığa çıkar. İnsan, kainatın akort edilmiş mikro halidir.",
        "original_or_context": "Die Kosmische Oktave - Gesetz des Pendels und Tonoktavierung",
        "category": "mistik_akustik",
        "recommended_freq": 136.1,
        "reflection": "Kozmik oktav formülü $f = \\frac{1}{T} \\cdot 2^n$ ile makrokozmos ve insan biyofiziğinin tam örtüşmesi."
    },
    {
        "id": "beethoven_revelation",
        "author": "Ludwig van Beethoven",
        "era": "18. - 19. Yüzyıl (1770 - 1827)",
        "work": "Bettina von Arnim'e Mektuplar (1810)",
        "quote_tr": "Müzik, insanın ruhunu tutuşturan bir kıvılcımdır; o, tüm bilgelik ve felsefeden daha yüksek bir ifşa ve vahiydir. Müziğimin derin anlamına nüfuz edebilen bir kimse, diğer insanların sürüklendiği bütün sefaletlerden ve dünyevi ıstıraplardan ebediyen azade olur.",
        "original_or_context": "Musik ist höhere Offenbarung als alle Weisheit und Philosophie",
        "category": "mistik_akustik",
        "recommended_freq": 432.0,
        "reflection": "Müziğin aşkın ve kathartik gücü: Sanatın felsefeyi aşan doğrudan ontolojik şifası."
    },
    {
        "id": "goethe_frozen_music",
        "author": "Johann Wolfgang von Goethe",
        "era": "18. - 19. Yüzyıl (1749 - 1832)",
        "work": "Eckermann ile Konuşmalar (1829)",
        "quote_tr": "Asil bir mimari eser gördüğümde aklıma daima şu fikir gelir: Mimari, taşların kalıbında donmuş mûsikîden başka bir şey değildir. Bir katedralin sütunları ve kubbeleri arasındaki nispetler, bir senfoninin ölçüleri ve akort aralıklarıdır.",
        "original_or_context": "Ich habe unter meinen Papieren ein Blatt gefunden, wo ich die Baukunst eine erstarrte Musik nenne",
        "category": "mistik_akustik",
        "recommended_freq": 432.0,
        "reflection": "Sematik mimari: Üç boyutlu mekanların akustik harmonik oranlarla inşası."
    },
    {
        "id": "victor_hugo_music_ineffable",
        "author": "Victor Hugo",
        "era": "19. Yüzyıl (1802 - 1885)",
        "work": "William Shakespeare Üzerine Denemeler (1864)",
        "quote_tr": "Müzik, kelimelerle ifade edilmesi imkansız olanı ve aynı zamanda sessiz kalınması asla kabil olmayanı haykırır.",
        "original_or_context": "La musique exprime ce qui ne peut être dit et sur quoi il est impossible de rester silencieux",
        "category": "mistik_akustik",
        "recommended_freq": 639.0,
        "reflection": "Duygusal sıkışmışlıkların çözümü: Dilin yetersiz kaldığı yerde kalbin sesle boşalması."
    },
    {
        "id": "inayat_khan_sound_creator",
        "author": "Hazrat Inayat Khan",
        "era": "19. - 20. Yüzyıl (1882 - 1927)",
        "work": "The Mysticism of Sound and Music (Sesin ve Müziğin Mistisizmi)",
        "quote_tr": "Kainatın bütün yapısı sesten bina edilmiştir; insan bedeni ise ruhun elindeki yaşayan bir sazdır. Bedenin teli fazla gerildiğinde veya gevşediğinde hastalık ve ızdırap doğar. Şifacı hekim, hastanın beden sazını ilahi ezgiyle yeniden akort eden kimsedir.",
        "original_or_context": "The Mysticism of Sound and Music: The Sufi Teachings on Sound",
        "category": "tasavvuf",
        "recommended_freq": 432.0,
        "reflection": "Sufi müzikterapi felsefesi: İnsan bedenini yaşayan bir enstrüman olarak akort etme sanatı."
    },
    {
        "id": "nietzsche_life_without_music",
        "author": "Friedrich Nietzsche",
        "era": "19. Yüzyıl (1844 - 1900)",
        "work": "Putların Alacakaranlığı (Götzen-Dämmerung, 1888)",
        "quote_tr": "Müziksiz bir hayat, bir hata, bir külfet, bir sürgün olurdu.",
        "original_or_context": "Ohne Musik wäre das Leben ein Irrthum",
        "category": "antik_felsefe",
        "recommended_freq": 432.0,
        "reflection": "Müziğin varoluşsal yaşama gücü (Wille zur Macht) ve trajik neşe aşılaması."
    },
    {
        "id": "kahlil_gibran_music_language",
        "author": "Halil Cibran (Kahlil Gibran)",
        "era": "19. - 20. Yüzyıl (1883 - 1931)",
        "work": "Müzik Üzerine (Al-Musiqa, 1905)",
        "quote_tr": "Müzik, ruhun lisanıdır. Nağmeler göğsün tellerine vurduğunda, fani dünyanın kelimeleri eriyip gider; geriye sadece aşkın, hüznün ve ümidin berrak nehri kalır. Müzik, göklerin yeryüzündeki sürgün çocuklarına fısıldadığı ana dilidir.",
        "original_or_context": "الموسيقى هي لغة الأرواح - جبران خليل جبران",
        "category": "mistik_akustik",
        "recommended_freq": 639.0,
        "reflection": "Evrensel duygusal rezonans: Kültürleri ve dilleri aşan ortak kalp tınısı."
    },
    {
        "id": "yehudi_menuhin_order",
        "author": "Yehudi Menuhin",
        "era": "20. Yüzyıl (1916 - 1999)",
        "work": "Unfinished Journey & Tema ve Çeşitlemeler",
        "quote_tr": "Müzik, kaosun ortasındaki ruha düzen, karmaşanın içindeki zihne huzur, yalnız kalmış bir kalbe ise evrensel bir kardeşlik hissi bağışlar. Kemanın yayını tele dokundurduğumda, sadece bir enstrüman çalmam; insanlığın ortak yaralarını sarmaya çalışırım.",
        "original_or_context": "Music creates order out of chaos: for rhythm imposes unanimity upon the divergent.",
        "category": "mistik_akustik",
        "recommended_freq": 432.0,
        "reflection": "Akustik koherans: Ritim ve armoninin beyin dalgalarındaki kaotik gürültüyü nizam ve sükuna çevirmesi."
    },
    {
        "id": "heisenberg_prob_waves",
        "author": "Werner Heisenberg",
        "era": "20. Yüzyıl (1901 - 1976)",
        "work": "Fizik ve Felsefe (Physics and Philosophy, 1958)",
        "quote_tr": "Madde sandığımız en küçük atomaltı parçacıklar gerçekte birer 'şey' değildir; onlar titreşen olasılık dalgaları ve bağlantılar ağıdır. Evren nesnelerden değil, sürekli dans eden dinamik rezonans olaylarından dokunmuştur.",
        "original_or_context": "The atoms or elementary particles themselves are not real; they form a world of potentialities or possibilities rather than one of things or facts.",
        "category": "bilim_ve_fizik",
        "recommended_freq": 7.83,
        "reflection": "Kuantum belirsizliği ve potansiyeller alanı: Madde, gözlemcinin niyet ve frekansıyla somutlaşır."
    }
]

# ID'si daha önce eklenmemişleri ekle
added_count = 0
for q in new_quotes:
    if q["id"] not in existing_ids:
        existing_quotes.append(q)
        existing_ids.add(q["id"])
        added_count += 1

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_quotes, f, ensure_ascii=False, indent=2)

print(f"Başarıyla {added_count} yeni alıntı eklendi. Toplam alıntı sayısı: {len(existing_quotes)}")
