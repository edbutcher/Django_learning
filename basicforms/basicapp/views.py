from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'basicapp/index.html')


def form_view(request):
    form = forms.FormName()

    if request.method == 'post':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOME CODE HERE
            print("Validation success!")
            print("Name:" + form.cleaned_data['data'])
            print("Email:" + form.cleaned_data['email'])
            print("Text:" + form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form': form})
