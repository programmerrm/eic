/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import Image from "next/image";
import Link from "next/link";
import { useState } from "react";
import BannerImg from "../../public/images/banner-img.svg";

export default function BlogsPage({ topBarData, initialBlogs, initialNext, jsonLd }: any) {
    const [blogs, setBlogs] = useState(initialBlogs);
    const [nextUrl, setNextUrl] = useState(initialNext);
    const [loading, setLoading] = useState(false);

    const handleLoadMore = async () => {
        if (!nextUrl) return;
        setLoading(true);
        try {
            const res = await fetch(nextUrl);
            const data = await res.json();

            if (data?.results?.data) {
                setBlogs(data.results.data);
                setNextUrl(data.next);
            }
        } catch (err) {
            console.error("Failed to load more blogs:", err);
        } finally {
            setLoading(false);
        }
    };

    const firstBlog = blogs[0];
    const formattedDate = firstBlog?.created_at
        ? new Date(firstBlog.created_at).toLocaleString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })
        : '';

    return (
        <>
            {jsonLd && (
                <script
                    type="application/ld+json"
                    dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
                />
            )}
            {topBarData && (
                <section className="mt-24 md:mt-36 banner-section bg-blue [clip-path:polygon(0_0,100%_0,100%_calc(100%-50px),calc(100%-60px)_100%,0_100%)] md:[clip-path:polygon(0_0,100%_0,100%_calc(100%-100px),calc(100%-150px)_100%,0_100%)]">
                    <div className="container">
                        <div className="bg-bottom bg-contain bg-no-repeat" style={{ backgroundImage: `url(${BannerImg.src})` }}>
                            <div className="max-w-[740px] mx-auto py-10 sm:py-20 md:py-30 lg:py-40 xl:py-[232px] text-white text-center ">
                                {topBarData?.title && <h1 className="uppercase">{topBarData?.title}</h1>}
                                {topBarData?.description && (
                                    <p className="text-base sm:text-lg md:text-2xl md:leading-8 font-spacegrotesk mt-4 sm:mt-8 w-full max-w-[626px] mx-auto">{topBarData?.description}</p>
                                )}
                            </div>
                        </div>
                    </div>
                </section>
            )}
            <section className="pt-6 md:pt-12 pb-12 md:pb-[100px]">
                <div className="container">
                    {firstBlog && (
                        <div className="flex flex-col sm:flex-row items-center">
                            <Link href={`/blogs/${firstBlog.slug}`} className="w-full sm:max-w-[49.118%] group">
                                <Image
                                    src={`${firstBlog?.image}`}
                                    alt={firstBlog?.title}
                                    width={670}
                                    height={480}
                                    className="w-full h-auto transition-transform duration-500 ease-in-out group-hover:scale-105"
                                />
                            </Link>
                            <div className="w-full sm:max-w-[50.882%] sm:pl-6 md:pl-12">
                                <time className="text-body text-sm font-medium leading-5 -tracking-[0.14px] mt-3 md:mt-7 inline-block transition-all">
                                    {formattedDate}
                                </time>
                                <h4 className="my-1 md:my-3 font-dmsans transition-all hover:text-blue">
                                    <Link href={`/blogs/${firstBlog.slug}`}>{firstBlog?.title}</Link>
                                </h4>
                                {firstBlog?.tags && (
                                    <div className="flex gap-2 flex-wrap">
                                    {firstBlog?.tags?.map((item: any) => (
                                        <button key={item.id} className="bg-[#EBF3F8] px-3 py-1 rounded-lg text-body font-medium text-sm leading-5 -tracking-[0.14px] font-inter cursor-pointer transition-all hover:text-blue">{item.name}</button>
                                    ))}
                                </div>
                                )}
                                
                                <Link href={`/blogs/${firstBlog.slug}`}
                                    className="btn-primary inline-flex p-0 bg-transparent text-body text-sm capitalize underline border-0 underline-offset-6 mt-4 transition-all hover:text-blue group">
                                    Read More
                                    <svg className="transition-all duration-500 group-hover:rotate-45 w-5 md:w-6 h-5 md:h-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                        <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M6 18 18 6m0 0H9m9 0v9" />
                                    </svg>
                                </Link>
                            </div>
                        </div>
                    )}
                    {blogs && (
                        <div id="blog-items" className="grid sm:grid-cols-2 md:grid-cols-3 pt-10 md:pt-12 gap-x-5 lg:gap-x-9 gap-y-10 lg:gap-y-16">
                            {blogs.map((item: any) => {
                                const itemDate = item?.created_at ? new Date(item.created_at) : null;
                                const formattedItemDate = itemDate
                                    ? itemDate.toLocaleString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })
                                    : '';
                                return (
                                    <div className="items" key={item.id}>
                                        <Link href={`/blogs/${item.slug}`} className="group">
                                            <Image src={`${item?.image}`} alt={item?.title} width={430} height={315} className="w-full h-auto transition-transform duration-500 ease-in-out group-hover:scale-105" />
                                        </Link>
                                        <div>
                                            <time className="text-body text-sm font-medium leading-5 -tracking-[0.14px] mt-3 md:mt-7 inline-block transition-all">
                                                {formattedItemDate}
                                            </time>
                                            <h4 className="my-1 md:my-3 font-dmsans transition-all hover:text-blue">
                                                <Link href={`/blogs/${item.slug}`}>{item?.title}</Link>
                                            </h4>
                                            {item?.tags && (
                                                <div className="flex gap-2 flex-wrap">
                                                {item?.tags?.map((tag: any) => (
                                                    <button key={tag.id} className="bg-[#EBF3F8] px-3 py-1 rounded-lg text-body font-medium text-sm leading-5 -tracking-[0.14px] font-inter cursor-pointer transition-all hover:text-blue">
                                                        {tag?.name}
                                                    </button>
                                                ))}
                                            </div>
                                            )}
                                        </div>
                                    </div>
                                );
                            })}
                        </div>
                    )}
                    {nextUrl && (
                        <div className="flex items-center justify-center mt-5 lg:mt-12 xl:mt-16">
                            <button onClick={handleLoadMore} disabled={loading} className="btn-primary group">
                                {loading ? "Loading..." : "Load More"}
                                <svg className="transition-all duration-500 group-hover:rotate-45 w-5 md:w-6 h-5 md:h-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                    <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M6 18 18 6m0 0H9m9 0v9" />
                                </svg>
                            </button>
                        </div>
                    )}
                </div>
            </section>
        </>
    );
}
