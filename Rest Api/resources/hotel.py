import this
from flask_restful import Resource,reqparse
from models.hotel import HotelModel
hoteis=[
    {
        'hotel_id':'alpha',
        'nome':'Alpha Hotel',
        'estrela':4.3,
        'diaria':420.34,
        'cidade':'Rio de Janeiro'
        
    },
    {
        'hotel_id':'Bravo',
        'nome':'Bravo Hotel',
        'estrela':4.4,
        'diaria':380.90,
        'cidade':'Santa Catarina'
    },
    {
        'hotel_id':'charlie',
        'nome':'Charlie Hotel',
        'estrela':3.9,
        'diaria':320.20,
        'cidade':'Santa Catarina'
    }
]
class Hoteis(Resource):
    def get (self):
        return {'hoteis':hoteis}
    
class Hotel(Resource):
    argumentos=reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
    def busca_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id']== hotel_id:
               return hotel
        return None
    def get(self, hotel_id):
        hotel=Hotel.busca_hotel(hotel_id)
        if hotel != None:
            return hotel    
        return {'massage':'Hotel not found'},404 #not found
    
    
    
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return{'message':f"Hotel id {hotel_id} already exists"},400 
        
        dados=Hotel.argumentos.parse_args()
        hotel_obj=HotelModel(hotel_id,**dados)
        #novo_hotel=hotel_obj.json()#comvertendo os dados para json
        #hoteis.append(novo_hotel)
        #return novo_hotel,200
        hotel_obj.save_hotel()
        return hotel_obj.json()
    
    def put (self , hotel_id):
        dados=Hotel.argumentos.parse_args()
        hotel_obj=HotelModel(hotel_id,**dados)
        novo_hotel=hotel_obj.json()
        hotel=Hotel.busca_hotel(hotel_id)
        if hotel != None:
            hotel.update(novo_hotel)
            return novo_hotel,200 #okk
        hoteis.append(novo_hotel)
        return novo_hotel,201 #created criado
    
    
    def delete(self , hotel_id):
        global hoteis
        hoteis=[ hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id ]
        return{'message':'Hotel deleted.'}
    