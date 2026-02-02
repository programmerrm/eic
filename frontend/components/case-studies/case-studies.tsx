/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useState } from "react";
import BannerImg from "../../public/images/banner-img.svg";
import SectionImg from "../../public/images/finger.svg";
import Link from "next/link";
import Image from "next/image";

export default function CaseStudies({ topBarData, initialItem, initialNext }: any) {
    const [items, setItems] = useState(initialItem);
    const [nextUrl, setNextUrl] = useState(initialNext);
    const [loading, setLoading] = useState(false);


    const handleLoadMore = async () => {
        if (!nextUrl) return;
        setLoading(true);
        try {
            const res = await fetch(nextUrl);
            const data = await res.json();

            if (data?.results?.data) {
                setItems(data.results.data);
                setNextUrl(data.next);
            }
        } catch (err) {
            console.error("Failed to load more blogs:", err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <>
            {topBarData && (
                <section className="mt-24 md:mt-36 banner-section bg-blue [clip-path:polygon(0_0,100%_0,100%_calc(100%-50px),calc(100%-60px)_100%,0_100%)] md:[clip-path:polygon(0_0,100%_0,100%_calc(100%-100px),calc(100%-150px)_100%,0_100%)]">
                    <div className="container">
                        <div className="bg-bottom bg-contain bg-no-repeat" style={{ backgroundImage: `url(${BannerImg.src})` }}>
                            <div className="max-w-[740px] mx-auto py-10 sm:py-20 md:py-40 lg:py-[232px] text-white text-center ">
                                {topBarData?.title && <h1 className="uppercase">{topBarData?.title}</h1>}
                                {topBarData?.description && (
                                    <p className="text-base sm:text-lg md:text-2xl md:leading-8 font-spacegrotesk mt-2 sm:mt-4 w-full max-w-[626px] mx-auto">
                                        {topBarData?.description}
                                    </p>
                                )}
                            </div>
                        </div>
                    </div>
                </section>
            )}

            <section className="pt-6 md:pt-12 pb-12 md:pb-[100px] bg-center bg-cover bg-no-repeat" style={{ backgroundImage: `url(${SectionImg.src})` }}>
                <div className="container">
                    {items && (
                        <div className="grid sm:grid-cols-2 md:grid-cols-3 py-6 md:py-12 gap-5 lg:gap-9">
                            {items?.map((item: any) => (
                                <div className="items" key={item.id}>
                                    <Link href={`/case-studies/${item.slug}`} className="group">
                                        <Image
                                            src={item.image}
                                            alt={item.title}
                                            width={435}
                                            height={290}
                                            className="transition-transform duration-500 ease-in-out group-hover:scale-105"
                                            priority 
                                            fetchPriority="high"
                                        />
                                    </Link>
                                    <div className="group">
                                        <span className="text-body text-sm sm:text-lg font-dmsans font-medium leading-5 mt-3 md:mt-7 inline-block">
                                            {item.budget_description}
                                        </span>
                                        <h3 className="my-1 md:my-3 font-dmsans transition-all group-hover:text-blue">
                                            <Link href={`/case-studies/${item.slug}`}>{item.title}</Link>
                                        </h3>
                                    </div>
                                </div>
                            ))}
                        </div>
                    )}


                    {nextUrl && (
                        <div className="flex items-center justify-center mt-8">
                            <button
                                onClick={handleLoadMore}
                                disabled={loading}
                                className="btn-primary group"
                            >
                                {loading ? "Loading..." : "Load More"}
                                <svg
                                    className="transition-all duration-500 group-hover:rotate-45 w-5 md:w-6 h-5 md:h-6"
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                >
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
