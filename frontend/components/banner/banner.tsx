import { MEDIA_URL } from "@/utils/api";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";
import BannerImg from "../../public/images/hero-banner.svg"
import PaymentInfo from "../paymnet-info/paymnet-info";

export default async function Banner() {
    const banner = await getFetchData('https://eicsec.com/api/v1/homepage/banner/');
    return (
        <>
            <section className="relative pb-11 w-full mx-auto overflow-hidden bg-contain bg-top bg-no-repeat"
                style={{
                    backgroundImage: `url(${BannerImg.src})`,
                }}
            >
                <div className="container relative z-10">
                    <div className="flex flex-col lg:flex-row pt-[120px] lg:pt-[190px] pb-12 2xl:pb-[130px]">
                        <div className="w-full lg:max-w-[754px] order-2 lg:order-1 mt-10 lg:mt-0">
                            {banner?.data?.title && (
                                <h1 className="text-body uppercase">{banner?.data?.title}</h1>
                            )}
                            {banner?.data?.description && (
                                <p className="w-full max-w-[606px] text-base sm:text-xl md:text-2xl md:leading-8 font-normal text-[#245E86] font-spacegrotesk my-4 sm:my-8">{banner?.data?.description}</p>
                            )}
                            <div className="flex flex-col sm:flex-row items-center gap-2">
                                {banner?.data?.secure_business_btn_name && (
                                    <Link href={banner?.data?.secure_business_btn_url || ""} className="w-fit btn-primary group">{banner?.data?.secure_business_btn_name}
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
                                )}
                                {banner?.data?.company_profile_btn_name && (
                                    <Link href={banner?.data?.company_profile_btn_url || ""} className="w-fit btn-secondary group">{banner?.data?.company_profile_btn_name}
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
                                )}
                            </div>
                        </div>
                        <div className="w-full lg:max-w-[52.132%] order-1 lg:order-2 lg:mt-16">
                            {banner?.data?.image && (
                                <Image
                                    src={`${MEDIA_URL}${banner?.data?.image}`}
                                    alt="hero-banner-image"
                                    width={710}
                                    height={640}
                                />
                            )}
                        </div>
                    </div>
                    <PaymentInfo />
                </div>
            </section>
        </>
    );
}
