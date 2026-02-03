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
  compiler: {
    removeConsole: process.env.NODE_ENV === 'production',
  },
};

export default nextConfig;
