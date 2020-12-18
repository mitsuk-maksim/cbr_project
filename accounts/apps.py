from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        """Регистрируем сигнал"""
        import accounts.signal
