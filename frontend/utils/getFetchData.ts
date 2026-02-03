import { FRONTEND_API_KEY, SERVER_URL } from "./api";

type NextFetchOptions = {
    cache?: "force-cache" | "no-store" | "default";
    tags?: string[];
};

export const getFetchData = async (
    url: string,
    options: RequestInit & { next?: NextFetchOptions } = {}
) => {
    try {
        const fetchOptions: RequestInit & { next?: NextFetchOptions } = {
            ...options,
            headers: {
                "X-API-KEY": FRONTEND_API_KEY || "",
                "Content-Type": "application/json",
                ...(options.headers || {}),
            },
            next: {
                cache: "no-store"
            },
        };
        const response = await fetch(`${SERVER_URL}${url}`, fetchOptions);
        if (!response.ok) {
            throw new Error(`Fetch failed: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error("Fetch error:", error);
        return null;
    }
};
