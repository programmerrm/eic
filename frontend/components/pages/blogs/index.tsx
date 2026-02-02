/* eslint-disable @typescript-eslint/no-explicit-any */
import BlogsApp from "@/components/blogsApp/blogsApp";
import StayCompliant from "@/components/stay-compliant/stay-compliant";
import { getFetchData } from "@/utils/getFetchData";

export default async function BlogsPage(jsonSchema:any) {
    const topBarData = await getFetchData('/blogs/top-bar/');
    const blogsData = await getFetchData('/blogs/list/');
    return (
        <>
            {jsonSchema && (
                <script
                    type="application/ld+json"
                    dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonSchema) }}
                />
            )}
            <BlogsApp
                topBarData={topBarData?.data}
                initialBlogs={blogsData?.results?.data || []}
                initialNext={blogsData?.next || null}
            />
            <StayCompliant />
        </>
    );
}
