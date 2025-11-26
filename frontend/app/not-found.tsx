import Image from "next/image";
import { MEDIA_URL } from "../utils/api";
import { getFetchData } from "../utils/getFetchData";
import NotFoundImg from "../public/images/not-found.svg";

export default async function NotFound() {
    const not_found_data = await getFetchData('/configuration/not-found-content/');
    return (
        <section className="error-section">
            <div className="container">
                <div className="error-image">
                    {not_found_data?.data?.image ? (
                        <Image
                            src={`${MEDIA_URL}${not_found_data?.data?.image}`}
                            alt="not-found-icon"
                            width={302}
                            height={300}
                        />
                    ) : (
                        <Image
                            src={NotFoundImg}
                            alt="not-found-icon"
                            width={302}
                            height={300}
                        />
                    )}
                </div>
                <div className="error-content">
                    <h4>{not_found_data?.data?.title || "Oops! This page has gone missing."}</h4>
                    <p>{not_found_data?.data?.description || "Uh-oh! This page doesn't exist. It might’ve moved or been deleted. Head to our homepage or explore below!"}</p>
                </div>
            </div>
        </section>
    );
}
