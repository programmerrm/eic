import Image from "next/image";
import Link from "next/link";
import ContactForm from "../../components/forms/ContactForm";
import address from "../../public/images/address.svg";
import BannerImg from "../../public/images/banner-img.svg";
import email from "../../public/images/email.svg";
import ContactFormBG from "../../public/images/finger.svg";
import phone from "../../public/images/phone-icon.svg";
import { MEDIA_URL } from "../../utils/api";
import { getFetchData } from "../../utils/getFetchData";

export default async function Page() {
    const topBarData = await getFetchData("/contact/top-bar/", {
        tag: "contact-data",
    });

    const infomation = await getFetchData("/contact/infomation/", {
        tag: "contact-data",
    });

    const googleMap = await getFetchData("/contact/google-map/", {
        tag: "contact-data",
    });

    return (
        <>
            {topBarData?.data && (
                <section className="mt-24 md:mt-36 banner-section bg-blue [clip-path:polygon(0_0,100%_0,100%_calc(100%-50px),calc(100%-60px)_100%,0_100%)] md:[clip-path:polygon(0_0,100%_0,100%_calc(100%-100px),calc(100%-150px)_100%,0_100%)]">
                    <div className="container">
                        <div className="bg-bottom bg-contain bg-no-repeat" style={{
                            backgroundImage: `url(${BannerImg.src})`,
                        }}>
                            <div className="max-w-[740px] mx-auto py-10 sm:py-20 md:py-40 lg:py-[232px] text-white text-center ">
                                {topBarData?.data?.title && (
                                    <h1 className="uppercase">{topBarData?.data?.title}</h1>
                                )}
                                {topBarData?.data?.description && (
                                    <p className="text-base sm:text-lg md:text-2xl md:leading-8 font-bold font-spacegrotesk mt-2 sm:mt-4 w-full max-w-[626px] mx-auto">{topBarData?.data?.description}</p>
                                )}
                            </div>
                        </div>
                    </div>
                </section>
            )}
            <section className="py-12 md:py-[100px] bg-center bg-cover bg-no-repeat" style={{
                backgroundImage: `url(${ContactFormBG.src})`,
            }}>
                <div className="container">
                    <div className="flex flex-col lg:flex-row justify-between">
                        <div className="w-full max-w-[755px] mr-[110px] bg-[#EBF3F8] p-4 md:p-8 xl:p-[58px] rounded-[10px] order-2 lg:order-1">
                            <ContactForm />
                        </div>
                        <div className="w-full max-w-[494px] mx-auto order-1 lg:order-2">
                            {topBarData?.data?.image && (
                                <div>
                                    {topBarData?.data?.image && (
                                        <Image
                                            width={495}
                                            height={525}
                                            src={`${MEDIA_URL}${topBarData?.data?.image}`}
                                            alt="contact form background image"
                                            priority 
                                            fetchPriority="high"
                                        />
                                    )}
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            </section>
            {infomation?.data && (
                <section className="bg-blue pt-12 md:pt-[100px] pb-11 md:pb-[90px]">
                    <div className="container">
                        <div className="mb-10 md:mb-20 w-full max-w-[668px]">
                            {infomation?.data?.title && (
                                <h2 className="text-white  mb-4 md:mb-6">{infomation?.data?.title}</h2>
                            )}
                            {infomation?.data?.description && (
                                <p className="text-white text-base sm:text-lg md:text-2xl md:leading-8 font-normal font-spacegrotesk">{infomation?.data?.description}</p>
                            )}
                        </div>
                        <div className="flex items-center sm:items-start justify-between flex-wrap gap-x-5 gap-y-8 md:gap-y-10 lg:gap-y-16">
                            <div className="w-full max-w-[272px] flex flex-col justify-between gap-6">
                                <div className="w-full max-w-11 sm:max-w-[60px]">
                                    <Image
                                        src={email}
                                        alt="email"
                                        width={60}
                                        height={66}
                                    />
                                </div>
                                <div className="content">
                                    <h5 className="text-base sm:text-2xl leading-8 font-bold text-white">Email address</h5>
                                    <div className="h-0.5 w-full bg-white/30 mt-4"></div>
                                    {infomation?.data?.email && (
                                        <Link href={`mailto:${infomation?.data?.email}`}
                                            className="text-sm sm:text-base leading-6 font-normal text-white font-dmsans mt-4 block">{infomation?.data?.email}</Link>
                                    )}
                                </div>
                            </div>
                            <div className="w-full max-w-[272px] flex flex-col justify-between gap-6">
                                <div className="w-full max-w-11 sm:max-w-[60px]">
                                    <Image
                                        src={address}
                                        alt="address"
                                        width={60}
                                        height={66}
                                    />
                                </div>
                                <div className="content">
                                    <h5 className="text-base sm:text-2xl leading-8 font-bold text-white">Office address</h5>
                                    <div className="h-0.5 w-full bg-white/30 mt-4"></div>
                                    {infomation?.data?.address && (
                                        <span
                                            className="text-sm sm:text-base leading-6 font-normal text-white font-dmsans mt-4 block">{infomation?.data?.address}</span>
                                    )}
                                </div>
                            </div>
                            <div className="w-full max-w-[272px] flex flex-col justify-between gap-6">
                                <div className="w-full max-w-11 sm:max-w-[60px]">
                                    <Image
                                        src={phone}
                                        alt="Phone"
                                        width={60}
                                        height={66}
                                    />
                                </div>
                                <div className="content">
                                    <h5 className="text-base sm:text-2xl leading-8 font-bold text-white">Phone number</h5>
                                    <div className="h-0.5 w-full bg-white/30 mt-4"></div>
                                    <div>
                                        {infomation?.data?.phone_number1 && (
                                            <Link href={`tel:${infomation?.data?.phone_number1}`} className="text-sm sm:text-base leading-6 font-normal text-white font-dmsans mt-4 block">{infomation?.data?.phone_number1}</Link>
                                        )}
                                        {infomation?.data?.phone_number2 && (
                                            <Link href={`tel:${infomation?.data?.phone_number2}`} className="text-sm sm:text-base leading-6 font-normal text-white font-dmsans mt-4 block">{infomation?.data?.phone_number2}</Link>
                                        )}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            )}
            {googleMap?.data && (
                <section>
                    <div className="map w-full overflow-hidden">
                        {googleMap?.data?.url && (
                            <iframe
                            className="block w-full min-h-75 sm:min-h-100 lg:min-h-125 xl:min-h-203.75"
                            src={googleMap.data.url}
                            style={{ border: 0 }}
                            allowFullScreen
                            referrerPolicy="no-referrer-when-downgrade"
                            />
                        )}
                    </div>
                </section>
            )}
        </>
    );
}
