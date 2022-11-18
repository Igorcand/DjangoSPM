from ninja import Router

router = Router()

@router.get('person/', tags=['Person'])
def listar(request):
    return 'na app person'