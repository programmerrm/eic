/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable react-hooks/exhaustive-deps */
"use client";
import { useEffect, useRef, useState } from "react";

export default function Progressbar({ response, compliance, security }: any) {
    const ref = useRef(null);
    const [inView, setInView] = useState(false);

    useEffect(() => {
        const observer = new IntersectionObserver(
            ([entry]) => {
                if (entry.isIntersecting) setInView(true);
            },
            { threshold: 0.5 }
        );

        if (ref.current) observer.observe(ref.current);

        return () => {
            if (ref.current) observer.unobserve(ref.current);
        };
    }, []);

    return (
        <div
            ref={ref}
            className="w-full max-w-[708px] bg-body text-white py-8 xl:py-16 pr-[62px] pl-8 xl:pl-16 
            [clip-path:polygon(0_0,100%_0,100%_calc(100%-50px),calc(100%-40px)_100%,0_100%)] 
            lg:[clip-path:polygon(0_0,100%_0,100%_calc(100%-80px),calc(100%-56px)_100%,0_100%)] flex flex-col relative"
        >
            <div className="w-full max-w-[708px] chart relative">
                <div className="flex flex-col gap-6">
                    <div className="flex items-center text-white">
                        <p className="w-full max-w-20 xl:max-w-[116px]">Response</p>
                        <div className="relative h-16 lg:h-20 w-72 2xl:w-[400px] bg-white/10">
                            <div
                                className="absolute h-full bg-[#2E78AC] bar"
                                style={{
                                    width: inView ? `${response}%` : "0%",
                                    transition: "width 1.8s ease",
                                }}
                            ></div>
                        </div>
                    </div>
                    <div className="flex items-center text-white">
                        <p className="w-full max-w-20 xl:max-w-[116px]">Compliance</p>
                        <div className="relative h-16 lg:h-20 w-72 2xl:w-[400px] bg-white/10">
                            <div
                                className="absolute h-full bg-white bar"
                                style={{
                                    width: inView ? `${compliance}%` : "0%",
                                    transition: "width 1.8s ease",
                                }}
                            ></div>
                        </div>
                    </div>
                    <div className="flex items-center text-white">
                        <p className="w-full max-w-20 xl:max-w-[116px]">Security</p>
                        <div className="relative h-16 lg:h-20 w-72 2xl:w-[400px] bg-white/10">
                            <div
                                className="absolute h-full bg-[#76ADD3] bar"
                                style={{
                                    width: inView ? `${security}%` : "0%",
                                    transition: "width 1.8s ease",
                                }}
                            ></div>
                        </div>
                    </div>
                </div>
                
                <div className="absolute -right-10 xl:right-0 top-0 bottom-0 flex flex-col justify-between text-white text-sm py-5 lg:py-8">
                    <span>{response}%</span>
                    <span>{compliance}%</span>
                    <span>{security}%</span>
                </div>
            </div>
        </div>
    );
}
