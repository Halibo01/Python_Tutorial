# Temel Veri Tipleri Örnekleri
x = 5          # int
y = 3.14       # float
name = "Halil" # str
items = [1, 2, 3]  # list
diction = {"isim": "halil"}
"""
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(name))  # <class 'str'>
print(type(items))  # <class 'list'>
print(type(diction)) # <class 'dict'>
"""


"""
print(type(x) == int)
print(type(y) == float)
print(type(name) == str)
print(type(items) == list)
print(type(diction) == dict)
"""

# bazı elemanlar başka sınıflara dönüştürülebilir

print(int("80"), float("80"), "80", list("80"))
