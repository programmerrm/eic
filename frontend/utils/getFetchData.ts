import { SERVER_URL } from "./api";

export const getFetchData = async (url: string, options = {}) => {
  try {
    const response = await fetch(`${SERVER_URL}${url}`, {
      cache: "no-store",
      ...options,
    });

    return await response.json();

  } catch (error) {
    console.error("Fetch error:", error);
    return null;
  }
};
