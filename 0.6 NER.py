#NER (Varlık İsmi Tanıma)

"""
NER Nedir ?
Metin içinde geçen özel isimleri bulma ve sınıflandırma işlemidir.
Yani Varlıkların isimlerini tanıma işlemi.

----->Basit tanımını yapacak olursam:
Bir metin içerisindeki: kişi isimlerini, şirketleri, şehirleri, tarihleri,
para birimlerini otomatik olarak bulabilir.



Örnek olarak:
'Elon Musk 2002 yılında SpaceX şirketini kurdu.'
Elon Musk - Kişi
2002 - Tarih
SpaceX - Şirket


**** Bu çok önemlidir çünkü bilgisayar metni sadece kelime olarak değil, anlam olarak yorumlar.
"""


#Spacy üzerinen örnek oluşturacak olursak
import spacy

nlp = spacy.load("en_core_web_sm")

text = "Elon Musk SpaceX i 2002'de California'da kurdu."

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)


#Örnek 2:

import spacy

nlp = spacy.load("tr_core_news_sm")

text = "Ahmet 2024 yılında İstanbul Üniversitesi'nde okudu."

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)


"""
NER Uygulama Alanları:

Bilgi Çıkarma
Metinden veri toplama

Otomatik Özetleme
Önemli isimleri çıkarma

Hukuk Sistemleri
Kanun ve dava isimleri bulma

E-Ticaret
Ürün ve marka tanıma

Güvenlik
Şüpheli kişi ve organizasyon analizi
"""



#Tokenizasyon ile pipline
#Metin - Tokenization - POS Tagging - NER -Bilgi Çıkarma
