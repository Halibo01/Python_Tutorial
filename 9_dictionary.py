# Dictionary, anahtar-değer (key-value) çiftleri ile veri saklar.
# Anahtarlar eşsiz olmalıdır, ancak değerler tekrarlanabilir.
ornek_dict = {"isim": "Ahmet", "yas": 25, "sehir": "Ankara"}

# 1. Dictionary elemanlarına erişim
"""
print(ornek_dict["isim"])  # "isim" anahtarının değerini döndürür: "Ahmet"
print(ornek_dict.get("yas"))  # "yas" anahtarının değerini döndürür: 25
print(ornek_dict.get("meslek", "Bilinmiyor"))  # Anahtar yoksa varsayılan değer döndürür: "Bilinmiyor"
"""

# 2. Dictionary'e yeni eleman ekleme
"""
ornek_dict["meslek"] = "Mühendis"  # Yeni bir anahtar-değer çifti eklenir
print(ornek_dict)  # {'isim': 'Ahmet', 'yas': 25, 'sehir': 'Ankara', 'meslek': 'Mühendis'}
"""

# 3. Mevcut bir değeri güncelleme
"""
ornek_dict["yas"] = 26  # "yas" anahtarının değeri güncellenir
print(ornek_dict)  # {'isim': 'Ahmet', 'yas': 26, 'sehir': 'Ankara', 'meslek': 'Mühendis'}
"""

# 4. Anahtar veya değerleri listeleme
"""
print(ornek_dict.keys())  # Anahtarları döndürür: dict_keys(['isim', 'yas', 'sehir', 'meslek'])
print(ornek_dict.values())  # Değerleri döndürür: dict_values(['Ahmet', 26, 'Ankara', 'Mühendis'])
print(ornek_dict.items())  # Anahtar-değer çiftlerini döndürür: dict_items([('isim', 'Ahmet'), ('yas', 26), ...])
"""

# 5. Anahtar kontrolü
"""
print("isim" in ornek_dict)  # True: "isim" anahtarı var
print("adres" in ornek_dict)  # False: "adres" anahtarı yok
"""

# 6. Eleman silme
"""
ornek_dict.pop("sehir")  # "sehir" anahtarını ve değerini siler
print(ornek_dict)  # {'isim': 'Ahmet', 'yas': 26, 'meslek': 'Mühendis'}
"""

# Varsayılan değerle eleman silme
"""
ornek_dict.pop("adres", "Anahtar bulunamadı")  # Anahtar yoksa hata vermez, varsayılan döner
"""
# 7. Tüm elemanları temizleme
"""
ornek_dict.clear()  # Sözlükteki tüm elemanları siler
print(ornek_dict)  # {}
"""

# 8. Yeni bir dictionary oluşturma
# a. Boş bir dictionary
bos_dict = {}
print(bos_dict)

# b. dict() kullanarak oluşturma
yeni_dict = dict(isim="Ayşe", yas=30, sehir="İstanbul")
print(yeni_dict)  # {'isim': 'Ayşe', 'yas': 30, 'sehir': 'İstanbul'}

# 9. Dictionary kopyalama
ornek_dict = {"isim": "Ali", "yas": 28}
kopya_dict = ornek_dict.copy()  # Sözlüğün bir kopyasını oluşturur
print(kopya_dict)  # {'isim': 'Ali', 'yas': 28}

# 10. Dictionary birleştirme
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)  # dict1'e dict2'nin elemanlarını ekler (var olanları günceller)
print(dict1)  # {'a': 1, 'b': 3, 'c': 4}

# 11. Dictionary anahtarlarının sırasız ve eşsiz olduğu unutulmamalıdır.
ornek_dict = {"a": 1, "b": 2, "a": 3}  # "a" anahtarı tekrarlanamaz, sonuncusu geçerli olur
print(ornek_dict)  # {'a': 3, 'b': 2}