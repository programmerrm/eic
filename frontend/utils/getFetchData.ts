import { SERVER_URL } from "./api";

export const getFetchData = async (url: string, options: RequestInit = {}) => {
  try {
    const response = await fetch(`${SERVER_URL}${url}`, {
      next: { revalidate: 60 },
      ...options,
    });

    if (!response.ok) {
      if (process.env.NODE_ENV === "development") {
        console.error(`Failed to fetch: ${response.status} ${response.statusText}`);
      }
      return null;
    }

    return await response.json();
  } catch (error) {
    if (process.env.NODE_ENV === "development") {
      console.error("Fetch error:", error);
    }
    return null;
  }
};

