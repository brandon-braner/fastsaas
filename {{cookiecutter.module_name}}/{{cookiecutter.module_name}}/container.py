from lagom import Container
from lagom.integrations.fast_api import FastApiIntegration

from .config.settings import Settings, get_settings
from .providers.supabase_provider import register as supabase_register
from .providers.settings_provider import register as settings_register


di: Container = Container()
deps: FastApiIntegration = FastApiIntegration(di)


def register_providers():
    # register providers here
    settings_register(di)
    supabase_register(di)
