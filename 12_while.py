# while döngüsü, belirli bir koşul sağlandığı sürece çalışmaya devam eder.
# Koşul True olduğu sürece döngü sürekli çalışır, False olduğu zaman döngü sona erer.

# Basit string ifadesiyle bir örnek:
"""
my_string = "halil hasan hüseyin yusuf"

while "hasan" in my_string:  # "hasan" string içinde bulunduğu sürece devam et
    # Stringin son karakterini siliyoruz ve yeni değer olarak atıyoruz
    my_string = my_string[:-1]
    
    # Her bir silmeden sonra güncel stringi yazdırıyoruz
    print(f"Sonraki hal: {my_string}")

# Eğer "hasan" kelimesi bulunmadığında, döngü otomatik olarak sonlanacaktır.
print(f"Son hal: {my_string}")
"""


# Basit bir örnek: 0'dan 4'e kadar olan sayıları yazdıran bir while döngüsü
"""
i = 0
while i < 5:  # i değişkeni 5'ten küçük olduğu sürece döngü devam eder
    print(i)  # i'nin değerini yazdırır
    i += 1  # i'yi her döngüde 1 artırır (bu, sonsuz döngüye girmemek için önemlidir)
# Çıktı:
# 0
# 1
# 2
# 3
# 4
"""

# Koşul False olduğunda döngü sonlanır. Örneğin, i 5'e ulaşınca döngü durur.
# i >= 5 olduğunda while döngüsü sona erer.

# while döngüsünde sonsuz döngü de oluşturulabilir, ancak dikkatli olmalıyız
# Aşağıdaki örnekte sonsuz döngü bulunmakta, kullanıcı bu döngüyü manuel olarak durdurmak zorunda kalabilir.
# Sonsuz döngüde dikkat edilmesi gereken şey, döngüye son vermek için bir çıkış koşulu veya break ifadesi eklememiz gerektiğidir.

# Sonsuz döngü örneği:
# while True:
#     print("Bu bir sonsuz döngüdür.")  
#     # Bu döngü manuel olarak durdurulmadığı sürece devam eder

# NOT!: Eğer sonsuz döngüye girdiyseniz terminal kısmına mouse ile basıp ctrl+c yaparak programı manuel olarak kapatabilirsiniz

# Bunun dışında sonsuz döngüye nasıl son verilir?
# break ifadesiyle döngü herhangi bir anda sonlandırılabilir.

"""
i = 0
while True:  # Sonsuz döngü başlatıyoruz
    print(i)  # i'yi yazdır
    i += 1  # i'yi 1 artır
    if i >= 5:  # i 5'e ulaştığında döngüyü bitir
        break  # break komutu döngüyü sonlandırır
# Çıktı:
# 0
# 1
# 2
# 3
# 4
"""


# continue ifadesi ile döngüde bir adımı atlayabiliriz
# continue ifadesi, bir döngüde şu anki iterasyonu atlar ve bir sonraki iterasyona geçer.
"""
i = 0
while i < 5:
    i += 1  # i'yi artırıyoruz
    if i == 3:
        continue  # i 3 olduğunda, şu anki iterasyonu atlar ve bir sonraki iterasyona geçer
    print(i)  # i'yi yazdır
# Çıktı:
# 1
# 2
# 4
# 5
# Bu örnekte, 3 yazdırılmayacak çünkü 3'e geldiğinde continue ile o iterasyon atlanacak.
"""
