from django.shortcuts import render

# Create your views here.
def build(request):
    return render(request,'build.html')