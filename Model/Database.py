import mysql.connector

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="",   
            database="Wisata_kaltim" 
        )
        myCursor = self.connection.cursor() 
        myCursor.execute("USE Wisata_Kaltim")

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
    
    def registrasi(self, nama_user, gender, usia):
        query = "INSERT INTO Pengunjung (ID_Pengunjung, Nama_Pengunjung, Jenis_Kelamin, Umur) VALUES (NULL, %s, %s, %s)"
        values = (nama_user, gender, usia)

        myCursor = self.connection.cursor() 
        myCursor.execute(query, values) 

        self.connection.commit()

        return myCursor.lastrowid
