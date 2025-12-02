export const dynamic = 'force-dynamic';
import Banner from "@/components/banner/banner";
import HomePageRelatedBlog from "@/components/blogs/homePageRelatedBlog";
import Cybersecurity from "@/components/cybersecurity/cybersecurity";
import Features from "@/components/features/features";
import GloballyAccredited from "@/components/globally-accredited/GloballyAccredited";
import OurProvenProcessSecurity from "@/components/our-proven-process-security/our-proven-process-security";
import Review from "@/components/review/review";
import SecurityFirm from "@/components/security-firm/security-firm";
import HomePageRelated from "@/components/services/homepageRelated";
import HomePageSuccessStoriesRelated from "@/components/success-stories/HomePageSuccessStoriesRelated";
import WhyChoose from "@/components/why-choose/why-choose";

export default function Page() {
    return (
        <>
            <Banner />
            <SecurityFirm />
            <Features />
            <Cybersecurity />
            <HomePageRelated />
            <OurProvenProcessSecurity />
            <WhyChoose />
            <Review />
            <HomePageSuccessStoriesRelated />
            <GloballyAccredited />
            <HomePageRelatedBlog />
        </>
    );
}
