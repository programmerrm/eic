/* eslint-disable @typescript-eslint/no-explicit-any */
import Link from "next/link";
import BannerImg from "../../../public/images/banner-img.svg";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import { MEDIA_URL } from "@/utils/api";
import CaseStudiesContent from "./content";
import { Metadata } from "next";

type SingleCaseStudiesProps = {
    params: Promise<{ slug: string }>;
};

export async function generateMetadata({
    params,
}: SingleCaseStudiesProps): Promise<Metadata> {

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

export default async function Page({ params }: SingleCaseStudiesProps) {
    const { slug } = await params;
    const singleSuccessStoriesData = await getFetchData(`/success-stories/single/${slug}/`);
    const singleSuccessStories = singleSuccessStoriesData?.data;
    return (
        <>
            <section className="mt-24 md:mt-36 banner-section bg-blue [clip-path:polygon(0_0,100%_0,100%_calc(100%-50px),calc(100%-60px)_100%,0_100%)] md:[clip-path:polygon(0_0,100%_0,100%_calc(100%-100px),calc(100%-150px)_100%,0_100%)]">
                <div className="container">
                    <div className="bg-bottom bg-contain bg-no-repeat" style={{ backgroundImage: `url(${BannerImg.src})` }}>
                        <div className="max-w-[1139px] mx-auto py-10 sm:py-20 md:py-40 lg:py-[232px] text-white text-center ">
                            <h1 className="uppercase">{singleSuccessStories?.title}</h1>
                            <p className="text-base sm:text-lg md:text-2xl md:leading-8 font-spacegrotesk mt-2 sm:mt-4 max-w-[626px] mx-auto">{singleSuccessStories?.short_description}</p>
                        </div>
                    </div>
                </div>
            </section>
            <section className="pt-6 md:pt-12 pb-12 md:pb-[100px]">
                <div className="container">
                    <div className="lg:px-20">

                        <div className="flex flex-wrap gap-6 lg:gap-12 border-b border-[#C0D9EB] pb-[26px]">
                            {singleSuccessStories?.client_name && (
                                <div className="item">
                                    <span className="text-sm sm:text-base font-bold text-body">Client:</span>
                                    <p className="font-bold">{singleSuccessStories?.client_name}</p>
                                </div>
                            )}
                            {singleSuccessStories?.subject && (
                                <div className="item">
                                    <span className="text-sm sm:text-base font-bold text-body">Subject:</span>
                                    <p className="font-bold">{singleSuccessStories?.subject}</p>
                                </div>
                            )}
                            {singleSuccessStories?.budget && (
                                <div className="item">
                                    <span className="text-sm sm:text-base font-bold text-body">Budget:</span>
                                    <p className="font-bold">{singleSuccessStories?.budget}</p>
                                </div>
                            )}
                            {singleSuccessStories?.duration && (
                                <div className="item">
                                    <span className="text-sm sm:text-base font-bold text-body">Duration:</span>
                                    <p className="font-bold">{singleSuccessStories?.duration}</p>
                                </div>
                            )}
                        </div>
                        {singleSuccessStories?.content && (
                            <CaseStudiesContent content={singleSuccessStories?.content.replace(/src="\/media/g, `src="${MEDIA_URL}/media`)} />
                        )}
                    </div>
                </div>
            </section>
            {singleSuccessStories?.related_success_stories && (
                <section className="pb-12 md:pb-[100px]">
                    <div className="container">
                        <h2 className="max-w-[393px] w-full mx-auto text-center">Case studies & <span className="text-blue">success</span> stories
                        </h2>
                        <div className="grid sm:grid-cols-2 gap-6 my-6 sm:my-12">
                            {singleSuccessStories?.related_success_stories?.map((item: any) => {
                                return (
                                    <div className="group items" key={item.id}>
                                        <Link href={`/case-studies/${item.slug}`} className="mb-3 sm:mb-6">
                                            <Image src={`${MEDIA_URL}${item.image}`} alt={item.title} className="transition-transform duration-500 ease-in-out group-hover:scale-105" width={668} height={518} />
                                        </Link>
                                        <span className="mt-6 block">{item.budget_description}</span>
                                        <h3 className="mt-1 sm:mt-2 transition-all group-hover:text-blue">
                                            <Link href={`/case-studies/${item.slug}`}>{item.title}</Link>
                                        </h3>
                                    </div>
                                );
                            })}
                        </div>
                        <div className="flex items-center justify-center">
                            <Link className="btn-primary group" href={"/case-studies"}>Explore All
                                <svg
                                    className="transition-all duration-500 group-hover:rotate-45 w-5 md:w-6 h-5 md:h-6"
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                >
                                    <path
                                        stroke="currentColor"
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        strokeWidth={1.5}
                                        d="M6 18 18 6m0 0H9m9 0v9"
                                    />
                                </svg>
                            </Link>
                        </div>
                    </div>
                </section>
            )}
        </>
    );
}
