import Image from "next/image";
import { MEDIA_URL } from "../utils/api";
import { getFetchData } from "../utils/getFetchData";

export default async function NotFound() {
    const not_found_data = await getFetchData('/configuration/not-found-content/');
    return (
        <section className="error-section">
            <div className="container">
                <div className="error-image">
                    <Image
                        width={302}
                        height={300}
                        src={`${MEDIA_URL}${not_found_data?.data?.image}`}
                        alt="not-found-icon"
                    />
                </div>
                <div className="error-content">
                    <h4>{not_found_data?.data?.title}</h4>
                    <p>{not_found_data?.data?.description}</p>
                </div>
            </div>
        </section>
    );
}
