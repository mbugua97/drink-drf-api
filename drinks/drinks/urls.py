from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.drink.as_view(),name='oneurl'),
    path('<int:pk>',views.drinks.as_view(),name='manyurl')
]
