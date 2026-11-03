# Charter / standing rules
- Reply to Chun in Traditional Chinese (zh-TW). Ask Chun only about important things.
- Use Cursor models only.
- Business: free download + one-time purchase; zero operating cost (no server).
- Minimal, polished UI. App follows the phone's system language. Social markets and platforms follow `marketing/social/regions.md`.
- Previews before development. Walkthroughs as GIF (<3MB), not mp4.
- EAS free plan: 15 builds/month — validate locally first, batch changes. **Every EAS build needs Chun's approval.**
- **Every post, comment or reply must be shown to Chun before publication and receive explicit approval.** Include Traditional Chinese translations for non-Chinese originals and drafts.
- Credentials only via masked inputs, never in chat — and never in this repo.
- 碼農直接提交並推送 main，不另開 branch 或 PR。漏洞大師負責 App 程式變更的安全審查且不改程式碼；推送 App 程式變更及 EAS 前仍須通過阿姨的 test-flows.md。

## 品牌帳號與權限（2026-10-20）
- 自 2026-10-20 起，兩個 repo（`tinytoolshedhq/app`、`tinytoolshedhq/tinytoolshed-backup`）已轉移到品牌帳號 tinytoolshedhq。
- 權限、帳號、金鑰、登入相關的步驟只能由黑嘛嘛和蘋果大師處理；其他 bot 遇到這類事項必須交給他們，不得自行操作。
- Chun 定案（2026-11-03）：後續變更直接提交並推送 main，不另開 branch 或 PR。本條優先於其他文件的舊 PR／分支流程；既有 App 安全審查、使用者測試及每次 EAS 的明確核准要求繼續適用。

## 社群內容規則（Chun，2026-11-03）
- 平台與市場依 `marketing/social/regions.md`；每日候選、逐則審核與翻譯格式依 `marketing/tiny-toolshed-launch.md`。
- 每天每國跨三平台合計最多 2 則；主題須與 App 相關（第一條件）；48 小時內發布；按讚數 ≥100 或留言數 ≥50（2026-11-03 Chun 核准）。
- 每次發布前通知 Chun 並送審；非中文的原文及擬發布內容分別附繁體中文翻譯，明確核准後才發布。
- 各國文案依當地語氣撰寫，只做文字或圖片。

## App PR 規則（Chun，2026-10-20）
- 每個 app PR（`tinytoolshedhq/app`）必須先通過漏洞大師的安全審查。
- 審查通過後，可憐的碼農負責通知胖嘟嘟阿姨。
- 阿姨必須實際跑一次 `bots/user-tester/test-flows.md` 裡的流程。
- 只有阿姨通過後，才能合併或打包（EAS）。
- 備份 repo 的純文件 PR 免跑使用者測試。
