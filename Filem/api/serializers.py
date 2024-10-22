# api/serializers.py

from rest_framework import serializers
from filemanager.models import Site, Item, BusinessProcess, FileUpload

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'name']

class ItemSerializer(serializers.ModelSerializer):
    site = SiteSerializer(read_only=True)  # 嵌套序列化器以获取站点名称
    site_id = serializers.PrimaryKeyRelatedField(
        queryset=Site.objects.all(),
        write_only=True,
        source='site'
    )

    class Meta:
        model = Item
        fields = ['id', 'name', 'site', 'site_id']

class BusinessProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProcess
        fields = ['id', 'name']

class FileUploadSerializer(serializers.ModelSerializer):
    site = SiteSerializer(read_only=True)
    item = ItemSerializer(read_only=True)
    process = BusinessProcessSerializer(read_only=True)
    site_id = serializers.PrimaryKeyRelatedField(
        queryset=Site.objects.all(),
        write_only=True,
        source='site'
    )
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all(),
        write_only=True,
        source='item'
    )
    process_id = serializers.PrimaryKeyRelatedField(
        queryset=BusinessProcess.objects.all(),
        write_only=True,
        source='process'
    )

    class Meta:
        model = FileUpload
        fields = ['id', 'site', 'item', 'process', 'file', 'uploaded_at', 'site_id', 'item_id', 'process_id']
