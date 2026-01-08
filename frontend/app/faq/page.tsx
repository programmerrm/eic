import FAQ from "@/components/FAQ/FAQ";
import BannerImg from "../../public/images/banner-img.svg";
import StayCompliant from "@/components/stay-compliant/stay-compliant";
import { MEDIA_URL } from "@/utils/api";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";

export default async function Faq() {
    const topBarData = await getFetchData("/faq/top-bar/");
    const faqSection = await getFetchData('/faq/section/');
    const faqItems = await getFetchData('/faq/item-list/');
    const schemaData = await getFetchData('/faq/schema/');
    const jsonLd = schemaData?.data?.json_ld ? JSON.parse(schemaData.data.json_ld) : null;

    return (
        <>
            {jsonLd && (
                <script
                    type="application/ld+json"
                    dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
                />
            )}
            <section className="mt-24 md:mt-36 banner-section bg-blue [clip-path:polygon(0_0,100%_0,100%_calc(100%-50px),calc(100%-60px)_100%,0_100%)] md:[clip-path:polygon(0_0,100%_0,100%_calc(100%-100px),calc(100%-150px)_100%,0_100%)]">
                <div className="container">
                    <div className="bg-bottom bg-contain bg-no-repeat" style={{
                        backgroundImage: `url(${BannerImg.src})`,
                    }}>
                        <div className="max-w-[740px] mx-auto py-10 sm:py-20 md:py-40 lg:py-[232px] text-white text-center ">
                            {topBarData?.data?.title && (
                                <h1 className="uppercase">{topBarData?.data?.title}</h1>
                            )}
                            {topBarData?.data?.description && (
                                <p className="text-base sm:text-lg md:text-2xl md:leading-8 font-bold font-spacegrotesk mt-2 sm:mt-4 w-full max-w-[626px] mx-auto">{topBarData?.data?.description}</p>
                            )}
                        </div>
                    </div>
                </div>
            </section>
            <section className="py-12 md:py-[100px] ">
                <div className="container">
                    <h2 className="w-full max-w-[458px] mx-auto lg:mx-0 text-center lg:text-start"><span className="text-blue">FAQs</span> {faqSection?.data?.title}</h2>
                    <div className="flex flex-col lg:flex-row items-center ">
                        <div className="w-full lg:max-w-[60.955%] order-2 lg:order-1">

                            <div className="w-full max-w-[696px] space-y-4 mt-10 md:mt-20">
                                <FAQ faqItems={faqItems?.data || []} />
                            </div>

                        </div>
                        <div className="w-full lg:max-w-[calc(100%-60.955%)] order-1 lg:order-2">
                            {faqSection?.data?.image && (
                                <Image
                                    src={`${MEDIA_URL}${faqSection?.data?.image}`}
                                    alt="faq"
                                    width={515}
                                    height={482}
                                    priority 
                                    fetchPriority="high"
                                />
                            )}
                        </div>
                    </div>
                </div>
            </section>
            <StayCompliant />
        </>
    );
}
