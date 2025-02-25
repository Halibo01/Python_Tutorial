# Pythonda Özel Karakterler
# Python'da özel karakterler, genellikle bir dizide belirli işlevleri yerine getirmek için kullanılır.
# Özel karakterler ters bölü (backslash) '\' ile başlar ve ardından belirli bir sembol gelir.
# Bu karakterler, özellikle dizilerde biçimlendirme ve kaçış (escape) yapmak için kullanılır.

# 1. '\n' -> Satır Sonu (Newline)
# '\n' karakteri, bir satır sonu (yeni bir satıra geçiş) ekler.
# Bu sayede metinlerde satır sonları eklenebilir.
print("Merhaba dünya!\nPython çok eğlenceli!")  # Satır sonunda 'Python çok eğlenceli!' yeni satırda yazılır

# 2. '\t' -> Tab (Sekme)
# '\t' karakteri, bir tab boşluğu ekler. Bu, metni hizalamak için kullanılır.
"""
print("İsim\tYaş\tŞehir")  # İsim, Yaş ve Şehir arasına tab boşluğu ekler
print("Ali\t23\tİstanbul")  # Tab kullanımıyla düzgün hizalama sağlar
"""

# 3. '\\' -> Ters Bölü (Backslash)
# '\\' karakteri, bir ters bölü (backslash) karakterini ekler.
# Çünkü tek bir ters bölü, Python'da kaçış karakteri olarak kabul edilir, bu yüzden bir ters bölü eklemek için '\\' kullanılır.
"""
print("C:\\Program Files\\Python")  # 'C:\Program Files\Python' yolunu yazdırır
"""

# '\\' kullanmak yerine string elemanının başına "r" koyarak bu kullanılabilir.
# Bu biraz ezber olsa da yinede kullanılabilir bir yöntemdir.
"""
print(r"C:\Program Files\Python")
"""

# 4. '\"' -> Çift Tırnak (Double Quote)
# '\"' karakteri, bir çift tırnak karakterini dizinin içine ekler.
# Bu, tırnak içinde tırnak kullanmak için yararlıdır.
"""
print("Python \"güzel\" bir dil!")  # Çift tırnakları dizinin içine ekler
"""

# 5. "\'" -> Tek Tırnak (Single Quote)
# "\'" karakteri, bir tek tırnak karakterini dizinin içine ekler.
# Bu da tırnak içinde tek tırnak kullanmak için yararlıdır.
"""
print('Python, \'harika\' bir dil!')  # Tek tırnakları dizinin içine ekler
"""

# 6. '\r' -> Satır Başına Geri Dönme (Carriage Return)
# '\r' karakteri, satır başına geri döner. Bu, mevcut satırın üzerine yazmak için kullanılır.
"""
print("12345\rABCDE")  # '12345' silinir ve 'ABCDE' ile yer değiştirilir
"""

# 7. '\b' -> Backspace (Silme)
# '\b' karakteri, bir karakteri silmek için kullanılır.
# Bu, bir karakteri geri siler ve bir sonraki karakteri önceden yazılmış olanın yerine koyar.
"""
print("Python\b Rocks")  # 'Python' sonrasındaki 'n' silinir ve ' Rocks' yazılır
"""

# 8. '\f' -> Sayfa Sonu (Form Feed)
# '\f' karakteri, sayfa sonu (form feed) ekler. Bu, eski yazıcılarla ilgili bir işlevdi ve genellikle modern sistemlerde kullanılmaz.
"""
print("Python\f öğreniyorum!")  # Bu karakter genellikle sayfa sonu eklerdi
"""

# 9. '\ooo' -> Oktal Sayılar
# Oktal sayılarla bir karakteri ifade etmek için '\ooo' şeklinde yazılır. Burada 'ooo' oktal (8'lik) bir sayı olmalıdır.
"""
print("\101")  # Oktal değer '101' ASCII tablosunda 'A' karakterine karşılık gelir
"""

# 10. '\xhh' -> Hexadecimal (Onaltılık) Sayılar
# Hexadecimal (onaltılık) sayılarla bir karakteri ifade etmek için '\xhh' yazılır. Burada 'hh' onaltılık bir sayı olmalıdır.
"""
print("\x48\x65\x6c\x6c\x6f")  # Hexadecimal değerler, 'Hello' kelimesini oluşturur
"""