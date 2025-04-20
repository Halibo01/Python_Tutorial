# pillow_tutorial.py

# ===============================
# Python Pillow (PIL) Eğitimi 😊
# ===============================

# Pillow, Python'da resim işleme yapmak için kullanılan güçlü bir kütüphanedir.

# Önce Pillow kütüphanesini içe aktaralım.
from PIL import Image, ImageFilter, ImageDraw, ImageFont

# ----------------------------------
# 1. Görüntü Açma ve Gösterme
# ----------------------------------
# Bir resmi açmak için Image.open() kullanılır.
img = Image.open("ornek_resim.jpg")  # Bu dosya dizininde olmalı
"""
img.show()  # Resmi varsayılan görüntüleyici ile açar
"""
# ----------------------------------
# 2. Resim Boyutunu ve Formatını Görüntüleme
# ----------------------------------
"""
print("Boyut:", img.size)      # (genişlik, yükseklik)
print("Format:", img.format)  # Örneğin: JPEG, PNG
"""
# ----------------------------------
# 3. Yeniden Boyutlandırma
# ----------------------------------
# resize() fonksiyonu ile yeni boyut verilir
"""
resized_img = img.resize((200, 200))
resized_img.show()  # Yeni boyutlu resmi kaydet
"""
# ----------------------------------
# 4. Kırpma (Cropping)
# ----------------------------------
# (sol, üst, sağ, alt) koordinatları ile kırpılır
"""
crop_img = img.crop((100, 100, 400, 400))
crop_img.show()
"""
# ----------------------------------
# 5. Döndürme (Rotate) ve Çevirme (Flip)
# ----------------------------------
"""
rotated = img.rotate(90)  # Saat yönünün tersine 90 derece döndür
rotated.show()

flipped = img.transpose(Image.FLIP_LEFT_RIGHT)  # Aynalama
flipped.show()
"""
# ----------------------------------
# 6. Filtre Ekleme
# ----------------------------------
# ImageFilter modülü ile filtre uygulanabilir
"""
blurred = img.filter(ImageFilter.BLUR)
blurred.show()
"""
# ----------------------------------
# 7. Üzerine Yazı Yazma
# ----------------------------------
"""
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()  # Basit bir font
draw.text((50, 50), "Merhaba PIL!", fill="red", font=font)
img.show()
"""
# ----------------------------------
# 8. Yeni Görüntü Oluşturma
# ----------------------------------
# Yeni boş bir resim oluşturalım (RGB, beyaz arka plan)
"""
new_img = Image.new("RGB", (300, 300), "white")
draw = ImageDraw.Draw(new_img)
draw.rectangle([50, 50, 250, 250], fill="blue")  # Mavi bir kare çiz
new_img.show()
"""
# ----------------------------------
# 9. Görüntüyü Gri Tonlamaya Dönüştürme
# ----------------------------------
"""
gray_img = img.convert("L")  # 'L' modu gri tonlama için kullanılır
gray_img.show()
"""
# ----------------------------------
# 10. Piksel Verilerine Erişim
# ----------------------------------
# getpixel() ile belirli bir pikselin rengini alabiliriz
"""
renk = img.getpixel((10, 10))
print("10,10 pikselinin rengi:", renk)
"""
# ===============================
# Pillow ile temel işlemler bu kadar! 😊
# Daha fazlası için: https://pillow.readthedocs.io
# ===============================