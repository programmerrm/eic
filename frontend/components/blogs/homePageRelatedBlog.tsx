/* eslint-disable @typescript-eslint/no-explicit-any */
import Link from "next/link";
import BannerImg from "../../public/images/banner-img.svg";
import Image from "next/image";
import { getFetchData } from "@/utils/getFetchData";

export default async function HomePageRelatedBlog() {
    const blogsItem = await getFetchData('/blogs/list/', {
        tag: "blogs-list-data",
    });
    if (!blogsItem?.results?.data) {
        return null;
    }
    return (
        <section
            className="pt-6 md:pt-12 pb-12 md:pb-[100px] bg-bottom 2xl:bg-position-[center_calc(100%+300px)] bg-contain bg-no-repeat -mt-20"
            style={{
                backgroundImage: `url(${BannerImg.src})`,
            }}>
            <div className="container">
                <div className="w-full max-w-[616px] mx-auto text-center">
                    <h2>Browse Our Latest Insights on <span className="text-blue">Cybersecurity</span></h2>
                </div>
                <div id="BrowserLatest" className="grid sm:grid-cols-2 md:grid-cols-3 py-6 md:py-12 gap-5 lg:gap-9">
                    {blogsItem?.results?.data && (
                        <>
                            {blogsItem?.results?.data?.map((item: any) => {
                                <div className="items">
                                    <Link href={`/blogs/${item.slug}`} className="group">
                                        {item.image && (
                                            <Image
                                                src={item.image}
                                                alt={item.title}
                                                width={429}
                                                height={312}
                                                className="w-full h-auto transition-transform duration-500 ease-in-out group-hover:scale-105"
                                            />
                                        )}
                                    </Link>
                                    <div className="group">
                                        <time
                                            className="text-body text-sm font-medium leading-5 -tracking-[0.14px] mt-3 md:mt-7 inline-block transition-all group-hover:text-blue">July
                                            15, 2025 · 7 min read</time>
                                        <h4 className="my-1 md:my-3 font-dmsans transition-all group-hover:text-blue">
                                            <Link href={`/blogs/${item.slug}`}>{item.title}</Link>
                                        </h4>
                                        <div className="flex gap-2 flex-wrap">
                                            <button className="bg-[#EBF3F8] px-3 py-1 rounded-lg text-body font-medium text-sm leading-5 -tracking-[0.14px] font-inter cursor-pointer transition-all group-hover:text-blue">Research Report</button>
                                        </div>
                                    </div>
                                </div>
                            })}
                        </>
                    )}
                </div>
                <div className="flex items-center justify-center">
                    <Link href="/blogs" className="btn-primary group">Explore All
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
    );
}
