# 工作流程

## 溝通
- 用繁體中文回 Chun，簡短；只問重要的事。
- 只用 Cursor 模型。
- 影片一律給 GIF（< 3MB），mp4 Chun 打不開。
- 先給 preview 畫面，Chun 核准後才開發。

## 開發與 build
1. 黑嘛嘛（以 Cursor 雲端代理在 tinytoolshedhqOrg repo 開 PR）（不直接推 main）→ 漏洞大師審查（只審不改）→ merge。
2. 本機驗證、批次累積改動（EAS 免費版每月 15 次）。
3. **每次 EAS build 都要 Chun 先同意**，再交給蘋果大師（`--non-interactive`、`EXPO_NO_CAPABILITY_SYNC=1`）。
4. 蘋果大師回報 build 編號、TestFlight 狀態、剩餘次數 → 轉告 Chun。失敗就由黑嘛嘛開修正 PR，重試要再經 Chun 同意。

## 行銷與社群
- 社群小編已停用；社群貼文/回覆由行銷大師提草稿，Chun 核准後才發。市場與平台範圍見 [分工表](../../marketing/social/regions.md)。
- 每次社群發布前通知 Chun 並送審；原文及草稿非中文時各附繁中翻譯，收到該則明確核准才發布。候選數量與門檻依[社群執行規則](../../marketing/tiny-toolshed-launch.md)。
- App 跟隨系統語言。

## 安全
- 憑證只走遮罩輸入框，絕不進聊天或 repo。

## 備份
- 每天 21:00（台北）跑 `/workspace/backup/backup.sh`（必須 SCAN CLEAN），再在備份 repo（tinytoolshedhqOrg/tinytoolshed-backup）上開 cloud agent 發 PR，審過再合併。
- 重要檔案完成時也順便備份。
