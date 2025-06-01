from django.db import models
from company.models import Company , Individual 
from service.models import Service
 # Assuming you have a Company model

class Invoice(models.Model):
    client_type = models.CharField(max_length=10, choices=(('company', 'Company'), ('individual', 'Individual')))
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    individual = models.ForeignKey(Individual, on_delete=models.SET_NULL, null=True, blank=True)
    invoice_number = models.CharField(max_length=20, unique=True)
    date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    notes = models.TextField(blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.invoice_number

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.amount = self.rate * self.quantity
        super().save(*args, **kwargs)
