# Python'da for döngüsü, belirli bir diziyi, listeyi, tuple'ı, string'i veya başka bir iterable'ı döngüye sokarak her eleman üzerinde işlem yapmanıza olanak tanır.
# Aşağıdaki örneklerde for döngüsünün nasıl çalıştığını görebilirsiniz.

# 1. Liste üzerinde for döngüsü
"""
my_list = [1, 2, 3, 4, 5]

# Bu örnekte my_list içindeki her bir sayıyı sırayla yazdırıyoruz.
for num in my_list:
    print(num)  # Her bir num değerini tek tek yazdırır: 1, 2, 3, 4, 5

# Liste üzerinde direkt değişiklik yapılarak da elemanlar yazdırılabilir
for num in my_list[::-1]:
    print(num) # Her bir değeri tersten yazdırır: 5, 4, 3, 2, 1
"""


# 2. String üzerinde for döngüsü
"""
my_string = "Python"
# Bu örnekte my_string içindeki her bir karakteri sırayla yazdırıyoruz.
for char in my_string:
    print(char)  # Her bir char değerini yazdırır: 'P', 'y', 't', 'h', 'o', 'n'
"""


# 3. range() fonksiyonu ile for döngüsü
# range() fonksiyonu, belirli bir aralıkta sayı üretir.
"""
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4 sayıları yazdırılır çünkü range(5) 0'dan başlayıp 5'e kadar gider.
"""


# range() fonksiyonu, başlangıç ve bitiş değerleri ile de kullanılabilir
# Burada, 2'den başlayıp 6'ya kadar olan sayıları yazdırıyoruz.
"""
for i in range(2, 6):
    # 2'den başlayarak, 6'ya kadar (6 dahil değil) sayıları yazdırır
    print(i)
# Çıktı:
# 2
# 3
# 4
# 5
"""


# range() fonksiyonu, adım değeri de alabilir
# Bu durumda, aradaki farkı belirleyebiliriz. Örneğin her adımda 2 artacak şekilde bir döngü oluşturuyoruz.
"""
for i in range(1, 10, 2):
    # 1'den başlayarak, 10'a kadar (10 dahil değil) her adımda 2 artırarak sayıları yazdırır
    print(i)
# Çıktı:
# 1
# 3
# 5
# 7
# 9
"""


# range() fonksiyonu, negatif adımla da kullanılabilir.
# Bu durumda, sayılar azalarak işlenir. Örneğin 10'dan 0'a kadar her adımda 2 azaltarak bir döngü oluşturuyoruz.
"""
for i in range(10, 0, -2):
    # 10'dan başlayarak, 0'a kadar (0 dahil değil) her adımda 2 azalarak sayıları yazdırır
    print(i)
# Çıktı:
# 10
# 8
# 6
# 4
# 2
"""


# range() fonksiyonu ile ters yönde bir döngü oluşturabiliriz.
# Örneğin, 5'ten başlayıp 0'a kadar (0 dahil) bir döngü oluşturmak için aşağıdaki gibi kullanabiliriz.
"""
for i in range(5, -1, -1):
    # 5'ten başlayarak, 0'a kadar (0 dahil) her adımda 1 azaltarak sayıları yazdırır
    print(i)
# Çıktı:
# 5
# 4
# 3
# 2
# 1
# 0
"""



# 4. İç içe for döngüsü (Nested for loop)
# Bu örnekte, her bir sayıyı iç içe bir döngüyle yazdırıyoruz.
"""
for i in range(3):  # Dış döngü
    for j in range(2):  # İç döngü
        print(f"i: {i}, j: {j}")
    # Çıktı: i: 0, j: 0
    # Çıktı: i: 0, j: 1
    # Çıktı: i: 1, j: 0
    # Çıktı: i: 1, j: 1
    # Çıktı: i: 2, j: 0
    # Çıktı: i: 2, j: 1
"""



# 5. for döngüsü ile koşul kullanımı
# Bir dizideki sadece tek sayıları yazdırmak için if şartı ekleyebiliriz.
"""
for num in my_list:
    if num % 2 != 0:  # Eğer sayı tekse
        print(num)  # 1, 3, 5 yazdırılır çünkü bunlar tek sayılardır.
"""


# 6. for döngüsü ile break kullanımı
# break komutu döngüyü erken bitirmek için kullanılır. Bu örnekte sayılar 3'e ulaşınca döngüden çıkıyoruz.
"""
for num in my_list:
    if num == 3:
        break  # 3'e ulaştığında döngüyü kırar ve sonrasındaki elemanları yazdırmaz.
    print(num)  # Çıktı: 1, 2
"""


# 7. for döngüsü ile continue kullanımı
# continue komutu, döngüdeki bir adımı atlamak için kullanılır. Burada 3'ü atlayıp diğer sayıları yazdırıyoruz.
"""
for num in my_list:
    if num == 3:
        continue  # 3'ü atlar, diğer elemanları yazdırmaya devam eder.
    print(num)  # Çıktı: 1, 2, 4, 5
"""


# 8. for döngüsü ile listeyi tersten gezme
# Bu örnekte, listeyi tersten yazdırıyoruz.
"""
for num in reversed(my_list):  # reversed() fonksiyonu listeyi tersine çevirir.
    print(num)  # Çıktı: 5, 4, 3, 2, 1
"""


# 9. for döngüsü ile başka bir iterable üzerinde işlem
# Set üzerinde for döngüsü kullanımı
"""
my_set = {1, 2, 3, 4, 5}

# Set'in her elemanını yazdırıyoruz.

for num in my_set:
    print(num)  # Çıktı sırasız olur: 1, 2, 3, 4, 5 (Set sırasız veri yapısıdır)
"""


# 10. for döngüsü ile dictionary üzerinde işlem
# Dictionary üzerinde for döngüsü kullanarak anahtar ve değerleri yazdırma
"""
my_dict = {"ad": "Ali", "yaş": 25, "şehir": "İstanbul"}

# Anahtar ve değerlerini birlikte yazdırıyoruz.

for key, value in my_dict.items():
    print(f"Anahtar: {key}, Değer: {value}")
    # Çıktı: Anahtar: ad, Değer: Ali
    # Çıktı: Anahtar: yaş, Değer: 25
    # Çıktı: Anahtar: şehir, Değer: İstanbul
"""