export default function SingleBlogRootLayout({
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
