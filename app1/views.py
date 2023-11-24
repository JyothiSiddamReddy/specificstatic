from django.shortcuts import render

# Create your views here.
def specificStatic(request):
    return render(request,'specificStatic.html')