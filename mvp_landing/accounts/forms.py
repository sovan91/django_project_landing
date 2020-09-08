from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()



class LoginForm(forms.Form):
	username= forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'enter your username'}))
	password= forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'enter your password'}))

	
	'''	
	def clean_username(self):
		username = self.cleaned_data.get("username")
		#check username
		#return username
'''

'''

class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))

	class Meta:
		model = User
		fields = [
		'username',
		'email'
		]
	def clean(self):
		data = self.cleaned_data
		password_1 = data.get('password')
		password_2 = data.get('password2')
		if password_1 != password_2 :
			raise forms.ValidationError("password must matched!")
		return data
		#validation for username and email.If it is already exists then return to registration page
	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username__iexact=username)
		if qs.exists():
			raise forms.ValidationError(f"{username} already taken.Try new one.")
		return username
		#check if email already exists?
	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email__iexact=email)
		if qs.exists():
			raise forms.ValidationError(f"{email} already taken.Try new one.")
		return email

'''
class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]

    def clean(self):
        data = self.cleaned_data
        password_1 = data.get("password")
        password_2 = data.get("password2")
        if password_1 != password_2:
            # assign to non_field_error
            #raise forms.ValidationError("Passwords must match.")
            self.add_error("password", "Passwords must match.")
        return data

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError(f"{username} is taken. Try again")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError(f"{email} is taken. Try again")
        return email
