import sqlite3

class Database:

    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS libro (id INTEGER PRIMARY KEY, titulo text, autor,year integer, isbn integer)")
        self.con.commit()


    def insert(self,titulo, autor, year,isbn):
        self.cur.execute("INSERT INTO libro VALUES (NULL,?,?,?,?)",(titulo, autor, year,isbn))
        self.con.commit()

    def view(self):
        self.cur.execute("SELECT * FROM libro")
        rows=self.cur.fetchall()
        return rows

    def busqueda(self,titulo="",autor="",year="",isbn=""):
        self.cur.execute("SELECT * FROM libro WHERE titulo=? OR autor=? OR year=? OR  isbn=? ",(titulo, autor, year,isbn))
        rows=self.cur.fetchall()
        return rows    

    def delete(self,id):
        self.cur.execute("DELETE FROM libro WHERE id=?", (id,))
        self.con.commit()


    def update(self,id,titulo,autor,year,isbn):
        self.cur.execute("UPDATE libro SET titulo=?, autor=?, year=?, isbn=?  WHERE id=?", (titulo,autor,year,isbn,id))
        self.con.commit()

    def __del__(self):
        self.con.close()


#insert("the moon","John simth",1917, 18348)
#Database.update(3,"The sun","Jhonathan Smooth","1888","3143322")

