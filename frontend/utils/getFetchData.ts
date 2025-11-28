export const getFetchData = async (url: string, options = {}) => {
  try {
    const response = await fetch(`${url}`, {
      cache: "no-store",
      ...options,
    });

    return await response.json();

  } catch (error) {
    console.error("Fetch error:", error);
    return null;
  }
};
