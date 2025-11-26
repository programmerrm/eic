/* eslint-disable @typescript-eslint/no-explicit-any */
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";
import ComplianceBg from "../../public/images/compliance-bg.svg";

export default async function Compliance() {
    const complianceTitleData = await getFetchData('/configuration/compliance-title/');
    const complianceItemData = await getFetchData('/configuration/compliance-item/');
    return (
        <section className="py-12 md:py-[100px] bg-contain bg-bottom-right bg-no-repeat"
            style={{
                backgroundImage: `url(${ComplianceBg.src})`,
            }}>
            <div className="container">
                {complianceTitleData && (
                    <div className="flex flex-col sm:flex-row justify-between mb-10 md:mb-20 gap-5">
                        <h2 className="sm:max-w-[636px] w-full">{complianceTitleData[0]?.title_before_span} <span className="text-[#2E78AC]">{complianceTitleData[0]?.title_span}</span>
                            {complianceTitleData[0]?.title_after_span}</h2>
                        <div className="flex items-center justify-center sm:justify-end">
                            <Link href={complianceTitleData[0]?.btn_url || ""} className="btn-primary group">{complianceTitleData[0]?.btn_name}
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
                {complianceItemData && (
                    <div className="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                        {complianceItemData?.map((item: any) => {
                            return (
                                <div
                                    className="p-4 md:p-8 bg-white border border-[#E6E7EB] rounded-[10px] transition-all hover:shadow-[25px_36px_18px_rgba(0,0,0,0.01),14px_20px_15px_rgba(0,0,0,0.05),6px_9px_11px_rgba(0,0,0,0.09),2px_2px_6px_rgba(0,0,0,0.1)] cursor-pointer" key={item.id}>
                                    <div className="max-w-10 md:max-w-[60px] w-full">
                                        {item?.image && (
                                            <Image
                                                src={item?.image}
                                                alt={item?.title}
                                                width={60}
                                                height={66}
                                            />
                                        )}
                                    </div>
                                    {item?.title && (
                                        <h4 className="mt-4">{item?.title}</h4>
                                    )}
                                    {item?.item_list && (
                                        <ul className="protection-list mt-4">
                                            {item?.item_list.map((i: any) => {
                                                return (
                                                    <li key={i.id}>{i.name}</li>
                                                );
                                            })}
                                        </ul>
                                    )}
                                </div>
                            );
                        })}
                    </div>
                )}
            </div>
        </section>
    );
}
