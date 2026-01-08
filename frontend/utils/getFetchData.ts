import { SERVER_URL } from "./api";

type NextFetchOptions = {
    cache?: 'force-cache' | 'no-store' | 'default';
};

export const getFetchData = async (
    url: string,
    options: RequestInit & { next?: NextFetchOptions } = {}
) => {
    try {
        const fetchOptions: RequestInit & { next?: NextFetchOptions } = {
            ...options,
            next: {
                cache: 'force-cache',
            },
        };
        const response = await fetch(`${SERVER_URL}${url}`, fetchOptions);
        return await response.json();
    } catch (error) {
        console.error("Fetch error:", error);
        return null;
    }
};
