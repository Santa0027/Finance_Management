from django.contrib import admin
from .models import Company,Individual
# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')


@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    list_display = ('name','email')