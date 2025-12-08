/* eslint-disable @typescript-eslint/no-explicit-any */
import { SERVER_URL } from "./api";

type FetchOptions = RequestInit & {
  tag?: string;
};

export const getFetchData = async (
  url: string,
  options: FetchOptions = {}
) => {
  const { tag, ...rest } = options;

  const fetchOptions: RequestInit & { next?: { tags?: string[] } } = {
    ...rest,
    cache: 'force-cache',
  };

  if (tag) {
    fetchOptions.next = {
      ...(rest as any).next,
      tags: [
        ...(((rest as any).next?.tags as string[] | undefined) || []),
        tag,
      ],
    };
  }

  try {
    const response = await fetch(`${SERVER_URL}${url}`, fetchOptions);

    if (!response.ok) {
      const errorData = await response.json();
      console.error("Fetch failed:", response.status, response.statusText, errorData);
      return null;
    }

    return await response.json();
  } catch (error) {
    console.error("Fetch error:", error);
    return null;
  }
};
