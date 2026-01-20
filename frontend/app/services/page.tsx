import SectionBanner from "../../components/banner/section-banner";
import Compliance from "../../components/compliance/compliance";
import Features from "../../components/features/features";
import Services from "../../components/services/services";
import StayCompliant from "../../components/stay-compliant/stay-compliant";
import { getFetchData } from "@/utils/getFetchData";

export default async function Page() {
    const topBarFetchData = await getFetchData('/services/top-bar/');
    const schemaData = await getFetchData('/services/schema/');
    const jsonLd = JSON.parse(schemaData.data.schema);

    return (
        <>
        {jsonLd && (
                <script
                    type="application/ld+json"
                    dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
                />
            )}
            <SectionBanner topBarData={topBarFetchData?.data} />
            <Services />
            <Features />
            <Compliance />
            <StayCompliant />
        </>
    );
}
