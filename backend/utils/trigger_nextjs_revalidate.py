import os
import requests
import logging

logger = logging.getLogger(__name__)

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

        logging.info(f"[Next.js Revalidate] Sending request to: {url} with params: {params}")

        resp = requests.get(url, params=params, timeout=5)

        logging.info(f"[Next.js Revalidate] Response status: {resp.status_code}")
        logging.info(f"[Next.js Revalidate] Response body: {resp.text}")

        return resp.status_code == 200

    except Exception as exc:
        print("[Next.js Revalidate] Error:", exc)
        return False
