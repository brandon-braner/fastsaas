from supabase_py import create_client, Client as SupabaseClient
from singlepane_api.config.settings import Settings
from lagom import Container, Singleton


def register(di: Container):
    settings = di[Settings]
    di[SupabaseClient] = Singleton(
        create_client(settings.supabase_url, settings.supabase_key)
    )
