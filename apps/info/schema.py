from datetime import date
from ninja import Schema

class EmailSchema(Schema):
    pessoa_id: str 
    email: str 

class PhoneSchema(Schema):
    pessoa_id: str 
    tipo_telefone: str 
    telefone: str 

class BankSchema(Schema):
    pessoa_id: str 
    banco: str 
    agencia: str 
    conta: str
    digito: str

class DocumentSchema(Schema):
    pessoa_id: str 
    tipo: str 
    documento: str 

class AddressSchema(Schema):
    pessoa_id: str 
    tipo_endereco: str 
    logradouro: str 
    numero: str
    bairro: str 
    pais: str 
    municipio: str 
    uf: str