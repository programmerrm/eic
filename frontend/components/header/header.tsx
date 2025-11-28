/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { MEDIA_URL } from "@/utils/api";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useState } from "react";
import Logo from "../../public/images/eic-logo.svg";

export default function Header() {
    const pathname = usePathname();
    const [isOpen, setIsOpen] = useState(false);
    const [isScrolled, setIsScrolled] = useState(false);
    const [logo, setLogo] = useState<any>(null);

    useEffect(() => {
        async function fetchLogo() {
            const res = await getFetchData("https://eicsec.com/api/v1/configuration/logo/");
            setLogo(res?.data);
        }
        fetchLogo();
    }, []);

    useEffect(() => {
        const onScroll = () => setIsScrolled(window.scrollY > 50);
        window.addEventListener("scroll", onScroll);
        return () => window.removeEventListener("scroll", onScroll);
    }, []);

    const isActive = (route: string) =>
        route === pathname ? "text-blue-dark!" : "text-black";

    const handleLinkClick = () => setIsOpen(false);

    return (
        <header
            className={`home-page fixed top-0 left-0 right-0 z-50 transition-all duration-500 
            ${isScrolled ? "bg-white! shadow-md py-3 sm:py-6" : "py-7 md:py-[54px]"}`}
        >
            <div className="container">
                <div className="flex items-center justify-between gap-2">
                    <Link href="/" className="w-16 md:w-auto" onClick={handleLinkClick}>
                        {logo?.image ? (
                            <Image
                                src={`${MEDIA_URL}${logo?.image || ""}`}
                                alt={logo?.alt_text || "Logo"}
                                width={90}
                                height={50}
                            />
                        ) : (
                            <Image
                                src={Logo}
                                alt="eic"
                                width={90}
                                height={50}
                            />
                        )}
                    </Link>
                    <nav
                        className={`absolute top-0 ${isOpen ? "left-0" : "left-[-9999px]"}
                        right-0 bg-white lg:bg-transparent w-full h-screen lg:h-auto 
                        lg:w-auto lg:static flex items-center flex-col justify-between 
                        lg:block py-10 lg:py-0 transition-all duration-500 ease-in-out overflow-y-auto`}
                    >
                        <ul className="header-nav flex flex-col lg:flex-row items-center justify-center flex-wrap xl:gap-6">
                            <li>
                                <Link href="/" className={isActive("/")} onClick={handleLinkClick}>Home</Link>
                            </li>
                            <li>
                                <Link href="/about-us" className={isActive("/about-us")} onClick={handleLinkClick}>About Us</Link>
                            </li>
                            <li>
                                <Link href="/services" className={isActive("/services")} onClick={handleLinkClick}>Services</Link>
                            </li>
                            <li>
                                <Link href="/case-studies" className={isActive("/case-studies")} onClick={handleLinkClick}>Case Studies</Link>
                            </li>
                            <li>
                                <Link href="/blogs" className={isActive("/blogs")} onClick={handleLinkClick}>Blog</Link>
                            </li>
                            <li>
                                <Link href="/contact" className={isActive("/contact")} onClick={handleLinkClick}>Contact</Link>
                            </li>
                        </ul>
                        <div className="lg:hidden flex items-center justify-center mt-5">
                            <a className="btn-primary group" href="">
                                Schedule a Call
                                <svg
                                    className="transition-all duration-500 group-hover:rotate-45 w-5 md:w-6 h-5 md:h-6"
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                >
                                    <path
                                        stroke="currentColor"
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        strokeWidth={1.5}
                                        d="M6 18 18 6m0 0H9m9 0v9"
                                    />
                                </svg>
                            </a>
                        </div>
                        <div className="w-6 absolute top-5 right-5 lg:hidden">
                            <button className="w-full cursor-pointer" onClick={() => setIsOpen(false)}>
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" className="w-full">
                                    <path
                                        fill="none"
                                        stroke="#000000"
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        strokeWidth="2"
                                        d="M6 18L18 6M6 6l12 12"
                                    />
                                </svg>
                            </button>
                        </div>
                    </nav>
                    <div className="hidden lg:block min-w-[212px]">
                        <a className="btn-primary group" href="">
                            Schedule a Call
                            <svg
                                className="transition-all duration-500 group-hover:rotate-45 w-5 md:w-6 h-5 md:h-6"
                                xmlns="http://www.w3.org/2000/svg"
                                fill="none"
                                viewBox="0 0 24 24"
                            >
                                <path
                                    stroke="currentColor"
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    strokeWidth={1.5}
                                    d="M6 18 18 6m0 0H9m9 0v9"
                                />
                            </svg>
                        </a>
                    </div>
                    <div className="block lg:hidden w-8">
                        <button className="w-8 cursor-pointer" onClick={() => setIsOpen(true)}>
                            <svg className="w-full" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                                <path
                                    fill="none"
                                    stroke="#000000"
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    strokeWidth="2"
                                    d="M3 12h18M3 6h18M3 18h18"
                                />
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
        </header>
    );
}
