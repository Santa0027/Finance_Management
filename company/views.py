from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Company, Individual
from .forms import CompanyForm, IndividualForm  # create Django ModelForms for validation
from django.shortcuts import render,redirect
from django.contrib import messages

def company_list(request):
    companies = Company.objects.all()
    individuals = Individual.objects.all()
    form = CompanyForm()
    return render(request, 'company/company_list.html', {
        'companies': companies,
        'form': form,
        'individuals': individuals  # ✅ FIXED HERE
    })

def company_add(request):
    
    if request.method == 'POST':
        print("Received company add request")
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request method'})

def company_edit(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return JsonResponse({'success': False, 'errors': 'Company not found'})

    if request.method == 'POST':
        print("Received company add request")
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request method'})

def company_delete(request, id):
    if request.method == 'POST':
        try:
            company = Company.objects.get(id=id)
            company.delete()
            return JsonResponse({'success': True})
        except Company.DoesNotExist:
            return JsonResponse({'success': False, 'errors': 'Company not found'})
    return JsonResponse({'success': False, 'errors': 'Invalid request method'})

# Similarly for individual

def individual_add(request):
    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        if not name:
            return JsonResponse({'success': False, 'error': 'Name is required.'}, status=400)

        Individual.objects.create(name=name, email=email, phone=phone)
        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)


def individual_edit(request, id):
    try:
        individual = Individual.objects.get(id=id)
    except Individual.DoesNotExist:
        return JsonResponse({'success': False, 'errors': 'Individual not found'})

    if request.method == 'POST':
        form = IndividualForm(request.POST, instance=individual)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request method'})

def individual_delete(request, id):
    if request.method == 'POST':
        try:
            individual = Individual.objects.get(id=id)
            individual.delete()
            messages.success(request, "Individual deleted successfully.")
        except Individual.DoesNotExist:
            messages.error(request, "Individual not found.")
        return redirect('company:company_list')  # Replace 'company:home' with your main page URL name
    else:
        messages.error(request, "Invalid request method.")
        return redirect('company:company_list')
