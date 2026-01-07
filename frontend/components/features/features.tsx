/* eslint-disable @typescript-eslint/no-explicit-any */
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";

export default async function Features() {
    const featureTitleRes = await getFetchData('/feature/title/', {
        tag: "feature-title-data",
    });
    const featureItemsRes = await getFetchData('/feature/items/', {
        tag: "feature/items-data",
    });
    const featureTitle = featureTitleRes?.data || null;
    const featureItems = Array.isArray(featureItemsRes?.data) ? featureItemsRes.data : [];
    return (
        <section className="py-6 md:py-12 lg:py-25">
            <div className="container">
                {featureTitle && (
                    <div className="flex flex-col sm:flex-row justify-between mb-10 gap-5">
                        <h2 className="w-full max-w-210.5">{featureTitle?.title_before_span} <span className="text-[#2E78AC]">{featureTitle?.title_span} </span>{featureTitle?.title_after_span}</h2>
                        <div className="flex items-center w-fit justify-center sm:justify-end min-w-[212px]">
                            <Link
                                href={featureTitle?.features_btn_url || ""}
                                className="btn-primary group"
                            >
                                {featureTitle?.features_btn_name}
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
                <div className="flex flex-col flex-wrap pb-10 md:pb-16">
                    <h3>More Than Compliance - Our <span className="text-[#2E78AC]">Unique</span> Commitments</h3>
                </div>
                <div className="grid md:grid-cols-2 gap-6">
                    {featureItems.map((item: any) => (
                        <div
                            key={item.id}
                            className="border-2 border-[#EBF3F8] rounded-[10px] shadow-3xl transition-all hover:shadow-4xl bg-bottom bg-contain bg-no-repeat"
                            style={{
                                backgroundImage: `url(${item.bg || ""})`,
                            }}
                        >
                            <div className="flex flex-col justify-between h-full p-8 pb-10">
                                <div className="pr-4 md:pr-7 w-full max-w-[581px] text-center sm:text-start">
                                    <h3>{item.name}</h3>
                                    <p className="font-medium mt-4">{item.description}</p>
                                </div>
                                <div className="flex items-center justify-center mt-[30px]">
                                    <Image
                                        src={item.image}
                                        alt={item.name}
                                        width={200}
                                        height={300}
                                        priority
                                        fetchPriority="high"
                                    />
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
}
