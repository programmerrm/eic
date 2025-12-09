/* eslint-disable @typescript-eslint/no-explicit-any */
import SectionBanner from "@/components/banner/section-banner";
import StayCompliant from "@/components/stay-compliant/stay-compliant";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";
import complianceBG from "../../../public/images/compliance-bg.svg";
import RelatedBGImg from "../../../public/images/related-image-bg.svg";
import trustedForProven from "../../../public/images/trusted-for-proven.png";
import FAQ from "@/components/FAQ/FAQ";
import Description from "@/components/paymnet-info/description";

type SingleServiceProps = {
    params: { slug: string };
};

export default async function SingleService({ params }: SingleServiceProps) {
    const { slug } = params;
    const singleService = await getFetchData(`/services/single/${slug}`);
    const complianceTitleData = await getFetchData('/configuration/compliance-title/');
    const complianceItemData = await getFetchData('/configuration/compliance-item/');
    const singleServiceData = singleService?.data || {};

    const topBar = {
        title: singleServiceData?.title || "",
        description: singleServiceData?.description || "",
    };

    return (
        <>
            <SectionBanner topBarData={topBar} />
            {/* MAIN ITEM SECTION */}
            {singleServiceData?.main_item && (
                <section className="py-6 md:py-12 lg:py-[100px]">
                    <div className="container">
                        <h2 className="w-full max-w-[692px] text-center sm:text-left">
                            {singleServiceData?.main_item?.normal_title}{" "}
                            <span className="text-blue">{singleServiceData?.main_item?.span_title}</span>
                        </h2>
                        <div className="mt-6 md:mt-12">
                            {singleServiceData?.items?.map((item: any) => (
                                <div
                                    className="flex flex-col sm:flex-row items-center gap-7 md:gap-14 mb-12 md:mb-24"
                                    key={item.id}
                                >
                                    <div className="w-full max-w-[215px]">
                                        <Image src={item.image} alt="pci" width={200} height={200} />
                                    </div>
                                    <div className="space-y-6 w-full max-w-[800px] text-center sm:text-start">
                                        <h3>{item.title}</h3>
                                        <p className="text-center sm:text-left">{item.description}</p>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                </section>
            )}
            {/* INCLUDE TOP SECTION */}
            {(singleServiceData?.include_top_title ||
                singleServiceData?.include_top_items?.length > 0) && (
                    <section className="bg-blue pt-6 md:pt-12 lg:pt-[100px] pb-6 md:pb-11 lg:pb-[90px]">
                        <div className="container">
                            <div className="text-white">
                                <div className="mb-10 md:mb-20 w-full max-w-[668px]">
                                    <h2 className="text-white max-w-[602px] mb-4 md:mb-6">
                                        {singleServiceData?.include_top_title?.title}
                                    </h2>
                                    <p className="text-base sm:text-lg md:text-2xl md:leading-8 font-normal font-spacegrotesk">
                                        {singleServiceData?.include_top_title?.description}
                                    </p>
                                </div>
                                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 w-full h-full gap-5">
                                    {singleServiceData?.include_top_items?.map((item: any) => (
                                        <div className="w-full md:max-w-[272px] flex flex-col items-start h-auto" key={item.id}>
                                            <div className="w-full max-w-11 sm:max-w-[60px]">
                                                <Image src={item?.image} alt={item.title} width={60} height={66} />
                                            </div>
                                            <h4 className="text-white mt-6 lg:min-h-[100px]">{item.title}</h4>
                                            <div className="h-0.5 w-full lg:max-w-full bg-white/30 mt-4"></div>
                                            <p className="text-sm sm:text-base mt-4">{item.description}</p>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        </div>
                    </section>
                )}
            {/* WHY CHOOSE US SECTION */}
            {(singleServiceData?.why_choose_us_title ||
                singleServiceData?.why_choose_us_item?.length > 0) && (
                    <section className="why-choose relative z-10 overflow-hidden">
                        <div className="container">
                            <div className="flex flex-col lg:flex-row justify-between">
                                <div className="w-full lg:w-1/2 order-2 lg:order-1">
                                    <div className="w-full lg:max-w-[400px] xl:max-w-[673px] pt-10 xl:pt-64">
                                        <h2 className="w-full md:w-[520px] relative z-20">
                                            {singleServiceData?.why_choose_us_title?.title_before_span}{" "}
                                            <span className="text-blue">
                                                {singleServiceData?.why_choose_us_title?.title_span}
                                            </span>{" "}
                                            {singleServiceData?.why_choose_us_title?.title_after_span}
                                        </h2>
                                        <ul className="mt-8">
                                            {singleServiceData?.why_choose_us_item?.map((item: any) => (
                                                <li key={item.id}>{item.name}</li>
                                            ))}
                                        </ul>
                                        <Link href="https://eic.com.bd/" className="btn-primary group inline-flex mt-10">Secure Your DATA
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
                                <div className="w-full lg:w-1/2 flex items-center justify-center lg:justify-end order-1 lg:order-2">
                                    <div className="pci-wrap w-full max-w-[200px] sm:max-w-[300px] md:max-w-[400px] lg:max-w-[536px] max-h-[640px] pt-24 md:pt-33 lg:pt-48 xl:pt-56 mb-20 sm:mb-28 md:mb-44 xl:mb-60 relative flex items-center justify-center">
                                        {singleServiceData?.why_choose_us_title?.image && (
                                            <Image
                                                className="lg:-ml-20"
                                                src={singleServiceData?.why_choose_us_title?.image}
                                                alt="components"
                                                width={536}
                                                height={640}
                                                priority
                                                fetchPriority="high"
                                            />
                                        )}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                )}
            {/* COMPLIANCE SECTION */}
            {complianceTitleData?.[0] &&
                Array.isArray(complianceItemData) &&
                complianceItemData.length > 0 && (
                    <section
                        className="pb-[270px] sm:pb-[300px] pt-6 md:pt-12 lg:pt-[210px] bg-contain bg-top-left bg-no-repeat lg:mt-[-290px]"
                        style={{ backgroundImage: `url(${trustedForProven.src})` }}
                    >
                        <div
                            className="my-12 md:my-[100px] bg-contain bg-bottom-right bg-no-repeat"
                            style={{ backgroundImage: `url(${complianceBG.src})` }}
                        >
                            <div className="container">
                                <div className="flex flex-col sm:flex-row justify-between mb-10 md:mb-14 gap-5">
                                    <h2 className="sm:max-w-[636px] w-full">
                                        {complianceTitleData[0]?.title_before_span}
                                        <span className="text-[#2E78AC]">
                                            {complianceTitleData[0]?.title_span}
                                        </span>
                                        {complianceTitleData[0]?.title_after_span}
                                    </h2>
                                    {complianceTitleData[0]?.btn_url && (
                                        <div className="flex items-center sm:max-w-[300px] w-full justify-start sm:justify-end">
                                            <Link href={complianceTitleData[0]?.btn_url} className="btn-primary group">
                                                {complianceTitleData[0]?.btn_name}
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
                                    )}
                                </div>

                                <div className="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                                    {complianceItemData?.map((item: any) => (
                                        <div
                                            className="p-4 md:p-6 bg-white border border-[#E6E7EB] rounded-[10px] transition-all hover:shadow-[25px_36px_18px_rgba(0,0,0,0.01),14px_20px_15px_rgba(0,0,0,0.05),6px_9px_11px_rgba(0,0,0,0.09),2px_2px_6px_rgba(0,0,0,0.1)]"
                                            key={item.id}
                                        >
                                            <div className="max-w-10 md:max-w-[60px] w-full">
                                                {item?.image && (
                                                    <Image src=
                                                        {item?.image}
                                                        alt={item?.title}
                                                        width={60}
                                                        height={66}
                                                        priority
                                                        fetchPriority="high"
                                                    />
                                                )}
                                            </div>
                                            <h4 className="mt-4">{item?.title}</h4>
                                            <ul className="protection-list mt-4 space-y-2">
                                                {item?.item_list?.map((i: any) => (
                                                    <li key={i.id}>{i.name}</li>
                                                ))}
                                            </ul>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        </div>
                    </section>
                )}
            {/* PAYMENT INFO */}
            <section className="relative z-10 pb-5 md:pb-10 -mt-[280px]">
                <div className="container">
                    <div className="flex flex-col lg:flex-row gap-5 justify-between">
                        <div className="w-full lg:max-w-[37.720%] pr-9 mt-8 lg:mt-16 xl:mt-28">
                            <h2 className="text-2xl sm:text-3xl md:text-[40px] md:leading-12 w-full lg:w-[500px] xl:w-[610px]">
                                {singleServiceData?.payment_info?.title_before_span}<span
                                    className="text-blue"> {singleServiceData?.payment_info?.title_span}</span> {singleServiceData?.payment_info?.title_after_span}
                            </h2>
                            <Description content={singleServiceData?.payment_info?.description} />
                            <div className="btn-wrap">
                                <Link href={singleServiceData?.payment_info?.btn_url || ""}
                                    className="btn-primary group inline-flex">{singleServiceData?.payment_info?.btn_name}
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
                        <div className="w-full lg:max-w-[calc(100%-37.720%)] flex flex-col items-end">
                            <div className="max-w-fit rounded-xl sm:rounded-3xl p-2 sm:p-[17px]">
                                <div className="flex items-center justify-between gap-5 px-2 sm:px-[30px] py-3 sm:py-5 rounded-md sm:rounded-[10px]">
                                    {singleServiceData?.payment_info?.image && (
                                        <Image
                                            src={singleServiceData?.payment_info?.image}
                                            alt="ieps"
                                            width={840}
                                            height={406}
                                            priority
                                            fetchPriority="high"
                                        />
                                    )}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            {/* INCLUDE BOTTOM SECTION */}
            {(singleServiceData?.include_bottom_title ||
                singleServiceData?.include_bottom_items?.length > 0) && (
                    <section className="bg-blue pt-6 md:pt-12 lg:pt-[100px] pb-6 md:pb-11 lg:pb-[90px]">
                        <div className="container">
                            <div className="mb-5 md:mb-10 w-full max-w-[668px]">
                                <h2 className="text-white max-w-[602px] mb-4 md:mb-6">
                                    {singleServiceData?.include_bottom_title?.title}
                                </h2>
                                <p className="text-white text-base sm:text-lg md:text-2xl md:leading-8 font-normal font-spacegrotesk">
                                    {singleServiceData?.include_bottom_title?.description}
                                </p>
                            </div>

                            <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-x-6 md:gap-x-8 2xl:gap-x-[125px] gap-y-5 md:gap-y-10 lg:gap-y-14">
                                {singleServiceData?.include_bottom_items?.map((item: any, index: number) => (
                                    <div className="flex flex-col gap-1 pr-4" key={item.id}>
                                        <h2 className="text-5xl md:text-6xl lg:text-[88px] font-bold bg-linear-to-b from-white from-30% to-blue bg-clip-text text-transparent font-svatopluk py-1">
                                            {index + 1}
                                        </h2>
                                        <div className="content">
                                            <h4 className="text-white">{item?.title}</h4>
                                            <div className="h-0.5 w-full bg-white/30 mt-4"></div>
                                            <p className="text-white text-sm sm:text-base mt-4">{item?.description}</p>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </section>
                )}

            {/* RELATED SERVICES */}
            {singleServiceData?.related_services?.length > 0 && (
                <section
                    className="mt-12 lg:mt-[100px] pb-6 md:pb-12 lg:pb-[164px] bg-contain bg-top-right bg-no-repeat"
                    style={{ backgroundImage: `url(${RelatedBGImg.src})` }}
                >
                    <div className="container">
                        <div className="w-full max-w-[588px] mx-auto">
                            <h2 className="text-center">Comprehensive Cybersecurity Solutions</h2>
                        </div>
                        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-8 mt-12">
                            {singleServiceData?.related_services?.slice(0, 3)?.map((item: any) => (
                                <div key={item.id} className="hover:filter hover:drop-shadow-[6px_6px_8px_rgba(50,50,0,0.1)]">
                                    <div className="group h-full bg-[#E6E7EB] hover:bg-blue p-0.5 rounded-2xl [clip-path:polygon(0_0,100%_0,100%_calc(100%-50px),calc(100%-50px)_100%,0_100%)] relative transition-all ">
                                        <Link 
                                            
                                            href={`/services/${item?.slug}`}
                                            className=" absolute inset-0 z-10"
                                        > </Link>
                                        <div className="h-full bg-white group-hover:bg-blue transition-all duration-500 rounded-2xl pt-5 xl:pt-8 pb-5 xl:pb-6 pl-6 xl:pl-10 pr-5 xl:pr-8 [clip-path:polygon(0_0,100%_0,100%_calc(100%-49px),calc(100%-49px)_100%,0_100%)]">
                                            <div className="text-center sm:text-start flex flex-col justify-between h-full">
                                                <div className="text-center sm:text-start">
                                                    <div className="flex items-center justify-center px-16">
                                                        <Image
                                                            src={item?.image}
                                                            alt={item?.title}
                                                            width={235}
                                                            height={224}
                                                            priority 
                                                            fetchPriority="high"
                                                        />
                                                    </div>
                                                </div>
                                                <div className="content mt-5 sm:mt-0">
                                                    <h3 className="mt-2.5 group-hover:text-white">{item?.title}</h3>
                                                    <p className=" mt-3 mx-auto sm:mx-0 group-hover:text-white">
                                                        {item.description}
                                                    </p>
                                                    <span
                                                        className="btn-primary inline-flex p-0 bg-transparent text-body text-sm capitalize underline border-0 underline-offset-6 mt-4 group-hover:text-white">Read
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
                                                    </span>
                                                </div>
                                            </div>


                                        </div>
                                    </div>
                                </div>
                            ))}
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

            {/* FAQ SECTION */}
            {singleServiceData?.faqs?.length > 0 && (
                <section className="pb-12 lg:pb-[100px]">
                    <div className="container">
                        <div className="w-full lg:flex lg:items-center lg:justify-between lg:gap-8">

                            {/* LEFT: FAQ */}
                            <div className="w-full lg:w-[60%] order-2 lg:order-1 mt-5 lg:mt-0">
                                <h2 className="max-w-[500px]">
                                    <span className="text-blue">FAQs</span>{" "}
                                    {singleServiceData?.faqs?.[0]?.title}
                                </h2>
                                <div className="w-full max-w-[696px] space-y-4 mt-10">
                                    <FAQ faqItems={singleServiceData?.faq_items || []} />
                                </div>
                            </div>

                            {/* RIGHT: IMAGE */}
                            <div className="w-full lg:w-[40%] order-1 lg:order-2 lg:flex lg:justify-end">
                                {singleServiceData?.faqs?.[0]?.image && (
                                    <Image
                                        src={singleServiceData?.faqs?.[0]?.image}
                                        alt="faq"
                                        width={515}
                                        height={485}
                                        priority
                                        fetchPriority="high"
                                        className="h-auto w-auto max-w-full"
                                    />
                                )}
                            </div>

                        </div>
                    </div>
                </section>
            )}


            <StayCompliant />
        </>
    );
}
