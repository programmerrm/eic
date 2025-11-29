import SectionBanner from "@/components/banner/section-banner";
import AboutSecurity from "@/components/security-firm/about-security";
import StayCompliant from "@/components/stay-compliant/stay-compliant";
import { getFetchData } from "@/utils/getFetchData";

export default async function Page() {
    const topBarFetchData = await getFetchData('/about/top-bar/', {
        tag: "about-to-bar-data",
    });

    return (
        <>
            <SectionBanner topBarData={topBarFetchData?.data} />
            <AboutSecurity />
            <section className="bg-white py-12 md:py-[100px] relative">
                <div className="container">
                    <h2 className="text-center mb-10 sm:-mb-20">The <span className="text-blue">Core Principles</span> We Uphold</h2>
                    <div className="our-core-value">
                        <button
                            className="text-xs sm:text-sm md:text-base lg:text-lg bg-body py-2 md:py-3 lg:py-4 px-4 sm:px-6 md:px-10 rounded-full text-white absolute bottom-27 sm:bottom-46 left-0 md:-left-2 rotate-25">Customer-Centricity</button>
                        <button
                            className="text-xs sm:text-sm md:text-base lg:text-lg bg-body py-2 md:py-3 lg:py-4 px-4 sm:px-6 md:px-10 rounded-full text-white absolute bottom-4 sm:bottom-12 lg:bottom-10 left-1/2 -translate-x-1/2 rotate-0">Reliability</button>
                        <button
                            className="text-xs sm:text-sm md:text-base lg:text-lg bg-body py-2 md:py-3 lg:py-4 px-4 sm:px-6 md:px-10 rounded-full text-white absolute bottom-12 sm:bottom-22 left-46 -rotate-6">Innovation</button>
                        <button
                            className="text-xs sm:text-sm md:text-base lg:text-lg bg-body py-2 md:py-3 lg:py-4 px-4 sm:px-6 md:px-10 rounded-full text-white absolute bottom-13 sm:bottom-26 right-41 rotate-8">Collaboration</button>
                        <button
                            className="text-xs sm:text-sm md:text-base lg:text-lg bg-body py-2 md:py-3 lg:py-4 px-4 sm:px-6 md:px-10 rounded-full text-white absolute bottom-23 sm:bottom-44 right-6 -rotate-21">Transparency</button>
                        <button
                            className="text-xs sm:text-sm md:text-base lg:text-lg bg-body py-2 md:py-3 lg:py-4 px-4 sm:px-6 md:px-10 rounded-full text-white absolute bottom-27 sm:bottom-41 right-24 sm:right-80 -rotate-15">Integrity</button>
                    </div>
                </div>
            </section>
            <StayCompliant />
        </>
    );
}
