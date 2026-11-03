# 美國（英文）X：App 開發者都在哪類貼文底下留言推廣？

調查日：2026-11-03（台北時間）；樣本：2026-10-27～11-03 的公開貼文。只讀取，未登入、未發文、未按讚。
工具：Grok Bot 公開 X 讀取 API（7 次搜尋，約 170 則貼文/回覆）＋ 5 篇網路文章。
注意：不引用陌生人原文、不列帳號；連結僅作證據。`lang:en` 不能證明是美國人（見 search-strategy/x.md 第 2 節）。

## 方法
1. 反向找：搜「回覆中含 App Store 連結＋ I built / my app」（`url:apps.apple.com is:reply`），看這些推廣回覆掛在哪種原文底下。25 則樣本。
2. 正向找：用候選關鍵字搜原文，記錄互動數；挑一則熱門串讀 25 則回覆。
3. X API 沒有互動數篩選（`min_replies:` 會被移除），互動門檻只能拿到結果後再篩。

## 五種貼文類型（依「適合 Tiny Toolshed」排序）

| # | 類型 | 找得到的查詢 | 觀察到的互動 | 推廣回覆的反應 | 適合 |
|---|---|---|---|---|---|
| 1 | 抱怨某 App／訂閱、或「怎麼還沒有這種 App」 | `"they need to make" app`、`"is there an app"`、`"cancel a subscription"`、`"this app's"`、`"why is there no app"` | 多數很小（例 14 讚/10 回）；偶爾爆紅（取消訂閱被挽留的梗文 66k 讚/136 回） | 本次最好的一則推廣回覆在這類：原文 1.5k 讚，回覆「我的 app 免費、做一樣的事」有 723 次曝光、1 讚。另一則「我也這樣想所以做了一個」在小貼文底下 | 高：買斷、免訂閱是直接賣點（分貝計、Been Ages） |
| 2 | 新裝置／新功能熱議貼文（例：iPhone Duo） | `"iPhone" (new OR "just got" OR wallpaper)`、`iOS 27` | 原文 800～1.2k 讚，但回覆只有 30～35 | 同一人把同一句＋連結貼在 5 篇熱門文底下：曝光 2～52、0 讚 → 典型被當垃圾 | 中：只有 app 真的有對應功能時才合理 |
| 3 | 策展「回覆你的 app，我收進清單」 | `"reply with" (app OR apps) link`、`"app directory"`、`"add your app"` | 266 讚/281 回、152 讚/25 回 | 回覆幾乎都 0～1 讚，但目的是被收錄，不是拿讚 | 中高：低風險、被收錄有長尾流量 |
| 4 | 開發者互推串「Drop your startup / What are you building」 | `"drop your startup" OR "drop your app" OR "what are you building"` | 25 篇中最高 178 回/68 讚；125/48；86/39；**沒有一篇達 100 讚** | 讀了 178 回那串的 25 則：多數是產品介紹，幾乎全 0 讚、曝光個位數～30；觀眾是其他開發者，不是買家 | 低：不違規但幾乎沒用戶，只適合找測試者/交流 |
| 5 | 「你用什麼 app 做 X？」「推薦冷門 app」 | `"what app do you use"`、`"underrated apps"`、`"recommend an app"` | 多在 2～80 讚、0～30 回（例 32 讚/29 回、81 讚/30 回） | 樣本中未見明顯推廣回覆 | 中：主題剛好對上時回答最自然 |

另外試了需求主題（`stiff neck`/`posture`/`upstairs neighbor`/`how long has it been since`）：大多是健身內容帳號或與 app 無關的閒聊，互動小，`how long has it been since` 幾乎全是追星/運動語境，不適合 Been Ages。

## 證據連結（只列原文）
- 類型 1：https://x.com/i/status/2116460202279186562 （1.5k 讚/17 回，下方有成效最好的推廣回覆）、https://x.com/i/status/2114720019342893560 （取消訂閱梗文）、https://x.com/i/status/2114247767019155919 、https://x.com/i/status/2115242688744485055
- 類型 2：https://x.com/i/status/2116907381217226941 、https://x.com/i/status/2116891987550834792
- 類型 3：https://x.com/i/status/2113696042797396479 、https://x.com/i/status/2114749725471580411
- 類型 4：https://x.com/i/status/2116402669828911601 、https://x.com/i/status/2115278800376504657
- 類型 5：https://x.com/i/status/2117433836384469438

## 每日搜尋關鍵字（建議，加 `lang:en -is:retweet -is:reply`）
1. `"is there an app" (track OR remember OR noise OR stretch)`
2. `"they need to make an app"`
3. `"why is there no app"`
4. `"cancel" subscription app (annoying OR scam OR "free trial")`
5. `"one time purchase" app`
6. `"no subscription" app`
7. `"what app do you use" (track OR noise OR stretch OR habit)`
8. `"underrated apps" OR "apps you can't live without"`
9. `"recommend an app" OR "app recommendations"`
10. `"reply with" (app OR apps) OR "add your app"`
11. `"decibel" OR "how loud" (concert OR neighbor OR neighbors)`
12. `"noisy neighbors" OR "upstairs neighbor"`
13. `"last time I" (cleaned OR changed OR washed)`
14. `"when did I last" OR "forgot when I last"`
15. `"neck pain" (desk OR work OR laptop) OR "tech neck"`
16. `"stretch" (desk OR "sitting all day")`
（11～16 是需求情境；1～10 是推薦意圖。與現有 x.md 的 A/B 組互補，取代 A 組中命中率低的 `"iPhone apps"`。）

## 門檻是否可行
- 「24 小時內、>100 回覆且 >100 讚」：樣本中只有和 app 無關的爆紅文（梗文、明星、新聞）同時達標；開發者互推串回覆可破 100 但讚數不到 100；需求類、推薦類幾乎都達不到。
- 建議：改成「48 小時內，讚 ≥100 **或** 回覆 ≥50」，並把「主題相關」當第一條件；照現行門檻，很可能每天 0 則合格。

## 風險與語氣（文章＋觀察）
- 同一句話＋連結貼在多篇熱門文 = 本次最明顯的失敗模式（0 讚、曝光個位數）。
- 多篇指南（xfaste.st、dev.to/threadotter、replyman.app、x-jumper.com）一致：冷回覆帶連結易被降權；免費帳號回覆排序靠後（Premium 排前，為廠商測試非官方）；每天 2～3 則、內容各不相同、先回答問題再提 app。
- 與我們規則的衝突：上架後規則要求每則附 App Store 連結＋影片＋照片，這正是被認為最容易降權的形式。建議 Chun 考慮：連結放個人簡介或在對方回應後再補。
- 有效語氣：先具體回應原文痛點 → 一句說明「我做了一個買斷、不用訂閱的 X」→ 誠實註明只有 iOS。

## 限制
- 樣本小（約 170 則），一週內；未測 Threads/IG；無法確認帳號所在國。
- 推廣成效只能看公開讚/曝光，看不到下載數。

## 附錄（2026-11-03 18:20 台北時間）：本週合格貼文與他人推廣回覆實例

新門檻：主題相關優先；讚 ≥100 或 回覆 ≥50。範圍 10/28～11/3。數字為 11/3 18:19 台北時間重新抓取並驗證存在。距今時間＝到 11/3 18:20 為止。
**注意：48 小時內的只有 #1、#2、#3、#6、#7、#9（若嚴格算 48h）。**

### A. 合格貼文（11 則，主題相關、達門檻）
| # | 連結 | 類型／適合 app | 讚/回覆 | 距今 |
|---|---|---|---|---|
| 1 | https://x.com/i/status/2117301702088937749 | 每晚 4 個伸展動作教學／伸展 app | 2007/10 | 約 25h |
| 2 | https://x.com/i/status/2117281562731614392 | Mac 待辦 app 該選哪個（推薦串）／App 推薦 | 32/54 | 約 19h |
| 3 | https://x.com/i/status/2116943533718249563 | 抱怨某 app 一直沒修好（開發者有人回）／抱怨 | 16480/371 | 約 41h |
| 4 | https://x.com/i/status/2116904512325878162 | 反感 app 要求同步通訊錄／免登入、隱私賣點 | 221292/184 | 約 44h |
| 5 | https://x.com/i/status/2116831831756620175 | 租屋前先問鄰居（含噪音）／分貝計 | 1390/42 | 約 2 天 |
| 6 | https://x.com/i/status/2117426312239362499 | 「用其他 app 追賽事怎麼受得了」／App 推薦（弱相關） | 180/21 | 約 17h |
| 7 | https://x.com/i/status/2116460202279186562 | 抱怨某 app 做得很爛（下方有成效最好的推廣回覆）／抱怨 | 1494/17 | 約 3 天 |
| 8 | https://x.com/i/status/2115975664281251897 | 樓上鄰居噪音梗圖／分貝計 | 324/6 | 約 4 天 |
| 9 | https://x.com/i/status/2115923714025881804 | 超大音量喇叭擾鄰（影片）／分貝計 | 22988/493 | 約 5 天 |
| 10 | https://x.com/i/status/2115730085487825396 | 「Drop your project URL」開發者互推串 | 448/461 | 約 5 天 |
| 11 | https://x.com/i/status/2116907381217226941 | iPhone Duo 熱門貼文（新裝置）／僅適合有對應功能時 | 1189/35 | 約 2 天 |

合格且相關的不到 20 則；Been Ages 主題（`last time I`、`when did I last`）本週沒有任何一則達門檻。
接近但未達（near-miss）：
- https://x.com/i/status/2116954566012842301 用什麼 app 追閱讀進度（70/35，約 2 天）— 最接近 Been Ages 的「紀錄」需求
- https://x.com/i/status/2117433836384469438 用什麼 app 做縮圖（33/30）
- https://x.com/i/status/2116139416410349643 CleanShot 替代品推薦（16/43）
- 稍早於本週但很典型：https://x.com/i/status/2113957408225866057 （清空間抱怨，2055/635，10/24）、https://x.com/i/status/2115058681712918737 （新 MacBook 先裝什麼，286/209，10/27）、https://x.com/i/status/2115181960066933136 （Show off what you've built，97/192，10/27）
- 排除：一則「is there an app…」爆紅文（5k 讚）為成人梗，不適合品牌。

### B. 其他開發者的推廣回覆（15 則，皆已用 API 驗證存在）
| # | 回覆 | 原文 | 類型 | 回覆讚/曝光 | 手法（一句話） |
|---|---|---|---|---|---|
| 1 | https://x.com/i/status/2116530101978333250 | https://x.com/i/status/2116460202279186562 | 抱怨 app | 1/723 | 「我的免費、功能一樣」＋連結；本次成效最好 |
| 2 | https://x.com/i/status/2117019456547508368 | https://x.com/i/status/2116943533718249563 | 抱怨 app | 1/66 | 直接說「我們做了更好的」＋連結，在 1.6 萬讚文底下仍只有 66 曝光 |
| 3 | https://x.com/i/status/2115383025899049151 | https://x.com/i/status/2113957408225866057 | 抱怨（清空間） | 0/0 | 先共感再推自家清理工具 |
| 4 | https://x.com/i/status/2115443194733162544 | https://x.com/i/status/2115058681712918737 | 推薦串 | 0/25 | 「我有偏見因為是我做的」＋說明用途 |
| 5 | https://x.com/i/status/2116166470988333105 | https://x.com/i/status/2116139416410349643 | 找替代品 | 0/93 | 同上自揭身分，回答具體需求 |
| 6 | https://x.com/i/status/2116175611949695079 | https://x.com/i/status/2115850918616784915 | 產品話題 | 0/4 | 主打「不用月費、本機處理」 |
| 7 | https://x.com/i/status/2115799992996970771 | https://x.com/i/status/2115757833748914315 | 使用困擾 | 2/35 | 「如果你用 iPhone，我做了個可能有幫助的」 |
| 8 | https://x.com/i/status/2116178046898032732 | https://x.com/i/status/2116051287716315433 | 忘記取消訂閱 | 0/7 | 對痛點表示同情，再推訂閱追蹤 app |
| 9 | https://x.com/i/status/2117305737978544576 | https://x.com/i/status/2117259833724264490 | 「怎麼管理訂閱？」 | 0/5 | 先給方法（列續訂日），再帶出 app |
| 10 | https://x.com/i/status/2116709576070316251 | https://x.com/i/status/2114247767019155919 | 許願「有沒有這種 app」 | 0/2 | 「我也這樣想，所以做了一個」＋只支援 iPhone |
| 11 | https://x.com/i/status/2117527443452109224 | https://x.com/i/status/2117281562731614392 | 推薦串 | 1/7 | 先公正比較競品，再順帶提自己 |
| 12 | https://x.com/i/status/2116973277520285927 | https://x.com/i/status/2116907381217226941 | 新裝置熱門文 | 0/6 | 同一句＋連結複製到多篇（反例） |
| 13 | https://x.com/i/status/2115782059180580878 | https://x.com/i/status/2115730085487825396 | 開發者互推串 | 1/23 | 「看看我們做的」＋兩個連結 |
| 14 | https://x.com/i/status/2115499903430394024 | https://x.com/i/status/2115405720871129393 | 開發者互推串 | 1/19 | 針對策展者讀者群說明用途 |
| 15 | https://x.com/i/status/2117262697813172614 | https://x.com/i/status/2116402669828911601 | 開發者互推串 | 0/7 | 一句話描述 iOS app＋連結 |

觀察：15 則推廣回覆最多 2 讚；曝光只有 #1 破百。原文熱度高不代表回覆被看到（#2）。自揭身分＋先回答問題的寫法（#4、#5、#9、#11）沒有負評，但曝光仍低。
