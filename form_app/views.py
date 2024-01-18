from django.shortcuts import render, HttpResponse
from .forms import contactForm, StudentForm
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

def DjangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./form_app/upload/image' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = contactForm()
    return render(request, 'django_form.html', {'form': form})


def studentForm(request):
    if request.method == 'POST':
        s_form = StudentForm(request.POST, request.FILES)
        if s_form.is_valid():
            s_file = s_form.cleaned_data['s_file']
            with open('./form_app/upload/image' + s_file.name, 'wb+') as destination:
                for chunk in s_file.chunks():
                    destination.write(chunk)
            print(s_form.cleaned_data)
    else:
        s_form = StudentForm()
    return render(request, 'student_form.html', {'s_form' : s_form})

