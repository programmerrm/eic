import type { NextConfig } from "next";

const nextConfig: NextConfig = {
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



// images: {
//   remotePatterns: [
//     {
//       protocol: 'http',
//       hostname: '127.0.0.1',
//       port: '8000',
//       pathname: '/media/**',
//     },
//     {
//       protocol: 'http',
//       hostname: 'localhost',
//       port: '8000',
//       pathname: '/media/**',
//     },
//   ],
//   unoptimized: true,
// },