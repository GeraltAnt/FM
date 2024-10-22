# api/urls.py

from django.urls import path
from .views import (
    SiteListView,
    ItemListView,
    BusinessProcessListView,
    FileUploadListView,
    FileUploadView,
    AddItemView,
    DeleteItemView,
    DeleteFileView,
)

urlpatterns = [
    path('sites/', SiteListView.as_view(), name='api_sites'),
    path('items/', ItemListView.as_view(), name='api_items'),
    path('business-processes/', BusinessProcessListView.as_view(), name='api_business_processes'),
    path('files/', FileUploadListView.as_view(), name='api_files'),
    path('files/upload/', FileUploadView.as_view(), name='api_upload_file'),
    path('add-item/', AddItemView.as_view(), name='api_add_item'),
    path('delete-item/<int:item_id>/', DeleteItemView.as_view(), name='api_delete_item'),
    path('delete-file/<int:file_id>/', DeleteFileView.as_view(), name='api_delete_file'),
]
