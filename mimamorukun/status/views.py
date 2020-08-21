from django.shortcuts import render
from django.http import HttpResponse
from .models import Member

# Create your views here.


def index(request):
    member = Member.objects.order_by('id')
    return render(request, 'status/index.html', {'member': member})