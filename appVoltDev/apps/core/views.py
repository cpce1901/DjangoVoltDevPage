from django.views.generic import TemplateView
from .models import PersonalImagen, PersonalCV

class Home(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personal_imagen'] = PersonalImagen.objects.first()
        context['personal_cv'] = PersonalCV.objects.first()
        return context

class Projects(TemplateView):
    template_name = 'core/projects.html'

class Contact(TemplateView):
    template_name = 'core/contact.html'
