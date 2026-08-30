#!/usr/bin/env python3
"""檢查改寫稿：禁用 AI 詞、免責修飾語、平坦句長。

僅用標準庫。通過結束碼 0，缺失結束碼 1。
詞庫讀自 ../references/banned-lexicon.md。
支援繁體中文、簡體中文與英文。

用法：
  python lint_human_style.py draft.txt
  python lint_human_style.py --stdin
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LEXICON = SKILL_ROOT / "references" / "banned-lexicon.md"

ZH_JUST_AS_SAID = re.compile(r"正如.{0,12}所言")
ZH_MAYBE = re.compile(r"(?<![不])可能(?!性)")
SENTENCE_SPLIT = re.compile(r"(?<=[。！？.!?])\s*")
CJK = re.compile(r"[\u3400-\u9fff]")
PAREN_NOTE = re.compile(r"[（(].*?[）)]")

# 小說短句連寫不當失敗。
SHORT_WINDOW_MAX = 8


@dataclass
class Lexicon:
    zh_banned: list[str] = field(default_factory=list)
    en_banned: list[str] = field(default_factory=list)
    zh_hedge: list[str] = field(default_factory=list)
    en_hedge: list[str] = field(default_factory=list)


def _split_variants(item: str) -> list[str]:
    cleaned = PAREN_NOTE.sub("", item).strip()
    if not cleaned or "正如" in cleaned:
        return []
    return [part.strip() for part in re.split(r"\s*/\s*", cleaned) if part.strip()]


def load_lexicon(path: Path) -> Lexicon:
    text = path.read_text(encoding="utf-8-sig")
    section = ""
    lex = Lexicon()
    skip_soft = False

    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("## "):
            section = line[3:].strip()
            skip_soft = section.startswith("宜避")
            continue
        if line.startswith("### "):
            continue
        if skip_soft or not line.startswith("- "):
            continue

        item = line[2:].strip()
        if section.startswith("中文禁用詞"):
            lex.zh_banned.extend(_split_variants(item))
        elif section.startswith("英文禁用詞"):
            lex.en_banned.extend(v.lower() for v in _split_variants(item))
        elif section.startswith("中文免責"):
            if item.startswith("可能"):
                continue
            lex.zh_hedge.extend(_split_variants(item))
        elif section.startswith("英文免責"):
            lex.en_hedge.extend(v.lower() for v in _split_variants(item))

    if not lex.zh_banned or not lex.en_banned:
        raise ValueError(f"詞庫讀不到禁用詞：{path}")
    return lex


def split_sentences(text: str) -> list[str]:
    parts = [p.strip() for p in SENTENCE_SPLIT.split(text) if p.strip()]
    return [p for p in parts if not re.fullmatch(r"[\s\-—–]*", p)]


def sentence_length(sentence: str) -> tuple[int, str]:
    compact = re.sub(r"\s+", "", sentence)
    cjk = len(CJK.findall(sentence))
    if compact and (cjk / max(len(compact), 1)) >= 0.4:
        return cjk, "cjk"
    words = re.findall(r"[A-Za-z0-9']+", sentence)
    return len(words), "words"


def find_hits(text: str, needles: list[str], *, english: bool = False) -> list[str]:
    hits = []
    if english:
        for needle in needles:
            if re.search(rf"\b{re.escape(needle)}\b", text, flags=re.IGNORECASE):
                hits.append(needle)
        return hits
    for needle in needles:
        if needle in text:
            hits.append(needle)
    return hits


def lint(text: str, lexicon: Lexicon | None = None) -> list[str]:
    lex = lexicon or load_lexicon(DEFAULT_LEXICON)
    errors: list[str] = []

    for hit in find_hits(text, lex.zh_banned):
        errors.append(f"中文禁用詞：{hit}")
    if ZH_JUST_AS_SAID.search(text):
        errors.append("中文禁用詞：正如…所言")
    for hit in find_hits(text, lex.en_banned, english=True):
        errors.append(f"英文禁用詞：{hit}")
    for hit in find_hits(text, lex.zh_hedge):
        errors.append(f"中文免責語：{hit}")
    if ZH_MAYBE.search(text):
        errors.append("中文免責語：可能")
    for hit in find_hits(text, lex.en_hedge, english=True):
        errors.append(f"英文免責語：{hit}")

    sentences = split_sentences(text)
    lengths = [sentence_length(s)[0] for s in sentences]
    for i in range(len(lengths) - 2):
        a, b, c = lengths[i], lengths[i + 1], lengths[i + 2]
        window = [a, b, c]
        if min(window) <= 0:
            continue
        if max(window) <= SHORT_WINDOW_MAX:
            continue
        if max(window) / min(window) < 1.35 and max(window) - min(window) <= 4:
            errors.append(
                f"句長過平：第 {i + 1}–{i + 3} 句長度 {a}、{b}、{c}"
            )

    return errors


def _configure_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def main() -> int:
    _configure_stdout()
    parser = argparse.ArgumentParser(description="檢查人類風格改寫草稿")
    parser.add_argument("path", nargs="?", help="要檢查的草稿檔")
    parser.add_argument("--stdin", action="store_true", help="由標準輸入讀取草稿")
    parser.add_argument(
        "--lexicon",
        type=Path,
        default=DEFAULT_LEXICON,
        help="禁用詞清單（預設為技能內 references/banned-lexicon.md）",
    )
    args = parser.parse_args()

    if args.stdin:
        text = sys.stdin.read()
    elif args.path:
        text = Path(args.path).read_text(encoding="utf-8-sig")
    else:
        parser.error("請提供檔案路徑或使用 --stdin")

    errors = lint(text, load_lexicon(args.lexicon))
    if not errors:
        print("OK")
        return 0
    print("FAIL")
    for err in errors:
        print(f"- {err}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
