from django import forms  
from .models import Teacher 
class MoviesForm(forms.ModelForm):
        class Meta:  
            model = Teacher
            fields = ['title', 'genre'] 