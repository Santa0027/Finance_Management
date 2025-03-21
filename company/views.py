from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Company
from .forms import CompanyForm

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company/company_profile.html', {'companies': companies})

def add_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Company added successfully!") 
            return redirect('company_list')  # Redirect to update list
        else:
            messages.error(request, "Error adding company.")
    else:
        form = CompanyForm()
    
    companies = Company.objects.all()  # Fetch updated data
    return render(request, 'company/company_profile.html', {'form': form, 'companies': companies})

def edit_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, "Company updated successfully!") 
            return redirect('company_list')
        else:
            messages.error(request, "Error updating company.")
    else:
        form = CompanyForm(instance=company)

    return render(request, 'company/edit_company.html', {'form': form, 'company': company})
