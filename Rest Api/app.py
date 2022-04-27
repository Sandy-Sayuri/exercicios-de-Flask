from Flask import Flask
from flask_restful import Api
from  resources.hotel import Hoteis,Hotel
from sql_alchemy import banco
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
api=Api(app)

@app.before_first_request
#criar o bd automarico
def cria_banco():
    banco.create_all()

api.add_resource(Hoteis,'/hoteis')
api.add_resource(Hotel,'/hoteis/<string:hotel_id>')


if __name__=='__main__':
    banco.init_app(app)
    app.run(debug=True)