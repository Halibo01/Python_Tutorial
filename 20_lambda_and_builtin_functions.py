# Python'da Lambda Fonksiyonları Kullanımı

# Lambda fonksiyonları, Python'da tek satırda anonim (ismi olmayan) fonksiyonlar oluşturmak için kullanılır.
# Genellikle küçük ve basit işlemler için tercih edilir.


# Basit bir lambda fonksiyonu tanımlama
# lambda parametre1, parametre2, ...: işlem

# Fonksiyon ifadesi:
def kare_al(x):
    return x ** 2
print(kare_al(5))  # Çıktı: 25

# Lambda ifadesi:
kare_al = lambda x: x ** 2

# Kullanım örneği
print(kare_al(5))  # Çıktı: 25



# Birden fazla parametre alan lambda fonksiyonu

# Fonksiyon ifadesi:
def carp(x, y):
    return x * y
print(carp(3, 4))  # Çıktı: 12


# Lambda ifadesi:
carp = lambda x, y: x * y
print(carp(3, 4))  # Çıktı: 12



# Koşullu ifadelerle lambda kullanımı
# Koşulların yapısı şu şekildedir:
# lambda <argümanlar> : <Koşulu karşılarsa: 1.Çıktı> if <Koşul> else <Koşulu karşılamazsa: 2.Çıktı>
even_or_odd = lambda x: "Çift" if x % 2 == 0 else "Tek"
print(even_or_odd(10))  # Çıktı: Çift
print(even_or_odd(7))   # Çıktı: Tek





# map() fonksiyonunun açıklaması
# map(), bir fonksiyonu bir liste veya başka bir iterable üzerindeki her elemana uygular.
# Sonuç olarak, dönüşen öğeleri içeren bir map nesnesi döndürür.
# Genellikle list() fonksiyonu ile çevrilerek kullanılır.

# Lambda fonksiyonlarını map() ile kullanma
sayilar = [1, 2, 3, 4, 5]
kareler = list(map(lambda x: x ** 2, sayilar))
print(kareler)  # Çıktı: [1, 4, 9, 16, 25]




# filter() fonksiyonunun açıklaması
# filter(), verilen bir fonksiyonun True döndürdüğü öğeleri içeren bir filtrelenmiş iterable döndürür.
# Yani, belirli bir koşulu sağlayan öğeleri seçmek için kullanılır.

# Lambda fonksiyonlarını filter() ile kullanma
cift_sayilar = list(filter(lambda x: x % 2 == 0, sayilar))
print(cift_sayilar)  # Çıktı: [2, 4]




# reduce() fonksiyonunun açıklaması
# reduce(), bir liste veya iterable üzerindeki elemanları belirli bir işlemi tekrarlayarak birleştirmek için kullanılır.
# İlk iki elemanı işlemden geçirir, sonucu alır ve bir sonraki elemanla aynı işlemi yapar.
# Kullanmak için functools modülünden içe aktarılması gerekir.

from functools import reduce

# Lambda fonksiyonlarını reduce() ile kullanma
liste = [1, 2, 3, 4, 5]
toplam = reduce(lambda x, y: x + y, liste)
print(toplam)  # Çıktı: 15



# sorted() fonksiyonunun açıklaması
# sorted(), verilen bir iterable'ı belirli bir sıraya göre sıralamak için kullanılır.
# Varsayılan olarak küçükten büyüğe sıralar, ancak key parametresi ile özel sıralamalar yapılabilir.

# Lambda fonksiyonlarını sorted() ile kullanma
isimler = ["Ali", "Zeynep", "Mehmet", "Ayşe"]


# İsimleri uzunluklarına göre sırala
sirali_isimler = sorted(isimler, key=lambda x: len(x)) # len() fonksiyonu stringin uzunluğunu hesaplar ve çıktı olarak verir.
print(sirali_isimler)  # Çıktı: ['Ali', 'Ayşe', 'Mehmet', 'Zeynep']


