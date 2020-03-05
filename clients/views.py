from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def create_client(request, name, company=None):
    if not company:
        company = 'no info'

    return HttpResponse('mi nombre es: {} y trabajo en {}'.format(name, company))


def delete_client(request):
    name = request.GET['name']
    company = request.GET['company']
    return HttpResponse(name)
