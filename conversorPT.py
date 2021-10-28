from modules import Numeros

def converte_numero(num):
    #tam = len(num) #se fosse string pegava por tamanho e posicoes dos algarismos na string
    if num == 0:
        resposta = 'zero'
        return resposta
    elif num < 0:
        resposta = 'menos '
        num = num*-1
    else:
        resposta = ''

    dezenaMilhar,resto = extrai_algarismos(num,10000)
    unidadeMilhar, resto = extrai_algarismos(resto, 1000)
    centena, resto = extrai_algarismos(resto, 100)
    dezena, unidade = extrai_algarismos(resto, 10)


    if dezenaMilhar > 1:
        numero = Numeros.query.filter_by(indice=dezenaMilhar).first()
        num_escrito = numero.dezena
        resposta = resposta+num_escrito
        if unidadeMilhar==0:
            resposta = resposta+' mil'
        elif unidadeMilhar > 0:
            numero = Numeros.query.filter_by(indice=unidadeMilhar).first()
            num_escrito = numero.unidade
            resposta = resposta+' e '+num_escrito+' mil'
    elif dezenaMilhar == 1:
        #onze, doze, treze, quatorze...
        if unidadeMilhar > 0:
            numero = Numeros.query.filter_by(indice=unidadeMilhar).first()
            num_escrito = numero.dezenaDez
            resposta = resposta+num_escrito+' mil'
        else: # unidadeMilhar == 0
            resposta = resposta+' dez '+' mil'
    else: # dezenaMilhar == 0
        if unidadeMilhar > 0:
            numero = Numeros.query.filter_by(indice=unidadeMilhar).first()
            num_escrito = numero.unidade
            resposta = resposta + num_escrito + ' mil'

    if centena > 1:
        if dezenaMilhar or unidadeMilhar != 0:
            resposta = resposta+' e '
        else:
            resposta = resposta
        numero = Numeros.query.filter_by(indice=centena).first()
        num_escrito = numero.centena
        resposta = resposta+num_escrito
    elif centena == 1:
        if dezenaMilhar or unidadeMilhar != 0:
            resposta = resposta + ' e '
        else:
            resposta = resposta
        if dezena==0 and unidade==0:
            resposta = resposta+'cem'
        else:
            numero = Numeros.query.filter_by(indice=centena).first()
            resposta = resposta + numero.centena

    if dezena > 1:
        if dezenaMilhar or unidadeMilhar or centena != 0:
            resposta = resposta + ' e '
        numero = Numeros.query.filter_by(indice=dezena).first()
        resposta = resposta + numero.dezena
    elif dezena == 1:
        if dezenaMilhar or unidadeMilhar or centena != 0:
            resposta = resposta + ' e '
        if unidade > 0:
            # onze, doze, treze...
            numero = Numeros.query.filter_by(indice=unidade).first()
            resposta = resposta + numero.dezenaDez
        else: # unidade == 0
            numero = Numeros.query.filter_by(indice=dezena).first()
            resposta = resposta+numero.dezena
        return resposta

    if unidade > 0:
        if dezenaMilhar or unidadeMilhar or centena or dezena != 0:
            resposta = resposta + ' e '
        numero = Numeros.query.filter_by(indice=unidade).first()
        resposta = resposta + numero.unidade

    return resposta

def extrai_algarismos(valor,ordem):
    resto = valor % ordem
    resposta = int((valor - (resto)) / ordem)
    return resposta,resto