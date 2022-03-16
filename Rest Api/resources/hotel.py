from flask_restful import Resource
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
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id']== hotel_id:
               return hotel
        return {'massage':'Hotel not found'},404 #not found
    
    def post(self, hotel_id):
        pass
    
    def put (self , hotel_id):
        pass
    
    def delete(self , hotel_id):
        pass
    