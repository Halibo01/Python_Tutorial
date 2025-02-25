# Python'da İteratörler ve Generatörler


# Generatörler (Generators):
# Bellek verimliliği sağlayan ve ihtiyaç duyuldukça değer üreten özel bir iteratör türüdür.
# Bir fonksiyon içerisinde 'yield' ifadesi kullanıldığında bir generatör oluşturulmuş olur.


# Generatörlerin Kullanımı
def karmaşık_generatör():
    """Karmaşık bir generatör örneği: Farklı veri türleri döndürme"""
    yield "Başlangıç"
    for i in range(3):
        yield i  # Sayıyı döndürür
    yield [10, 20, 30]  # Liste döndürür
    yield {"anahtar": "değer"}  # Sözlük döndürür
    yield "Bitiş"

# Generatör örneği kullanımı
# Generatör ifadesi sona ulaşana kadar çalışmaya devam eder
# Generatör ifadesi sonsuz olarak devam ediyorsa kod sonsuz olarak çalışır
for eleman in karmaşık_generatör():
    print(eleman)

# Generatörlerin Bellek Verimliliği
# Normal liste yerine generatör kullanarak büyük veri kümelerinde bellekten tasarruf edilir.
# Böylece herhangi bir duraksama olmadan yada fazladan işlem yapmadan kod çalışmaya kaldığı yerden devam eder.
from sys import getsizeof

liste = [x for x in range(10000)]  # Tüm elemanlar bellekte tutulur
generator = (x for x in range(10000))  # Değerler gerektiğinde üretilir

print(getsizeof(liste))  # Büyük bir değer dönebilir
print(getsizeof(generator))  # Çok daha küçük bir değer döner

# yield from Kullanımı (İç içe generatörler)
# Birden fazla yield ifadesi kullanılabilir bu fonksiyonun normal çalışmasını değiştirmez
# return den farklı kılan özelliği fonksiyonu geri döndürür ama fonksiyonun işlevselliğini durdurmaz
def alt_sayilar():
    yield from range(1, 4)
    yield from range(6, 9)

for sayi in alt_sayilar():
    print(sayi)  # Çıktı: 1, 2, 3, 6, 7, 8

# Daha karmaşık bir generatör: Fibonacci sayıları ve kareleri
def fibonacci_kare(n):
    """İlk n Fibonacci sayısını ve karelerini üreten generatör."""
    a, b = 0, 1
    for _ in range(n):
        yield (a, a ** 2)  # Fibonacci sayısı ve karesi
        a, b = b, a + b

# Kullanım örneği
for fib, kare in fibonacci_kare(10):
    print(f"Fibonacci: {fib}, Karesi: {kare}")