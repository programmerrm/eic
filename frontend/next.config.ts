import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  turbopack: {
    root: __dirname,
  },
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "eicsec.com",
        pathname: "/media/**",
      },
      {
        protocol: "https",
        hostname: "eic.com.bd",
        pathname: "/media/**",
      },
    ],
  },
};

export default nextConfig;
