"use client";

import Image from "next/image";
import Plus from "../../public/images/+.svg";
import Minus from "../../public/images/minus.svg";
import { useEffect, useRef, useState } from "react";
import { TextEditor } from "../text-editor/textEditor";

type FAQItemProps = {
    question: string;
    answer: string;
    isActive: boolean;
    onClick: () => void;
};

export default function FAQItem({ question, answer, isActive, onClick }: FAQItemProps) {
    const contentRef = useRef<HTMLDivElement | null>(null);
    const [height, setHeight] = useState<string>("0px");

    useEffect(() => {
        if (isActive && contentRef.current) {
            setHeight(`${contentRef.current.scrollHeight}px`);
        } else {
            setHeight("0px");
        }
    }, [isActive, answer]);

    return (
        <div
            className={`flex flex-col flex-wrap faq-item cursor-pointer p-4 rounded-md mb-2 transition-colors duration-300 ${isActive ? "bg-blue text-white" : "bg-white text-black"
                }`}
            onClick={onClick}
        >
            <div className="flex flex-row flex-wrap justify-between items-center w-full">
                <h4
                    className={`w-full max-w-[90%] transition-colors duration-300 ${isActive ? "text-white" : "text-[#4E5B76]"
                        }`}
                >
                    {question}
                </h4>
                <Image
                    src={isActive ? Minus : Plus}
                    alt="icon"
                    width={12}
                    height={12}
                    priority
                    fetchPriority="high"
                />
            </div>
            <div
                ref={contentRef}
                className={`overflow-hidden transition-[height,opacity] duration-300 ease-in-out ${isActive ? "visible opacity-100 mt-2" : "invisible opacity-0"
                    }`}
                style={{ height }}
            >
                <TextEditor content={answer} style={"text-sm sm:text-base w-full"} />
            </div>
        </div>
    );
}
