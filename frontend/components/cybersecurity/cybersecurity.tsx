import { MEDIA_URL } from "@/utils/api";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import CybersecurityCounters from "../progressbar/CybersecurityCounters";

export default async function Cybersecurity() {
    const cybersecuritySolutionTitle = await getFetchData('/homepage/cyber-security-solution-title/', {
        tag: "cyber-security-solution-title-data",
    });
    const cybersecuritySolutionItems = await getFetchData('/homepage/cyber-security-solution-items/', {
        tag: "cyber-security-solution-items-data",
    });
    return (
        <section className="bg-blue pt-12 md:pt-[100px] pb-11 md:pb-[90px]">
            <div className="container">
                <div className="grid lg:grid-cols-2 items-center gap-8 md:gap-14 text-white">
                    <div className="order-2 lg:order-1">
                        <div className="mb-10 md:mb-[114px]">
                            <h2 className="text-white max-w-[602px] mb-4 md:mb-6">{cybersecuritySolutionTitle?.data?.title}</h2>
                            <p className="text-base sm:text-lg md:text-2xl md:leading-8 font-normal font-spacegrotesk">{cybersecuritySolutionTitle?.data?.description}</p>
                        </div>
                        <CybersecurityCounters items={cybersecuritySolutionItems || []} />
                    </div>
                    <div className="order-1 lg:order-2">
                        <div>
                            {cybersecuritySolutionTitle?.data?.image && (
                                <Image
                                src={`${MEDIA_URL}${cybersecuritySolutionTitle?.data?.image}`}
                                alt="syber security"
                                width={762}
                                height={762}
                            />
                            )}
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
}
