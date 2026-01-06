"use client";

import Image from "next/image";
import { useEffect, useRef, useState } from "react";

type Data = {
  title_before_span?: string;
  title_span?: string;
  title_after_span?: string;
  description?: string;
  image?: string;
};

type Item = {
  id: number | string;
  image: string;
  title: string;
  description: string;
};

export default function OurProvenProcessSecurityClient({
  data,
  items,
}: {
  data: Data;
  items: Item[];
}) {
  const [activeImage, setActiveImage] = useState<string | null>(null);
  const itemRefs = useRef<(HTMLDivElement | null)[]>([]);
  const parentSectionRef = useRef<HTMLElement | null>(null);

  useEffect(() => {
    if (typeof window === "undefined") return;

    const handleScroll = () => {
      if (!parentSectionRef.current) return;

      const sectionTop = parentSectionRef.current.getBoundingClientRect().top;
      const sectionBottom = parentSectionRef.current.getBoundingClientRect().bottom;
      const viewportHeight = window.innerHeight;

      // Parent section viewport-এ visible হলে
      if (sectionTop < viewportHeight && sectionBottom > 0) {
        const viewportCenter = viewportHeight / 2;

        // Right items-এ loop
        for (let i = 0; i < itemRefs.current.length; i++) {
          const el = itemRefs.current[i];
          if (!el) continue;

          const rect = el.getBoundingClientRect();

          // Item viewport center এ এলে active
          if (rect.top <= viewportCenter && rect.bottom >= viewportCenter) {
            setActiveImage(items[i].image);
            break;
          }
        }
      }
    };

    window.addEventListener("scroll", handleScroll);
    handleScroll(); // Initial check

    return () => window.removeEventListener("scroll", handleScroll);
  }, [items]);

  return (
    <section ref={parentSectionRef} className="relative lg:h-[130vh]">
      <div className="flex flex-col lg:flex-row justify-between gap-10">

        {/* LEFT SIDE — STICKY */}
        <div className="lg:sticky top-28 self-start h-fit w-full max-w-120 mx-auto lg:mx-0 text-center lg:text-start flex flex-col items-center lg:items-start">
          <h2 className="mb-3 lg:mb-6">
            {data?.title_before_span}{" "}
            <span className="text-blue">{data?.title_span}</span>{" "}
            {data?.title_after_span}
          </h2>

          <p className="mb-6 lg:mb-11">{data?.description}</p>

          <div className="proven-icon-wrap max-w-120 lg:max-w-full relative">
            {data?.image && activeImage && (
              <>
                <Image
                  src={data.image}
                  alt="Our Proven Security"
                  width={345}
                  height={345}
                  className="circle"
                  priority
                />

                <div className="bg-white rounded-full p-5 circle-icon w-full max-w-24 lg:max-w-37.25 absolute top-0 left-0">
                  <Image
                    key={activeImage}
                    src={activeImage}
                    alt="Active Process"
                    width={142}
                    height={142}
                    className="transition-opacity duration-500 ease-in-out opacity-100"
                    priority
                  />
                </div>
              </>
            )}
          </div>
        </div>

        {/* RIGHT SIDE — NORMAL CONTENT */}
        <div className="w-full max-w-111 mx-auto lg:mx-0">
          {items.map((item, index) => (
            <div
              key={item.id}
    ref={(el) => {
      itemRefs.current[index] = el;
    }}

              data-image={item.image}
              className="text-center lg:text-start flex flex-col items-center lg:items-start mb-8 lg:mb-14 last:mb-0"
            >
              <div className="mb-2 lg:mb-4.5 max-w-20">
                <Image
                  src={item.image}
                  alt={item.title}
                  width={100}
                  height={106}
                />
              </div>

              <h3 className="mb-2 lg:mb-4">{item.title}</h3>
              <p>{item.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
