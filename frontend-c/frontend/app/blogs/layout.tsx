import { Metadata } from "next";
import { DOMAIN_NAME } from "@/utils/api";
import { getFetchData } from "@/utils/getFetchData";

const fetchSeoTag = async () => {
    const res = await getFetchData('/blogs/seo-tag/');
    return res?.data || null;
};

export async function generateMetadata(): Promise<Metadata> {
    const seo = await fetchSeoTag();

    if (!seo) {
        return {
            title: "Blogs",
            description: "Blogs page",
        };
    }

    return {
        title: seo.title,
        description: seo.description,
        keywords: seo.keywords,
        alternates: {
            canonical: `${DOMAIN_NAME}/blogs`,
        },
        openGraph: {
            title: seo.og_title || seo.title,
            description: seo.og_description || seo.description,
            url: seo.og_url || `${DOMAIN_NAME}/blogs`,
            type: seo.og_type || "website",
            images: seo.og_image ? [{ url: seo.og_image }] : undefined,
        },
        twitter: {
            card: "summary_large_image",
            title: seo.twitter_title || seo.title,
            description: seo.twitter_description || seo.description,
            images: seo.twitter_image ? [seo.twitter_image] : undefined,
        },
    };
}

export default function BlogRootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <main>
            {children}
        </main>
    );
}
