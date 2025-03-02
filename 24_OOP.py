# Python Nesne Yönelimli Programlama (OOP) 
# 
# OOP, kodun daha düzenli ve tekrar kullanılabilir olmasını sağlayan bir programlama paradigmasıdır.
# Python'da OOP'nin temel bileşenleri: 
# - Sınıflar (Classes) 
# - Nesneler (Objects) 
# - Kapsülleme (Encapsulation) 
# - Miras Alma (Inheritance) 
# - Çok Biçimlilik (Polymorphism) 
# - Özel Hata Sınıfları (Custom Exceptions)
# - Özel Metotlar (Special Methods)
# - İteratörler (Iterators)

# Basit bir sınıf tanımlayalım.
class Person:
    # Bu sınıf bir kişinin adını ve yaşını saklar.
    def __init__(self, name, age):
        # Kurucu metod: Nesne oluşturulduğunda çalışır.
        self.name = name  # Nesne değişkeni (attribute)
        self.age = age
    
    def introduce(self):
        # Kişinin adını ve yaşını yazdırır.
        print(f"Merhaba, ben {self.name} ve {self.age} yaşındayım.")

# Nesne oluşturalım.
p1 = Person("Halil", 22)
p1.introduce()






# Miras Alma (Inheritance) 
class Student(Person):
    # Person sınıfından türetilmiş bir öğrenci sınıfı.
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Üst sınıfın kurucusunu çağırıyoruz.
        self.student_id = student_id
    
    def introduce(self):
        # Kendi metodunu ezerek öğrenci bilgilerini ekler.
        print(f"Ben {self.name}, {self.age} yaşındayım ve öğrenci numaram {self.student_id}.")

s1 = Student("Ayşe", 20, "12345")
s1.introduce()





# Kapsülleme (Encapsulation) 
class BankAccount:
    # Bankadaki bir hesabı temsil eden sınıf.
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Çift alt çizgi ile gizli değişken
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} TL yatırıldı. Yeni bakiye: {self.__balance} TL")
    
    def get_balance(self):
        return self.__balance

acc = BankAccount("Halil", 1000)
acc.deposit(500)
print(f"Bakiye: {acc.get_balance()} TL")





# Çok Biçimlilik (Polymorphism) 
class Dog:
    def make_sound(self):
        print("Hav hav!")

class Cat:
    def make_sound(self):
        print("Miyav miyav!")

def animal_sound(animal):
    animal.make_sound()

d = Dog()
c = Cat()
animal_sound(d)
animal_sound(c)




# Özel Hata Sınıfı (Custom Exception) 
class NegativeBalanceError(Exception):
    def __init__(self, balance, message="Bakiye negatif olamaz!"):
        self.balance = balance
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message} - Mevcut Bakiye: {self.balance} TL"

class SecureBankAccount(BankAccount):
    def withdraw(self, amount):
        if self._BankAccount__balance - amount < 0:
            raise NegativeBalanceError(self._BankAccount__balance)
        self._BankAccount__balance -= amount
        print(f"{amount} TL çekildi. Yeni bakiye: {self._BankAccount__balance} TL")

try:
    acc2 = SecureBankAccount("Mehmet", 500)
    acc2.withdraw(600)
except NegativeBalanceError as e:
    print(e)

# Özel Metotlar (Special Methods) 
class CustomClass:
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return f"CustomClass içeriği: {self.data}"
    
    def __len__(self):
        return len(self.data)
    
    def __call__(self, value):
        print(f"Nesne çağrıldı! Değer: {value}")

obj = CustomClass("Python OOP")
print(obj)
print(len(obj))
obj("Özel metodlar")

# İteratörler (Iterators) 
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

my_iter = MyIterator(1, 5)
for num in my_iter:
    print(num)

# Sonuç: 
# - OOP, kodu düzenli ve tekrar kullanılabilir hale getirir. 
# - Sınıflar ve nesnelerle çalışarak veriyi daha iyi yönetebiliriz. 
# - Miras alma, kapsülleme ve çok biçimlilik sayesinde kod daha esnek hale gelir. 
# - Özel hata sınıfları, hata yönetimini daha kontrollü ve okunabilir hale getirir.
# - Özel metotlar, nesneleri daha işlevsel hale getirir.
# - İteratörler, özel veri yapıları oluşturmak için kullanılır.
