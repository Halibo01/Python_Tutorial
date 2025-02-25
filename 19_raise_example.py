# raise Kullanımı - Python'da Hata Fırlatma

# `raise` ifadesi, programın belirli bir durumda hata fırlatmasını sağlamak için kullanılır.
# Bu, özel durumları kontrol etmek veya belirli koşullarda programın çalışmasını durdurmak için kullanılabilir.
# Try-catch'den farklı olarak hataları yakalamak yerine kod için özel hatalar üretir ve kod parçasını durdurur.


# Basit bir raise örneği

def bolme_islemi(a, b):
    
    # a sayısını b sayısına böler.
    # Eğer b sıfır ise ZeroDivisionError fırlatır.
    
    if b == 0:
        raise ZeroDivisionError("Bir sayı sıfıra bölünemez!")
    return a / b

# Örnek olarak hatayı görebilmek için aşağıdaki kodu çalıştırınız:
"""
bolme_islemi(5, 0) # Bölen sayı 0 olduğu için kod hata verir
"""




# Hata fırlatma örneği
def yas_kontrol(yas):
    
    # Eğer yaş 18'den küçükse ValueError fırlatır.
    
    if yas < 18: # if blokları ile yazılır.
        raise ValueError("Yaş 18'den küçük olamaz!") # Herhangi bir hata örnek olarak yazılabilir.
    return "Giriş başarılı!"
# Aşağıdaki yorum satırından çıkartarak kodu çalıştırınız
"""
print(yas_kontrol(17)) # Sayı 17 den küçük olduğu için kod hata verir
"""



# Özel hata türü oluşturma

class OzellestirilmisHata(Exception):
    
    # Kullanıcı tanımlı özel bir hata sınıfı.
    
    pass

def ozellestirilmis_hata_ornegi():
    
    # Belirli bir durum oluştuğunda özel hata fırlatır.
    
    raise OzellestirilmisHata("Bu özel bir hata mesajıdır!")
# Yukarıdaki fonksiyonu çağırmak için aşağıdaki kodu yorum satırından çıkartınız.
"""
ozellestirilmis_hata_ornegi()
"""



# try-except ile raise kullanımı
# try-except ile raise ile oluşturulan hatalar yakalanabilir böylece özel olarak oluşturulan hatalar başka kodlar tarafından önemsenmeyebilir.

def try_except_ornegi():
    
    # Raise edilen hatayı yakalamak için try-except bloğu kullanımı.
    
    try:
        bolme_islemi(10, 0)
    except ZeroDivisionError as e:
        print(f"Hata yakalandı: {e}") # e değişkeni hata mesajının string olarak çıktı alınmış halidir.
"""
try_except_ornegi()
"""



# Örnek çağırmalar
"""
try:
    print(yas_kontrol(16))
except ValueError as e:
    print(f"Hata: {e}")

try:
    ozellestirilmis_hata_ornegi()
except OzellestirilmisHata as e:
    print(f"Özel hata yakalandı: {e}")
"""