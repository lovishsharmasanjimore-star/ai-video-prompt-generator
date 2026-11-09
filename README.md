# AI Video Prompt Generator

A small Python CLI that converts a story or scene description into structured image-generation and image-to-video prompt briefs.

## What it does
- Splits a story into scenes using blank lines or numbered scene headings.
- Builds consistent prompt briefs with subject, action, setting, camera, lighting, style, and motion fields.
- Exports the result as JSON for use in your preferred image/video generation tools.

## What it does not do
This starter project does not call an AI API, generate images/videos, create voiceovers, or upload to YouTube. It prepares structured prompts that can be edited and pasted into those tools.

## Requirements
- Python 3.10+

## Run
```bash
python src/prompt_generator.py examples/story.txt --output output/prompts.json
```

## Test
```bash
python -m unittest discover -s tests
```

## Output
The JSON contains one object per scene, with `image_prompt` and `video_prompt` fields. Edit `src/prompt_generator.py` to customize the prompt template for your workflow.
