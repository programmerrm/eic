/* eslint-disable @typescript-eslint/no-explicit-any */
import { REVALIDATE_SECRET } from "@/utils/api";
import { NextResponse } from "next/server";

export async function GET(request: Request) {
    const url = new URL(request.url);
    const secret = url.searchParams.get("secret");
    const path = url.searchParams.get("path");

    if (secret !== REVALIDATE_SECRET) {
        return NextResponse.json({ message: "Invalid token" }, { status: 401 });
    }

    try {
        if (typeof path === "string") {
            const { revalidatePath } = await import("next/cache");
            revalidatePath(path);
            return NextResponse.json({ revalidated: true });
        }
        return NextResponse.json({ message: "No path provided" }, { status: 400 });
    } catch (error: any) {
        console.error("Revalidate error:", error);
        return NextResponse.json({ error: error.message }, { status: 500 });
    }
}
