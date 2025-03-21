from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Service
from django.contrib import messages
from django.http import JsonResponse


def dashboard(request):
    categories = Category.objects.all()
    services = Service.objects.all()
    return render(request, 'service.html', {'categories': categories, 'services': services})

def add_category(request):
    if request.method == "POST":
        name = request.POST['category_name']
        description = request.POST['description']
        status = request.POST['status']
        Category.objects.create(name=name, description=description, status=status)
    return redirect('service')

def add_service(request):
    if request.method == "POST":
        name = request.POST['service_name']
        category_id = request.POST['category']
        description = request.POST['description']
        category = get_object_or_404(Category, id=category_id)
        Service.objects.create(name=name, category=category, description=description)
    return redirect('service')


def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.description = request.POST.get('description')
        category.save()
        return redirect('dashboard')  # Redirect after update

    return render(request, 'service/edit_category.html', {'category': category})

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('service') 

def edit_service(request):
    if request.method == "POST":
        service_id = request.POST.get("service_id")
        service = get_object_or_404(Service, id=service_id)

        service.name = request.POST.get("name")
        service.description = request.POST.get("description")
        service.save()

        return JsonResponse({"success": True})

    return JsonResponse({"success": False}, status=400)


def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    messages.success(request, "Service deleted successfully.")
    return redirect('dashboard')