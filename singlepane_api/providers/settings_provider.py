from supabase_py import create_client, Client as SupabaseClient
from singlepane_api.config.settings import Settings, get_settings
from lagom import Container, Singleton


def register(di: Container):
    di[Settings] = Singleton(get_settings())
