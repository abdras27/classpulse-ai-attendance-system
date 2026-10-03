import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from supabase import create_client, Client

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env", override=True)

def _pick_setting(name: str) -> str | None:
    value = os.getenv(name) or st.secrets.get(name)
    if not value:
        return None

    placeholders = {
        "SUPABASE_URL": {
            "https://example.supabase.com",
            "https://example.supabase.co",
        },
        "SUPABASE_KEY": {
            "public-anon-key",
        },
    }

    if value in placeholders.get(name, set()):
        return None

    return value


supabase_url = _pick_setting("SUPABASE_URL")
supabase_key = _pick_setting("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    raise RuntimeError("Missing SUPABASE_URL or SUPABASE_KEY")

supabase: Client = create_client(
    supabase_url,
    supabase_key
)
