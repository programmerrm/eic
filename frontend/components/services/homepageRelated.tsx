/* eslint-disable @typescript-eslint/no-explicit-any */
import Link from "next/link";
import BannerImg from "../../public/images/compliance-bg.svg";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";

export default async function HomePageRelated() {
    const data = await getFetchData("/services/list-items/", {
        tag: "services-item",
    });
    return (
        <section className="pt-5 md:pt-10 lg:pt-[52px] mt-5 md:mt-10 lg:mt-12 pb-3 md:pb-6 mb-12 lg:mb-24 bg-contain bg-top-right bg-no-repeat"
            style={{
                backgroundImage: `url(${BannerImg.src})`,
            }}>
            <div className="container">
                <div className="w-full max-w-[588px] mx-auto">
                    <h2 className="text-center">Comprehensive Cybersecurity Solutions</h2>
                </div>
                <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-8 mt-12">
                    {data?.results?.data?.slice(0, 3)?.map((item: any) => {
                        return (
                            <div key={item.id} className=" transition-all hover:filter hover:drop-shadow-[6px_6px_8px_rgba(50,50,0,0.1)]">
                                <div className="h-full group bg-[#E6E7EB] transition-all hover:bg-blue p-0.5 rounded-2xl [clip-path:polygon(0_0,100%_0,100%_calc(100%-50px),calc(100%-50px)_100%,0_100%)] relative">
                                <Link href={`/services/${item.slug}`} className=" absolute inset-0 z-10">
                                </Link>
                                    <div className="h-full bg-white transition-all duration-500 group-hover:bg-blue group-hover:text-white group-hover:border-blue rounded-2xl pt-5 xl:pt-8 pb-5 xl:pb-6 pl-6 xl:pl-10 pr-5 xl:pr-8 [clip-path:polygon(0_0,100%_0,100%_calc(100%-49px),calc(100%-49px)_100%,0_100%)]">
                                        <div className="text-center sm:text-start flex flex-col justify-between h-full">
                                            <div className="flex items-center justify-center px-16">
                                                <Image
                                                    src={item.image}
                                                    alt={item.title}
                                                    width={216}
                                                    height={220}
                                                    priority 
                                                    fetchPriority="high"
                                                />
                                            </div>
                                            <div>
                                                <h3 className="mt-2.5 group-hover:text-white">{item.title}</h3>
                                                <p className=" mt-3 mx-auto sm:mx-0">{item.description}</p>
                                                <span className="btn-primary inline-flex p-0 bg-transparent text-body text-sm capitalize underline border-0 underline-offset-6 mt-4 cursor-pointer group-hover:text-white ">
                                                    Read More
                                                    <svg
                                                        className="transition-all duration-500 w-5 md:w-6 h-5 md:h-6 ml-1 group-hover:rotate-45"
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
                            </div>
                            
                        );
                    })}
                </div>
                <div className="flex items-center justify-center mt-6 md:mt-12">
                    <Link href="/services" className="btn-primary group">View All Services
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
