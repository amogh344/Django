from django import forms
from .models import Student

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=40, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': True}))
    email = forms.EmailField(label='Email', max_length=40, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required': True}))
    message = forms.CharField(label='Message', max_length=200, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message', 'required': True}))

    def clean(self):
        cleaned_data = super().clean()
        if self.errors: return cleaned_data
        if cleaned_data.get('name') and len(cleaned_data.get('name')) < 3:
            raise forms.ValidationError('Name must be at least 3 characters long.')
        return cleaned_data

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Username', 'required': True}))
    email = forms.EmailField(label='', max_length=50, widget=forms.EmailInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Email', 'required': True}))
    password = forms.CharField(label='', max_length=50, widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Password', 'required': True}))
    confirm_password = forms.CharField(label='', max_length=50, widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Confirm Password', 'required': True}))

    class Meta:
        model = Student
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class StudentForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    age = forms.IntegerField()

    class Meta:
        model = Student
        fields = "__all__"