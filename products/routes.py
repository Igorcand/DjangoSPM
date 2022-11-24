from ninja import Router
from .models import Categoria, Marca, Unidade, Produto

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
