# Python Tip Anotasyonları (Type Annotations)
# 
# Tip anotasyonları, Python'da değişkenlerin, fonksiyon parametrelerinin ve dönüş değerlerinin hangi türde olması gerektiğini belirtir.
# Tip anotasyonları zorunlu değildir, ancak kodun okunabilirliğini artırır ve statik analiz araçlarının hataları tespit etmesine yardımcı olur.

# Basit Tip Anotasyonları
# C / C++ formatı:
# C++ --> string name = "Halil" 
# C   --> char String[] "Halil"
# int age = 22
# float height = 1.75
# bool is_student = true


# Python formatı alternatif tip belirleme:
name: str = "Halil"         # Değişkenin string olduğunu belirtir
age: int = 22               # Değişkenin tamsayı olduğunu belirtir
height: float = 1.75        # Değişkenin ondalıklı olduğunu belirtir
is_student: bool = True     # Değişkenin boolean olduğunu belirtir




# Fonksiyonlarda Tip Anotasyonları
def add(x: int, y: int) -> int:  # Fonksiyona verilen x ve y argümanının tam sayı değer olması gerektiğini söyler.
                                 # Çıktı olarak ise integer verdiğini söyler (herhangi bir şey yazılmadığında python kendisi bu değeri söyler)
    # İki tam sayıyı toplar ve sonucu döndürür.
    return x + y

result: int = add(5, 3)  # <--- Mouse'unuzu 'add' fonksiyonun üstüne getirdiğinizde argümanların olması gereken tipini görebilirsiniz.
print(result)




# Listeler ve Sözlüklerde Tip Anotasyonları

numbers: list[int] = [1, 2, 3, 4, 5] # Sayı listesi olduğunu belirtir
info: dict[str, int] = {"age": 22, "year": 2024} # {string : tamsayı} formatında dictionary olduğunu belirtir





# Birden Fazla Tipi Desteklemek (Union)

def process_value(value: int | str) -> str: # Argümanın tam sayı ve string değerde verilebileceğini söyler. Çıktı olarak string verdiğini söyler.
    # Değer tam sayıysa, iki katını döndürür, string ise büyük harfe çevirir.
    if type(value) == int:
        return str(value * 2)
    return value.upper()

print(process_value(10))        # Çıktı: 20
print(process_value("python"))  # Çıktı: PYTHON




# İsteğe Bağlı Parametreler (Optional)

def greet(name: str | None = None) -> str: # String değeri yazılabileceğini söyler. Eğer herhangi bir değer yazılmazsa değerin standart olarak None girileceğini söyler.
    # Eğer isim verilmezse, varsayılan selamlamayı kullanır.
    return f"Merhaba, {name if name else 'Ziyaretçi'}!"

print(greet())
print(greet("Ayşe"))




# Özel Sınıflar İçin Tip Anotasyonları
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def introduce(self) -> str:
        return f"Benim adım {self.name} ve {self.age} yaşındayım."

p: Person = Person("Halil", 22)
print(p.introduce())




# İteratörler ve Generatörler İçin Tip Anotasyonları
from typing import Iterator # Bunun için typing kütüphanesi import edilmelidir.

def number_generator(n: int) -> Iterator[int]: # Girdi olarak bir tam sayı ve çıktı olarak bir iteratör/generatör döndürdüğünü söyler
    for i in range(n):
        yield i

for num in number_generator(5): # Çıktı olarak almak için bu şekilde kullanılabilir.
    print(num)

liste = list(number_generator(5)) # Tüm çıktıları bir liste halinde alabilmek için bu şekilde kullanılabilir
print(liste)


    

# Çağrılabilir Tipler (Callable)
from typing import Callable

def execute_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    # Herhangi bir 2 argümanı tam sayı girilebilecek ve çıktı olarak tam sayı verebilecek bir fonksiyonun fonksiyon içinde olması gerektiğini söyler.
    return func(a, b)

print(execute_function(add, 10, 20))

# Sonuç:
# - Tip anotasyonları, kodun daha okunaklı olmasını sağlar.
# - Statik analiz araçları ile hataları önceden tespit etmemize yardımcı olur.
# - Listeler, sözlükler, union, optional ve callable gibi gelişmiş tipleri destekler.
# - Büyük projelerde hata oranını azaltarak kod bakımını kolaylaştırır.
