from django import forms
from django.core import validators

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


# for learning validation
# class StudentForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 8:
#     #         raise forms.ValidationError("Enter a name with at least 8 characters")
#     #     return valname
    
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError('Email must be contain .com')
#     #     return valemail

#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 8:
#             raise forms.ValidationError("Enter a name with at least 8 characters")
#         if '.com' not in valemail:
#             raise forms.ValidationError('Email must be contain .com')

def len_check(value):
    if len(value) > 20 :
        raise forms.ValidationError("Comments letter exceeding!")

class StudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MaxLengthValidator(8, message='Enter a name with at most 8 characters')])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a Valid Email')])
    age = forms.IntegerField(widget=forms.NumberInput, validators=[validators.MaxValueValidator(25, message='Age at most 25'), validators.MinValueValidator(18, message='Age at least 18')])
    s_file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'], message='Only image file accepted')])
    comments = forms.CharField(widget = forms.Textarea(attrs={'placeholder' : 'Enter your comments here...'}), validators=[len_check])
