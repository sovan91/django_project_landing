from django import forms
from .models import EmailEntry


class EmailEntryUpdateForm(forms.ModelForm):
    class Meta:
        model = EmailEntry
        fields = ['name', 'email', 'bio']


class EmailEntryForm(forms.ModelForm):
    class Meta:
        model = EmailEntry
        fields = ['email']

    # validation check if some match with db?
    def clean_email(self):  # clean <fieldname>
        email = self.cleaned_data.get("email")
        # if email.endswith("gmail.com"):
        # 	raise forms.ValidationError ("Invalid email")
        qs = EmailEntry.objects.filter(email__iexact=email)  # abcW@gmail.com = abcw@gamil.com
        if qs.exists():
            raise forms.ValidationError("Thank you! you are already registered")
        return email
