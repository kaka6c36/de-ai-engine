# De-AI Engine

由 **Anson Tsang** 製作的 Cursor 技能與子代理：把小說、論文、日常文章改寫成帶人類寫作節奏的文字，或只檢查 AI 風格指紋、不改稿。

專案說明以**繁體中文**書寫。改寫時依原文輸出：**繁體中文**、**簡體中文**或**英文**。

這是文風重構流程，不宣稱能打敗市售 AI 偵測器。

## 版權與授權

- 技能、子代理、說明與檢查腳本：Copyright (c) 2026 **Anson Tsang**，[MIT License](LICENSE)
- 理論依據引用四篇論文的核心觀察，**不收錄論文全文**。出處與連結見 [CITATIONS.md](CITATIONS.md)

## 叫用

| 指令 | 作用 |
| --- | --- |
| `/human-style-rewrite` | 改寫貼上或選取的文字。只輸出重構後全文。 |
| `/ai-style-audit` | 列出指紋，不改寫。 |
| `/de-ai-engine` | 交給專責子代理（改寫或檢查）。 |

亦可把 `human-style-rewrite` 開成 Custom Mode（書本圖示、橙色）。

在 Cursor 打開本庫時，`.cursor/skills` 與 `.cursor/agents` 指向 `skills/`、`agents/` 正本並自動載入。第一次請跑：

```powershell
powershell -File scripts\link-cursor-dev.ps1
```

```bash
sh scripts/link-cursor-dev.sh
```

## 裝到其他專案

**Windows (PowerShell)**

```powershell
Copy-Item -Recurse skills\human-style-rewrite <your-repo>\.cursor\skills\human-style-rewrite
Copy-Item -Recurse skills\ai-style-audit <your-repo>\.cursor\skills\ai-style-audit
Copy-Item agents\de-ai-engine.md <your-repo>\.cursor\agents\de-ai-engine.md
```

**Unix**

```bash
mkdir -p your-repo/.cursor/skills your-repo/.cursor/agents
cp -R skills/human-style-rewrite your-repo/.cursor/skills/
cp -R skills/ai-style-audit your-repo/.cursor/skills/
cp agents/de-ai-engine.md your-repo/.cursor/agents/
```

## 裝到本機所有專案

**Windows (PowerShell)**

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.cursor\skills", "$env:USERPROFILE\.cursor\agents" | Out-Null
Copy-Item -Recurse skills\human-style-rewrite "$env:USERPROFILE\.cursor\skills\human-style-rewrite"
Copy-Item -Recurse skills\ai-style-audit "$env:USERPROFILE\.cursor\skills\ai-style-audit"
Copy-Item agents\de-ai-engine.md "$env:USERPROFILE\.cursor\agents\de-ai-engine.md"
```

**Unix**

```bash
mkdir -p ~/.cursor/skills ~/.cursor/agents
cp -R skills/human-style-rewrite ~/.cursor/skills/
cp -R skills/ai-style-audit ~/.cursor/skills/
cp agents/de-ai-engine.md ~/.cursor/agents/
```

複製後請重載 Cursor 視窗。使用者層技能不會跟著 Cloud Agents；遠端工作請把複本放進該專案的 `.cursor/`。

## 檢查腳本

改寫後必須執行：

```bash
python skills/human-style-rewrite/scripts/lint_human_style.py draft.txt
```

僅用標準庫。結束碼 `0` 為通過。詞庫正本：[skills/human-style-rewrite/references/banned-lexicon.md](skills/human-style-rewrite/references/banned-lexicon.md)。

```bash
python skills/human-style-rewrite/scripts/test_lint_human_style.py
```

## 論文（讀 HTML，不開 PDF）

核對理論依據時，讀 arXiv HTML：

- `https://arxiv.org/html/{id}`（例：https://arxiv.org/html/2503.01659v1）
- 後備：`https://ar5iv.labs.arxiv.org/html/{id}`

種子清單：[skills/human-style-rewrite/references/papers.md](skills/human-style-rewrite/references/papers.md)

## 外掛

`.cursor-plugin/plugin.json`、`skills/`、`agents/` 已齊，可供本機安裝。

## 目錄

```text
skills/human-style-rewrite/   # 改寫技能（正本）
skills/ai-style-audit/        # 只檢查、不改寫
agents/de-ai-engine.md        # 子代理
.cursor/skills/               # 指向 skills/，打開本庫時載入
.cursor/agents/               # 指向 agents/
CITATIONS.md                  # 論文引用聲明
LICENSE                       # MIT，著作權人 Anson Tsang
```
