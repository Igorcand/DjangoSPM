from ninja import Router
# from .models import Pagamento
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from apps.transactions.models import Compra
from .schema import PaymentSchema

router = Router()

@router.get('list_payments/', tags=['Payment'])
def list_payments(request):
    payments = Pagamento.objects.all()
    response = [
        {'id': i.id, 
        'indice_parcela': i.indice_parcela, 
        'vencimento': i.vencimento, 
        'valor_parcela': i.valor_parcela, 

        } for i in payments]
    return response


@router.get('get_payment/', tags=['Payment'])
def get_payment(request, payment_id:str):
    payment = get_object_or_404(Pagamento, id=payment_id)
    return model_to_dict(payment)

@router.post('create_payment/', tags=['Payment'])
def create_payment(request, requirements: PaymentSchema):
    requirements = requirements.dict()
    compra = get_object_or_404(Compra, id=requirements['compra_id'])
    requirements['compra_id'] = compra
    payment = Pagamento.objects.create(**requirements)
    return model_to_dict(payment)

@router.put('update_payment/', tags=['Payment'])
def update_payment(request, payment_id: str, requirements: PaymentSchema):
    payment = get_object_or_404(Pagamento, id=payment_id)
    requirements = requirements.dict()
    compra = get_object_or_404(Compra, id=requirements['compra_id'])
    requirements['compra_id'] = compra
    for attr, value in requirements.items():
        setattr(payment, attr, value)
    payment.save()
    return {"success": True}

@router.delete('delete_payment/', tags=['Payment'])
def delete_payment(request, payment_id:str):
    payment = get_object_or_404(Pagamento, id=payment_id)
    payment.delete()
    return {"success": True}