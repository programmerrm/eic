/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState, useRef } from "react";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import fingerWhite from "../../public/images/finger-white.svg";

export default function HappyJourney() {
    const [happyJourneyData, setHappyJourneyData] = useState<any>(null);
    const [happyJourneyItemData, setHappyJourneyItemData] = useState<any[]>([]);
    const containerRef = useRef<HTMLDivElement | null>(null);
    const bulletRefs = useRef<(HTMLSpanElement | null)[]>([]);

    const [fillPercent, setFillPercent] = useState(100);
    const [bulletWhiteStates, setBulletWhiteStates] = useState<boolean[]>([]);

    // data fetch
    useEffect(() => {
        const fetchData = async () => {
            try {
                const happyJourneyRes = await getFetchData("/about/happy-journey/", {
                    tag: "happy-journey-data",
                });
                const happyJourneyItemRes = await getFetchData(
                    "/about/happy-journey-item/",
                    { tag: "happy-journey-item-data" }
                );

                setHappyJourneyData(happyJourneyRes?.data || null);
                setHappyJourneyItemData(happyJourneyItemRes?.data || []);
            } catch (error) {
                console.error("Failed to fetch happy journey data:", error);
            }
        };
        fetchData();
    }, []);

    // scroll logic
    useEffect(() => {
        const handleScroll = () => {
            const el = containerRef.current;
            if (!el) return;

            const rect = el.getBoundingClientRect();
            const windowHeight =
                window.innerHeight || document.documentElement.clientHeight;

            const totalScrollable = rect.height + windowHeight;
            const scrolled = windowHeight - rect.top;

            let progress = scrolled / totalScrollable; // 0–1
            progress = Math.min(Math.max(progress, 0), 1);

            let fill = 100 - progress * 100; // নিচ থেকে সাদা অংশের %
            fill = Math.max(0, Math.min(100, fill));
            setFillPercent(fill);

            // bullet position অনুযায়ী color ঠিক করা
            const containerHeight = rect.height;
            const whiteHeightPx = (fill / 100) * containerHeight;

            const newStates: boolean[] = [];

            bulletRefs.current.forEach((bulletEl, idx) => {
                if (!bulletEl) {
                    newStates[idx] = false;
                    return;
                }

                const bRect = bulletEl.getBoundingClientRect();
                const bulletCenterY = bRect.top + bRect.height / 2;
                const containerBottom = rect.bottom;

                const distanceFromBottomPx = containerBottom - bulletCenterY;

                newStates[idx] = distanceFromBottomPx <= whiteHeightPx;
            });

            setBulletWhiteStates(newStates);
        };

        handleScroll();
        window.addEventListener("scroll", handleScroll);
        window.addEventListener("resize", handleScroll);

        return () => {
            window.removeEventListener("scroll", handleScroll);
            window.removeEventListener("resize", handleScroll);
        };
    }, [happyJourneyItemData.length]);

    const itemCount = happyJourneyItemData.length;

    return (
        <section className="bg-blue py-12 md:py-[100px] rounded-[18px]">
            <div className="container">
                <div className="w-full max-w-[668px] mx-auto text-center mb-12 md:mb-[100px]">
                    <h2 className="text-white">{happyJourneyData?.title}</h2>
                </div>

                <div className="relative h-auto" ref={containerRef}>
                    {happyJourneyItemData?.map((item: any, index: number) => {
                        const isLast = index === itemCount - 1;
                        const isEven = index % 2 === 0;

                        const bulletBaseClasses =
                            "absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 " +
                            "w-6 h-6 rounded-full z-20";

                        const isWhite = bulletWhiteStates[index] ?? false;
                        const bulletColorClass = isWhite ? "bg-white" : "bg-black";

                        return (
                            <div
                                className="relative grid grid-cols-2 gap-5 sm:gap-12 lg:gap-48"
                                key={item.id}
                            >
                                {isEven ? (
                                    <>
                                        {/* LEFT: Year */}
                                        <div className="pt-8 md:pt-[51px] pb-10 md:pb-20">
                                            <div className="flex items-center justify-end gap-4">
                                                <h3 className="text-white text-2xl sm:text-3xl md:text-4xl lg:text-5xl lg:leading-12">
                                                    {item?.year}
                                                </h3>
                                                <div className="w-[130px] h-1 bg-white rounded-[18px]" />
                                            </div>
                                        </div>

                                        {/* RIGHT: Content */}
                                        <div className="pt-8 md:pt-[51px] pb-10 md:pb-20">
                                            <h3 className="text-white text-xl sm:text-3xl md:text-4xl lg:text-[40px] lg:leading-12">
                                                {item.title}
                                            </h3>
                                            <p className="text-sm sm:text-base sm:leading-6 font-medium font-dmsans text-white mt-4">
                                                {item.description}
                                            </p>
                                        </div>
                                    </>
                                ) : (
                                    <>
                                        {/* LEFT: Content */}
                                        <div className="pt-8 md:pt-[51px] pb-10 md:pb-20 text-right">
                                            <h3 className="text-white text-xl sm:text-3xl md:text-4xl lg:text-[40px] lg:leading-12">
                                                {item.title}
                                            </h3>
                                            <p className="text-sm sm:text-base sm:leading-6 font-medium font-dmsans text-white mt-4">
                                                {item.description}
                                            </p>
                                        </div>

                                        {/* RIGHT: Year */}
                                        <div className="pt-8 md:pt-[51px] pb-10 md:pb-20">
                                            <div className="flex items-center justify-start gap-4">
                                                <div className="w-[130px] h-1 bg-white rounded-[18px]" />
                                                <h3 className="text-white text-2xl sm:text-3xl md:text-4xl lg:text-5xl lg:leading-12">
                                                    {item?.year}
                                                </h3>
                                            </div>
                                        </div>
                                    </>
                                )}

                                {!isLast && (
                                    <span
                                        ref={(el) => {
                                            bulletRefs.current[index] = el;
                                        }}
                                        className={`${bulletBaseClasses} ${bulletColorClass}`}
                                    />
                                )}
                            </div>
                        );
                    })}

                    {/* Timeline line */}
                    <div className="absolute top-0 left-1/2 -translate-x-1/2 w-3 h-full bg-black rounded-full overflow-hidden">
                        <div
                            className="absolute left-0 w-full bg-white rounded-full transition-all duration-300 ease-out"
                            style={{
                                bottom: 0,
                                height: `${fillPercent}%`,
                                opacity: fillPercent > 0 ? 1 : 0,
                            }}
                        />
                    </div>

                    {/* Finger image */}
                    <div
                        className="pointer-events-none absolute left-1/2 -translate-x-1/2 translate-y-1/2 flex items-center justify-center z-20"
                        style={{
                            bottom: `${fillPercent}%`,
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
