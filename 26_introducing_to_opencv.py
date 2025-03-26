import cv2  # OpenCV kütüphanesini içe aktarıyoruz.
import numpy as np  # Sayısal işlemler için NumPy kütüphanesini içe aktarıyoruz.

# Kütüphaneler yalnızca komut satırına:
# pip install opencv-python
# Şeklinde yazıldığında kolaylıkla kurulumu yapılabilir



# Görüntüler çok basit olarak 2 boyutlu matrislerden oluşur yani matrisler listeler içindeki eşit uzunluktaki listeler olarak ifade edilebilir.
# Ve liste işlemleriyle aynı olarak matrislerle çalışılabilir. Bundan dolayı matrisler listeler olarak da işlev görmektedir.
# Örnek olarak 5'e 5'lik bir matris: (5 satır ve 5 sütun uzunluğunda)
#  +------0----1----2----3----4----> X
#  |  [
#  0     [120, 130, 156, 32 , 21], <- 0. indexteki satır
#  1     [87 , 65 , 43 , 210, 99],
#  2     [54 , 178, 201, 15 , 76],
#  3     [33 , 140, 89 , 190, 11],
#  4     [41 , 84 , 193, 54 , 0 ]  <- 4. indexteki satır
#  |  ]
#  Y

# Burada eleman alma işlemi karmaşık olabilir fakat eleman alırken ilk önce satır değeri yazılır sonrasında sütun değeri yazılır
# spesifik değer alma örneği:
# matris[Y, X]
# örnek olarak yukarıdaki matrisin 0. sütun ve 0. satırına ulaşabilmek için
# matris[0, 0]
# yazılmalıdır ve çıkış matris[0, 0] çıkış değeri 120 olacaktır

# matris[0] ın çıktısı 0. indexteki satırın tamamıdır yani 0. satırdaki listenin hepsini almaktadır.
# print(matris[0])
# Çıktı: [120, 130, 156, 32 , 21]


# Sonrasında yapılan iş bu listedeki elemanı almaktır.
# print(matris[0, 0])
# Çıktı: 120
# matris[2, 2] nin çıkış değeri 201 dir
# matris[4, 0] ın  çıkış değeri 41  dir
# matris[1, 3] ün  çıkış değeri 210 dur


# Aşağıdaki kodu kullanarak matris değerleriyle oynayabilirsiniz yada daha yakından inceleyebilirsiniz
"""
matris = [
    [120, 130, 156, 32 , 21],
    [87 , 65 , 43 , 210, 99],
    [54 , 178, 201, 15 , 76],
    [33 , 140, 89 , 190, 11],
    [41 , 84 , 193, 54 , 0 ]
]
matris = np.array(matris)                                            # Listeyi matrise dönüştürme işlemi
print(matris[4, 0])                                                  # matrisin 4. satır 0. sütundaki değerini alma işlemi
matris[4, 4] = 0                                                     # matris değerlerinde değişiklik yapabilirsiniz
"""





# Oluşturduğunuz matrisi aşağıdaki koddan görüntüleyebilirsiniz:
"""
matris = np.uint8(matris)                                               # unsigned integer 8 değerine dönüştürme işlemi. Resimler standart olarak 0 ile 255 arasına yani 8 bitlik görüntülerdir.
                                                                        # matrisin veri tipi bu kod ile belirlenir
matris = cv2.resize(matris, (600, 600), interpolation=cv2.INTER_NEAREST)# Kübik olarak yeniden boyutlandırma
cv2.imshow("Benim matrisim :)", matris)                                 # Ekrana gösterme
cv2.waitKey(0)
"""




# matris eğitiminden sonra diğer eğitime geçelim
# 1. Bir görüntüyü yükleyelim.

image = cv2.imread(r"26_introducing_to_opencv/Lena.png") # Eğer dosya yolu bulunamıyorsa yada görüntü bu yolu değiştirdiğiniz halde okunamadıysa bilgisayarınızda bulunan resmin üstüne sağ tıklayıp yolu kopyala
                                    # butonuna tıklayınız. Sonrasında r yazısını kaldırmadan dosya yolunu yapıştırınız.



# 2. Görüntüyü ekrana gösterelim.

cv2.imshow('Original Image', image)     # cv2.imshow(str, matrix) değeri almaktadır. String değeri yalnızca pencerenin yazısını belli eder ondan dolayı önemli değildir
cv2.waitKey(0)                          # cv2.waitKey(0) Koymamızın nedeni görselin süresiz bir şekilde göstermek istememizdir. 0 değerine herhangi başka bir sayı yazılabilir
                                        # cv2.waitKey fonksiyonundaki sayı değeri görselin milisaniye bakımından ne kadar kalacağını belirler. Eğer değer 5000 olursa görsel 5 saniye
                                        # boyunca ekranda kalır


# 3. Görüntüde matrix işlemleri
# Görseldeki tek bir matrixi görüntüleyelim:
"""
print(image[250, 250]) # Görsel içindeki 250. satırdaki ve 250. sütundaki renk değerlerini inceleyelim
"""


# Çıktı: [167 175 215]
# Çıktıda (B, G, R) kanallarının hangi renk değerlerini aldığını gösterir
# B kanalının renk değeri: 167
# G kanalının renk değeri: 175
# R kanalının renk değeri: 215


# Aşağıdaki gibi (BGR) formatında olan görüntülerin teker teker B, G, R kanallarını alıyoruz
"""
B = image[:, :, 0] # Matrixin içindeki tüm mavi    rengi alıyoruz
G = image[:, :, 1] # Matrixin içindeki tüm yeşil   rengi alıyoruz
R = image[:, :, 2] # Matrixin içindeki tüm kırmızı rengi alıyoruz



merged_image = cv2.hconcat([B, G, R])   # Görüntüleri karşılaştırma yapmak amacıyla birleştiriyoruz
cv2.imshow("merge", merged_image)       # Görüntüler tek kanallı olduğu için yalnızca grayscale yani gri tonlamalı olarak görünecektir
cv2.imshow("normal_image", image)       # Resmin kendisi
cv2.waitKey(0)
"""

# image.shape kodunu yazarak görselin boyutunu öğrenebilirsiniz
# Çıktı olarak (512, 512, 3) Çıktısı üretecektir. 
# Nedeni görselin boyunun 512 pixel, eninin 512 pixel ve 3 kanallı (BGR) renk yapısına sahip olmasıdır
"""
print(image.shape)
"""

# 4. Görüntüyü gri tonlamaya çevirelim.
"""
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # cv2.COLOR_BGR2GRAY yerine farklı değerler kullanabilirsiniz. Bunların hepsini inceleyebilirsiniz.
cv2.imshow("image", gray_image)
cv2.waitKey(0)


# Gri tonlamadaki pixel değerini inceleyelim
print(gray_image[250, 250])
# Çıktı: 186
# Görüntü belirli hesaplamalarla gri tonlamaya yani yalnızca tek bir renk kanalına dönüştüğü için 3 adet renk değeri yerine 1 adet renk değeri görünür

"""



# 5. Görüntüyü bulanıklaştıralım.
"""
blurred_image = cv2.GaussianBlur(image, (3, 3), 0)  # Blurlama için gauss bulanıklaştırma algoritması uygulanır
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
"""

# 6. Görüntü üzerinde kenar tespiti yapalım.
"""
edges = cv2.Canny(image, 50, 150)       # Canny fonksiyonunda görselin kendisi ve bunlarla beraber alt sınıf ve üst sınır belirlenir
cv2.imshow('Edge Detection', edges)
cv2.waitKey(0)
"""

# 7. Görüntüyü yeniden boyutlandıralım.
"""
resized_image = cv2.resize(image, (800, 800))   # Görüntü 800x800 lük genişliğe sahip olur
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
"""


# 8. Görüntüleri yatay ve dikey birleştirelim.
"""
hconcat_image = cv2.hconcat([image, image])                     # Yatay birleştirme fonksiyonu
cv2.imshow('Horizontally Concatenated Image', hconcat_image)
cv2.waitKey(0)
"""

"""
vconcat_image = cv2.vconcat([image, image])                     # Dikey birleştirme fonksiyonu
cv2.imshow('Vertically Concatenated Image', vconcat_image)
cv2.waitKey(0)
"""



# 9. Görüntü üzerine dikdörtgen çizelim.
"""
image_with_rectangle = image.copy()                        # Copy işlemi orijinal görüntüyü değiştirmemek için kullanılır.

# image_copy = image işlemi aynı görseli ifade ettiğinden image_copy üzerinde yapılan değişikliklerden orijinal görüntü de etkilenir bundan dolayı copy() fonksiyonu ile görsel başka bir değişkene kopyalanır

cv2.rectangle(image_with_rectangle, (50, 50), (250, 250), (0, 255, 0), 3)   # Fonksiyonda görüntü, 1. pixel noktası, 2. pixel noktası, renk ve kalınlık argüman olarak verilmiştir
cv2.imshow('Image with Rectangle', image_with_rectangle)
cv2.waitKey(0)
"""

# 10. Görüntünün belirli bir kısmını tamamen mavi yapalım.
# Bu işlemde görüntü direkt manüpile edilerek pixel değerleri değiştirilmiştir
"""
image_with_blue_patch = image.copy()
image_with_blue_patch[200:300, 200:300] = (255, 0, 0)  # BGR formatında mavi renk
cv2.imshow('Image with Blue Patch', image_with_blue_patch)
cv2.waitKey(0)
"""

# 11. Görüntü üzerine daire çizelim.
"""
image_with_circle = image.copy()
cv2.circle(image_with_circle, (150, 150), 50, (0, 0, 255), -1)  # Kırmızı dolu daire
cv2.imshow('Image with Circle', image_with_circle)
cv2.waitKey(0)
"""

# 12. Görüntü üzerine yazı ekleyelim.
"""
image_with_text = image.copy()
cv2.putText(image_with_text, 'OpenCV Tutorial', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2) # Bu fonksiyonda oynama yaparak ne işe yaradıklarını inceleyebilirsiniz
cv2.imshow('Image with Text', image_with_text)
cv2.waitKey(0)
"""

# 13. Görüntüyü kaydedelim.
"""
cv2.imwrite("new_image.jpg", image) # Görüntü jpg, jpeg, png, ve diğer farklı formatlarda da kaydedilebilir
"""
# OpenCV tutorial tamamlandı! 😊