from ninja import Router
from .models import Compra, ItensCompra
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

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
