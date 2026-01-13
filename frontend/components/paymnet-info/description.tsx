/* eslint-disable @typescript-eslint/no-explicit-any */

export default function Description({ content }: any) {
    if (!content) return null;
    return <p className="text-[#525666] text-base sm:text-lg xl:text-xl 2xl:text-2xl md:leading-8 mt-2 sm:mt-3 mb-3 sm:mb-6 w-full lg:w-[450px] xl:w-[480px] 2xl:w-[555px]" dangerouslySetInnerHTML={{ __html: content }}></p>
}
