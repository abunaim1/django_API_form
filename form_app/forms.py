from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='User Name', help_text='Total length must be within 70 characters' ,required=False, widget = forms.Textarea(attrs = {'id' : 'text_area', 'class' : 'class1 class2', 'placeholder' : 'Enter Your Name'}))
    email = forms.EmailField(label='User Email')
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appoinment = forms.CharField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    ITEM = [('P','Peparoni'),('B','Beef'),('M','Mashroom')]
    ingradient = forms.MultipleChoiceField(choices=ITEM, widget=forms.CheckboxSelectMultiple)
    file = forms.FileField()

class StudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.EmailInput)