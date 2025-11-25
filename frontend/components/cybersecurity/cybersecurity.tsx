/* eslint-disable @typescript-eslint/no-explicit-any */
import { MEDIA_URL } from "@/utils/api";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";

export default async function Cybersecurity() {
    const cybersecuritySolutionTitle = await getFetchData('/homepage/cyber-security-solution-title/');
    const cybersecuritySolutionItems = await getFetchData('/homepage/cyber-security-solution-items/');
    return (
        <section className="bg-blue pt-12 md:pt-[100px] pb-11 md:pb-[90px]">
            <div className="container">
                <div className="grid lg:grid-cols-2 items-center gap-8 md:gap-14 text-white">
                    <div className="order-2 lg:order-1">
                        <div className="mb-10 md:mb-[114px]">
                            <h2 className="text-white max-w-[602px] mb-4 md:mb-6">{cybersecuritySolutionTitle?.data?.title}</h2>
                            <p className="text-base sm:text-lg md:text-2xl md:leading-8 font-normal font-spacegrotesk">{cybersecuritySolutionTitle?.data?.description}</p>
                        </div>
                        <div className="grid grid-cols-2 gap-x-5 gap-y-16">
                            {cybersecuritySolutionItems?.map((item: any) => {
                                return (
                                    <div className="flex flex-col justify-between gap-6" key={item.id}>
                                        <div className="w-full max-w-11 sm:max-w-[60px]">
                                            <Image
                                                src={`${item?.image}`}
                                                alt="companies security"
                                                width={60}
                                                height={62}
                                            />
                                        </div>
                                        <div className="">
                                            <h5 className="text-base sm:text-lg leading-6 font-dmsans font-normal">{item?.title}</h5>
                                            <div className="h-0.5 w-full lg:max-w-[206px] bg-white/30 mt-4"></div>
                                            <span
                                                className="text-3xl sm:text-[40px] leading-10 font-semibold text-white font-spacegrotesk mt-4 block">{item?.count}+</span>
                                        </div>
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                    <div className="order-1 lg:order-2">
                        <div>
                            <Image
                                src={`${MEDIA_URL}${cybersecuritySolutionTitle?.data?.image}`}
                                alt="syber security"
                                width={762}
                                height={762}
                            />
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
}
