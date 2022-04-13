from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "entrega_intermedia.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import entrega_intermedia.users.signals  # noqa F401
        except ImportError:
            pass
