a = 10
b = 4

# Karşılaştırma Operatörleri
"""
print(a == b)  # == operatörü ile karşılaştırma yapılır. a ve b eşit mi? False döner çünkü a (10) b (4) ile eşit değil.
print(a > b)   # > operatörü ile 'a'nın b'den büyük olup olmadığı kontrol edilir. True döner çünkü 10 > 4.
print(a < b)   # < operatörü ile 'a'nın b'den küçük olup olmadığı kontrol edilir. False döner çünkü 10 < 4 değil.
print(a >= b)  # >= operatörü ile 'a'nın b'ye eşit ya da b'den büyük olup olmadığı kontrol edilir. True döner çünkü 10 >= 4.
print(a <= b)  # <= operatörü ile 'a'nın b'ye eşit ya da b'den küçük olup olmadığı kontrol edilir. False döner çünkü 10 <= 4 değil.
print(a != b)  # != operatörü ile 'a' ve 'b' eşit mi diye kontrol edilir. True döner çünkü 10 != 4.
"""

# Mantıksal Operatörler (not, and, or) ile Karşılaştırmalar
"""
# C dilindeki mantıksal NOT örneği:
# !(a < b) = "a b'den küçük değil" ifadesi
# Python'da ise not operatörü kullanılır:
print(not a > b)  # not a > b ifadesi, "a'nın b'den büyük olup olmadığına" tersini alır. True döner çünkü 10 > 4'ün tersidir yani False, tersini aldık True.

# C dilindeki mantıksal AND örneği:
# (a < b) && (a < 0) = "a'nın b'den küçük ve aynı zamanda negatif olduğu" ifadesi.
# Python'da and operatörü kullanılır:
print(a < b and a < 0)  # a < b False, a < 0 False olduğundan AND işlemiyle ikisi de False olduğundan False döner.

# C dilindeki mantıksal OR örneği:
# (a < b) || (a < 0) = "a'nın b'den küçük ya da negatif olduğu" ifadesi.
# Python'da or operatörü kullanılır:
print(a < b or a < 0)  # a < b False, a < 0 False olduğundan OR işlemiyle ikisi de False olduğu için False döner.
"""

# NOT: Python'da boşluklar (indentation) çok önemlidir.
# Python'da kod blokları boşluklarla belirlenir. Her kod bloğu, bir önceki satırdaki ifade ile aynı hiyerarşiye sahip olmalıdır.

# C Dili Örneği:
# C dilinde boşluklar genellikle yalnızca kodun görünümünü belirler ve işleyişte doğrudan bir etkisi yoktur.

"""
if (x > 0) {  # Parantez kullanılır, bloklar {} ile belirlenir
    printf("Pozitif\n");  # Pozitif mesajı yazdırılır
} else {
    printf("Negatif veya sıfır\n");  # Negatif ya da sıfır mesajı yazdırılır
}
"""

# Python Örneği:
# Python'da ise boşluklar çok önemlidir! Kod blokları girintilerle (indentation) belirlenir.
"""
if a > 0:  # Bu if bloğu a'nın pozitif olup olmadığını kontrol eder.
    print("Pozitif")  # Eğer a > 0 ise "Pozitif" yazdırılır.
else:  # Eğer a <= 0 ise else bloğu çalışır.
    print("Negatif veya sıfır")  # "Negatif veya sıfır" yazdırılır.
"""

# Boşluk Hataları (Indentation Error)
# Python'da yanlış girinti yapmak, kodun doğru çalışmamasına yol açar.
"""
if a > 0:  # Bu satır doğru bir şekilde başlatılmış bir if bloğudur
    print("Pozitif")  # Bu satır da if bloğunun içine girer
    else:  # Bu satır hata verir, çünkü else if bloğunun bir parçası olmalı, ancak yanlış girintilenmiştir.
        print("Negatif veya sıfır")
"""
# Yukarıdaki örnekte, else if bloğuna ait olmalı ancak doğru şekilde girintilenmediği için Python hata verir.
# else satırının, if bloğunun altına uygun şekilde girintilenmesi gerekir.

# DOĞRU KULLANIM:
"""
if a > 0:
    print("Pozitif")  # Bu satır doğru bir şekilde if bloğunun içine yerleştirilmiştir.
else:
    print("Negatif veya sıfır")  # else bloğu doğru bir şekilde hizalanmıştır.
"""

# Yanlış kullanım:
"""
count = 0

while count < 5:  # Bu satır doğru
        print(count)  # Hata: 'print' fonksiyonu yanlış girintilenmiş!

    count += 1  # Hata: 'count' değişkeninin artırılması da yanlış girintilenmiş!
"""

# Doğru kullanım:
"""
count = 0

while count < 5:  # Bu satır doğru
    print(count)  # Hata: 'print' fonksiyonu yanlış girintilenmiş!

    count += 1  # Hata: 'count' değişkeninin artırılması da yanlış girintilenmiş!
"""

# Bazı kullanımlar da yanlış gibi görünebilir ama orijinal olarak doğrudurlar
"""
count = 1
if count == 1:print("Bu doğru bir kullanımdır")
"""

"""
toplam = 0
liste = [1,2,3,4,5,6,7,8,9]
for i in liste: print(i); print("doğru kullanım örneği"); toplam += i
print(toplam)
"""

"""
def function():...
function()
"""