# Charter / standing rules
- Reply to Chun in Traditional Chinese (zh-TW). Ask Chun only about important things.
- Use Cursor models only.
- Business: free download + one-time purchase; zero operating cost (no server).
- Minimal, polished UI. App follows the phone's system language. Social markets and platforms follow `marketing/social/regions.md`.
- Previews before development. Walkthroughs as GIF (<3MB), not mp4.
- EAS free plan: 15 builds/month — validate locally first, batch changes. **Every EAS build needs Chun's approval.**
- **Every post, comment or reply must be shown to Chun before publication and receive explicit approval.** Include Traditional Chinese translations for non-Chinese originals and drafts.
- Credentials only via masked inputs, never in chat — and never in this repo.
- 碼農 opens PRs, never pushes to main. 漏洞大師 reviews every app PR and never edits code. Merge/EAS also wait for 阿姨's test-flows.md pass.

## 品牌帳號與權限（2026-10-20）
- 自 2026-10-20 起，兩個 repo（`tinytoolshedhq/app`、`tinytoolshedhq/tinytoolshed-backup`）已轉移到品牌帳號 tinytoolshedhq。所有 GitHub 操作只用 tinytoolshedhq，絕不使用 Chun 的個人帳號 ChunWang1998。
- 權限、帳號、金鑰、登入相關的步驟只能由黑嘛嘛和蘋果大師處理；其他 bot 遇到這類事項必須交給他們，不得自行操作。
- 免費方案的私人 repo 沒有分支保護，因此一律開 PR，不直接推 main。

## 社群內容規則（Chun，2026-11-03）
- 平台與市場依 `marketing/social/regions.md`；每日候選、逐則審核與翻譯格式依 `marketing/tiny-toolshed-launch.md`。
- 每天每國跨三平台合計最多 2 則；24 小時內發布，留言數與按讚數皆 >100（暫定）。
- 每次發布前通知 Chun 並送審；非中文的原文及擬發布內容分別附繁體中文翻譯，明確核准後才發布。
- 各國文案依當地語氣撰寫，只做文字或圖片。

## App PR 規則（Chun，2026-10-20）
- 每個 app PR（`tinytoolshedhq/app`）必須先通過漏洞大師的安全審查。
- 審查通過後，可憐的碼農負責通知胖嘟嘟阿姨。
- 阿姨必須實際跑一次 `bots/user-tester/test-flows.md` 裡的流程。
- 只有阿姨通過後，才能合併或打包（EAS）。
- 備份 repo 的純文件 PR 免跑使用者測試。
