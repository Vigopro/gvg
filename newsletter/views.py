from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import SignUpForm, ContactForm
from .models import SignUp


def home(request):
	title = "Подпишись на рассылку"
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form,
	}
	if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("Имя")
		if not full_name:
			full_name = "Новое имя"
		instance.full_name = full_name
		instance.save() #С добавлением этой строки будет появляться дата регистрации
		context = {
			"title": "Спасибо за регистрацию %s" %full_name
		}
	return render(request, "home.html", context)


def contact(request):
	title = 'Задать вопрос'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
#		for key, value in form.cleaned_data.items():
#			print (key, value)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("Сообщение")
		form_full_name = form.cleaned_data.get("Имя")
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




















