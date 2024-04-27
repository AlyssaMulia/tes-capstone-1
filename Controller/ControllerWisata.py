from Model.Database import Database

class HistoryWisata:
    def __init__(self):
        self.head = None
        self.tail = None
        self.history = []

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

class WisataController:
    def __init__(self, database):
        self.db = database
        
    def add_wisata(self, nama_wisata, lokasi, deskripsi):
        return self.db.add_wisata(nama_wisata, lokasi, deskripsi)
    
    def get_wisata(self):
        results = self.db.get_wisata()
        for result in results:
            print(f"ID: {result[0]}\nNama: {result[1]}\nDeskripsi: {result[2]}\nLokasi: {result[3]}\n")

    def update_wisata(self, wisata_id, nama_wisata, lokasi, deskripsi):
        self.db.update_wisata(wisata_id, nama_wisata, lokasi, deskripsi)
    
    def delete_wisata(self, wisata_id):
        self.db.delete_wisata(wisata_id)
    
    def search_wisata(self, search_query):
        results = self.db.search_wisata(search_query)
        if results:
            for result in results:
                print(f"ID: {result[0]}, Nama: {result[1]}, Lokasi: {result[2]}, Deskripsi: {result[3]}")
        else:
            print("No matching wisata found.")
    
    # def show_sorted_wisata_ascending(self):
    #     results = self.db.get_sorted_wisata_ascending()
    #     if results:
    #         for result in results:
    #             print(f"ID: {result[0]}\nNama: {result[1]}\nLokasi: {result[2]}\nDeskripsi: {result[3]}\n")
    #     else:
    #         print("Tidak ada wisata yang tersedia.")

    
    # def show_sorted_wisata_descending(self):
    #     results = self.db.get_sorted_wisata_descending()
    #     if results:
    #         for result in results:
    #             print(f"ID: {result[0]}\nNama: {result[1]}\nLokasi: {result[2]}\nDeskripsi: {result[3]}\n")
    #     else:
    #         print("Tidak ada wisata yang tersedia.")