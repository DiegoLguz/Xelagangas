from django import forms
from .models import Post
from .models import Archivos

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "nombrealbum",
            "title",
            "cancion",
            "image",
            "content",
        ]  
        
class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivos
        fields = [
            "artista",
            "album"
        ]