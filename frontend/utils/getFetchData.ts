export const getFetchData = async (url: string, options = {}) => {
  try {
    const response = await fetch(`https://eicsec.com/api/v1${url}`, {
      cache: "no-store",
      ...options,
    });

    return await response.json();

  } catch (error) {
    console.error("Fetch error:", error);
    return null;
  }
};
