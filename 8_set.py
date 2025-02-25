# *** SET ÖZELLİKLERİ ***

# Set sırasız ve tekrarsız elemanlardan oluşur
ornek_set = {1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,10,10,10,10,10,10,10,10}
"""
# Tekrarlayan elemanlar otomatik olarak kaldırılır
print(ornek_set)  # {1, 2, 3, 4, 5} tüm sayılardan yalnızca bir tane kalır

# Eleman ekleme ve çıkarma işlemleri
ornek_set.add(6)  # 6 elemanını sete ekler
print(ornek_set)  # {1, 2, 3, 4, 5, 6}
ornek_set.remove(3)  # 3 elemanını setten çıkarır
print(ornek_set)  # {1, 2, 4, 5, 6}
ornek_set.discard(10)  # 10 elemanı yoksa hata vermez
ornek_set.pop()  # Rastgele bir eleman çıkarır
print(ornek_set)
"""


# Kümeler arası işlemler

"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))  # Birleşim: {1, 2, 3, 4, 5}
print(set1.intersection(set2))  # Kesişim: {3}
print(set1.difference(set2))  # Fark: {1, 2}
print(set1.symmetric_difference(set2))  # Simetrik fark: {1, 2, 4, 5}
"""


# Eleman kontrolü ve uzunluk

"""
print(2 in ornek_set)  # True: 2 elemanı set1 içinde var
print(len(ornek_set))  # Ornek_set'in eleman sayısı: 10
"""

# Set'lerin listelere ve tuple'lara dönüştürülmesi
"""
ornek_set = {7, 8, 9}
ornek_tuple = tuple(ornek_set)  # Set'ten tuple'a dönüşüm
print(ornek_liste)  # (7, 8, 9)
ornek_liste = list(ornek_set)  # Set'ten listeye dönüşüm
print(ornek_tuple)  # [7, 8, 9]
ornek_liste.append(9)
print(ornek_liste) # [7, 8, 9, 9]
ornek_set = set(ornek_liste) # Listenin Set'e dönüştürülmesi
print(ornek_set) # {7, 8, 9} Tekrarlı sayılar yazılmaz
ornek_liste = list(ornek_set) # Set'ten listeye dönüştürülmesi
print(ornek_liste) # [7, 8, 9]
"""

