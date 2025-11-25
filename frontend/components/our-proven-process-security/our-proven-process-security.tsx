/* eslint-disable @typescript-eslint/no-explicit-any */
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";

export default async function OurProvenProcessSecurity() {
    const ourProvenProcessSecurity = await getFetchData('/homepage/our-proven-process-security/');
    const ourProvenProcessSecurityItems = await getFetchData('/homepage/our-proven-process-security-items/');
    return (
        <section className="bg-[#F4F8FB] py-12 md:py-[100px]">
            <div className="container">
                <div className="flex flex-col lg:flex-row justify-between gap-10">
                    <div className="w-full max-w-[480px] mx-auto lg:mx-0 text-center lg:text-start flex flex-col items-center lg:items-start">
                        <h2 className="mb-3 lg:mb-6">{ourProvenProcessSecurity?.data?.title_before_span} <span className="text-blue">{ourProvenProcessSecurity?.data?.title_span}</span> {ourProvenProcessSecurity?.data?.title_after_span}</h2>
                        <p className="mb-6 lg:mb-11">{ourProvenProcessSecurity?.data?.description}</p>
                        <div className="max-w-[200px] lg:max-w-full">
                            <Image
                                src={ourProvenProcessSecurity?.data?.image}
                                alt="Our Proven Security"
                                width={345}
                                height={345}
                            />
                        </div>
                    </div>
                    <div className="w-full max-w-[444px] mx-auto lg:mx-0">
                        {ourProvenProcessSecurityItems?.map((item: any) => {
                            return (
                                <div className=" text-center lg:text-start flex flex-col items-center lg:items-start mb-4 lg:mb-8 last-of-type:mb-0" key={item.id}>
                                    <div className="mb-2 lg:mb-[18px] max-w-20 lg:max-w-full">
                                        <Image
                                            src={item?.image}
                                            alt={item?.title}
                                            width={100}
                                            height={106}
                                        />
                                    </div>
                                    <h3 className="mb-2 lg:mb-4">{item?.title}</h3>
                                    <p>{item?.description}</p>
                                </div>
                            );
                        })}
                    </div>
                </div>
            </div>
        </section>
    );
}
