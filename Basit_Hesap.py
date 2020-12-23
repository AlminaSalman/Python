# Toplama Fonksiyonu
def Topla(x, y):
   return x + y
 
# Çıkarma Fonksiyonu
def Cikar(x, y):
   return x - y
 
# Çarpma Fonksiiyonu
def Carp(x, y):
   return x * y
 
# Bölme Fonksiyonu
def Bol(x, y):
   return x // y

x=int(input("Bir Sayı Giriniz: "))
y=int(input("İkinci Sayıyı Giriniz: "))
print("+, -, *, /")
islem=input("İşlem Seçiniz: ")

if islem=="+":
    print("Toplama İşlemi Sonucu: ",Topla(x,y))
elif islem=="-":
    print("Çıkarma İşlemi Sonucu: ",Cikar(x,y))
elif islem=="*":
    print("Çarpma İşlemi Sonucu: ",Carp(x,y))
elif islem=="/":
    print("Bölme İşlemi Sonucu: ",Bol(x,y))

