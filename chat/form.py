from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields=('what','how_much','by_when','punishment')
        help_texts={
            'what':'なにを',
            'how_much':'どのくらい',
            'by_when':'いつまでに',
            'punishment':'罰'
        }
        widgets={
            'by_when':forms.SelectDateWidget
        }