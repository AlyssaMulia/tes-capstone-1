import mysql.connector

class Database:
    def __init__(self):
        self.connect()

    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="",   
            database="Wisata_kaltim")
            
        myCursor = self.connection.cursor() 
        myCursor.execute("USE wisata_kaltim")

    def find_nama_id(self, nama_user, id_user):
        query = "SELECT * FROM Pengunjung WHERE Nama_Pengunjung = %s AND ID_Pengunjung = %s"
        values = (nama_user, id_user)
        
        myCursor = self.connection.cursor() 
        myCursor.execute(query, values)  # Eksekusi kueri dengan menggunakan variabel values
        myresult = myCursor.fetchall()   # Ambil hasil dari kueri
        
        return myresult  # Mengembalikan hasil kueri
    
    def find_admin(self, username, password):
        query = "SELECT * FROM Admin WHERE Username = %s AND password = %s"
        values = (username, password)
        
        myCursor = self.connection.cursor() 
        myCursor.execute(query, values)  # Eksekusi kueri dengan menggunakan variabel values
        myresult = myCursor.fetchall()   # Ambil hasil dari kueri

        return myresult 
    
    def find_bookmark(self, wisata_bookmark):
        query = "SELECT * FROM Wisata WHERE Nama_Wisata = %s"
        values = (wisata_bookmark)
        
        myCursor = self.connection.cursor() 
        myCursor.execute(query, values)
        myresult = myCursor.fetchall()

        return myresult 
    
    def registrasi(self, nama_user, gender, usia):
        query = "INSERT INTO Pengunjung (ID_Pengunjung, Nama_Pengunjung, Jenis_Kelamin, Umur) VALUES (NULL, %s, %s, %s)"
        values = (nama_user, gender, usia)

        myCursor = self.connection.cursor() 
        myCursor.execute(query, values) 
        self.connection.commit()

        return myCursor.lastrowid

    def get_wisata(self):
        myCursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM Wisata"
        myCursor.execute(query)
        return myCursor.fetchall()

    def tambah_bookmark(self, tanggal_sekarang, wisata_bookmark, id_user):
        myCursor = self.connection.cursor()
        query = "INSERT INTO Bookmark (Tanggal_Ditandai, Destinasi_Wisata, ID_Pengunjung) VALUES (%s, %s, %s)"
        values = (tanggal_sekarang, wisata_bookmark, id_user)
        myCursor.execute(query, values)
        self.connection.commit()
    
    def lihat_bookmark(self, id_user):
        myCursor = self.connection.cursor()
        query = "SELECT * FROM Bookmark WHERE ID_Pengunjung = %s"
        myCursor.execute(query, (id_user,))
        return myCursor.fetchall()
    
    def find_profil(self, id_user):
        myCursor = self.connection.cursor()
        query = "SELECT * FROM Pengunjung WHERE ID_Pengunjung = %s"
        myCursor.execute(query, (id_user,))
        pengunjung = myCursor.fetchone()
        return pengunjung
    
    def lihat_sponsor(self):
        myCursor = self.connection.cursor()
        query = "SELECT * FROM Sponsor"
        myCursor.execute(query)
        return myCursor.fetchall()

    def tambah_sponsor (self, jenis, kontak, alamat, bentuk):
        myCursor = self.connection.cursor()
        query = "INSERT INTO Sponsor (Jenis_Sponsor, Kontak, Alamat, Bentuk_Sponsor) VALUES (%s, %s, %s, %s)"
        values = (jenis, kontak, alamat, bentuk)
        myCursor.execute(query, values)
        self.connection.commit()
