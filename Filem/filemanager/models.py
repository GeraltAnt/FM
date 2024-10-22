from django.db import models

class Site(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='站点名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '站点'
        verbose_name_plural = '站点'

class Item(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='items', verbose_name='所属站点')
    name = models.CharField(max_length=100, verbose_name='物品名称')

    def __str__(self):
        return f"{self.name} ({self.site.name})"

    class Meta:
        verbose_name = '物品'
        verbose_name_plural = '物品'

class BusinessProcess(models.Model):
    name = models.CharField(max_length=100, verbose_name='业务流程名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '业务流程'
        verbose_name_plural = '业务流程'

class FileUpload(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='files', verbose_name='站点')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='files', verbose_name='物品')
    process = models.ForeignKey(BusinessProcess, on_delete=models.CASCADE, related_name='files', verbose_name='业务流程')
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='文件')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    def __str__(self):
        return f"文件: {self.item.name} - {self.process.name}"

    class Meta:
        verbose_name = '文件上传'
        verbose_name_plural = '文件上传'
