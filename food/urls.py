from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home_page'),
    path('item/', views.item, name='item'),
    path('<int:item_id>/', views.details, name='details'),
    path('add_item/', views.create_item, name='create_item'),
    path('update_item/<int:id>/', views.update_item, name="update_item"),
    path("delete<int:id>/", views.delete_item, name="delete_item"),
    
    
]
