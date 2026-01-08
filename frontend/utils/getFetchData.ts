// import { SERVER_URL } from "./api";

// type NextFetchOptions = {
//     cache?: 'force-cache' | 'no-store' | 'default';
// };

// export const getFetchData = async (
//     url: string,
//     options: RequestInit & { next?: NextFetchOptions } = {}
// ) => {
//     try {
//         const fetchOptions: RequestInit & { next?: NextFetchOptions } = {
//             ...options,
//             next: {
//                 cache: 'force-cache',
//             },
//         };
//         const response = await fetch(`${SERVER_URL}${url}`, fetchOptions);
//         return await response.json();
//     } catch (error) {
//         console.error("Fetch error:", error);
//         return null;
//     }
// };

import { SERVER_URL } from "./api";

type NextFetchOptions = {
    cache?: 'force-cache' | 'no-store' | 'default';
};

export const getFetchData = async (
    url: string,
    options: RequestInit & { next?: NextFetchOptions } = {}
) => {
    try {
        if (process.env.NEXT_PHASE === "phase-production-build") {
            console.log("Skipping fetch at build time:", url);
            return null;
        }

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

