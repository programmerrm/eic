"use client";

import { useEffect, useRef } from "react";
import Image from "next/image";
import SwiperCore from "swiper";
import Swiper from "swiper/bundle";
import "swiper/css/bundle";
import sliderIcon from "../../public/images/slider-icon.svg";

type ReviewItem = {
    id: number;
    author_image: string;
    author_name: string;
    author_bio: string;
    content: string;
};

type Props = {
    items: ReviewItem[];
};

export default function ReviewSlider({ items }: Props) {
    const swiperInstance = useRef<SwiperCore | null>(null);

    useEffect(() => {
        if (!items.length) return;
        if (swiperInstance.current) return;

        swiperInstance.current = new Swiper(".mySwiper", {
            slidesPerView: 2.5,
            spaceBetween: 36,
            centeredSlides: true,
            loop: true,
            grabCursor: true,
            slideToClickedSlide: true,

            navigation: {
                nextEl: ".custom-next",
                prevEl: ".custom-prev",
            },

            breakpoints: {
                1024: { slidesPerView: 2.5 },
                768: { slidesPerView: 1.5 },
                0: { slidesPerView: 1.1 },
            },
        });

        return () => {
            if (swiperInstance.current) {
                swiperInstance.current.destroy(true, true);
                swiperInstance.current = null;
            }
        };
    }, [items]);

    if (!items.length) return null;

    return (
        <div className="swiper mySwiper">
            <div className="swiper-wrapper">
                {items.map((item) => (
                    <div className="swiper-slide" key={item.id}>
                        <div className="slide-content flex flex-col gap-6 items-start bg-white border border-[#C0D9EB] rounded-2xl px-4 md:px-8 py-5 md:py-11">
                            <div className="flex flex-col sm:flex-row items-center gap-8">
                                <div className="max-w-28 md:max-w-[173px] w-full p-5 md:p-10 bg-blue flex items-center justify-center text-blue">
                                    <Image
                                        src={item.author_image}
                                        alt={item.author_name}
                                        width={97}
                                        height={97}
                                        priority 
                                        fetchPriority="high"
                                    />
                                </div>
                                <p className="text-body text-lg sm:text-xl md:text-2xl md:leading-8 text-center sm:text-start">
                                    {item.content}
                                </p>
                            </div>

                            <div className="content w-full flex flex-col sm:flex-row gap-5 sm:gap-12 md:gap-[90px] mt-4 sm:mt-8 md:mt-14">
                                <div className="max-w-16 md:max-w-24 mx-auto md:mx-0 flex items-center justify-center w-full">
                                    <Image
                                        src={sliderIcon}
                                        alt="icon"
                                        width={95}
                                        height={76}
                                        priority 
                                        fetchPriority="high"
                                    />
                                </div>
                                <div className="text-center sm:text-start">
                                    <h4 className="sm:text-start leading-8">
                                        {item.author_name}
                                    </h4>
                                    <p>{item.author_bio}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                ))}
            </div>


            <div className="swiper-btn-wrap -mt-8 md:mt-0">
                <div className="swiper-button-next custom-next">

                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="16" fill="none" viewBox="0 0 19 16">
                        <g clipPath="url(#a)">
                            <g clipPath="url(#b)">
                                <g
                                    stroke="currentColor"
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    strokeWidth={1.5}
                                    clipPath="url(#c)"
                                >
                                    <path d="M18.061 8H1M8 1 1 8l7 7" />
                                </g>
                            </g>
                        </g>
                        <defs>
                            <clipPath id="a">
                                <path fill="currentColor" d="M0 0h19v16H0z" />
                            </clipPath>
                            <clipPath id="b">
                                <path fill="currentColor" d="M0 0h19v16H0z" />
                            </clipPath>
                            <clipPath id="c">
                                <path fill="currentColor" d="M0 0h19v16H0z" />
                            </clipPath>
                        </defs>
                    </svg>
                </div>

                <div className="swiper-button-prev custom-prev">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="16" fill="none" viewBox="0 0 20 16">
                        <g clipPath="url(#a)">
                            <g clipPath="url(#b)">
                                <g
                                    stroke="currentColor"
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    strokeWidth={1.5}
                                    clipPath="url(#c)"
                                >
                                    <path d="M1.408 8H18.47M11.469 1l7 7-7 7" />
                                </g>
                            </g>
                        </g>
                        <defs>
                            <clipPath id="a">
                                <path fill="currentColor" d="M0 0h20v16H0z" />
                            </clipPath>
                            <clipPath id="b">
                                <path fill="currentColor" d="M0 0h20v16H0z" />
                            </clipPath>
                            <clipPath id="c">
                                <path fill="currentColor" d="M0 0h20v16H0z" />
                            </clipPath>
                        </defs>
                    </svg>
                </div>
            </div>
        </div>
    );
}
