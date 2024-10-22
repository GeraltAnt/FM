from django.shortcuts import render, redirect, get_object_or_404
from .models import Site, Item, BusinessProcess, FileUpload
from .forms import FileUploadForm, ItemForm
from django.urls import reverse
from django.http import JsonResponse

def home(request):
    return render(request, 'filemanager/home.html')

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display_files')
    else:
        form = FileUploadForm()
    return render(request, 'filemanager/upload_file.html', {'form': form})

def load_items(request):
    site_id = request.GET.get('site')
    items = Item.objects.filter(site_id=site_id).order_by('name')
    return render(request, 'filemanager/item_dropdown_list_options.html', {'items': items})

def display_files(request):
    sites = Site.objects.all()
    selected_site = request.GET.get('site')
    selected_item = request.GET.get('item')
    selected_process = request.GET.get('process')

    files = FileUpload.objects.all()

    if selected_site:
        files = files.filter(site_id=selected_site)
    if selected_item:
        files = files.filter(item_id=selected_item)
    if selected_process:
        files = files.filter(process_id=selected_process)

    context = {
        'sites': sites,
        'files': files,
        'selected_site': selected_site,
        'selected_item': selected_item,
        'selected_process': selected_process,
        'processes': BusinessProcess.objects.all(),
        'items': Item.objects.filter(site_id=selected_site) if selected_site else Item.objects.none(),
    }
    return render(request, 'filemanager/display_files.html', context)

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_item')
    else:
        form = ItemForm()
    items = Item.objects.all()
    return render(request, 'filemanager/add_item.html', {'form': form, 'items': items})

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('add_item')
