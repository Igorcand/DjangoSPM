from ninja import Router
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from .models import Email, Endereco, Telefone, Banco, Documento

router = Router()

@router.get('list_email/', tags=['Info'])
def list_emails(request):
    emails = Email.objects.all()
    response = [
        {'id': i.id, 
        'email': i.email, 
        } for i in emails]
    return response

@router.get('list_address/', tags=['Info'])
def list_address(request):
    addresses = Endereco.objects.all()
    response = [
        {'id': i.id, 
        'tipo_endereco': i.tipo_endereco, 
        'logradouro': i.logradouro, 
        'numero': i.numero, 
        'bairro': i.bairro, 
        'complemento': i.complemento, 
        'pais': i.pais, 
        'cpais': i.cpais, 
        'municipio': i.municipio, 
        'cmun': i.cmun, 
        'cep': i.cep, 
        'uf': i.uf, 
        } for i in addresses]
    return response

@router.get('list_phones/', tags=['Info'])
def list_phones(request):
    phones = Telefone.objects.all()
    response = [
        {'id': i.id, 
        'tipo_telefone': i.tipo_telefone, 
        'telefone': i.telefone, 
        } for i in phones]
    return response

@router.get('list_bank/', tags=['Info'])
def list_bank(request):
    banks = Banco.objects.all()
    response = [
        {'id': i.id, 
        'banco': i.banco, 
        'agencia': i.agencia, 
        'conta': i.conta, 
        'digito': i.digito, 

        } for i in banks]
    return response

@router.get('list_document/', tags=['Info'])
def list_document(request):
    documents = Documento.objects.all()
    response = [
        {'id': i.id, 
        'tipo': i.tipo, 
        'documento': i.documento, 

        } for i in documents]
    return response


@router.get('get_email/', tags=['Info'])
def get_emails(request, email_id:str):
    email = get_object_or_404(Email, pessoa_email=email_id)
    return model_to_dict(email)

@router.get('get_address/', tags=['Info'])
def get_address(request, address_id:str):
    address = get_object_or_404(Endereco, pessoa_end=address_id)
    return model_to_dict(address)

@router.get('get_phones/', tags=['Info'])
def get_phones(request, phone_id:str):
    phone = get_object_or_404(Telefone, pessoa_tel=phone_id)
    return model_to_dict(phone)

@router.get('get_bank/', tags=['Info'])
def get_bank(request, bank_id:str):
    bank = get_object_or_404(Banco, pessoa_banco=bank_id)
    return model_to_dict(bank)

@router.get('get_document/', tags=['Info'])
def get_document(request, document_id:str):
    document = get_object_or_404(Documento, pessoa_documento=document_id)
    return model_to_dict(document)