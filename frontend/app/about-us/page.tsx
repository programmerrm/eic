/* eslint-disable @typescript-eslint/no-explicit-any */
import SectionBanner from "@/components/banner/section-banner";
import AboutSecurity from "@/components/security-firm/about-security";
import StayCompliant from "@/components/stay-compliant/stay-compliant";
import { getFetchData } from "@/utils/getFetchData";
import GlobalBGImg from "../../public/images/world-map.svg";
import Image from "next/image";
import HappyJourney from "@/components/about-page/happyJourney";
import Core from "./core";

export default async function Page() {
    const topBarFetchData = await getFetchData('/about/top-bar/');
    const digitalSecuritySolutionTopBarData = await getFetchData('/about/digital-security-solution-top-bar/')
    const digitalSecuritySolutionItemData = await getFetchData('/about/digital-security-solution-item/');
    const secureFutureTopBarData = await getFetchData('/about/secure-future-top-bar/')
    const secureFutureItemData = await getFetchData('/about/secure-future-item/')

    return (
        <main>
            <SectionBanner topBarData={topBarFetchData?.data} />
            <AboutSecurity />
            <HappyJourney />

            <section className=" py-12 md:py-[100px]">
                <div className="container">
                    <h2 className="text-center">{secureFutureTopBarData?.data?.normal_title} <span className="text-blue">{secureFutureTopBarData?.data?.title_span}</span></h2>
                    <div className="mt-8 sm:mt-[60px]">
                        {secureFutureItemData?.data?.map((item: any) => {
                            return (
                                <div
                                    className="flex flex-col lg:flex-row items-center border-t border-[#EDF4F9] py-5 sm:py-10  last-of-type:border-b" key={item.id}>
                                    <div className="w-full max-w-full lg:max-w-[calc(100%-56.770%)] text-center lg:text-start mb-4 lg:mb-0">
                                        <h3>{item.title}</h3>
                                    </div>
                                    <div
                                        className="w-full max-w-full lg:max-w-[56.770%] flex flex-col sm:flex-row text-center sm:text-start items-center gap-5 md:gap-10 lg:gap-14">
                                        <div className="w-full max-w-40">
                                            {item.image && (
                                                <Image
                                                src={item.image}
                                                alt={item.title}
                                                width={160}
                                                height={100}
                                            />
                                            )}
                                        </div>
                                        <p className="text-sm md:text-base leading-[26px] font-poppins font-normal text-center sm:text-left">{item.description}</p>
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                </div>
            </section>

            <section className="pt-12 md:pt-[100px] bg-blue text-white">
                <div className="container">
                    <div className="pb-12 md:pb-[100px] bg-center md:bg-bottom bg-contain bg-no-repeat"
                        style={{
                            backgroundImage: `url(${GlobalBGImg.src})`,
                        }}>
                        <div
                            className="flex flex-col lg:flex-row text-center lg:text-start items-center lg:items-start justify-between gap-5">
                            <h2 className="text-white w-full max-w-3xl">{digitalSecuritySolutionTopBarData?.data?.title}</h2>
                            <p className="w-full max-w-[480px] text-base sm:text-xl md:text-2xl font-normal font-spacegrotesk md:leading-8">{digitalSecuritySolutionTopBarData?.data?.description}</p>
                        </div>
                        <div className="pt-12 md:pt-[100px] grid grid-cols-2 md:grid-cols-4 gap-8 lg:gap-16 xl:gap-[74px]">
                            {digitalSecuritySolutionItemData?.data?.map((item: any) => {
                                return (
                                    <div className="items-info" key={item.id}>
                                        <span
                                            className="text-2xl sm:text-3xl md:text-[40px] md:leading-[72px] font-bold font-spacegrotesk tracking-[-2%] mb-3 inline-block">{item.count}</span>
                                        <h3 className="text-lg md:text-xl lg:text-2xl text-white mb-2">{item.title}</h3>
                                        <p>{item.description}</p>
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                </div>
            </section>

            <Core />

            <StayCompliant />
        </main>
    );
}
