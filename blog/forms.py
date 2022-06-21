from django import forms

class ToDoForm(forms.Form):
    text = forms.CharField(max_length=255, widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter todo Delete',
                'aria-label': 'Todo',
                'aria-describedby': 'add-btn'
            }
        ))
