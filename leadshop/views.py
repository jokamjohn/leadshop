from django.views.generic import TemplateView


class Home(TemplateView):
    """
    Site home page view
    """
    template_name = "index.html"

