"use client";

import Image from "next/image";
import { useState, useRef, useEffect } from "react";

type Data = {
    title_before_span?: string;
    title_span?: string;
    title_after_span?: string;
    description?: string;
    image?: string;
};

type Item = {
    id: number | string;
    image: string;
    title: string;
    description: string;
};

export default function OurProvenProcessSecurityClient({
    data,
    items,
}: {
    data: Data;
    items: Item[];
}) {
    const [isStatic, setIsStatic] = useState(false);
    const [activeIndex, setActiveIndex] = useState(0);
    const scrollContainerRef = useRef<HTMLDivElement | null>(null);

    const activeItem = items[activeIndex];

    useEffect(() => {
        const container = scrollContainerRef.current;

        if (!container) return;

        const handleScroll = () => {
            const scrollTop = container.scrollTop;
            const scrollHeight = container.scrollHeight;
            const clientHeight = container.clientHeight;

            if (scrollTop === 0) {
                setIsStatic(true)
            } else if (scrollTop + clientHeight >= scrollHeight) {
                setIsStatic(false)
            }
        };

        container.addEventListener("scroll", handleScroll);

        return () => {
            container.removeEventListener("scroll", handleScroll);
        };
    }, []);

    return (
        <div className={`${isStatic ? 'static' : 'relative'}`}>
            <div className="flex flex-col lg:flex-row justify-between gap-10">

                {/* LEFT SIDE */}
                <div className="w-full max-w-120 mx-auto lg:mx-0 text-center lg:text-start flex flex-col items-center lg:items-start justify-center">
                    <h2 className="mb-3 lg:mb-6">
                        {data?.title_before_span}{" "}
                        <span className="text-blue">{data?.title_span}</span>{" "}
                        {data?.title_after_span}
                    </h2>
                    <p className="mb-6 lg:mb-11">{data?.description}</p>

                    <div className="proven-icon-wrap max-w-120 lg:max-w-full relative">
                        {data?.image && activeItem && (
                            <>
                                <Image
                                    src={data.image}
                                    alt="Our Proven Security"
                                    width={345}
                                    height={345}
                                    className="circle"
                                    priority
                                />
                                <div className="bg-white rounded-full p-5 circle-icon w-full max-w-24 lg:max-w-37.25 absolute top-0 left-0">
                                    <Image
                                        src={activeItem.image}
                                        alt={activeItem.title}
                                        width={142}
                                        height={142}
                                        priority
                                    />
                                </div>
                            </>
                        )}
                    </div>
                </div>

                {/* RIGHT SIDE — INTERNAL SCROLL */}
                <div className="w-full max-w-111 mx-auto lg:mx-0 flex items-center">
                    <div
                        className="w-full overflow-y-auto scroll-width-hidden"
                        ref={scrollContainerRef}
                        style={{ maxHeight: "500px" }} // scroll height adjust করো
                    >
                        <div>
                            {items.map((item, index) => (
                                <div
                                    key={item.id}
                                    className="text-center lg:text-start flex flex-col items-center lg:items-start mb-4 lg:mb-8 last-of-type:mb-0"
                                    onMouseEnter={() => setActiveIndex(index)}
                                >
                                    <div className="mb-2 lg:mb-4.5 max-w-20 lg:max-w-full">
                                        <Image
                                            src={item.image}
                                            alt={item.title}
                                            width={100}
                                            height={106}
                                            priority
                                        />
                                    </div>
                                    <h3 className="mb-2 lg:mb-4">{item.title}</h3>
                                    <p>{item.description}</p>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>

            </div>
        </div>
    );
}
