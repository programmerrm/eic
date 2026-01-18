import { Metadata } from "next";

export const metadata: Metadata = {
    title: "Eic Services Page",
    description: "Create your Services page",
    alternates: {
        canonical: "https://eic.com.bd/services/",
    },
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <main>
            {children}
        </main>
    );
}