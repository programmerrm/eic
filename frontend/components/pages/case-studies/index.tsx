/* eslint-disable @typescript-eslint/no-explicit-any */
import CaseStudies from "@/components/case-studies/case-studies";
import { getFetchData } from "@/utils/getFetchData";

export default async function CaseStudiesPage(jsonSchema:any) {
    const itemsData = await getFetchData('/success-stories/list/');
    const topBarData = await getFetchData('/success-stories/top-bar/');
    return (
        <>
            {jsonSchema && (
                <script
                    type="application/ld+json"
                    dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonSchema) }}
                />
            )}
            <CaseStudies
                topBarData={topBarData?.data}
                initialItem={itemsData?.results?.data || []}
                initialNext={itemsData?.next || null}
            />
        </>
    );
}