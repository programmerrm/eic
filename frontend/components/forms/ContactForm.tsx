/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { FRONTEND_API_KEY, SERVER_URL } from "@/utils/api";
import { useState } from "react";

export default function ContactForm() {
    const [loading, setLoading] = useState(false);
    const [success, setSuccess] = useState("");
    const [error, setError] = useState("");

    const handleSubmit = async (e: any) => {
        e.preventDefault();
        setLoading(true);
        setSuccess("");
        setError("");

        const formData = {
            full_name: e.target.full_name.value,
            email: e.target.email.value,
            phone_number: e.target.phone_number.value,
            company_name: e.target.company_name.value,
            message: e.target.message.value,
        };

        try {
            const res = await fetch(`${SERVER_URL}/contact/form-create/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-API-KEY": FRONTEND_API_KEY || "",
                },
                body: JSON.stringify(formData),
            });

            const data = await res.json();

            if (data.success) {
                setSuccess("Message sent successfully!");
                e.target.reset();
            } else {
                setError(data.message || "Failed to send message.");
            }
        } catch {
            setError("Something went wrong.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="space-y-3 md:space-y-6">
            <div className="flex flex-col sm:flex-row gap-3 sm:gap-10">
                <div className="sm:w-1/2">
                    <label className="text-base font-medium text-body leading-6">Full Name</label>
                    <input
                        name="full_name"
                        required
                        type="text"
                        placeholder="Ex. Hugh Steuber"
                        className="block w-full bg-white py-[13px] px-4 rounded-full mt-3 focus:outline-blue"
                    />
                </div>
                <div className="sm:w-1/2">
                    <label className="text-base font-medium text-body leading-6">Email address</label>
                    <input
                        name="email"
                        required
                        type="email"
                        placeholder="Ex. Hugh_@yahoo.com"
                        className="block w-full bg-white py-[13px] px-4 rounded-full mt-3 focus:outline-blue"
                    />
                </div>
            </div>
            <div className="flex flex-col sm:flex-row gap-3 sm:gap-10">
                <div className="sm:w-1/2">
                    <label className="text-base font-medium text-body leading-6">Phone Number</label>
                    <input
                        name="phone_number"
                        required
                        type="text"
                        placeholder="Ex. 413.625.1312"
                        className="block w-full bg-white py-[13px] px-4 rounded-full mt-3 focus:outline-blue"
                    />
                </div>
                <div className="sm:w-1/2">
                    <label className="text-base font-medium text-body leading-6">Company Name</label>
                    <input
                        name="company_name"
                        required
                        type="text"
                        placeholder="Ex. Schimmel"
                        className="block w-full bg-white py-[13px] px-4 rounded-full mt-3 focus:outline-blue"
                    />
                </div>
            </div>
            <div>
                <label className="text-base font-medium text-body leading-6">Your message</label>
                <textarea
                    name="message"
                    required
                    placeholder="How can we help you ?"
                    className="block w-full bg-white py-[13px] px-4 rounded-[10px] mt-3 min-h-[120px] focus:outline-blue"
                ></textarea>
            </div>
            {success && <p className="text-green-600">{success}</p>}
            {error && <p className="text-red-600">{error}</p>}
            <button disabled={loading} className="btn-primary group font-bold">
                {loading ? "Sending..." : "Send Message"}
                <svg
                    className="transition-all duration-500 group-hover:rotate-45 w-5 md:w-6 h-5 md:h-6"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                >
                    <path
                        stroke="currentColor"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth={1.5}
                        d="M6 18 18 6m0 0H9m9 0v9"
                    />
                </svg>
            </button>
        </form>
    );
}
