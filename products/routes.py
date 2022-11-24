from ninja import Router
from .models import Categoria, Marca, Unidade, Produto
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from .schema import *

router = Router()

@router.get('list_categories/', tags=['Products'])
def list_categories(request):
    cats = Categoria.objects.all()
    response = [
        {'id': i.id, 
        'cat': i.categoria, 
        } for i in cats]
    return response

@router.get('list_brands/', tags=['Products'])
def list_brands(request):
    marcas = Marca.objects.all()
    response = [
        {'id': i.id, 
        'marca': i.marca, 
        } for i in marcas]
    return response

@router.get('list_units/', tags=['Products'])
def list_units(request):
    units = Unidade.objects.all()
    response = [
        {'id': i.id, 
        'sigla_unidade': i.sigla_unidade, 
        'unidade': i.unidade, 
        } for i in units]
    return response

@router.get('list_products/', tags=['Products'])
def list_products(request):
    products = Produto.objects.all()
    response = [
        {'id': i.id, 
        'codigo': i.codigo, 
        'codigo_barras': i.codigo_barras, 
        'descricao': i.descricao, 
        'categoria': i.categoria.categoria, 
        'marca': i.marca.marca, 
        'unidade': i.unidade.unidade, 
        'custo': i.custo, 
        'venda': i.venda, 
        'inf_adicionais': i.inf_adicionais, 
        } for i in products]
    return response

@router.get('get_category/', tags=['Products'])
def get_email(request, category_id:str):
    category = get_object_or_404(Categoria, id=category_id)
    return model_to_dict(category)

@router.get('get_brand/', tags=['Products'])
def get_brand(request, brand_id:str):
    brand = get_object_or_404(Marca, id=brand_id)
    return model_to_dict(brand)

@router.get('get_unit/', tags=['Products'])
def get_unit(request, unit_id:str):
    unit = get_object_or_404(Unidade, id=unit_id)
    return model_to_dict(unit)

@router.get('get_product/', tags=['Products'])
def get_product(request, product_id:str):
    product = get_object_or_404(Produto, id=product_id)
    return model_to_dict(product)

@router.post('create_category/', tags=['Products'])
def create_category(request, requirements: CategorySchema):
    cat = Categoria.objects.create(**requirements.dict())
    return model_to_dict(cat)

@router.post('create_brand/', tags=['Products'])
def create_brand(request, requirements: BrandSchema):
    brand = Marca.objects.create(**requirements.dict())
    return model_to_dict(brand)

@router.post('create_unit/', tags=['Products'])
def create_unit(request, requirements: UnitSchema):
    unit = Unidade.objects.create(**requirements.dict())
    return model_to_dict(unit)

@router.post('create_product/', tags=['Products'])
def create_product(request, requirements: ProductSchema):
    requirements = requirements.dict()
    brand = get_object_or_404(Marca, id=requirements['marca_id'])
    unit = get_object_or_404(Unidade, id=requirements['unidade_id'])
    category = get_object_or_404(Categoria, id=requirements['categoria_id'])

    del requirements['categoria_id']
    del requirements['unidade_id']
    del requirements['marca_id']

    product = Produto.objects.create(marca=brand, unidade=unit, categoria=category,**requirements)
    return model_to_dict(product)

@router.put('update_category/', tags=['Products'])
def update_category(request, category_id: str, requirements: CategorySchema):
    cat = get_object_or_404(Categoria, id=category_id)
    for attr, value in requirements.dict().items():
        setattr(cat, attr, value)
    cat.save()
    return {"success": True}

@router.put('update_brand/', tags=['Products'])
def update_brand(request, brand_id: str, requirements: BrandSchema):
    brand = get_object_or_404(Categoria, id=brand_id)
    for attr, value in requirements.dict().items():
        setattr(brand, attr, value)
    brand.save()
    return {"success": True}

@router.put('update_unit/', tags=['Products'])
def update_unit(request, unit_id: str, requirements: UnitSchema):
    unit = get_object_or_404(Categoria, id=unit_id)
    for attr, value in requirements.dict().items():
        setattr(unit, attr, value)
    unit.save()
    return {"success": True}

@router.put('update_product/', tags=['Products'])
def update_product(request, product_id: str, requirements: ProductSchema):

    product = get_object_or_404(Produto, id=product_id)

    requirements = requirements.dict()
    brand = get_object_or_404(Marca, id=requirements['marca_id'])
    requirements['marca'] = brand
    unit = get_object_or_404(Unidade, id=requirements['unidade_id'])
    requirements['unidade'] = unit
    category = get_object_or_404(Categoria, id=requirements['categoria_id'])
    requirements['categoria'] = category

    del requirements['categoria_id']
    del requirements['unidade_id']
    del requirements['marca_id']

    for attr, value in requirements.items():
        setattr(product, attr, value)
    product.save()
    return {"success": True}

