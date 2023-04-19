from ninja import Router
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from .models import Email, Address, Phone, Bank, Document
from .schema import EmailSchema,  AddressSchema, PhoneSchema, BankSchema, DocumentSchema

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
    email = Email.objects.create(**requirements.dict())
    return model_to_dict(email)

@router.post('phone/', tags=['Info'])
def create_phone(request, requirements: PhoneSchema):
    phone = Phone.objects.create(**requirements.dict())
    return model_to_dict(phone)

@router.post('bank/', tags=['Info'])
def create_bank(request, requirements: BankSchema):
    bank = Bank.objects.create(**requirements.dict())
    return model_to_dict(bank)

@router.post('document/', tags=['Info'])
def create_document(request, requirements: DocumentSchema):
    document = Document.objects.create(**requirements.dict())
    return model_to_dict(document)

@router.post('address/', tags=['Info'])
def create_address(request, requirements: AddressSchema):
    address = Address.objects.create(**requirements.dict())
    return model_to_dict(address)

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

