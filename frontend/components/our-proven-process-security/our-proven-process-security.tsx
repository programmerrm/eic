import { getFetchData } from "@/utils/getFetchData";
import OurProvenProcessSecurityClient from "./OurProvenProcessSecurityItems";

export default async function OurProvenProcessSecurity() {
    const ourProvenProcessSecurity = await getFetchData(
        "/homepage/our-proven-process-security/",
        { tag: "our-proven-process-security-data" }
    );

    const ourProvenProcessSecurityItems = await getFetchData(
        "/homepage/our-proven-process-security-items/",
        { tag: "our-proven-process-security-items-data" }
    );

    return (
        <section className="bg-[#F4F8FB] pb-48 md:pb-[100px] pt-12 md:pt-[100px]">
            <div className="container">
                <OurProvenProcessSecurityClient
                    data={ourProvenProcessSecurity?.data}
                    items={ourProvenProcessSecurityItems || []}
                />
            </div>
        </section>
    );
}
