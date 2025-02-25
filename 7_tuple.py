# tuple ifadeleri bu şekilde ifade edilebilir
ornek_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9)

# tuple ifadeleri listelere benzer yapılardır fakat listelerden farklı olarak tuple ifadelerinde değişiklik yapılamaz
"""
print(ornek_tuple[0]) # Tek bir eleman alma

print(ornek_tuple[3:6]) # Çoklu eleman alma

print(ornek_tuple.count(9)) # 9 sayısının miktarını yazdırma

print(len(ornek_tuple)) # uzunluğunu yazdırma

print(9 in ornek_tuple) # 9 ifadesinin içinde olduğunu kontrol etme (9 tuple içinde olduğu için True yazacaktır)

print(ornek_tuple.index(5)) # 5 sayısının konumunu/indexini yazdıracaktır
"""


# Tuple ifadeleri dinamik olmadığı için bu ifadelerde değişiklik yapılamaz
# Bundan dolayı aşağıdaki tüm ifadeler uyarı verecektir

"""
ornek_tuple[0] = 6 # 0. indexini 6 yapma

ornek_tuple.append(10) # 10 sayısını ekleme fonksiyonu

ornek_tuple.insert(3, 333) # 3. indexine 333 sayısını ekleme fonksiyonu

ornek_tuple.pop() # Sonunda bulunan elemanı silme

ornek_tuple.remove(1) # "1" elemanını silme
"""

# Bununla beraber Tuple ifadeleri listelere dönüştürülebilir. Aynı şekilde liste ifadeleri Tuple ifadelerine dönüştürülebilir

"""
ornek_liste = list(ornek_tuple) # Tuple ifadesini listeye dönüştürme
print(ornek_liste, type(ornek_liste))

ornek_liste.append(10) # Yeni liste ifadesine 10 ekleme

ornek_tuple = tuple(ornek_liste) # Listeyi Tuple ifadesine dönüştürme
print(ornek_tuple, type(ornek_tuple))
"""