from ninja import NinjaAPI

from django.contrib import admin
from django.urls import path
from apps.person.routes import router as person_router
from apps.info.routes import router as info_router
# from apps.products.routes import router as products_router
# from apps.transactions.routes import router as shopping_router
# from apps.payment.routes import router as payment_router



api = NinjaAPI()

api.add_router("/person/", person_router)
api.add_router("/info/", info_router)
# api.add_router("/products/", products_router)
# api.add_router("/shopping/", shopping_router)
# api.add_router("/payment/", payment_router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
