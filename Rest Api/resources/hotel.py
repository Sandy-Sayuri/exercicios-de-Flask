import re
from tkinter import NO
from flask_restful import Resource,reqparse

hoteis=[{
    "hotel_id":"alpha",
    "nome":"Alpha Hotel",
    "estrelas":4.3,
    "diaria":420.34,
    "cidades":"Rio de Janeiro"
    },
    {
    "hotel_id":"bravo",
    "nome":"Bravo Hotel",
    "estrelas":4.4,
    "diaria":380.90,
    "cidades":"Santa Catarina"
    },
    {
    "hotel_id":"charlie",
    "nome":"Charlie Hotel",
    "estrelas":3.9,
    "diaria":320.20,
    "cidades":"Santa Catarina"
    }]
class Hoteis(Resource):
    def get(self):
        return{'hoteis':hoteis}
    
    
    
class Hotel(Resource):
    def buscar_hotel(hotel_id):
        for hotel in hoteis:
            if(hotel['hotel_id']==hotel_id):
                return hotel
        return None #not found
    
    
    def novo_hotel():
        argumento=reqparse.RequestParser()
        argumento.add_argument('nome')
        argumento.add_argument('estrelas')
        argumento.add_argument('diaria')
        argumento.add_argument('cidades')
    def get(self,hotel_id):
        hotel=Hotel.buscar_hotel(hotel_id)
        if hotel != None:
            return hotel
        return{'message':'Hotel not found'},404#not found
    def post(self,hotel_id):
        argumetos=reqparse.RequestParser()
        argumetos.add_argument('nome')
        argumetos.add_argument('estrelas')
        argumetos.add_argument('diaria')
        argumetos.add_argument('cidade')
        
        dados=argumetos.parse_args()
        novo_hotel={
            'hotel_id':hotel_id,
            'nome':dados['nome'],
            'estrelas':dados['estrelas'],
            'diaria':dados['diaria'],
            'cidade':dados['cidade']
        }
        hoteis.append(novo_hotel)
        return novo_hotel,200
    def put(self,hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id']==hotel_id:
                return hotel
    def delete(self,hotel_id):
        pass
    
        