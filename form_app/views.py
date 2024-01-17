from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'about.html', {'name': name, 'email' : email, 'select' : select})
    else:
        return render(request, 'about.html')
         

def form(request):
    return render(request, 'form.html')