/* eslint-disable @typescript-eslint/no-explicit-any */
import BannerImg from "../../public/images/banner-img.svg";

export default async function SectionBanner({ topBarData }: any) {
    return (
        <section className="mt-24 md:mt-36 banner-section bg-blue [clip-path:polygon(0_0,100%_0,100%_calc(100%-50px),calc(100%-60px)_100%,0_100%)] md:[clip-path:polygon(0_0,100%_0,100%_calc(100%-100px),calc(100%-150px)_100%,0_100%)]">
            <div className="container">
                <div className="bg-bottom bg-contain bg-no-repeat" style={{
                    backgroundImage: `url(${BannerImg.src})`,
                }}>
                    <div className="py-10 sm:py-20 md:py-40 lg:py-[232px] text-white text-center ">
                        {topBarData?.title && (
                            <h1 className="uppercase">{topBarData?.title}</h1>
                        )}
                        {topBarData?.description && (
                            <p className="text-base sm:text-lg md:text-2xl md:leading-8 font-spacegrotesk mt-4 sm:mt-8 w-full max-w-4/5 lg:max-w-[60%] mx-auto">{topBarData?.description}</p>
                        )}
                    </div>
                </div>
            </div>
        </section>
    );
}
