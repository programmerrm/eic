/* eslint-disable react-hooks/exhaustive-deps */
"use client";

import Image from "next/image";
import CoreImg from "../../public/images/core-principles.svg";
import { useEffect, useRef, useState } from "react";

export default function Core() {
  const sectionRef = useRef(null);
  const [isInView, setIsInView] = useState(false);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsInView(true);
          observer.unobserve(entry.target);
        }
      },
      { threshold: 0.1 }
    );

    if (sectionRef.current) {
      observer.observe(sectionRef.current);
    }

    return () => {
      if (sectionRef.current) observer.unobserve(sectionRef.current);
    };
  }, []);

  return (
    <section className="bg-white py-12 md:py-25 relative" ref={sectionRef}>
      <div className="container">
        <h2 className="text-center sm:-mb-20">
          The <span className="text-blue">Core Principles</span> We Uphold
        </h2>
        <div className="flex items-center justify-center">
          {isInView && (
            <Image
              src={CoreImg}
              alt="core"
              width={844}
              height={296}
              priority
              fetchPriority="high"
            />
          )}
        </div>
      </div>
    </section>
  );
}
