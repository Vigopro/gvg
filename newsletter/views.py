from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import SignUpForm, ContactForm

def home(request):
	title = "Sing Up Now"
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form,
	}
	if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save() #С добавлением этой строки будет появляться дата регистрации
		context = {
			"title": "Спасибо за регистрацию %s" %full_name
		}
	if request.user.is_authenticated() and request.user.is_staff:
		context = {
			"queryset": [123, 456]
		}

	return render(request, "home.html", context)


def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
#		for key, value in form.cleaned_data.items():
#			print (key, value)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
#		print email, message, full_name
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'youotheremail@email.com']
		contact_message = " %s: %s via %s "%(
				form_full_name,
				form_message,
				form_email)
		some_html_message = '''<h1>Hello</h1>'''
		send_mail(subject,
				contact_message,
				from_email,
				to_email,
				html_message=some_html_message,
				fail_silently=True)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}

	return render(request, "forms.html", context)




















