from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'social_project/test.html'


class ThanksPage(TemplateView):
    template_name = 'social_project/thanks.html'


class HomePage(TemplateView):
    template_name = 'social_project/index.html'
