"use client";

import { useState } from "react";
import FAQItem from "../FAQItem/FAQItem";

type FAQProps = {
    faqItems: { question: string; answer: string }[];
};

export default function FAQ({ faqItems }: FAQProps) {
    const [activeIndex, setActiveIndex] = useState<number | null>(0);

    const handleClick = (index: number) => {
        if (activeIndex === index) {
            setActiveIndex(null);
        } else {
            setActiveIndex(index);
        }
    };

    return (
        <div className="w-full max-w-[696px] space-y-4 mt-10 md:mt-20">
            {faqItems.map((item, index) => (
                <FAQItem
                    key={index}
                    question={item.question}
                    answer={item.answer}
                    isActive={index === activeIndex}
                    onClick={() => handleClick(index)}
                />
            ))}
        </div>
    );
}
