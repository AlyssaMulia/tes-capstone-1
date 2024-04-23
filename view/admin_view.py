from Controller.ControllerAccount import Account
from Controller.ControllerLinkedList import LinkedList
from View import user_view
from View import main_view
import os

ll = LinkedList()
acc = Account()

def login_admin():
    while True :
        try :
            print("===================================")
            print("            LOGIN ADMIN           ")
            print("===================================")
            username = str(input("Masukan Username : "))
            password= int(input("Masukan Password : "))
            account = Account()

            result = account.find_admin (username, password)
            if result:
                print("     <<<    Login berhasil!    >>>\n")
                menu_admin()
                break
            else:
                print("Nama pengunjung atau ID tidak cocok.")

        except KeyboardInterrupt:
            print("tidak valid")

def menu_admin():
        try:
            while True:
                print("+----------------------------------+")
                print("|            MENU ADMIN            |")
                print("+----------------------------------+")
                print("|                                  |")
                print("|         1. Tambah Wisata         |")
                print("|         2. Lihat Wisata          |")
                print("|         3. Edit Wisata           |")
                print("|         4. Hapus Wisata          |")
                print("|         5. Cari Wisata           |")
                print("|         6. Urutkan Wisata        |")
                print("|         7. Hubungi Sponsor       |")
                print("|         8. keluar                |")
                print("|                                  |")
                print("+----------------------------------+")
                opsi = str(input("Pilih opsi anda (1/2/3/4/5): "))

                if opsi == '1':
                    os.system('cls')
                    pass
                elif opsi == '2':
                    os.system('cls')
                    ll.tampilkan_wisata()
                elif opsi == '3':
                    os.system('cls')
                    pass
                elif opsi == '4':
                    os.system('cls')
                    pass
                elif opsi == '5':
                    pass
                elif opsi == '6':
                    pass
                elif opsi == '7':
                    pass
                elif opsi == '8':
                    pass
                else:
                    print("Opsi tidak tersedia!")

        except KeyboardInterrupt:
            print("\nTerjadi Kesalahan!")

def create():
    print("====================================")
    print("|       TAMBAH TEMPAT WISATA       |")
    print("====================================")
    
