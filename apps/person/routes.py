from ninja import Router
from .models import Person, Physical, Juridical
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

from .schema import PersonSchema, PhysicalPersonSchema, EntityPersonSchema

router = Router()

@router.get('person/', tags=['Person'])
def list_person(request, person_id: str):
    person = get_object_or_404(Person, id=person_id)
    return model_to_dict(person)

@router.get('physical_person_/', tags=['Person'])
def list_physical_person_(request, person_id: str):
    person = get_object_or_404(Physical, pessoa=person_id)
    return model_to_dict(person)

@router.get('juridical_person/', tags=['Person'])
def list_entity_person(request, person_id: str):
    person = get_object_or_404(Juridical, pessoa=person_id)
    return model_to_dict(person)

@router.post('person/', tags=['Person'])
def create_person(request, requirements: PersonSchema):
    person = Person.objects.create(**requirements.dict())
    return {"id": person.id}

@router.post('physical_person/', tags=['Person'])
def create_physical_person(request, requirements: PhysicalPersonSchema):
    dict_requirements = requirements.dict()
    person = Physical.objects.create(**dict_requirements)
    return model_to_dict(person)

@router.post('juridical_person/', tags=['Person'])
def create_entity_person(request, requirements: EntityPersonSchema):
    dict_requirements = requirements.dict()
    person = Juridical.objects.create(**dict_requirements)
    return model_to_dict(person)

@router.delete('person/', tags=['Person'])
def delete_person(request, person_id: str):
    person = get_object_or_404(Person, id=person_id)
    person.delete()
    return {"success": True}

@router.delete('physical_person/', tags=['Person'])
def delete_physical_person(request, person_id: str):
    person = get_object_or_404(Physical, pessoa=person_id)
    person.delete()
    return {"success": True}

@router.delete('juridical_person/', tags=['Person'])
def delete_entity_person(request, person_id: str):
    person = get_object_or_404(Juridical, pessoa=person_id)
    person.delete()
    return {"success": True}