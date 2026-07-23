from django.contrib.auth.tokens import PasswordResetTokenGenerator

class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        user_id = str((user.pk))
        timestamp = str((timestamp))
        is_active = str((user.is_active))
        return f"{user_id}{timestamp}{is_active}"

account_activation_token = EmailVerificationTokenGenerator()