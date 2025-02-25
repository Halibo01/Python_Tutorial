# Dosya İşlemleri
# Python'da dosya işlemleri için "open()" fonksiyonu kullanılır.
# Dosyalar genellikle "r" (okuma), "w" (yazma), "a" (ekleme) ve "x" (oluşturma) modlarında açılabilir.

# 1. Dosya Açma ve Yazma
# "w" modu dosya yoksa yeni bir dosya oluşturur.
# Eğer dosya zaten varsa, içeriğini tamamen silerek sıfırdan yazmaya başlar.
# Yani var olan veriler korunmaz, dosyanın içeriği tamamen yenilenir.
# "close()" satırı dosyayı kapatmak ve yapılan değişiklikleri kaydetmek için kullanılır.
# Kapatma işlemi kod için şarttır. Kapanmayan dosyalar bellekte veri kaplar.
"""
dosya = open("ornek.txt", "w")
dosya.write("Merhaba, bu bir dosya işlemi örneğidir.\n")
dosya.write("Python ile dosya işlemleri oldukça kolaydır.\n")
dosya.close()
"""

# 2. Dosya Okuma
# "r" modu dosyayı okuma modunda açar. Dosya yoksa hata verir.
# Varolmayan dosyada bir işlem yapamaz veya yeni dosya oluşturamaz. Bu komut için python dosyasıyla aynı konumda dosyanın bulunması gerekir.
"""
dosya = open("ornek.txt", "r")
icerik = dosya.read()  # Tüm içeriği okur
dosya.close()
print("Dosya İçeriği:\n", icerik)
"""

# 3. Satır Satır Okuma
# "readlines()" fonksiyonu ile tüm satırları liste olarak alabiliriz.
"""
dosya = open("ornek.txt", "r")
satirlar = dosya.readlines()  # Her satırı bir liste elemanı olarak döndürür
dosya.close()
print(satirlar)
for satir in satirlar:
    print("Satır:", satir.strip())  # "strip()" ile gereksiz boşlukları kaldırıyoruz
"""

# 4. With Kullanımı
# "with" bloğu kullanıldığında dosya işlemi tamamlandığında dosya otomatik olarak kapatılır.
# "close()" çağırmaya gerek kalmaz. Bu, dosya kapanmasını unutmamak için güvenli bir yöntemdir.
"""
with open("ornek.txt", "r") as dosya:
    icerik = dosya.read()
    print("With ile Okunan İçerik:\n", icerik)
"""

# 5. Dosyaya Veri Ekleme
# "a" modu, dosyanın sonuna veri ekler, önceki verileri silmez. Böylelikle veri eklemeye devam eder.
"""
with open("ornek.txt", "a") as dosya:
    dosya.write("Bu satır dosyanın sonuna eklendi.\n")
"""

# 6. "r+" Modu Kullanımı (Okuma ve Yazma)
# "r+" hem okuma hem de yazma işlemleri için kullanılır.
# Dosya başından itibaren yazma yapar ve var olan içeriğin üzerine yazabilir.
# Eğer dosya yoksa hata verir.
"""
with open("ornek.txt", "r+") as dosya:
    mevcut_icerik = dosya.read()  # Mevcut içeriği oku
    dosya.seek(0)  # Dosyanın başına git
    dosya.write("Dosyanın başına bu satır eklendi.\n")  # Üzerine yazma işlemi yap
    dosya.write(mevcut_icerik)  # Önceki içeriği koru ve yeniden yaz
"""

# "r+" modunda seek(0) kullanmazsak, yeni yazılan veri mevcut verinin üzerine gelebilir.