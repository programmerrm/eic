import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";

export default async function StayCompliant() {
    const stayCompliantData = await getFetchData('/configuration/stay-compliant/');
    const data = stayCompliantData[0];
    console.log('image url -- ', data);
    return (
        <>
            {data && (
                <section className="stay-compliant-section pb-12 md:pb-[100px]">
                    <div className="container">
                        <div
                            className="bg-blue pl-6 sm:pl-12 md:pl-[83px] pr-6 sm:pr-12 md:pr-[90px] rounded-2xl flex flex-col lg:flex-row items-center ">
                            <div className="w-full lg:max-w-[49.283%] xl:-mr-9 order-2 lg:order-1 mb-6 sm:mb-11 lg:mb-0">
                                {data?.title && (
                                    <h2 className="text-white mb-6">{data?.title}</h2>
                                )}
                                {data?.description && (
                                    <p className="text-white mb-8">{data?.description}</p>
                                )}
                                <div className="flex flex-wrap items-center gap-4">
                                    <Link href="" className="btn-secondary group">Get started with us
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
                                    <Link href="/contact" className="btn-primary group border border-white">Contact us
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
                            <div className="w-full lg:max-w-[53.664%] mt-6 sm:mt-11 mb-8 sm:mb-16 lg:mb-[124px] order-1 lg:order-2">
                                {data?.image && (
                                    <Image
                                        src={data?.image}
                                        alt="stay compliant"
                                        width={640}
                                        height={485}
                                    />
                                )}
                            </div>
                        </div>
                    </div>
                </section>
            )}
        </>
    );
}
