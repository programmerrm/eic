/* eslint-disable @typescript-eslint/no-explicit-any */
import SectionBanner from "@/components/banner/section-banner";
import StayCompliant from "@/components/stay-compliant/stay-compliant";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";
import complianceBG from "../../../public/images/compliance-bg.svg";
import RelatedBGImg from "../../../public/images/related-image-bg.svg";
import trustedForProven from "../../../public/images/trusted-for-proven.png";

type SingleServiceProps = {
    params: Promise<{ slug: string }>;
};

export default async function SingleService({ params }: SingleServiceProps) {
    const { slug } = await params;
    const singleService = await getFetchData(`/services/single/${slug}`);
    const complianceTitleData = await getFetchData('/configuration/compliance-title/');
    const complianceItemData = await getFetchData('/configuration/compliance-item/');

    const singleServiceData = singleService[0];
    const topBar = {
        title: singleService[0]?.title || "",
        description: singleService[0]?.description || "",
    };

    return (
        <>
            <SectionBanner topBarData={topBar} />

            {/* SERVICE ITEM SECTION START */}
            {singleServiceData?.main_item && (
                <section className="py-12 md:py-[100px]">
                    <div className="container">
                        <h2 className="w-full max-w-[692px]">{singleServiceData?.main_item?.normal_title} <span className="text-blue">{singleServiceData?.main_item?.span_title}</span></h2>
                        <div className="mt-6 md:mt-12">
                            {singleServiceData?.items?.map((item: any) => {
                                return (
                                    <div className="flex flex-col sm:flex-row items-center gap-7 md:gap-14 mb-12 md:mb-24" key={item.id}>
                                        <div className="w-full max-w-[215px]">
                                            <Image
                                                src={item.image}
                                                alt="pci"
                                                width={215}
                                                height={210}
                                            />
                                        </div>
                                        <div className="space-y-6 w-full max-w-[800px] text-center sm:text-start">
                                            <h3>{item.title}</h3>
                                            <p>{item.description}</p>
                                        </div>
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                </section>
            )}
            {/* SERVICE ITEM SECTION END */}

            {/* SERVICE TOP START */}
            <section className="bg-blue pt-12 md:pt-[100px] pb-11 md:pb-[90px]">
                <div className="container">
                    <div className=" text-white">
                        <div className="mb-10 md:mb-[114px] w-full max-w-[668px]">
                            <h2 className="text-white max-w-[602px] mb-4 md:mb-6">{singleServiceData?.include_top_title?.title}</h2>
                            <p className="text-base sm:text-lg md:text-2xl md:leading-8 font-normal font-spacegrotesk">{singleServiceData?.include_top_title?.description}</p>
                        </div>
                        <div className="flex flex-wrap justify-between h-full gap-5">
                            {singleServiceData?.include_top_items?.map((item: any) => {
                                return (
                                    <div className="w-full max-w-[272px] flex flex-col items-start h-auto" key={item.id}>
                                        <div>
                                            <div className="w-full max-w-11 sm:max-w-[60px]">
                                                <Image
                                                    src={item?.image}
                                                    alt={item.title}
                                                    width={60}
                                                    height={66}
                                                />
                                            </div>
                                            <h4 className="text-white mt-6 lg:min-h-[100px]">{item.title}</h4>
                                        </div>
                                        <div className="">
                                            <div className="h-0.5 w-full lg:max-w-full bg-white/30 mt-4"></div>
                                            <p className="text-sm sm:text-base mt-4">{item.description}</p>
                                        </div>
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                </div>
            </section>
            {/* SERVICE TOP END */}

            <section className="pb-[270px] sm:pb-[300px] pt-12 lg:pt-[210px] bg-contain bg-top-left bg-no-repeat"
                style={{
                    backgroundImage: `url(${trustedForProven.src})`,
                }}>
                <div className="my-12 md:my-[100px] bg-contain bg-bottom-right bg-no-repeat"
                    style={{
                        backgroundImage: `url(${complianceBG.src})`,
                    }}>
                    <div className="container">
                        <div className="flex flex-col sm:flex-row justify-between mb-10 md:mb-20 gap-5">
                            <h2 className="sm:max-w-[636px] w-full">{complianceTitleData[0]?.title_before_span}<span className="text-[#2E78AC]">{complianceTitleData[0]?.title_span}</span>
                                {complianceTitleData[0]?.title_after_span}</h2>
                            <div className="flex items-center sm:max-w-[300px] w-full justify-center sm:justify-end">
                                <a href={complianceTitleData[0]?.btn_url || ""} className="btn-primary group">{complianceTitleData[0]?.btn_name}
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
                                </a>
                            </div>
                        </div>
                        <div className="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                            {complianceItemData?.map((item: any) => {
                                return (
                                    <div
                                        className="p-4 md:p-8 bg-white border border-[#E6E7EB] rounded-[10px] transition-all hover:shadow-[25px_36px_18px_rgba(0,0,0,0.01),14px_20px_15px_rgba(0,0,0,0.05),6px_9px_11px_rgba(0,0,0,0.09),2px_2px_6px_rgba(0,0,0,0.1)] cursor-pointer" key={item.id}>
                                        <div className="max-w-10 md:max-w-[60px] w-full">
                                            {item?.image && (
                                                <Image
                                                    src={item?.image}
                                                    alt={item?.title}
                                                    width={60}
                                                    height={66}
                                                />
                                            )}
                                        </div>
                                        {item?.title && (
                                            <h4 className="mt-4">{item?.title}</h4>
                                        )}
                                        {item?.item_list && (
                                            <ul className="protection-list mt-4">
                                                {item?.item_list.map((i: any) => {
                                                    return (
                                                        <li key={i.id}>{i.name}</li>
                                                    );
                                                })}
                                            </ul>
                                        )}
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                </div>
            </section>

            <section className="relative z-10 pb-5 md:pb-10 -mt-[280px]">
                <div className="container">
                    <div className="flex flex-col lg:flex-row  gap-5 justify-between">
                        <div className="w-full lg:max-w-[37.720%] pr-9 mt-8 lg:mt-16 xl:mt-28">
                            <h2 className="text-2xl sm:text-3xl md:text-[40px] md:leading-12 w-full lg:w-[500px] xl:w-[610px]">Securing <span
                                className="text-blue">Top</span> Brands</h2>
                            <p
                                className=" text-base sm:text-xl md:text-2xl md:leading-8 text-[#245E86] mt-2 sm:mt-3 mb-3 sm:mb-6 w-full lg:w-[400px] xl:w-[610px] font-spacegrotesk">
                                Trusted by nearly 200+ Companies</p>

                            <div className="btn-wrap">
                                <a href="#" className="btn-primary group inline-flex">Get Started
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
                                </a>
                            </div>
                        </div>
                        <div className="w-full lg:max-w-[calc(100%-37.720%)] flex flex-col items-end">
                            <div className="w-[71.074%] border border-[#F4F4F6] rounded-xl sm:rounded-3xl p-2 sm:p-[17px]">
                                <div
                                    className="bg-[#F4F4F6] flex items-center justify-between gap-5 px-2 sm:px-[30px] py-3 sm:py-5 rounded-md sm:rounded-[10px]">
                                    <a href="">
                                        <Image
                                            src="./src/assets/logo/ieps.svg"
                                            alt="ieps"
                                            width={835}
                                            height={410}
                                        />
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* SERVICE BOTTOM START */}
            <section className="bg-blue pt-12 md:pt-[100px] pb-11 md:pb-[90px]">
                <div className="container">
                    <div className="mb-5 md:mb-10 w-full max-w-[668px]">
                        <h2 className="text-white max-w-[602px] mb-4 md:mb-6">{singleServiceData?.include_bottom_title?.title}</h2>
                        <p className="text-white text-base sm:text-lg md:text-2xl md:leading-8 font-normal font-spacegrotesk">{singleServiceData?.include_bottom_title?.description}</p>
                    </div>
                    <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-x-6 md:gap-x-8 lg:gap-x-16 xl:gap-x-[125px] gap-y-5 md:gap-y-9">
                        {singleServiceData?.include_bottom_items?.map((item: any, index: number) => {
                            return (
                                <div className="flex flex-col justify-between gap-1 pr-4" key={item.id}>
                                    <h2 className="text-6xl md:text-[88px] font-bold bg-linear-to-b from-white to-blue bg-clip-text text-transparent font-sans">{index + 1}</h2>
                                    <div className="content">
                                        <h4 className="text-white">{item?.title}</h4>
                                        <div className="h-0.5 w-full bg-white/30 mt-4"></div>
                                        <p className="text-white text-sm sm:text-base my-4">{item?.description}</p>
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                </div>
            </section>
            {/* SERVICE BOTTOM END */}

            {/* SERVICE RELATED START */}
            {singleServiceData?.related_services && (
                <section className="mt-12 md:mt-[100px] pb-12 lg:pb-[164px] bg-contain bg-top-right bg-no-repeat"
                    style={{
                        backgroundImage: `url(${RelatedBGImg.src})`,
                    }}>
                    <div className="container">
                        <div className="w-full max-w-[588px] mx-auto">
                            <h2 className="text-center">Comprehensive Cybersecurity Solutions</h2>
                        </div>
                        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-8 mt-12">
                            {singleServiceData?.related_services?.map((item: any) => {
                                return (
                                    <Link
                                        className="h-full transition-all hover:filter hover:drop-shadow-[6px_6px_8px_rgba(50,50,0,0.1)]" key={item.id} href={`/services/${item?.slug}`}>
                                        <div
                                            className="h-full bg-[#E6E7EB] transition-all hover:bg-blue p-0.5 rounded-2xl [clip-path:polygon(0_0,100%_0,100%_calc(100%-50px),calc(100%-50px)_100%,0_100%)] relative">
                                            <div
                                                className="h-full bg-white rounded-2xl pt-5 xl:pt-8 pb-5 xl:pb-6 pl-6 xl:pl-10 pr-5 xl:pr-8 [clip-path:polygon(0_0,100%_0,100%_calc(100%-49px),calc(100%-49px)_100%,0_100%)]">
                                                <div className="text-center sm:text-start">
                                                    <div className="flex items-center justify-center px-16">
                                                        <Image
                                                            src={item?.image}
                                                            alt={item?.title}
                                                            width={220}
                                                            height={224}
                                                        />
                                                    </div>
                                                    <h3 className="mt-2.5">{item?.title}</h3>
                                                    <p className=" mt-3 mx-auto sm:mx-0">
                                                        {item.description}
                                                    </p>
                                                    <Link href={`/services/${item?.slug}`}
                                                        className="btn-primary group inline-flex p-0 bg-transparent text-body text-sm capitalize underline border-0 underline-offset-6 mt-4">Read
                                                        More
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
                                        </div>
                                    </Link>
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
            )}
            {/* SERVICE RELATED END */}

            {/* FAQ SECTION START */}
            {singleServiceData?.faqs.length > 0 && (
                <section className="pb-12 md:pb-[100px]">
                    <div className="container">

                        <div className="flex flex-col lg:flex-row items-center">
                            <div className="w-full lg:max-w-[60.955%] order-2 lg:order-1">
                                <h2 className="w-full max-w-[658px] mx-auto lg:mx-0 text-center lg:text-start"><span className="text-blue">FAQs</span> {singleServiceData?.faqs[0]?.title}</h2>
                                <div className="w-full max-w-[696px] space-y-4 mt-10 md:mt-20">
                                    {singleServiceData?.faq_items?.map((item: any) => {
                                        return (
                                            <div className="faq-item" key={item.id}>
                                                <div className="faq-content">
                                                    <h4>{item?.question}</h4>
                                                    <p className="mt-2 text-sm sm:text-base">{item?.answer}</p>
                                                </div>
                                                <div className="faq-icon">
                                                    <i></i>
                                                    <i></i>
                                                </div>
                                            </div>
                                        );
                                    })}
                                </div>
                            </div>
                            <div className="w-full lg:max-w-[calc(100%-60.955%)] order-1 lg:order-2">
                                <Image
                                    src={singleServiceData?.faqs[0]?.image}
                                    alt='faq'
                                    width={515}
                                    height={485}
                                />
                            </div>
                        </div>
                    </div>
                </section>
            )}
            {/* FAQ SECTION END */}

            <StayCompliant />
        </>
    );
}
