from ninja import Schema

class CategorySchema(Schema):
    category: str 

class BrandSchema(Schema):
    brand: str 

class UnitSchema(Schema):
    acronym: str 
    unit: str 

class ProductSchema(Schema):
    name: str 
    category_id: str 
    brand_id: str 
    unit_id: str 
    add_info: str 