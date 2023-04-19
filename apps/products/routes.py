from ninja import Router
from .models import Category, Brand, Unit, Product
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from .schema import *

router = Router()

@router.get('list_categories/', tags=['Products'])
def list_categories(request):
    cats = Category.objects.all()
    response = [
        {'id': i.id, 
        'cat': i.category, 
        } for i in cats]
    return response

@router.get('list_brands/', tags=['Products'])
def list_brands(request):
    brands = Brand.objects.all()
    response = [
        {'id': i.id, 
        'marca': i.brand, 
        } for i in brands]
    return response

@router.get('list_units/', tags=['Products'])
def list_units(request):
    units = Unit.objects.all()
    response = [
        {'id': i.id, 
        'acronym': i.acronym, 
        'unit': i.unit, 
        } for i in units]
    return response

@router.get('list_products/', tags=['Products'])
def list_products(request):
    products = Product.objects.all()
    response = [
        {'id': i.id, 
        'name': i.name, 
        'category': i.category.category, 
        'brand': i.brand.brand, 
        'unit': i.unit.unit, 
        'stock': i.stock, 
        } for i in products]
    return response

@router.get('get_category/', tags=['Products'])
def get_email(request, category_id:str):
    category = get_object_or_404(Category, id=category_id)
    return model_to_dict(category)

@router.get('get_brand/', tags=['Products'])
def get_brand(request, brand_id:str):
    brand = get_object_or_404(Brand, id=brand_id)
    return model_to_dict(brand)

@router.get('get_unit/', tags=['Products'])
def get_unit(request, unit_id:str):
    unit = get_object_or_404(Unit, id=unit_id)
    return model_to_dict(unit)

@router.get('get_product/', tags=['Products'])
def get_product(request, product_id:str):
    product = get_object_or_404(Product, id=product_id)
    return model_to_dict(product)

@router.post('create_category/', tags=['Products'])
def create_category(request, requirements: CategorySchema):
    cat = Category.objects.create(**requirements.dict())
    return model_to_dict(cat)

@router.post('create_brand/', tags=['Products'])
def create_brand(request, requirements: BrandSchema):
    brand = Brand.objects.create(**requirements.dict())
    return model_to_dict(brand)

@router.post('create_unit/', tags=['Products'])
def create_unit(request, requirements: UnitSchema):
    unit = Unit.objects.create(**requirements.dict())
    return model_to_dict(unit)

@router.post('create_product/', tags=['Products'])
def create_product(request, requirements: ProductSchema):
    product = Product.objects.create(**requirements.dict())
    return model_to_dict(product)

@router.put('update_product/', tags=['Products'])
def update_product(request, product_id: str, requirements: ProductSchema):
    product = get_object_or_404(Product, id=product_id)
    requirements = requirements.dict()
    for attr, value in requirements.items():
        setattr(product, attr, value)
    product.save()
    return {"success": True}


@router.delete('delete_category/', tags=['Products'])
def delete_email(request, category_id:str):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return {"success": True}

@router.delete('delete_brand/', tags=['Products'])
def delete_brand(request, brand_id:str):
    brand = get_object_or_404(Brand, id=brand_id)
    brand.delete()
    return {"success": True}

@router.delete('delete_unit/', tags=['Products'])
def delete_unit(request, unit_id:str):
    unit = get_object_or_404(Unit, id=unit_id)
    unit.delete()
    return {"success": True}

@router.delete('delete_product/', tags=['Products'])
def delete_product(request, product_id:str):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return {"success": True}

