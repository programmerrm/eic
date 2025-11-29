/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useState } from "react";

export default function SubscribeForm() {
    const [email, setEmail] = useState("");
    const [loading, setLoading] = useState(false);
    const [success, setSuccess] = useState("");
    const [error, setError] = useState("");

    const handleSubmit = async (e: any) => {
        e.preventDefault();
        setLoading(true);
        setSuccess("");
        setError("");

        try {
            const res = await fetch(`https://eicsec.com/api/v1/configuration/subscribe/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ email }),
            });
            const data = await res.json();
            if (res.ok && data.success) {
                setSuccess("Subscribe form has been submitted successfully.");
                setEmail("");
            } else {
                setError(data.message || "Failed to submit.");
            }
        } catch {
            setError("Something went wrong.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="mt-6">
            <div className="flex items-center gap-1">
                <input
                    className="bg-white rounded-full focus:outline-0 text-sm leading-3.5 font-roboto py-[13px] px-4 text-[#142149] w-full max-w-[241px] placeholder:text-[#142149] focus:outline-blue"
                    type="email"
                    required
                    placeholder="Enter your email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <button
                    className="text-base font-roboto font-medium leading-4 px-6 py-3 rounded-full bg-blue disabled:opacity-60 cursor-pointer"
                    type="submit"
                    disabled={loading}
                >
                    {loading ? "Submitting..." : "Submit"}
                </button>
            </div>
            {success && <p className="text-green-600 mt-2">{success}</p>}
            {error && <p className="text-red-600 mt-2">{error}</p>}
        </form>
    );
}
