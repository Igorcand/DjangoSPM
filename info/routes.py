from ninja import Router

router = Router()

@router.get('info/', tags=['Info'])
def listar(request):
    return 'na app info'