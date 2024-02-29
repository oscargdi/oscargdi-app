from django import forms


class MessageForm(forms.Form):
    title = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
