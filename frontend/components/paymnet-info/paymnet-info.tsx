import { MEDIA_URL } from "@/utils/api";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";
import Description from "./description";

export default async function PaymentInfo() {
    const paymnetInfo = await getFetchData('/homepage/paymnet-info/');
    return (
        <>
            {paymnetInfo?.data && (
                <div className="relative z-10 pb-5 md:pb-10 mx-auto">
                    <div className="container">
                        <div className="flex flex-col items-center md:mt-12 lg:mt-[98px] lg:flex-row  gap-5 justify-between">
                            <div className="w-full lg:max-w-[37.720%] pr-9 order-2 lg:order-1 lg:-mt-9">
                                <h2 className="text-2xl sm:text-3xl md:text-[40px] md:leading-12 w-full lg:w-[500px] xl:w-[610px]">{paymnetInfo?.data?.title_before_span} <span className="text-blue">{paymnetInfo?.data?.title_span}</span> {paymnetInfo?.data?.title_after_span}</h2>
                                <Description content={paymnetInfo?.data?.description} />
                                <div className="btn-wrap">
                                    <Link href={paymnetInfo?.data?.btn_url || ""} className="btn-primary group inline-flex">{paymnetInfo?.data?.btn_name || "Get Started"}
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
                            <div className="w-full lg:max-w-[calc(100%-37.720%)] flex flex-col items-end order-1 lg:order-2">
                                <div className="w-full lg:max-w-fit flex flex-col items-end">
                                    {paymnetInfo?.data?.image && (
                                        <Image
                                            src={`${MEDIA_URL}${paymnetInfo?.data?.image}`}
                                            alt="payment-logo"
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
                </div >
            )}
        </>
    );
}
