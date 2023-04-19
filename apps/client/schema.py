from datetime import date
from ninja import Schema

class ClientSchema(Schema):
    name: str 
    type_client: str 

class PhysicalSchema(Schema):
    client_id: str 
    cpf: str 
    rg: str 
    birth: str

class JuridicalSchema(Schema):
    client_id: str 
    cnpj: str 
    fantasy_name: str 
    owner: str 




