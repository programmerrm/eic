import StayCompliant from "@/components/stay-compliant/stay-compliant";
import { getFetchData } from "../../utils/getFetchData";
import BlogsPage from "@/components/blogsPage/blogsPage";

export default async function Page() {
    const schemaData = await getFetchData('/blogs/schema/');
    const jsonLd = schemaData?.data?.json_ld ? JSON.parse(schemaData.data.json_ld) : null;
    const topBarData = await getFetchData('/blogs/top-bar/');
    const blogsData = await getFetchData('/blogs/list/');
    return (
        <>
            <BlogsPage
                topBarData={topBarData?.data}
                initialBlogs={blogsData?.results?.data || []}
                initialNext={blogsData?.next || null}
                jsonLd={jsonLd}
            />
            <StayCompliant />
        </>
    );
}
