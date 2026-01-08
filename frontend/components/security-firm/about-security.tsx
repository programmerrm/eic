import { MEDIA_URL } from "@/utils/api";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";
import PaymentInfo from "../about-page/paymnet-info";

export default async function AboutSecurity() {
    const security_firm_data = await getFetchData('/about/security-firm/');
    const bgImage = security_firm_data?.data?.bg ? `${MEDIA_URL}${security_firm_data.data.bg}` : null;
    return (
        <section className="bg-white py-12 md:py-[100px]">
            <div className="container">
                <div className="flex flex-col lg:flex-row">
                    <div className="w-full lg:max-w-[52.058%] lg:pt-8">
                        <h2>
                            <span className="text-blue">{security_firm_data?.data?.title_span}</span> {security_firm_data?.data?.title_normal}
                        </h2>
                        {security_firm_data?.data?.main_img && (
                            <div className="mt-5 md:mt-10 lg:mt-20">
                                {security_firm_data?.data?.main_img && (
                                    <Image src={`${MEDIA_URL}${security_firm_data?.data?.main_img}`} alt="security" width={655} height={555} />
                                )}
                            </div>
                        )}
                    </div>
                    <div className="w-full lg:max-w-[calc(100%-52.058%)] mb-16 relative mt-4 sm:mt-0">
                        <div
                            className="absolute w-[250px] mx-auto sm:w-full lg:max-w-[362px] xl:max-w-[462px] 2xl:max-w-[562px] h-[250px] sm:h-full lg:max-h-[362px] xl:max-h-[462px] 2xl:max-h-[562px] inset-0 bg-contain bg-top bg-no-repeat bg-rotate overflow-hidden rounded-full"
                            style={{
                                backgroundImage: `url(${bgImage})`,
                            }}></div>
                        <div className="content">
                            <div className="pt-10 lg:pt-[70px] xl:pt-[152px] sm:pl-16 lg:pl-20 xl:pl-40">
                                <div className=" text-body">
                                        <h3>{security_firm_data?.data?.mission_title}</h3>
                                        <p className="mt-3.5">{security_firm_data?.data?.mission_description}</p>
                                    </div>
                                    <div className="mt-8 text-body">
                                        <h3>{security_firm_data?.data?.vision_title}</h3>
                                        <p className="mt-3.5">{security_firm_data?.data?.vision_description}</p>
                                    </div>
                                    <div className="pt-12 z-50 relative">
                                        <Link href={security_firm_data?.data?.get_to_know_us_btn_url || ""} className="w-fit btn-primary group">
                                            {security_firm_data?.data?.get_to_know_us_btn_name}
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
                    </div>
                </div>
            </div>
            <PaymentInfo />
        </section>
    );
}
