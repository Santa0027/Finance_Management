from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Invoice, InvoiceItem
from company.models import Company  # Fetch company data
from django.views.decorators.csrf import csrf_exempt
import json





def billing(request):
    invoices = Invoice.objects.all()
    return render(request, 'billing/billing.html', {'invoices': invoices})

def create_invoice(request):
    companies = Company.objects.all()
    invoices = Invoice.objects.all()  # Fetch all invoices
    return render(request, 'invoice/create_invoice.html', {'companies': companies, 'invoices': invoices})

@csrf_exempt
def save_invoice(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        invoice_id = data.get('invoice_id')
        customer_type = data.get('customer_type')
        customer_id = data.get('customer_id')
        invoice_date = data.get('invoice_date')
        due_date = data.get('due_date')

        if invoice_id:  # Editing existing invoice
            invoice = get_object_or_404(Invoice, id=invoice_id)
            invoice.customer_type = customer_type
            invoice.company_id = customer_id if customer_type == "company" else None
            invoice.individual_id = customer_id if customer_type == "individual" else None
            invoice.invoice_date = invoice_date
            invoice.due_date = due_date
            invoice.save()
            message = "Invoice updated successfully"
        else:  # Creating new invoice
            invoice = Invoice.objects.create(
                customer_type=customer_type,
                company_id=customer_id if customer_type == "company" else None,
                individual_id=customer_id if customer_type == "individual" else None,
                invoice_date=invoice_date,
                due_date=due_date
            )
            message = "Invoice created successfully"

        return JsonResponse({'message': message, 'invoice_id': invoice.id})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def delete_invoice(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        invoice_id = data.get('invoice_id')
        invoice = get_object_or_404(Invoice, id=invoice_id)
        invoice.delete()
        return JsonResponse({'message': 'Invoice deleted successfully'})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def add_invoice_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('item_id')
        invoice_id = data.get('invoice_id')
        description = data.get('description')
        quantity = int(data.get('quantity'))
        unit_price = float(data.get('unit_price'))
        discount = float(data.get('discount'))
        tax = int(data.get('tax'))

        invoice = get_object_or_404(Invoice, id=invoice_id)

        total_price = (unit_price * quantity)
        discount_amount = total_price * (discount / 100)
        tax_amount = (total_price - discount_amount) * (tax / 100)
        final_price = (total_price - discount_amount) + tax_amount

        if item_id:  # Editing item
            item = get_object_or_404(InvoiceItem, id=item_id)
            item.description = description
            item.quantity = quantity
            item.unit_price = unit_price
            item.discount = discount
            item.tax = tax
            item.total_price = final_price
            item.save()
            message = "Item updated successfully"
        else:  # Creating item
            InvoiceItem.objects.create(
                invoice=invoice,
                description=description,
                quantity=quantity,
                unit_price=unit_price,
                discount=discount,
                tax=tax,
                total_price=final_price
            )
            message = "Item added successfully"

        return JsonResponse({'message': message, 'final_price': final_price})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def delete_invoice_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('item_id')
        item = get_object_or_404(InvoiceItem, id=item_id)
        item.delete()
        return JsonResponse({'message': 'Item deleted successfully'})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
