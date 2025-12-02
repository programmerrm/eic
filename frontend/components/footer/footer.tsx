/* eslint-disable @typescript-eslint/no-explicit-any */
import { MEDIA_URL } from "@/utils/api";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";
import emailImage from "../../public/images/footer-email.svg";
import footerBgImg from "../../public/images/footer-bg.png";
import phoneImage from "../../public/images/footer-phone.svg";
import SubscribeForm from "../forms/subscribeForm";
import Logo from "../../public/images/eic-logo.svg";

export default async function Footer() {
    const logo = await getFetchData('/configuration/logo/', {
        tag: "logo-data",
    });
    const copyRight = await getFetchData('/configuration/copy-right/', {
        tag: "copy-right-data",
    });
    const infomation = await getFetchData('/contact/infomation/', {
        tag: "contact-data",
    });

    const socialLinkRes = await getFetchData('/configuration/social-link/', {
        tag: "social-link-data",
    });
    const socialLink = Array.isArray(socialLinkRes?.data)
        ? socialLinkRes.data
        : Array.isArray(socialLinkRes)
            ? socialLinkRes
            : [];

    const services = await getFetchData('/services/list-items/', {
        tag: "services-data",
    });
    const servicesList = Array.isArray(services?.results?.data)
        ? services.results.data
        : Array.isArray(services)
            ? services
            : [];

    return (
        <footer className="bg-body py-[30px] md:py-[60px]">
            <div className="bg-contain bg-right bg-no-repeat" style={{
                backgroundImage: `url(${footerBgImg.src})`,
            }}>
                <div className="container">
                    <div className="flex items-center justify-between border-b border-[#EBF3F833]/20 py-5">
                        <Link className="w-full max-w-16 md:max-w-[114px]" href="/">
                            {logo?.data?.image ? (
                                <Image
                                    className="w-full"
                                    src={`${MEDIA_URL}${logo?.data?.image || ""}`}
                                    alt={logo?.data?.alt_text || "eic"}
                                    width={115}
                                    height={60}
                                />
                            ) : (
                                <Image
                                    src={Logo}
                                    alt="eic"
                                    width={115}
                                    height={60}
                                />
                            )}
                        </Link>
                        <div className="flex flex-col sm:flex-row gap-2 sm:gap-7 text-white">
                            <div className="flex items-center gap-2 sm:gap-4">
                                <Image src={phoneImage} alt="phone" width={40} height={40} />
                                <div className="flex flex-col">
                                    <Link className="text-sm sm:text-base font-medium font-roboto py-1" href={`tel:${infomation?.data?.phone_number1 || ""}`}>
                                        {infomation?.data?.phone_number1 || ""}
                                    </Link>
                                    <Link className="text-sm sm:text-base font-medium font-roboto py-1" href={`tel:${infomation?.data?.phone_number2 || ""}`}>
                                        {infomation?.data?.phone_number2 || ""}
                                    </Link>
                                </div>
                            </div>
                            <div className="flex items-center gap-2 sm:gap-4">
                                <Image src={emailImage} alt="mail" width={40} height={40} />
                                <Link className="text-sm sm:text-base font-medium font-roboto" href={`mailto:${infomation?.data?.email || ""}`}>
                                    {infomation?.data?.email || ""}
                                </Link>
                            </div>
                        </div>
                    </div>
                    <div className="flex flex-col lg:flex-row justify-between pt-6 border-b border-[#EBF3F8]/20 pb-12 gap-10 text-white">
                        <div className="w-full max-w-[352px]">
                            <p>Subscribe our newsletter for latest <br /> security related knowledge</p>
                            <SubscribeForm />
                        </div>
                        <div className="w-full max-w-[642px] flex justify-between flex-wrap gap-10">
                            <div className="menu">
                                <h4>Main Page</h4>
                                <ul>
                                    <li><Link href="/">Home</Link></li>
                                    <li><Link href="/about-us">About Us</Link></li>
                                    <li><Link href="/case-studies">Case Studies</Link></li>
                                    <li><Link href="/faq">FAQ</Link></li>
                                    <li><Link href="/blogs">Blog</Link></li>
                                    <li><Link href="/contact">Contact</Link></li>
                                </ul>
                            </div>
                            <div className="menu">
                                <h4>Services</h4>
                                <ul>
                                    {servicesList.map((item: any) => (
                                        <li key={item.id}>
                                            <Link href={`/services/${item.slug}`}>{item.title}</Link>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                            <div className="menu">
                                <h4>Social Link</h4>
                                {socialLink && (
                                    <ul>
                                        {socialLink.map((item: any) => (
                                            <li key={item.id}>
                                                <Link href={item.url} target="_blank">
                                                    <Image
                                                        src={item?.icon || ""}
                                                        alt="social"
                                                        width={16}
                                                        height={16}
                                                        priority 
                                                        fetchPriority="high"
                                                    />
                                                </Link>
                                            </li>
                                        ))}
                                    </ul>
                                )}
                            </div>
                        </div>
                    </div>
                    <div className="flex flex-col xl:flex-row justify-between items-center text-white pt-10 gap-5">
                        <span className="text-[##E6E7EB] text-sm sm:text-base sm:leading-6 font-roboto font-medium">{copyRight?.data?.text || "Powered by Ontik Creative"}</span>
                        <div className="flex gap-4 flex-wrap flex-col items-center lg:flex-row">
                            <Link className="text-[#F4F4F6] text-sm sm:text-base sm:leading-6 font-dmsans font-medium transition-all hover:text-white/50 pr-5 lg:border-r border-white last:border-r-0 last:pr-0" href="/privacy-policy">Privacy Policy</Link>
                            <Link className="text-[#F4F4F6] text-sm sm:text-base sm:leading-6 font-dmsans font-medium transition-all hover:text-white/50 pr-5 lg:border-r border-white last:border-r-0 last:pr-0" href="/terms-conditions">Terms & Conditions</Link>
                            <span className="text-center">{infomation?.data?.address || "House No-15, Road No- 7, Block- C, Gulshan, Niketon, Dhaka-1212"}</span>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
    );
}
