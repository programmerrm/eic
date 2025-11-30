import CaseStudiesPage from "@/components/case-studies-page/case-studies-page";
import { getFetchData } from "@/utils/getFetchData";

export default async function Page() {
    const itemsData = await getFetchData('/success-stories/list/');
    const topBarData = await getFetchData('/success-stories/top-bar/');
    return (
        <>
            <CaseStudiesPage 
                topBarData={topBarData?.data}
                initialItem={itemsData?.results?.data || []}
                initialNext={itemsData?.next || null}
            />
        </>
    );
}