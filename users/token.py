from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        user_id = text_type(user.pk)
        timestamp = text_type(timestamp)
        is_active = text_type(user.is_active)
        return f"{user_id}{timestamp}{is_active}"

account_activation_token = EmailVerificationTokenGenerator()