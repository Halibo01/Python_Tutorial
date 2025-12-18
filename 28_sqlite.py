# ====================================================
# SQLite ile Python Kullanımı - Detaylı Anlatım
# ====================================================

# sqlite3 modülü, Python ile birlikte gelen yerleşik bir veritabanı modülüdür.
# Harici bir kütüphane yüklemeye gerek yoktur.
import sqlite3

# --------------------------------------
# 1. Veritabanına Bağlanma / Oluşturma
# --------------------------------------

# Aşağıdaki kod, "okul.db" adında bir veritabanı dosyası oluşturur (eğer yoksa)
# Bu dosya aynı dizine kaydedilir. Eğer varsa, o dosyaya bağlanır.
conn = sqlite3.connect("28_sqlite/okul.db")

# SQL komutlarını çalıştırmak için bir cursor (imleç) oluşturuyoruz
cursor = conn.cursor()

# --------------------------------------
# 2. Tablo Oluşturma
# --------------------------------------

# Öğrenciler adlı bir tablo oluşturuyoruz.
# IF NOT EXISTS ifadesi, tablo daha önce oluşturulmuşsa hata verilmesini engeller.

cursor.execute("""
CREATE TABLE IF NOT EXISTS ogrenciler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Her öğrenci için benzersiz bir ID (otomatik artar)
    ad TEXT NOT NULL,                       -- Öğrencinin adı (boş bırakılamaz)
    soyad TEXT,                             -- Öğrencinin soyadı
    yas INTEGER                             -- Öğrencinin yaşı
)sq
""")

# --------------------------------------
# 3. Veri Ekleme (INSERT)
# --------------------------------------

# Örnek öğrenci verilerini tabloya ekleyelim
"""
cursor.execute("INSERT INTO ogrenciler (ad, soyad, yas) VALUES (?, ?, ?)", ("Ali", "Yılmaz", 20))
cursor.execute("INSERT INTO ogrenciler (ad, soyad, yas) VALUES (?, ?, ?)", ("Zeynep", "Demir", 21))
cursor.execute("INSERT INTO ogrenciler (ad, soyad, yas) VALUES (?, ?, ?)", ("Mehmet", "Kara", 22))

# Değişiklikleri veritabanına kaydetmeyi unutma
conn.commit()
"""
# --------------------------------------
# 4. Veri Listeleme (SELECT)
# --------------------------------------

# Tüm öğrencileri çekelim
"""
cursor.execute("SELECT * FROM ogrenciler")
ogrenciler = cursor.fetchall()  # fetchall() tüm sonuçları liste olarak getirir

# Öğrencileri ekrana yazdıralım
print("=== Tüm Öğrenciler ===")
for ogrenci in ogrenciler:
    print(ogrenci)
"""

# --------------------------------------
# 5. Filtreli Sorgulama
# --------------------------------------

# Yaşı 21 ve üstü olan öğrencileri çekelim
"""
cursor.execute("SELECT ad, soyad FROM ogrenciler WHERE yas >= ?", (21,))
sonuclar = cursor.fetchall()
print("\n21 yaş ve üzeri öğrenciler:")
for s in sonuclar:
    print(s)
"""

# --------------------------------------
# 6. Veri Güncelleme (UPDATE)
# --------------------------------------

# Ali'nin yaşını 23 olarak güncelleyelim
"""
cursor.execute("UPDATE ogrenciler SET yas = ? WHERE ad = ?", (23, "Ali"))
conn.commit()
"""

# --------------------------------------
# 7. Veri Silme (DELETE)
# --------------------------------------

# Mehmet adlı öğrenciyi silelim
"""
cursor.execute("DELETE FROM ogrenciler WHERE ad = ?", ("Mehmet",))
conn.commit()
"""

# --------------------------------------
# 8. fetchone() Kullanımı
# --------------------------------------

# İlk öğrenci kaydını çekmek için fetchone() kullanılır
"""
cursor.execute("SELECT * FROM ogrenciler")
ilk_kayit = cursor.fetchone()  # İlk kaydı getirir
print("\nİlk öğrenci kaydı:")
print(ilk_kayit)
"""

# --------------------------------------
# 9. fetchmany() Kullanımı
# --------------------------------------

# Belirli sayıda kayıt çekmek için fetchmany(n) kullanılır
"""
cursor.execute("SELECT * FROM ogrenciler")
iki_kayit = cursor.fetchmany(2)  # İlk iki kaydı getirir
print("\nİlk iki öğrenci:")
for k in iki_kayit:
    print(k)
"""

# --------------------------------------
# 10. executemany() Kullanımı
# --------------------------------------

# Birden fazla veriyi tek seferde eklemek için executemany() kullanılır
"""
coklu_ogrenciler = [
    ("Deniz", "Aydın", 19),
    ("Selim", "Koç", 22),
    ("Elif", "Aksoy", 20)
]
cursor.executemany("INSERT INTO ogrenciler (ad, soyad, yas) VALUES (?, ?, ?)", coklu_ogrenciler)
conn.commit()
"""

# --------------------------------------
# 11. Güvenlik Notu
# --------------------------------------

# SQL sorgularında kullanıcıdan alınan verileri doğrudan string olarak eklemek SQL Injection'a yol açabilir.
# Bu yüzden değerleri daima ? sembolüyle parametre olarak geçmeliyiz (yukarıdaki gibi).

# --------------------------------------
# 12. Bağlantıyı Kapatma
# --------------------------------------

# Tüm işlemler bittiğinde veritabanı bağlantısını kapatmalıyız.
conn.close()
