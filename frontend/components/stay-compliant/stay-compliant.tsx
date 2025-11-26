// import { getFetchData } from "@/utils/getFetchData";
// import Image from "next/image";
// import Link from "next/link";

// export default async function StayCompliant() {
//     const stayCompliantData = await getFetchData('/configuration/stay-compliant/');
//     const data = stayCompliantData[0];
//     return (
//         <>
//             {data && (
//                 <section className="stay-compliant-section pb-12 md:pb-[100px]">
//                     <div className="container">
//                         <div
//                             className="bg-blue pl-6 sm:pl-12 md:pl-[83px] pr-6 sm:pr-12 md:pr-[90px] rounded-2xl flex flex-col lg:flex-row items-center ">
//                             <div className="w-full lg:max-w-[49.283%] xl:-mr-9 order-2 lg:order-1 mb-6 sm:mb-11 lg:mb-0">
//                                 {data?.title && (
//                                     <h2 className="text-white mb-6">{data?.title}</h2>
//                                 )}
//                                 {data?.description && (
//                                     <p className="text-white mb-8">{data?.description}</p>
//                                 )}
//                                 <div className="flex flex-wrap items-center gap-4">
//                                     <Link href="" className="btn-secondary group">Get started with us
//                                         <svg
//                                             className="transition-all duration-500 group-hover:rotate-45 w-5 md:w-6 h-5 md:h-6"
//                                             xmlns="http://www.w3.org/2000/svg"
//                                             fill="none"
//                                             viewBox="0 0 24 24"
//                                         >
//                                             <path
//                                                 stroke="currentColor"
//                                                 strokeLinecap="round"
//                                                 strokeLinejoin="round"
//                                                 strokeWidth={1.5}
//                                                 d="M6 18 18 6m0 0H9m9 0v9"
//                                             />
//                                         </svg>
//                                     </Link>
//                                     <Link href="/contact" className="btn-primary group border border-white">Contact us
//                                         <svg
//                                             className="transition-all duration-500 group-hover:rotate-45 w-5 md:w-6 h-5 md:h-6"
//                                             xmlns="http://www.w3.org/2000/svg"
//                                             fill="none"
//                                             viewBox="0 0 24 24"
//                                         >
//                                             <path
//                                                 stroke="currentColor"
//                                                 strokeLinecap="round"
//                                                 strokeLinejoin="round"
//                                                 strokeWidth={1.5}
//                                                 d="M6 18 18 6m0 0H9m9 0v9"
//                                             />
//                                         </svg>
//                                     </Link>
//                                 </div>
//                             </div>
//                             <div className="w-full lg:max-w-[53.664%] mt-6 sm:mt-11 mb-8 sm:mb-16 lg:mb-[124px] order-1 lg:order-2">
//                                 {data?.image && (
//                                     <Image
//                                         src={data?.image}
//                                         alt="stay compliant"
//                                         width={640}
//                                         height={485}
//                                     />
//                                 )}
//                             </div>
//                         </div>
//                     </div>
//                 </section>
//             )}
//         </>
//     );
// }

/* eslint-disable @typescript-eslint/no-explicit-any */
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";
import ComplianceBg from "../../public/images/compliance-bg.svg";

export default async function Compliance() {
    const complianceTitleData = await getFetchData('/configuration/compliance-title/');
    const complianceItemData = await getFetchData('/configuration/compliance-item/');

    const title = complianceTitleData?.data || [];  
    const items = Array.isArray(complianceItemData?.data) ? complianceItemData.data : [];

    return (
        <section
            className="py-12 md:py-[100px] bg-contain bg-bottom-right bg-no-repeat"
            style={{ backgroundImage: `url(${ComplianceBg.src})` }}
        >
            <div className="container">

                {title.length > 0 && (
                    <div className="flex flex-col sm:flex-row justify-between mb-10 md:mb-20 gap-5">
                        <h2 className="sm:max-w-[636px] w-full">
                            {title[0]?.title_before_span}
                            <span className="text-[#2E78AC]">{title[0]?.title_span}</span>
                            {title[0]?.title_after_span}
                        </h2>

                        <div className="flex items-center justify-center sm:justify-end">
                            <Link href={title[0]?.btn_url || ""} className="btn-primary group">
                                {title[0]?.btn_name}
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

                <div className="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                    {items.map((item: any) => (
                        <div
                            key={item.id}
                            className="p-4 md:p-8 bg-white border border-[#E6E7EB] rounded-[10px] transition-all hover:shadow-[25px_36px_18px_rgba(0,0,0,0.01),14px_20px_15px_rgba(0,0,0,0.05),6px_9px_11px_rgba(0,0,0,0.09),2px_2px_6px_rgba(0,0,0,0.1)] cursor-pointer"
                        >
                            {item?.image && (
                                <Image src={item.image} alt={item.title} width={60} height={66} />
                            )}
                            <h4 className="mt-4">{item.title}</h4>

                            {Array.isArray(item.item_list) && (
                                <ul className="protection-list mt-4">
                                    {item.item_list.map((i: any) => (
                                        <li key={i.id}>{i.name}</li>
                                    ))}
                                </ul>
                            )}
                        </div>
                    ))}
                </div>

            </div>
        </section>
    );
}
