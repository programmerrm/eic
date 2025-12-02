/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable react-hooks/exhaustive-deps */
"use client";

import { useEffect, useRef, useState } from "react";
import Image from "next/image";

export default function CybersecurityCounters({ items }: any) {
    const ref = useRef<HTMLDivElement | null>(null);
    const [inView, setInView] = useState(false);
    const [counters, setCounters] = useState<number[]>(items?.map(() => 0) || []);

    useEffect(() => {
        const element = ref.current;
        if (!element) return;

        const observer = new IntersectionObserver(
            ([entry]) => {
                if (entry.isIntersecting) setInView(true);
            },
            { threshold: 0.3 }
        );

        observer.observe(element);

        return () => {
            if (element) observer.unobserve(element);
        };
    }, []);

    useEffect(() => {
        if (!inView) return;

        const duration = 1500;
        const stepTime = 30;
        const steps = Math.ceil(duration / stepTime);

        const startValues = counters.slice();
        const endValues = items.map((item: any) => item.count);
        let currentStep = 0;

        const interval = setInterval(() => {
            currentStep++;
            const newValues = startValues.map((start, i) => {
                const diff = endValues[i] - start;
                return Math.min(Math.round(start + (diff * currentStep) / steps), endValues[i]);
            });
            setCounters(newValues);

            if (currentStep >= steps) clearInterval(interval);
        }, stepTime);

        return () => clearInterval(interval);
    }, [inView]);

    return (
        <div ref={ref} className="grid grid-cols-2 gap-x-5 gap-y-16">
            {items?.map((item: any, index: number) => (
                <div key={item.id} className="flex flex-col justify-between gap-6">
                    <div className="w-full max-w-11 sm:max-w-[60px]">
                        <Image
                            src={item.image}
                            alt={item.title}
                            width={60}
                            height={62}
                        />
                    </div>
                    <div>
                        <h5 className="text-base sm:text-lg leading-6 font-dmsans font-normal">
                            {item.title}
                        </h5>
                        <div className="h-0.5 w-full lg:max-w-[206px] bg-white/30 mt-4"></div>
                        <span className="text-3xl sm:text-[40px] leading-10 font-semibold text-white font-spacegrotesk mt-4 block">
                            {counters[index]}+
                        </span>
                    </div>
                </div>
            ))}
        </div>
    );
}
