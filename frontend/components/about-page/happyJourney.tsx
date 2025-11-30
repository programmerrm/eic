/* eslint-disable @typescript-eslint/no-explicit-any */
import Image from "next/image";
import fingerWhite from "../../public/images/finger-white.svg";
import { getFetchData } from "@/utils/getFetchData";

export default async function HappyJourney() {
    const happyJourneyData = await getFetchData('/about/happy-journey/', {
        tag: 'happy-journey-data',
    });
    const happyJourneyItemData = await getFetchData('/about/happy-journey-item/', {
        tag: 'happy-journey-item-data',
    });

    return (
        <section className="bg-blue py-12 md:py-[100px] rounded-[18px]">
            <div className="container">
                <div className="w-full max-w-[668px] mx-auto text-center mb-12 md:mb-[100px]">
                    <h2 className="text-white">{happyJourneyData?.data?.title}</h2>
                </div>
                <div className="relative">
                    {happyJourneyItemData?.data?.map((item: any) => {
                        return (
                            <div className="flex justify-center gap-5 sm:gap-[51px] group even:flex-row-reverse" key={item.id}>
                                <div className="w-[40%] sm:w-full max-w-[580px] pt-8 md:pt-[51px] pb-10 md:pb-20">
                                    <div
                                        className="flex items-center justify-end gap-4 group-even:flex-row-reverse relative after:absolute after:top-1/2 after:-translate-y-1/2 group-even:after:-left-9 sm:group-even:after:-left-[65px] 2xl:group-even:after:-left-[67px] group-odd:after:-right-9 sm:group-odd:after:-right-[65px] 2xl:group-odd:after:-right-[67px] after:content-[''] after:w-6 after:h-6 after:rounded-full after:bg-white ">
                                        <span
                                            className="absolute top-1/2 -translate-y-1/2 group-even:-left-9 sm:group-even:-left-[65px] 2xl:group-even:-left-[67px] group-odd:-right-9 sm:group-odd:-right-[65px] 2xl:group-odd:-right-[67px] content-[''] w-6 h-6 rounded-full bg-white z-10 "></span>
                                        <h3 className="text-white text-2xl sm:text-3xl md:text-4xl lg:text-5xl lg:leading-12">{item?.year}</h3>
                                        <div className="w-[130px] h-1 bg-white rounded-[18px]"></div>
                                    </div>
                                </div>
                                <div className="w-2 flex items-center justify-center relative">
                                    <div className="absolute w-2 h-full bg-black group-last:rounded-b-[18px] group-first:rounded-t-[18px]"></div>
                                    <div className="absolute bottom-0 w-3 h-full bg-white group-last:rounded-b-[18px] group-first:rounded-t-[18px]">
                                    </div>
                                </div>
                                <div className="group-even:text-end w-[40%] sm:w-full max-w-[580px] pt-8 md:pt-[51px] pb-10 md:pb-20">
                                    <h3 className="text-white text-xl sm:text-3xl md:text-4xl lg:text-[40px] lg:leading-12">{item.title}</h3>
                                    <p className="text-sm sm:text-base sm:leading-6 font-medium font-dmsans text-white mt-4 text-justify">{item.description}</p>
                                </div>
                            </div>
                        )
                    })}
                    <div className="absolute top-10 left-1/2 -translate-x-1/2 w-full h-auto flex items-center justify-center z-20">
                        <Image
                            src={fingerWhite}
                            alt="finger"
                            width={74}
                            height={98}
                        />
                    </div>
                </div>
            </div>
        </section>
    );
}
