from django.shortcuts import render
from django.http import HttpResponse
tax_rate=1.15
def index(request):
    return HttpResponse("this is a site to calculate tax")
def calctax(request, num):
    return HttpResponse(f"the number you entered is: {num} and after tax is: {num*tax_rate}")
def htmlfile(request):
    simpleRate=15
    return render(request, "labApp/tax.html",{'rate':simpleRate})


# Create your views here.
