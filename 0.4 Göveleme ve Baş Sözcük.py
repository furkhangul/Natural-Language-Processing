#Gövdeleme ve Baş Sözcük Çıkarımı

"""
Neden Gövdeleme ve Baş Sözcük İhtiyacı Vardır ?
Metinleri daha sonraki aşamalara götürmek için kullanılır.
Daha açık şekilde :
Aynı anlamı taşıyan kelimelerin çok fazla farklı biçimde karşımıza çıkması.
Meslea
Kitap
Kitaplar
Kitaptan
Kitabım
Gövdeleme, kelimenin eklerini atarak ortak gövdeyi bulur:
kitaplar → kitap


Gövdeleme kelime sayısını azaltır.
Arama ve sınıflandırma sonuçlarını iyileştirir
Modeli daha hızlı ve verimli yapar
Aynı anlamlı kelimeleri tek temsil altında toplar
Fakat
Dil bilgisi kurallarını tam dikkate almaz
Bazen anlamsız gövdeler üretir


Lemmatization yani baş sözcük daha akıllı ve dilbilgisel bir işlemdir.
Amaç kelimeyi sözlükteki temel anlamına (lemma) indirmek
"""
