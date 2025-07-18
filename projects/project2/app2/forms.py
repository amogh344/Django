from django import forms
from .models import Student_info


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=40,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your name',
            'required': True
        })
    )
    
    email = forms.EmailField(
        label='Email',
        max_length=40,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your email',
            'required': True
        })
    )
    
    message = forms.CharField(
        label='Message',
        max_length=200,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Your message',
            'rows': 4,
            'required': True
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        if self.errors:
            return cleaned_data
            
        name = cleaned_data.get('name')
        if name and len(name) < 3:
            raise forms.ValidationError('Name must be at least 3 characters long.')
            
        return cleaned_data


class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'required': True
        })
    )
    
    email = forms.EmailField(
        label='',
        max_length=50,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'required': True
        })
    )
    
    password = forms.CharField(
        label='',
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'required': True
        })
    )
    
    confirm_password = forms.CharField(
        label='',
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password',
            'required': True
        })
    )

    class Meta:
        model = Student_info
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
            
        return cleaned_data


class StudentForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Student name'
        })
    )
    
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Student age'
        })
    )

    class Meta:
        model = Student_info
        fields = "__all__"
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Student bio'
            }),
        }