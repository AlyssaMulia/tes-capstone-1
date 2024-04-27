from Model.Database import Database
from Model.Wisata import Wisata
from prettytable import PrettyTable
import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def reset_data(self):
        self.head = None

    def refresh(self):
        self.reset_data()
        results = self.get_data()
        for result in results:
            id_wisata = result ["ID_Wisata"]
            nama_wisata = result ["Nama_Wisata"]
            deskripsi = result["Deskripsi"]  # Misalnya, deskripsi berada di indeks ke-1 dalam tuple
            lokasi = result["Lokasi"]     # Misalnya, lokasi berada di indeks ke-2 dalam tuple
            self.add_wisata(id_wisata, nama_wisata, deskripsi, lokasi)

    def get_data(self):
        db = Database()
        return db.get_wisata()

    def lihat_wisata(linked_list):
        current_node = linked_list.head
        while current_node:
            print("ID         :", current_node.id_wisata)
            print("Nama Wisata:", current_node.nama_wisata)
            print("Deskripsi  :", current_node.deskripsi)
            print("Lokasi     :", current_node.lokasi)
            print("--------------------------------------------------------------")
            current_node = current_node.next

    def add_wisata(self, id_wisata, nama_wisata, deskripsi, lokasi):
        wisata_baru = Wisata(id_wisata, nama_wisata, deskripsi, lokasi)
        if self.head is None:
            self.head = wisata_baru
            self.tail = wisata_baru
        else:
            wisata_baru.previous = self.tail
            self.tail.next = wisata_baru
            self.tail = wisata_baru
