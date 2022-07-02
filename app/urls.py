# countries/urls.py
from django.urls import path, include
#from rest_framework.routers import DefaultRouter
from . import views
from django.conf import settings
from django.conf.urls.static import static
# router = DefaultRouter(trailing_slash=False)
# router.register("cta", views.CarViewSet)

urlpatterns = [
    #path("car-api", include(router.urls)),
    path('<slug:pk>/', views.CarDetailView.as_view(), name='car-detail'),
    path("", views.CarListView.as_view(), name='list-cars'),
    path("searches", views.get_search_data, name='search-data'),

]
