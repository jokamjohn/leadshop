from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        """
        Creates and returns a token to be attached to the url to be sent
        to the user.
        :param user: User
        :param timestamp: Timestamp
        :return:
        """
        return (
                six.text_type(user.pk) +
                six.text_type(timestamp) +
                six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()
