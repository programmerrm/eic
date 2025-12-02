/* eslint-disable @typescript-eslint/no-explicit-any */
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";

export default async function WhyChoose() {
    const experienceEic = await getFetchData('/homepage/experience-eic/', {
        tag: 'experience-eic-data',
    })
    const experienceEicItem = await getFetchData('/homepage/experience-eic-item/', {
        tag: 'experience-eic-item-data',
    });

    return (
        <section className="why-choose eic-home relative z-10 overflow-hidden">
            <div className="container">
                <div className="flex flex-col lg:flex-row justify-between">
                    <div className="w-full lg:w-1/2 order-2 lg:order-1">
                        <div className="w-full lg:w-[450px] max-w-[370px] lg:max-w-[450px] pt-10 lg:pt-74">
                            <h2>{experienceEic?.data?.normal_title} <span className="text-blue">{experienceEic?.data?.span_title}</span></h2>
                            {experienceEicItem?.data && (
                                <ul className="mt-8 w-full max-w-[380px] xl:max-w-[450px]">
                                    {experienceEicItem?.data?.map((item: any) => {
                                        return (
                                            <li key={item.id}>{item.name}</li>
                                        );
                                    })}
                                </ul>
                            )}
                            <Link href={experienceEic?.data?.btn_url} className="btn-primary group inline-flex mt-10">{experienceEic?.data?.btn_name}
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
                        <div
                            className="pci-wrap w-full max-w-[250px] sm:max-w-[350px] md:max-w-[420px] lg:max-w-[687px] max-h-[740px] pt-20 sm:pt-33 lg:pt-48 xl:pt-56 mb-20 sm:mb-28 md:mb-20 xl:mb-60 relative flex items-center justify-center lg:justify-end">
                            {experienceEic?.data?.image && (
                                <Image
                                    src={experienceEic?.data?.image}
                                    alt="eic"
                                    width={687}
                                    height={742}
                                    priority 
                                    fetchPriority="high"
                                />
                            )}
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
}
