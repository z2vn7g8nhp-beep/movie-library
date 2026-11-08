U = dict(id="fast", n="速度与激情", en="The Fast Saga", short="FAMILY",
         tag="从洛杉矶的街头赛车，到东京、里约、伦敦和太空。不管去哪儿，都是为了家人。",
         theme=["#C8502E", "#E8C27A", "#140E0C"], timeline=True, wd=["Q1576873"])
ORDER = 14

WORKS = """
## main | 正传 | The Fast Saga
ff1 | The Fast and the Furious | 2001 | 速度与激情 | tl=2001
ff2 | 2 Fast 2 Furious | 2003 | 速度与激情2 | tl=2003
ff3 | The Fast and the Furious: Tokyo Drift | 2006 | 速度与激情3：东京漂移 | tl=2013.5
ff4 | Fast & Furious | 2009 | 速度与激情4 | tl=2009
ff5 | Fast Five | 2011 | 速度与激情5 | tl=2011
ff6 | Fast & Furious 6 | 2013 | 速度与激情6 | tl=2013
ff7 | Furious 7 | 2015 | 速度与激情7 | tl=2015
ff8 | The Fate of the Furious | 2017 | 速度与激情8 | tl=2017
ff9 | F9: The Fast Saga | 2021 | 速度与激情9 | tl=2021
ff10 | Fast X | 2023 | 速度与激情10 | tl=2023
ff11 | Fast Forever | 2028 | 速度与激情11 | tl=2028
## spin | 外传 | Spin-off
hs | Fast & Furious Presents: Hobbs & Shaw | 2019 | 速度与激情：特别行动 | x tl=2019
"""

CHARS = """
# —— 家人
dom | 多米尼克·托雷托 | Dominic Toretto | 家人至上 | Vin Diesel | ff1 ff3 ff4 ff5 ff6 ff7 ff8 ff9 ff10 ff11 | #5A4A3A | 托雷托家族;街头赛车之王 | 座驾:1970 道奇 Charger R/T;最爱:科罗娜啤酒、周日家庭烧烤;座右铭:一次只活四分之一英里;信条:我没有朋友，我只有家人 | letty:一生挚爱;brian:兄弟;mia:妹妹;jakob:弟弟;littleb:儿子;han:兄弟;hobbs:从对手到战友;charger:老伙计
> 洛杉矶街头赛车的王者，肌肉、背心、十字架项链。他的规矩只有一条：家人。为了家人，他能开车冲出飞机、冲下大楼、冲进潜艇。
brian | 布莱恩·奥康纳 | Brian O'Conner | 卧底警察 · 兄弟 | Paul Walker | ff1 ff2 ff4 ff5 ff6 ff7 | #4A7AA0 | 托雷托家族;前 FBI 卧底 | 座驾:丰田 Supra、日产 GT-R;出身:洛杉矶警局卧底;最爱:改装日系跑车 | dom:兄弟;mia:妻子;roman:发小;supra:座驾
> 本来是潜进车队的卧底警察，却真心爱上了这个家。和多米尼克从对手变成兄弟，最后一程，两辆车在岔路口各自开向远方。
letty | 莱蒂·奥尔蒂斯 | Letty Ortiz | 最飒的车手 | Michelle Rodriguez | ff1 ff4 ff6 ff7 ff8 ff9 ff10 ff11 | #8A3A3A | 托雷托家族 | 擅长:赛车、格斗;往事:一度失去记忆 | dom:一生挚爱;mia:好姐妹;gisele:并肩作战
> 一个能和任何男人飙车、打架的女人。她曾经“死”过，失去记忆后又回到多米尼克身边。
mia | 米娅·托雷托 | Mia Toretto | 多米尼克的妹妹 | Jordana Brewster | ff1 ff4 ff5 ff6 ff7 ff9 ff10 ff11 | #A06A5A | 托雷托家族 | 身份:多米尼克的妹妹、布莱恩的妻子 | dom:哥哥;brian:丈夫;jakob:哥哥;letty:好姐妹
> 多米尼克的妹妹，看起来最温柔，开起车来一点不输哥哥。
roman | 罗曼·皮尔斯 | Roman Pearce | 话最多的那个 | Tyrese Gibson | ff2 ff5 ff6 ff7 ff8 ff9 ff10 ff11 | #6A5A8A | 托雷托家族 | 特长:嘴贫、自以为是队长;趣事:坚信自己刀枪不入 | brian:发小;tej:斗嘴搭档;ramsey:追了好多部的人
> 布莱恩的发小，话痨、爱吹牛、永远在抢镜。他坚信自己是天选之人，因为每次都没死。
tej | 特吉·帕克 | Tej Parker | 技术担当 | Ludacris | ff2 ff5 ff6 ff7 ff8 ff9 ff10 ff11 | #3A6A8A | 托雷托家族 | 特长:机械、黑客、改装;出身:迈阿密改装车行老板 | roman:斗嘴搭档;ramsey:心动的人
> 迈阿密的改装车行老板，团队里的技术大脑，被罗曼吐槽了十几年。
han | 韩 | Han Lue | 永远在吃零食 | Sung Kang | ff3 ff4 ff5 ff6 ff9 ff10 ff11 | #6A8A3A | 托雷托家族;东京漂移 | 习惯:手里永远拿着零食;座驾:马自达 RX-7 VeilSide;粉丝口号:Justice for Han | gisele:恋人;dom:兄弟;sean:东京的徒弟;deckard:因他而起的恩怨;rx7:座驾
> 酷到不需要说话的韩，手里永远拿着零食。粉丝为他喊了好多年“Justice for Han”，然后他回来了。
gisele | 吉赛尔 | Gisele Yashar | 前摩萨德特工 | Gal Gadot | ff4 ff5 ff6 ff7 ff10 ff11 | #5A6A5A | 托雷托家族 | 出身:以色列前情报人员;擅长:摩托车、枪械 | han:恋人;letty:并肩作战
> 原本是毒枭身边的联络人，后来加入了家人。她和韩之间，是整个系列最让人心疼的一段。
ramsey | 拉姆齐 | Ramsey | 天才黑客 | Nathalie Emmanuel | ff7 ff8 ff9 ff10 ff11 | #6A5AA0 | 托雷托家族 | 发明:天眼程序;趣事:不会开车（一开始） | tej:心动的人;roman:追她的人
> 开发出“天眼”的英国黑客，一加入就被罗曼和特吉争着献殷勤。
# —— 霍布斯与肖
hobbs | 卢克·霍布斯 | Luke Hobbs | 外交安全局特工 | Dwayne Johnson | ff5 ff6 ff7 ff8 hs ff10 | #3A5A3A | 外交安全局;萨摩亚 | 特长:肌肉、一拳打爆、用手臂改变导弹方向;女儿:萨曼莎 | dom:从对手到战友;deckard:死对头兼搭档;elena:搭档
> 一身肌肉、汗流浃背的联邦特工，追捕多米尼克的时候是最强对手，并肩作战的时候是最强外援。
deckard | 德卡德·肖 | Deckard Shaw | 前英国特种兵 | Jason Statham | ff6 ff7 ff8 hs ff9 ff10 | #5A5A5A | 肖家;前 SAS | 特长:近身格斗、开车也很快;母亲:梅格达琳·肖 | owen:弟弟;hattie:妹妹;queenie:母亲;hobbs:死对头兼搭档;han:因他而起的恩怨
> 前英国特种兵，为了弟弟找上家人复仇，后来却成了最不可能的盟友。最爱嘲讽霍布斯，也最爱自己妈妈。
owen | 欧文·肖 | Owen Shaw | 雇佣兵首领 | Luke Evans | ff6 ff7 | #4A4A5A | 肖家 | 装备:翻转车;信条:精确与纪律 | deckard:哥哥;queenie:母亲
> 德卡德的弟弟，冷静精确的雇佣兵首领，开着一辆能把车掀飞的翻转车。
hattie | 哈蒂·肖 | Hattie Shaw | 军情六处特工 | Vanessa Kirby | hs | #6A6A7A | 肖家;军情六处 | 擅长:格斗、伪装 | deckard:哥哥;hobbs:搭档;brixton:对手
> 德卡德的妹妹，军情六处的王牌特工，和霍布斯打着打着就有了火花。
queenie | 梅格达琳·肖 | Magdalene Shaw | 肖家的母亲 | Helen Mirren | ff8 ff9 ff10 | #8A6A8A | 肖家 | 爱好:开车（很猛）;气质:女王 | deckard:儿子;owen:儿子;hattie:女儿;dom:欣赏的年轻人
> 肖家三兄妹的母亲，优雅得像女王，开起车来一点不含糊。
brixton | 布里克斯顿 | Brixton Lore | 黑人超级战士 | Idris Elba | hs | #3A3A4A | 艾提昂;改造人 | 自称:黑色超人 | hattie:对手;deckard:昔日战友
> 被科技改造的超级战士，自称“黑色超人”。
# —— 政府的人
mrnobody | 无名氏先生 | Mr. Nobody | 神秘特工头子 | Kurt Russell | ff7 ff8 ff9 | #5A5A4A | 秘密机构 | 最爱:比利时啤酒 | littlenobody:徒弟
> 神秘机构的头子，总在关键时刻出现，给家人派一个不可能完成的任务。
littlenobody | 小无名氏 | Little Nobody | 无名氏的跟班 | Scott Eastwood | ff8 ff9 ff10 | #6A7A8A | 秘密机构 | mrnobody:师父
> 无名氏先生的手下，一本正经，常被罗曼和特吉耍。
elena | 埃琳娜 | Elena Neves | 里约警察 | Elsa Pataky | ff5 ff6 ff7 ff8 | #8A6A5A | 里约警察;外交安全局 | dom:相恋过的人;hobbs:搭档;littleb:儿子
> 里约的女警，在莱蒂“离开”的日子里陪在多米尼克身边。
jah | 贾 | Jah | 欧文·肖的手下 | Joe Taslim | ff6 | #4A4A4A | 肖的团队 | 擅长:跑酷、近身格斗 | owen:老板;han:在伦敦地铁里交手的对手
> 欧文·肖团队里身手最快的打手，和韩、罗曼在伦敦地铁站里打了一场。
riley | 莱莉 | Riley Hicks | 霍布斯的搭档 | Gina Carano | ff6 | #5A5A6A | 外交安全局 | 擅长:格斗 | hobbs:搭档;letty:打了两场的对手
> 霍布斯新招的搭档，和莱蒂在地铁里打了一场。
# —— 第一部 · 洛杉矶
vince | 文斯 | Vince | 多米尼克的发小 | Matt Schulze | ff1 ff5 | #6A5A4A | 托雷托车队 | mia:暗恋的人;dom:发小
> 多米尼克的发小，一直暗恋米娅，看布莱恩不顺眼。
jesse | 杰西 | Jesse | 车队的技术宅 | Chad Lindberg | ff1 | #8A8A6A | 托雷托车队 | 特长:电脑、调车
> 车队里最年轻的技术宅，冲动起来什么都敢赌。
leon | 莱昂 | Leon | 车队成员 | Johnny Strong | ff1 | #5A6A5A | 托雷托车队
> 多米尼克车队里话不多的一员。
tran | 约翰尼·陈 | Johnny Tran | 地下赛车对手 | Rick Yune | ff1 | #3A3A3A | 洛杉矶 | 座驾:本田 S2000
> 骑着摩托、开着 S2000 的地下车队老大，和多米尼克是死对头。
tanner | 坦纳警长 | Sgt. Tanner | 布莱恩的上司 | Ted Levine | ff1 | #5A5A5A | 洛杉矶警局 | brian:手下
> 布莱恩在洛杉矶警局的上司。
# —— 第二部 · 迈阿密
suki | 苏琪 | Suki | 粉色跑车女车手 | Devon Aoki | ff2 | #E08AB0 | 迈阿密 | 座驾:粉色本田 S2000
> 开着粉色 S2000 的迈阿密女车手，飞车越过大桥那场最惊险。
monica | 莫妮卡 | Monica Fuentes | 海关卧底 | Eva Mendes | ff2 ff5 | #8A5A6A | 美国海关 | brian:暧昧的搭档
> 潜伏在毒枭身边的海关探员，和布莱恩之间有点火花。
verone | 卡特·维罗内 | Carter Verone | 迈阿密毒枭 | Cole Hauser | ff2 | #4A4A3A | 毒枭 | 刑具:老鼠和铁桶
> 迈阿密的毒枭，用老鼠审讯人的狠角色。
# —— 第三部 · 东京
sean | 肖恩·博斯韦尔 | Sean Boswell | 东京漂移的主角 | Lucas Black | ff3 ff7 ff8 | #4A6A9A | 东京漂移 | 特长:漂移;来历:被送去东京的美国高中生 | han:师父;neela:女朋友;takashi:漂移之王的对手
> 屡次闯祸被送到东京的美国高中生，在韩的车库里学会了漂移。
twinkie | 特温基 | Twinkie | 东京的倒爷 | Bow Wow | ff3 | #6AA03A | 东京漂移 | 座驾:绿巨人涂装的面包车
> 在东京高中里什么都能弄到的美国小子，开着一辆绿巨人涂装的面包车。
neela | 妮拉 | Neela | 东京女车手 | Nathalie Kelley | ff3 | #8A6A7A | 东京漂移 | sean:男朋友;takashi:前男友
> 漂移之王的女朋友，后来坐上了肖恩的副驾。
takashi | 漂移之王 | D.K. | 高桥 | Brian Tee | ff3 | #3A3A5A | 东京漂移;山口组 | 本名:高桥;座驾:日产 350Z
> 东京的“漂移之王”，叔叔是黑帮大佬，山路漂移无人能敌。
# —— 第四、五部
braga | 布拉加 | Arturo Braga | 毒枭 | John Ortiz | ff4 ff6 | #4A3A3A | 毒枭
> 藏在暗处的墨西哥毒枭，害死了家人里的重要一员。
fenix | 菲尼克斯 | Fenix | 布拉加的打手 | Laz Alonso | ff4 | #3A3A3A | 毒枭集团
> 布拉加手下最狠的车手兼打手。
santos | 桑托斯 | Santos | 波多黎各搭档 | Tego Calderón | ff4 ff5 | #8A6A3A | 托雷托家族 | leo:搭档
> 和里奥形影不离的波多黎各人，抢完钱就去赌场。
leo | 里奥 | Leo | 波多黎各搭档 | Don Omar | ff4 ff5 | #6A5A3A | 托雷托家族 | santos:搭档
> 桑托斯的搭档，两人一唱一和。
reyes | 埃尔南·雷耶斯 | Hernan Reyes | 里约黑帮老大 | Joaquim de Almeida | ff5 | #4A4A4A | 里约黑帮 | 金库:藏在警察局里
> 掌控里约的黑帮老大，把一亿美元藏在警察局的保险柜里——然后家人拖着保险柜满城跑。
# —— 第七部之后
jakande | 莫斯·贾坎德 | Mose Jakande | 雇佣兵首领 | Djimon Hounsou | ff7 | #3A3A3A | 雇佣兵 | 目标:天眼
> 想抢天眼的雇佣兵首领，开着武装直升机满城追杀。
kiet | 基特 | Kiet | 贾坎德的打手 | Tony Jaa | ff7 | #5A4A3A | 雇佣兵 | 擅长:泰拳、跑酷
> 托尼·贾饰演的打手，身手快得像风。
kara | 卡拉 | Kara | 贾坎德的保镖 | Ronda Rousey | ff7 | #6A6A6A | 雇佣兵 | 擅长:格斗
> 迪拜派对上和莱蒂大打出手的保镖。
cipher | 赛弗 | Cipher | 网络恐怖分子 | Charlize Theron | ff8 ff9 ff10 | #8A9AAA | 黑客 | 特长:黑掉全世界的车;发型:脏辫 | dom:利用过的人;littleb:用来要挟的孩子
> 世界上最危险的黑客，能把全城的汽车变成“僵尸车”。她是唯一让多米尼克背叛家人的人。
jakob | 雅各布·托雷托 | Jakob Toretto | 多米尼克的弟弟 | John Cena | ff9 ff10 | #5A6A7A | 托雷托家族 | 擅长:特工技能、开车 | dom:哥哥;mia:哥哥;littleb:保护的侄子
> 被家里遗忘多年的托雷托家老三，带着一身特工本事回来了。
dante | 但丁·雷耶斯 | Dante Reyes | 复仇的疯子 | Jason Momoa | ff10 ff11 | #8A3A6A | 雷耶斯家族 | 动机:为父报仇;风格:疯癫、花哨、指甲油 | reyes:父亲;dom:复仇对象
> 里约黑帮老大的儿子，花枝招展、疯得彻底。他花了十二年计划复仇。
tess | 泰丝 | Tess | 无名氏的女儿 | Brie Larson | ff10 | #4A5A8A | 秘密机构 | mrnobody:父亲
> 无名氏先生的女儿，接替父亲站在了家人这边。
isabel | 伊莎贝尔 | Isabel | 埃琳娜的妹妹 | Daniela Melchior | ff10 | #A05A5A | 里约 | elena:姐姐
> 埃琳娜的妹妹，里约的地下赛车手，也是小布莱恩的小姨。
littleb | 小布莱恩 | Little B | 多米尼克的儿子 | Leo Abelo Perry | ff10 | #6A8AA0 | 托雷托家族 | 名字由来:以布莱恩命名 | dom:爸爸;elena:妈妈;letty:后来的妈妈
> 多米尼克的儿子，名字取自布莱恩。他最喜欢的事，是和爸爸一起开车。
abuelita | 外婆 | Abuelita | 托雷托家的老奶奶 | Rita Moreno | ff10 | #A08A7A | 托雷托家族 | dom:外孙
> 多米尼克的外婆，在家庭烧烤上给大家讲道理。
# —— 座驾
charger | 道奇 Charger | Dodge Charger | 多米尼克的老伙计 | - | ff1 ff4 ff5 ff6 ff7 ff8 ff9 ff10 | #2A2A2A | 座驾 | 型号:1970 道奇 Charger R/T;马力:约 900 匹（多米尼克这么说）;来历:多米尼克和父亲一起造的 | dom:主人
> 多米尼克和父亲一起造的黑色肌肉车，几乎每部都在，翘头、冲刺、飞跃，它是这个家的老成员。
supra | 丰田 Supra | Toyota Supra | 布莱恩的跑车 | - | ff1 ff7 | #E07A2E | 座驾 | 型号:丰田 Supra MK4;名场面:第一部的橙色 Supra、第七部结尾的白色 Supra | brian:主人
> 布莱恩的橙色 Supra，后来那辆白色的，陪他开完了最后一程。
rx7 | 马自达 RX-7 | Mazda RX-7 | 韩的座驾 | - | ff3 | #E07A2E | 座驾 | 型号:马自达 RX-7 VeilSide Fortune;涂装:橙黑相间 | han:主人
> 东京街头最好看的车，橙黑相间的宽体 RX-7，属于韩。
"""

DECKS = """
family | 家人 | The Family | 🍺 | dom brian letty mia roman tej han gisele ramsey
og | 初代车队 | The Original Crew | 🏁 | dom brian letty mia vince jesse leon
miami | 迈阿密 | 2 Fast 2 Furious | 🌴 | brian roman tej suki monica verone
tokyo | 东京漂移 | Tokyo Drift | 🗼 | sean han twinkie neela takashi
rio | 里约十一人 | The Rio Heist | 💰 | dom brian mia roman tej han gisele santos leo vince
shaws | 肖家人 | The Shaws | 🇬🇧 | deckard owen hattie queenie
hobbsshaw | 霍布斯与肖 | Hobbs & Shaw | 💪 | hobbs deckard hattie brixton
agency | 政府的人 | The Agency | 🕶 | hobbs mrnobody littlenobody tess elena riley
toretto | 托雷托家族 | The Torettos | ✝ | dom mia jakob littleb abuelita
villains | 宿敌 | Big Bads | 💥 | tran verone braga reyes owen jakande cipher dante
rides | 名车 | Iconic Rides | 🚗 | charger supra rx7
shawcrew | 欧文·肖的团队 | Shaw's Crew | 🎯 | owen jah riley
couples | 情侣 | Ride or Die | ❤ | dom letty brian mia han gisele
"""

RARE = {"UR": "dom brian letty han hobbs deckard"}
