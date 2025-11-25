import SectionBanner from "../../components/banner/section-banner";
import Compliance from "../../components/compliance/compliance";
import Features from "../../components/features/features";
import Services from "../../components/services/services";
import StayCompliant from "../../components/stay-compliant/stay-compliant";
import { getFetchData } from "../../utils/getFetchData";

export default async function Page() {
    const topBarFetchData = await getFetchData('/services/top-bar/');
    const topBar = topBarFetchData[0];
    return (
        <>
            <SectionBanner topBarData={topBar} />
            <Services />
            <Features />
            <Compliance />
            <StayCompliant />
        </>
    );
}
