from ninja import Schema

class ShoppingSchema(Schema):
    data_emissao: str 
    valor_total: float 
    desconto: float 
    despesas: float 
    frete: float 
    seguro: float 
    observacoes: str 

class ItensShoppingSchema(Schema):
    produto_id: str 
    compra_id: str 
    quantidade: float 
    valor_unit: float 
    tipo_desconto: str 
    desconto: float 
    subtotal: float 