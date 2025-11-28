/* eslint-disable @typescript-eslint/no-explicit-any */
import { NextResponse } from "next/server";
import { revalidateTag, revalidatePath } from "next/cache";
import { REVALIDATE_SECRET } from "@/utils/api";

export async function POST(req: Request) {
  try {
    let body: any = {};
    try {
      body = await req.json();
    } catch {
      body = {};
    }

    const secret = body?.secret;

    if (secret !== REVALIDATE_SECRET) {
      return NextResponse.json(
        { message: "Invalid token" },
        { status: 401 }
      );
    }

    const tags: string[] = body?.tags || [];
    const paths: string[] = body?.paths || [];

    if (Array.isArray(tags) && tags.length > 0) {
      tags.forEach((tag) => {
        revalidateTag(tag, "max");
      });
    }

    if (Array.isArray(paths) && paths.length > 0) {
      paths.forEach((path) => {
        revalidatePath(path);
      });
    }

    return NextResponse.json({
      revalidated: true,
      tags,
      paths,
    });
  } catch (error) {
    console.error("Revalidate error:", error);
    return NextResponse.json(
      { message: "Error revalidating", error: String(error) },
      { status: 500 }
    );
  }
}
