import Image from "next/image";

export default function SingleService() {
    return (
        <div className="border-2 border-[#EBF3F8] rounded-[10px] shadow-3xl bg-bottom bg-contain bg-no-repeat"
            style="background-image: url(./src/assets/image/commitment-item-bg.png);">
            <div className="p-8 pb-10">
                <div className="pr-7">
                    <h3>Client-centric Approach</h3>
                    <p className="text-base font-medium leading-6 mt-4">Compliance solutions are customized to address unique
                        needs while ensuring regulatory adherence.</p>
                </div>
                <div className="flex items-center justify-center mt-[30px]">
                    <div>
                        <Image src="./src/assets/image/client.png" alt="client" />
                    </div>
                </div>
            </div>
        </div>
    );
}
