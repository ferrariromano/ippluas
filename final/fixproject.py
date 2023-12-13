import os
import json
import time

data = []
barang = []
total = 0

#FUNGSI RESET SCREEN
def clear_screen():
    os.system("cls")

def back():
    print()
    print("TUNGGU SEBENTAR....")
    time.sleep(1)
    menu_home()

#DATA FILE SAVE JSON
def tulis_data_json():
    with open("data.json", 'w') as output:
        json.dump(data, output, indent=4)

#DATA FILE LOAD JSON
def baca_data_json():
    with open("data.json", "r") as output: 
        baca = json.load(output) 
        for i in baca:
            data.append(i)

#BANNER/NAMA TOKO
def nama_toko():
    print("-"*61)
    print("{:^61}".format("SELAMAT DATANG DI WARMINDO DEPELE"))
    print("{:^61}".format(""" Jl. Mastrip No.29, Krajan Timur, Sumbersari, Kec. Sumbersari
            Kabupaten Jember, Jawa Timur 68123"""))
    print("-"*61)

#MENU UNTUK PENJUAL
def menu_penjual():
    clear_screen()
    nama_toko()
    time.sleep(1)
    print("{:^61}".format("WARMINDO DEPELE"))
    print("-"*61)
    print("\t1. restock barang"   "\t2. review barang")
    print("\t3. edit barang"'\t' "\t4. hapus barang")
    print("\t5. keluar")
    print("-"*61)
    penjual = int(input("pilih >> "))
    time.sleep(1)
    if penjual == 1:
        clear_screen()
        show_admin()
        restock_barang()
        clear_screen()
        show_admin()
        time.sleep(1)
        menu_penjual()
    elif penjual == 2:
        clear_screen()
        show_admin()
        kembali = input("kembali [y]/[t] : ")
        if kembali == "y":
            clear_screen()
            time.sleep(1)
            menu_penjual()
        elif kembali == "t":
            clear_screen()
            time.sleep(1)
            show_admin()
        else:
            time.sleep(1)
            print("{:^58}".format("Maaf pilihan anda tidak ada"))
    elif penjual == 3:
        clear_screen()
        edit_data()
    elif penjual == 4:
        clear_screen()
        show_admin()
        hapus_barang()
        tanya = input("yakin akan dihapus [y]/[t]: ")
        if tanya == "y":
            time.sleep(1)
            print("data berhasil dihapus")
            time.sleep(1)
            menu_penjual()
        elif tanya == "t":
            hapus_barang()
    else:
        back()

#FUNGSI TAMBAH DATA
def restock_barang():
    nb = input("nama barang : ")
    j = int(input("jumlah : "))
    h = int(input("harga : "))
    d = {
        "Nama Barang" : nb,
        "Jumlah Barang" : j,
        "Harga Barang" : h
    }
    data.append(d)
    tulis_data_json()

# FUNGSI HAPUS DATA
def hapus_barang():
    index = int(input('barang yang dihapus : '))
    data.pop(index-1)
    tulis_data_json()

# FUNGSI DAN MENU EDIT DATA
def edit_data():
    show_admin()
    data_barang = data
    index = int(input("Nomor ke : "))
    print("Pilih")
    print("1. Nama Barang")
    print("2. Tambah Jumlah Barang")
    print("3. Ubah Harga Barang")
    pilih = int(input("pilih >> "))
    
    if pilih == 1:
        nama= input("Masukan Nama Barang baru : ")
        yakin = input("apakah yakin diubah [y/t] : ")
        if yakin == "y":
            nama_baru = {
                "Nama Barang" : nama,
                "Jumlah Barang" : data_barang[index-1]["Jumlah Barang"],
                "Harga Barang" : data_barang[index-1]["Harga Barang"]
            }
            data_barang[index-1]=nama_baru
            tulis_data_json()
            time.sleep(1)
            print("Nama Barang Berhasil diubah!")
            time.sleep(1)
            menu_penjual()
        else:
            print("data tidak jadi diubah")
            time.sleep(1)
            menu_penjual()
    elif pilih == 2:
        jumlah_barang= int(input("Tambah Stok Barang : "))

        for i in data_barang:
            total_stok = i["Jumlah Barang"] + jumlah_barang

        yakin = input("apakah yakin [y/t] : ")
        time.sleep(1)
        if yakin == "y":
            jm_barang = {
                "Nama Barang" : data_barang[index -1]["Nama Barang"],
                "Jumlah Barang" : total_stok,
                "Harga Barang" : data_barang[index-1]["Harga Barang"]
            }
            data_barang[index-1]=jm_barang
            tulis_data_json()
            time.sleep(1)
            print("Jumlah Barang Berhasil ditambah!")
            time.sleep(1)
            menu_penjual()
        else:
            print("data tidak jadi diubah")
            time.sleep(1)
            menu_penjual()
    elif pilih == 3:
        harga= int(input("Masukan Harga Barang baru : "))
        yakin = input("apakah yakin diubah [y/t] : ")
        if yakin == "y":
            harga_baru = {
                "Nama Barang" : data_barang[index -1]["Nama Barang"],
                "Jumlah Barang" : data_barang[index-1]["Jumlah Barang"],
                "Harga Barang" : harga
            }
            data_barang[index-1]=harga_baru
            tulis_data_json()
            time.sleep(1)
            print("Harga Barang Berhasil diubah!")
            time.sleep(1)
            menu_penjual()
        else:
            print("data tidak jadi diubah")
            time.sleep(1)
            menu_penjual()
    else:
        print("pilihan anda tidak ada")
        menu_penjual()

#TAMPILKAN DATA
def show_admin():
    print("\n")
    print("{:^68}".format("WARMINDO DEPELE"))
    print("{:^68}".format(""" Jl. Mastrip No.29, Krajan Timur, Sumbersari, Kec. Sumbersari
            Kabupaten Jember, Jawa Timur 68123"""))
    print("\n")
    print("{:^68}".format("KERANJANG BARANG"))
    print("-"*68)
    print("| {0:3s} | {1:14s} | {2:16s} | {3:22s} |".format("No", "Nama", "Jumlah Barang", "Harga/pcs"))
    print("-"*68)
    for i in range (len(data)):
        print('| %-3s | %-14s | %-16s | %-22s |' %(i+1, data[i]['Nama Barang'],data[i]['Jumlah Barang'],data[i]['Harga Barang'] ))  

#MENU UNTUK PEMBELI
def menu_pembeli():
    nama_toko()
    time.sleep(1)
    print("{:^61}".format("WARMINDO DEPELE"))
    print("-"*61)
    print("\t1. beli barang""\t2. transaksi""\t3. keluar")
    print("-"*61)

#MENU HOME
def menu_home():
    clear_screen()
    nama_toko()
    time.sleep(1)
    print("\t1. Penjual""\t2. Pembeli""\t3. keluar")
    print("-"*61)

baca_data_json()
menu_home()
while True:
    pilih = int(input("pilih >> "))
    time.sleep(1)
    if pilih == 1:
        clear_screen()
        nama_toko()
        username = input("username : ")
        password = input("password : ")
        if username == "admin" and password == "admin":
            time.sleep(1)
            print("LOGIN ANDA BERHASIL.......")
            time.sleep(1)
            print("SELAMAT DATANG DI TOKO SUKA-SUKA")
            time.sleep(1)
            menu_penjual()
        else:
            username != "admin" and password != "admin"
            time.sleep(1)
            print("LOGIN ANDA GAGAL.......")
            time.sleep(1)
            exit()

    elif pilih == 2:
        clear_screen()
        menu_pembeli()
        pembeli = int(input("pilih [1/2/3]>> "))
        time.sleep(1)
        if pembeli == 1:
            clear_screen()
            show_admin()
            nama_barang = input("Nama Barang : ")
            Jumlah_beli = int(input("Jumlah Barang : "))
            for i in data:
                if nama_barang == i['Nama Barang'] : 
                    i['Jumlah Barang'] = i['Jumlah Barang'] - Jumlah_beli
                    tulis_data_json()
            
                    keranjang = Jumlah_beli*i['Harga Barang']
                    total+=keranjang
                else:
                    continue
            b = {
                "Barang": nama_barang,
                "Jumlah" : Jumlah_beli,
                "Total" : total
            }
            barang.append(b)
            print("{:61}".format("Barang Berhasil ditambah"))
            time.sleep(1)
            menu_pembeli()

        elif pembeli == 2:
            clear_screen()
            nama_toko()
            for i in range(len(barang)):
                print(barang[i]["Barang"], ">--->", barang[i]["Jumlah"])

            kondisi = True

            print("total Rp.", total)
            while kondisi:
                uang = int(input("Bayar : "))
                kembalian = uang - total
                if kembalian < 0:
                    kondisi = True
                else:
                    kondisi = False
                    time.sleep(1)
            clear_screen()
            nama_toko()
            for i in range(len(barang)):
                print(barang[i]["Barang"], ">--->", barang[i]["Jumlah"])
            print("total Rp.", total)
            print("Kembalian Rp.", kembalian)
            print("{:^61}".format("TERIMA KASIH TELAH BERBELANJA DI TOKO SUKA-SUKA"))
            print("{:^61}".format("SEMOGA HARI-HARI ANDA MENYENANGKAN"))
            time.sleep(1)
            quit()
        elif pembeli == 3:
            menu_home()
        else:
            print("{:^61}".format("Maaf pilihan anda tidak ada"))
            back()
            
    else:
        quit()