# 推論基準論文（讀 HTML，不開 PDF）

核對理論依據、或要對照新的 AI 寫作特徵時讀本檔。

論文著作權屬原作者。本技能只引用核心觀察，不重發全文。出處總表見倉庫 [CITATIONS.md](../../../CITATIONS.md)。

讀 HTML 版，不要開 `arxiv.org/pdf/...`。

## 讀取步驟

1. 從下方或檢索結果取得 arXiv 編號。
2. 先抓 `https://arxiv.org/html/{id}`（最新）或 `https://arxiv.org/html/{id}v{n}`（釘版本）。
3. 若 404，改抓 `https://ar5iv.labs.arxiv.org/html/{id}`。
4. 任何 arXiv 連結都改成 HTML：`/abs/{id}` → `/html/{id}`；`/pdf/{id}.pdf` → `/html/{id}`。
5. 讀摘要與關於詞彙多樣性、爆發度、指紋、詞性的發現。不要把論文倒進改寫輸出。
6. 只在解釋回覆裡引用，不要寫進重構正文。

動態擴充關鍵詞：`"Stylometrics AI Detection"`、`"LLM Burstiness"`、`"Perplexity Variation in Human Writing"`。

## 種子論文

### 1. Terčon, L., & Dobrovoljc, K. (2025)

*Linguistic Characteristics of AI-Generated Text: A Survey.*

- HTML：https://arxiv.org/html/2510.05136
- 後備：https://ar5iv.labs.arxiv.org/html/2510.05136
- 摘要頁：https://arxiv.org/abs/2510.05136
- 核心理論：AI 文本具備低詞彙多樣性（Low Lexical Diversity）、過度使用名詞化與正式過渡詞之特徵。

### 2. 風格計量與困惑度研究 (2025)

*Feature-Based Detection of AI-Generated Text: An Analysis of Stylometric and Perplexity Markers in Contemporary Large Language Models.*

- ResearchGate：https://www.researchgate.net/publication/398588043_Feature-Based_Detection_of_AI-Generated_Text_An_Analysis_of_Stylometric_and_Perplexity_Markers_in_Contemporary_Large_Language_Models
- 無 arXiv HTML。只抓摘要頁；沒有公開 HTML 就不要轉載全文。
- 核心理論：AI 文本的 Perplexity（困惑度／詞彙預測難度）與 Burstiness（句長與複雜度波動度）顯著低於人類寫作。

### 3. LLM 風格指紋研究 (2025)

*Detecting Stylistic Fingerprints of Large Language Models.*

- HTML：https://arxiv.org/html/2503.01659v1
- 最新：https://arxiv.org/html/2503.01659
- 後備：https://ar5iv.labs.arxiv.org/html/2503.01659
- 摘要頁：https://arxiv.org/abs/2503.01659
- 核心理論：自迴歸語言模型存在穩定的「風格指紋」（包含特定轉折詞組與對稱式句構）。

### 4. Tarım, İ., & Onan, A. (2025)

*Can You Detect the Difference? Stylometric Analysis of Language Models.*

- HTML：https://arxiv.org/html/2507.10475
- 後備：https://ar5iv.labs.arxiv.org/html/2507.10475
- 摘要頁：https://arxiv.org/abs/2507.10475
- 核心理論：以平均句子長度方差（Sentence Length Variance）與詞性搭配（POS Bigrams）打碎自迴歸模型的平滑文法結構。
