from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Invoice, InvoiceItem
from company.models import Company , Individual 
from service.models import Service


from company.models import Company  # Fetch company data
from django.views.decorators.csrf import csrf_exempt
import json



def create_invoice(request):
    companies = Company.objects.all()
    individuals = Individual.objects.all()
    services = Service.objects.all()

    if request.method == "POST":
        # extract form data, create Invoice and InvoiceItems
        pass

    return render(request, 'billing/create_invoice.html', {
        'companies': companies,
        'individuals': individuals,
        'services': services
    })
