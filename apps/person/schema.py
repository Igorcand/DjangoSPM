from datetime import date
from ninja import Schema

class PersonSchema(Schema):
    nome_razao_social: str 
    tipo_pessoa: str 

class PhysicalPersonSchema(Schema):
    pessoa_id: str 
    cpf: str 
    rg: str 
    nascimento: str

class EntityPersonSchema(Schema):
    pessoa_id: str 
    cnpj: str 
    nome_fantasia: str 
    responsavel: str 




