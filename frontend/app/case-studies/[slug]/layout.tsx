export default function SingleCaseStudiesRootLayout({
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
