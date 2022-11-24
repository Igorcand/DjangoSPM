from ninja import Router
from .models import Compra, ItensCompra
from .schema import *
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from products.models import Produto

router = Router()



@router.get('list_shoppings/', tags=['Shopping'])
def list_shoppings(request):
    shoppings = Compra.objects.all()
    response = [
        {'id': i.id, 
        'data_emissao': i.data_emissao, 
        'valor_total': i.valor_total, 
        'desconto': i.desconto, 
        'despesas': i.despesas, 
        'frete': i.frete, 
        'seguro': i.seguro, 
        'observacoes': i.observacoes, 

        } for i in shoppings]
    return response

@router.get('list_itens_shoppings/', tags=['Shopping'])
def list_itens_shoppings(request):
    itens_shoppings = ItensCompra.objects.all()
    response = [
        {'id': i.id, 
        'produto': i.produto.descricao, 
        'compra_id': i.compra_id.id, 
        'quantidade': i.quantidade, 
        'valor_unit': i.valor_unit, 
        'tipo_desconto': i.tipo_desconto, 
        'desconto': i.desconto, 
        'subtotal': i.subtotal, 

        } for i in itens_shoppings]
    return response

@router.get('get_shopping/', tags=['Shopping'])
def get_shopping(request, shopping_id:str):
    shopping = get_object_or_404(Compra, id=shopping_id)
    return model_to_dict(shopping)

@router.get('get_item_shopping/', tags=['Shopping'])
def get_item_shopping(request, shopping_id:str):
    shopping = get_object_or_404(ItensCompra, id=shopping_id)
    return model_to_dict(shopping)

@router.post('create_shopping/', tags=['Shopping'])
def create_category(request, requirements: ShoppingSchema):
    shopping = Compra.objects.create(**requirements.dict())
    return model_to_dict(shopping)

@router.post('create_item_shopping/', tags=['Shopping'])
def create_item_shopping(request, requirements: ItensShoppingSchema):
    requirements = requirements.dict()
    produto = get_object_or_404(Produto, id=requirements['produto_id'])
    requirements['produto'] = produto
    compra = get_object_or_404(Compra, id=requirements['compra_id'])
    requirements['compra_id'] = compra

    del requirements['produto_id']
    items_shopping = ItensCompra.objects.create(**requirements)
    return model_to_dict(items_shopping)

@router.put('update_shopping/', tags=['Shopping'])
def update_shopping(request, shopping_id: str, requirements: ShoppingSchema):
    shopping = get_object_or_404(Compra, id=shopping_id)
    for attr, value in requirements.dict().items():
        setattr(shopping, attr, value)
    shopping.save()
    return {"success": True}

@router.put('update_item_shopping/', tags=['Shopping'])
def update_item_shopping(request, shopping_id: str, requirements: ItensShoppingSchema):

    shopping = get_object_or_404(ItensCompra, id=shopping_id)

    requirements = requirements.dict()
    produto = get_object_or_404(Produto, id=requirements['produto_id'])
    requirements['produto'] = produto
    compra = get_object_or_404(Compra, id=requirements['compra_id'])
    requirements['compra_id'] = compra

    del requirements['produto_id']

    for attr, value in requirements.items():
        setattr(shopping, attr, value)
    shopping.save()
    return {"success": True}


@router.delete('delete_shopping/', tags=['Shopping'])
def delete_shopping(request, shopping_id:str):
    shopping = get_object_or_404(Compra, id=shopping_id)
    shopping.delete()
    return {"success": True}

@router.delete('delete_item_shopping/', tags=['Shopping'])
def delete_item_shopping(request, shopping_id:str):
    shopping = get_object_or_404(ItensCompra, id=shopping_id)
    shopping.delete()
    return {"success": True}
