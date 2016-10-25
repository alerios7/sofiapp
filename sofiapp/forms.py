from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(label="Email de contacto", required=True)
    subject = forms.CharField(label="Asunto", required=True)
    message = forms.CharField(label="Mensaje", widget=forms.Textarea, required=True)

    #this is to add bootstrap class form-control to form
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['from_email'].widget.attrs = {'class': 'form-control'}
        self.fields['subject'].widget.attrs = {'class': 'form-control'}
        self.fields['message'].widget.attrs = {'class': 'form-control'}
