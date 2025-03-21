from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Company
from .forms import CompanyForm

from django.http import JsonResponse

def delete_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    company.delete()
    messages.success(request, "Company deleted successfully!")
    return redirect('company_list')


def company_list(request):
    companies = Company.objects.all()
    form = CompanyForm()
    return render(request, 'company/company_list.html', {'companies': companies, 'form': form})

def add_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Company added successfully!")
            return redirect('company_list')
        else:
            for field, error in form.errors.items():
                messages.error(request, f"{field.capitalize()}: {error.as_text()}")

    # If there are errors, return to the list page with the form data
    companies = Company.objects.all()
    return render(request, 'company/company_list.html', {'companies': companies, 'form': form})

def edit_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, "Company updated successfully!")
            return redirect('company_list')
        else:
            for field, error in form.errors.items():
                messages.error(request, f"{field.capitalize()}: {error.as_text()}")

    # If there are errors, return the form and company list
    companies = Company.objects.all()
    return render(request, 'company/company_list.html', {'companies': companies, 'form': form, 'editing': True, 'company': company})
