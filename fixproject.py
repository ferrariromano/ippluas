import os
import json
import time

class InventoryManagement:
    def __init__(self):
        self.data = []
        self.total = 0

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def tulis_data_json(self):
        with open("data.json", 'w') as output:
            json.dump(self.data, output, indent=4)

    def baca_data_json(self):
        try:
            with open("data.json", "r") as output:
                self.data = json.load(output)
        except FileNotFoundError:
            self.data = []

    def cari_barang(self, nama_barang):
        for barang in self.data:
            if barang['Nama Barang'] == nama_barang:
                return True, barang
        return False, None

    def menu_penjual(self):
        self.clear_screen()
        self.nama_toko()
        print("{:^61}".format("WARMINDO DEPELE"))
        print("-" * 61)
        print("\t1. restock barang" "\t2. review barang")
        print("\t3. edit barang" '\t' "\t4. hapus barang")
        print("\t5. keluar")
        print("-" * 61)
        penjual = input("pilih >> ")
        if penjual == '1':
            self.clear_screen()
            self.show_admin()
            self.restock_barang()
        elif penjual == '2':
            self.clear_screen()
            self.show_admin()
            kembali = input("kembali [y]/[t] : ")
            if kembali == "t":
                self.clear_screen()
                self.show_admin()
            else:
                time.sleep(1)
                self.menu_penjual()
        elif penjual == '3':
            self.clear_screen()
            self.edit_data()
        elif penjual == '4':
            self.clear_screen()
            self.show_admin()
            self.hapus_barang()
            tanya = input("yakin akan dihapus [y]/[t]: ")
            if tanya == "t":
                self.hapus_barang()
        else:
            self.back()

    def restock_barang(self):
        nb = input("nama barang : ")
        j = int(input("jumlah : "))
        h = int(input("harga : "))
        d = {
            "Nama Barang": nb,
            "Jumlah Barang": j,
            "Harga Barang": h
        }
        self.data.append(d)
        self.tulis_data_json()

    def hapus_barang(self):
        index = int(input('barang yang dihapus : '))
        if 0 < index <= len(self.data):
            del self.data[index - 1]
            self.tulis_data_json()
        else:
            print("Nomor barang tidak valid")

    def edit_data(self):
        self.show_admin()
        data_barang = self.data
        index = int(input("Nomor ke : "))
        if 0 < index <= len(data_barang):
            print("Pilih")
            print("1. Nama Barang")
            print("2. Tambah Jumlah Barang")
            print("3. Ubah Harga Barang")
            pilih = int(input("pilih >> "))

            if pilih == 1:
                nama = input("Masukan Nama Barang baru : ")
                yakin = input("apakah yakin diubah [y/t] : ")
                if yakin == "y":
                    data_barang[index - 1]["Nama Barang"] = nama
                    self.tulis_data_json()
                    time.sleep(1)
                    print("Nama Barang Berhasil diubah!")
                    time.sleep(1)
                    self.menu_penjual()
                else:
                    print("data tidak jadi diubah")
                    time.sleep(1)
                    self.menu_penjual()
            elif pilih == 2:
                jumlah_barang = int(input("Tambah Stok Barang : "))
                for i in data_barang:
                    total_stok = i["Jumlah Barang"] + jumlah_barang

                yakin = input("apakah yakin [y/t] : ")
                time.sleep(1)
                if yakin == "y":
                    data_barang[index - 1]["Jumlah Barang"] = total_stok
                    self.tulis_data_json()
                    time.sleep(1)
                    print("Jumlah Barang Berhasil ditambah!")
                    time.sleep(1)
                    self.menu_penjual()
                else:
                    print("data tidak jadi diubah")
                    time.sleep(1)
                    self.menu_penjual()
            elif pilih == 3:
                harga = int(input("Masukan Harga Barang baru : "))
                yakin = input("apakah yakin diubah [y/t] : ")
                if yakin == "y":
                    data_barang[index - 1]["Harga Barang"] = harga
                    self.tulis_data_json()
                    time.sleep(1)
                    print("Harga Barang Berhasil diubah!")
                    time.sleep(1)
                    self.menu_penjual()
                else:
                    print("data tidak jadi diubah")
                    time.sleep(1)
                    self.menu_penjual()
            else:
                print("pilihan anda tidak ada")
                self.menu_penjual()
        else:
            print("Nomor barang tidak valid")
            self.menu_penjual()

    def show_admin(self):
        self.clear_screen()
        self.nama_toko()
        print("\n")
        print("{:^68}".format("WARMINDO DEPELE"))
        print("{:^68}".format(""" Jl. Mastrip No.29, Krajan Timur, Sumbersari, Kec. Sumbersari
                Kabupaten Jember, Jawa Timur 68123"""))
        print("\n")
        print("{:^68}".format("KERANJANG BARANG"))
        print("-" * 68)
        print("| {0:3s} | {1:14s} | {2:16s} | {3:22s} |".format("No", "Nama", "Jumlah Barang", "Harga/pcs"))
        print("-" * 68)
        for i in range(len(self.data)):
            print('| %-3s | %-14s | %-16s | %-22s |' % (
            i + 1, self.data[i]['Nama Barang'], self.data[i]['Jumlah Barang'], self.data[i]['Harga Barang']))

    def menu_pembeli(self):
        nama_barang = input("Masukkan nama barang yang ingin dibeli: ")
        jumlah_beli = int(input("Masukkan jumlah barang yang ingin dibeli: "))

        for item in self.data:
            if item['Nama Barang'] == nama_barang:
                if item['Jumlah Barang'] >= jumlah_beli:
                    item['Jumlah Barang'] -= jumlah_beli
                    print("Barang berhasil dibeli.")
                else:
                    print("Jumlah barang tidak mencukupi.")
                    return

        print("Barang tidak ditemukan.")

    def menu_home(self):
        self.clear_screen()
        self.nama_toko()
        print("\t1. Penjual""\t2. Pembeli""\t3. keluar")
        print("-" * 61)

    def run(self):
        self.baca_data_json()
        self.menu_home()
        while True:
            pilih = input("pilih >> ")
            if pilih == '1':
                self.clear_screen()
                self.nama_toko()
                username = input("username : ")
                password = input("password : ")
                if username == "admin" and password == "admin":
                    time.sleep(1)
                    print("LOGIN ANDA BERHASIL.......")
                    time.sleep(1)
                    print("SELAMAT DATANG DI TOKO SUKA-SUKA")
                    time.sleep(1)
                    self.menu_penjual()
                else:
                    print("LOGIN ANDA GAGAL.......")
                    time.sleep(1)
                    exit()
            elif pilih == '2':
                self.clear_screen()
                self.menu_pembeli()
                pembeli = input("pilih [1/2/3]>> ")
                time.sleep(1)
                if pembeli == '1':
                    self.clear_screen()
                    self.show_admin()
                    nama_barang = input("Nama Barang : ")
                    jumlah_beli = int(input("Jumlah Barang : "))
                    barang_ditemukan, barang = self.cari_barang(nama_barang)
                    if barang_ditemukan and barang['Jumlah Barang'] >= jumlah_beli:
                        barang['Jumlah Barang'] -= jumlah_beli
                        self.tulis_data_json()
                        keranjang = jumlah_beli * barang['Harga Barang']
                        self.total += keranjang
                        print("{:61}".format("Barang Berhasil ditambah"))
                    else:
                        print("Barang tidak ditemukan atau stok tidak cukup.")
                    time.sleep(1)
                elif pembeli == '2':
                    self.clear_screen()
                    self.nama_toko()
                    for i in range(len(self.data)):
                        print(self.data[i]["Nama Barang"], ">--->", self.data[i]["Jumlah Barang"])
                    kondisi = True
                    print("total Rp.", self.total)
                    while kondisi:
                        uang = int(input("Bayar : "))
                        kembalian = uang - self.total
                        if kembalian < 0:
                            kondisi = True
                        else:
                            kondisi = False
                            time.sleep(1)
                    self.clear_screen()
                    self.nama_toko()
                    for i in range(len(self.data)):
                        print(self.data[i]["Nama Barang"], ">--->", self.data[i]["Jumlah Barang"])
                    print("total Rp.", self.total)
                    print("Kembalian Rp.", kembalian)
                    print("{:^61}".format("TERIMA KASIH TELAH BERBELANJA DI TOKO SUKA-SUKA"))
                    print("{:^61}".format("SEMOGA HARI-HARI ANDA MENYENANGKAN"))
                    time.sleep(1)
                    exit()
                elif pembeli == '3':
                    self.menu_home()
                else:
                    print("{:^61}".format("Maaf pilihan anda tidak ada"))
                    self.back()
            else:
                exit()

    def back(self):
        print()
        print("TUNGGU SEBENTAR....")
        time.sleep(1)
        self.menu_home()

    def nama_toko(self):
        print("-" * 61)
        print("{:^61}".format("SELAMAT DATANG DI WARMINDO DEPELE"))
        print("{:^61}".format(""" Jl. Mastrip No.29, Krajan Timur, Sumbersari, Kec. Sumbersari
                Kabupaten Jember, Jawa Timur 68123"""))
        print("-" * 61)

if __name__ == '__main__':
    inventory = InventoryManagement()
    inventory.run()
