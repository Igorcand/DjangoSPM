from ninja import Router
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from .models import Email, Address, Phone, Bank, Document
from .schema import EmailSchema,  AddressSchema, PhoneSchema, BankSchema, DocumentSchema
from apps.info.models import Person

router = Router()

@router.get('email/', tags=['Info'])
def get_emails(request, email_id:str):
    email = get_object_or_404(Email, id=email_id)
    return model_to_dict(email)

@router.get('address/', tags=['Info'])
def get_address(request, address_id:str):
    address = get_object_or_404(Address, id=address_id)
    return model_to_dict(address)

@router.get('phone/', tags=['Info'])
def get_phones(request, phone_id:str):
    phone = get_object_or_404(Phone, id=phone_id)
    print(f'phone = {phone}')
    return model_to_dict(phone)

@router.get('bank/', tags=['Info'])
def get_bank(request, bank_id:str):
    bank = get_object_or_404(Bank, id=bank_id)
    return model_to_dict(bank)

@router.get('document/', tags=['Info'])
def get_document(request, document_id:str):
    document = get_object_or_404(Document, id=document_id)
    return model_to_dict(document)

@router.post('email/', tags=['Info'])
def create_email(request, requirements: EmailSchema):
    requirements = requirements.dict()
    person = get_object_or_404(Person, id=requirements['pessoa_id'])

    email = Email.objects.create(pessoa_email=person, email=requirements['email'])
    return model_to_dict(email)

@router.post('phone/', tags=['Info'])
def create_phone(request, requirements: PhoneSchema):
    requirements = requirements.dict()
    person = get_object_or_404(Person, id=requirements['pessoa_id'])
    del requirements['pessoa_id']
    phone = Phone.objects.create(pessoa_tel=person, **requirements)
    return model_to_dict(phone)

@router.post('bank/', tags=['Info'])
def create_bank(request, requirements: BankSchema):
    requirements = requirements.dict()
    person = get_object_or_404(Person, id=requirements['pessoa_id'])
    del requirements['pessoa_id']
    bank = Bank.objects.create(pessoa_banco=person, **requirements)
    return model_to_dict(bank)

@router.post('document/', tags=['Info'])
def create_document(request, requirements: DocumentSchema):
    requirements = requirements.dict()
    person = get_object_or_404(Person, id=requirements['pessoa_id'])
    del requirements['pessoa_id']
    document = Document.objects.create(pessoa_documento=person, **requirements)
    return model_to_dict(document)

@router.post('address/', tags=['Info'])
def create_address(request, requirements: AddressSchema):
    requirements = requirements.dict()
    person = get_object_or_404(Person, id=requirements['pessoa_id'])
    del requirements['pessoa_id']
    address = Address.objects.create(pessoa_end=person, **requirements)
    return model_to_dict(address)

@router.put('email/', tags=['Info'])
def update_email(request, email_id: str, requirements: EmailSchema):
    email = get_object_or_404(Email, id=email_id)
    for attr, value in requirements.dict().items():
        setattr(email, attr, value)
    email.save()
    return {"success": True}

@router.put('phone/', tags=['Info'])
def update_phone(request, phone_id: str, requirements: PhoneSchema):
    phone = get_object_or_404(Phone, id=phone_id)
    for attr, value in requirements.dict().items():
        setattr(phone, attr, value)
    phone.save()
    return {"success": True}

@router.put('address/', tags=['Info'])
def update_address(request, address_id: str, requirements: AddressSchema):
    address = get_object_or_404(Address, id=address_id)
    for attr, value in requirements.dict().items():
        setattr(address, attr, value)
    address.save()
    return {"success": True}

@router.delete('email/', tags=['Info'])
def delete_email(request, email_id: str):
    email = get_object_or_404(Email, id=email_id)
    email.delete()
    return {"success": True}

@router.delete('phone/', tags=['Info'])
def delete_phone(request, phone_id: str):
    phone = get_object_or_404(Phone, id=phone_id)
    phone.delete()
    return {"success": True}

@router.delete('address/', tags=['Info'])
def delete_address(request, address_id: str):
    address = get_object_or_404(Address, id=address_id)
    address.delete()
    return {"success": True}

@router.delete('document/', tags=['Info'])
def delete_document(request, document_id: str):
    document = get_object_or_404(Document, id=document_id)
    document.delete()
    return {"success": True}

@router.delete('bank/', tags=['Info'])
def delete_bank(request, bank_id: str):
    bank = get_object_or_404(Bank, id=bank_id)
    bank.delete()
    return {"success": True}

