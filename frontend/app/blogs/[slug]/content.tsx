"use client"; 

interface BlogContentProps {
    content: string;
}

export default function BlogContent({ content }: BlogContentProps) {
    if (!content) return null;

    return (
        <div
            className="space-y-5 lg:space-y-8"
            dangerouslySetInnerHTML={{ __html: content }}
        ></div>
    );
}
