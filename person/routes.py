from ninja import Router
from .models import Pessoa, PessoaFisica, PessoaJuridica
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

router = Router()

@router.get('list_all_people/', tags=['Person'])
def list_person(request):
    people = Pessoa.objects.all()

    response = [
        {'id': i.id, 
        'nome_razao_social': i.nome_razao_social, 
        'tipo_pessoa': i.tipo_pessoa, 
        'inscricao_municipal': i.inscricao_municipal, 
        'informacoes_adicionais': i.informacoes_adicionais
        } for i in people]
    return response

@router.get('list_person/', tags=['Person'])
def list_physical_person_(request, person_id: str):
    people = get_object_or_404(Pessoa, id=person_id)
    return model_to_dict(people)

@router.get('list_physical_person_/', tags=['Person'])
def list_physical_person_(request, person_id: str):
    people = get_object_or_404(PessoaFisica, pessoa=person_id)
    return model_to_dict(people)

@router.get('list_entity_person/', tags=['Person'])
def list_entity_person(request, person_id: str):
    people = get_object_or_404(PessoaJuridica, pessoa=person_id)
    return model_to_dict(people)