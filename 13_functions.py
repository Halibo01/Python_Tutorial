# Fonksiyonlar, belirli bir görevi yerine getiren kod bloklarıdır.
# Bir fonksiyon, genellikle bir isimle tanımlanır ve gerektiğinde o fonksiyon çağrılarak işler yapılır.

# Fonksiyon tanımlama:
# Python'da bir fonksiyon tanımlamak için 'def' anahtar kelimesi kullanılır.
# Ardından fonksiyon ismi ve parantez açılıp kapanır, fonksiyonun yapılacak işlemi
# ise girintili bir şekilde yazılır.
"""
def greet(name):
    
    # Bu fonksiyon, kendisine bir 'name' parametresi alır ve bu ismi kullanarak
    # ekrana 'Merhaba, <isim>!' şeklinde bir mesaj yazdırır.
    
    # Fonksiyon içinde yapılacak işlem:
    print(f"Merhaba, {name}!")

# Fonksiyon çağrısı:
# Tanımlanan fonksiyon, fonksiyon ismi ve parantez ile çağrılır.
# Fonksiyona bir değer (argüman) gönderilir.
greet("Halil")  # Burada "Halil" parametre olarak fonksiyona gönderilir

# Çıktı:
# Merhaba, Halil!
"""


# Fonksiyonlarda birden fazla parametre de kullanılabilir.
# Aşağıdaki örnekte iki parametreli bir fonksiyon oluşturacağız.
"""
def add_numbers(a, b):
    
    # Bu fonksiyon, iki sayıyı toplar ve sonucu döndürür.
    # 'a' ve 'b' parametreleri fonksiyona verilen iki sayıdır.
    
    return a + b  # 'return' komutuyla toplama işleminin sonucu geri döndürülür.

# Fonksiyonu çağırırken iki sayı parametre olarak gönderilir.
result = add_numbers(5, 7)  # '5' ve '7' fonksiyona gönderilir
print(result)  # Çıktı: 12
"""


# Varsayılan Parametreler:
# Fonksiyon parametrelerine varsayılan değerler de verilebilir.
# Eğer fonksiyona argüman verilmezse, varsayılan/default değerler kullanılır.
"""
def greet_person(name="Misafir"):
    
    # Bu fonksiyon, bir ismi alır ve 'Merhaba, <isim>!' mesajı verir.
    # Eğer isim verilmezse, varsayılan olarak 'Misafir' kullanılır.

    print(f"Merhaba, {name}!")

greet_person()  # "Misafir" mesajı gösterilecektir, çünkü parametre verilmedi.
greet_person("Ahmet")  # "Ahmet" mesajı gösterilecektir.

# Çıktı:
# Merhaba, Misafir!
# Merhaba, Ahmet!
"""


# Fonksiyonlardan birden fazla değer döndürme:
# Python'da bir fonksiyon birden fazla değer döndürebilir.
# Bu değerler genellikle bir tuple (demet) olarak döner.
# Demet ifadesiyle değer döndüren fonksiyonlarda değerler ayrı olarak alınabilir yada direkt demet olarak alınabilir

"""
def calculate(a, b):
    
    # Bu fonksiyon, iki sayının toplamını ve farkını döndüren bir fonksiyondur.
    
    total = a + b
    difference = a - b
    return total, difference  # İki değer döndürüyoruz.

demet = calculate(10, 5) # Fonksiyonu demet olarak alma. Çıktı: (15, 5)
print(demet)            # demeti yazdırma
print(f"Toplam: {demet[0]}, Fark: {demet[1]}")
sum_result, diff_result = calculate(10, 5)  # İki değeri birden değer olarak alıyoruz.
print(f"Toplam: {sum_result}, Fark: {diff_result}")

# Çıktı:
# (15, 5)
# Toplam: 15, Fark: 5
# Toplam: 15, Fark: 5
"""


# Fonksiyonlar, başka fonksiyonları çağırabilir,
# Bu durum, fonksiyonel programlamanın temel bir özelliğidir.
"""
def toplama(x, y) # İlk fonksiyon yazılır
    return x + y

def toplama_yapma(x, y):
    
    # Bu fonksiyon, kendisine verilen fonksiyonu (func) iki parametre ile uygular.
    
    return toplama(x, y) # Başka bir fonksiyon çağırılır

# 'multiply' fonksiyonunu 'apply_function' fonksiyonuna parametre olarak geçiriyoruz
result = toplama(3, 4)
print(result)  # Çıktı: 12
"""