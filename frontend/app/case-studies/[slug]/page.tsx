import { getFetchData } from "@/utils/getFetchData";

type SinglePageProps = {
    params: Promise<{ slug: string }>;
};

export default async function SinglePage({ params }: SinglePageProps) {
    const { slug } = await params;
    const singleBlog = await getFetchData(`/success-stories/single/${slug}/`);

    console.log('singleBlog -- ', singleBlog);

    return (
        <>
            
        </>
    );
}
