from multiprocessing import connection
import sqlite3

connection=sqlite3.connect('banco.bd')
cursor=connection.cursor()

cria_tabela="CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY ,\
    nome text, estrelas real ,diaria real, cidade text)"

cria_hotel="INSERT INTO hoteis VALUES ('Alpha','Alpha Hotel', 4.3 , 345.30, 'Rio de Janeiro')"
cursor.execute(cria_tabela)
cursor.execute(cria_hotel)
connection.commit
connection.close()