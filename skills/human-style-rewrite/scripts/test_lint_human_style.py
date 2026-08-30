#!/usr/bin/env python3
"""lint_human_style 的標準庫測試。"""

from __future__ import annotations

import unittest
from pathlib import Path

from lint_human_style import load_lexicon, lint

EXAMPLES = Path(__file__).resolve().parent.parent / "examples.md"
LEXICON = Path(__file__).resolve().parent.parent / "references" / "banned-lexicon.md"


class LintTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lex = load_lexicon(LEXICON)

    def test_lexicon_loads_hard_words(self) -> None:
        self.assertIn("此外", self.lex.zh_banned)
        self.assertIn("总而言之", self.lex.zh_banned)
        self.assertIn("furthermore", self.lex.en_banned)
        self.assertNotIn("重塑", self.lex.zh_banned)
        self.assertNotIn("notably", self.lex.en_banned)

    def test_ai_chinese_fails(self) -> None:
        text = "此外，值得注意的是，人工智慧正在重塑產業。總而言之，它是一把雙刃劍。"
        errors = lint(text, self.lex)
        joined = " ".join(errors)
        self.assertTrue(any("此外" in e for e in errors), errors)
        self.assertTrue("雙刃劍" in joined or "双刃剑" in joined, errors)
        self.assertFalse(any("重塑" in e for e in errors), errors)

    def test_literary_soft_words_pass(self) -> None:
        text = "石匠把基石放下。雨把舊牆重新塑過一遍。她在燈下編織一條圍巾。"
        self.assertEqual(lint(text, self.lex), [])

    def test_maybe_not_false_positive(self) -> None:
        self.assertEqual(lint("這件事不可能發生。", self.lex), [])
        self.assertEqual(lint("我們討論過可能性。", self.lex), [])
        self.assertTrue(any("可能" in e for e in lint("結果可能不準。", self.lex)))

    def test_english_ai_fails(self) -> None:
        text = "Furthermore, it is worth noting that the report may, to some extent, harness growth."
        errors = lint(text, self.lex)
        self.assertTrue(any("furthermore" in e for e in errors), errors)
        self.assertFalse(any("harness" in e for e in errors), errors)

    def test_short_sentence_run_passes(self) -> None:
        text = "好處有。帳也在。別裝沒看見。"
        self.assertEqual(lint(text, self.lex), [])

    def test_flat_medium_sentences_fail(self) -> None:
        text = "我們檢查了十二個領域的對照文本。我們記錄了每篇的類型標記比。我們比較了機器稿與人工稿。"
        errors = lint(text, self.lex)
        self.assertTrue(any("句長過平" in e for e in errors), errors)

    def test_example_rewrites_pass(self) -> None:
        raw = EXAMPLES.read_text(encoding="utf-8")
        afters = []
        capture = False
        buf: list[str] = []
        for line in raw.splitlines():
            if line.strip() in ("**改後**", "**After**"):
                if buf:
                    afters.append("\n".join(buf).strip())
                    buf = []
                capture = True
                continue
            if line.startswith("## ") or line.startswith("**改前**") or line.startswith("**Before**"):
                if capture and buf:
                    afters.append("\n".join(buf).strip())
                    buf = []
                capture = False
                continue
            if capture:
                buf.append(line)
        if capture and buf:
            afters.append("\n".join(buf).strip())
        self.assertGreaterEqual(len(afters), 4, afters)
        for block in afters:
            if not block:
                continue
            errors = lint(block, self.lex)
            self.assertEqual(errors, [], block)


if __name__ == "__main__":
    unittest.main()
