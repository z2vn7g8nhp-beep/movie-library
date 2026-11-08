U = dict(id="monsters", n="环球怪物", en="Universal Monsters", short="MONSTERS",
         tag="德古拉、科学怪人、木乃伊、狼人和隐形人——近一百年的银幕怪物，和猎杀它们的人。",
         theme=["#5A6A5A", "#C8C0A8", "#0A0C0A"], wd=["Q96409720"])
ORDER = 31

WORKS = """
## classic | 经典怪物 | The Classics
dracula31 | Dracula | 1931 | 德古拉
frank31 | Frankenstein | 1931 | 科学怪人
mummy32 | The Mummy | 1932 | 木乃伊
invisible33 | The Invisible Man | 1933 | 隐形人
bride35 | Bride of Frankenstein | 1935 | 科学怪人的新娘
wolfman41 | The Wolf Man | 1941 | 狼人
creature54 | Creature from the Black Lagoon | 1954 | 黑湖妖谭
## mummy | 木乃伊三部曲 | The Mummy Trilogy
mummy99 | The Mummy | 1999 | 木乃伊
mummy01 | The Mummy Returns | 2001 | 木乃伊归来
mummy08 | The Mummy: Tomb of the Dragon Emperor | 2008 | 木乃伊3：龙帝之墓
## modern | 新世纪 | The Modern Era
vh | Van Helsing | 2004 | 范海辛
wolfman10 | The Wolfman | 2010 | 狼人
mummy17 | The Mummy | 2017 | 新木乃伊
invisible20 | The Invisible Man | 2020 | 隐形人
wolfman25 | Wolf Man | 2025 | 狼人
"""

CHARS = """
# —— 经典
dracula_l | 德古拉伯爵 | Count Dracula | 卢戈西版 | Bela Lugosi | dracula31 | #3A2A3A | 吸血鬼 | 名台词:我从不喝……酒;造型:大斗篷、匈牙利口音 | dracula_v:后来的德古拉
> 银幕上最经典的吸血鬼，贝拉·卢戈西的斗篷和口音，定义了“德古拉”在之后一百年里的样子。
monster_k | 科学怪人 | Frankenstein's Monster | 卡洛夫版 | Boris Karloff | frank31 bride35 | #5A7A5A | 人造生命 | 造型:平头、脖子上的螺栓、笨重的靴子;造物主:弗兰肯斯坦博士 | henry:造出他的人;bride:为他造的新娘;monster_v:后来的科学怪人
> 用尸体拼起来、被闪电唤醒的“怪物”。他不会说话，只想被接纳，却一次次被人类追打。
henry | 亨利·弗兰肯斯坦 | Henry Frankenstein | 科学家 | Colin Clive | frank31 bride35 | #6A6A5A | 科学家 | 名台词:它活了！它活了！ | monster_k:造出的生命
> 在闪电交加的夜里大喊“它活了！”的科学家。
bride | 新娘 | The Bride | 怪物的新娘 | Elsa Lanchester | bride35 | #E0E0E0 | 人造生命 | 造型:高耸的黑发、两道白色闪电纹 | monster_k:为她而生的“丈夫”
> 只出场几分钟，却凭一头带闪电纹的高耸黑发成为影史经典。她看了“丈夫”一眼，尖叫起来。
imhotep_k | 伊莫顿 | Imhotep | 卡洛夫版木乃伊 | Boris Karloff | mummy32 | #8A7A5A | 木乃伊 | 化名:阿达斯·贝 | imhotep_v:后来的伊莫顿
> 1932 年的木乃伊，复活后化名阿达斯·贝，寻找转世的恋人。
invisible_r | 隐形人 | The Invisible Man | 杰克·格里芬 | Claude Rains | invisible33 | #C8C8C8 | 科学家 | 造型:全身绷带、墨镜;副作用:药物让他发疯 | adrian:后来的隐形人
> 喝下隐形药水的科学家，裹着绷带、戴着墨镜，越来越疯。
wolfman_c | 狼人 | The Wolf Man | 拉里·塔尔博特 | Lon Chaney Jr. | wolfman41 | #6A5A3A | 狼人 | 诅咒:被狼人咬伤，满月时变身 | lawrence:后来的塔尔博特
> 被狼人咬伤后每逢满月就会变身的拉里·塔尔博特，悲伤又可怜的经典怪物。
gillman | 半鱼人 | The Gill-man | 黑湖的生物 | - | creature54 | #3A6A4A | 水陆两栖生物 | 住处:亚马逊的黑湖
> 亚马逊黑湖里的两栖怪物，《水形物语》的灵感来源之一。
# —— 木乃伊三部曲
rick | 里克·奥康纳 | Rick O'Connell | 冒险家 | Brendan Fraser | mummy99 mummy01 mummy08 | #8A6A3A | 冒险家;前法国外籍军团 | 武器:双枪、各种刀;性格:嘴贫、大胆、永远在逃命 | evelyn:一生挚爱;jonathan:大舅子;alex:儿子;ardeth:盟友;imhotep_v:宿敌
> 法国外籍军团出身的冒险家，痞帅、嘴贫、运气爆棚。布兰登·弗雷泽这一版的里克，是很多人童年的冒险偶像。
evelyn | 伊芙琳·卡纳汉 | Evelyn Carnahan | 古埃及学者 | Rachel Weisz; Maria Bello | mummy99 mummy01 mummy08 | #A07A5A | 图书馆员;古埃及学者 | 名台词:我是一个图书馆员！;秘密:她是埃及公主纳芙蒂丽的转世 | rick:一生挚爱;jonathan:哥哥;alex:儿子
> 在开罗图书馆把书架推倒成一排的笨拙学者，读出了不该读的咒语。她骄傲地说：“我是一个图书馆员！”
jonathan | 乔纳森 | Jonathan Carnahan | 伊芙琳的哥哥 | John Hannah | mummy99 mummy01 mummy08 | #6A6A5A | 冒险家（自称） | 最爱:金子、酒 | evelyn:妹妹;rick:妹夫
> 伊芙琳不靠谱的哥哥，见到金子就挪不动脚，关键时刻却总能帮上忙。
alex | 亚历克斯 | Alex O'Connell | 奥康纳家的儿子 | Freddie Boath; Luke Ford | mummy01 mummy08 | #6A8AA0 | 奥康纳家 | 戴过:阿努比斯手镯 | rick:父亲;evelyn:母亲
> 里克和伊芙琳的儿子，八岁时戴上了阿努比斯手镯，长大后去了中国考古。
ardeth | 阿德斯·贝 | Ardeth Bay | 守护者首领 | Oded Fehr | mummy99 mummy01 | #3A3A4A | 守护者部落 | 使命:世代守护，不让伊莫顿复活 | rick:盟友
> 世代守护哈姆纳塔、阻止伊莫顿复活的部落首领，冷峻又帅气。
imhotep_v | 伊莫顿 | Imhotep | 沃斯洛版 · 大祭司 | Arnold Vosloo | mummy99 mummy01 | #8A7A5A | 木乃伊;法老的大祭司 | 诅咒:活着被做成木乃伊;能力:操控沙暴、召唤圣甲虫 | anck:三千年的爱人;rick:宿敌;imhotep_k:1932 年的伊莫顿
> 为了爱人被活生生做成木乃伊的大祭司，三千年后醒来，带着沙暴和圣甲虫找回他的爱人。
anck | 安苏娜 | Anck-su-namun | 法老的情妇 | Patricia Velásquez | mummy99 mummy01 | #C8A040 | 古埃及 | imhotep_v:三千年的爱人
> 伊莫顿的爱人，法老的情妇。为了她，伊莫顿受了三千年的诅咒。
beni | 贝尼 | Beni | 墙头草 | Kevin J. O'Connor | mummy99 | #6A5A4A | 投机者 | 特长:会用很多种语言祈祷 | rick:旧战友
> 里克的老战友，见风使舵，最后投靠了伊莫顿。
scorpionking | 蝎子王 | The Scorpion King | 远古战士 | Dwayne Johnson | mummy01 | #8A6A3A | 远古战士 | 契约:把灵魂卖给阿努比斯
> 五千年前把灵魂献给阿努比斯换取军队的战士——巨石强森的第一个电影角色。
dragonemp | 龙帝 | The Dragon Emperor | 秦始皇 | Jet Li | mummy08 | #6A5A3A | 皇帝;兵马俑 | 诅咒:和他的兵马俑大军一起被封印 | ziyuan:诅咒他的女巫
> 被女巫诅咒、和兵马俑大军一起封印的暴君皇帝。李连杰饰演。
ziyuan | 紫元 | Zi Yuan | 女巫 | Michelle Yeoh | mummy08 | #6A3A6A | 女巫 | lin:女儿;dragonemp:诅咒的皇帝
> 诅咒了皇帝的女巫，活了两千年守护着秘密。杨紫琼饰演。
lin | 林 | Lin | 紫元的女儿 | Isabella Leong | mummy08 | #8A5A6A | 守护者 | alex:恋人;ziyuan:母亲
> 紫元的女儿，守护者的后人，和亚历克斯相恋。
# —— 新世纪
vanhelsing | 范海辛 | Van Helsing | 怪物猎人 | Hugh Jackman | vh | #4A3A2A | 圣职骑士团 | 武器:旋转刀刃、连发十字弩;秘密:他失去了过去的记忆 | anna:并肩作战;carl:搭档;dracula_v:宿敌
> 为梵蒂冈秘密骑士团猎杀怪物的猎人，金刚狼演员的另一个经典角色。
anna | 安娜·瓦勒里斯 | Anna Valerious | 吉普赛公主 | Kate Beckinsale | vh | #6A3A4A | 瓦勒里斯家族 | 家族诅咒:不消灭德古拉，祖先就不能进天堂 | vanhelsing:并肩作战;velkan:哥哥
> 世代与德古拉作战的瓦勒里斯家族最后的后人。
carl | 卡尔 | Carl | 修士发明家 | David Wenham | vh | #8A7A5A | 圣职骑士团 | 特长:发明武器 | vanhelsing:搭档
> 跟着范海辛的修士，负责发明各种猎魔武器。
dracula_v | 德古拉伯爵 | Count Dracula | 范海辛版 | Richard Roxburgh | vh | #3A2A3A | 吸血鬼 | 计划:用科学怪人的力量让吸血鬼后代复活 | vanhelsing:宿敌;dracula_l:经典的德古拉
> 《范海辛》里的德古拉，想利用科学怪人唤醒自己成千上万的后代。
monster_v | 科学怪人 | Frankenstein's Monster | 范海辛版 | Shuler Hensley | vh | #5A7A5A | 人造生命 | 特点:温和、会说话、想活下去 | monster_k:经典的科学怪人
> 《范海辛》里的科学怪人，这一次他会说话，只想好好活下去。
velkan | 维尔肯 | Velkan Valerious | 安娜的哥哥 | Will Kemp | vh | #6A5A4A | 狼人 | anna:妹妹
> 安娜的哥哥，被狼人咬伤后成了德古拉的傀儡。
hyde | 海德先生 | Mr. Hyde | 巴黎圣母院的怪物 | Robbie Coltrane | vh | #6A5A5A | 怪物
> 开场在巴黎圣母院被范海辛追杀的海德先生，演员是海格。
lawrence | 劳伦斯·塔尔博特 | Lawrence Talbot | 2010 版狼人 | Benicio Del Toro | wolfman10 | #5A4A3A | 狼人 | john_t:父亲;gwen:心上人
> 回到英国老家调查哥哥之死的演员，被狼人咬伤后继承了诅咒。
john_t | 约翰·塔尔博特爵士 | Sir John Talbot | 劳伦斯的父亲 | Anthony Hopkins | wolfman10 | #6A6A5A | 塔尔博特家族 | 秘密:他也是狼人 | lawrence:儿子
> 劳伦斯的父亲，阴沉古怪，藏着一个可怕的家族秘密。
gwen | 格温 | Gwen Conliffe | 劳伦斯哥哥的未婚妻 | Emily Blunt | wolfman10 | #8A7A7A | 平民 | lawrence:心上人
> 劳伦斯哥哥的未婚妻，后来和劳伦斯相爱。
ahmanet | 阿玛奈特 | Ahmanet | 2017 版女木乃伊 | Sofia Boutella | mummy17 | #C8A040 | 木乃伊;古埃及公主 | 特点:双瞳、全身符文 | nick:选中的容器
> 被抹去历史的古埃及公主，双瞳、满身符文，醒来后要找一个“容器”。
nick | 尼克·莫顿 | Nick Morton | 盗墓的军人 | Tom Cruise | mummy17 | #6A6A4A | 美军;盗墓者 | ahmanet:选中他的人;jekyll:神秘组织的首领
> 一不小心唤醒了女木乃伊的军人兼盗墓贼。
jekyll | 杰基尔博士 | Dr. Henry Jekyll | 普罗迪组织的首领 | Russell Crowe | mummy17 | #4A4A5A | 普罗迪组织 | 另一面:海德先生
> 专门研究和消灭怪物的神秘组织首领，自己身体里也住着一个怪物。
adrian | 阿德里安·格里芬 | Adrian Griffin | 2020 版隐形人 | Oliver Jackson-Cohen | invisible20 | #C8C8C8 | 科技天才 | 手段:光学隐身衣 | cecilia:控制欲极强的前男友;invisible_r:经典的隐形人
> 控制欲极强的光学科技天才，“死后”变成了一个看不见的跟踪者。
cecilia | 西西莉亚 | Cecilia Kass | 逃离控制的女人 | Elisabeth Moss | invisible20 | #6A6A8A | 平民 | adrian:她逃离的前男友
> 深夜逃离控制狂男友的女人。没人相信她说的“看不见的人”，她只能自己面对。
blake | 布莱克 | Blake Lovell | 2025 版狼人 | Christopher Abbott | wolfman25 | #5A4A3A | 狼人 | charlotte:妻子
> 回到俄勒冈老家的父亲，在一个夜晚被不知名的东西抓伤，开始一点点变成另一种东西。
charlotte | 夏洛特 | Charlotte Lovell | 布莱克的妻子 | Julia Garner | wolfman25 | #8A7A8A | 平民 | blake:丈夫
> 眼看着丈夫慢慢变成野兽的妻子。
"""

DECKS = """
classic | 经典怪物 | The Classic Monsters | 🦇 | dracula_l monster_k bride imhotep_k invisible_r wolfman_c gillman
oconnell | 奥康纳一家 | The O'Connells | 🏺 | rick evelyn alex jonathan
medjai | 哈姆纳塔 | Hamunaptra | 🐞 | rick evelyn jonathan ardeth imhotep_v anck beni
mummies | 历代木乃伊 | The Mummies | ⚱ | imhotep_k imhotep_v ahmanet dragonemp
wolves | 历代狼人 | The Wolf Men | 🐺 | wolfman_c velkan lawrence blake
draculas | 两代德古拉 | Two Draculas | 🧛 | dracula_l dracula_v
monsters | 两代科学怪人 | Two Monsters | ⚡ | monster_k monster_v
invisibles | 两代隐形人 | Two Invisible Men | 👤 | invisible_r adrian
hunters | 范海辛小队 | Van Helsing's Crew | ✝ | vanhelsing anna carl
dark | 东方的诅咒 | Tomb of the Dragon Emperor | 🐉 | dragonemp ziyuan lin alex
"""

RARE = {"UR": "rick evelyn dracula_l monster_k"}
