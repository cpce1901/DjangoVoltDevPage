from django.views.generic import TemplateView
from .models import PersonalImagen, PersonalCV
from .models import Projects

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personal_imagen'] = PersonalImagen.objects.first()
        context['personal_cv'] = PersonalCV.objects.first()
        context['projects'] = Projects.objects.all()
        return context

class ProjectsView(TemplateView):
    template_name = 'core/projects.html'

class ContactView(TemplateView):
    template_name = 'core/contact.html'
