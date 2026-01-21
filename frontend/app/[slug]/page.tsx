type SlugProps = {
    params: { slug: string };
};

export default async function Page({ params }: SlugProps) {
    const { slug } = await params;
    return (
        <div>
            <h2>{slug}</h2>
        </div>
    );
}
