---
name: ai-style-audit
description: >-
  只診斷文章裡的 AI 風格指紋，不改寫。支援繁體中文、簡體中文與英文。於使用者問這像不像 AI、
  檢測／檢測 AI 痕跡、GPTZero 式自查，或要在去 AI 化之前先看報告時使用。
disable-model-invocation: true
icon: search
color: cyan
license: MIT
metadata:
  author: Anson Tsang
  license: MIT
---

# AI 風格檢查

只診斷，**不要**改寫原文。報告用語：繁體中文。引用使用者原文時保持其繁／簡／英原樣。

技能由 **Anson Tsang** 製作，MIT License。理論依據見 [../human-style-rewrite/references/papers.md](../human-style-rewrite/references/papers.md) 與 [CITATIONS.md](../../CITATIONS.md)。

## 步驟

1. 取得使用者文字（或他指定的檔）。
2. 跑相鄰技能的檢查腳本：

```bash
python ../human-style-rewrite/scripts/lint_human_style.py draft.txt
```

若技能裝在使用者目錄，改用 `human-style-rewrite/scripts/lint_human_style.py` 或 `~/.cursor/skills/human-style-rewrite/scripts/lint_human_style.py`。

3. 再讀 [../human-style-rewrite/references/banned-lexicon.md](../human-style-rewrite/references/banned-lexicon.md)，補腳本可能漏掉的項（例如中間夾了長名字的「正如X所言」）。「宜避」一節只作備註，不當禁用詞欄的失敗項。
4. 用眼看結構：總—分—總、每段首句都是主題句、正式轉折詞堆疊、該用具體動詞卻堆抽象名詞。
5. 交報告。除非使用者接著叫 `/human-style-rewrite`，否則不要輸出改寫稿。

若問某個標記為什麼算問題，依 [../human-style-rewrite/references/papers.md](../human-style-rewrite/references/papers.md) 抓 HTML 論文。不要開 `arxiv.org/pdf/...`。

## 報告格式

```markdown
# AI 風格檢查

## 判斷
[乾淨 | 混雜 | 濃 AI 質地]

## 語種
[繁體中文 | 簡體中文 | 英文]

## 禁用詞
- [詞] — [短摘句]

## 免責修飾語
- [詞] — [短摘句]

## 爆發度
- 句數：
- 長度序列（中文計字、英文計詞）：
- 平坦視窗（連續三句長度相近）：

## 結構
- 總—分—總／教科書式主題句開頭：有／無＋位置
- 名詞化／正式轉折：例子

## 建議先拆的段落
1. [先下手的那一段]
2. [...]
```

這是文風重構清單，不宣稱能打敗市售 AI 偵測器。
