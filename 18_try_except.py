# Pythonda Hata Yakalama
# Python'da 'try' ve 'except' yapıları, hata yönetimi (exception handling) için kullanılır.
# Bu yapı sayesinde, bir hata meydana geldiğinde program çökmeden hatayı yakalayabiliriz.
# Hatalar yakalanabilir ve gerektiğinde işlem yapılabilir.
# 'try' bloğunun içinde gerçekleşen hatalar exception dediğimiz 'except' bloğuna aktarılır ve böylece kod durmadan kaldığı yerden çalışmaya devam eder.
"""
try:
    # Kullanıcıdan bir sayı alıyoruz
    sayi = int(input("Bir sayı girin: "))  # Kullanıcıdan sayı girmesini istiyoruz
    print(f"Girdiğiniz sayı: {sayi}")  # Girilen sayıyı ekrana yazdırıyoruz

except:
    # Eğer kullanıcı geçersiz bir değer girerse (örneğin metin), burada hata yakalanır
    print("Hata: Lütfen geçerli bir sayı girin!")  # Kullanıcıya hata mesajı gösteriyoruz
"""

# Hatalar direkt olarak tek bir hata bloğuna yönlendirilebilir.
# Bununla beraber hatalar spesifik olarak yakalanabilir ve bu sayede kod çalışmaya devam ederken kullanıcıya hata mesajı verilebilir.
# 'finally' bloğu 'try' ve 'except' bloklarından bağımsız olarak her daim çalışmayı sürdüren bloklardır. 
"""
try:
    # Burada, hata meydana gelebilecek kodu yazıyoruz.
    sayi1 = int(input("Birinci sayıyı girin: "))  # Kullanıcıdan bir sayı alınır.
    sayi2 = int(input("İkinci sayıyı girin: "))  # Kullanıcıdan başka bir sayı alınır.
    sonuc = sayi1 / sayi2  # Sayıları böleriz.
    print(f"Sonuç: {sonuc}")  # Sonucu ekrana yazdırırız.

except ZeroDivisionError:
    # 'ZeroDivisionError' hatası, sıfıra bölme yapılmaya çalışıldığında meydana gelir.
    # Bu hatayı yakalayarak, kullanıcıya anlamlı bir mesaj verebiliriz.
    print("Hata: Sıfıra bölme yapamazsınız!")  # Hata mesajını kullanıcıya gösteririz.

except ValueError:
    # 'ValueError' hatası, kullanıcı geçersiz bir değer girdiğinde meydana gelir.
    # Örneğin, bir string değeri sayıya dönüştürmeye çalıştığınızda bu hata alınır.
    print("Hata: Geçersiz giriş! Lütfen sayılar girin.")  # Hata mesajını kullanıcıya gösteririz.

except Exception as e:
    # 'Exception' sınıfı, yukarıdaki belirli hatalar dışında kalan tüm hata türlerini yakalar.
    # Burada, herhangi bir beklenmeyen hatayı yakalamak için kullanılır.
    print(f"Beklenmeyen bir hata oluştu: {e}")  # Hata mesajını ekrana yazdırırız.

finally:
    # 'finally' bloğu, hata olup olmamasına bakmaksızın her durumda çalışır.
    # Bu, örneğin dosya kapama, kaynak temizleme gibi işlemler için kullanılır.
    print("İşlem tamamlandı.")  # Bu mesaj her durumda yazdırılır.
"""

# Karşılaştığınızda yazabileceğiniz hata yakalama türleri:
# ZeroDivisionError: Sıfıra bölme hatası.
# ValueError: Geçersiz bir tür dönüşümü hatası (örneğin string'i sayıya dönüştürme hatası).
# IndexError: Geçersiz bir liste veya dizin erişimi.
# KeyError: Sözlükte olmayan bir anahtara erişim.
# FileNotFoundError: Dosya bulunamadığında oluşur.
# TypeError: Uygunsuz veri tipi hatası.
# AttributeError: Mevcut olmayan bir özellik veya metoda erişim hatası.
# ImportError: Modül veya fonksiyon yüklenemediğinde oluşur.
# OSError: Genel dosya sistemi veya işletim sistemi hatası.
# MemoryError: Yetersiz bellek hatası.
# NotImplementedError: Bir fonksiyon veya metodun henüz uygulanmadığını belirtir.
# OverflowError: Bir sayının çok büyük olduğunda oluşur.
# AssertionError: assert ifadesi sağlanmadığında oluşur.
# UnicodeEncodeError: Unicode karakterlerini doğru bir şekilde kodlarken meydana gelen hata.
# UnicodeDecodeError: Byte dizisini Unicode'a dönüştürürken meydana gelen hata.
# StopIteration: Bir iterator sona erdiğinde bu hata fırlatılır.