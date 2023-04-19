from datetime import date
from ninja import Schema

class EmailSchema(Schema):
    client_id: str 
    email: str 

class PhoneSchema(Schema):
    client_id: str 
    type: str 
    phone: str 

class BankSchema(Schema):
    client_id: str 
    bank: str 
    agency: str 
    acount: str
    digit: str

class DocumentSchema(Schema):
    client_id: str 
    type: str 
    document: str 

class AddressSchema(Schema):
    client_id: str 
    type: str 
    public_place: str 
    number: str
    neighborhood: str 
    country: str 
    city: str 
    uf: str