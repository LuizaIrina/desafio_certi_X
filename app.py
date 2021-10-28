from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from conversorPT import converte_numero

app = Flask(__name__)
api = Api(app)

class Numero(Resource):
    def get(self,numero):
        try:
            num_verificado = int(numero)
        except ValueError:
            return {'mensagem':'escreva um número entre -99999 e 99999'}
        if num_verificado < -99999 or num_verificado > 99999:
            return {'mensagem': 'escreva um número entre -99999 e 99999'}
        else:
            num_convertido = converte_numero(num_verificado)
            return {'numero':"escreveu {}".format(numero),
                    'numero convertido':num_convertido}
    def post(self,numero):
        return {'erro':'método inválido'}
    def put(self,numero):
        return {'erro':'método inválido'}
    def delete(self,numero):
        return {'erro':'método inválido'}


api.add_resource(Numero,'/<string:numero>')

if __name__=='__main__':
    app.run(debug=True)