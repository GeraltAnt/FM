from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_file, name='upload_file'),
    path('load-items/', views.load_items, name='load_items'),
    path('files/', views.display_files, name='display_files'),
    path('add-item/', views.add_item, name='add_item'),
    path('delete-item/<int:item_id>/', views.delete_item, name='delete_item'),
]
