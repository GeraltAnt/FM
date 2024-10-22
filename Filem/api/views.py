# api/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from filemanager.models import Site, Item, BusinessProcess, FileUpload
from .serializers import (
    SiteSerializer,
    ItemSerializer,
    BusinessProcessSerializer,
    FileUploadSerializer,
)
from rest_framework.parsers import MultiPartParser, FormParser

# 获取站点列表
class SiteListView(generics.ListAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = []  # 允许任何人访问

# 获取物品列表，支持按站点过滤
class ItemListView(generics.ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = []  # 允许任何人访问

    def get_queryset(self):
        site_id = self.request.query_params.get('site', None)
        if site_id:
            return Item.objects.filter(site_id=site_id)
        return Item.objects.all()

# 获取业务流程列表
class BusinessProcessListView(generics.ListAPIView):
    queryset = BusinessProcess.objects.all()
    serializer_class = BusinessProcessSerializer
    permission_classes = []  # 允许任何人访问

# 获取文件列表
class FileUploadListView(generics.ListAPIView):
    serializer_class = FileUploadSerializer
    permission_classes = []  # 允许任何人访问

    def get_queryset(self):
        queryset = FileUpload.objects.all()
        site_id = self.request.query_params.get('site', None)
        item_id = self.request.query_params.get('item', None)
        process_id = self.request.query_params.get('process', None)
        if site_id:
            queryset = queryset.filter(site_id=site_id)
        if item_id:
            queryset = queryset.filter(item_id=item_id)
        if process_id:
            queryset = queryset.filter(process_id=process_id)
        return queryset.order_by('-uploaded_at')

# 上传文件视图
class FileUploadView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = []  # 允许任何人访问

    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# 添加物品视图
class AddItemView(generics.CreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = []  # 允许任何人访问

# 删除物品视图
class DeleteItemView(APIView):
    permission_classes = []  # 允许任何人访问

    def delete(self, request, item_id, format=None):
        try:
            item = Item.objects.get(id=item_id)
            item.delete()
            return Response(status=204)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=404)

# 删除文件视图
class DeleteFileView(generics.DestroyAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    permission_classes = []  # 允许任何人访问
    lookup_url_kwarg = 'file_id'