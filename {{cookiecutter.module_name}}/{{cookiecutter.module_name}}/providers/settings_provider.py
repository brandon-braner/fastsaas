from supabase_py import create_client, Client as SupabaseClient
from {{ cookiecutter.module_name }}.config.settings import Settings, get_settings
from lagom import Container, Singleton


def register(di: Container):
    di[Settings] = Singleton(get_settings())
