import Link from "next/link";
import BannerImg from "../../public/images/banner-img.svg";

export default async function TermsConditions() {
    return (
        <>
            <section
                className="mt-24 md:mt-36 banner-section bg-blue [clip-path:polygon(0_0,100%_0,100%_calc(100%-50px),calc(100%-60px)_100%,0_100%)] md:[clip-path:polygon(0_0,100%_0,100%_calc(100%-100px),calc(100%-150px)_100%,0_100%)]">
                <div className="container">
                    <div className="bg-bottom bg-contain bg-no-repeat" style={{
                        backgroundImage: `url(${BannerImg.src})`,
                    }}>
                        <div className="max-w-[1190px] mx-auto py-10 sm:py-20 md:py-40 lg:py-[232px] text-white text-center ">
                            <h1 className="uppercase">Terms & Conditions</h1>
                            <p className="text-base sm:text-lg md:text-2xl md:leading-8 font-spacegrotesk mt-2 sm:mt-4 max-w-[626px] mx-auto">EIC the digital world by delivering innovative security solutions & promoting cybersecurity awareness.</p>
                        </div>
                    </div>
                </div>
            </section>
            <section className="py-12 md:py-[100px]">
                <div className="container">
                    <div className="p-6 md:p-[60px] border-2 border-[#C0D9EB] rounded-2xl shadow-[41px_82px_37px_rgba(150,150,150,0.01),23px_46px_31px_rgba(150,150,150,0.05),10px_21px_23px_rgba(150,150,150,0.09),3px_5px_13px_rgba(150,150,150,0.1)]">
                        <div className="border-b-2 border-[#C0D9EB] pb-6">
                            <h2 className="mb-3 sm:mb-4">Terms & Conditions</h2>
                            <p>Last updated: 25/11/2024</p>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>1. Acceptance of Terms</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">Welcome to EIC – Enterprise Intelligence & Cybersecurity (“we,” “us,” “our”). By accessing or using our website or services, you agree to be bound by the following Terms and Conditions. Please read them carefully.</p>
                            <p>By using our website and services, you agree to comply with and be legally bound by these Terms. If you do not agree, please do not use our site or services.</p>
                            <ul className="mt-4">
                                <li className="list-disc ml-6">Provide accurate, up-to-date information when using our service</li>
                                <li className="list-disc ml-6">Not misuse our services in any way that could harm our company or others</li>
                                <li className="list-disc ml-6">Maintain the confidentiality of any login credentials or access provided</li>
                            </ul>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>2. User Responsibilities</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">Lorem ipsum dolor sit amet consectetur. Id dictum rutrum eget nulla tristique id viverra. Donec massa ut morbi enim. Fermentum nunc ultricies ornare lacus ipsum aliquam ultrices. Morbi non orci lacus malesuada interdum quisque ornare eros. Aliquam senectus ullamcorper fringilla tincidunt sed eget imperdiet. Ornare blandit lacus risus in magnis elementum elementum et. Est cras id quis quis vitae enim. Aliquam cursus faucibus vestibulum erat nulla. Auctor montes duis nisl vel.</p>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>3. Intellectual Property</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">All content on this website — including text, images, logos, graphics, and documentation — is the property of EIC or its licensors. You may not copy, distribute, or reproduce any content without prior written permission.</p>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>4. Limitation of Liability</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">EIC will not be held liable for any direct, indirect, incidental, or consequential damages arising fro</p>
                            <ul>
                                <li className="list-disc ml-6">Use or misuse of our website or services</li>
                                <li className="list-disc ml-6">Delays in service delivery</li>
                                <li className="list-disc ml-6">Security breaches that occur beyond our contractual scope</li>
                            </ul>
                            <p>Our liability is limited to the amount paid for services rendered.</p>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>5. Confidentiality</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">We uphold strict confidentiality with client data. All data shared during assessments, audits, or consultations is handled according to cybersecurity industry best practices and relevant laws.</p>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>6. Third-Party Tools & Links</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">Our platform may integrate external services for enhanced functionality. EIC is not liable for the data practices, security protocols, or performance of these third-party entities. Users should review the privacy policies and terms of service of any third-party services before use. Use of these links and tools is at your own discretion. EIC disclaims all responsibility for any issues arising from third-party usage.</p>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>7. Termination</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">At EIC Solutions, we reserve the right to terminate or suspend your access to our services under certain circumstances. These include violations of our service policies, suspected fraudulent activities, or when legal mandates require such action. We are committed to providing notice to our users whenever feasible, ensuring transparency and understanding. Our aim is to maintain a secure and compliant environment for all users, and we appreciate your cooperation in adhering to our terms. For any queries or concerns regarding termination or suspension, please contact our support team for clarification.Thank you for your understanding and continued trust in Cynergy Solutions.</p>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>8. Governing Law</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">These Terms and Conditions are subject to the laws of the Republic of Eldoria, without regard to its conflict of law principles. Any legal claims related to these Terms must be resolved in the courts of New Aethel, Eldoria. By using our services, you submit to the jurisdiction and venue of these courts, waiving any objections. This ensures a clear, consistent legal framework for all users of EIC.</p>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>9. Changes to Terms</h4>
                            <p className="mt-4 sm:mt-6 mb-5 sm:mb-8">We reserve the right to update these Terms at any time. Changes will be effective immediately upon posting. We recommend checking this page regularly.</p>
                        </div>
                        <div className="mt-5 md:mt-10">
                            <h4>10. Contact Information</h4>
                            <p className="mt-6">If you have any questions about these Terms, please contact us at:</p>
                            <p >Email: <Link href="mailto:info@eic.com.bd">info@eic.com.bd</Link></p>
                            <p>Office: House No-15, Road No- 7, Block- C, Gulshan, Niketon, Dhaka-1212.</p>
                            <p>Phone: <Link href="tel:+8809617204204">+8809617204204</Link> <a href="tel:+880241082448">+880241082448</a></p>
                        </div>
                    </div>
                </div>
            </section>
        </>
    );
}
