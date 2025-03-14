from django import forms 
from .models import File, Tag 

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'content', 'tags', 'file'] 
