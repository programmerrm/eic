/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useState, useEffect } from "react";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";

export default function Services() {
    const [services, setServices] = useState<any[]>([]);
    const [nextUrl, setNextUrl] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const fetchInitialData = async () => {
            const data = await getFetchData("/services/list-items/", {
                tag: "services-items",
            });
            setServices(data?.results?.data || []);
            setNextUrl(data?.next || null);
        };
        fetchInitialData();
    }, []);

    const handleLoadMore = async () => {
        if (!nextUrl) return;
        setLoading(true);
        try {
            const res = await fetch(nextUrl);
            const data = await res.json();
            if (data?.results?.data) {
                setServices(data.results.data);
                setNextUrl(data.next);
            }
        } catch (err) {
            console.error("Failed to load more services:", err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <>
            {services && (
                <section className="py-12 md:py-[100px] border-b-2 border-[#C0D9EB]/30">
                    <div className="container">
                        {services && (
                            <div
                                id="items"
                                className="grid sm:grid-cols-2 lg:grid-cols-3 gap-8"
                            >
                                {services.map((item: any) => (
                                    <Link
                                        key={item.id}
                                        href={`/services/${item.slug}`}
                                        className="h-full block transition-all hover:filter hover:drop-shadow-[6px_6px_8px_rgba(50,50,0,0.1)]"
                                    >
                                        <div className="h-full bg-[#E6E7EB] transition-all hover:bg-blue p-0.5 rounded-2xl [clip-path:polygon(0_0,100%_0,100%_calc(100%-50px),calc(100%-50px)_100%,0_100%)] relative">
                                            <div className="h-full bg-white pt-5 rounded-2xl xl:pt-8 pb-5 px-5 xl:px-10 [clip-path:polygon(0_0,100%_0,100%_calc(100%-49px),calc(100%-49px)_100%,0_100%)]">
                                                <div className="text-center sm:text-start flex flex-col justify-between h-full">
                                                    <div className="flex items-center justify-center px-16">
                                                        {item?.image && (
                                                            <Image
                                                                src={item.image}
                                                                alt={item?.title || "service image"}
                                                                width={220}
                                                                height={224}
                                                            />
                                                        )}
                                                    </div>
                                                    <div className="content mt-5 sm:mt-0">
                                                        {item?.title && (
                                                            <h3 className="mt-2.5">{item.title}</h3>
                                                        )}
                                                        {item?.description && (
                                                            <p className="mt-3 text-base sm:text-lg font-normal">{item.description}</p>
                                                        )}
                                                        <span className="btn-primary group inline-flex p-0 bg-transparent text-body text-sm capitalize underline border-0 underline-offset-6 mt-4 cursor-pointer">
                                                            Read More
                                                            <svg
                                                                className="transition-all duration-500 group-hover:rotate-45 w-5 md:w-6 h-5 md:h-6 ml-1"
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
                                                        </span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </Link>
                                ))}
                            </div>
                        )}
                        {nextUrl && (
                            <div className="flex items-center justify-center mt-6 md:mt-12">
                                <button
                                    onClick={handleLoadMore}
                                    disabled={loading}
                                    className="btn-primary group inline-flex items-center"
                                >
                                    {loading ? "Loading..." : "Load More"}
                                    <svg
                                        className="transition-all duration-500 group-hover:rotate-45 w-5 md:w-6 h-5 md:h-6 ml-1"
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
                                </button>
                            </div>
                        )}
                    </div>
                </section>
            )}
        </>
    );
}
