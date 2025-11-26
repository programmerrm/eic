/* eslint-disable @typescript-eslint/no-explicit-any */
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";

export default async function Features() {
    const featureTitle = await getFetchData('/feature/title/');
    const featureItems = await getFetchData('/feature/items/');
    return (
        <section className="py-12 md:py-[100px]">
            <div className="container">
                {featureTitle?.data && (
                    <div className="flex flex-col sm:flex-row justify-between mb-10 md:mb-20 gap-5">
                        <h2 className="w-full max-w-[841px]">{featureTitle?.data?.title_before_span} <span className="text-[#2E78AC]">{featureTitle?.data?.title_span}</span>{featureTitle?.data?.title_after_span}</h2>
                        <div className="flex items-center sm:max-w-[300px] w-full justify-center sm:justify-end">
                            <Link href={featureTitle?.data?.features_btn_url || ""} className="btn-primary group">{featureTitle?.data?.features_btn_name}
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
                )}
                {featureItems?.data && (
                    <div className="grid md:grid-cols-2 gap-6">
                        {featureItems?.data?.map((item: any) => {
                            return (
                                <div key={item.id} className="border-2 border-[#EBF3F8] rounded-[10px] shadow-3xl transition-all hover:shadow-4xl bg-bottom bg-contain bg-no-repeat cursor-pointer" style={{
                                    backgroundImage: `url(${item.bg})`,
                                }}>
                                    <div className="p-8 pb-10">
                                        <div className="pr-4 md:pr-7 w-full max-w-[581px]">
                                            <h3>{item.name}</h3>
                                            <p className="font-medium mt-4">{item.description}</p>
                                        </div>
                                        <div className="flex items-center justify-center mt-[30px]">
                                            <div>
                                                <Image
                                                    src={`${item.image}`}
                                                    alt={item.name}
                                                    width={200}
                                                    height={300}
                                                />
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                )}
            </div>
        </section>
    );
}
