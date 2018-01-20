from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from . import emails


class UserCreateForm(UserCreationForm):
    """
    Form class to which persists a User into the database.
    """

    class Meta:
        fields = ('email', 'username', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['email'].label = "Email Address"

    def save(self, commit=True):
        """
        The user data is saved if it is valid and also a user is sent a
        verification email upon successful sign up.
        :param commit:
        :return:
        """
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_merchant = True
        if commit:
            user.save()
            emails.send_user_registration_activation_email(self.request, user, user.email)
        return user
