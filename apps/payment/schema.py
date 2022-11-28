from ninja import Schema

class PaymentSchema(Schema):
    compra_id: str 
    indice_parcela: int 
    vencimento: str 
    valor_parcela: float 