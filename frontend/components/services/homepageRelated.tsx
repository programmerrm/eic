import BannerImg from "../../public/images/compliance-bg.svg";
import { getFetchData } from "@/utils/getFetchData";
import ServicesGrid from "./ServicesGrid";

export default async function HomePageRelated() {
    const data = await getFetchData("/services/list-items/");

    const items = data?.results?.data.reverse() ?? [];

    return (
        <section
            className="pt-5 md:pt-10 lg:pt-13 mt-5 md:mt-10 lg:mt-12 pb-3 md:pb-6 mb-12 lg:mb-24 bg-contain bg-top-right bg-no-repeat"
            style={{
                backgroundImage: `url(${BannerImg.src})`,
            }}
        >
            <div className="container">
                <div className="w-full max-w-147 mx-auto">
                    <h2 className="text-center">Comprehensive Cybersecurity Solutions</h2>
                </div>

                <ServicesGrid items={items} />
            </div>
        </section>
    );
}
