# Random Kütüphanesi
# 'random' kütüphanesini içe aktarırız. Bu kütüphane rastgele sayılar üretmek için kullanılır.
# C++ örneği:
# #include <random>  // random sayı üretimi için
import random

# 'random.randint(a, b)' fonksiyonu, a ile b arasındaki (a ve b dahil) rastgele bir tamsayı döndürür.
"""
rastgele_sayi = random.randint(1, 10)  # 1 ile 10 arasında rastgele bir tamsayı
print(f"Rastgele sayi: {rastgele_sayi}")
"""

# 'random.choice(sequence)' fonksiyonu, verilen diziden (list, tuple, string vs.) rastgele bir öğe seçer.
"""
liste = [10, 20, 30, 40, 50]
rastgele = random.choice(liste)  # Liste içinden rastgele bir öğe seçer
print(f"Rastgele öğe: {rastgele}")
"""

# 'random.shuffle(sequence)' fonksiyonu, verilen dizinin elemanlarını rastgele karıştırır.
"""
random.shuffle(liste)  # Listeyi karıştırır
print(f"Karıştırılmış liste: {liste}")
"""

# 'random.sample(sequence, k)' fonksiyonu, verilen diziden k adet rastgele öğe seçer.
# Bu fonksiyon orijinal diziyi değiştirmez.
"""
rastgele_ogeler = random.sample(liste, 3)  # Liste içinden 3 rastgele öğe seçer
print(f"Rastgele öğeler: {rastgele_ogeler}")
"""

# 'random.uniform(a, b)' fonksiyonu, a ile b arasında rastgele bir ondalıklı sayı döndürür.
"""
rastgele_ondalik_sayi = random.uniform(1.5, 10.5)  # 1.5 ile 10.5 arasında rastgele bir ondalıklı sayı
print(f"Rastgele ondalıklı sayı: {rastgele_ondalik_sayi}")
"""