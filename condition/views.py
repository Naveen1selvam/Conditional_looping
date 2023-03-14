from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':'Naveen'}
    return render(request,'conditions.html',d)
