from ninja import Schema

class CategorySchema(Schema):
    categoria: str 

class BrandSchema(Schema):
    marca: str 

class UnitSchema(Schema):
    sigla_unidade: str 
    unidade: str 

class ProductSchema(Schema):
    codigo: str 
    codigo_barras: str 
    descricao: str 
    categoria_id: str 
    marca_id: str 
    unidade_id: str 
    custo: str 
    venda: str 
    inf_adicionais: str 