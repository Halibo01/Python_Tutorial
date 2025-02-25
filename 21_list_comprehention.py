# List comprehension, Python'da bir listenin kısa ve öz bir şekilde oluşturulmasını sağlayan bir özelliktir.
# Temelde, bir listeyi tek bir satırda oluşturmanıza olanak tanır.

# Aşağıdaki örnekte, 1'den 10'a kadar olan sayıları içeren bir liste oluşturacağız.
# List comprehension, bunun için kısa ve etkili bir yol sunar.

# Normal bir döngü kullanarak liste oluşturma:
"""
numbers = []
for i in range(1, 11):
    numbers.append(i)
print(numbers)
"""


# List comprehension kullanarak aynı listeyi oluşturma:
"""
numbers_comprehension = [i for i in range(1, 11)]
print(numbers_comprehension)
"""


# List comprehension, bir for döngüsü içinde işlemleri doğrudan yapmanızı sağlar.

# Şimdi, list comprehension ile bazı ek özellikleri göstereceğiz.

# 1. Koşullu ifadelerle list comprehension kullanma:
# Örneğin, 1'den 10'a kadar olan sayılardan sadece çift olanları listeye ekleyelim.
"""
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)
"""


# 2. List comprehension ile bir işlemi uygulama:
# Örneğin, 1'den 5'e kadar olan sayıları karelerine alalım.
"""
squares = [i ** 2 for i in range(1, 6)]
print(squares)
"""


# 3. İç içe list comprehension kullanma:
# Aşağıdaki örnekte, 1'den 3'e kadar olan her bir sayı için 1'den 3'e kadar olan sayıları içeren
# bir liste oluşturacağız.
"""
nested_list = [[i, j] for i in range(1, 4) for j in range(1, 4)]
print(nested_list)
"""


# 4. `if-else` kullanarak list comprehension örneği:
# Burada, 1'den 10'a kadar olan sayıları listeleyeceğiz, ancak sayı çiftse "even" ve tekse "odd" yazalım.
"""
even_or_odd = ["even" if i % 2 == 0 else "odd" for i in range(1, 11)]
print(even_or_odd)
"""


# List comprehension daha karmaşık işlemler için de kullanılabilir.
# Örneğin, bir metnin her harfini büyük harfe dönüştürmek:
"""
text = "hello"
uppercase_letters = [char.upper() for char in text]
print(uppercase_letters)
"""




# 5. List comprehension ile bir fonksiyon uygulama:
# Diyelim ki her sayıyı bir fonksiyona uygulamak istiyoruz.
"""
def double(x):
    return x * 2

doubled_numbers = [double(i) for i in range(1, 6)]
"""



# 6. Lambda kullanarak list comprehension:
# Bu örnekte, 1'den 5'e kadar olan sayıların iki katını almak için lambda fonksiyonu kullanacağız.
"""
doubled_numbers_lambda = [(lambda x: x * 2)(i) for i in range(1, 6)]
print(doubled_numbers_lambda)
"""

# Bu şekilde list comprehension kullanarak daha kısa ve anlaşılır kodlar yazabilirsiniz.
