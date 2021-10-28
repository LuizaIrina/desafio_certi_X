from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///numerosextenso.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Numeros(Base):
    __tablename__ = 'numeros'
    indice = Column(Integer, primary_key=True)
    unidade = Column(String(20), index=True)
    dezena = Column(String(20), index=True)
    centena = Column(String(20), index=True)
    dezenaDez = Column(String(20), index=True)

    def save(self):
        db_session.add(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)

def insere_dados():
    um = Numeros(indice=1, unidade='um',dezena='dez', centena='cento', dezenaDez='onze')
    um.save()
    dois = Numeros(indice=2, unidade='dois',dezena='vinte', centena='duzentos', dezenaDez='doze')
    dois.save()
    tres = Numeros(indice=3, unidade='tres', dezena='trinta', centena='trezentos', dezenaDez='treze')
    tres.save()
    quatro = Numeros(indice=4, unidade='quatro', dezena='quarenta', centena='quatrocentos', dezenaDez='quatorze')
    quatro.save()
    cinco = Numeros(indice=5, unidade='cinco', dezena='cinquenta', centena='quinhentos', dezenaDez='quinze')
    cinco.save()
    seis = Numeros(indice=6, unidade='seis', dezena='sessenta', centena='seicentos', dezenaDez='dezesseis')
    seis.save()
    sete = Numeros(indice=7, unidade='sete', dezena='setenta', centena='setecentos', dezenaDez='dezessete')
    sete.save()
    oito = Numeros(indice=8, unidade='oito', dezena='oitenta', centena='oitocentos', dezenaDez='dezoito')
    oito.save()
    nove = Numeros(indice=9, unidade='nove', dezena='noventa', centena='novecentos', dezenaDez='dezenove')
    nove.save()
    #print(pessoa)


if __name__ == '__main__':
    init_db()
    insere_dados()