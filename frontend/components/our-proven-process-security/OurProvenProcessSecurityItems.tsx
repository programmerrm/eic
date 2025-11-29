"use client";

import Image from "next/image";
import { useEffect, useRef, useState } from "react";

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
    const wrapperRef = useRef<HTMLDivElement | null>(null);
    const viewportRef = useRef<HTMLDivElement | null>(null);
    const itemsRef = useRef<HTMLDivElement | null>(null);

    const [translate, setTranslate] = useState(0);
    const [maxTranslate, setMaxTranslate] = useState(0);
    const [wrapperMinHeight, setWrapperMinHeight] = useState(600);
    const [viewportHeight, setViewportHeight] = useState(260);
    const [itemOffsets, setItemOffsets] = useState<number[]>([]);
    const [activeIndex, setActiveIndex] = useState(0);

    const stickyHeight = 600;

    useEffect(() => {
        const calcHeights = () => {
            const itemsEl = itemsRef.current;
            if (!itemsEl) return;

            const children = itemsEl.children;
            let desiredVH = 260;

            if (children.length >= 2) {
                const firstRect = (children[0] as HTMLElement).getBoundingClientRect();
                const secondRect = (children[1] as HTMLElement).getBoundingClientRect();
                desiredVH = firstRect.height + secondRect.height;
            } else if (children.length === 1) {
                const firstRect = (children[0] as HTMLElement).getBoundingClientRect();
                desiredVH = firstRect.height;
            }

            setViewportHeight(desiredVH);

            const itemsHeight = itemsEl.getBoundingClientRect().height;
            const diff = Math.max(0, itemsHeight - desiredVH);

            setMaxTranslate(diff);
            setWrapperMinHeight(stickyHeight + diff);

            const baseTop = itemsEl.getBoundingClientRect().top;
            const offsets: number[] = [];
            Array.from(children).forEach((child) => {
                const rect = (child as HTMLElement).getBoundingClientRect();
                offsets.push(rect.top - baseTop);
            });
            setItemOffsets(offsets);
        };

        calcHeights();
        window.addEventListener("resize", calcHeights);
        return () => window.removeEventListener("resize", calcHeights);
    }, [items.length]);

    useEffect(() => {
        const handleScroll = () => {
            const wrapper = wrapperRef.current;
            if (!wrapper) return;

            const rect = wrapper.getBoundingClientRect();
            const wrapperTop = window.scrollY + rect.top;

            const currentScroll = window.scrollY;
            const rawProgress = currentScroll - wrapperTop;

            let clamped = rawProgress;
            if (clamped <= 0) clamped = 0;
            else if (clamped >= maxTranslate) clamped = maxTranslate;

            setTranslate(clamped);

            if (itemOffsets.length > 0) {
                const centerY = clamped + viewportHeight / 2;
                let idx = 0;
                for (let i = 0; i < itemOffsets.length; i++) {
                    const start = itemOffsets[i];
                    const end =
                        i < itemOffsets.length - 1
                            ? itemOffsets[i + 1]
                            : Number.POSITIVE_INFINITY;
                    if (centerY >= start && centerY < end) {
                        idx = i;
                        break;
                    }
                }
                setActiveIndex(idx);
            }
        };

        handleScroll();

        window.addEventListener("scroll", handleScroll, { passive: true });
        return () => window.removeEventListener("scroll", handleScroll);
    }, [maxTranslate, viewportHeight, itemOffsets]);

    const activeItem = items[activeIndex];

    return (
        <div
            ref={wrapperRef}
            style={{ minHeight: wrapperMinHeight }}
            className="relative"
        >
            <div className="sticky top-24 h-[600px] flex flex-col lg:flex-row justify-between gap-10">
                {/* LEFT SIDE */}
                <div className="w-full max-w-[480px] mx-auto lg:mx-0 text-center lg:text-start flex flex-col items-center lg:items-start justify-center">
                    <h2 className="mb-3 lg:mb-6">
                        {data?.title_before_span}{" "}
                        <span className="text-blue">{data?.title_span}</span>{" "}
                        {data?.title_after_span}
                    </h2>
                    <p className="mb-6 lg:mb-11">{data?.description}</p>

                    <div className="proven-icon-wrap max-w-[200px] lg:max-w-full relative">
                        {data?.image && (
                            <>
                                <Image
                                    src={data.image}
                                    alt="Our Proven Security"
                                    width={345}
                                    height={345}
                                    className="circle"
                                />
                                {activeItem && (
                                    <div className="bg-white rounded-full p-5 circle-icon w-full max-w-24 lg:max-w-[149px] absolute top-0 left-0">
                                        <Image
                                            src={activeItem.image}
                                            alt={activeItem.title}
                                            width={142}
                                            height={142}
                                            className=""
                                        />
                                    </div>
                                )}
                            </>
                        )}
                    </div>
                </div>
                {/* RIGHT SIDE */}
                <div className="w-full max-w-[444px] mx-auto lg:mx-0 h-full flex items-center">
                    <div
                        ref={viewportRef}
                        className="w-full overflow-hidden"
                        style={{ height: viewportHeight }}
                    >
                        <div
                            ref={itemsRef}
                            style={{
                                transform: `translateY(-${translate}px)`,
                                transition: "transform 0.08s linear",
                            }}
                        >
                            {items?.map((item) => (
                                <div
                                    key={item.id}
                                    className="
                                        text-center lg:text-start
                                        flex flex-col items-center lg:items-start
                                        mb-4 lg:mb-8 last-of-type:mb-0
                                    "
                                >
                                    <div className="mb-2 lg:mb-[18px] max-w-20 lg:max-w-full">
                                        <Image
                                            src={item.image}
                                            alt={item.title}
                                            width={100}
                                            height={106}
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
