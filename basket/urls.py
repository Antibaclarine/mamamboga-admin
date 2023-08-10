from django .urls import path
from .views import create_basket

urlpatterns = [
    path("baskets/form",create_basket,name="create_basket_view")
]
