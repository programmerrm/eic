import BannerImg from "../../public/images/banner-img.svg";

export default function PrivacyPolicy() {
    return (
        <>
            <section
                className="mt-24 md:mt-36 banner-section bg-blue [clip-path:polygon(0_0,100%_0,100%_calc(100%-50px),calc(100%-60px)_100%,0_100%)] md:[clip-path:polygon(0_0,100%_0,100%_calc(100%-100px),calc(100%-150px)_100%,0_100%)]">
                <div className="container">
                    <div className="bg-bottom bg-contain bg-no-repeat" style={{
                        backgroundImage: `url(${BannerImg.src})`,
                    }}>
                        <div className="max-w-[1190px] mx-auto py-10 sm:py-20 md:py-40 lg:py-[232px] text-white text-center ">
                            <h1 className="uppercase">Privacy Policy</h1>
                            <p className="text-base sm:text-lg md:text-2xl md:leading-8 font-spacegrotesk mt-2 sm:mt-4 max-w-[626px] mx-auto">EIC the digital world by delivering innovative security solutions & promoting cybersecurity awareness.</p>
                        </div>
                    </div>
                </div>
            </section>
            <section className="py-12 md:py-[100px]">
                <div className="container">
                    <div className="p-6 md:p-[60px] border-2 border-[#C0D9EB] rounded-2xl shadow-[41px_82px_37px_rgba(150,150,150,0.01),23px_46px_31px_rgba(150,150,150,0.05),10px_21px_23px_rgba(150,150,150,0.09),3px_5px_13px_rgba(150,150,150,0.1)]">
                        <div className="border-b-2 border-[#C0D9EB] pb-6">
                            <h2 className="mb-3 sm:mb-4">Privacy Policy of EIC</h2>
                            <p>Last updated: 25/11/2024</p>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>1. Information We Collect</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">At EIC – Enterprise Intelligence & Cybersecurity (“EIC,” “we,” “us,” or “our”), we are committed to protecting your privacy. This Privacy Policy explains how we collect, use, store, and protect your personal information when you visit our website or use our services.</p>
                            <h5 className="text-lg text-body font-bold font-dmsans">a. Personal Information</h5>
                            <ul>
                                <li className="list-disc ml-8">Name</li>
                                <li className="list-disc ml-8">Email address</li>
                                <li className="list-disc ml-8">Phone number</li>
                                <li className="list-disc ml-8">Company name</li>
                                <li className="list-disc ml-8">Job title</li>
                                <li className="list-disc ml-8">Billing information (for paid services)</li>
                            </ul>
                            <h5 className="text-lg text-body font-bold font-dmsans mt-8">b. Technical Information</h5>
                            <ul>
                                <li className="list-disc ml-8">IP address</li>
                                <li className="list-disc ml-8">Browser type</li>
                                <li className="list-disc ml-8">Device type</li>
                                <li className="list-disc ml-8">Company name</li>
                                <li className="list-disc ml-8">Pages visited</li>
                                <li className="list-disc ml-8">Date and time of visit</li>
                            </ul>


                            <h5 className="text-lg text-body font-bold font-dmsans mt-8">c. Information Through Forms</h5>
                            <ul>
                                <li className="list-disc ml-8">Details submitted via contact forms, consultation requests, or quote forms</li>
                            </ul>
                        </div>

                        <div className="mt-5 md:mt-10">
                            <h4>2. How We Use Your Information</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">We use your information to:</p>
                            <ul>
                                <li className="list-disc ml-8">Respond to inquiries and support requests</li>
                                <li className="list-disc ml-8">Provide cybersecurity services and assessments</li>
                                <li className="list-disc ml-8">Improve our website performance and security</li>
                                <li className="list-disc ml-8">Send service-related updates, reports, or newsletters (with your consent)</li>
                                <li className="list-disc ml-8">Fulfill legal or regulatory obligations (e.g., audits, compliance)</li>
                            </ul>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>3. How We Share Your Information</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">We do not sell or rent your personal data. We may share it with:</p>
                            <ul>
                                <li className="list-disc ml-8">Authorized team members for service delivery</li>
                                <li className="list-disc ml-8">Trusted third-party providers (e.g., hosting, analytics) under strict confidentiality</li>
                                <li className="list-disc ml-8">Legal or regulatory authorities when required by law</li>
                            </ul>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>4. Data Retention</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">We retain personal data only for as long as necessary to:</p>
                            <ul>
                                <li className="list-disc ml-8">Deliver services</li>
                                <li className="list-disc ml-8">Comply with legal or contractual obligations</li>
                                <li className="list-disc ml-8">Maintain business and security records</li>
                            </ul>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>5. Cookies & Tracking</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">We use cookies and similar technologies to:</p>

                            <ul>
                                <li className="list-disc ml-8">Analyze website usage</li>
                                <li className="list-disc ml-8">Improve site performance</li>
                                <li className="list-disc ml-8">Enhance user experience</li>
                            </ul>
                            <p className="mt-4 sm:mt-6">You can control or disable cookies through your browser settings. Note: some features may not function properly without cookies</p>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>6. Your Rights</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">Depending on your location (e.g., GDPR or CCPA jurisdictions), you have the right to:</p>
                            <ul>
                                <li className="list-disc ml-8">Access your data</li>
                                <li className="list-disc ml-8">Request correction or deletion</li>
                                <li className="list-disc ml-8">Withdraw consent</li>
                                <li className="list-disc ml-8">Request data portability</li>
                                <li className="list-disc ml-8">Lodge a complaint with a data protection authority</li>
                            </ul>
                            <p className="mt-6">To exercise these rights, contact us at info@eic.com.bd</p>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>7. Security Measures</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">As a cybersecurity company, your data security is our top priority. <br />
                                We use encryption, firewalls, intrusion detection systems, and access control policies to protect your data. However, no method of online transmission is 100% secure.</p>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>8. Third-Party Links</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">Our website may contain links to third-party websites or tools. We are not responsible for their privacy practices or content. Please review their privacy policies separately.</p>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>9. Changes to This Policy</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">We may update this Privacy Policy from time to time. Updates will be posted on this page with a new “Last Updated” date. We encourage you to review this page periodically.</p>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>10. Contact Information</h4>
                            <p className="mt-6">If you have any questions about these Terms, please contact us at:</p>
                            <p >Email: <a href="mailto:info@eic.com.bd">info@eic.com.bd</a></p>
                            <p>Office: House No-15, Road No- 7, Block- C, Gulshan, Niketon, Dhaka-1212.</p>
                            <p>Phone: <a href="tel:+8809617204204">+8809617204204</a> <a href="tel:+880241082448">+880241082448</a></p>
                        </div>
                    </div>
                </div>
            </section>
        </>
    );
} 