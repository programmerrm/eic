import BannerImg from "../../public/images/trusted-for-proven.png";
import { getFetchData } from "@/utils/getFetchData";
import ReviewSlider from "./ReviewSlider"; // ⬅ client component

export default async function Review() {
    const reviewTopBarData = await getFetchData("/homepage/review-top-bar/", {
        tag: "review-top-bar-data",
    });

    const reviews = await getFetchData("/homepage/review-items/", {
        tag: "review-items-data",
    });

    const items = reviews?.data || [];

    return (
        <section
            className="bg-contain bg-left bg-no-repeat pb-12 md:pb-56 pt-12 sm:pt-14 lg:pt-[380px] lg:mt-[-352px]"
            style={{
                backgroundImage: `url(${BannerImg.src})`,
            }}
        >
            <div className="container">
                <div className="max-w-md w-full mx-auto text-center mb-12 sm:mb-[98px]">
                    <h2>
                        {reviewTopBarData?.data?.title_before_span}{" "}
                        <span className="text-blue">
                            {reviewTopBarData?.data?.title_span}
                        </span>{" "}
                        {reviewTopBarData?.data?.title_after_span}
                    </h2>
                </div>
            </div>
            <ReviewSlider items={items} />
        </section>
    );
}
