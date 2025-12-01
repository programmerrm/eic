import Image from "next/image";
import NotFoundImg from "@/public/images/404.svg";

export default function NotFound() {
    return (
        <section className="error-section">
            <div className="container">
                <div className="error-image">
                    <Image
                        src={NotFoundImg}
                        alt="not-found-icon"
                        width={302}
                        height={300}
                        priority 
                        fetchPriority="high"
                    />
                </div>
                <div className="error-content">
                    <h4>Oops! This page has gone missing.</h4>
                    <p>
                        Uh-oh! This page does exist. It might have moved or been
                        deleted. Head to our homepage or explore below!
                    </p>
                </div>
            </div>
        </section>
    );
}
