from ninja import Router

router = Router()

@router.get('shopping/', tags=['Shopping'])
def listar(request):
    return 'na app shopping'