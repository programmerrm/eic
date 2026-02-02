import AboutUs from "@/components/pages/about-us";
import BlogsPage from "@/components/pages/blogs";
import CaseStudiesPage from "@/components/pages/case-studies";
import ContactPage from "@/components/pages/contact-us";
import FaqPage from "@/components/pages/faq";
import ServicesPage from "@/components/pages/services";
import { getFetchData } from "@/utils/getFetchData";
import { Metadata } from "next";
import { notFound } from "next/navigation";

type SlugProps = {
    params: { slug: string };
};

export async function generateMetadata({
    params,
}: SlugProps): Promise<Metadata> {

    const { slug } = await params;

    const response = await getFetchData(`/pages/${slug}`);
    const data = response?.seo || {};

    return {
        title: data?.title || "Cybersecurity Service Provider and Top cybersecurity companies in Bangladesh | EIC",
        description: data?.description || "Protect your business with EIC—VAPT, ISO 27001, PCI DSS & IT audits. A trusted cybersecurity service provider among the top cybersecurity companies in Bangladesh.",
        keywords: data?.keywords || "Cybersecurity Service Provider, Top cybersecurity company, cybersecurity service provider, network and security solutions, cybersecurity managed services, cybersecurity services company, Top cybersecurity companies in Bangladesh, Top cybersecurity companies, Cybersecurity as a service companies, Best cybersecurity companies to work for, top application security companies, leading trustworthy cybersecurity consultants, best cybersecurity firms, top security company, security software companies, Cybersecurity top companies, global security firm, cybersecurity service",
        authors: data?.author || "EIC Team",
        category: data?.category || "cybersecurity",
        alternates: { canonical: data?.canonical_url || `https://eic.com.bd` },

        openGraph: {
            title: data?.og_title || "Cybersecurity Service Provider and Top cybersecurity companies in Bangladesh | EIC",
            description: data?.og_description || "Protect your business with EIC—VAPT, ISO 27001, PCI DSS & IT audits. A trusted cybersecurity service provider among the top cybersecurity companies in Bangladesh.",
            url: data?.og_url || data?.canonical_url,
            type: data?.og_type || "website",
            siteName: data?.og_site_name || "EIC",
            locale: data?.og_locale || "en_US",
            images: data?.og_image ? [{ url: data.og_image }] : [],
        },

        twitter: {
            card: data?.twitter_card || "summary_large_image",
            title: data?.twitter_title || "Cybersecurity Service Provider and Top cybersecurity companies in Bangladesh | EIC",
            description: data?.twitter_description || "Protect your business with EIC—VAPT, ISO 27001, PCI DSS & IT audits. A trusted cybersecurity service provider among the top cybersecurity companies in Bangladesh.",
            images: data?.twitter_image ? [data.twitter_image] : [],
            site: data?.twitter_site || "",
            creator: data?.twitter_creator || "",
        },

        metadataBase: new URL(data?.canonical_url || `https://eic.com.bd`),
        other: {
            "creator": data?.creator || undefined,
            "article:published_time": data?.published_time || undefined,
            "article:modified_time": data?.modified_time || undefined,
        },
    };
}

export default async function Page({ params }: SlugProps) {
    const { slug } = await params;
    const pageData = await getFetchData(`/pages/${slug}/`);
    const jsonSchema = pageData?.schema?.schema || {};
    if (!pageData) return notFound();

    switch (pageData.name) {
        case "About Us":
            return <AboutUs jsonSchema={jsonSchema} />;
        case "Services":
            return <ServicesPage jsonSchema={jsonSchema} />;
        case "Case Studies":
            return <CaseStudiesPage jsonSchema={jsonSchema} />;
        case "Blogs":
            return <BlogsPage jsonSchema={jsonSchema} />;
        case "Contact Us":
            return <ContactPage jsonSchema={jsonSchema} />;
        case "Faq":
            return <FaqPage />;
        default:
            return notFound();
    }
}
