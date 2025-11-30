import Image from "next/image";
import NotFoundImg from "@/public/images/not-found.svg";
import { getFetchData } from "@/utils/getFetchData";
import { MEDIA_URL } from "@/utils/api";

export default async function NotFound() {
    const notFoundData = await getFetchData('/configuration/not-found-content/', {
        tag: 'not-found-content-data',
    });
    return (
        <section className="error-section">
            <div className="container">
                <div className="error-image">
                    <Image
                        src={`${MEDIA_URL}${notFoundData?.data?.image}` || NotFoundImg}
                        alt="not-found-icon"
                        width={302}
                        height={300}
                    />
                </div>
                <div className="error-content">
                    <h4>{notFoundData?.data?.title || "Oops! This page has gone missing."}</h4>
                    <p>{notFoundData?.data?.description || "Uh-oh! This page does exist. It might have moved or been deleted. Head to our homepage or explore below!"}</p>
                </div>
            </div>
        </section>
    );
}
