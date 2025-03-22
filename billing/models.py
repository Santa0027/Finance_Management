from django.db import models
from company.models import Company , Individual  # Assuming you have a Company model



class Invoice(models.Model):
    CUSTOMER_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('company', 'Company')
    ]
    customer_type = models.CharField(max_length=10, choices=CUSTOMER_TYPE_CHOICES)
    individual = models.ForeignKey(Individual, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    invoice_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return f"Invoice {self.id} - {self.customer_type}"

class InvoiceItem(models.Model):
    TAX_CHOICES = [
        (5, '5%'),
        (12, '12%'),
        (18, '18%'),
        (28, '28%')
    ]
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    tax = models.IntegerField(choices=TAX_CHOICES, default=5)

    def total_price(self):
        price = self.quantity * self.unit_price
        discount_amount = (price * self.discount) / 100
        tax_amount = ((price - discount_amount) * self.tax) / 100
        return price - discount_amount + tax_amount

    def __str__(self):
        return f"{self.description} - {self.invoice}"
