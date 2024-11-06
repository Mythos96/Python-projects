#Yapılacaklar Listesi
Yapılacaklar_Listesi = []

#Fonksiyonlar
def gorev_ekleme():
    gorev = input("Eklenecek görevi giriniz: ")
    Yapılacaklar_Listesi.append(gorev)
    print("Görev eklendi!")

def gorev_cıkarma():
    cıkacak = input("Çıkarmak istediğiniz görevi yazınız: ")
    Yapılacaklar_Listesi.remove(cıkacak)
    print("Görev Çıkarıldı!")

def gorev_goruntuleme():
    print("Yapılacak Görevler:")
    for gorev in Yapılacaklar_Listesi:
        print("-", gorev)

#Başlangıç
print("<To Do List>")
print("Lütfen başlamak için bir görev giriniz")
gorev_ekleme()

#Ana döngü
while True:
    print("")
    print("Görev Ekle(1)\nGörev Çıkar(2)\nGörevleriGörüntüle(3)\nÇık(0)")
    secim = input("Seçiminizin numarasını giriniz: ")

    if secim == "1":
        gorev_ekleme()
    elif secim == "2":
        gorev_cıkarma()
    elif secim == "3":
        gorev_goruntuleme()
    elif secim == "0":
        break
    else:
        print("Hatalı Numara, Lütfen tekrar giriniz")
