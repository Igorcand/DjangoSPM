from ninja import Router

router = Router()

@router.get('products/', tags=['Products'])
def listar(request):
    return 'na app products'