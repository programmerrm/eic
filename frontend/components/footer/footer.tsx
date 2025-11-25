/* eslint-disable @typescript-eslint/no-explicit-any */
import { MEDIA_URL } from "@/utils/api";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";
import emailImage from "../../public/images/footer-email.svg";
import footerBgImg from "../../public/images/footer-bg.png";
import phoneImage from "../../public/images/footer-phone.svg";

export default async function Footer() {
    const logo = await getFetchData('/configuration/logo/');
    const copyRight = await getFetchData('/configuration/copy-right/');
    const socialLink = await getFetchData('/configuration/social-link/');
    return (
        <footer className="bg-body py-[30px] md:py-[60px]">
            <div className="bg-contain bg-right bg-no-repeat" style={{
                backgroundImage: `url(${footerBgImg.src})`,
            }}>
                <div className="container">
                    <div className="flex items-center justify-between border-b border-[#EBF3F833]/20 py-5">
                        <Link className="w-fit" href="/">
                            <Image className="w-full"
                                src={`${MEDIA_URL}${logo?.data.image}`}
                                alt={logo.data?.alt_text}
                                width={115}
                                height={60}
                            />
                        </Link>
                        <div className="flex flex-col sm:flex-row gap-2 sm:gap-7 text-white">
                            <div className="flex items-center gap-2 sm:gap-4">
                                <div className="w-full max-w-6 sm:max-w-full">
                                    <Image src={phoneImage} alt="phone" />
                                </div>
                                <div className="flex flex-col">
                                    <a className="text-sm sm:text-base" href={`tel:+880174692777`}>+880174692777</a>
                                    <a className="text-sm sm:text-base" href={`tel:+880174692777`}>+880174692777</a>
                                </div>
                            </div>
                            <div className="flex items-center gap-2 sm:gap-4">
                                <div className="w-full max-w-6 sm:max-w-full">
                                    <Image src={emailImage} alt="mail" />
                                </div>
                                <div className="flex flex-col items-center">
                                    <a className="text-sm sm:text-base" href={`mailto:880174692777`}>880174692777</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="flex flex-col lg:flex-row justify-between pt-6 border-b border-[#EBF3F8]/20 pb-6 sm:pb-12 gap-10">
                        <div className="w-full max-w-[352px] text-white">
                            <p className="">Subscribe our newsletter for latest security related knowledge</p>
                            <form action="" className="mt-6">
                                <div className="flex items-center gap-1">
                                    <input
                                        className="bg-white rounded-full focus:outline-0 text-sm leading-3.5 font-roboto py-[13px] px-4 text-[#142149] w-full max-w-[241px]"
                                        type="email" required placeholder="Enter your email" />

                                    <button className="text-base font-roboto font-medium leading-4 px-6 py-3 rounded-full bg-blue"
                                        type="submit">Submit</button>
                                </div>
                            </form>
                        </div>
                        <div className="w-full max-w-[642px] flex justify-between flex-wrap gap-5 sm:gap-10 text-white">
                            <div className="menu">
                                <h5>Main Page</h5>
                                <ul className="font-medium font-dmsans">
                                    <li><Link href="/">Home</Link></li>
                                    <li><Link href="/about-us">About Us</Link></li>
                                    <li><Link href="/case-studies">Case Studies</Link></li>
                                    <li><Link href="/blogs">Blog</Link></li>
                                    <li><Link href="/contact">Contact</Link></li>
                                </ul>
                            </div>
                            <div className="menu">
                                <h5>Services</h5>
                                <ul>
                                    <li><Link href="">PCI DSS Compliance </Link></li>
                                    <li><Link href="">ISO 27001ISMS</Link></li>
                                    <li><Link href="">Swift CSP Assessment</Link></li>
                                    <li><Link href="">ISO 22301:2019</Link></li>
                                    <li><Link href="">Penetration Testing</Link></li>
                                </ul>
                            </div>
                            {socialLink && (
                                <div className="menu">
                                    <h5>Social link</h5>
                                    <ul>
                                        {socialLink && socialLink?.map((item: any) => {
                                            return (
                                                <li key={item.id}>
                                                    <Link target="_blank" href={item.url}>{item.name}</Link>
                                                </li>
                                            );
                                        })}
                                    </ul>
                                </div>
                            )}
                        </div>
                    </div>
                    <div className="flex flex-col sm:flex-row gap-3 items-center justify-between text-white pt-5 sm:pt-10">
                        {copyRight?.data && (
                            <span className="text-white text-sm sm:text-base sm:leading-6 font-roboto font-medium">{copyRight?.data?.text}</span>
                        )}
                        <div className="flex items-center gap-4">
                            <Link href="/privacy-policy"
                                className="text-white text-sm sm:text-base sm:leading-6 font-roboto font-medium transition-all hover:text-white/50">Privacy
                                Policy</Link>
                            <span className="w-0.5 h-3 bg-white"></span>
                            <Link href="/terms-condition"
                                className="text-white text-sm sm:text-base sm:leading-6 font-roboto font-medium transition-all hover:text-white/50">Terms
                                & Condition</Link>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
    );
}
