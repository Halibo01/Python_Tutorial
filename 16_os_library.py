# Os Kütüphanesi
# 'os' kütüphanesini içe aktarırız. Bu kütüphane, işletim sistemi ile etkileşime geçmek için kullanılır.
import os

# 'os.getcwd()' fonksiyonu, geçerli çalışma dizininin (current working directory) yolunu döndürür.
# Yani şu anda Python betiğinizin çalıştığı dizini alır.
gecerli_dizin = os.getcwd()  # Geçerli çalışma dizini. Bu kodu yorum satırına eklemeyiniz.
print(f"Geçerli çalışma dizini: {gecerli_dizin}")


# 'os.listdir(path)' fonksiyonu, belirtilen dizindeki tüm dosya ve klasörlerin bir listesini döndürür.
# Eğer path verilmezse, geçerli dizini kullanır.
"""
dosya_listesi = os.listdir(gecerli_dizin)  # Geçerli dizindeki dosyaları listeler
print(f"Dizindeki dosyalar: {dosya_listesi}")
"""

# 'os.mkdir(path)' fonksiyonu, belirtilen dizinde yeni bir klasör oluşturur.
# Eğer klasör zaten varsa hata verir.
"""
os.mkdir("yeni_klasor")  # 'yeni_klasor' adında bir klasör oluşturur.
print("Yeni klasör oluşturuldu!")
"""

# 'os.makedirs' birden fazla dizin oluşturabilir
# Eğer 'ana_dizin' ve 'ana_dizin/alt_dizin' yoksa, her iki dizin de oluşturulur
"""
os.makedirs("ana_dizin/alt_dizin", exist_ok=True)  # 'ana_dizin' ve 'alt_dizin' oluşturulur. exists_ok argümanı koymamızın sebebi klasörün varlığında hata vermesini önlemek.
print("Dizinler başarıyla oluşturuldu!")
"""

# 'os.rename(src, dst)' fonksiyonu, src (kaynak) dosyasını dst (hedef) olarak yeniden adlandırır.
"""
os.rename("yeni_klasor", "yeniden_adi_verildi")  # Klasörün adını değiştirir
print("Klasör adı değiştirildi!")
"""

# 'os.remove(path)' fonksiyonu, belirtilen dosyayı siler.
# Bu işlem kalıcı olarak silme işlemi yapar, dikkatli kullanılmalıdır.
# os.remove("yeniden_adi_verildi")  # Eğer bu satırı aktif ederseniz, klasör silinir.
# Bu fonksiyonu kullanmayın yada dikkatli kullanın. Herhangi bir yanlış kullanımda bu notu yazan kişi sorumlu değildir :)

# 'os.path.exists(path)' fonksiyonu, belirtilen yolun var olup olmadığını kontrol eder.
# Eğer yol varsa True, yoksa False döner.
"""
yol_var_mi = os.path.exists("yeniden_adi_verildi")  # Yolun var olup olmadığını kontrol eder
print(f"Yol mevcut mu? {yol_var_mi}")
"""

# 'os.path.join(path1, path2, ...)' fonksiyonu, verilen yolları platform bağımsız bir şekilde birleştirir.
"""
tam_yol = os.path.join(gecerli_dizin, "yeniden_adi_verildi")  # İki yolu birleştirir
print(f"Birleşik yol: {tam_yol}")
"""

# Windows kullanan kişiler genellikle "\" kullanımında sorun yaşayabilirler çünkü bu özel karakter yazımından önce kullanıldığı için 