---
name: human-style-rewrite
description: >-
  將小說、論文、日常文章改寫為帶人類寫作特徵的文字，去掉 AI 風格指紋（低詞彙多樣性、平坦爆發度、禁用轉折詞）。
  支援繁體中文、簡體中文與英文。於使用者要求去AI化、humanize、de-AI、改得像人寫、或
  De-AI Engine / Human Style Reconstruction Engine 時使用。
disable-model-invocation: true
icon: book-open
color: orange
license: MIT
metadata:
  author: Anson Tsang
  license: MIT
---

# 人類風格重構引擎（De-AI Engine）

把輸入文字（小說、論文或日常文章）改寫成具備人類寫作特徵的內容，去掉 AI 生成痕跡。

專案說明用繁體中文。改寫輸出必須跟原文語種一致：繁體中文、簡體中文或英文。勿把簡體稿改成繁體，也勿把英文稿譯成中文，除非使用者明確要求。

技能由 **Anson Tsang** 製作，MIT License。理論依據見 [references/papers.md](references/papers.md) 與倉庫 [CITATIONS.md](../../CITATIONS.md)。改寫正文不要附授權或論文清單。

## 步驟

1. 辨識語種（繁中 / 簡中 / 英文）與文類（小說 / 論文 / 日常）。輸出跟原文走。
2. 依下方規則改寫。爆發度按文類調整。
3. 草稿寫入暫存檔，跑檢查腳本。失敗就改、再檢查，直到結束碼 0。
4. **只輸出**重構後全文。不要前言、不要「這是為您改寫的文章：」、不要結語、不要在改寫稿裡加引用。

若要解釋改寫理由，可暫時離開「只輸出正文」規則：讀 [references/papers.md](references/papers.md)，依該檔抓 HTML 論文並引用。不要把論文倒進改寫稿。

## 規則

### 1. 禁用 AI 特徵詞

詞庫正本：[references/banned-lexicon.md](references/banned-lexicon.md)。禁用詞與免責修飾語命中即失敗。

- **中文禁用詞**（繁簡皆禁）：此外、值得注意的是、總而言之、綜上所述、不難發現、正如…所言、毋庸置疑、換言之、深入探討、賦能、畫卷、紐帶、雙刃劍、不可或缺、不言而喻。
- **英文禁用詞**：Delve, Tapestry, Furthermore, In conclusion, Beacon, Nuanced, Interplay.
- **宜避、腳本不判失敗**：重塑、基石、編織；notably, harness, testify。套話用法仍應改掉。

### 2. 句式節奏

- 連續三句不要都是中等長度。極短句、中句、長句交錯。
- 小說／日常可用單句成段。論文不要硬塞五字短句或口語。

### 3. 詞彙

- 把抽象名詞換成具體動詞或感官說法（「推動行業發展」→「直接搶走同行的生意」；英文把 “drive industry growth” 改成會碰到人手、店鋪、訂單的說法）。
- 刪「可能」、「在某種程度上」、「或許」、「值得討論的是」以及英文 perhaps / maybe / to some extent，直接陳述。

### 4. 結構

- 不要用「總—分—總」，也不要每段第一句都是主題句。
- 用場景、對話或具體事件開頭。

## 輸出格式

直接輸出重構後的完整文字，不要引言或結語。

## 文類

- **小說 / 日常**：極短句與長句對撞，可用單句成段。
- **論文**：仍禁 AI 詞庫、仍要句長有起伏、仍拆掉教科書式總—分—總。不要硬塞 5 字短句或口語。

## 檢查

在本技能目錄執行：

```bash
python scripts/lint_human_style.py draft.txt
```

```bash
python scripts/lint_human_style.py --stdin < draft.txt
```

寫草稿 → 跑檢查 → 修正 → 再檢查至結束碼 0 → 只印重構正文。

使用者若只要診斷，改走 `ai-style-audit`，不要把檢查結果塞進改寫輸出。

## 範例與參考

- 繁、簡、英對照：[examples.md](examples.md)
- 禁用詞與免責語：[references/banned-lexicon.md](references/banned-lexicon.md)
- 論文與 HTML 讀取步驟：[references/papers.md](references/papers.md)
