from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm

def home(request):
	title = "Welcome"
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
	return render(request, "home.html", context)


def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		message = form.cleaned_data.get("message")
		full_name = form.cleaned_data.get("full_name")
		print email, message, full_name
	context = {
		"form": form,
	}

	return render(request, "forms.html", context)




















