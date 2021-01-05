from django import forms
from .models import Contact, Note


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
        ]

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'text',
            'contact',
        ]

