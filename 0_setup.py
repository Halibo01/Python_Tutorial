import os
import subprocess
# Gerekli kütüphanelerin yüklemelerini yapmak için bu python programını çalıştırınız
base_dir = os.path.dirname(os.path.abspath(__file__))

for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)

    requirements_path = os.path.join(folder_path, "requirements.txt")
    if os.path.isdir(folder_path) and os.path.isfile(requirements_path):
        print(f"📌 Kütüphaneler yükleniyor: {requirements_path}")
        subprocess.run(["pip", "install", "-r", requirements_path], check=True)

print("✅ Tüm kütüphaneler yüklendi!")