from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length = 100,
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter your name:'
            }
        )
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter your email:'
            }
        )
    )
    subject = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Subject:'
            }
        )
    )
    message = forms.CharField( 
        widget = forms.Textarea( 
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Give your report:',
                'rows': 5 
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Custom validation
        if 'example.com' in email:
            raise forms.ValidationError('Example.com emails are not allowed : /')
        return email
