/* eslint-disable @typescript-eslint/no-explicit-any */

export default function Description({ content }: any) {
    return <p className="text-base sm:text-xl md:text-2xl md:leading-8 mt-2 sm:mt-3 mb-3 sm:mb-6 w-full lg:w-[400px] xl:w-[555px]" dangerouslySetInnerHTML={{ __html: content }}></p>
}
