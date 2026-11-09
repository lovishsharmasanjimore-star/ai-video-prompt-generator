"""Turn a plain-text story into structured image and video prompt briefs."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable


def split_scenes(story: str) -> list[str]:
    """Split story text on blank lines and remove simple scene labels."""
    chunks = re.split(r"\n\s*\n+", story.strip())
    scenes = []
    for chunk in chunks:
        cleaned = re.sub(r"^\s*(?:scene\s*)?\d+\s*[:.-]\s*", "", chunk.strip(), flags=re.I)
        if cleaned:
            scenes.append(cleaned)
    return scenes


def build_prompt(scene: str, index: int, style: str = "cinematic 3D animated film") -> dict:
    """Create editable prompt briefs; no external AI service is called."""
    image_prompt = (
        f"{style}. Scene {index}: {scene} "
        "Show one clear focal subject, expressive composition, detailed environment, "
        "coherent anatomy, cinematic lighting, depth of field, high visual clarity."
    )
    video_prompt = (
        f"Animate scene {index}: {scene} "
        "Use natural continuous motion, consistent character appearance, subtle camera "
        "movement, physically plausible actions, and preserve the scene composition."
    )
    return {
        "scene_number": index,
        "scene_text": scene,
        "image_prompt": image_prompt,
        "video_prompt": video_prompt,
        "duration_seconds": 8,
    }


def generate(story: str, style: str = "cinematic 3D animated film") -> list[dict]:
    return [build_prompt(scene, i, style) for i, scene in enumerate(split_scenes(story), start=1)]


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate structured image/video prompt briefs from a story.")
    parser.add_argument("input", type=Path, help="Path to a UTF-8 story text file")
    parser.add_argument("--output", type=Path, default=Path("prompts.json"), help="Output JSON path")
    parser.add_argument("--style", default="cinematic 3D animated film", help="Visual style phrase")
    args = parser.parse_args(argv)

    story = args.input.read_text(encoding="utf-8")
    prompts = generate(story, args.style)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(prompts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Created {len(prompts)} scene prompt(s): {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
