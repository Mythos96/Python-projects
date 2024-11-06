#Hesap makinesi
while True:

    islemler = ["toplama","çıkarma","çarpma","bölme","üs alma","kalansız bölme"]

    #Kullanıcıdan veri alımı
    islem = input("Yapmak istediğiniz işlemi küçük harf kullanarak yazınız: ")
    if islem in islemler:
        a = int(input("İlk sayıyı giriniz: "))
        b = int(input("İkinci sayıyı giriniz: "))
    else:
        print("Geçersiz işlem")


    #fonksiyonlar
    def toplama(a,b):
        return a+b
        
    def cıkarma(a,b):
        return a-b

    def carpma(a,b):
        return a*b

    def bolme(a,b):
        return a/b

    def us_alma(a,b):
        return a**b

    def kalansız_bolme(a,b):
        return a//b


    #Çıktılar
    if islem == "toplama":
        print(a, "+", b, "=", toplama(a,b))
    elif islem == "çıkarma":
        print(a, "-", b, "=", cıkarma(a,b))
    elif islem == "bölme":
        print(a, "/", b, "=", bolme(a,b))
    elif islem == "çarpma":
        print(a, "*", b, "=", carpma(a,b))
    elif islem == "üs alma":
        print(a, "**", b, "=", us_alma(a,b))
    elif islem == "kalansız bölme":
        print(a, "//", b, "=", kalansız_bolme(a,b))
    
