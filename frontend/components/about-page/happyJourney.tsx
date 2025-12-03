/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState, useRef } from "react";
import Image from "next/image";
import fingerWhite from "../../public/images/finger-white.svg";
import { getFetchData } from "@/utils/getFetchData";

export default function HappyJourney() {
    const [happyJourneyData, setHappyJourneyData] = useState<any>(null);
    const [happyJourneyItemData, setHappyJourneyItemData] = useState<any[]>([]);
    const [fingerTop, setFingerTop] = useState(40);
    const containerRef = useRef<HTMLDivElement | null>(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const happyJourneyRes = await getFetchData("/about/happy-journey/", {
                    tag: "happy-journey-data",
                });
                const happyJourneyItemRes = await getFetchData("/about/happy-journey-item/", {
                    tag: "happy-journey-item-data",
                });

                setHappyJourneyData(happyJourneyRes?.data || null);
                setHappyJourneyItemData(happyJourneyItemRes?.data || []);
            } catch (error) {
                console.error("Failed to fetch happy journey data:", error);
            }
        };

        fetchData();
    }, []);

    useEffect(() => {
        const handleScroll = () => {
            const el = containerRef.current;
            if (!el) return;

            const rect = el.getBoundingClientRect();
            const containerHeight = rect.height;
            if (containerHeight <= 0) return;

            const scrolledInside = Math.min(
                Math.max(-rect.top, 0),
                containerHeight
            );

            const progress = scrolledInside / containerHeight;

            const baseTop = 40;
            const fingerApproxHeight = 80;
            const maxMove = Math.max(containerHeight - fingerApproxHeight - baseTop, 0);

            const newTop = baseTop + progress * maxMove;
            setFingerTop(newTop);
        };

        handleScroll();
        window.addEventListener("scroll", handleScroll, { passive: true });

        return () => window.removeEventListener("scroll", handleScroll);
    }, []);

    return (
        <section className="bg-blue py-12 md:py-[100px] rounded-[18px]">
            <div className="container">
                <div className="w-full max-w-[668px] mx-auto text-center mb-12 md:mb-[100px]">
                    <h2 className="text-white">{happyJourneyData?.title}</h2>
                </div>


                <div className="relative" ref={containerRef}>
                    {happyJourneyItemData?.map((item: any) => {
                        return (
                            <div
                                className="flex justify-center gap-5 sm:12 lg:gap-24"
                                key={item.id}
                            >

                                
                                <div className="w-[40%] sm:w-full max-w-[580px] pt-8 md:pt-[51px] pb-10 md:pb-20">
                                    <div
                                        className="flex items-center justify-end gap-4"
                                    >


                                        {/* <span className="absolute top-1/2 -translate-y-1/2 group-even:-left-9 sm:group-even:-left-[34px] lg:group-even:-left-[111px] group-odd:-right-9 sm:group-odd:-right-[34px] lg:group-odd:-right-[111px] content-[''] w-6 h-6 rounded-full bg-white z-10 "></span> */}


                                        <h3 className="text-white text-2xl sm:text-3xl md:text-4xl lg:text-5xl lg:leading-12">
                                            {item?.year}
                                        </h3>
                                        <div className="w-[130px] h-1 bg-white rounded-[18px]"></div>
                                    </div>
                                </div>

                                {/* <div className="w-2 flex items-center justify-center relative">
                                    <div className="absolute w-2 h-full bg-black group-last:rounded-b-[18px] group-first:rounded-t-[18px]"></div>
                                    <div className="absolute bottom-0 w-3 h-full bg-white group-last:rounded-b-[18px] group-first:rounded-t-[18px]"></div>
                                </div> */}

                                <div className="group-even:text-end w-[40%] sm:w-full max-w-[580px] pt-8 md:pt-[51px] pb-10 md:pb-20">
                                    <h3 className="text-white text-xl sm:text-3xl md:text-4xl lg:text-[40px] lg:leading-12">
                                        {item.title}
                                    </h3>
                                    <p className="text-sm sm:text-base sm:leading-6 font-medium font-dmsans text-white mt-4">
                                        {item.description}
                                    </p>
                                </div>


                            </div>
                        );
                    })}
                    <div
                        className="absolute left-1/2 -translate-x-1/2 w-full max-w-10 lg:max-w-[74px] h-auto flex items-center justify-center z-20"
                        style={{
                            top: fingerTop > 40 ? `${fingerTop + 150}px` : `${fingerTop}px`,
                        }}

                    >
                        <Image
                            src={fingerWhite}
                            alt="finger"
                            width={74}
                            height={98}
                            priority 
                            fetchPriority="high"
                        />
                    </div>
                </div>


            </div>
        </section>
    );
}
