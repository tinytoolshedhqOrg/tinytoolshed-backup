import re
RULES=[
 ("隱私・網路工具（代理、廣告阻擋、加密通訊）", r"shadowrocket|stash|quantumult|loon|easytier|threema|teleguard|wipr|adguard|iverify|280blocker|광고 차단|unicorn|teamspeak|noir|tampermonkey|alook|fongo|imo video|socialfocus|untrap|dumbify|vpn"),
 ("相機・濾鏡・底片感", r"cam|camera|film|フィルム|카메라|필름|相機|底片|菲林|berry|베리|영뽀또|oldi|올디|analog|gika|기카|iy2k|lumy|chromagraph|procamera|photopills|shutter|无锐化|네거티브|youngphoto|rollie|롤리즈|blackvideo|ブラックビデオ|비디오 마스터|resolutioner|filca|ee35|moment pro|sun seeker"),
 ("考試・學習・語言", r"."),  # placeholder for genre 6017
]
GENRE={"6017":"考試・學習・語言","6013":"健康・睡眠・運動紀錄","6020":"健康・醫療參考","6011":"音樂創作・樂器練習","6010":"導航・測速・戶外","6003":"旅遊・戶外","6027":"繪圖・設計","6015":"記帳理財","6006":"參考工具（字典・宗教典籍）","6018":"閱讀・內容","6005":"通訊","6004":"運動・計時","6001":"天氣・災害警報","6016":"娛樂・惡搞","6000":"商務工具","6023":"食譜・飲食"}
MANUAL=[
 ("生活紀錄・日記・行事規劃", r"daypic|daygrid|上次是什麼時候|auday|cat calendar|calcs|streaks|心想事成|things 3|paprika|whisper notes|goblin tools|typedraw|camscanner|flickme|flkb|計算機鍵盤|短語鍵盤|mytan|heredis|site audit|quickbend|hotschedules|紫白飛星|龍躍八字|星夢|universalis|iliturgia|prophet|bíblia|josemaria|holyrics|القاعدة|spirit talker|靈體|해병|해군|babyphone|baby phone|baby led|halloween|hue|iconnecthue|画師牆紙|tierMaker|loto|real sensi|gerador de sensi|atvtools|runa|rpgplayer|ifacialmocap|aracersmart|forscan|necrophonic|manager for scooters|audyssey|virtualdj|動森"),
]
SUB=[("遠端連線・檔案・播放器",r"jump desktop|fe file|nplayer|plezy|imo video|fongo|gse smart|vesc"),("旅遊・戶外",r"wikicamps"),("生產力・鍵盤・掃描・AI筆記",r"camscanner"),("娛樂・惡搞",r"해병|해군|靈體|airpong"),("健康・醫療參考",r"squeezy"),("生活紀錄・日記・行事規劃",r"daypic|daygrid|上次是什麼時候|auday|cat calendar|calcs|streaks|心想事成|things 3"),
     ("生產力・鍵盤・掃描・AI筆記",r"whisper notes|goblin tools|camscanner|flickme|flkb|計算機鍵盤|短語鍵盤|mytan|typedraw|tampermonkey"),
     ("宗教・命理・靈異",r"紫白飛星|龍躍八字|universalis|iliturgia|prophet|bíblia|josemaria|holyrics|القاعدة|spirit talker|靈體"),
     ("嬰兒・家庭",r"babyphone|baby phone|baby led"),
     ("智慧家電・車用・硬體配套",r"hue|forscan|manager for scooters|audyssey|virtualdj|aracersmart|racechrono|qz fitness|necrophonic"),
     ("遊戲周邊工具",r"real sensi|gerador de sensi|atvtools|runa|rpgplayer|動森|tiermaker|loto"),
     ("食譜・飲食",r"paprika|fodmap|happycow"),]
def classify(name,genre):
  n=name.lower()
  if genre=="6014": return "遊戲"
  for k,p in SUB[:5]:
    if re.search(p,n,re.I): return k
  for k,p in RULES[:2]:
    if re.search(p,n): return k
  for k,p in SUB:
    if re.search(p,n,re.I): return k
  return GENRE.get(genre,"其他("+genre+")")
