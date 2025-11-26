// /* eslint-disable @typescript-eslint/no-explicit-any */
// import { MEDIA_URL } from "@/utils/api";
// import { getFetchData } from "@/utils/getFetchData";
// import Image from "next/image";
// import Link from "next/link";
// import emailImage from "../../public/images/footer-email.svg";
// import footerBgImg from "../../public/images/footer-bg.png";
// import phoneImage from "../../public/images/footer-phone.svg";
// import SubscribeForm from "../forms/subscribeForm";

// export default async function Footer() {
//     const logo = await getFetchData('/configuration/logo/');
//     const copyRight = await getFetchData('/configuration/copy-right/');
//     const socialLink = await getFetchData('/configuration/social-link/');
//     const infomation = await getFetchData('/contact/infomation/');
//     const services = await getFetchData('/services/list-items/');
//     return (
//         <footer className="bg-body py-[30px] md:py-[60px]">
//             <div className="bg-contain bg-right bg-no-repeat" style={{
//                 backgroundImage: `url(${footerBgImg.src})`,
//             }}>
//                 <div className="container">

//                     <div className="flex items-center justify-between border-b border-[#EBF3F833]/20 py-5">
//                         <Link className="w-fit" href="/">
//                             <Image className="w-full"
//                                 src={`${MEDIA_URL}${logo?.data.image}`}
//                                 alt={logo.data?.alt_text}
//                                 width={115}
//                                 height={60}
//                             />
//                         </Link>
//                         <div className="flex flex-col sm:flex-row gap-2 sm:gap-7 text-white">
//                             <div className="flex items-center gap-2 sm:gap-4">
//                                 <div className="w-full max-w-6 sm:max-w-full">
//                                     <Image src={phoneImage} alt="phone" />
//                                 </div>
//                                 <div className="flex flex-col">
//                                     <Link className="text-sm sm:text-base" href={`tel:${infomation?.data?.phone_number1}`}>{infomation?.data?.phone_number1}</Link>
//                                     <Link className="text-sm sm:text-base" href={`tel:${infomation?.data?.phone_number2}`}>{infomation?.data?.phone_number2}</Link>
//                                 </div>
//                             </div>
//                             <div className="flex items-center gap-2 sm:gap-4">
//                                 <div className="w-full max-w-6 sm:max-w-full">
//                                     <Image src={emailImage} alt="mail" />
//                                 </div>
//                                 <div className="flex flex-col items-center">
//                                     <a className="text-sm sm:text-base" href={`mailto:${infomation?.data?.email}`}>{infomation?.data?.email}</a>
//                                 </div>
//                             </div>
//                         </div>
//                     </div>

//                     <div className="flex flex-col lg:flex-row justify-between pt-6 border-b border-[#EBF3F8]/20 pb-6 sm:pb-12 gap-10">
//                         <div className="w-full max-w-[352px] text-white">
//                             <p className="">Subscribe our newsletter for latest security related knowledge</p>
//                             <SubscribeForm />
//                         </div>
//                         <div className="w-full max-w-[642px] flex justify-between flex-wrap gap-5 sm:gap-10 text-white">
//                             <div className="menu">
//                                 <h5>Main Page</h5>
//                                 <ul className="font-medium font-dmsans">
//                                     <li><Link href="/">Home</Link></li>
//                                     <li><Link href="/about-us">About Us</Link></li>
//                                     <li><Link href="/case-studies">Case Studies</Link></li>
//                                     <li><Link href="/faq">FAQ</Link></li>
//                                     <li><Link href="/blogs">Blog</Link></li>
//                                     <li><Link href="/contact">Contact</Link></li>
//                                 </ul>
//                             </div>
//                             <div className="menu">
//                                 <h5>Services</h5>
//                                 {services?.results?.data && (
//                                     <ul>
//                                     {services?.results?.data?.map((item:any) => {
//                                         return (
//                                             <li key={item.id}><Link href={`/services/${item.slug}`}>{item.title}</Link></li>
//                                         );
//                                     })}
//                                 </ul>
//                                 )}
                                
//                             </div>
//                             {socialLink && (
//                                 <div className="menu">
//                                     <h5>Social link</h5>
//                                     <ul>
//                                         {socialLink && socialLink?.map((item: any) => {
//                                             return (
//                                                 <li key={item.id}>
//                                                     <Link target="_blank" href={item.url}>
//                                                         <Image
//                                                             src={`${item?.icon}`}
//                                                             alt="socal-link"
//                                                             width={16}
//                                                             height={16}
//                                                         />
//                                                     </Link>
//                                                 </li>
//                                             );
//                                         })}
//                                     </ul>
//                                 </div>
//                             )}
//                         </div>
//                     </div>

//                     <div className="flex flex-col sm:flex-row flex-wrap gap-3 items-center justify-between text-white pt-5 sm:pt-10">
//                         <span className="text-white text-sm sm:text-base sm:leading-6 font-roboto font-medium">{copyRight?.data?.text}</span>
//                         <div className="flex items-center justify-center sm:justify-start gap-4 flex-wrap">
//                             <Link href="/privacy-policy"
//                                 className="text-white text-sm sm:text-base sm:leading-6 font-roboto font-medium transition-all hover:text-white/50 pr-5 border-r border-white last:border-r-0 last:pr-0">Privacy
//                                 Policy</Link>
//                             <Link href="/terms-conditions"
//                                 className="text-white text-sm sm:text-base sm:leading-6 font-roboto font-medium transition-all hover:text-white/50 pr-5 border-r border-white last:border-r-0 last:pr-0">Terms
//                                 & Condition</Link>
//                             <span className=" pr-5 border-r border-white last:border-r-0 last:pr-0">{infomation?.data?.address}</span>
//                         </div>
//                     </div>
//                 </div>
//             </div>
//         </footer>
//     );
// }


/* eslint-disable @typescript-eslint/no-explicit-any */
import { MEDIA_URL } from "@/utils/api";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";
import emailImage from "../../public/images/footer-email.svg";
import footerBgImg from "../../public/images/footer-bg.png";
import phoneImage from "../../public/images/footer-phone.svg";
import SubscribeForm from "../forms/subscribeForm";

export default async function Footer() {
    const logo = await getFetchData('/configuration/logo/') || {};
    const copyRight = await getFetchData('/configuration/copy-right/') || {};
    const socialLinkRes = await getFetchData('/configuration/social-link/') || {};
    const infomation = await getFetchData('/contact/infomation/') || {};
    const services = await getFetchData('/services/list-items/') || {};

    // SAFE VALUES
    const socialLink = Array.isArray(socialLinkRes?.data) ? socialLinkRes.data : [];
    const servicesList = Array.isArray(services?.results?.data) ? services.results.data : [];

    return (
        <footer className="bg-body py-[30px] md:py-[60px]">
            <div className="bg-contain bg-right bg-no-repeat" style={{
                backgroundImage: `url(${footerBgImg.src})`,
            }}>
                <div className="container">

                    {/* LOGO + CONTACT */}
                    <div className="flex items-center justify-between border-b border-[#EBF3F833]/20 py-5">
                        <Link className="w-fit" href="/">
                            <Image
                                className="w-full"
                                src={`${MEDIA_URL}${logo?.data?.image || ""}`}
                                alt={logo?.data?.alt_text || "Logo"}
                                width={115}
                                height={60}
                            />
                        </Link>

                        <div className="flex flex-col sm:flex-row gap-2 sm:gap-7 text-white">
                            <div className="flex items-center gap-2 sm:gap-4">
                                <Image src={phoneImage} alt="phone" />
                                <div className="flex flex-col">
                                    <Link href={`tel:${infomation?.data?.phone_number1 || ""}`}>
                                        {infomation?.data?.phone_number1 || ""}
                                    </Link>
                                    <Link href={`tel:${infomation?.data?.phone_number2 || ""}`}>
                                        {infomation?.data?.phone_number2 || ""}
                                    </Link>
                                </div>
                            </div>

                            <div className="flex items-center gap-2 sm:gap-4">
                                <Image src={emailImage} alt="mail" />
                                <a href={`mailto:${infomation?.data?.email || ""}`}>
                                    {infomation?.data?.email || ""}
                                </a>
                            </div>
                        </div>
                    </div>

                    {/* MENUS */}
                    <div className="flex flex-col lg:flex-row justify-between pt-6 border-b border-[#EBF3F8]/20 pb-12 gap-10 text-white">

                        <div className="w-full max-w-[352px]">
                            <p>Subscribe our newsletter</p>
                            <SubscribeForm />
                        </div>

                        <div className="w-full max-w-[642px] flex justify-between flex-wrap gap-10">
                            
                            <div className="menu">
                                <h5>Main Page</h5>
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
                                <h5>Services</h5>
                                <ul>
                                    {servicesList.map((item: any) => (
                                        <li key={item.id}>
                                            <Link href={`/services/${item.slug}`}>{item.title}</Link>
                                        </li>
                                    ))}
                                </ul>
                            </div>

                            <div className="menu">
                                <h5>Social Link</h5>
                                <ul>
                                    {socialLink.map((item: any) => (
                                        <li key={item.id}>
                                            <Link href={item.url} target="_blank">
                                                <Image
                                                    src={item?.icon || ""}
                                                    alt="social"
                                                    width={16}
                                                    height={16}
                                                />
                                            </Link>
                                        </li>
                                    ))}
                                </ul>
                            </div>

                        </div>
                    </div>

                    {/* COPYRIGHT */}
                    <div className="flex flex-col sm:flex-row justify-between text-white pt-10">
                        <span>{copyRight?.data?.text || ""}</span>
                        <div className="flex gap-4 flex-wrap">
                            <Link href="/privacy-policy">Privacy Policy</Link>
                            <Link href="/terms-conditions">Terms & Conditions</Link>
                            <span>{infomation?.data?.address || ""}</span>
                        </div>
                    </div>

                </div>
            </div>
        </footer>
    );
}
