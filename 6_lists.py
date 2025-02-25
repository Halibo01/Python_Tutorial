import os

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # Sayılardan oluşan bir liste
names = ["Ali", "Ayşe", "Ahmet"]  # Stringlerden oluşan bir liste
mixed_list = [1, "apple", 3.14, True, my_list, "ahmet".upper, os.makedirs, os]  # Farklı türlerden öğeler içeren bir liste


# Listeden eleman alma ve dilimleme
"""
# Listenin uzunluğunu sayı olarak yazdırır
print(len(my_list)) 

# Sayılardan oluşan listeyi ekrana yazdırır
print(my_list)

# Listenin ilk elemanını (0. indeks) yazdırır
print(my_list[0])

# Listenin 0. ile 2. indeksler arasındaki elemanları yazdırır (3. indeks dahil değildir)
print(my_list[0:3])  

# Aynı şekilde, 0. ile 2. indeksler arasındaki elemanları yazdırır (3. indeks dahil değildir), ama burada dilimleme yöntemi farklı
print(my_list[:3])  # Bu da [0, 1, 2] olur

# Listenin 3. ile 5. indeksler arasındaki elemanları yazdırır
print(my_list[3:6])  # Bu da [3, 4, 5] olur

# Listenin 3. indeksten başlayıp, kalan tüm elemanları yazdırır
print(my_list[3:])  # Bu da [3, 4, 5] olur

# 2. ve 3. indeksler arasındaki elemanları yazdırır
print(my_list[2:4])  # Bu da [2, 3] olur

# Listedeki son elemanı alma
print(my_list[len(my_list) - 1])

# Listenin son elemanını yazdırır (negatif indeks kullanılır)
print(my_list[-1])  # Çıktı: 5 (Son eleman, -1 ile erişilir)

# Listenin son iki elemanını yazdırır (negatif indeksle dilimleme yapılır)
print(my_list[-2:])  # Çıktı: [4, 5] (Son iki eleman, -2 ile başlanarak alınır)

# Listenin elemanları farklı sırayla yazdırılabilir yada alınabilir


# Listenin elemanları her seferinde 1 eleman atlanarak yazdırılır
print(my_list[::2])

# Listenin elemanları tersten yazdırılır
print(my_list[::-1])

"""

# Liste özelliklerini yazdırma
"""
print(len(my_list)) # Listenin uzunluğunu yazdırır

print(my_list.count(2)) # 2 elemanının liste içindeki miktarını yazdırır

print(my_list.index(2)) # 2 sayısının konumunu/indexini yazdırır (eğer listede birden çok 2 değeri bulunuyorsa değerin bulunduğu ilk konumunu/indexini yazdırır)
"""


# Liste değişiklikleri gerçekleştirme
"""
my_list[0] = 10  # Listenin 0. index elemanını değiştirir
print(my_list)

my_list.append(7)  # Listenin sonuna 7 elemanını ekler
print(my_list)

# Listenin ortasına eleman koyma
my_list.insert(6, 6)  # Listenin 6. indeksine (yani 7. pozisyona) 6 elemanını ekler
print(my_list)

my_list.remove(10)  # Listeden ilk karşılaştığı 10 değerini çıkarır
print(my_list)

my_list.pop(0)  # Listenin 1. indeksindeki öğeyi çıkarır ve döndürür (Bu örnekte 7'yi çıkarır)
print(my_list)

my_list.reverse()  # Listeyi tersine çevirir
print(my_list)

my_list.sort()  # Listeyi küçükten büyüğe sıralar
print(my_list)


"""

# Stringler de liste gibi davranabilir
"""
example = "Örnek string"

print(example[0])

print(example[6:])

print(example[-1])

print(len(example))

print(example.count("r"))
"""
