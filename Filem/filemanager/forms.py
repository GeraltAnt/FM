from django import forms
from .models import FileUpload, Item

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['site', 'item', 'process', 'file']

    def __init__(self, *args, **kwargs):
        super(FileUploadForm, self).__init__(*args, **kwargs)
        self.fields['item'].queryset = Item.objects.none()

        if 'site' in self.data:
            try:
                site_id = int(self.data.get('site'))
                self.fields['item'].queryset = Item.objects.filter(site_id=site_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['item'].queryset = self.instance.site.items.order_by('name')

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['site', 'name']
