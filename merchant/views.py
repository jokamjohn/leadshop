from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "merchant/dashboard_layout.html"

    def get(self, request, *args, **kwargs):
        """
        Redirect the user to the login page if they are not merchants.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if not request.user.is_merchant:
            return redirect('/login/?next=%s' % request.path)
        return super().get(request, *args, **kwargs)
