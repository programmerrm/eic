import "./globals.css";
import {
  DM_Sans,
  Inter,
  Lexend,
  Poppins,
  Roboto,
  Space_Grotesk,
} from "next/font/google";
import Header from "@/components/header/header";
import Footer from "@/components/footer/footer";
import ScrollTopBottom from "@/components/scroll/scrollTopBottom";
import Head from "next/head";
export const dynamic = 'force-dynamic';

const dmSans = DM_Sans({
  subsets: ["latin"],
  variable: "--font-dmsans",
});

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
});

const poppins = Poppins({
  subsets: ["latin"],
  weight: ["100", "200", "300", "400", "500", "600", "700", "800", "900"],
  variable: "--font-poppins",
});

const roboto = Roboto({
  subsets: ["latin"],
  weight: ["100", "300", "400", "500", "700", "900"],
  variable: "--font-roboto",
});

const lexend = Lexend({
  subsets: ["latin"],
  weight: ["100", "200", "300", "400", "500", "600", "700", "800", "900"],
  variable: "--font-lexend",
});

const spaceGrotesk = Space_Grotesk({
  subsets: ["latin"],
  weight: ["300", "400", "500", "600", "700"],
  variable: "--font-spacegrotesk",
});

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html
      lang="en"
      className={`
        ${dmSans.variable}
        ${inter.variable}
        ${poppins.variable}
        ${roboto.variable}
        ${lexend.variable}
        ${spaceGrotesk.variable}
      `}
    >
      <Head>
        <link rel="icon" href="/favicon.ico" sizes="any" />
        <link rel="icon" href="/favicon-16x16.png" sizes="16x16" type="image/png" />
        <link rel="icon" href="/favicon-32x32.png" sizes="32x32" type="image/png" />
        <link rel="icon" href="/android-chrome-192x192.png" sizes="192x192" type="image/png" />
        <link rel="icon" href="/android-chrome-512x512.png" sizes="512x512" type="image/png" />
        <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
        <link rel="apple-touch-icon" sizes="152x152" href="/apple-touch-icon-152x152.png" />
        <link rel="apple-touch-icon" sizes="167x167" href="/apple-touch-icon-167x167.png" />
        <link rel="manifest" href="/site.webmanifest" />
      </Head>
      <body suppressHydrationWarning={true}>
        <ScrollTopBottom />
        <Header />
        {children}
        <Footer />
      </body>
    </html>
  );
}
