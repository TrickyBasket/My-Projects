import tkinter as tk

# Değişkenler
x = 0
ders_sayi = 5
toplam = 0
sayilar = []
ders_toplam = 0
dertler=[]
y = 0
def ortalama():
    uyari_label.config(text="")
    global sayilar
    sayilar = [] 
    dertler = []
    for i in range(ders_sayi):
        deger = girisler[i].get().strip()
        if deger:
            sayilar.append(deger)
        else:
            # Hangi derse giriş yapılmadı söle
            uyari_label.config(text=f"Lütfen Sayı Girin - Ders {i + 1}")
    global toplam
    global ders_toplam
    global y
    try:

        ders_toplam = 0
        ortalamam = 0
        for d in derzler:
            s = d.get()
            dertler.append(float(s))
            ders_toplam +=float(s)

        # Ortalama Hesaplama
        for i in sayilar:
            kat_sayili = float(i) * dertler[y]
            ortalamam += kat_sayili
            y +=1 
        print(ders_toplam)
        toplam = ortalamam / ders_toplam
        y = 0

        # Sonucu yazdır
        sonuc_cikisi.config(text=f"Ortalaman: {toplam}")
    except ValueError:
        # Hata varsa yazdır
        sonuc_cikisi.config(text="Hatalı giriş! Lütfen sayıları doğru girin.")

# Pencere oluşturma
pencere = tk.Tk()
pencere.title("Ortalama hesaplama programı")

# Ders sayısı
girisler = []
derzler = []
while x != ders_sayi:
    ders_adi = tk.Label(pencere, text=f"Ders{x+1}")
    ders_adi.grid(row=x, column=0, padx=10, pady=10)
    spinbox = tk.Spinbox(pencere, from_=0, to=10)
    spinbox.grid(row=x, column=2, padx=10, pady=10)
    giris = tk.Entry(pencere)
    giris.grid(row=x, column=1, padx=10, pady=10)
    girisler.append(giris)
    derzler.append(spinbox)
    x += 1

# Uyarı label'ı
uyari_label = tk.Label(pencere, text="")
uyari_label.grid(row=x, column=1, columnspan=2, pady=10)

# Hesap butonu
hesap_buttonu = tk.Button(pencere, text="Hesapla", command=ortalama)
hesap_buttonu.grid(row=x + 1, column=0, columnspan=2, pady=10)

# Sonuç
sonuc_cikisi = tk.Label(pencere, text="")
sonuc_cikisi.grid(row=x + 2, column=1, columnspan=2, pady=10)

# Pencereyi çalıştırma   
pencere.mainloop()
