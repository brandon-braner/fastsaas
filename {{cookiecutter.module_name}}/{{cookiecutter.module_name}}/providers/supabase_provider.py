from supabase_py import create_client, Client as SupabaseClient
from {{ cookiecutter.module_name }}.config.settings import Settings
from lagom import Container, Singleton


def register(di: Container):
    settings = di[Settings]
    di[SupabaseClient] = Singleton(
        create_client(settings.supabase_url, settings.supabase_key)
    )
