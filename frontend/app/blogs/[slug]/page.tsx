/* eslint-disable @typescript-eslint/no-explicit-any */
import { Metadata } from "next";
import { MEDIA_URL } from "@/utils/api";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";
import BannerImg from "../../../public/images/banner-img.svg";
import eager from "../../../public/images/eager.png";
import facebook_icon from "../../../public/images/facebook.svg";
import medium_icon from "../../../public/images/medium.svg";
import search from "../../../public/images/search.svg";
import twitter_icon from "../../../public/images/twitter.svg";
import BlogContent from "./content";

type SingleBlogProps = {
    params: Promise<{ slug: string }>;
};

export async function generateMetadata({
    params,
}: SingleBlogProps): Promise<Metadata> {

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

export default async function Page({ params }: SingleBlogProps) {
    const { slug } = await params;
    const singleBlog = await getFetchData(`/blogs/single/${slug}/`);

    const createdAt = singleBlog?.data?.created_at ? new Date(singleBlog.data.created_at) : null;
    const formattedDate = createdAt
        ? createdAt.toLocaleString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })
        : '';
        
    return (
        <>
            <section className="mt-24 md:mt-36 banner-section bg-blue [clip-path:polygon(0_0,100%_0,100%_calc(100%-50px),calc(100%-60px)_100%,0_100%)] md:[clip-path:polygon(0_0,100%_0,100%_calc(100%-100px),calc(100%-150px)_100%,0_100%)]">
                <div className="container">
                    <div className="bg-bottom bg-contain bg-no-repeat" style={{ backgroundImage: `url(${BannerImg.src})` }}>
                        <div className="max-w-[1240px] mx-auto py-10 sm:py-20 md:py-40 lg:py-[232px] text-white text-center ">
                            <p className="text-sm sm:text-base md:leading-6 font-dmsans">{formattedDate}</p>
                            <h1 className="uppercase">{singleBlog?.data?.title}</h1>
                        </div>
                    </div>
                </div>
            </section>
            <section className="py-12 md:py-[100px]">
                <div className="container">
                    <div className="flex flex-col lg:flex-row">
                        {/* SIDEBAR */}
                        <div className="w-full lg:max-w-[408px] space-y-8">
                            <form>
                                <div className="w-full relative bg-[#EBF3F8] py-5 pl-6 pr-12 rounded-full">
                                    <input type="text" placeholder="Search" className="w-full focus:outline-0" />
                                    <button type="submit" className="absolute top-1/2 right-6 -translate-y-1/2 cursor-pointer">
                                        <Image src={search} alt="search" width={15} height={15} />
                                    </button>
                                </div>
                            </form>
                            <div className="p-4 md:p-8 border border-[#C0D9EB] rounded-2xl">
                                <h4>Table of Contents</h4>
                                <ul className="list">
                                    <li className="mt-4">
                                        <Link href="https://eic.com.bd/" className="text-sm md:text-lg font-dmsans font-normal md:leading-6 transition-all duration-500 text-gray hover:text-body hover:font-bold">Understanding Cyber Threats</Link>
                                    </li>

                                </ul>
                            </div>
                            <div className="px-8 py-11 rounded-2xl bg-top bg-cover bg-no-repeat" style={{ backgroundImage: `url(${eager.src})` }}>
                                <div className="space-y-8">
                                    <h4 className="text-white font-dmsans w-full max-w-[318px]">Eager to fortify your cyber defenses and ensure robust security?</h4>
                                    <Link href="[https://eic.com.bd/]" className="btn-primary group inline-flex">Schedule a Call
                                        <svg className="transition-all duration-500 group-hover:rotate-45 w-5 md:w-6 h-5 md:h-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                            <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M6 18 18 6m0 0H9m9 0v9" />
                                        </svg>
                                    </Link>
                                </div>
                            </div>
                            {singleBlog?.related_blogs && (
                                <div className="p-4 md:p-8 border border-[#C0D9EB] rounded-2xl">
                                    <h4>Related Blogs</h4>
                                    <ul className="list divide-y divide-[#EBF3F8] mt-6">
                                        {singleBlog?.related_blogs?.map((item: any) => {
                                            return (
                                                <li className="mt-4" key={item.id}>
                                                    <Link href={`/blogs/${item.slug}`} className="text-sm md:text-lg font-dmsans font-normal md:leading-6 transition-all duration-500 text-gray hover:text-body hover:font-bold mb-1 block">{item.title}</Link>
                                                </li>
                                            );
                                        })}
                                    </ul>
                                </div>
                            )}
                        </div>
                        {/* BLOG CONTENT */}
                        <div className="w-full lg:max-w-[calc(100%-408px)] lg:pl-14">
                            <nav className="py-1.5" aria-label="Breadcrumb">
                                <ol className="flex items-center space-x-2 flex-wrap">
                                    <li>
                                        <Link href="/" className="text-body text-base leading-6 font-medium font-dmsans hover:underline">Home</Link>
                                    </li>
                                    <li>
                                        <span className="text-body text-base">/</span>
                                    </li>
                                    <li>
                                        <Link href="/blogs" className="text-body text-base leading-6 font-medium font-dmsans hover:underline">Blog</Link>
                                    </li>
                                    <li>
                                        <span className="text-body text-base">/</span>
                                    </li>
                                    <li className="text-gray text-base leading-6 font-medium font-dmsans">
                                        {singleBlog?.data?.title}
                                    </li>
                                </ol>
                            </nav>
                            <div className="space-y-8">
                                <div className="text-body">
                                    <BlogContent content={singleBlog?.data?.content.replace(/src="\/media/g, `src="${MEDIA_URL}/media`)} />
                                </div>
                                <div className="flex flex-col md:flex-row md:items-center gap-2 lg:gap-4 mt-12">
                                    <span className="text-base leading-[25px] font-inter text-[#151517]">Tagged with:</span>
                                    {singleBlog?.data?.tags?.map((item: any) => {
                                        return (
                                            <div className="flex items-center gap-2.5 flex-wrap" key={item.id}>
                                                <button type="button" className="px-3 py-1 text-body text-sm leading-5 font-inter font-medium rounded-lg bg-[#EBF3F8] cursor-pointer">{item.name}</button>
                                            </div>
                                        );
                                    })}
                                </div>
                            </div>
                        </div>
                    </div>
                    {/* AUTHOR */}
                    <div className="bg-[#EBF3F8] p-8 rounded-2xl flex flex-col md:flex-row gap-3 lg:gap-6 mt-12 md:mt-[100px]">
                        {singleBlog?.data?.author_image && (
                            <div className="w-16 h-16">
                                <Image src=
                                {singleBlog?.data?.author_image} 
                                alt={singleBlog?.data?.author_name}
                                 width={64} 
                                 height={64} 
                                 priority 
                                fetchPriority="high"
                                />
                            </div>
                        )}
                        <div className="w-full max-w-[1147px] ">
                            {singleBlog?.data?.author_name && (
                                <h6 className="text-base leading-6 font-dmsans font-bold text-body">{singleBlog?.data?.author_name}</h6>
                            )}
                            {singleBlog?.data?.author_bio && (
                                <p className="text-sm text-gray font-dmsans leading-[22px] font-normal mt-1">{singleBlog?.data?.author_bio}</p>
                            )}
                            {singleBlog?.data?.author_description && (
                                <ul className="flex items-center mt-4 flex-wrap">
                                    <li className="font-inter font-normal text-base leading-[25px] text-body mr-1 pr-1 relative">{singleBlog?.data?.author_description}</li>
                                </ul>
                            )}
                        </div>
                        <div className="w-full sm:w-9 flex flex-row sm:flex-col gap-2">
                            {singleBlog?.data?.author_facebook_url && (
                                <Link href={singleBlog?.data?.author_facebook_url} target="_blank">
                                    <Image 
                                    src={facebook_icon}
                                    alt="Facebook"
                                    width={36}
                                    height={36}
                                    priority
                                    fetchPriority="high"
                                />
                                </Link>
                            )}
                            {singleBlog?.data?.author_medium_url && (
                                <Link href={singleBlog?.data?.author_medium_url} target="_blank">
                                    <Image 
                                    src={medium_icon} 
                                    alt="Network"
                                    width={36}
                                    height={36}
                                    priority
                                    fetchPriority="high"
                                />
                                </Link>
                            )}
                            {singleBlog?.data?.author_twitter_url && (
                                <Link href={singleBlog?.data?.author_twitter_url} target="_blank">
                                    <Image 
                                    src={twitter_icon} 
                                    alt="X icon"
                                    width={36}
                                    height={36}
                                    priority
                                    fetchPriority="high"
                                />
                                </Link>
                            )}
                        </div>
                    </div>
                </div>
            </section >
        </>
    );
}
