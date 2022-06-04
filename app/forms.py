from django import forms
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ("__all__")
        
        widgets = {
            'book_name':forms.TextInput(attrs={'class':'form-control'}),
            'book_author':forms.TextInput(attrs={'class':'form-control'}),
            'book_price':forms.TextInput(attrs={'class':'form-control'}),
            'book_category':forms.TextInput(attrs={'class':'form-control'})
        }
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("__all__")
        
        widgets = {
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'Password':forms.TextInput(attrs={'class':'form-control'})
        }