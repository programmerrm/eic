"use client";
import { useState, useEffect } from "react";
import Image from "next/image";
import ScrollIcon from "../../public/images/scrooltopbottom.svg";

export default function ScrollTopBottom() {
    const [isVisible, setIsVisible] = useState(false);

    const handleScroll = () => {
        if (window.scrollY === 0) {
            window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
        } else {
            window.scrollTo({ top: 0, behavior: "smooth" });
        }
    };

    const handleVisibility = () => {
        if (window.scrollY > 100) {
            setIsVisible(true);
        } else {
            setIsVisible(false);
        }
    };

    useEffect(() => {
        window.addEventListener("scroll", handleVisibility);
        return () => {
            window.removeEventListener("scroll", handleVisibility);
        };
    }, []);

    return (
        <button 
            className={`fixed bottom-4 right-4 z-50 p-2.5 text-white bg-blue transition-all duration-300 ease-in-out rounded-full shadow-lg cursor-pointer ${isVisible ? "opacity-100" : "opacity-0 pointer-events-none"}`}
            type="button"
            onClick={handleScroll}
        >
            <Image 
                src={ScrollIcon}
                alt="ScrollTopBottom"
                width={40}
                height={40}
            />
        </button>
    );
}
