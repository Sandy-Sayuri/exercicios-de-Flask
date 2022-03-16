from sql_alchemy import banco
class HotelModel(banco.Model):
    #isso é para  estruturar a tabela
    __tablename__='hoteis'
    hotel_id= banco.Column(banco.String, primary_key=True)
    nome=banco.Column(banco.String(80))
    estrelas=banco.Column(banco.Float(precision=1))
    diaria=banco.Column(banco.Float(precision=2))
    cidade=banco.Column(banco.String(40))
    
    def __init__(self,hotel_id,nome,estrelas,diaria,cidade):
       self.hotel_id= hotel_id
       self.nome=nome
       self.estrelas=estrelas
       self.diaria=diaria
       self.cidade=cidade
       print('oii')
       
    def json(self):
        print('oiii')
        return{
            'holtel_id':self.hotel_id,
            'nome':self.nome,
            'estrelas':self.estrelas,
            'diaria':self.diaria,
            'cidade':self.cidade
        }
    @classmethod
    def find_hotel(cls , hotel_id):
        hotel=cls.query.filter_by(hotel_id= hotel_id).first() 
        if hotel:
            print(hotel)
            return hotel
        print('oiii')
        return None
    
    def save_hotel(self):
        print(banco)
        banco.session.add(self)
        banco.session.commit()