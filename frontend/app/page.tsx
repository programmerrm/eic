export const dynamic = 'force-dynamic';
import Banner from "@/components/banner/banner";
import Cybersecurity from "@/components/cybersecurity/cybersecurity";
import Features from "@/components/features/features";
import OurProvenProcessSecurity from "@/components/our-proven-process-security/our-proven-process-security";
import SecurityFirm from "@/components/security-firm/security-firm";
import HomePageRelated from "@/components/services/homepageRelated";

export default function Page() {
    return (
        <>
            <Banner />
            <SecurityFirm />
            <Features />
            <Cybersecurity />
            <HomePageRelated />
            <OurProvenProcessSecurity />
        </>
    );
}
