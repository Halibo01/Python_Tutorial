
# Python Decorators (Dekoratörler) 

# Dekoratörler, bir fonksiyonun veya metodun davranışını değiştirmek için kullanılan Python özellikleridir. 
# Genellikle kod tekrarını azaltmak ve fonksiyonlara ek işlevsellik kazandırmak için kullanılırlar. 


# Basit bir dekoratör tanımlayalım.
def my_decorator(func):
    
    # Bu dekoratör, fonksiyon çağrılmadan önce ve sonra bir mesaj yazdırır.
    
    def wrapper():
        print("Fonksiyon çağrılmadan önce çalışıyorum.")
        func()
        print("Fonksiyon çağrıldıktan sonra çalışıyorum.")
    return wrapper

# Dekoratörü bir fonksiyona uygulayalım.

@my_decorator
def say_hello():
    # Basit bir selamlama fonksiyonu.
    print("Merhaba!")

# Fonksiyonu çağıralım.
"""
say_hello()
"""
 
# Parametre Alan Dekoratörler 
# Dekoratörler, parametre alan fonksiyonlarla da kullanılabilir.

def repeat(n):
    
    # Bu dekoratör, süslediği fonksiyonu n kez çalıştırır.
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    # Verilen ismi selamlayan fonksiyon.
    print(f"Merhaba, {name}!")
"""
greet("Halil")
"""


 
# Birden Fazla Dekoratör Kullanımı 
# Bir fonksiyona birden fazla dekoratör eklenebilir. 


@repeat(2)
@my_decorator
def test():
    print("Test fonksiyonu çalışıyor!")
"""
test()
"""

# Sonuç: 
# - Dekoratörler fonksiyonları değiştirmeden, onları süsleyerek ek işlevler kazandırır. 
# - Parametre alabilen, sınıf tabanlı veya iç içe geçmiş dekoratörler tanımlanabilir. 
# - Birden fazla dekoratör aynı fonksiyona uygulanabilir. 

