#Tokenizasyon İşlemleri

"""
Token Nedir ?
NLP'de token, metinin makinenin anlayabilmesi için küçük parçalara ayrıdığı
en temel birimdir.

Token kimi zaman bir kelime kimi zaman bir harf veya hece olabilir.
Değişiklik gösterir yani projeden projeye.
Token kullanılmasını sebebi ise cümleyi makine tek seferde anlayamaz.
Fakat tokelar ile duygu  analizi, çeviri, metinlerin sınıflandırmasını
hallettiğinden bu işlemler hız kazanır.

Tokenize Etmek Nedir ?
Tokenizasyon ise bu metnin parçalara ayrılma işlemine verilen addır.

"Bugün", "hava", "çok", "güzel", "."
Bu işlem mesela bir tokenizasyon işlemidir.


1-Cümle Tokenizasyonu:
 "Bugün hava çok güzel.",
 "Yarın yağmur yağacak!",
 "Hazır mısın?"
  gibi ifadeler cümlelerin metinden ayrılması sonucu tokinize edilmiş halidir.
2-Kelime Tokenizasyonu:
"Doğal", "dil", "işleme", "çok", "eğlenceli", "!"
Bu ifade ise kelimelerin cümlelere ayrıldıktan sonra kendi içerisinde kelime
kelime, noktalamasına kadar ayrılması işlemidir.

"""

#Örnek olacak ise:

from nltk.tokenize  import word_tokenize
text = "Merhaba! Doğal dil işleme üzerine çalışıyorum. Ben Furkan Gül"
tokens = word_tokenize(text,language="turkish")
print(tokens)
