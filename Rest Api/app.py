from doctest import debug
from flask import Flask
from flask_restful import Resource,Api
app=Flask(__name__)
api=Api(app)

hoteis=[
    {
        'hotel_id':'alpha',
        'nome':'Alpha Hotel',
        'estrela':4.3,
        'diaria':420.34
    }
    {
        'hotel_id':'beta',
        'nome':'Alpha Hotel',
        'estrela':4.3,
        'diaria':420.34
    }
    {
        'hotel_id':'alpha',
        'nome':'Alpha Hotel',
        'estrela':4.3,
        'diaria':420.34
    }
]
class Hoteis(Resource):
    def get (self):
        return {'hoteis':'meus hoteis'}
    
api.add_resource(Hoteis,'/hoteis')

if __name__=='__main__':
    app.rum(debug=True)