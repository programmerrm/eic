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

        print(f"[Next.js Revalidate] Sending request to: {url} with params: {params}")  # ✅ print request

        resp = requests.get(url, params=params, timeout=5)

        print(f"[Next.js Revalidate] Response status: {resp.status_code}")  # ✅ print response status
        print(f"[Next.js Revalidate] Response body: {resp.text}")  # ✅ print response body

        return resp.status_code == 200

    except Exception as exc:
        print("[Next.js Revalidate] Error:", exc)
        return False
