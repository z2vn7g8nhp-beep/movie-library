"""影库的「宇宙」专题：漫威电影宇宙、DC 宇宙、异形宇宙。

这里是手写的底稿（片名 + 年份 + 中文名，角色 + 演员 + 出场作品），
运行一次会对照离线片库查出 IMDb 编号，写成网页用的 docs/universes.json：

    python scraper/universes.py --idx 片库索引目录 --out docs/universes.json

想加片子、加角色：改下面的 UNIVERSES，再跑一遍。
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

# ---------------------------------------------------------------- 作品
# (key, 英文片名, 年份, 中文名[, {"ty": 类型, "tl": 故事里的年份, "x": True 外传不计入大满贯}])
MCU_WORKS = [
    ("p1", "第一阶段", "Phase One", [
        ("im1", "Iron Man", 2008, "钢铁侠"),
        ("hulk", "The Incredible Hulk", 2008, "无敌浩克"),
        ("im2", "Iron Man 2", 2010, "钢铁侠2"),
        ("thor1", "Thor", 2011, "雷神"),
        ("cap1", "Captain America: The First Avenger", 2011, "美国队长"),
        ("av1", "The Avengers", 2012, "复仇者联盟"),
    ]),
    ("p2", "第二阶段", "Phase Two", [
        ("im3", "Iron Man 3", 2013, "钢铁侠3"),
        ("thor2", "Thor: The Dark World", 2013, "雷神2：黑暗世界"),
        ("cap2", "Captain America: The Winter Soldier", 2014, "美国队长2"),
        ("gotg1", "Guardians of the Galaxy", 2014, "银河护卫队"),
        ("av2", "Avengers: Age of Ultron", 2015, "复仇者联盟2：奥创纪元"),
        ("ant1", "Ant-Man", 2015, "蚁人"),
    ]),
    ("p3", "第三阶段", "Phase Three", [
        ("cw", "Captain America: Civil War", 2016, "美国队长3"),
        ("ds1", "Doctor Strange", 2016, "奇异博士"),
        ("gotg2", "Guardians of the Galaxy Vol. 2", 2017, "银河护卫队2"),
        ("sh", "Spider-Man: Homecoming", 2017, "蜘蛛侠：英雄归来"),
        ("thor3", "Thor: Ragnarok", 2017, "雷神3：诸神黄昏"),
        ("bp1", "Black Panther", 2018, "黑豹"),
        ("iw", "Avengers: Infinity War", 2018, "复仇者联盟3：无限战争"),
        ("ant2", "Ant-Man and the Wasp", 2018, "蚁人2：黄蜂女现身"),
        ("cm", "Captain Marvel", 2019, "惊奇队长"),
        ("eg", "Avengers: Endgame", 2019, "复仇者联盟4：终局之战"),
        ("ffh", "Spider-Man: Far from Home", 2019, "蜘蛛侠：英雄远征"),
    ]),
    ("p4", "第四阶段", "Phase Four", [
        ("wv", "WandaVision", 2021, "旺达幻视", {"ty": "ms"}),
        ("faws", "The Falcon and the Winter Soldier", 2021, "猎鹰与冬兵", {"ty": "ms"}),
        ("loki", "Loki", 2021, "洛基", {"ty": "s"}),
        ("bw", "Black Widow", 2021, "黑寡妇"),
        ("whatif", "What If...?", 2021, "假如…？", {"ty": "s"}),
        ("shang", "Shang-Chi and the Legend of the Ten Rings", 2021, "尚气与十环传奇"),
        ("eter", "Eternals", 2021, "永恒族"),
        ("hawk", "Hawkeye", 2021, "鹰眼", {"ty": "ms"}),
        ("nwh", "Spider-Man: No Way Home", 2021, "蜘蛛侠：英雄无归"),
        ("mk", "Moon Knight", 2022, "月光骑士", {"ty": "ms"}),
        ("ds2", "Doctor Strange in the Multiverse of Madness", 2022, "奇异博士2：疯狂多元宇宙"),
        ("msm", "Ms. Marvel", 2022, "惊奇少女", {"ty": "ms"}),
        ("thor4", "Thor: Love and Thunder", 2022, "雷神4：爱与雷霆"),
        ("shehulk", "She-Hulk: Attorney at Law", 2022, "女浩克", {"ty": "ms"}),
        ("wbn", "Werewolf by Night", 2022, "狼人之夜", {"ty": "tm"}),
        ("bp2", "Black Panther: Wakanda Forever", 2022, "黑豹2：瓦坎达万岁"),
        ("gotghs", "The Guardians of the Galaxy Holiday Special", 2022, "银河护卫队：假日特别篇", {"ty": "sp"}),
    ]),
    ("p5", "第五阶段", "Phase Five", [
        ("ant3", "Ant-Man and the Wasp: Quantumania", 2023, "蚁人与黄蜂女：量子狂潮"),
        ("gotg3", "Guardians of the Galaxy Vol. 3", 2023, "银河护卫队3"),
        ("si", "Secret Invasion", 2023, "秘密入侵", {"ty": "ms"}),
        ("marvels", "The Marvels", 2023, "惊奇队长2"),
        ("echo", "Echo", 2024, "回声", {"ty": "ms"}),
        ("dw", "Deadpool & Wolverine", 2024, "死侍与金刚狼"),
        ("agatha", "Agatha All Along", 2024, "阿加莎：一切都是她", {"ty": "ms"}),
        ("yfns", "Your Friendly Neighborhood Spider-Man", 2025, "你的好邻居蜘蛛侠", {"ty": "s"}),
        ("cap4", "Captain America: Brave New World", 2025, "美国队长4"),
        ("ddba", "Daredevil: Born Again", 2025, "夜魔侠：重生", {"ty": "s"}),
        ("tbolts", "Thunderbolts*", 2025, "雷霆特工队*"),
        ("ironheart", "Ironheart", 2025, "钢铁之心", {"ty": "ms"}),
        ("eow", "Eyes of Wakanda", 2025, "瓦坎达之眼", {"ty": "ms"}),
    ]),
    ("p6", "第六阶段", "Phase Six", [
        ("ff", "The Fantastic Four: First Steps", 2025, "神奇四侠：初露锋芒"),
        ("mz", "Marvel Zombies", 2025, "漫威僵尸", {"ty": "ms"}),
        ("wm", "Wonder Man", 2026, "奇迹人", {"ty": "s"}),
        ("bnd", "Spider-Man: Brand New Day", 2026, "蜘蛛侠：全新之日"),
        ("vq", "VisionQuest", 2026, "幻视任务", {"ty": "ms"}),
        ("doom", "Avengers: Doomsday", 2026, "复仇者联盟5：末日"),
        ("sw", "Avengers: Secret Wars", 2027, "复仇者联盟6：秘密战争"),
    ]),
]

DC_WORKS = [
    ("dceu", "DC 扩展宇宙", "DC Extended Universe", [
        ("mos", "Man of Steel", 2013, "超人：钢铁之躯"),
        ("bvs", "Batman v Superman: Dawn of Justice", 2016, "蝙蝠侠大战超人：正义黎明"),
        ("ss1", "Suicide Squad", 2016, "X特遣队"),
        ("ww1", "Wonder Woman", 2017, "神奇女侠"),
        ("jl", "Justice League", 2017, "正义联盟"),
        ("aqua1", "Aquaman", 2018, "海王"),
        ("shazam1", "Shazam!", 2019, "雷霆沙赞！"),
        ("bop", "Birds of Prey: And the Fantabulous Emancipation of One Harley Quinn", 2020, "猛禽小队和哈莉·奎茵"),
        ("ww84", "Wonder Woman 1984", 2020, "神奇女侠1984"),
        ("zsjl", "Zack Snyder's Justice League", 2021, "扎克·施奈德版正义联盟"),
        ("tss", "The Suicide Squad", 2021, "X特遣队：全员集结"),
        ("ba", "Black Adam", 2022, "黑亚当"),
        ("shazam2", "Shazam! Fury of the Gods", 2023, "雷霆沙赞！众神之怒"),
        ("flash", "The Flash", 2023, "闪电侠"),
        ("bb", "Blue Beetle", 2023, "蓝甲虫"),
        ("aqua2", "Aquaman and the Lost Kingdom", 2023, "海王2：失落的王国"),
    ]),
    ("dcu", "DCU 新宇宙", "DC Universe · Gods and Monsters", [
        ("pm", "Peacemaker", 2022, "和平使者", {"ty": "s"}),
        ("cc", "Creature Commandos", 2024, "怪物特攻队", {"ty": "s"}),
        ("superman", "Superman", 2025, "超人"),
        ("supergirl", "Supergirl", 2026, "超级少女"),
        ("lanterns", "Lanterns", 2026, "绿灯军团", {"ty": "s"}),
        ("clayface", "Clayface", 2026, "泥脸"),
        ("mot", "Man of Tomorrow", 2027, "明日之人"),
    ]),
    ("else", "Elseworlds 外传", "Elseworlds", [
        ("bb05", "Batman Begins", 2005, "蝙蝠侠：侠影之谜", {"x": True}),
        ("tdk", "The Dark Knight", 2008, "蝙蝠侠：黑暗骑士", {"x": True}),
        ("tdkr", "The Dark Knight Rises", 2012, "蝙蝠侠：黑暗骑士崛起", {"x": True}),
        ("joker", "Joker", 2019, "小丑", {"x": True}),
        ("batman", "The Batman", 2022, "新蝙蝠侠", {"x": True}),
        ("penguin", "The Penguin", 2024, "企鹅人", {"ty": "ms", "x": True}),
        ("joker2", "Joker: Folie à Deux", 2024, "小丑2：双重妄想", {"x": True}),
    ]),
]

ALIEN_WORKS = [
    ("main", "正传", "The Saga", [
        ("a1", "Alien", 1979, "异形", {"tl": 2122}),
        ("a2", "Aliens", 1986, "异形2", {"tl": 2179}),
        ("a3", "Alien³", 1992, "异形3", {"tl": 2179.5}),
        ("a4", "Alien Resurrection", 1997, "异形4：浴火重生", {"tl": 2381}),
        ("prom", "Prometheus", 2012, "普罗米修斯", {"tl": 2093}),
        ("cov", "Alien: Covenant", 2017, "异形：契约", {"tl": 2104}),
        ("rom", "Alien: Romulus", 2024, "异形：夺命舰", {"tl": 2142}),
        ("earth", "Alien: Earth", 2025, "异形：地球", {"ty": "s", "tl": 2120}),
    ]),
    ("avp", "异形大战铁血战士", "Alien vs. Predator", [
        ("avp", "AVP: Alien vs. Predator", 2004, "异形大战铁血战士", {"x": True, "tl": 2004}),
        ("avpr", "Aliens vs. Predator: Requiem", 2007, "异形大战铁血战士2", {"x": True, "tl": 2004.5}),
    ]),
]

# ---------------------------------------------------------------- 角色
# (key, 中文名, 英文名, 真名 / 版本, [演员], [出场作品], 主色)
# 演员为空的是生物（异形、抱脸虫……），只按出场作品点亮。
MCU_CHARS = [
    ("ironman", "钢铁侠", "Iron Man", "托尼·斯塔克", ["Robert Downey Jr."], "im1 hulk im2 av1 im3 av2 cw sh iw eg", "#C8303A"),
    ("cap", "美国队长", "Captain America", "史蒂夫·罗杰斯", ["Chris Evans"], "cap1 av1 thor2 cap2 av2 sh cw iw cm eg", "#2F5BB7"),
    ("thor", "雷神", "Thor", "索尔·奥丁森", ["Chris Hemsworth"], "thor1 av1 thor2 av2 ds1 thor3 iw eg thor4 doom", "#4A78C9"),
    ("hulk", "绿巨人", "Hulk", "布鲁斯·班纳", ["Mark Ruffalo", "Edward Norton"], "hulk av1 im3 av2 thor3 iw eg shang shehulk", "#4E9A4A"),
    ("widow", "黑寡妇", "Black Widow", "娜塔莎·罗曼诺夫", ["Scarlett Johansson"], "im2 av1 cap2 av2 cw iw cm eg bw", "#B3263A"),
    ("hawkeye", "鹰眼", "Hawkeye", "克林特·巴顿", ["Jeremy Renner"], "thor1 av1 av2 cw eg hawk", "#6B4FA8"),
    ("loki", "洛基", "Loki", "洛基·劳菲森", ["Tom Hiddleston"], "thor1 av1 thor2 thor3 iw eg loki doom", "#3E8B57"),
    ("fury", "尼克·弗瑞", "Nick Fury", "神盾局局长", ["Samuel L. Jackson"], "im1 im2 thor1 cap1 av1 cap2 av2 iw cm eg ffh si marvels", "#3B3B48"),
    ("pepper", "小辣椒", "Pepper Potts", "佩珀·波茨", ["Gwyneth Paltrow"], "im1 im2 av1 im3 sh iw eg", "#D9695F"),
    ("peggy", "佩吉·卡特", "Peggy Carter", "特工卡特", ["Hayley Atwell"], "cap1 cap2 ant1 eg whatif ds2", "#B8453C"),
    ("jane", "简·福斯特", "Jane Foster", "雷神·简", ["Natalie Portman"], "thor1 thor2 eg thor4", "#7A8FD6"),
    ("spidey", "蜘蛛侠", "Spider-Man", "彼得·帕克", ["Tom Holland"], "cw sh iw eg ffh nwh bnd", "#D2343F"),
    ("mj", "MJ", "MJ", "米歇尔·琼斯", ["Zendaya"], "sh ffh nwh bnd", "#A9577A"),
    ("strange", "奇异博士", "Doctor Strange", "斯蒂芬·斯特兰奇", ["Benedict Cumberbatch"], "ds1 thor3 iw eg nwh ds2", "#C4472F"),
    ("wong", "王", "Wong", "至尊法师", ["Benedict Wong"], "ds1 iw eg shang nwh ds2 shehulk", "#B9862F"),
    ("tchalla", "黑豹", "Black Panther", "特查拉", ["Chadwick Boseman"], "cw bp1 iw eg", "#5B3FA0"),
    ("shuri", "舒莉", "Shuri", "瓦坎达公主", ["Letitia Wright"], "bp1 iw eg bp2 doom", "#7B53C4"),
    ("okoye", "奥科耶", "Okoye", "朵拉米拉吉将军", ["Danai Gurira"], "bp1 iw eg bp2", "#A4373B"),
    ("killmonger", "杀戮者", "Killmonger", "埃里克·史蒂文斯", ["Michael B. Jordan"], "bp1 whatif", "#B88A2E"),
    ("starlord", "星爵", "Star-Lord", "彼得·奎尔", ["Chris Pratt"], "gotg1 gotg2 iw eg thor4 gotghs gotg3", "#C0552C"),
    ("gamora", "卡魔拉", "Gamora", "宇宙最致命的女人", ["Zoe Saldana"], "gotg1 gotg2 iw eg gotg3", "#3F9A6A"),
    ("rocket", "火箭浣熊", "Rocket", "89P13", ["Bradley Cooper"], "gotg1 gotg2 iw eg thor4 gotghs gotg3", "#A9743E"),
    ("groot", "格鲁特", "Groot", "我是格鲁特", ["Vin Diesel"], "gotg1 gotg2 iw eg thor4 gotghs gotg3", "#7C8F3A"),
    ("drax", "德拉克斯", "Drax", "毁灭者", ["Dave Bautista"], "gotg1 gotg2 iw eg thor4 gotghs gotg3", "#6E7E8C"),
    ("nebula", "星云", "Nebula", "灭霸的养女", ["Karen Gillan"], "gotg1 gotg2 iw eg thor4 gotghs gotg3", "#4E77A8"),
    ("mantis", "螳螂女", "Mantis", "共情者", ["Pom Klementieff"], "gotg2 iw eg thor4 gotghs gotg3", "#6EA55A"),
    ("antman", "蚁人", "Ant-Man", "斯科特·朗", ["Paul Rudd"], "ant1 cw ant2 eg ant3 doom", "#B6353A"),
    ("wasp", "黄蜂女", "The Wasp", "霍普·范·戴恩", ["Evangeline Lilly"], "ant1 ant2 eg ant3", "#C79A2A"),
    ("carol", "惊奇队长", "Captain Marvel", "卡罗尔·丹弗斯", ["Brie Larson"], "cm eg marvels", "#C23C4A"),
    ("wanda", "绯红女巫", "Scarlet Witch", "旺达·马克西莫夫", ["Elizabeth Olsen"], "cap2 av2 cw iw eg wv ds2", "#B0283F"),
    ("vision", "幻视", "Vision", "心灵宝石的化身", ["Paul Bettany"], "av2 cw iw eg wv vq", "#A33A55"),
    ("sam", "猎鹰", "Falcon", "山姆·威尔逊", ["Anthony Mackie"], "cap2 av2 ant1 cw iw eg faws cap4 doom", "#3C6EB5"),
    ("bucky", "冬兵", "Winter Soldier", "巴基·巴恩斯", ["Sebastian Stan"], "cap1 cap2 cw bp1 iw eg faws tbolts doom", "#5A6577"),
    ("rhodey", "战争机器", "War Machine", "詹姆斯·罗德", ["Don Cheadle", "Terrence Howard"], "im1 im2 im3 av2 cw iw eg faws si", "#6F7480"),
    ("thanos", "灭霸", "Thanos", "泰坦星的疯狂泰坦", ["Josh Brolin"], "gotg1 av2 iw eg", "#7D4FA6"),
    ("ultron", "奥创", "Ultron", "", ["James Spader"], "av2", "#8A8F9C"),
    ("hela", "海拉", "Hela", "死亡女神", ["Cate Blanchett"], "thor3", "#2E6B4A"),
    ("valkyrie", "女武神", "Valkyrie", "新阿斯加德国王", ["Tessa Thompson"], "thor3 eg thor4 marvels", "#4F6FA8"),
    ("kang", "征服者康", "Kang", "坚守者 / 胜者", ["Jonathan Majors"], "loki ant3", "#4D5FA3"),
    ("shangchi", "尚气", "Shang-Chi", "十环的继承人", ["Simu Liu"], "shang doom", "#C4422E"),
    ("moonknight", "月光骑士", "Moon Knight", "马克·斯佩克特", ["Oscar Isaac"], "mk", "#8C93A6"),
    ("kamala", "惊奇少女", "Ms. Marvel", "卡玛拉·汗", ["Iman Vellani"], "msm marvels", "#C04A6B"),
    ("monica", "莫妮卡", "Photon", "莫妮卡·兰博", ["Teyonah Parris"], "wv marvels", "#C79635"),
    ("jen", "女浩克", "She-Hulk", "珍妮弗·沃尔特斯", ["Tatiana Maslany"], "shehulk", "#5AA25A"),
    ("agatha", "阿加莎", "Agatha Harkness", "女巫", ["Kathryn Hahn"], "wv agatha", "#6D4C9C"),
    ("yelena", "叶莲娜", "Yelena Belova", "黑寡妇的妹妹", ["Florence Pugh"], "bw hawk tbolts doom", "#6C7F9A"),
    ("redguardian", "红色卫士", "Red Guardian", "阿列克谢", ["David Harbour"], "bw tbolts doom", "#B23A3A"),
    ("usagent", "美国特工", "U.S. Agent", "约翰·沃克", ["Wyatt Russell"], "faws tbolts doom", "#3B5E9C"),
    ("ghost", "幽灵", "Ghost", "艾娃·斯塔尔", ["Hannah John-Kamen"], "ant2 tbolts doom", "#8E9AAE"),
    ("sentry", "哨兵", "Sentry", "鲍勃", ["Lewis Pullman"], "tbolts doom", "#D0A43A"),
    ("kate", "凯特·毕肖普", "Kate Bishop", "新鹰眼", ["Hailee Steinfeld"], "hawk", "#7652B5"),
    ("echo", "回声", "Echo", "玛雅·洛佩兹", ["Alaqua Cox"], "hawk echo", "#7A4E3C"),
    ("daredevil", "夜魔侠", "Daredevil", "马特·默多克", ["Charlie Cox"], "nwh shehulk echo ddba", "#9E2630"),
    ("kingpin", "金并", "Kingpin", "威尔逊·菲斯克", ["Vincent D'Onofrio"], "hawk echo ddba", "#4A4A52"),
    ("riri", "钢铁之心", "Ironheart", "莉莉·威廉姆斯", ["Dominique Thorne"], "bp2 ironheart", "#C0453E"),
    ("deadpool", "死侍", "Deadpool", "韦德·威尔逊", ["Ryan Reynolds"], "dw", "#B8232E"),
    ("wolverine", "金刚狼", "Wolverine", "罗根", ["Hugh Jackman"], "dw", "#D1A72E"),
    ("wonderman", "奇迹人", "Wonder Man", "西蒙·威廉姆斯", ["Yahya Abdul-Mateen II"], "wm", "#B5492F"),
    ("reed", "神奇先生", "Mister Fantastic", "里德·理查兹", ["Pedro Pascal"], "ff doom", "#3D79BF"),
    ("sue", "隐形女", "Invisible Woman", "苏·斯托姆", ["Vanessa Kirby"], "ff doom", "#4B8AC6"),
    ("johnny", "霹雳火", "Human Torch", "约翰尼·斯托姆", ["Joseph Quinn"], "ff doom", "#D5632B"),
    ("ben", "石头人", "The Thing", "本·格林", ["Ebon Moss-Bachrach"], "ff doom", "#B57A44"),
    ("galactus", "行星吞噬者", "Galactus", "银河吞噬者", ["Ralph Ineson"], "ff", "#5D4C8E"),
    ("silversurfer", "银影侠", "Silver Surfer", "沙拉·芭尔", ["Julia Garner"], "ff", "#9CA8BC"),
    ("doctordoom", "毁灭博士", "Doctor Doom", "维克多·冯·杜姆", ["Robert Downey Jr."], "doom sw", "#4C6B4B"),
]

DC_CHARS = [
    ("superman_c", "超人", "Superman", "DCEU · 卡维尔", ["Henry Cavill"], "mos bvs jl zsjl ba", "#2F5EB8"),
    ("batman_a", "蝙蝠侠", "Batman", "DCEU · 本·阿弗莱克", ["Ben Affleck"], "bvs ss1 jl zsjl flash", "#3A3D4A"),
    ("ww", "神奇女侠", "Wonder Woman", "戴安娜·普林斯", ["Gal Gadot"], "bvs ww1 jl zsjl ww84 flash shazam2", "#B8323C"),
    ("aquaman", "海王", "Aquaman", "亚瑟·库瑞", ["Jason Momoa"], "bvs jl aqua1 zsjl flash aqua2", "#2E8A86"),
    ("flash", "闪电侠", "The Flash", "巴里·艾伦", ["Ezra Miller"], "bvs ss1 jl zsjl flash", "#C8352F"),
    ("cyborg", "钢骨", "Cyborg", "维克多·斯通", ["Ray Fisher"], "bvs jl zsjl", "#7D8794"),
    ("mera", "湄拉", "Mera", "泽贝尔公主", ["Amber Heard"], "jl aqua1 zsjl aqua2", "#3E9A6E"),
    ("zod", "佐德将军", "General Zod", "氪星将军", ["Michael Shannon"], "mos bvs flash", "#5B6070"),
    ("lex_e", "莱克斯·卢瑟", "Lex Luthor", "DCEU · 艾森伯格", ["Jesse Eisenberg"], "bvs jl zsjl", "#6B7C4A"),
    ("harley", "小丑女", "Harley Quinn", "哈莉·奎茵", ["Margot Robbie"], "ss1 bop tss", "#D24B78"),
    ("joker_l", "小丑", "The Joker", "DCEU · 杰瑞德·莱托", ["Jared Leto"], "ss1 zsjl", "#5BA05B"),
    ("deadshot", "死亡射手", "Deadshot", "弗洛伊德·劳顿", ["Will Smith"], "ss1", "#8A6E4A"),
    ("waller", "阿曼达·沃勒", "Amanda Waller", "X特遣队的主人", ["Viola Davis"], "ss1 tss pm cc", "#4E4A5E"),
    ("bloodsport", "血腥运动", "Bloodsport", "罗伯特·杜波依斯", ["Idris Elba"], "tss", "#9C3A3A"),
    ("peacemaker", "和平使者", "Peacemaker", "克里斯托弗·史密斯", ["John Cena"], "tss pm", "#C7A33A"),
    ("shazam", "沙赞", "Shazam", "比利·巴特森", ["Zachary Levi"], "shazam1 shazam2", "#C8392E"),
    ("blackadam", "黑亚当", "Black Adam", "泰斯-亚当", ["Dwayne Johnson"], "ba", "#3E3A30"),
    ("bluebeetle", "蓝甲虫", "Blue Beetle", "杰米·雷耶斯", ["Xolo Maridueña"], "bb", "#2E7DC2"),
    ("superman_d", "超人", "Superman", "DCU · 科伦斯维特", ["David Corenswet"], "superman mot", "#2A64C9"),
    ("lois", "露易丝·莱恩", "Lois Lane", "星球日报王牌记者", ["Rachel Brosnahan"], "superman mot", "#B44A5A"),
    ("lex_h", "莱克斯·卢瑟", "Lex Luthor", "DCU · 霍尔特", ["Nicholas Hoult"], "superman mot", "#4C7A54"),
    ("krypto", "小氪", "Krypto", "超人的狗狗", [], "superman supergirl", "#D0A03A"),
    ("supergirl", "超级少女", "Supergirl", "卡拉·佐-艾尔", ["Milly Alcock"], "superman supergirl", "#C23A48"),
    ("guy", "盖·加德纳", "Guy Gardner", "绿灯侠", ["Nathan Fillion"], "superman pm lanterns", "#3A9A55"),
    ("terrific", "了不起先生", "Mister Terrific", "迈克尔·霍尔特", ["Edi Gathegi"], "superman", "#3E4E7A"),
    ("hawkgirl", "鹰女", "Hawkgirl", "肯德拉·桑德斯", ["Isabela Merced"], "superman", "#B0673A"),
    ("hal", "哈尔·乔丹", "Hal Jordan", "绿灯侠", ["Kyle Chandler"], "lanterns", "#2F9A5A"),
    ("john", "约翰·斯图尔特", "John Stewart", "绿灯侠", ["Aaron Pierre"], "lanterns", "#2A8A5E"),
    ("flag", "里克·弗拉格", "Rick Flag Sr.", "怪物特攻队队长", ["Frank Grillo"], "cc pm superman", "#5E6B4A"),
    ("clayface", "泥脸", "Clayface", "马特·黑根", ["Tom Rhys Harries"], "clayface", "#8C6B4A"),
    ("batman_b", "蝙蝠侠", "Batman", "诺兰三部曲 · 贝尔", ["Christian Bale"], "bb05 tdk tdkr", "#2E3038"),
    ("joker_h", "小丑", "The Joker", "诺兰版 · 希斯·莱杰", ["Heath Ledger"], "tdk", "#6E4C9A"),
    ("bane", "贝恩", "Bane", "黑暗骑士崛起", ["Tom Hardy"], "tdkr", "#5E5546"),
    ("catwoman_h", "猫女", "Catwoman", "诺兰版 · 安妮·海瑟薇", ["Anne Hathaway"], "tdkr", "#3E3A4A"),
    ("batman_p", "蝙蝠侠", "Batman", "《新蝙蝠侠》· 帕丁森", ["Robert Pattinson"], "batman", "#3A2E2E"),
    ("catwoman_k", "猫女", "Catwoman", "《新蝙蝠侠》· 佐伊·克罗维兹", ["Zoë Kravitz"], "batman", "#4A3A52"),
    ("penguin", "企鹅人", "The Penguin", "奥兹·科布", ["Colin Farrell"], "batman penguin", "#4E5A48"),
    ("joker_p", "小丑", "Joker", "《小丑》· 华金·菲尼克斯", ["Joaquin Phoenix"], "joker joker2", "#B5463A"),
    ("lee", "哈莉·奎茵", "Lee Quinzel", "《小丑2》· Lady Gaga", ["Lady Gaga"], "joker2", "#B9476F"),
]

ALIEN_CHARS = [
    ("ripley", "雷普利", "Ellen Ripley", "诺斯特罗莫号准尉", ["Sigourney Weaver"], "a1 a2 a3 a4", "#6C7A5A"),
    ("xeno", "异形", "Xenomorph", "完美的生物", [], "a1 a2 a3 a4 cov rom earth avp avpr", "#2E3A3A"),
    ("facehugger", "抱脸虫", "Facehugger", "寄生的第一步", [], "a1 a2 a3 a4 cov rom earth avp avpr", "#8E8A6A"),
    ("chestburster", "破胸者", "Chestburster", "从胸口出生", [], "a1 a2 a3 a4 cov rom earth avp avpr", "#8A4A3A"),
    ("queen", "异形女王", "Alien Queen", "巢穴之母", [], "a2 a3 avp", "#3A3048"),
    ("jones", "琼斯猫", "Jonesy", "诺斯特罗莫号的橘猫", [], "a1 a2", "#C9873A"),
    ("dallas", "达拉斯", "Dallas", "诺斯特罗莫号船长", ["Tom Skerritt"], "a1", "#5A6A7A"),
    ("kane", "凯恩", "Kane", "第一个被抱脸的人", ["John Hurt"], "a1", "#7A6A5A"),
    ("ash", "艾什", "Ash", "科学官 · 合成人", ["Ian Holm"], "a1", "#9AA0A8"),
    ("lambert", "兰伯特", "Lambert", "领航员", ["Veronica Cartwright"], "a1", "#7A5A6A"),
    ("parker", "帕克", "Parker", "总工程师", ["Yaphet Kotto"], "a1", "#5A5A48"),
    ("hicks", "希克斯", "Hicks", "殖民海军陆战队下士", ["Michael Biehn"], "a2", "#4E5E3E"),
    ("hudson", "哈德森", "Hudson", "“游戏结束了，伙计！”", ["Bill Paxton"], "a2", "#6A6A4A"),
    ("vasquez", "瓦斯奎兹", "Vasquez", "智能炮手", ["Jenette Goldstein"], "a2", "#5E4A3E"),
    ("newt", "纽特", "Newt", "哈德利希望殖民地的幸存者", ["Carrie Henn"], "a2", "#C49A6A"),
    ("bishop", "毕晓普", "Bishop", "合成人", ["Lance Henriksen"], "a2 a3", "#A8ACB4"),
    ("call", "考尔", "Call", "第二代合成人", ["Winona Ryder"], "a4", "#8A7A9A"),
    ("shaw", "伊丽莎白·肖", "Elizabeth Shaw", "考古学家", ["Noomi Rapace"], "prom cov", "#6A8A9A"),
    ("david", "大卫", "David", "合成人 · 造物者", ["Michael Fassbender"], "prom cov", "#B8BCC4"),
    ("vickers", "维克斯", "Meredith Vickers", "维兰德公司主管", ["Charlize Theron"], "prom", "#8A9AA8"),
    ("engineer", "工程师", "Engineer", "人类的造物主", [], "prom cov", "#C4C8CE"),
    ("daniels", "丹尼尔斯", "Daniels", "契约号大副", ["Katherine Waterston"], "cov", "#6A7A6A"),
    ("rain", "瑞恩", "Rain Carradine", "杰克逊星的矿工", ["Cailee Spaeny"], "rom", "#6A7EA0"),
    ("andy", "安迪", "Andy", "瑞恩的合成人弟弟", ["David Jonsson"], "rom", "#8A6A4A"),
    ("wendy", "温蒂", "Wendy", "第一个混合体", ["Sydney Chandler"], "earth", "#9A7AA8"),
    ("kirsh", "柯什", "Kirsh", "合成人", ["Timothy Olyphant"], "earth", "#B0B4BA"),
    ("predator", "铁血战士", "Predator", "猎人", [], "avp avpr", "#6A6A3A"),
]

# ---------------------------------------------------------------- 套牌：集齐一组角色解锁
MCU_DECKS = [
    ("avengers", "初代复仇者", "The Avengers", "ironman cap thor hulk widow hawkeye", "🛡"),
    ("guardians", "银河护卫队", "Guardians of the Galaxy", "starlord gamora rocket groot drax nebula mantis", "🌌"),
    ("wakanda", "瓦坎达万岁", "Wakanda Forever", "tchalla shuri okoye killmonger", "🐾"),
    ("mystic", "至尊法师与魔法", "Masters of the Mystic Arts", "strange wong wanda agatha", "🔮"),
    ("asgard", "阿斯加德", "Asgard", "thor loki jane valkyrie hela", "⚡"),
    ("spidey", "友好邻居", "Friendly Neighborhood", "spidey mj ironman", "🕸"),
    ("thunderbolts", "雷霆特工队*", "Thunderbolts*", "yelena bucky redguardian usagent ghost sentry", "⭐"),
    ("ff", "神奇四侠", "Fantastic Four", "reed sue johnny ben", "④"),
    ("street", "街头英雄", "Street Level", "daredevil kingpin echo kate", "🌃"),
    ("villains", "宿敌", "Big Bads", "thanos ultron hela killmonger kang", "💀"),
]
DC_DECKS = [
    ("jl", "正义联盟", "Justice League", "superman_c batman_a ww aquaman flash cyborg", "⭐"),
    ("squad", "X 特遣队", "Task Force X", "harley deadshot waller bloodsport peacemaker", "🎯"),
    ("gang", "正义帮", "Justice Gang", "guy terrific hawkgirl", "💚"),
    ("lanterns", "绿灯军团", "Green Lantern Corps", "guy hal john", "🟢"),
    ("house_el", "超人一家", "House of El", "superman_d supergirl krypto lois", "🔰"),
    ("bats", "三代蝙蝠侠", "Three Batmen", "batman_b batman_a batman_p", "🦇"),
    ("jokers", "三代小丑", "Three Jokers", "joker_h joker_l joker_p", "🃏"),
    ("cats", "猫女", "Catwomen", "catwoman_h catwoman_k", "🐈‍⬛"),
]
ALIEN_DECKS = [
    ("nostromo", "诺斯特罗莫号船员", "Crew of the Nostromo", "ripley dallas kane ash lambert parker jones", "🚀"),
    ("marines", "殖民海军陆战队", "Colonial Marines", "hicks hudson vasquez bishop newt", "🪖"),
    ("life", "异形生命周期", "Life Cycle", "facehugger chestburster xeno queen", "🥚"),
    ("synth", "合成人", "Synthetics", "ash bishop call david andy kirsh", "🤖"),
    ("makers", "造物者", "The Makers", "engineer david shaw vickers", "🧬"),
]

UNIVERSES = [
    {"id": "mcu", "n": "漫威电影宇宙", "en": "Marvel Cinematic Universe", "short": "MCU",
     "tag": "从钢铁侠的第一套战甲开始，一路走到多元宇宙。",
     "theme": ["#C8303A", "#E7B54A", "#2A1A2E"], "sections": MCU_WORKS, "chars": MCU_CHARS, "decks": MCU_DECKS,
     "sagas": [["无限传奇", "The Infinity Saga", "p1 p2 p3"], ["多元宇宙传奇", "The Multiverse Saga", "p4 p5 p6"]],
     "wd": ["Q642878"]},
    {"id": "dc", "n": "DC 宇宙", "en": "DC Universe", "short": "DC",
     "tag": "从钢铁之躯到众神与怪物，再加上哥谭的几位外传主角。",
     "theme": ["#2A64C9", "#C9A46C", "#141B2E"], "sections": DC_WORKS, "chars": DC_CHARS, "decks": DC_DECKS,
     "wd": ["Q18281265", "Q116778263"]},
    {"id": "alien", "n": "异形宇宙", "en": "Alien Universe", "short": "ALIEN",
     "tag": "在太空里，没人听得见你的尖叫。",
     "theme": ["#5E8A6A", "#B8C4A8", "#0E1614"], "sections": ALIEN_WORKS, "chars": ALIEN_CHARS, "decks": ALIEN_DECKS,
     "timeline": True, "wd": ["Q1990792"]},
]


# ---------------------------------------------------------------- 对照离线片库
def norm(s):
    s = "".join(c for c in unicodedata.normalize("NFKD", s or "") if not unicodedata.combining(c))
    s = s.lower().replace("&", "and").replace("³", "3")
    return re.sub(r"[\W_]+", "", s)


def load_index(idx):
    rows = []
    for f in ("s1.txt", "s2.txt"):
        for line in (idx / f).read_text(encoding="utf-8").splitlines():
            x = line.split("\t")
            if len(x) < 11:
                continue
            rows.append({"id": "tt" + x[0], "t": x[1], "y": int(x[2] or 0), "n": x[4], "o": x[5], "cn": x[6],
                         "v": int(x[10] or 0)})
    return rows


def find_title(rows, by_norm, title, year, ty):
    cands = by_norm.get(norm(title), [])
    best = None
    for r in cands:
        dy = abs(r["y"] - year) if r["y"] else 3
        if dy > 1:
            continue
        score = (dy == 0, (r["t"] == ty) if ty else r["t"] in ("m", "tm"), r["v"])
        if not best or score > best[0]:
            best = (score, r)
    return best[1] if best else None


def crew_of(idx, tid, cache):
    n = 512
    i = int(tid[2:]) % n
    if i not in cache:
        m = {}
        p = idx / "p" / f"{i}.txt"
        if p.exists():
            for line in p.read_text(encoding="utf-8").splitlines():
                x = line.split("\t")
                ppl = [q.split(":", 1) for col in (x[3:5] if len(x) > 4 else []) for q in col.split("|") if ":" in q]
                m["tt" + x[0]] = {"nm" + a: b for a, b in ppl}
        cache[i] = m
    return cache[i].get(tid, {})


def build(idx, out):
    rows = load_index(idx)
    by_norm = {}
    for r in rows:
        for k in {norm(r["n"]), norm(r["o"])}:
            if k:
                by_norm.setdefault(k, []).append(r)
    names = {}
    for line in (idx / "names.txt").read_text(encoding="utf-8").splitlines():
        x = line.split("\t")
        if len(x) >= 3:
            names.setdefault(norm(x[1]), []).append(("nm" + x[0], int(x[2] or 0)))
    info = json.loads((idx / "info.json").read_text(encoding="utf-8"))
    shard_cache, misses, res = {}, [], []
    for u in UNIVERSES:
        works, secs, key2id = [], [], {}
        for sk, sn, sen, items in u["sections"]:
            keys = []
            for it in items:
                key, title, year, cn = it[:4]
                ex = it[4] if len(it) > 4 else {}
                r = find_title(rows, by_norm, title, year, ex.get("ty"))
                if not r:
                    misses.append(f"{u['id']}: {title} ({year})")
                w = {"k": key, "id": r["id"] if r else "", "en": title, "y": year, "cn": cn, "sec": sk}
                if ex.get("x"):
                    w["x"] = 1
                if "tl" in ex:
                    w["tl"] = ex["tl"]
                if ex.get("ty"):
                    w["ty"] = ex["ty"]
                works.append(w)
                keys.append(key)
                key2id[key] = w["id"]
            secs.append({"k": sk, "n": sn, "en": sen})
        chars = []
        for ck, cn, en, sub, actors, ws, color in u["chars"]:
            wl = ws.split()
            for k in wl:
                if k not in key2id:
                    raise SystemExit(f"{u['id']} 角色 {ck} 的作品 {k} 不存在")
            crew = {}
            for k in wl:
                if key2id[k]:
                    crew.update(crew_of(idx, key2id[k], shard_cache))
            ids = []
            for a in actors:
                cands = names.get(norm(a), []) + [(i, 0) for i, n in crew.items() if norm(n) == norm(a)]
                hit = [c for c in cands if c[0] in crew]
                pick = (hit or sorted(cands, key=lambda c: -c[1]) or [("", 0)])[0][0]
                if not pick:
                    misses.append(f"{u['id']}: 演员 {a}（{cn}）")
                elif not hit:
                    print(f"  提示：{a} 不在 {ck} 出场作品的主演表里，按名字取了 {pick}", file=sys.stderr)
                ids.append([pick, a])
            chars.append({"k": ck, "cn": cn, "en": en, "sub": sub, "a": ids, "w": wl, "c": color})
        decks = []
        for dk, dn, den, mem, ic in u["decks"]:
            ml = mem.split()
            for m in ml:
                if m not in {c["k"] for c in chars}:
                    raise SystemExit(f"{u['id']} 套牌 {dk} 的角色 {m} 不存在")
            decks.append({"k": dk, "n": dn, "en": den, "m": ml, "ic": ic})
        o = {k: u[k] for k in ("id", "n", "en", "short", "tag", "theme", "wd") if k in u}
        o.update({"secs": secs, "works": works, "chars": chars, "decks": decks})
        if u.get("sagas"):
            o["sagas"] = [{"n": a, "en": b, "secs": c.split()} for a, b, c in u["sagas"]]
        if u.get("timeline"):
            o["timeline"] = True
        res.append(o)
    Path(out).write_text(json.dumps({"built": info.get("built"), "universes": res}, ensure_ascii=False,
                                    separators=(",", ":")) + "\n", encoding="utf-8")
    for m in misses:
        print("  没找到：" + m, file=sys.stderr)
    print(f"宇宙 {len(res)} 个，作品 {sum(len(u['works']) for u in res)} 部，角色 {sum(len(u['chars']) for u in res)} 位，"
          f"没对上 {len(misses)} 条")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--idx", required=True)
    ap.add_argument("--out", default="docs/universes.json")
    a = ap.parse_args()
    build(Path(a.idx), a.out)
