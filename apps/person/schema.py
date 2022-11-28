from datetime import date
from ninja import Schema

class PersonSchema(Schema):
    nome_razao_social: str 
    tipo_pessoa: str 
    inscricao_municipal: str = None 
    informacoes_adicionais: str = None 

class PhysicalPersonSchema(Schema):
    pessoa_id: str 
    cpf: str 
    rg: str 
    nascimento: str

class EntityPersonSchema(Schema):
    pessoa_id: str 
    cnpj: str 
    nome_fantasia: str 
    inscricao_estadual: str 
    responsavel: str 
    suframa: str 




