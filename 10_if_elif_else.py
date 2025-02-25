
a = 10
b = 0

# If örnek kullanımı
"""
if a < b:
    print("b, a dan büyüktür")
elif a > b: # C programlama dilinde else if şeklinde kullanılır fakat python da elif şeklinde kullanılır
    print("b, a dan küçüktür")
else:
    print("b ve a eşittir")
"""

# if girdiler için kolaylıkla kullanılabilir
"""
number = int(input("Sayı giriniz: "))
if 0 < number:
    print(f"{number} sayısı 0 dan büyüktür")
elif 0 > number:
    print(f"{number} sayısı 0 dan küçüktür")
else:
    print("girdiğiniz sayı 0 dır")
"""


# Bazı boş değerler False olarak ifade edilir yani bu değerler de direkt olarak if ifadelerin içinde kullanılabilir

"""
print(bool(10))
print(bool("string"))
print(bool([1, 2, 3]))
print(bool((1, 2, 3)))
print(bool({1,1,2,2,3,3}))
print(bool({"yaş": 19}))

# Dolu olan değerler True olarak ifade edilir

print("\n\n")

print(bool(0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))
"""
# Boş değerlerin hepsi False olduğu için aşağıdaki if blokları çıktı vermeyecektir

"""
if 0:
    print("sıfır")
if "":
    print("boş yazı")
if []:
    print("boş liste")
if ():
    print("boş tuple")
if {}:
    print("boş set/dictionary")
if None:
    print(None)
"""

# Dolu olan değerlerin hepsi True olarak ifade edilir

"""
if 10:  # 0 olmayan sayılar True kabul edilir (eksili ifade olsa bile)
    print("10 bir sayı ve True olarak değerlendirilir.")  # Çıktı: "10 bir sayı ve True olarak değerlendirilir."

if "string":  # Boş olmayan string'ler True kabul edilir
    print('"string" bir metin ve True olarak değerlendirilir.')  # Çıktı: '"string" bir metin ve True olarak değerlendirilir.'

if [1, 2, 3]:  # Boş olmayan listeler True kabul edilir
    print("[1, 2, 3] bir liste ve True olarak değerlendirilir.")  # Çıktı: "[1, 2, 3] bir liste ve True olarak değerlendirilir."

if (1, 2, 3):  # Boş olmayan tuple'lar True kabul edilir
    print("(1, 2, 3) bir tuple ve True olarak değerlendirilir.")  # Çıktı: "(1, 2, 3) bir tuple ve True olarak değerlendirilir."

if {1, 1, 2, 2, 3, 3}:  # Boş olmayan set'ler True kabul edilir
    print("{1, 2, 3} bir set ve True olarak değerlendirilir.")  # Çıktı: "{1, 2, 3} bir set ve True olarak değerlendirilir."

if {"yaş": 19}:  # Boş olmayan sözlükler True kabul edilir
    print('{"yaş": 19} bir dictionary ve True olarak değerlendirilir.')  # Çıktı: '{"yaş": 19} bir dictionary ve True olarak değerlendirilir.'
"""