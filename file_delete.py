import os
from path import Path
import time
import tkinter as tk
from tkinter import filedialog


lsit = []

try:
    dosya = open("config.txt", "r")
    lines = dosya.readlines()
    for line in lines:
        if not line.strip():
            continue
        lsit.append(line.replace("\n", ""))

    dosya.close()

    # tup = tuple(lsit)
    # print(tup)
except FileNotFoundError:
    print("config.txt bulunamadı!!! \n Programdan Çıkılıyor...")
    time.sleep(2)
    exit()

root = tk.Tk()
root.withdraw()

filetypes = (
    ('Text Files', '*.txt'),
    ('All files', '.')
)

file_path = filedialog.askopenfilename(title='Lütfen Liste Dosyanızı seçiniz', filetypes=filetypes, multiple=True)
print(file_path)

try:
    for filename in file_path:
        file = open(filename, "r")
        lines = file.readlines()
        for line in lines:
            if not line.strip():
                continue
            lsit.append(line.replace("\n", ""))

        file.close()
    print(lsit)
    tup = tuple(lsit)
    print(tup)
except FileNotFoundError:
    print("Liste dosyası bulunamadı !!!")
    cevap = input("Programdan çıkmak ister misiniz (e/H): ")
    if cevap == "e" or cevap == "E":
        exit()
    elif cevap == "h" or cevap == "H":
        print("Silme işlemi yalnızca config dosyasıyla devam ediyor...")
    else:
        print("Geçerli bir cevap girilmedi programdan çıkılıyor...")
        time.sleep(2)
        exit()

HEDEF = "X:\\"

h = Path(HEDEF)  # HEDEF Adlı ifadeyi Path tipine dönüştürüyoruz


def delete():
    print("\n\nDosyalar %s adresinden siliniyor !!\n" % h)
    dosya_sayisi = 0
    sayac = 0
    for i in h.walk():  # dizinin içindek dosyaları gez
        a = str(i)  # dosya içerisinde kontrol yapmak için gezilen dosya yollarını string ifadeye dönüştürür
        # print(a[70:])
        if i.isfile() and not a[3:].startswith(tup):  # eğer mevcut indiste dosya listedeki isimle
            # başlamıyorsa yukarıdaki ifadede belirttiğim yol 70 karakter yer kapladığı için böyle sunucuya
            # aktarılacak programda 3 olacak
            dosya_sayisi += 1  # dosya sayısını artır
            print("Siliniyor : %s" % a[3:])
            os.remove(i)  # hedefte bulunan mevcut indisteki dosyayı sil
            sayac += 1
            if sayac == 0:
                print("Mevcut dizinde belirtilen dosya bulunamadı ! ")
            else:
                print("\n%s adet dosya başarılı şekilde silindi" % dosya_sayisi)
                sayac = 0


if _name_ == "_main_":
    if os.path.exists(HEDEF):
        delete()
    else:
        print("\n\nDosya Yolu Bulunamadı")