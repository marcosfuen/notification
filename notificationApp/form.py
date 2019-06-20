from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre',)
    email = forms.CharField(label='Correo Electrónico',)
    to = forms.CharField(label='Correo Electrónico del destinatario',)
    message = forms.CharField(label='Mensaje', widget=forms.Textarea)
    attach = forms.CharField(label='Attach', widget = forms.FileInput, required=False)
