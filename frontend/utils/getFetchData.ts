import { SERVER_URL } from "./api";

export const getFetchData = async (url: string, options = {}) => {
  // Check if we are in server-side rendering during build
  const isBuildTime = typeof window === "undefined";

  try {
    // During build-time, skip actual fetch or use fallback
    if (isBuildTime) {
      console.warn(`Skipping fetch for ${url} during build-time.`);
      return { data: {} }; // empty fallback to avoid build errors
    }

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
