a = input("Birinci Sayıyı Girin:\n")
b=input("İkinici Sayıyı Griniz:\n")
say=0

if int(a)>=0:
    print("Çift sayılar :")
    for i in range(int(a),int(b)):
        if i % 2 == 0:
            say=say+1
            print(i)
        
    print("\nToplam Çift Sayı:",say)
else:
    print("Lütfen Sayı girin.")
