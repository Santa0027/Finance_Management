from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Service
from django.contrib import messages

def dashboard(request):
    categories = Category.objects.all()
    services = Service.objects.all()
    return render(request, 'service.html', {'categories': categories, 'services': services})

def add_category(request):
    if request.method == "POST":
        name = request.POST.get('category_name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        Category.objects.create(name=name, description=description, status=status)
        messages.success(request, "Category added successfully.")
    return redirect('service')


def add_service(request):
    if request.method == "POST":
        name = request.POST.get('service_name')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        category = get_object_or_404(Category, id=category_id, is_active=True)  # Ensure it's active
        Service.objects.create(name=name, category=category, description=description)
        messages.success(request, "Service added successfully.")
        return redirect('service')
    
    # For GET request: load only active categories
    active_categories = Category.objects.filter(is_active=True)
    return render(request, 'service', {'categories': active_categories})


def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.name = request.POST.get('category_name')
        category.description = request.POST.get('description')
        category.status = request.POST.get('status')
        category.save()
        messages.success(request, "Category updated successfully.")
    return redirect('service')

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    messages.success(request, "Category deleted successfully.")
    return redirect('service')

def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        service.name = request.POST.get('service_name')
        service.category_id = request.POST.get('category')
        service.description = request.POST.get('description')
        service.save()
        messages.success(request, "Service updated successfully.")
    return redirect('service')

def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    messages.success(request, "Service deleted successfully.")
    return redirect('service')
