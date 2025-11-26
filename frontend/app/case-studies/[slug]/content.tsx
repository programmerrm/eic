"use client"; 

interface CaseStudiesContentProps {
    content: string;
}

export default function CaseStudiesContent({ content }: CaseStudiesContentProps) {
    if (!content) return null;
    return <div className="mt-6 md:mt-12 space-y-5 lg:space-y-8" dangerouslySetInnerHTML={{ __html: content }}></div>
}
