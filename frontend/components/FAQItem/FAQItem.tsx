"use client";

import Image from "next/image";
import Plus from "../../public/images/+.svg";
import Minus from "../../public/images/minus.svg";

type FAQItemProps = {
    question: string;
    answer: string;
    isActive: boolean;
    onClick: () => void;
};

export default function FAQItem({ question, answer, isActive, onClick }: FAQItemProps) {
    return (
        <div
            className={`flex flex-col flex-wrap faq-item cursor-pointer p-4 rounded-md mb-2 transition-all duration-700 ${isActive ? "bg-blue text-white" : "bg-white text-black"
                }`}
            onClick={onClick}
        >
            <div className="flex flex-row flex-wrap justify-between items-center w-full">
                <h4 className={`w-full max-w-[90%] ${isActive ? "text-white!" : " text-[#4E5B76]!"}`}>{question}</h4>
                <Image
                    src={isActive ? Minus : Plus}
                    alt="icon"
                    width={12}
                    height={12}
                />
            </div>
            {isActive && <p className="mt-2 text-sm sm:text-base w-full">{answer}</p>}
        </div>
    );
}
