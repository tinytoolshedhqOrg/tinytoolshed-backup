# PR #53 複審（tinytoolshedhq/app，Been Ages IAP，head 2a1f957）
結論：**通過**（策略取捨可接受；建議加 TTL，列 L1，不阻擋）

驗證：10 檔 +562/-58；跟 main 沒有衝突（merge-tree 乾淨）；jest 522/522 全過（TZ=UTC、Asia/Taipei）；secret regex 掃描只命中欄位名稱字串 'purchaseToken'（iap.js 去重 key 清單），不是 secret；iap.js/entitlements.js 沒有 console 輸出，也不印 JWS、收據或 transactionId。Checklist：沒動到 podspec、expo-file-system/媒體套件、app.json（buildNumber 仍是 12）。新增檔案和變更都跟 IAP、loading 有關，沒有無關操作；5 個語系都有加 iap.processing。

## 取捨評估：購買事件 + verify≠true → 持久化 pending — 可接受
- 進入條件嚴格（iap.js grantFullpackPurchase）：isPendingPurchase → false；purchaseMatches(正確 productId) 且 !isRevoked 才繼續；之後先重讀 entitlements（立即、1s、3s），都讀不到才寫 pending（iap.js:281）。
- 偽造需要越獄或 hook 才能注入 purchase-updated 事件；本機買斷的價值低，可以接受。審核員重開 app 仍是解鎖狀態，符合 2.1(b)。
- 啟動時（verifyProOnLaunch，iap.js:~626-650）：查到 entitlement → setProUnlocked(true) 寫 '1'，清掉 pending；明確撤銷 → 立即鎖；查詢成功但列表空 → streak +1 並持久化（setEmptyPurchaseStreak），第 3 次撤銷；離線或讀取失敗（ok:false 或 catch）→ 不改 streak、不撤銷。streak 累加和持久化正確，測試有涵蓋。

## 發現
- L1｜iap.js:281 + entitlements.js:78：pending 沒有上限。永遠離線（或查詢一直失敗）時，pending 會永久有效；ts 有寫入但沒被使用。另外每次合法的購買事件都會把 streak 歸零（iap.js:282）。正常情況下，已擁有的非消耗品不會再產生新事件，只有 hook 注入才可能，所以風險低。
  修法：在 verifyProOnLaunch 裡，若 record.pendingVerification 且 Date.now()-ts > N 天（建議 7–14 天），就撤銷，或要求下一次成功查詢必須查到 entitlement；查詢成功但空時也不要讓購買事件歸零 pending 的 streak（或另外記 pendingSince，不被重設）。注意：完全離線的使用者即使有 TTL 也無法得知退款，所以 TTL 的效果主要是限制 hook 造成的永久解鎖；可以列為下一版改善。
- L2｜iap.js:184-188：沒有 transactionId 時，去重 key 會退回 `sku:<id>:<date>`；date 也沒有時，所有事件共用同一個 key。只會在執行中合併，finally 會刪除（含 `grantInFlight.get(key)===run` 檢查），所以不會卡住，也不會漏掉後續交易；stopPurchaseUpdates 也會 reset。可以接受。
- L2｜PaywallScreen.js / SettingsScreen.js：busyLock useRef 防連點，finally 都會解鎖，正確。Settings 的「兌換代碼」在 busy 時也被停用，合理。
- L2｜app.json:13：buildNumber 仍是 12，下次 EAS build 前必須改成 >12。
