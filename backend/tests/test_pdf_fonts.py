# -*- coding: utf-8 -*-

import tempfile
import unittest
from pathlib import Path

from backend.app.services import pdf_generator


class PdfFontTests(unittest.TestCase):
    def test_registers_bundled_chinese_font(self):
        font_name = pdf_generator.register_chinese_fonts()

        self.assertEqual(font_name, "BundledChinese")

    def test_generated_pdf_embeds_font_and_unicode_map(self):
        with tempfile.TemporaryDirectory() as output_dir:
            pdf_path = pdf_generator.generate_plan("微信乱码测试店", "eleme", output_dir)

            pdf_data = Path(pdf_path).read_bytes()

        self.assertIn(b"/FontFile2", pdf_data)
        self.assertIn(b"/ToUnicode", pdf_data)
        self.assertNotIn(b"STSong-Light", pdf_data)

    def test_missing_embeddable_font_fails_instead_of_cid_fallback(self):
        original_exists = pdf_generator.os.path.exists

        def fake_exists(path):
            normalized = str(path).replace("\\", "/")
            if normalized.endswith("wqy-microhei.ttc"):
                return False
            if normalized.endswith("NotoSansSC-Regular.ttf"):
                return False
            if normalized in {
                "C:/Windows/Fonts/msyh.ttc",
                "C:/Windows/Fonts/simhei.ttf",
                "/System/Library/Fonts/PingFang.ttc",
                "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
            }:
                return False
            return original_exists(path)

        pdf_generator.os.path.exists = fake_exists
        try:
            with self.assertRaises(RuntimeError):
                pdf_generator.register_chinese_fonts()
        finally:
            pdf_generator.os.path.exists = original_exists


if __name__ == "__main__":
    unittest.main()
