#POS Tags (Sözcük Türleri)

"""
POS Tags:
Bir kelimenin cümlede isim mi, sıfat mı olduğunu gösteren etiektlerdir.
Buradaki amaç bilgisayarın dili anlamasını sağlamaktır.
"""

#Temel sözcük türleri

"""
1-Noun (İsim)
Bir yeri, kişiyi, kavramı belirtir.
Örnek olarka:
Kitap
Masa
İstanbul
Öğrenci

2-Verb (Fiil)
Eylem belirtir.
Örnek olarak:
Gitmek
Okumak
Koşmak


3-Adjective (Sıfat)
İsmi niteler.
Örnek olarak:
Güzel
Büyük
Hızlı


4-Adverb (Zarf)
Fiili veya sıfatı niteler.
Örnek olarak:
Hızlıca
Çokça
Yavaşça
Çok


5-Pronoun (Zamir)
İsmin yerine geçer.
Örnek olarak:
Ben
Sen
O


6-Preposition (Edat)
Yer zaman ve yön belirtir.
Örnek olarak:
içinde
önünde
yanında
yarın
sabah


7-Conjunction (Bağlaç)
Kelime ve cümleleri bağlar.
Örnek olarak:
Ve
Veya 
Yada
Ama

8-Determiner (Belirteç)
İsimleri belirtir.
Örnek olarak:
bir
bu 
şu
ordaki
"""


#Genelde NLTK veya spaCy kullanılır.
#NLTK Örneği
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "The dog runs fast"
tokens = nltk.word_tokenize(text)

print(nltk.pos_tag(tokens))
