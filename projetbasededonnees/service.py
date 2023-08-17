import mysql.connector

def connection():
    try: #conncetion de la base de donnée
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="application")
        print("Connection établie")

        return conn
    except:
        print("Connection non établie")
    
def ajouter(person): #ajouter une personne
    conn = connection()
    cursor = conn.cursor()

    valeurs = (person.prenom, person.nom, person.photo)
    cursor.execute(""" INSERT INTO person (prenom, nom, photo) VALUES(%s, %s, %s)""", valeurs) #%s variables qui vont être reinseignées
    conn.close()

def parcourir(): 
    conn = connection()
    cursor = conn.cursor()

    cursor.execute(""" SELECT * FROM person""") 
    rows = cursor.fetchall()
    return rows
    conn.close()