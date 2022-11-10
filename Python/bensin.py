#input
kendaraan=input("Massukan nama kendaraan : ")
bensin=input("Masukkan jenis bensin :")
kota=input("Masukkan kota yang anda tuju :")

#Jenis Bensin
e="pertalite"
x="pertamax"
t="pertamax turbo"

if bensin==e:
    tempuh=bool(12)
    harga=bool(10)
elif bensin==x:
    tempuh=bool(13)
    harga=bool(14)
elif bensin==t:
    tempuh=bool(13.5)
    harga=bool(17)
else:
    tempuh="coba lagi pilih pertalite, pertamax, pertamax turbo"
    harga="coba lagi pilih pertalite, pertamax, petamax turbo"

#Jarak Kota
j="jakarta"
b="bekasi"
d="depok"
g="tangerang"
r="bogor"

if kota==j:
    jarak=bool(20)
elif kota==b:
    jarak=bool(35.7)
elif kota==d:
    jarak=bool(5)
elif kota==g:
    jarak=bool(99)
elif kota==r:
    jarak=bool(120.6)
else:
    jarak="jakarta, bekasi, depok, tangerang, bogor"

#pemakaian bensin
pemakaian= jarak/tempuh
total=pemakaian*harga

#output
print("Nama Kendaraan :", kendaraan)
print("Jenis Bensin :", bensin)
print("Pemakaian Bensin :", pemakaian, "lt")
print("Total Harga Bensin:", total)

    