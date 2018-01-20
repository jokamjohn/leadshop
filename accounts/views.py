from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views import View, generic

from . import forms
from accounts.tokens import account_activation_token


class MerchantRegistration(generic.CreateView):
    """
    View to register a merchant onto the platform.
    """
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

    def form_valid(self, form):
        """
        Set the request onto the form instance.
        :param form: UserCreateForm
        :return:
        """
        form.request = self.request
        return super().form_valid(form)


class ActivateUser(View):
    """
    Class to activate a user when they click the link sent in their emails.
    """

    def get(self, *args, **kwargs):
        """
        Validate and activate the user by turning the is_active to True.
        :param args:
        :param kwargs:
        :return:
        """
        User = get_user_model()
        try:
            uid = force_text(urlsafe_base64_decode(kwargs.get('uid')))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, kwargs.get('token')):
            user.is_active = True
            user.save()
            return redirect(reverse_lazy("login"))
        else:
            return HttpResponse("Invalid activation link")


class LoginSuccess(View):
    def get(self, request):
        if request.user.is_merchant:
            return redirect("merchant:dashboard")
        return redirect("shops")
