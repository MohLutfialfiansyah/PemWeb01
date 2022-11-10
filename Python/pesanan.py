#input
nama=input("Atas Nama :")
hp=input("Masukkan No Hp Anda :")
pesan=input("Pesan Menu (makanan/minuman) :")

a="makanan"
b="minuman"

#makanan
pesanan={}

if pesan==a:
    print("\n")
    print("1.nasi goreng Rp.15.000\n2.mie goreng Rp.12.000\n3.ayam geprek Rp.18.000")
    y=input("Masukkan Pesanan Anda :")
    if y=="1" or y=="nasi goreng":
        hasil="nasi goreng"
        jumlah1=int(input("Masukkan jumlah :"))
        pesanan["nasi goreng"]=jumlah1
        total=jumlah1*15000
    elif y=="2" or y=="mie goreng":
        hasil="mie goreng"
        jumlah2=int(input("Masukkan jumlah : "))
        pesanan["mie goreng"] = jumlah2
        total =jumlah2*12000
    elif y=="3" or y=="ayam geprek":
        hasil="ayam geprek"
        jumlah3=int(input("Masukkan jumlah : "))
        pesanan["ayam geprek"] = jumlah3
        total =jumlah3*18000
    else:
        hasil="Maaf Menu Belum Tersedia"
    
    print("=======STRUK======")
    print("Nama Pembeli:", nama)
    print("No Hp:", hp)
    print("Pesanan Anda:", pesanan)
    print("Total Harga :", total)

elif pesan==b:
    print("\n")
    print("1.aneka jus Rp.15.000\n2.soft drink Rp.10.000\n3.sweet ice tea Rp.5.000")
    x=input("Masukkan Pesanan Anda :")
    if x=="1" or x=="aneka jus":
        hasil="aneka jus"
        jumlah1=int(input("Masukkan jumlah :"))
        pesanan["aneka jus"]=jumlah1
        total=jumlah1*15000
    elif x=="2" or x=="soft drink":
        hasil="soft drink"
        jumlah2=int(input("Masukkan jumlah : "))
        pesanan["soft drink"] = jumlah2
        total =jumlah2*10000
    elif x=="3" or x=="sweet ice tea":
        hasil="sweet ice tea"
        jumlah3=int(input("Masukkan jumlah : "))
        pesanan["sweet ice tea"] = jumlah3
        total =jumlah3*5000
    else:
        hasil="Maaf Menu Belum Tersedia"

    print("=======STRUK======")
    print("Nama Pembeli:", nama)
    print("No Hp:", hp)
    print("Pesanan Anda:", pesanan)
    print("Total Harga :", total)
else:
    hasil="Error Tidak Tersedia"
    

