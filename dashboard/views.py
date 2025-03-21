from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

@login_required  # 🔒 Restrict access to logged-in users
# def home(request):
#     return render(request, 'dashboard/home.html')


def home(request):
    return render(request, 'dashboard/home.html', {'timestamp': now().timestamp()})
