# 美國（英文）X 搜尋關鍵字：依 App 驗證結果

驗證時間：2026-11-03 19:40（台北時間）；範圍：10/27 19:00～11/3（台北時間），約 7 天。
方法：每個查詢都加 `lang:en -is:retweet -is:reply`，用 X API 依相關性取前 25 則。合格＝主題相關且（讚 ≥100 或回覆 ≥50）。
相關率＝前 25 則中真的在講這個需求的比例，是人工判讀的估計值。
共 33 次查詢，消耗 33 次讀取。只讀取，沒有登入或發文。連結 ID 都由 API 回傳，不列帳號，也不引用原文。
判定：本週有 ≥1 則合格的相關貼文＝KEEP；沒有合格貼文但相關率高＝WEAK（適合找小帳號真實需求，不適合拿來衝門檻）；其餘 DROP。

## 1. Been Ages（好久沒做了）

| 判定 | 查詢 | 本週合格（相關） | 相關率 | 例子 |
|---|---|---|---|---|
| KEEP | `("how often do you" OR "how often should you") (wash OR clean OR change OR replace) -"how often do you think"` | 1 | 約 70% | https://x.com/i/status/2116544965765480582 （多久洗一次馬桶，115 讚/35 回，約 3 天前） |
| KEEP | `("change your sheets" OR "wash your sheets" OR "changed my sheets")` | 2 | 約 55% | https://x.com/i/status/2115170417702768953 （走出低潮：洗澡、換床單、打掃，5.7 萬讚/1322 回，約 7 天前）、https://x.com/i/status/2115881450360750218 （換床單測驗，255 讚，約 5 天前） |
| WEAK | `("replace your toothbrush" OR "change your toothbrush" OR "air filter" OR "water filter") (often OR months OR "last time")` | 0 | 約 60%（多為廠商廣告） | — |
| WEAK | `("call your parents" OR "call your mom" OR "called my mom" OR "haven't called")` | 0 | 約 50% | 最高 54 讚 |
| WEAK | `("water my plants" OR "forgot to water" OR "overwatered")` | 0（唯一合格是成人內容） | 約 40% | — |
| WEAK（推薦類） | `("habit tracker" OR "chore app" OR "app to track" OR "reminder app")` | 0 | 約 40%（多為開發者自推；看到一個同類競品在自推） | — |

DROP：
- `"oil change" OR "last haircut" OR "needs a haircut"`：大多是梗圖和名人髮型。
- `"cleaning schedule" OR "chore chart"…`：多為 Etsy 模板廣告和性別引戰。
- `"things you should clean" / "germiest"`：只找到 3 則。
- `"when was the last time you"`：多為政治文。
- `"can't remember the last time I"`：多為情緒文。
- `"lost track of"…`：雜訊。
- `"you should replace"…`：雜訊。
- 第 1 輪的 `"how often do you"` 已被上面改良版取代。

結論：Been Ages 的需求貼文本週很少衝到門檻，可用的只有「多久洗/換一次」和「換床單、做家事的自我照顧」兩組。建議另外增加原創貼文，或改搜「how often do you」類的投票串。

## 2. Tiny Decibel Meter（分貝計）

| 判定 | 查詢 | 本週合格（相關） | 相關率 | 例子 |
|---|---|---|---|---|
| KEEP | `(neighbor OR neighbors OR neighbour OR apartment) (loud OR noise OR noisy OR stomping OR bass) -football -derby -United -City` | 1（另 3 則合格但與噪音無關，是社會新聞） | 約 50% | https://x.com/i/status/2116844016977240103 （鄰居一個月投訴 3 次噪音，237 讚，約 2 天前） |
| KEEP | `("decibel" OR "noise meter" OR "sound meter" OR "how loud is") -Aptos -crypto -trade` | 2 | 約 55%（排除前被加密貨幣「Decibel」洗版；排除條件尚未重跑） | https://x.com/i/status/2117050784861032514 （質疑球場噪音計，333 讚，約 1.5 天前）、https://x.com/i/status/2116664066387406907 （球場有多吵，798 讚，約 3 天前） |
| WEAK | `(restaurant OR restaurants OR bar OR gym) ("too loud" OR "so loud" OR "can't hear" OR "music is loud")` | 1（公共場所大聲講話，987 讚/27 回：https://x.com/i/status/2116586636628898002 ） | 約 35% | — |
| WEAK | `("white noise" OR "baby monitor" OR "sound machine") (baby OR nursery OR sleep)` | 3 則合格，但都在講育兒/監視器，不是噪音量 | 約 20% | — |

DROP：
- `upstairs neighbor(s)…`：合格的只有成人內容。
- `(concert OR show) ("so loud" OR earplugs…)`：多為追星文。
- `"hearing loss" OR tinnitus OR decibel(s)`：多為醫療機構貼文和 LRAD 政治文。
- 辦公室/除草機/工地噪音：0 合格。
- `"ear protection" OR earplugs…`：0 則相關合格。
- `"too loud" (movie OR fireworks…)`：0 則相關。

結論：分貝計最好的兩條路是「鄰居/公寓噪音」和「球場、場館有多吵」。後者有運動賽季加成，適合「我量了一下大概幾分貝」這類回覆。

## 3. 伸展 App

| 判定 | 查詢 | 本週合格（相關） | 相關率 | 例子 |
|---|---|---|---|---|
| KEEP（最強） | `(stretch OR stretches OR mobility) (desk OR "sitting all day" OR "tight hips" OR "lower back" OR "upper traps") -#ad` | 5 | 約 85% | https://x.com/i/status/2117301702088937749 （每晚 4 個伸展，2062 讚，約 26 小時前）、https://x.com/i/status/2117155333483151766 （下背伸展，1189 讚，約 36 小時前） |
| KEEP | `("sitting all day" OR "desk job" OR "sit at a desk") (back OR hips OR neck OR stretch OR posture)` | 2 | 約 80% | https://x.com/i/status/2115526651106767139 （久坐下背僵硬，531 讚，約 6 天前） |
| KEEP | `("stretching routine" OR "stretch routine" OR "daily stretches" OR "mobility routine")` | 1（另 2 則合格但不相關） | 約 60% | https://x.com/i/status/2116165192945930291 （60 秒下背活動，184 讚，約 4 天前） |
| KEEP | `(posture OR "work from home" OR WFH) (stretch OR stretches OR neck OR shoulders)` | 1 | 約 60% | https://x.com/i/status/2116902521461780665 （辦公桌毛巾伸展肩頸，160 讚，約 2 天前） |
| WEAK | `("tech neck" OR "neck pain" OR "stiff neck" OR "forward head")` | 0 | 約 70% | 真實抱怨很多但互動小 |
| WEAK | `("my back hurts" OR "my neck hurts" OR "back is killing me" OR "neck is killing me") (desk OR sitting OR work OR laptop OR stretch)` | 0 | 約 80%（最真實的需求） | — |

DROP：
- `"back pain" (stretch OR mobility OR fix)`：0 合格，多為整脊和廣告。
- `(fitness OR yoga…) app (subscription OR recommend…)`：0 合格，多為開發者自推。

注意：伸展類合格貼文幾乎都來自健身內容帳號，在底下推廣容易被看成蹭流量，回覆要先補充有用的動作或建議。

## 推薦／抱怨類（三個 App 共用）
沿用 `us-x-reply-targets-2026-11-03.md` 第 1～10 條；本次另外測的 app 推薦查詢（habit tracker、fitness app）沒有合格貼文。

## 限制
- 每個查詢只看前 25 則，合格數是「至少」而不是全部。
- 相關率是人工估計。
- 部分合格貼文已超過 48 小時，只能算「這個關鍵字每週會出現熱門文」的證據。
- `lang:en` 不代表是美國用戶。
