# 工作流程

## 協作對象
- 黑嘛嘛：總管 bot，派任務、轉達 Chun 的指示；完成重要工作後回報。
- 區域小編依 [分工表](../../marketing/social/regions.md)負責所屬市場在 X、Threads、Instagram 的內容。
- 可憐的碼農（開發）：確認產品功能事實；文案中的功能聲明以開發確認為準。

## 檔案位置
- 共用電腦：/workspace/marketing/
  - launch/：各國 outreach、ASO、site-copy.md
  - learning/：產品研究與 ASO 資料
  - social/：regions.md、phrase-bank/、reply-log/、replies/
  - scripts/：ASO 檢查腳本
- Bot 文件：/workspace/backup/repo/bots/marketing-master/

## 備份
- 每次重大修改後，把 /workspace/marketing 整個複製到本 bot store 的 marketing-backup/。
- 從備份還原時，只複製較新或缺少的檔案，不覆蓋共用電腦上較新的檔案（其他編輯者可能在改）。

## 核准流程
1. 小編或我準備草稿（發文／回覆），附來源連結。
2. 送 Chun 核准；Chun 回「發」才發布。
3. 發布後記錄到 social/reply-log 或 replies/log.md。
- EAS build 也須 Chun 核准。重要決定才問 Chun。

## 品牌帳號（只列帳號名稱）
- X：@Tinytoolshedhq
- Threads：@tinytoolshedhq
- Instagram：使用已核准的品牌帳號；登入狀態另行確認。
- 聯絡信箱：tinytoolshedhq@gmail.com

## Chun 新規則（2026-10-20）
- **每週學習最高流量貼文**：每週一一次（台北時間）。督導三位小編在各國主要平台找近期高互動貼文，分析開頭鉤子、語氣、結構、結尾互動方式，更新到該國的 phrase-bank（`marketing/social/phrase-bank/<國家>.md`）。只做學習和更新用語庫，不做大量回覆。
- **各國腳本自己寫**：小編為每個國家自己寫腳本，不統一成同一套；每國都要符合當地語氣和習慣。
- **IG Reels**：用 CapCut 免費版剪輯並加字幕，不用付費 AI 生成工具。
