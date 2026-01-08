import { Metadata } from "next";
import { getFetchData } from "@/utils/getFetchData";
import { DOMAIN_NAME } from "@/utils/api";
import Logo from "@/public/images/eic-logo.svg";

const fetchSeoTag = async () => {
    const res = await getFetchData('/faq/seo-tag/');
    return res?.data || null;
};

export async function generateMetadata(): Promise<Metadata> {
    const seo = await fetchSeoTag();

    if (!seo) {
        return {
            title: "Faq",
            description: "Faq page",
        };
    }

    return {
        title: seo.title || "Eic - Faq",
        description: seo.description || "Eic - description",
        keywords: seo.keywords || "eic-faq",
        alternates: {canonical: `${DOMAIN_NAME}/faq`},
        openGraph: {
            type: seo.og_type || "website",
            title: seo.og_title || "Eic - og title",
            description: seo.og_description || "Eic - og description",
            url: seo.og_url || `${DOMAIN_NAME}/faq`,
            images: seo.og_image || Logo,
        },
        twitter: {
            card: "summary_large_image",
            title: seo.twitter_title || "eic - twitter title",
            description: seo.twitter_description || "eic - twitter description",
            images: seo.twitter_image || Logo,
        },
    };
}

export default function FaqRootLayout({
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
