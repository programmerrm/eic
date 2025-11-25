import { MEDIA_URL } from "@/utils/api";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";

export default async function Banner() {
    const banner = await getFetchData('/homepage/banner/');
    return (
        <>
            <section className="relative pb-11 w-full overflow-hidden min-h-[400px] sm:min-h-[500px] md:min-h-[600px] lg:min-h-[700px]">
                {banner?.data?.video_file && (
                    <video
                        className="absolute inset-0 w-full h-full object-cover"
                        src={`${MEDIA_URL}${banner.data.video_file}`}
                        autoPlay
                        muted
                        loop
                        playsInline
                    />
                )}
                <div className="container relative z-10">
                    <div className="max-w-[754px] pt-[211px] pb-12 md:pb-[260px]">
                        {banner?.data?.title && (
                            <h1 className="text-body uppercase">{banner?.data?.title}</h1>
                        )}
                        {banner?.data?.description && (
                            <p className="max-w-[691px] text-base sm:text-xl md:text-2xl md:leading-8 font-normal text-[#245E86] font-spacegrotesk my-4 sm:my-8">{banner?.data?.description}</p>
                        )}
                        <div className="flex flex-col sm:flex-row items-center gap-2">
                            {banner?.data?.secure_business_name && (
                                <Link href={banner?.data?.secure_business_url || ""} className="w-fit btn-primary group">{banner?.data?.secure_business_name}
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
                            {banner?.data?.company_profile_name && (
                                <Link href={banner?.data?.company_profile_url || ""} className="w-fit btn-secondary group">{banner?.data?.company_profile_name}
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
                </div>
            </section>
            <section className="relative z-10 pb-5 md:pb-10">
                <div className="container">
                    <div className="mt-8 sm:mt-16 xl:mt-28">
                        {banner?.data?.sub_title && (
                            <h2 className="text-2xl sm:text-3xl md:text-[40px] md:leading-12 -mb-28 w-full max-w-[500px] xl:max-w-[620px]">{banner?.data?.sub_title}</h2>
                        )}
                        <div className="flex flex-col lg:flex-row  gap-5 justify-between">
                            <div className="w-full lg:max-w-[37.720%] pr-9 mt-28">
                                {banner?.data?.short_description && (
                                    <p className="text-base sm:text-xl md:text-2xl md:leading-8 text-[#245E86] mt-2 sm:mt-3 mb-3 sm:mb-6">{banner?.data?.short_description}</p>
                                )}
                                <div className="btn-wrap">
                                    <Link href={banner?.data?.get_started_url || ""} className="w-fit btn-primary group">{banner?.data?.get_started_name}
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
                            {banner?.data?.payment_logo && (
                                <div className="w-full lg:max-w-[calc(100%-37.720%)] flex flex-col items-end">
                                    <Image src={`${MEDIA_URL}${banner?.data?.payment_logo}`} alt="payment-logo" width={770} height={410} />
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            </section >
        </>
    );
}
