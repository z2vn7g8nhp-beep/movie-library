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
    # 反派、配角、多元宇宙来客
    ("namor", "纳摩", "Namor", "塔洛肯之王", ["Tenoch Huerta"], "bp2 doom", "#2E8A86"),
    ("mysterio", "神秘客", "Mysterio", "昆汀·贝克", ["Jake Gyllenhaal"], "ffh", "#5E8E6E"),
    ("vulture", "秃鹫", "Vulture", "阿德里安·图姆斯", ["Michael Keaton"], "sh", "#4A5A6A"),
    ("redskull", "红骷髅", "Red Skull", "约翰·施密特", ["Hugo Weaving", "Ross Marquand"], "cap1 iw eg", "#B02A2A"),
    ("ego", "伊戈", "Ego", "活体星球", ["Kurt Russell"], "gotg2", "#6A8AC0"),
    ("yondu", "勇度", "Yondu", "掠夺者首领", ["Michael Rooker"], "gotg1 gotg2", "#3E6E9A"),
    ("ronan", "罗南", "Ronan", "指控者", ["Lee Pace"], "gotg1 cm", "#3A3A6A"),
    ("zemo", "泽莫男爵", "Baron Zemo", "赫尔穆特·泽莫", ["Daniel Brühl"], "cw faws", "#6A3A5A"),
    ("adam", "亚当·术士", "Adam Warlock", "茧中诞生", ["Will Poulter"], "gotg3", "#C9A040"),
    ("highevo", "至高进化", "High Evolutionary", "火箭的“创造者”", ["Chukwudi Iwuji"], "gotg3", "#8A3A3A"),
    ("gorr", "弑神者格尔", "Gorr", "手握弑神剑", ["Christian Bale"], "thor4", "#5A5A5A"),
    ("talos", "塔罗斯", "Talos", "斯克鲁人将军", ["Ben Mendelsohn"], "cm ffh si", "#4E8A4E"),
    ("hank", "汉克·皮姆", "Hank Pym", "初代蚁人", ["Michael Douglas"], "ant1 ant2 eg ant3", "#8A3A3A"),
    ("janet", "珍妮特", "Janet van Dyne", "初代黄蜂女", ["Michelle Pfeiffer"], "ant2 eg ant3", "#C79A2A"),
    ("happy", "哈皮", "Happy Hogan", "托尼的保镖兼司机", ["Jon Favreau"], "im1 im2 im3 sh eg ffh nwh", "#6A6A7A"),
    ("ned", "内德", "Ned Leeds", "彼得的好兄弟", ["Jacob Batalon"], "sh iw ffh nwh", "#C08A3A"),
    ("goblin", "绿魔", "Green Goblin", "诺曼·奥斯本", ["Willem Dafoe"], "nwh", "#4E8A3A"),
    ("ock", "章鱼博士", "Doctor Octopus", "奥托·奥克塔维斯", ["Alfred Molina"], "nwh", "#8A6A3A"),
    ("electro", "电光人", "Electro", "马克斯·狄龙", ["Jamie Foxx"], "nwh", "#3A8AC9"),
    ("sandman", "沙人", "Sandman", "弗林特·马可", ["Thomas Haden Church"], "nwh", "#B89A6A"),
    ("lizard", "蜥蜴博士", "The Lizard", "柯特·康纳斯", ["Rhys Ifans"], "nwh", "#4E7A3A"),
    ("spidey_t", "蜘蛛侠", "Spider-Man", "托比版 · 彼得·帕克", ["Tobey Maguire"], "nwh", "#C23A3A"),
    ("spidey_a", "蜘蛛侠", "Spider-Man", "加菲尔德版 · 彼得·帕克", ["Andrew Garfield"], "nwh", "#B8323C"),
    ("wenwu", "文武", "Wenwu", "十环之主", ["Tony Leung Chiu-wai"], "shang", "#B88A2E"),
    ("sylvie", "希尔薇", "Sylvie", "洛基的变体", ["Sophia Di Martino"], "loki", "#6A8A3A"),
    ("mobius", "莫比乌斯", "Mobius", "时间变异管理局探员", ["Owen Wilson"], "loki", "#8A7A5A"),
    ("sersi", "瑟茜", "Sersi", "永恒族", ["Gemma Chan"], "eter", "#C08AAA"),
    ("ikaris", "伊卡里斯", "Ikaris", "永恒族", ["Richard Madden"], "eter", "#C9A04A"),
    ("america", "美国小姐", "America Chavez", "穿梭多元宇宙的少女", ["Xochitl Gomez"], "ds2", "#3E6EB5"),
    ("taskmaster", "模仿大师", "Taskmaster", "安东尼娅", ["Olga Kurylenko"], "bw tbolts", "#6A6A7A"),
    ("val", "瓦伦蒂娜", "Valentina", "神秘的“瓦尔”", ["Julia Louis-Dreyfus"], "faws bw tbolts", "#4A4A5A"),
    ("abomination", "憎恶", "Abomination", "埃米尔·布朗斯基", ["Tim Roth"], "hulk shang shehulk", "#5A7A4A"),
    ("ross", "罗斯 / 红浩克", "Red Hulk", "萨迪厄斯·罗斯", ["William Hurt", "Harrison Ford"], "hulk cw iw eg bw cap4", "#B8323C"),
    ("leader", "领袖", "The Leader", "塞缪尔·斯特恩斯", ["Tim Blake Nelson"], "hulk cap4", "#6A9A4A"),
    ("x23", "X-23", "X-23", "劳拉", ["Dafne Keen"], "dw", "#5A5A6A"),
    ("elektra", "艾丽卡", "Elektra", "女刺客", ["Jennifer Garner"], "dw", "#A3263A"),
    ("blade", "刀锋战士", "Blade", "吸血鬼猎人", ["Wesley Snipes"], "dw", "#3A3A3A"),
    ("gambit", "牌皇", "Gambit", "雷米·勒博", ["Channing Tatum"], "dw doom", "#8A3A6A"),
    ("cassandra", "卡珊德拉·诺娃", "Cassandra Nova", "X 教授的双胞胎妹妹", ["Emma Corrin"], "dw", "#5A4A6A"),
    ("xavier", "X 教授", "Professor X", "查尔斯·泽维尔", ["Patrick Stewart"], "ds2 doom", "#4A5A8A"),
    ("magneto", "万磁王", "Magneto", "埃里克·兰谢尔", ["Ian McKellen"], "doom", "#8A2A4A"),
    # 阿斯加德、神盾局、钢铁侠的反派……
    ("odin", "奥丁", "Odin", "众神之父", ["Anthony Hopkins"], "thor1 thor2 thor3", "#C9A04A"),
    ("frigga", "弗丽嘉", "Frigga", "阿斯加德王后", ["Rene Russo"], "thor1 thor2 eg", "#B88AAA"),
    ("heimdall", "海姆达尔", "Heimdall", "彩虹桥守护者", ["Idris Elba"], "thor1 thor2 av2 thor3 iw thor4", "#C9A040"),
    ("sif", "希芙", "Sif", "阿斯加德女战士", ["Jaimie Alexander"], "thor1 thor2 thor4", "#8A6A5A"),
    ("korg", "克尔格", "Korg", "石头人角斗士", ["Taika Waititi"], "thor3 eg thor4", "#8A8A7A"),
    ("grandmaster", "宗师", "Grandmaster", "萨卡星的统治者", ["Jeff Goldblum"], "thor3", "#C9803A"),
    ("malekith", "马勒基斯", "Malekith", "黑暗精灵之王", ["Christopher Eccleston"], "thor2", "#4A4A6A"),
    ("mariahill", "玛丽亚·希尔", "Maria Hill", "神盾局副局长", ["Cobie Smulders"], "av1 cap2 av2 iw eg ffh si", "#3A4A6A"),
    ("coulson", "寇森", "Phil Coulson", "神盾局特工", ["Clark Gregg"], "im1 im2 thor1 av1 cm", "#5A6A7A"),
    ("sharon", "莎朗·卡特", "Sharon Carter", "特工 13", ["Emily VanCamp"], "cap2 cw faws", "#8A6A6A"),
    ("pierce", "皮尔斯", "Alexander Pierce", "世界安全理事会", ["Robert Redford"], "cap2 eg", "#5A5A6A"),
    ("crossbones", "交叉骨", "Crossbones", "布洛克·朗姆洛", ["Frank Grillo"], "cap2 cw eg", "#6A4A3A"),
    ("howard", "霍华德·斯塔克", "Howard Stark", "托尼的父亲", ["Dominic Cooper", "John Slattery"], "cap1 im2 ant1 cw eg", "#8A7A5A"),
    ("obadiah", "铁霸王", "Iron Monger", "奥巴代亚·斯坦", ["Jeff Bridges"], "im1", "#5A5A5A"),
    ("whiplash", "鞭索", "Whiplash", "伊万·万科", ["Mickey Rourke"], "im2", "#6A7A8A"),
    ("hammer", "贾斯汀·汉默", "Justin Hammer", "汉默工业", ["Sam Rockwell"], "im2", "#7A6A8A"),
    ("killian", "奇利安", "Aldrich Killian", "绝境病毒", ["Guy Pearce"], "im3", "#C9603A"),
    ("slattery", "特雷弗", "Trevor Slattery", "冒牌“满大人”", ["Ben Kingsley"], "im3 shang wm", "#B88A3A"),
    ("mordo", "莫度", "Mordo", "卡玛泰姬的法师", ["Chiwetel Ejiofor"], "ds1 ds2", "#6A4A3A"),
    ("ancientone", "古一", "The Ancient One", "至尊法师", ["Tilda Swinton"], "ds1 eg", "#C9A04A"),
    ("kaecilius", "卡西利亚斯", "Kaecilius", "黑暗法师", ["Mads Mikkelsen"], "ds1", "#6A3A5A"),
    ("clea", "克莉娅", "Clea", "黑暗维度的女术士", ["Charlize Theron"], "ds2", "#6A3A8A"),
    ("mbaku", "姆巴库", "M'Baku", "加巴里部落首领", ["Winston Duke"], "bp1 iw eg bp2 doom", "#6A5A3A"),
    ("nakia", "娜吉雅", "Nakia", "瓦坎达间谍", ["Lupita Nyong'o"], "bp1 eg bp2", "#3E8A5A"),
    ("ramonda", "拉蒙达", "Ramonda", "瓦坎达太后", ["Angela Bassett"], "bp1 eg bp2", "#8A6AA0"),
    ("klaw", "克劳", "Ulysses Klaw", "振金走私者", ["Andy Serkis"], "av2 bp1", "#7A5A3A"),
    ("collector", "收藏家", "The Collector", "坦利亚·提万", ["Benicio Del Toro"], "gotg1 iw", "#8A7A6A"),
    ("ebony", "乌木喉", "Ebony Maw", "灭霸的黑曜五将", ["Tom Vaughan-Lawlor"], "iw eg", "#6A6A8A"),
    ("ayesha", "阿伊莎", "Ayesha", "金色宗主的大祭司", ["Elizabeth Debicki"], "gotg2 gotg3", "#C9A040"),
    ("kraglin", "克拉格林", "Kraglin", "掠夺者", ["Sean Gunn"], "gotg1 gotg2 eg gotghs gotg3", "#5A6A8A"),
    ("cosmo", "宇宙狗", "Cosmo", "苏联太空犬", [], "gotghs gotg3", "#A08A6A"),
    ("yonrogg", "扬-罗格", "Yon-Rogg", "星际部队指挥官", ["Jude Law"], "cm", "#3A6A9A"),
    ("goose", "鹅猫", "Goose", "其实是弗莱肯", [], "cm marvels", "#C9873A"),
    ("darben", "达-本", "Dar-Benn", "克里人领袖", ["Zawe Ashton"], "marvels", "#6A3A6A"),
    ("mariarambeau", "惊奇队长", "Captain Marvel", "光照会 · 玛利亚·兰博", ["Lashana Lynch"], "cm ds2", "#C23C4A"),
    ("blackbolt", "黑蝠王", "Black Bolt", "光照会 · 异人族之王", ["Anson Mount"], "ds2", "#3A3A5A"),
    ("reed_k", "神奇先生", "Mister Fantastic", "光照会 · 卡拉辛斯基版", ["John Krasinski"], "ds2", "#3D79BF"),
    ("xialing", "夏玲", "Xialing", "尚气的妹妹", ["Meng'er Zhang"], "shang", "#8A3A4A"),
    ("katy", "凯蒂", "Katy", "尚气的好朋友", ["Awkwafina"], "shang", "#C08A6A"),
    ("kingo", "金格", "Kingo", "永恒族 · 宝莱坞明星", ["Kumail Nanjiani"], "eter", "#C9A04A"),
    ("thena", "希娜", "Thena", "永恒族 · 战神", ["Angelina Jolie"], "eter", "#B8BCC4"),
    ("ajak", "阿雅克", "Ajak", "永恒族首领", ["Salma Hayek"], "eter", "#C9A04A"),
    ("gilgamesh", "吉尔伽美什", "Gilgamesh", "永恒族 · 大力士", ["Ma Dong-seok"], "eter", "#8A6A4A"),
    ("harrow", "亚瑟·哈罗", "Arthur Harrow", "阿穆特的信徒", ["Ethan Hawke"], "mk", "#6A6A5A"),
    ("layla", "莱拉", "Scarlet Scarab", "绯红圣甲虫", ["May Calamawy"], "mk", "#B8423A"),
    ("watcher", "观察者", "The Watcher", "乌图", ["Jeffrey Wright"], "whatif", "#8A8AC0"),
    ("missminutes", "分钟小姐", "Miss Minutes", "时间变异管理局吉祥物", ["Tara Strong"], "loki", "#D9803A"),
    ("classicloki", "经典洛基", "Classic Loki", "洛基变体", ["Richard E. Grant"], "loki", "#3E8B57"),
    ("kidloki", "小洛基", "Kid Loki", "洛基变体", ["Jack Veal"], "loki", "#3E8B57"),
    ("alligatorloki", "鳄鱼洛基", "Alligator Loki", "洛基变体", [], "loki", "#4E8A3A"),
    ("ravonna", "雷沃娜", "Ravonna Renslayer", "时间变异管理局法官", ["Gugu Mbatha-Raw"], "loki", "#6A4A6A"),
    ("b15", "亨特 B-15", "Hunter B-15", "时间变异管理局猎手", ["Wunmi Mosaku"], "loki", "#6A5A4A"),
    ("ob", "欧比", "O.B.", "时间变异管理局技术员", ["Ke Huy Quan"], "loki", "#8A6A3A"),
    ("jackrussell", "杰克·罗素", "Jack Russell", "午夜狼人", ["Gael García Bernal"], "wbn", "#6A5A3A"),
    ("elsa", "艾尔莎", "Elsa Bloodstone", "怪物猎人", ["Laura Donnelly"], "wbn", "#8A2A2A"),
    ("manthing", "沼泽怪", "Man-Thing", "泰德", [], "wbn", "#4E6A3A"),
    ("titania", "泰坦尼亚", "Titania", "网红超能力者", ["Jameela Jamil"], "shehulk", "#C9A04A"),
    ("rio", "里奥", "Rio Vidal", "死神", ["Aubrey Plaza"], "agatha", "#3A6A4A"),
    ("teen", "少年比利", "Billy Maximoff", "维肯", ["Joe Locke"], "agatha", "#5A3A8A"),
    ("giah", "吉娅", "G'iah", "塔罗斯的女儿", ["Emilia Clarke"], "si", "#4E8A4E"),
    ("hood", "兜帽", "The Hood", "帕克·罗宾斯", ["Anthony Ramos"], "ironheart", "#5A3A3A"),
    ("punisher", "惩罚者", "The Punisher", "弗兰克·卡斯特", ["Jon Bernthal"], "ddba bnd", "#2E2E36"),
    ("bullseye", "靶眼", "Bullseye", "百发百中的杀手", ["Wilson Bethel"], "ddba", "#6A2A2A"),
    ("karen", "凯伦·佩奇", "Karen Page", "默多克的老搭档", ["Deborah Ann Woll"], "ddba", "#B8805A"),
    ("foggy", "福吉", "Foggy Nelson", "默多克的好兄弟", ["Elden Henson"], "ddba", "#8A7A5A"),
    ("torres", "华金·托雷斯", "Joaquin Torres", "新猎鹰", ["Danny Ramirez"], "faws cap4 doom", "#3C6EB5"),
    ("modok", "魔多客", "M.O.D.O.K.", "达伦·克罗斯", ["Corey Stoll"], "ant1 ant3", "#6A8A3A"),
    ("moleman", "鼹鼠人", "Mole Man", "地底之王", ["Paul Walter Hauser"], "ff", "#7A6A4A"),
    ("herbie", "赫比", "H.E.R.B.I.E.", "神奇四侠的机器人", [], "ff", "#9CA8BC"),
    ("scorpion", "蝎子", "Scorpion", "麦克·加尔根", ["Michael Mando"], "sh", "#4E8A4E"),
    ("lucky", "幸运披萨狗", "Lucky", "鹰眼收养的狗", [], "hawk", "#C9973A"),
    # 《死侍与金刚狼》的变体和老朋友
    ("ladypool", "女死侍", "Ladypool", "死侍变体", ["Blake Lively"], "dw", "#C2385A"),
    ("dogpool", "狗侍", "Dogpool", "死侍变体 · 小狗佩吉", [], "dw", "#C8586A"),
    ("kidpool", "小死侍", "Kidpool", "死侍变体", ["Inez Reynolds"], "dw", "#C23A3A"),
    ("cowboypool", "牛仔死侍", "Cowboy Deadpool", "死侍变体", ["Matthew McConaughey"], "dw", "#A06A3A"),
    ("nicepool", "好人死侍", "Nicepool", "死侍变体 · 头发很好", ["Ryan Reynolds"], "dw", "#C25A6A"),
    ("headpool", "头侍", "Headpool", "只剩一颗头的死侍", ["Nathan Fillion"], "dw", "#B8323C"),
    ("cavillrine", "卡维尔金刚狼", "Cavillrine", "金刚狼变体", ["Henry Cavill"], "dw", "#D1A72E"),
    ("johnny_e", "霹雳火", "Human Torch", "虚空里的 · 克里斯·埃文斯", ["Chris Evans"], "dw", "#D5632B"),
    ("paradox", "帕拉多克斯", "Mr. Paradox", "时间变异管理局", ["Matthew Macfadyen"], "dw", "#6A6A7A"),
    ("pyro", "火人", "Pyro", "约翰·阿勒代斯", ["Aaron Stanford"], "dw", "#D5632B"),
    ("sabretooth", "剑齿虎", "Sabretooth", "维克多·克里德", ["Tyler Mane"], "dw", "#8A6A3A"),
    ("juggernaut", "红坦克", "Juggernaut", "凯恩·马可", ["Aaron W. Reed"], "dw", "#8A3A2A"),
    ("alioth", "阿利奥斯", "Alioth", "吞噬一切的虚空巨兽", [], "loki dw", "#4A3A6A"),
    ("colossus", "钢力士", "Colossus", "彼得·拉斯普京", ["Stefan Kapicic"], "dw", "#8A9AAE"),
    ("negasonic", "弹头", "Negasonic Teenage Warhead", "艾莉", ["Brianna Hildebrand"], "dw", "#3A3A4A"),
    ("yukio", "由纪雄", "Yukio", "弹头的女友", ["Shioli Kutsuna"], "dw", "#C08AAA"),
    ("vanessa", "凡妮莎", "Vanessa", "死侍的前女友", ["Morena Baccarin"], "dw", "#A04A5A"),
    ("blindal", "盲眼阿尔", "Blind Al", "死侍的室友", ["Leslie Uggams"], "dw", "#8A7A9A"),
    ("dopinder", "多宾德", "Dopinder", "出租车司机", ["Karan Soni"], "dw", "#C9A04A"),
    ("peter_w", "彼得", "Peter", "死侍的好朋友", ["Rob Delaney"], "dw", "#8A8A7A"),
    # 《复联5》官宣的 X 战警
    ("beast", "野兽", "Beast", "汉克·麦考伊", ["Kelsey Grammer"], "marvels doom", "#3A5AA0"),
    ("cyclops", "镭射眼", "Cyclops", "斯科特·萨默斯", ["James Marsden"], "doom", "#3A4A8A"),
    ("nightcrawler", "夜行者", "Nightcrawler", "库尔特·瓦格纳", ["Alan Cumming"], "doom", "#3A3A8A"),
    ("mystique", "魔形女", "Mystique", "瑞雯·达克霍姆", ["Rebecca Romijn"], "doom", "#3A6AA0"),
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
    ("steppenwolf", "荒原狼", "Steppenwolf", "达克赛德的先锋", ["Ciarán Hinds"], "jl zsjl", "#6A6A7A"),
    ("darkseid", "达克赛德", "Darkseid", "天启星之主", ["Ray Porter"], "zsjl", "#4A4A5A"),
    ("doomsday", "毁灭日", "Doomsday", "氪星怪物", [], "bvs", "#5A4A3A"),
    ("manta", "黑蝠鲼", "Black Manta", "大卫·凯恩", ["Yahya Abdul-Mateen II"], "aqua1 aqua2", "#3A3A4A"),
    ("cheetah", "豹女", "Cheetah", "芭芭拉·米内尔瓦", ["Kristen Wiig"], "ww84", "#C9A04A"),
    ("trevor", "史蒂夫·特雷弗", "Steve Trevor", "神奇女侠的爱人", ["Chris Pine"], "ww1 ww84", "#3E6EB5"),
    ("ares", "阿瑞斯", "Ares", "战神", ["David Thewlis"], "ww1", "#6A3A3A"),
    ("kingshark", "鲨鱼王", "King Shark", "纳奈欧", ["Sylvester Stallone"], "tss", "#3E7A9A"),
    ("ratcatcher", "捕鼠者二代", "Ratcatcher 2", "克莱奥", ["Daniela Melchior"], "tss", "#6A5A4A"),
    ("hawkman", "鹰侠", "Hawkman", "卡特·霍尔", ["Aldis Hodge"], "ba", "#A06A3A"),
    ("fate", "命运博士", "Doctor Fate", "肯特·纳尔逊", ["Pierce Brosnan"], "ba", "#C9A040"),
    ("metamorpho", "变形人", "Metamorpho", "雷克斯·梅森", ["Anthony Carrigan"], "superman", "#8A6A4A"),
    ("lobo", "罗伯", "Lobo", "宇宙赏金猎人", ["Jason Momoa"], "supergirl", "#5A6A7A"),
    ("twoface", "双面人", "Two-Face", "哈维·登特", ["Aaron Eckhart"], "tdk", "#6A6A6A"),
    ("scarecrow", "稻草人", "Scarecrow", "乔纳森·克莱恩", ["Cillian Murphy"], "bb05 tdk tdkr", "#8A7A4A"),
    ("ras", "拉斯·艾尔·古尔", "Ra's al Ghul", "影武者联盟首领", ["Liam Neeson"], "bb05 tdkr", "#4A5A4A"),
    ("alfred_n", "阿尔弗雷德", "Alfred", "诺兰版 · 迈克尔·凯恩", ["Michael Caine"], "bb05 tdk tdkr", "#5A4A3A"),
    ("gordon_n", "戈登", "Jim Gordon", "诺兰版 · 加里·奥德曼", ["Gary Oldman"], "bb05 tdk tdkr", "#4A5A6A"),
    ("riddler", "谜语人", "The Riddler", "《新蝙蝠侠》· 保罗·达诺", ["Paul Dano"], "batman", "#3E8A4E"),
    ("sofia", "索菲亚·法尔科内", "Sofia Falcone", "法尔科内家族", ["Cristin Milioti"], "penguin", "#6A4A5A"),
    ("jonathan", "乔纳森·肯特", "Jonathan Kent", "超人的养父", ["Kevin Costner"], "mos bvs", "#8A6A3A"),
    ("martha", "玛莎·肯特", "Martha Kent", "超人的养母", ["Diane Lane"], "mos bvs jl zsjl", "#A07A5A"),
    ("jorel", "乔-艾尔", "Jor-El", "超人的生父", ["Russell Crowe"], "mos", "#3E6EB5"),
    ("faora", "法奥拉", "Faora", "佐德的副官", ["Antje Traue"], "mos", "#5A5A6A"),
    ("martian", "火星猎人", "Martian Manhunter", "琼恩·琼斯", ["Harry Lennix"], "zsjl", "#3E8A4E"),
    ("enchantress", "魔女", "Enchantress", "琼·穆恩", ["Cara Delevingne"], "ss1", "#4E8A4E"),
    ("croc", "杀手鳄", "Killer Croc", "韦伦·琼斯", ["Adewale Akinnuoye-Agbaje"], "ss1", "#4E6A3A"),
    ("boomerang", "回旋镖队长", "Captain Boomerang", "迪格·哈克尼斯", ["Jai Courtney"], "ss1 tss", "#3E6EB5"),
    ("diablo", "火魔", "El Diablo", "切托·迪亚兹", ["Jay Hernandez"], "ss1", "#C9603A"),
    ("katana", "武士刀", "Katana", "山代达津", ["Karen Fukuhara"], "ss1", "#6A3A4A"),
    ("flag_jr", "里克·弗拉格", "Rick Flag", "X 特遣队队长", ["Joel Kinnaman"], "ss1 tss", "#5E6B4A"),
    ("blackmask", "黑面具", "Black Mask", "罗曼·西恩尼斯", ["Ewan McGregor"], "bop", "#3A3A3A"),
    ("huntress", "女猎手", "Huntress", "海伦娜·贝蒂内利", ["Mary Elizabeth Winstead"], "bop", "#6A3A8A"),
    ("canary", "黑金丝雀", "Black Canary", "黛娜·兰斯", ["Jurnee Smollett"], "bop", "#3A3A4A"),
    ("montoya", "蕾妮·蒙托亚", "Renee Montoya", "哥谭警探", ["Rosie Perez"], "bop", "#6A5A4A"),
    ("orm", "海洋之王", "Ocean Master", "奥姆", ["Patrick Wilson"], "aqua1 aqua2", "#3E6E8A"),
    ("atlanna", "亚特兰娜", "Atlanna", "亚特兰蒂斯女王", ["Nicole Kidman"], "aqua1 aqua2", "#3E8A86"),
    ("vulko", "维科", "Vulko", "亚特兰蒂斯谋士", ["Willem Dafoe"], "aqua1 zsjl", "#5E7A6A"),
    ("sivana", "希瓦纳博士", "Dr. Sivana", "七宗罪的宿主", ["Mark Strong"], "shazam1", "#5A4A6A"),
    ("batman_k", "蝙蝠侠", "Batman", "《闪电侠》· 迈克尔·基顿", ["Michael Keaton"], "flash", "#2E3038"),
    ("supergirl_f", "超级少女", "Supergirl", "《闪电侠》· 萨莎·卡莱", ["Sasha Calle"], "flash", "#C23A48"),
    ("vigilante", "义警", "Vigilante", "阿德里安·蔡斯", ["Freddie Stroma"], "pm", "#3E5E8A"),
    ("harcourt", "哈考特", "Emilia Harcourt", "和平使者的队友", ["Jennifer Holland"], "tss pm", "#4A4A5A"),
    ("eagly", "伊格利", "Eagly", "和平使者的宠物鹰", [], "pm", "#8A6A3A"),
    ("bride", "新娘", "The Bride", "怪物特攻队", ["Indira Varma"], "cc", "#6A4A6A"),
    ("frankenstein", "埃里克·弗兰肯斯坦", "Eric Frankenstein", "怪物特攻队", ["David Harbour"], "cc", "#5A6A4A"),
    ("weasel", "鼬鼠", "Weasel", "怪物特攻队", [], "cc", "#8A7A5A"),
    ("gi", "机器人大兵", "G.I. Robot", "怪物特攻队", [], "cc", "#6A7A6A"),
    ("jimmy", "吉米·奥尔森", "Jimmy Olsen", "星球日报摄影师", ["Skyler Gisondo"], "superman", "#C9803A"),
    ("perry", "佩里·怀特", "Perry White", "星球日报主编", ["Wendell Pierce"], "superman", "#6A5A4A"),
    ("eve", "伊芙", "Eve Teschmacher", "莱克斯的女友", ["Sara Sampaio"], "superman", "#C08AAA"),
    ("ultraman", "极人", "Ultraman", "超人的克隆体", [], "superman", "#4A4A5A"),
    ("sinestro", "辛尼斯托", "Sinestro", "绿灯军团的叛徒", ["Ulrich Thomsen"], "lanterns", "#C9A040"),
    ("ruthye", "露蒂", "Ruthye", "超级少女的同伴", ["Eve Ridley"], "supergirl", "#8A6A4A"),
    ("krem", "克雷姆", "Krem", "黄山之主", ["Matthias Schoenaerts"], "supergirl", "#6A3A3A"),
    ("falcone", "卡迈恩·法尔科内", "Carmine Falcone", "哥谭黑帮老大", ["John Turturro"], "batman", "#4A4A4A"),
    ("alfred_p", "阿尔弗雷德", "Alfred", "《新蝙蝠侠》· 安迪·瑟金斯", ["Andy Serkis"], "batman", "#5A4A3A"),
    ("gordon_p", "戈登", "Jim Gordon", "《新蝙蝠侠》· 杰弗里·赖特", ["Jeffrey Wright"], "batman", "#4A5A6A"),
    ("lucius", "卢修斯·福克斯", "Lucius Fox", "韦恩企业的科技大师", ["Morgan Freeman"], "bb05 tdk tdkr", "#5A5A6A"),
    ("rachel", "瑞秋·道斯", "Rachel Dawes", "布鲁斯的青梅竹马", ["Katie Holmes", "Maggie Gyllenhaal"], "bb05 tdk", "#8A6A6A"),
    ("talia", "塔莉亚", "Talia al Ghul", "米兰达·泰特", ["Marion Cotillard"], "tdkr", "#6A4A4A"),
    ("blake", "约翰·布莱克", "John Blake", "年轻的警察", ["Joseph Gordon-Levitt"], "tdkr", "#3E5E8A"),
    ("victor", "维克多", "Victor Aguilar", "企鹅人的跟班", ["Rhenzy Feliz"], "penguin", "#6A5A3A"),
    ("murray", "默里·富兰克林", "Murray Franklin", "脱口秀主持人", ["Robert De Niro"], "joker", "#5A5A6A"),
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
    ("burke", "伯克", "Carter Burke", "公司代表", ["Paul Reiser"], "a2", "#6A6A5A"),
    ("weyland", "彼得·维兰德", "Peter Weyland", "维兰德公司创始人", ["Guy Pearce"], "prom cov", "#8A8A7A"),
    ("brett", "布雷特", "Brett", "诺斯特罗莫号维修工", ["Harry Dean Stanton"], "a1", "#6A6A4A"),
    ("dillon", "狄龙", "Dillon", "菲奥莉娜监狱的领袖", ["Charles S. Dutton"], "a3", "#5A4A3A"),
    ("clemens", "克莱门斯", "Clemens", "监狱医生", ["Charles Dance"], "a3", "#6A6A6A"),
    ("johner", "约纳", "Johner", "贝蒂号雇佣兵", ["Ron Perlman"], "a4", "#5A5A4A"),
    ("holloway", "霍洛威", "Charlie Holloway", "考古学家", ["Logan Marshall-Green"], "prom", "#6A7A8A"),
    ("tennessee", "田纳西", "Tennessee", "契约号驾驶员", ["Danny McBride"], "cov", "#8A6A4A"),
    ("kay", "凯", "Kay", "瑞恩的朋友", ["Isabela Merced"], "rom", "#8A6A7A"),
    ("tyler", "泰勒", "Tyler", "瑞恩的前男友", ["Archie Renaux"], "rom", "#5A6A7A"),
    ("hermit", "赫米特", "Hermit", "温蒂的哥哥", ["Alex Lawther"], "earth", "#6A7A6A"),
    ("kavalier", "卡瓦利尔", "Boy Kavalier", "神童公司老板", ["Samuel Blenkin"], "earth", "#C9A04A"),
    ("morrow", "莫罗", "Morrow", "维兰德-汤谷的半机械人", ["Babou Ceesay"], "earth", "#5A5A6A"),
    ("deacon", "执事", "The Deacon", "工程师体内诞生的生物", [], "prom", "#6A7A8A"),
    ("neomorph", "新形态", "Neomorph", "白色的异形", [], "cov", "#C4C8CE"),
    ("newborn", "新生儿", "The Newborn", "人类与异形的混血", [], "a4", "#A08A7A"),
    ("offspring", "后代", "The Offspring", "夺命舰上的混血怪物", [], "rom", "#8A7A6A"),
    ("ocellus", "眼球虫", "T. Ocellus", "能控制宿主的眼球生物", [], "earth", "#8A4A3A"),
]

# ---------------------------------------------------------------- 套牌：集齐一组角色解锁
MCU_DECKS = [
    ("avengers", "初代复仇者", "The Avengers", "ironman cap thor hulk widow hawkeye", "🛡"),
    ("guardians", "银河护卫队", "Guardians of the Galaxy", "starlord gamora rocket groot drax nebula mantis", "🌌"),
    ("wakanda", "瓦坎达万岁", "Wakanda Forever", "tchalla shuri okoye ramonda nakia mbaku killmonger", "🐾"),
    ("mystic", "至尊法师与魔法", "Masters of the Mystic Arts", "strange wong wanda agatha", "🔮"),
    ("asgard", "阿斯加德", "Asgard", "thor loki odin frigga heimdall sif jane valkyrie hela", "⚡"),
    ("spidey", "友好邻居", "Friendly Neighborhood", "spidey mj ironman", "🕸"),
    ("thunderbolts", "雷霆特工队*", "Thunderbolts*", "yelena bucky redguardian usagent ghost sentry", "⭐"),
    ("ff", "神奇四侠", "Fantastic Four", "reed sue johnny ben", "④"),
    ("street", "街头英雄", "Street Level", "daredevil kingpin echo kate", "🌃"),
    ("villains", "宿敌", "Big Bads", "thanos ultron hela killmonger kang", "💀"),
    ("spiders", "三代蜘蛛侠", "Spider-Men", "spidey spidey_t spidey_a", "🕷"),
    ("sinister", "反派五人组", "The Sinister Five", "goblin ock electro sandman lizard", "🦎"),
    ("void", "虚空抵抗军", "The Void Resistance", "deadpool wolverine x23 elektra blade gambit", "🌀"),
    ("gamma", "伽马家族", "Gamma Family", "hulk jen abomination ross leader", "☢"),
    ("dads", "星爵的两个爸爸", "Star-Lord's Dads", "ego yondu starlord", "👨"),
    ("quantum", "皮姆一家", "The Pyms & Langs", "antman wasp hank janet", "🐜"),
    ("corps", "死侍军团", "Deadpool Corps", "deadpool ladypool dogpool kidpool cowboypool nicepool headpool", "🦄"),
    ("dpfriends", "死侍的朋友们", "Deadpool's Crew", "colossus negasonic yukio vanessa blindal dopinder peter_w", "🍕"),
    ("voidbad", "虚空里的坏蛋", "Void Villains", "cassandra paradox pyro sabretooth juggernaut alioth", "🔥"),
    ("xmen", "X 战警", "X-Men", "xavier magneto beast cyclops nightcrawler mystique gambit wolverine", "✖"),
    ("lokis", "洛基变体", "Loki Variants", "loki sylvie classicloki kidloki alligatorloki", "🐊"),
    ("tva", "时间变异管理局", "TVA", "mobius b15 ob ravonna missminutes", "🕰"),
    ("illuminati", "光照会", "The Illuminati", "xavier mariarambeau blackbolt reed_k peggy mordo", "🔺"),
    ("ironfoes", "钢铁侠的对手", "Iron Man's Rogues", "obadiah whiplash hammer killian slattery", "🔩"),
    ("shield", "神盾局", "S.H.I.E.L.D.", "fury mariahill coulson sharon widow hawkeye", "🦅"),
    ("eternals", "永恒族", "The Eternals", "sersi ikaris kingo thena ajak gilgamesh", "✨"),
    ("midnight", "午夜怪物", "Midnight Monsters", "jackrussell elsa manthing", "🌕"),
    ("kitchen", "地狱厨房", "Hell's Kitchen", "daredevil karen foggy kingpin bullseye punisher", "😈"),
    ("pets", "超英的宠物", "Super Pets", "goose cosmo lucky dogpool", "🐾"),
]
DC_DECKS = [
    ("jl", "正义联盟", "Justice League", "superman_c batman_a ww aquaman flash cyborg", "⭐"),
    ("squad", "X 特遣队", "Task Force X", "harley deadshot waller bloodsport peacemaker", "🎯"),
    ("gang", "正义帮", "Justice Gang", "guy terrific hawkgirl", "💚"),
    ("lanterns", "绿灯军团", "Green Lantern Corps", "guy hal john", "🟢"),
    ("house_el", "超人一家", "House of El", "superman_d supergirl krypto lois", "🔰"),
    ("bats", "四代蝙蝠侠", "Four Batmen", "batman_k batman_b batman_a batman_p", "🦇"),
    ("jokers", "三代小丑", "Three Jokers", "joker_h joker_l joker_p", "🃏"),
    ("cats", "猫女", "Catwomen", "catwoman_h catwoman_k", "🐈‍⬛"),
    ("gotham", "哥谭罪恶录", "Rogues of Gotham", "joker_h twoface scarecrow ras bane riddler penguin", "🃏"),
    ("apokolips", "天启星入侵", "Apokolips", "steppenwolf darkseid", "🔥"),
    ("atlantis", "海王的世界", "Atlantis", "aquaman mera manta", "🔱"),
    ("themyscira", "天堂岛与人间", "Themyscira", "ww trevor ares cheetah", "🛡"),
    ("jsa", "黑亚当与正义协会", "Justice Society", "blackadam hawkman fate", "🪬"),
    ("squad16", "初代 X 特遣队", "Suicide Squad (2016)", "deadshot harley boomerang diablo katana croc enchantress flag_jr", "💀"),
    ("squad21", "全员集结", "The Suicide Squad", "bloodsport peacemaker kingshark ratcatcher harley boomerang flag_jr", "🦈"),
    ("birds", "猛禽小队", "Birds of Prey", "harley huntress canary montoya", "🐦"),
    ("kents", "肯特一家", "The Kents", "superman_c jonathan martha jorel", "🌾"),
    ("planet", "星球日报", "The Daily Planet", "lois jimmy perry", "📰"),
    ("commandos", "怪物特攻队", "Creature Commandos", "flag bride frankenstein weasel gi", "🧟"),
    ("allies", "哥谭的守护者", "Allies of Gotham", "alfred_n gordon_n lucius rachel blake", "🔦"),
    ("krypton", "氪星来客", "Kryptonians", "zod faora jorel supergirl", "💎"),
    ("eleven", "第 11 小队", "Team Peacemaker", "peacemaker vigilante harcourt eagly", "🦅"),
]
ALIEN_DECKS = [
    ("nostromo", "诺斯特罗莫号船员", "Crew of the Nostromo", "ripley dallas kane ash lambert parker jones", "🚀"),
    ("marines", "殖民海军陆战队", "Colonial Marines", "hicks hudson vasquez bishop newt", "🪖"),
    ("life", "异形生命周期", "Life Cycle", "facehugger chestburster xeno queen", "🥚"),
    ("synth", "合成人", "Synthetics", "ash bishop call david andy kirsh", "🤖"),
    ("makers", "造物者", "The Makers", "engineer david shaw vickers weyland", "🧬"),
    ("company", "维兰德-汤谷公司", "Weyland-Yutani", "weyland vickers burke ash bishop", "🏢"),
    ("variants", "异形变种", "Xeno Variants", "deacon neomorph newborn offspring ocellus queen", "🧪"),
    ("romulus", "夺命舰小队", "The Romulus Crew", "rain andy kay tyler", "🛰"),
    ("fury161", "菲奥莉娜监狱", "Fury 161", "ripley dillon clemens", "⛓"),
    ("earth", "《异形：地球》", "Alien: Earth", "wendy hermit kirsh kavalier morrow ocellus", "🏝"),
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


# ---------------------------------------------------------------- 角色介绍（电影版，尽量不剧透）
INTRO = {
    # 漫威
    "ironman": "天才、亿万富翁、花花公子、慈善家。在阿富汗被俘时造出第一套战甲，从军火商变成钢铁侠，也是复仇者联盟的核心。",
    "cap": "二战时瘦弱的布鲁克林青年，注射超级士兵血清后成为美国队长。冰封七十年后醒来，带着老派的正直守护新的时代。",
    "thor": "阿斯加德的王子、雷电之神。因为傲慢被奥丁放逐到地球，在一次次失去中学会担当。",
    "hulk": "物理学家布鲁斯·班纳在伽马射线事故后，一生气就会变成力大无穷的绿巨人。他一直在学着和体内的“另一个家伙”相处。",
    "widow": "红房子训练出的顶级特工，后来加入神盾局和复仇者联盟。没有超能力，靠格斗、枪械和情报在一群神和怪物之间站稳脚跟。",
    "hawkeye": "百发百中的神射手，神盾局特工、复仇者联盟初代成员。比起拯救世界，他更想回家陪老婆孩子过节。",
    "loki": "阿斯加德的诡计之神，索尔的养弟。野心、嫉妒和对认同的渴望，让他在反派与反英雄之间来回摇摆。",
    "fury": "神盾局局长，一手促成了“复仇者计划”。永远比别人多知道一点，也永远有所保留。",
    "pepper": "托尼的助理，后来的斯塔克工业 CEO 和恋人。冷静能干，是托尼身边最能稳住局面的人。",
    "peggy": "二战时的英国特工，史蒂夫的挚爱，战后参与创立神盾局。在男人主导的年代证明自己不需要谁的批准。",
    "jane": "天体物理学家，在新墨西哥的沙漠里“撞”到了被放逐的索尔，从此和九界扯上了关系。",
    "spidey": "皇后区的高中生彼得·帕克，被变种蜘蛛咬伤后获得超能力。被钢铁侠带进复仇者的世界，却始终是那个“友好邻居”。",
    "mj": "彼得的同学，冷淡、毒舌、观察力惊人，比谁都早看穿了彼得的秘密。",
    "strange": "傲慢的天才神经外科医生，车祸毁掉双手后远赴卡玛泰姬求医，最终成为守护地球的魔法师。",
    "wong": "卡玛泰姬的图书管理员，严肃又冷幽默，后来成为至尊法师，是斯特兰奇最可靠的同伴。",
    "tchalla": "瓦坎达国王，也是守护国家的黑豹。在传统与开放之间，他选择让瓦坎达走向世界。",
    "shuri": "特查拉的妹妹，瓦坎达科技的天才设计者，黑豹战衣和许多神奇装备都出自她手。",
    "okoye": "朵拉米拉吉女子卫队的将军，只忠于瓦坎达的王座，长矛之下几乎无人能敌。",
    "killmonger": "在美国长大的瓦坎达王族后裔，带着复仇和颠覆的目标归来，漫威最有说服力的反派之一。",
    "starlord": "八岁被外星海盗掳走的地球男孩，长大后自封“星爵”。随身带着妈妈留下的混音带，带着一群怪人成了银河护卫队。",
    "gamora": "灭霸的养女，被训练成宇宙最致命的刺客，背叛灭霸后加入了银河护卫队。",
    "rocket": "被基因改造的浣熊，机械天才，嘴毒心软。谁叫他浣熊他跟谁急。",
    "groot": "树人，只会说“我是格鲁特”，却能用这一句表达一切。火箭最好的朋友。",
    "drax": "一心为家人报仇的战士，完全听不懂比喻，说话直得吓人。",
    "nebula": "灭霸的另一个养女，被一点点改造成半机械体。和姐姐卡魔拉的关系是她最大的心结。",
    "mantis": "能通过触碰感知和影响别人情绪的共情者，天真又直白。",
    "antman": "有前科的电工兼神偷斯科特·朗，穿上皮姆博士的战衣，能缩小到蚂蚁大小，也能变成巨人。",
    "wasp": "皮姆博士的女儿霍普，接过母亲的黄蜂战衣，比斯科特更专业也更冷静。",
    "carol": "空军飞行员卡罗尔·丹弗斯，意外获得宇宙能量，成为漫威最强的英雄之一。",
    "wanda": "来自索科维亚的旺达，拥有操纵心灵和现实的力量。失去带来的痛苦，让她一步步走向“绯红女巫”。",
    "vision": "由奥创打造、贾维斯的意识和心灵宝石结合而诞生的人造人，一直在学习怎么做一个“人”。",
    "sam": "退伍军人“猎鹰”山姆·威尔逊，史蒂夫最信任的战友，后来接过了那面盾牌。",
    "bucky": "史蒂夫的儿时好友，被九头蛇洗脑成为杀手冬兵，之后一直在为过去赎罪。",
    "rhodey": "空军上校、托尼的好兄弟，穿上斯塔克打造的重装战甲成为战争机器。",
    "thanos": "来自泰坦星的疯狂泰坦，相信只有消灭一半生命才能拯救宇宙，为此收集六颗无限宝石。",
    "ultron": "托尼和班纳想造出守护地球的人工智能，结果诞生了想要毁灭人类的奥创。",
    "hela": "奥丁的长女、死亡女神，被封印数千年后归来，要夺回阿斯加德。",
    "valkyrie": "阿斯加德女武神战队最后的幸存者，流落萨卡星时嗜酒如命，后来成为新阿斯加德的国王。",
    "kang": "横跨无数时间线的征服者。在多元宇宙里，他的每一个变体都是巨大的威胁。",
    "shangchi": "十环帮首领文武之子，从小被训练成杀手，逃到旧金山当泊车员，最终要直面父亲。",
    "moonknight": "被埃及月神孔苏选为化身的前雇佣兵。礼品店员史蒂文和他共用一个身体。",
    "kamala": "新泽西的少女、惊奇队长的头号粉丝，一只手镯唤醒了她的能力，成为惊奇少女。",
    "monica": "卡罗尔老战友的女儿，从小就和她亲近。在旺达的结界里获得了感知和操纵能量的能力。",
    "jen": "布鲁斯的表妹、律师珍妮弗，意外沾到表哥的血变成女浩克。比起打架，她更关心律所和约会，还会打破第四面墙。",
    "agatha": "活了几百年的女巫，伪装成旺达的邻居。贪婪、狡猾又魅力十足。",
    "yelena": "和娜塔莎一起在红房子长大的“妹妹”，嘴毒、话多、身手一流。",
    "redguardian": "苏联版的“美国队长”，娜塔莎和叶莲娜的“爸爸”。爱吹牛，心里装着这个拼凑起来的家。",
    "usagent": "政府指定接替史蒂夫的“新美国队长”约翰·沃克，能力很强却总差了点什么，后来成了美国特工。",
    "ghost": "量子事故让艾娃的身体不停“相位穿透”，能穿墙也能隐身，一直在寻找治好自己的办法。",
    "sentry": "被实验改造的普通人鲍勃，拥有堪比神的力量，内心却藏着巨大的黑暗。",
    "kate": "从小崇拜鹰眼的富家女，自学射箭，阴差阳错和克林特过了一个不太平的圣诞节，成了新鹰眼。",
    "echo": "失聪的原住民战士玛雅，能完美模仿看到的任何动作，曾是金并的得力手下。",
    "daredevil": "白天是盲人律师马特·默多克，晚上是地狱厨房的守护者。失明让他的其他感官超乎常人。",
    "kingpin": "纽约地下世界之王威尔逊·菲斯克，体型巨大、心思缜密，是夜魔侠的宿敌。",
    "riri": "MIT 的天才少女莉莉，自己造出了战甲，被看作“下一个钢铁侠”。",
    "deadpool": "雇佣兵韦德·威尔逊，癌症实验让他拥有几乎不死的自愈能力。嘴炮第一，最爱打破第四面墙。",
    "wolverine": "拥有自愈能力和艾德曼合金爪的变种人罗根，脾气暴躁，是最出名的 X 战警。",
    "wonderman": "一心想当演员的西蒙·威廉姆斯，偏偏拥有超能力。",
    "reed": "神奇四侠的领袖、天才科学家，身体可以任意拉伸。",
    "sue": "里德的妻子，能隐身、制造力场，常被认为是四侠里最强的一位。",
    "johnny": "苏的弟弟，全身燃起火焰就能飞行，四侠里最爱出风头的那个。",
    "ben": "里德的好友，宇宙射线把他变成了一身岩石的大块头。外表吓人，心地最软。",
    "galactus": "以吞噬行星为生的宇宙级存在，他的到来意味着一个世界的终结。",
    "silversurfer": "行星吞噬者的先驱，乘着银色冲浪板为主人寻找下一颗星球。电影里由沙拉·芭尔担任这个身份。",
    "doctordoom": "拉特维尼亚的统治者，天才科学家兼魔法师，神奇四侠的宿敌，常被认为是漫威最强的反派。",
    # DC
    "superman_c": "来自氪星的卡尔-艾尔，在堪萨斯的农场长大。扎克·施奈德版的超人，更孤独，也更像一个神。",
    "batman_a": "打击犯罪二十年、伤痕累累的蝙蝠侠。愤怒和疲惫让他一度把超人视为威胁。",
    "ww": "天堂岛的亚马逊公主戴安娜，一战期间来到人类世界，从此守护着人类。",
    "aquaman": "灯塔看守人与亚特兰蒂斯女王的儿子亚瑟，一半人类一半亚特兰蒂斯人，七海之王。",
    "flash": "能以超光速奔跑的巴里·艾伦，话多又紧张，是正义联盟里的开心果。",
    "cyborg": "重伤后被父亲用母盒改造成半机械人的维克多，能接入世界上任何电子系统。",
    "mera": "泽贝尔王国的公主，能操控水，是海王的战友和爱人。",
    "zod": "氪星将军，为了复兴氪星不惜毁灭地球。",
    "lex_e": "天才而偏执的年轻富豪，坚信超人是人类的威胁。",
    "harley": "曾是阿卡姆疯人院的精神科医生，爱上小丑后成了哈莉·奎茵。疯狂、可爱又致命，后来学会了为自己而活。",
    "joker_l": "哥谭的犯罪王子，和哈莉·奎茵的关系疯狂又危险。",
    "deadshot": "百发百中的杀手，最大的软肋是他的女儿。",
    "waller": "冷酷的政府官员，用超级罪犯组成 X 特遣队，把他们当作随时可以丢弃的棋子。",
    "bloodsport": "曾经打伤超人的雇佣兵，被沃勒用女儿要挟加入 X 特遣队。",
    "peacemaker": "为了和平不惜一切代价的“英雄”，自大、幼稚又荒诞，他的剧集却出乎意料地动人。",
    "shazam": "寄养家庭的少年比利，喊出“沙赞”就能变成拥有神力的成年英雄，心里还是个孩子。",
    "blackadam": "五千年前坎达克的英雄，被封印后重新苏醒，用暴力的方式维护他心中的正义。",
    "bluebeetle": "刚毕业的墨西哥裔青年杰米，意外与外星圣甲虫共生，获得了强大的战甲。",
    "superman_d": "詹姆斯·古恩新宇宙里的超人，年轻、会犯错，却相信善良本身就是一种力量。",
    "lois": "星球日报的王牌记者，敏锐、强势，比任何人都先看清超人。",
    "lex_h": "新宇宙的莱克斯·卢瑟，科技巨头，对超人的嫉恨几乎成了执念。",
    "krypto": "超人的狗狗，有超能力，特别调皮，经常帮倒忙。",
    "supergirl": "超人的堂姐卡拉，亲历了氪星的毁灭，比堂弟更叛逆，也更沧桑。",
    "guy": "发型独特、脾气更独特的绿灯侠，正义帮成员。",
    "terrific": "世界第三聪明的人，靠科技和 T 型球战斗，正义帮里最靠谱的那位。",
    "hawkgirl": "长着翅膀、手持狼牙棒的鹰女，正义帮成员。",
    "hal": "试飞员哈尔·乔丹，被绿灯戒指选中的地球人，绿灯军团里最传奇的一位。",
    "john": "前海军陆战队员约翰·斯图尔特，新入职的绿灯侠，和哈尔搭档办案。",
    "flag": "美国陆军上校，怪物特攻队的指挥官。",
    "clayface": "被毁容的演员马特·黑根，变成能随意变形的泥人，向哥谭复仇。",
    "batman_b": "诺兰三部曲里的布鲁斯·韦恩，从目睹父母遇害的少年，成长为哥谭的黑暗骑士。",
    "joker_h": "混乱的化身，没有来历也没有动机，只想看世界燃烧。影史最经典的反派之一。",
    "bane": "戴着面罩的雇佣兵首领，力量和意志都足以折断蝙蝠侠。",
    "catwoman_h": "神出鬼没的猫女赛琳娜·凯尔，身手和立场都很灵活。",
    "batman_p": "第二年的蝙蝠侠，更像一个侦探，在复仇和希望之间寻找自己的意义。",
    "catwoman_k": "夜店服务生赛琳娜，在追查朋友失踪时和蝙蝠侠联手。",
    "penguin": "哥谭黑帮里不起眼的打手奥兹，在权力真空中一步步爬上顶端。",
    "joker_p": "失意的喜剧演员亚瑟·弗莱克，被社会一次次推开后，变成了小丑。",
    "lee": "在阿卡姆遇见亚瑟的李·奎泽尔，和他一起陷入了疯狂的二人世界。",
    # 异形
    "ripley": "诺斯特罗莫号的准尉艾伦·雷普利，冷静、坚韧，是影史最伟大的女性动作英雄之一。",
    "xeno": "完美的生物：酸性血液、第二副颚、黑色的生物机械外壳，H·R·吉格尔设计的噩梦。",
    "facehugger": "从异形卵里跳出的寄生体，扣住宿主的脸，把胚胎植入体内。",
    "chestburster": "在宿主体内长大后破胸而出的幼年异形，《异形》里的晚餐场景让无数观众难忘。",
    "queen": "巢穴之母，体型巨大，负责产卵，是整个异形族群的核心。",
    "jones": "诺斯特罗莫号上的橘猫，跟着雷普利一路活了下来。",
    "dallas": "诺斯特罗莫号的船长，冷静老练，亲自钻进通风管道追捕异形。",
    "kane": "诺斯特罗莫号的大副，在废弃飞船里第一个被抱脸虫扑上脸的人。",
    "ash": "诺斯特罗莫号的科学官，背后藏着公司的秘密命令。",
    "lambert": "诺斯特罗莫号的领航员，船员里最害怕的那一个。",
    "parker": "诺斯特罗莫号的总工程师，总在抱怨奖金不够。",
    "hicks": "冷静可靠的殖民海军陆战队下士，和雷普利并肩作战。",
    "hudson": "嘴上最狠、心里最慌的陆战队员，“游戏结束了，伙计！”",
    "vasquez": "陆战队里最硬的智能炮手，从不退缩。",
    "newt": "哈德利希望殖民地唯一的幸存者，雷普利拼了命也要救的小女孩。",
    "bishop": "公司派来的合成人，慢慢打破了雷普利对合成人的偏见。",
    "call": "混进贝蒂号的神秘女孩，秘密比她看上去多得多。",
    "shaw": "相信人类有造物主的考古学家，带着普罗米修斯号去寻找“工程师”。",
    "david": "维兰德打造的合成人，好奇、优雅又危险，对“创造”有着自己的野心。",
    "vickers": "维兰德公司派驻普罗米修斯号的主管，冷漠而强势。",
    "engineer": "高大苍白的远古种族，被认为是人类的创造者。",
    "daniels": "契约号的大副，在失去丈夫后扛起了整个殖民任务。",
    "rain": "杰克逊星的年轻矿工，一心想离开这颗永远见不到阳光的星球。",
    "andy": "瑞恩的合成人“弟弟”，程序设定要把瑞恩的利益放在第一位。",
    "wendy": "第一个被移植进合成躯体的孩子意识，“混合体”们的领头人。",
    "kirsh": "负责照看“混合体”的合成人科学家，立场暧昧。",
    "predator": "来自外星的猎人，以猎杀强大的猎物为荣，隐形、热成像和肩炮是它的标志。",
    # 新加的角色
    "namor": "海底王国塔洛肯的国王，长着脚踝上的小翅膀，为了保护子民不惜向地上世界开战。",
    "mysterio": "前斯塔克工业的员工，用无人机和全息投影制造“英雄”，是个顶级的骗术大师。",
    "vulture": "被斯塔克抢了生意的打捞商人，用外星科技做成飞行翼装，倒卖武器为生。",
    "redskull": "九头蛇首领，被超级士兵血清扭曲成红色骷髅脸，痴迷宇宙魔方的力量。",
    "ego": "以人形现身的“活体星球”，自称星爵的亲生父亲，魅力背后藏着可怕的计划。",
    "yondu": "蓝皮肤的掠夺者首领，用口哨控制飞箭。把星爵从地球掳走，也把他养大。",
    "ronan": "克里人里的极端分子，替灭霸寻找无限宝石，手持巨锤。",
    "zemo": "失去家人的索科维亚上校，用一个计划让复仇者从内部分裂。",
    "adam": "金色宗主们创造的“完美生命”，力量强大，心智却像个孩子。",
    "highevo": "执迷于创造完美世界的科学狂人，火箭痛苦的过去全拜他所赐。",
    "gorr": "失去女儿后对神明彻底绝望的男人，拿起弑神剑，誓要杀光所有神。",
    "talos": "斯克鲁人将军，能变成任何人的模样，和尼克·弗瑞有着几十年的交情。",
    "hank": "初代蚁人、皮姆粒子的发明者，脾气古怪，对自己的技术看得比命还重。",
    "janet": "初代黄蜂女，在量子领域困了三十年，那里的秘密只有她知道。",
    "happy": "托尼的保镖兼司机，后来成了彼得的“监护人”，嘴上嫌弃，心里最护短。",
    "ned": "彼得最好的兄弟，乐高迷、话痨，第一个知道彼得秘密的人。",
    "goblin": "另一个宇宙的诺曼·奥斯本，心里住着疯狂的绿魔，笑声能让人做噩梦。",
    "ock": "另一个宇宙的天才科学家，四条机械臂和他的身体融为了一体。",
    "electro": "另一个宇宙的电工马克斯，一次事故让他变成了能吸收和释放电能的电光人。",
    "sandman": "另一个宇宙的逃犯，身体可以化成沙子，心里只想回到女儿身边。",
    "lizard": "另一个宇宙的科学家，想用蜥蜴的再生能力治好自己的断臂，却变成了怪物。",
    "spidey_t": "另一个宇宙里的第一代蜘蛛侠，温和、真诚，经历过太多失去。",
    "spidey_a": "另一个宇宙的蜘蛛侠，嘴贫心善，一直没能放下对自己的责备。",
    "wenwu": "活了上千年的十环之主，尚气的父亲。失去爱人后，被执念一点点吞没。",
    "sylvie": "洛基的女性变体，从小在时间变异管理局的追捕中长大，比洛基更狠也更孤独。",
    "mobius": "时间变异管理局的探员，爱吃沙拉，喜欢摩托艇，是洛基难得的朋友。",
    "sersi": "永恒族成员，能改变物质的形态，在地球生活了七千年，深爱着人类。",
    "ikaris": "永恒族里最强的战士，能飞行、眼射光束，对使命的忠诚压过了一切。",
    "america": "能在多元宇宙之间开出星形传送门的少女，却控制不住自己的能力。",
    "taskmaster": "能完美模仿任何人战斗动作的神秘杀手，面具下的身份令人意外。",
    "val": "神秘的政府官员，四处招揽各路“特工”，没人知道她真正的打算。",
    "abomination": "为了打败绿巨人，主动注射血清变成怪物的军人。后来居然改邪归正，还去了格斗俱乐部。",
    "ross": "一辈子都在追捕绿巨人的将军，后来做了美国总统，自己也成了红浩克。",
    "leader": "研究绿巨人血液时意外变异的科学家，头脑大幅进化，成了“领袖”。",
    "x23": "金刚狼的克隆“女儿”劳拉，同样有自愈能力和爪子，沉默又凶猛。",
    "elektra": "身手绝顶的女刺客，被丢进了“虚空”，从没放弃战斗。",
    "blade": "半人半吸血鬼的吸血鬼猎人，在“虚空”里依然冷酷帅气。",
    "gambit": "卡津口音、能给扑克牌充能爆炸的变种人，终于在大银幕上出场了。",
    "cassandra": "X 教授的双胞胎妹妹，统治着“虚空”，拥有强大又扭曲的心灵能力。",
    "xavier": "X 战警的创始人，世界上最强的心灵感应者，梦想变种人和人类和平共处。",
    "magneto": "能操控一切金属的变种人，X 教授的老朋友，也是他最大的对手。",
    "steppenwolf": "达克赛德的先锋，为了收集母盒来到地球，想赎回自己犯下的错。",
    "darkseid": "天启星的暴君，追寻反生命方程式，宇宙中最可怕的存在之一。",
    "doomsday": "用氪星技术和佐德将军的尸体造出来的怪物，力量足以与超人同归于尽。",
    "manta": "海盗大卫·凯恩，认定海王害死了父亲，穿上亚特兰蒂斯战甲誓要复仇。",
    "cheetah": "原本自卑的宝石学家芭芭拉，许愿要成为戴安娜那样的人，一步步变成了豹女。",
    "trevor": "一战时坠落天堂岛的美国飞行员，把戴安娜带进了人类世界。",
    "ares": "希腊神话里的战神，相信人类天生就会自相残杀。",
    "kingshark": "能吃人的鲨鱼人，单纯又可爱，最想要的是交到朋友。",
    "ratcatcher": "能用父亲留下的装置指挥老鼠的女孩，X 特遣队里最温柔的一个。",
    "hawkman": "正义协会的领袖，戴着鹰形头盔、挥着钉锤，从天而降。",
    "fate": "能看到未来的命运博士，戴上纳布头盔就拥有强大的魔法。",
    "metamorpho": "能把身体变成任何化学元素的人，被莱克斯·卢瑟抓来当工具。",
    "lobo": "宇宙赏金猎人，粗暴、嗜酒、几乎杀不死，是超级少女的意外拍档。",
    "twoface": "哥谭的“光明骑士”检察官哈维·登特，悲剧之后用一枚硬币决定别人的生死。",
    "scarecrow": "用恐惧毒气控制人心的精神科医生，在诺兰三部曲里每部都有出场。",
    "ras": "影武者联盟的首领、布鲁斯的导师，想用极端的手段“净化”哥谭。",
    "alfred_n": "韦恩家的管家，看着布鲁斯长大，是蝙蝠侠背后最温暖的支撑。",
    "gordon_n": "哥谭警局里少有的好警察，和蝙蝠侠之间有着无需多言的信任。",
    "riddler": "在网上召集追随者的连环杀手，用一道道谜题揭开哥谭的腐败。",
    "sofia": "哥谭黑帮家族的女儿，从阿卡姆出来后，要夺回属于自己的一切。",
    "burke": "维兰德-汤谷公司的代表，表面热心，满脑子只有公司的利益。",
    "weyland": "维兰德公司的创始人，晚年痴迷于寻找延长生命的办法。",
    # 第三批
    "odin": "阿斯加德的众神之父，九界的统治者，索尔和洛基的父亲，智慧又深藏秘密。",
    "frigga": "阿斯加德王后，索尔和洛基的母亲，也是唯一真正懂洛基的人。",
    "heimdall": "能看见九界一切的彩虹桥守护者，金色的眼睛从不出错。",
    "sif": "阿斯加德最强的女战士之一，索尔从小一起长大的战友。",
    "korg": "萨卡星上的石头人角斗士，说话温吞，是索尔的新朋友。",
    "grandmaster": "统治垃圾星萨卡的“宗师”，热爱角斗比赛和派对，喜怒无常。",
    "malekith": "黑暗精灵之王，想用以太粒子让宇宙重回黑暗。",
    "mariahill": "神盾局副局长，冷静干练，尼克·弗瑞最可靠的左右手。",
    "coulson": "温和的神盾局特工，美国队长的头号粉丝，复仇者集结的关键人物。",
    "sharon": "佩吉·卡特的侄孙女，神盾局特工，曾经化名住在史蒂夫隔壁。",
    "pierce": "世界安全理事会的高官，表面是神盾局的靠山，背后另有身份。",
    "crossbones": "神盾局打击小队的队长，心狠手辣，后来成了交叉骨。",
    "howard": "托尼的父亲，天才发明家，参与了美国队长的诞生，也是神盾局的创始人之一。",
    "obadiah": "斯塔克工业的二把手，托尼父亲的老搭档，觊觎公司和战甲技术。",
    "whiplash": "带着家族恩怨的俄罗斯物理学家，用电鞭在赛车场上袭击托尼。",
    "hammer": "一心想取代斯塔克的军火商，技术不行，嘴上功夫一流。",
    "killian": "曾被托尼冷落的科学家，用“绝境病毒”造出了一支火焰军团。",
    "slattery": "被雇来扮演“满大人”的落魄演员，戏精本精，后来还去当了片场顾问。",
    "mordo": "斯特兰奇在卡玛泰姬的师兄，信念坚定到近乎偏执。",
    "ancientone": "活了几百年的至尊法师，斯特兰奇的老师，一直守护着地球。",
    "kaecilius": "背叛卡玛泰姬的法师，想把地球献给黑暗维度。",
    "clea": "来自黑暗维度的女术士，在片尾找上了斯特兰奇。",
    "mbaku": "加巴里部落的首领，嘴硬心软，关键时刻总会站出来保护瓦坎达。",
    "nakia": "瓦坎达的间谍，特查拉的爱人，想让瓦坎达帮助世界上更多的人。",
    "ramonda": "瓦坎达太后，特查拉和舒莉的母亲，威严又慈爱。",
    "klaw": "偷走振金的军火贩子，一只手装着声波炮。",
    "collector": "收集宇宙奇珍的收藏家，他的博物馆里什么都有。",
    "ebony": "灭霸麾下的黑曜五将之一，擅长念力，说话阴阳怪气。",
    "ayesha": "金色宗主的大祭司，傲慢、记仇，被银河护卫队偷了电池后穷追不舍。",
    "kraglin": "勇度手下的掠夺者，后来学会了用勇度的口哨箭。",
    "cosmo": "被送上太空的苏联狗狗，会心灵感应，是知无地的保安队长。",
    "yonrogg": "克里星际部队的指挥官，卡罗尔的“导师”。",
    "goose": "看起来是一只橘猫，其实是会吞东西的外星生物弗莱肯，尼克·弗瑞的心头好。",
    "darben": "克里人的领袖，想用量子手环拯救自己濒死的星球。",
    "mariarambeau": "另一个宇宙里成为惊奇队长的玛利亚·兰博，光照会成员。",
    "blackbolt": "异人族之王，开口说话就能摧毁一切，光照会成员。",
    "reed_k": "另一个宇宙的里德·理查兹，光照会里最聪明的人。",
    "xialing": "尚气的妹妹，从小被父亲冷落，自己闯出了一片天地。",
    "katy": "尚气在旧金山的泊车员搭档，嘴碎、讲义气，莫名其妙卷进了十环大战。",
    "kingo": "永恒族成员，混成了宝莱坞的大明星，能射出能量弹。",
    "thena": "永恒族的战神，能凭空造出各种武器，却被记忆错乱困扰。",
    "ajak": "永恒族的首领，能治愈伤痛，最早开始怀疑他们的使命。",
    "gilgamesh": "永恒族的大力士，一拳能打飞怪物，也会给大家做饭。",
    "harrow": "阿穆特女神的信徒，想在罪恶发生之前就审判所有人。",
    "layla": "马克的妻子，考古学家，后来成了埃及的超级英雄绯红圣甲虫。",
    "watcher": "注视着整个多元宇宙的观察者，发誓永不干预，却忍不住插了手。",
    "missminutes": "时间变异管理局的卡通时钟吉祥物，笑眯眯的，知道的比谁都多。",
    "classicloki": "穿着漫画经典戏服的老年洛基变体，留在了最后的一个自己的结局里。",
    "kidloki": "小孩模样的洛基变体，在虚空里当着“国王”。",
    "alligatorloki": "一只鳄鱼洛基。没错，就是一只鳄鱼。",
    "ravonna": "时间变异管理局的法官，对“神圣时间线”深信不疑。",
    "b15": "时间变异管理局的猎手，被希尔薇“唤醒”后开始怀疑一切。",
    "ob": "时间变异管理局的技术员，大家都叫他欧比，啥都能修。",
    "jackrussell": "其实是狼人的怪物猎人，在一场葬礼上卷入了猎杀比赛。",
    "elsa": "布拉德斯通家族的女儿，不想继承家业，却继承了血石。",
    "manthing": "沼泽里的怪物泰德，碰到恐惧的人就会把他烧掉。是杰克的好朋友。",
    "titania": "拿超能力当网红生意做的泰坦尼亚，最爱跟女浩克抢风头。",
    "rio": "绿色女巫里奥，也是死神本身，和阿加莎之间有说不清的过去。",
    "teen": "想走女巫之路的神秘少年，身份比他自己以为的更特别。",
    "giah": "塔罗斯的女儿，在斯克鲁人的激进派里当卧底。",
    "hood": "披着魔法斗篷的街头罪犯头目，用魔法和科技与钢铁之心对抗。",
    "punisher": "失去家人后以暴制暴的弗兰克·卡斯特，冷酷无情，却有自己的底线。",
    "bullseye": "几乎什么东西都能扔成致命武器的杀手，夜魔侠的死敌。",
    "karen": "默多克的老同事和老朋友，记者出身，一直在追真相。",
    "foggy": "马特的大学同学和合伙人，最乐观也最仗义的律师。",
    "torres": "山姆的战友、空军中尉，接过了新的猎鹰之名。",
    "modok": "被量子领域改造成一颗巨大脑袋的达伦·克罗斯，曾经的黄蜂侠。",
    "moleman": "地底世界之王，和神奇四侠的关系亦敌亦友。",
    "herbie": "神奇四侠家里的小机器人，会照顾孩子，也会做家务。",
    "scorpion": "道上混的麦克·加尔根，在《英雄归来》里第一次露面。",
    "lucky": "鹰眼和凯特收养的金毛，爱吃披萨，独眼也很勇敢。",
    "ladypool": "女版死侍，身手了得，在虚空里帮了大忙。",
    "dogpool": "戴着死侍头套的小狗佩吉，丑萌丑萌的，是死侍的灵魂伴侣。",
    "kidpool": "小孩模样的死侍变体，奶声奶气地说着脏话。",
    "cowboypool": "穿牛仔装的死侍变体，带着一口南方口音。",
    "nicepool": "头发很好、性格很好的死侍变体，好到让人起鸡皮疙瘩。",
    "headpool": "只剩一颗头还在说话的死侍变体。",
    "cavillrine": "长得特别帅的金刚狼变体，出场只有几秒，却让所有人尖叫。",
    "johnny_e": "流落虚空的霹雳火约翰尼·斯托姆，嘴比火还旺。",
    "paradox": "时间变异管理局的官员，想用一台机器提前抹掉整个宇宙。",
    "pyro": "能操控火焰的变种人，流落虚空后投靠了卡珊德拉。",
    "sabretooth": "野兽一样凶猛的变种人，金刚狼的老冤家。",
    "juggernaut": "一旦冲起来就停不下的红坦克，力气大得惊人。",
    "alioth": "吞噬一切时间与空间的虚空巨兽，连洛基们都怕它。",
    "colossus": "全身能变成钢铁的俄国变种人，正经得让死侍头疼。",
    "negasonic": "一身爆炸能力的少女变种人，话少，嫌死侍烦。",
    "yukio": "弹头的女友，总是热情地跟死侍打招呼：“嗨，韦德！”",
    "vanessa": "死侍一生的挚爱，也是最懂他的人。",
    "blindal": "和死侍合租的盲眼老太太，嘴比死侍还毒。",
    "dopinder": "开出租车的多宾德，一心想像死侍一样当个狠角色。",
    "peter_w": "一个普通到不能再普通的中年人，却是死侍最好的朋友。",
    "beast": "浑身蓝毛的天才科学家，X 战警的智囊。",
    "cyclops": "眼睛能射出镭射光的 X 战警队长，必须一直戴着护目镜。",
    "nightcrawler": "能瞬间移动的蓝色变种人，外表吓人，信仰虔诚。",
    "mystique": "能变成任何人的蓝皮肤变种人，立场一直在变。",
    "jonathan": "在堪萨斯收养了小克拉克的农夫，教他如何隐藏，也教他如何做人。",
    "martha": "克拉克的养母，无论他是谁，都是她的儿子。",
    "jorel": "氪星科学家，在星球毁灭前把唯一的儿子送往地球。",
    "faora": "佐德的副官，速度和战斗力都极强。",
    "martian": "伪装成人类潜伏多年的火星人，能变形，也是心灵感应者。",
    "enchantress": "被远古女巫附身的考古学家琼·穆恩，X 特遣队的失控王牌。",
    "croc": "生活在下水道里的鳄鱼人，话不多。",
    "boomerang": "爱喝啤酒、爱回旋镖的澳洲大盗，最不靠谱的队员。",
    "diablo": "能召唤火焰的帮派分子，背负着过去的悲剧，不愿再用能力。",
    "katana": "手持能吸收灵魂的武士刀，沉默的日本剑客。",
    "flag_jr": "X 特遣队的现场指挥官，正直的军人，夹在沃勒和罪犯之间。",
    "blackmask": "哥谭的黑帮老板，自恋又残忍，想得到一颗价值连城的钻石。",
    "huntress": "为家人复仇的十字弩刺客，还在练习怎么帅气地报出自己的代号。",
    "canary": "夜店歌手，一嗓子能把人震飞的“黑金丝雀”。",
    "montoya": "被同事看不起的哥谭警探，一直在追查黑面具。",
    "orm": "亚瑟同母异父的弟弟，亚特兰蒂斯国王，想向陆地开战。",
    "atlanna": "亚特兰蒂斯女王，亚瑟的母亲，为了爱逃离过海底王国。",
    "vulko": "亚特兰蒂斯的谋士，从小秘密训练亚瑟。",
    "sivana": "从小被魔法师拒之门外的希瓦纳，长大后和七宗罪结下契约。",
    "batman_k": "另一个宇宙里早已退隐的蝙蝠侠，一出场就让人想起 1989 年。",
    "supergirl_f": "另一个时间线里被关在俄罗斯的超级少女卡拉。",
    "vigilante": "和平使者的头号粉丝，开心地杀人，开心地交朋友。",
    "harcourt": "沃勒手下的特工，嘴硬、能打，是和平使者最靠谱的队友。",
    "eagly": "和平使者的宠物白头海雕，比主人还受欢迎。",
    "bride": "为弗兰肯斯坦怪物创造的“新娘”，怪物特攻队的实际领袖。",
    "frankenstein": "执着地追着新娘不放的弗兰肯斯坦怪物。",
    "weasel": "长得像鼬鼠的怪物，可爱又吓人。",
    "gi": "二战时造出来的士兵机器人，只想消灭纳粹。",
    "jimmy": "星球日报的年轻摄影师，人缘好得出奇。",
    "perry": "星球日报的主编，一切以新闻为先。",
    "eve": "莱克斯的女友，看起来不太聪明，关键时刻却很有用。",
    "ultraman": "莱克斯用超人的基因造出的克隆体，没有自己的意志。",
    "sinestro": "曾经最强的绿灯侠之一，后来走上了另一条路。",
    "ruthye": "向超级少女求助的外星女孩，一心要为父亲报仇。",
    "krem": "黄山之主克雷姆，超级少女这次的对手。",
    "falcone": "哥谭黑帮老大，表面风度翩翩，背后掌握着整座城市的秘密。",
    "alfred_p": "《新蝙蝠侠》里的阿尔弗雷德，和年轻的布鲁斯关系有些疏远。",
    "gordon_p": "《新蝙蝠侠》里的戈登，和蝙蝠侠一起追查谜语人。",
    "lucius": "韦恩企业应用科学部的负责人，蝙蝠侠大部分装备都出自他手。",
    "rachel": "布鲁斯的青梅竹马，坚持正义的检察官。",
    "talia": "以米兰达·泰特的身份接近布鲁斯，真实身份在最后才揭晓。",
    "blake": "看穿了布鲁斯身份的年轻警察，诺兰三部曲留下的伏笔。",
    "victor": "被企鹅人收作司机的哥谭少年，跟着他越陷越深。",
    "murray": "亚瑟最崇拜的脱口秀主持人，却把亚瑟当成笑话。",
    "brett": "诺斯特罗莫号的维修工，在找一只猫的时候……",
    "dillon": "菲奥莉娜监狱里囚犯们的精神领袖，信仰坚定。",
    "clemens": "菲奥莉娜监狱的医生，对雷普利格外关照。",
    "johner": "贝蒂号上粗鲁的雇佣兵，最爱嘲笑别人。",
    "holloway": "肖的男友，同样坚信人类有造物主的考古学家。",
    "tennessee": "契约号的驾驶员，戴着牛仔帽，靠得住。",
    "kay": "瑞恩的朋友，怀着身孕登上了夺命舰。",
    "tyler": "瑞恩的前男友，带大家去夺命舰找冷冻舱。",
    "hermit": "温蒂的亲哥哥，在神童公司里做医护兵。",
    "kavalier": "神童公司年轻的老板，天才而傲慢，把“混合体”当作自己的玩具。",
    "morrow": "维兰德-汤谷公司的半机械人，一心要把异形样本带回公司。",
    "deacon": "《普罗米修斯》结尾从工程师体内破出的生物，异形的雏形。",
    "neomorph": "由黑色孢子感染宿主后长出的白色异形，比经典异形更原始也更狂暴。",
    "newborn": "异形女王生下的人类混血，把雷普利当作母亲。",
    "offspring": "夺命舰上诞生的人类与异形混血怪物，看起来格外诡异。",
    "ocellus": "《异形：地球》里的眼球生物，能钻进眼眶控制宿主。",
}

# ---------------------------------------------------------------- 漫画原型（SuperHero API 的编号）
COMIC_ID = {
    "mcu": {"ironman": 346, "cap": 149, "thor": 659, "hulk": 332, "widow": 107, "hawkeye": 313, "loki": 414, "fury": 489,
            "spidey": 620, "spidey_t": 620, "spidey_a": 620, "strange": 226, "tchalla": 106, "starlord": 630, "gamora": 275,
            "rocket": 566, "groot": 303, "drax": 234, "nebula": 487, "mantis": 431, "antman": 31, "carol": 157, "wanda": 579,
            "vision": 697, "sam": 251, "bucky": 714, "rhodey": 703, "thanos": 655, "ultron": 680, "hela": 321, "kang": 379,
            "shangchi": 587, "moonknight": 470, "jen": 589, "sentry": 583, "kate": 314, "daredevil": 201, "kingpin": 391,
            "deadpool": 213, "wolverine": 717, "wonderman": 719, "reed": 456, "sue": 344, "johnny": 333, "ben": 658,
            "galactus": 273, "silversurfer": 598, "doctordoom": 222, "namor": 481, "mysterio": 479, "vulture": 701,
            "redskull": 550, "ego": 235, "hank": 30, "janet": 708, "goblin": 299, "ock": 225, "electro": 237, "sandman": 572,
            "lizard": 412, "taskmaster": 653, "abomination": 4, "ross": 547, "leader": 401, "x23": 723, "elektra": 238,
            "blade": 112, "gambit": 274, "xavier": 527, "magneto": 423, "odin": 498, "sif": 594, "klaw": 392, "blackbolt": 96,
            "modok": 463, "obadiah": 347, "watcher": 709, "manthing": 428, "colossus": 185, "negasonic": 488, "pyro": 532,
            "sabretooth": 570, "juggernaut": 374, "punisher": 530, "bullseye": 141, "beast": 75, "cyclops": 196,
            "nightcrawler": 490, "mystique": 480, "scorpion": 581, "reed_k": 456, "mariarambeau": 157, "johnny_e": 333,
            "cavillrine": 717, "nicepool": 213, "kidpool": 213, "cowboypool": 213, "headpool": 213},
    "dc": {"superman_c": 644, "superman_d": 644, "batman_a": 70, "batman_b": 70, "batman_p": 70, "ww": 720, "aquaman": 38,
           "flash": 265, "cyborg": 194, "mera": 444, "zod": 278, "lex_e": 405, "lex_h": 405, "harley": 309, "lee": 309,
           "joker_l": 370, "joker_h": 370, "joker_p": 370, "deadshot": 214, "shazam": 156, "blackadam": 95, "bluebeetle": 126,
           "krypto": 396, "supergirl": 643, "guy": 305, "hawkgirl": 315, "hal": 306, "flag": 557, "bane": 60,
           "catwoman_h": 165, "catwoman_k": 165, "penguin": 514, "steppenwolf": 637, "darkseid": 204, "doomsday": 230,
           "manta": 105, "cheetah": 174, "kingshark": 390, "fate": 224, "lobo": 413, "twoface": 678, "scarecrow": 576,
           "ras": 538, "alfred_n": 17, "alfred_p": 17, "riddler": 558, "martian": 432, "enchantress": 242, "croc": 386,
           "flag_jr": 557, "huntress": 334, "canary": 98, "sinestro": 601, "faora": 253, "batman_k": 70, "supergirl_f": 643},
    "alien": {"xeno": 18, "predator": 526},
}


def extract_comics(all_json):
    """从 SuperHero API 的 all.json 抽出用得到的：图、六维数值、真名、首次登场、身高体重……"""
    d = {h["id"]: h for h in json.loads(Path(all_json).read_text(encoding="utf-8"))}
    clean = lambda x: "" if (not x or x in ("-", "null", "No alter egos found.", "0 cm", "0 kg")) else x
    out = {}
    for u, m in COMIC_ID.items():
        for k, i in m.items():
            h = d[i]
            b, a, ps = h["biography"], h["appearance"], h["powerstats"]
            out[f"{u}:{k}"] = {"s": h["slug"], "n": h["name"],
                               "ps": [ps[x] for x in ("intelligence", "strength", "speed", "durability", "power", "combat")],
                               "fn": clean(b.get("fullName")), "fa": clean(b.get("firstAppearance")), "al": clean(b.get("alignment")),
                               "race": clean(a.get("race")), "h": clean((a.get("height") or ["", ""])[1]),
                               "wt": clean((a.get("weight") or ["", ""])[1])}
    Path(__file__).with_name("universes_comics.json").write_text(json.dumps(out, ensure_ascii=False, indent=0), encoding="utf-8")
    print(f"漫画原型 {len(out)} 位")


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
    # 漫画原型：图和设定数值来自 SuperHero API（akabab/superhero-api），用 --comics all.json 重新抽取
    cpath = Path(__file__).with_name("universes_comics.json")
    comics = json.loads(cpath.read_text(encoding="utf-8")) if cpath.exists() else {}
    # SuperHero API 里没有的（小辣椒、舒莉、露易丝……）：Marvel / DC 维基（fandom）的漫画图，只有图没有数值
    fpath = Path(__file__).with_name("universes_fandom.json")
    for k, v in (json.loads(fpath.read_text(encoding="utf-8")) if fpath.exists() else {}).items():
        if k not in comics:
            comics[k] = {"img": v["img"], "pg": v.get("pg", "")}
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
            ch = {"k": ck, "cn": cn, "en": en, "sub": sub, "a": ids, "w": wl, "c": color}
            if INTRO.get(ck):
                ch["i"] = INTRO[ck]
            else:
                print(f"  提示：{ck} 没有角色介绍", file=sys.stderr)
            if comics.get(f"{u['id']}:{ck}"):
                ch["cm"] = comics[f"{u['id']}:{ck}"]
            chars.append(ch)
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
    ap.add_argument("--comics", help="SuperHero API 的 all.json，给了就重新抽取漫画原型")
    a = ap.parse_args()
    if a.comics:
        extract_comics(a.comics)
    build(Path(a.idx), a.out)
