from django.shortcuts import render

# Create your views here.
def amit(request):
    return render(request, 'jobs/home.html')
