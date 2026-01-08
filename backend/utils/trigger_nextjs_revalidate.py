import os
import requests

def trigger_nextjs_revalidate(path: str, tag: str) -> bool:
    try:
        base_url = os.getenv("FRONTEND_DOMAIN")
        secret = os.getenv("REVALIDATE_SECRET")

        url = f"{base_url}/api/revalidate"
        params = {
            "secret": secret,
            "path": path,
            "tag": tag,
        }

        resp = requests.get(url, params=params, timeout=5)
        return resp.status_code == 200

    except Exception as exc:
        print("Revalidate error:", exc)
        return False
