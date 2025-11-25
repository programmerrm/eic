import { SERVER_URL } from "./api";

export const getFetchData = async (url: string, options = {}) => {
    try {
        const response = await fetch(`${SERVER_URL}${url}`, options);

        if (!response.ok) {
            console.error(`Failed to fetch: ${response.status} ${response.statusText}`);
            return null;
        }

        const data = await response.json();
        return data;

    } catch (error) {
        console.error("Fetch error:", error);
        return null;
    }
};
