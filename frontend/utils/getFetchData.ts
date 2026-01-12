import { SERVER_URL } from "./api";

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
            next: {
                cache: options.next?.cache ?? "no-store",
                // tags: options.next?.tags,
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
