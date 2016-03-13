from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']
#		exclude = ['full_name']
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split('@')
		domain, extension = provider.split('.')
		if not domain == 'USC':
			raise forms.ValidationError("Пожалуйста, убедитесь, что вы используете ваш USC электронной почты.")
		if not extension == 'edu':
			raise forms.ValidationError("Пожалуйста, используйте действительный адрес электронной почты .edu")
		return email