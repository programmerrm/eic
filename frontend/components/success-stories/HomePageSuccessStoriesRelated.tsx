/* eslint-disable @typescript-eslint/no-explicit-any */
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";

export default async function HomePageSuccessStoriesRelated() {
    const successStoriesItem = await getFetchData('/success-stories/list/');
    if (!successStoriesItem?.results?.data) {
        return null;
    }

    return (
        <section className="-mb-[113px] -mt-9 md:-mt-[120px] pt-12 sm:pt-0">
            <div className="container">
                <h2 className="max-w-[393px] w-full mx-auto text-center">Case studies & <span className="text-blue">success</span> stories</h2>
                <div className="grid sm:grid-cols-2 gap-6 my-6 sm:my-12">
                    {successStoriesItem?.results?.data && (
                        <>
                            {successStoriesItem?.results?.data?.slice(0, 2)?.map((item: any) => {
                                return (
                                    <div key={item.id}>
                                        <Link className="mb-3 sm:mb-6 block" href={`/case-studies/${item.slug}`}>
                                            {item.image && (
                                                <Image
                                                    src={item.image}
                                                    alt={item.title}
                                                    width={668}
                                                    height={516}
                                                    className="transition-transform duration-500 ease-in-out hover:scale-105"
                                                    priority 
                                                    fetchPriority="high"
                                                />
                                            )}
                                        </Link>
                                        <span className="block">{item.budget_description}</span>
                                        <h3 className="mt-1 sm:mt-2 transition-all hover:text-blue">
                                            <Link href={`/case-studies/${item.slug}`}>
                                                {item.title}
                                            </Link>
                                        </h3>
                                    </div>
                                );
                            })}
                        </>
                    )}
                </div>
                <div className="flex items-center justify-center">
                    <Link href="/case-studies" className="btn-primary group">Explore More
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
        </section>
    );
}
