import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Photographs are served as the original files the design was rendered from. Next's re-encoding
  // (WebP, quality 75) changes every pixel of every photo, which the visual test would count as a difference.
  images: { unoptimized: true },
};

export default nextConfig;
