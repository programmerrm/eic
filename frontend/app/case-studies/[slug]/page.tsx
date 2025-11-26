import BannerImg from "../../../public/images/banner-img.svg";
import { getFetchData } from "@/utils/getFetchData";

type SinglePageProps = {
    params: Promise<{ slug: string }>;
};

export default async function SinglePage({ params }: SinglePageProps) {
    const { slug } = await params;
    const singleSuccessStories = await getFetchData(`/success-stories/single/${slug}/`);

    return (
        <>
            <section className="mt-24 md:mt-36 banner-section bg-blue [clip-path:polygon(0_0,100%_0,100%_calc(100%-50px),calc(100%-60px)_100%,0_100%)] md:[clip-path:polygon(0_0,100%_0,100%_calc(100%-100px),calc(100%-150px)_100%,0_100%)]">
                <div className="container">
                    <div className="bg-bottom bg-contain bg-no-repeat" style={{ backgroundImage: `url(${BannerImg.src})` }}>
                        <div className="max-w-[1139px] mx-auto py-10 sm:py-20 md:py-40 lg:py-[232px] text-white text-center ">
                            <h1 className="uppercase">{singleSuccessStories?.title}</h1>
                            <p className="text-base sm:text-lg md:text-2xl md:leading-8 font-spacegrotesk mt-4 sm:mt-8 max-w-[626px] mx-auto">{singleSuccessStories?.short_description}</p>
                        </div>
                    </div>
                </div>
            </section>
        </>
    );
}
