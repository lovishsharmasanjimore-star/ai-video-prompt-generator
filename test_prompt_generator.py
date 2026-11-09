import unittest

from src.prompt_generator import generate, split_scenes


class PromptGeneratorTests(unittest.TestCase):
    def test_split_scenes(self):
        self.assertEqual(split_scenes("Scene 1: First.\n\nScene 2: Second."), ["First.", "Second."])

    def test_generate_fields_and_order(self):
        result = generate("A boy runs.\n\nA dog follows.")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["scene_number"], 1)
        self.assertIn("image_prompt", result[0])
        self.assertIn("video_prompt", result[0])
        self.assertEqual(result[1]["duration_seconds"], 8)


if __name__ == "__main__":
    unittest.main()
