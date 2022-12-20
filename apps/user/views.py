from django.views.generic import DetailView, UpdateView, CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import UserCreationForm


class StartPage(TemplateView):
    template_name = 'main/startpage.jinja'


start_page = StartPage.as_view()


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'auth/registration.jinja'
    success_url = reverse_lazy('stub')


register_user = RegisterUser.as_view()
