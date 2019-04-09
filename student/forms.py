from django import forms  
from .models import Student 
class MoviesForm(forms.ModelForm):
        class Meta:  
            model = Student 
            fields = ['title', 'genre']  
