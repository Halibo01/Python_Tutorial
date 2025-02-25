# Başlangıçtaki string
string = "    öRnEk sTrInG    "

# Tüm harfleri büyük yapar
string = string.upper()  
print(string)  # Çıktı: "    ÖRNEK STRING    "

# Tüm harfleri küçük yapar
string = string.lower()  
print(string)  # Çıktı: "    örnek string    "

# Başındaki ve sonundaki boşlukları kaldırır
string = string.strip()  
print(string)  # Çıktı: "örnek string"

# İlk harfi büyük yapar, geri kalan harfleri küçük tutar
string = string.capitalize()  
print(string)  # Çıktı: "Örnek string"

# "string" kelimesini "yazı" kelimesiyle değiştirir
string = string.replace("string", "yazı")  
print(string)  # Çıktı: "Örnek yazı"

# Stringin sonuna " örnek text" ekler
string += " örnek text"  
print(string)  # Çıktı: "Örnek yazı örnek text"

# "örnek text" stringini, mevcut stringin başına ekler
string = "örnek text" + string  
print(string)  # Çıktı: "örnek textÖrnek yazı örnek text"

# Stringin uzunluğunu döndürür 
print(len(string))  # Çıktı: 34 (Çünkü toplamda 34 karakter vardır)


# Çıktıları yazdırma

# Fonksiyonla yazdırma
print("fonksiyonla yazdırma:", string)

# Formatlayarak yazdırma
print(f"formatlanan yazı: {string}")

# Formatlamaya alternatif
print("formatlanan yazı: {}".format(string))

# Ekleme yaparak yazdırma
print("ekleyerek yazdırma:" + string)

