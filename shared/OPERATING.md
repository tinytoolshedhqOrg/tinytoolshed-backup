# SuperGrok ↔ Grok Bot Operating Agreement

## Core Rules (must follow)
1. Primary conversation partner is **SuperGrok**. Only call Grok Bots when the task truly requires the shared computer, browser logins, scheduled routines, or local execution.
2. Minimize Grok Bot weekly limit usage.
3. Push **directly to main**. Do **not** open PRs for shared/ documentation or handoff files.
4. Pure documentation (README, OPERATING.md, drafts without secrets) does **not** need review by 漏洞大師.

## Shared Workspaces
- **Short-term execution** → `tinytoolshedhq/app/shared/`
  - `drafts/` — posts, scripts, replies ready for bots
  - `tasks/` — briefs for specific bots
  - `calendar/` — schedules
- **Long-term durable** → `tinytoolshedhqOrg/tinytoolshed-backup/shared/`
  - `strategy/` — refined strategy docs
  - `notes/` — SuperGrok notes and summaries

## When to call which Bot
- 黑嘛嘛（以 Cursor 雲端代理在 tinytoolshedhqOrg repo 開 PR） — code changes and PRs (EAS builds: 蘋果大師, with Chun's approval)
- 社群小編已停用；社群貼文/回覆由行銷大師提草稿，Chun 核准後才發
- 漏洞大師 — secret / credential leak scans
- 黑麻麻 — only when coordination inside the bot system is needed
- Others only when their specific responsibility is required

## Bot Prompt Style
Keep bot prompts short and point to files already in the repo.
Example: "pull shared/drafts/week-43/ and schedule according to calendar. Do not post until approved."

## New Chat Starter
User will say: "請先讀 shared/OPERATING.md 再繼續" or paste a short reminder. Read this file (and the one in the backup repo) and follow all rules above.
