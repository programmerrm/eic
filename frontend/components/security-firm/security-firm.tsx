import { MEDIA_URL } from "@/utils/api";
import { getFetchData } from "@/utils/getFetchData";
import Image from "next/image";
import Link from "next/link";

export default async function SecurityFirm() {
    const security_firm_data = await getFetchData('/homepage/security-firm/');
    const bgImage = security_firm_data?.data?.bg ? `${MEDIA_URL}${security_firm_data.data.bg}` : null;
    return (
        <section className="bg-[#EBF3F8] py-12 md:py-[100px]">
            <div className="container">
                <div className="flex flex-col md:flex-row">
                    <div className="w-full md:max-w-[52.058%] lg:pt-8">
                        <h2>
                            <span className="text-blue">{security_firm_data?.data?.title_span}</span> {security_firm_data?.data?.title_normal}
                        </h2>
                        {security_firm_data?.data?.main_img && (
                            <div>
                                <Image src={`${MEDIA_URL}${security_firm_data?.data?.main_img}`} alt="security" width={375} height={235} />
                            </div>
                        )}
                    </div>
                    <div className="w-full md:max-w-[calc(100%-52.058%)] bg-contain bg-no-repeat mb-16"
                        style={{
                            backgroundImage: `url(${bgImage})`,
                            backgroundPosition: "center",
                            backgroundSize: "contain",
                        }}>
                        <div className="pt-10 lg:pt-[152px] pl-16 lg:pl-40">
                            <div className=" text-body">
                                <h3>{security_firm_data?.data?.mission_title}</h3>
                                <p className="mt-3.5">{security_firm_data?.data?.mission_description}</p>
                            </div>
                            <div className="mt-8 text-body">
                                <h3>{security_firm_data?.data?.vision_title}</h3>
                                <p className="mt-3.5">{security_firm_data?.data?.vision_description}</p>
                            </div>
                            <div className="pt-12">
                                <Link href={security_firm_data?.data?.get_to_know_us_btn_url || ""} className="w-fit btn-primary group">
                                    {security_firm_data?.data?.get_to_know_us_btn_name}
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
                                </Link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div className="border-t-2 border-[#C0D9EB] pt-12 md:pt-[100px]">
                <div className="container">
                    <div className="flex flex-col md:flex-row items-center gap-8 xl:gap-16">
                        <div
                            className="w-full max-w-[708px] bg-body text-white py-8 xl:py-16 pr-[62px] pl-8 xl:pl-16 [clip-path:polygon(0_0,100%_0,100%_calc(100%-50px),calc(100%-40px)_100%,0_100%)] lg:[clip-path:polygon(0_0,100%_0,100%_calc(100%-80px),calc(100%-56px)_100%,0_100%)] flex flex-col relative">
                            <div className="w-full max-w-[708px] chart relative">
                                <div className="flex flex-col gap-6">
                                    <div className="flex items-center text-white">
                                        <p className=" w-full max-w-20 xl:max-w-[116px]">Security</p>
                                        <div className="relative h-16 lg:h-20 w-72 2xl:w-[400px] bg-white/10">
                                            <div
                                                className="absolute h-full bg-[#2E78AC] bar animate-bar"
                                            ></div>
                                        </div>
                                    </div>
                                    <div className="flex items-center text-white">
                                        <p className=" w-full max-w-20 xl:max-w-[116px]">Ability</p>
                                        <div className="relative h-16 lg:h-20 w-72 2xl:w-[400px] bg-white/10">
                                            <div
                                                className="absolute h-full bg-white bar animate-bar"
                                            ></div>
                                        </div>
                                    </div>
                                    <div className="flex items-center text-white">
                                        <p className=" w-full max-w-20 xl:max-w-[116px]">Solving</p>
                                        <div className="relative h-16 lg:h-20 w-72 2xl:w-[400px] bg-white/10">
                                            <div
                                                className="absolute h-full bg-[#76ADD3] bar animate-bar"
                                            ></div>
                                        </div>
                                    </div>
                                </div>
                                <div className="absolute -right-10 xl:right-0 top-0 bottom-0 flex flex-col justify-between text-white text-sm py-5 lg:py-8">
                                    <span>{security_firm_data?.data?.security_persentences}%</span>
                                    <span>{security_firm_data?.data?.ability_persentences}%</span>
                                    <span>{security_firm_data?.data?.solving_persentences}%</span>
                                </div>
                            </div>
                        </div>
                        {security_firm_data?.data?.sub_img && (
                            <div className="w-full max-w-[605px]">
                                <Image
                                    src={`${MEDIA_URL}${security_firm_data?.data?.sub_img}`}
                                    alt="security"
                                    width={605}
                                    height={400}
                                />
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </section>
    );
}
