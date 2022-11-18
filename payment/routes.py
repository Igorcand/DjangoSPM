from ninja import Router

router = Router()

@router.get('payment/', tags=['Payment'])
def listar(request):
    return 'na app payment'