import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";

export default async function GloballyAccredited() {
    const globallyAccredited = await getFetchData('/homepage/globally-accredited/', {
        tag: "globally-accredited-data",
    })

    if (!globallyAccredited?.data) {
        return null;
    }

    return (
        <section className="pt-[213px] pb-[134px] bg-right bg-contain bg-no-repeat"
            style={{
                backgroundImage: `url(${globallyAccredited?.data?.bg})`,
            }}>
            <div className="container">
                <div
                    className="bg-[#EBF3F8] px-6 md:px-12 lg:px-[100px] py-6 md:py-[42px] rounded-2xl flex flex-col sm:flex-row items-center justify-center sm:justify-between gap-5">
                    <div className="sm:max-w-[660px] w-full flex flex-col items-center sm:items-start order-2 sm:order-1">
                        <h2 className="text-2xl sm:text-3xl md:text-4xl lg:text-5xl lg:leading-14 mb-4 md:mb-8 text-center sm:text-start">{globallyAccredited?.data?.title}</h2>
                        <Link href="/contact" className="btn-primary group inline-flex">Contact US
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
                    <div className="sm:max-w-[338px] w-full flex items-center justify-center order-1 sm:order-2">
                        {globallyAccredited?.data?.image && (
                            <Image
                                src={globallyAccredited?.data?.image}
                                alt="Globally Accredited"
                                width={338}
                                height={334}
                                priority 
                                fetchPriority="high"
                            />
                        )}
                    </div>
                </div>
            </div>
        </section>
    );
}
