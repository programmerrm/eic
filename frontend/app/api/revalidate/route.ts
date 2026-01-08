/* eslint-disable @typescript-eslint/no-explicit-any */
import { NextResponse } from "next/server";
import { revalidatePath, revalidateTag } from "next/cache";
import { REVALIDATE_SECRET } from "@/utils/api";

export async function GET(request: Request) {
    const url = new URL(request.url);

    const secret = url.searchParams.get("secret");
    const path = url.searchParams.get("path");
    const tag = url.searchParams.get("tag");

    if (secret !== REVALIDATE_SECRET) {
        return NextResponse.json({ message: "Invalid token" }, { status: 401 });
    }

    try {
        if (tag) {
            revalidateTag(tag, "default");
        }

        if (path) {
            revalidatePath(path);
        }

        return NextResponse.json({
            revalidated: true,
            tag,
            path,
        });
    } catch (error: any) {
        return NextResponse.json(
            { error: error.message },
            { status: 500 }
        );
    }
}
