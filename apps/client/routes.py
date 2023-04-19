from ninja import Router
from .models import Client, Physical, Juridical
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

from .schema import ClientSchema, PhysicalSchema, JuridicalSchema

router = Router()

@router.get('client/', tags=['Client'])
def list_client(request, client_id: str):
    client = get_object_or_404(Client, id=client_id)
    return model_to_dict(client)

@router.get('physical/', tags=['Client'])
def list_physical(request, client_id: str):
    client = get_object_or_404(Physical, client=client_id)
    return model_to_dict(client)

@router.get('juridical/', tags=['Client'])
def list_juridical(request, client_id: str):
    client = get_object_or_404(Juridical, client=client_id)
    return model_to_dict(client)

@router.post('client/', tags=['Client'])
def create(request, requirements: ClientSchema):
    client = Client.create(**requirements.dict())
    client.save()
    return model_to_dict(client)

@router.post('physical/', tags=['Client'])
def create_physical(request, requirements: PhysicalSchema):
    client = Physical.create(**requirements.dict())
    client.save()
    return model_to_dict(client)

@router.post('juridical/', tags=['Client'])
def create_juridical(request, requirements: JuridicalSchema):
    client = Juridical.create(**requirements.dict())
    client.save()
    return model_to_dict(client)

@router.delete('client/', tags=['Client'])
def delete_client(request, client_id: str):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return {"success": True}

@router.delete('physical/', tags=['Client'])
def delete_physical(request, client_id: str):
    client = get_object_or_404(Physical, client=client_id)
    client.delete()
    return {"success": True}

@router.delete('juridical/', tags=['Client'])
def delete_juridical(request, client_id: str):
    client = get_object_or_404(Juridical, client=client_id)
    client.delete()
    return {"success": True}