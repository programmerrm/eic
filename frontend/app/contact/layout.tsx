import { DOMAIN_NAME } from "@/utils/api";
import { getFetchData } from "@/utils/getFetchData";
import { Metadata } from "next";

const fetchSeoTag = async () => {
    const res = await getFetchData('/contact/seo-tag/');
    return res?.data || null;
};

export async function generateMetadata(): Promise<Metadata> {
    const seo = await fetchSeoTag();

    if (!seo) {
        return {
            title: "Contact",
            description: "Contact page",
        };
    }

    return {
        title: seo.title,
        description: seo.description,
        keywords: seo.keywords,
        alternates: {
            canonical: `${DOMAIN_NAME}/contact`,
        },
        openGraph: {
            title: seo.og_title || seo.title,
            description: seo.og_description || seo.description,
            url: seo.og_url || `${DOMAIN_NAME}/contact`,
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

export default function ContactRootLayout({
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
