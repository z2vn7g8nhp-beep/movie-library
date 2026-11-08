U = dict(id="jurassic", n="侏罗纪世界", en="Jurassic World", short="JURASSIC",
         tag="生命总会找到出路。从努布拉岛的大门打开那天起，恐龙就再没离开过人类的世界。",
         theme=["#B8402A", "#E8C86A", "#141A10"], timeline=True, wd=["Q17862144"])
ORDER = 15

WORKS = """
## jp | 侏罗纪公园 | Jurassic Park
jp1 | Jurassic Park | 1993 | 侏罗纪公园 | tl=1993
jp2 | The Lost World: Jurassic Park | 1997 | 侏罗纪公园2：失落的世界 | tl=1997
jp3 | Jurassic Park III | 2001 | 侏罗纪公园3 | tl=2001
## jw | 侏罗纪世界 | Jurassic World
jw1 | Jurassic World | 2015 | 侏罗纪世界 | tl=2015
jw2 | Jurassic World: Fallen Kingdom | 2018 | 侏罗纪世界2 | tl=2018
jw3 | Jurassic World: Dominion | 2022 | 侏罗纪世界3 | tl=2022
jwr | Jurassic World: Rebirth | 2025 | 侏罗纪世界：重生 | tl=2027
## anim | 动画剧集 | Animated Series
cc | Jurassic World: Camp Cretaceous | 2020 | 侏罗纪世界：白垩纪营地 | ty=s x tl=2015.5
ct | Jurassic World: Chaos Theory | 2024 | 侏罗纪世界：混沌理论 | ty=s x tl=2021
"""

CHARS = """
# —— 侏罗纪公园
grant | 艾伦·格兰特 | Dr. Alan Grant | 古生物学家 | Sam Neill | jp1 jp3 jw3 | #8A6A3A | 古生物学家;侏罗纪公园 | 研究:迅猛龙;标志:宽檐帽;最怕:小孩（后来改观了） | ellie:搭档与旧爱;malcolm:老冤家;lex:救下的孩子;tim:救下的孩子;raptors:研究了一辈子的动物
> 一辈子挖化石的古生物学家，不喜欢小孩也不喜欢电脑。第一次看见活着的腕龙时，他摘下墨镜，说不出话来。
ellie | 艾莉·萨特勒 | Dr. Ellie Sattler | 古植物学家 | Laura Dern | jp1 jp3 jw3 | #A07A4A | 古植物学家;侏罗纪公园 | 名场面:把手伸进三角龙的粪便里找病因;名言:恐龙和人类……你决定吧 | grant:搭档与旧爱;malcolm:老友
> 聪明、利落的古植物学家，不怕脏也不怕恐龙。公园停电时，是她去重启了电源。
malcolm | 伊恩·马尔科姆 | Dr. Ian Malcolm | 混沌理论数学家 | Jeff Goldblum | jp1 jp2 jw2 jw3 | #2E2E36 | 数学家;侏罗纪公园 | 专业:混沌理论;名言:生命总会找到出路;标志:黑色皮衣、敞开的衬衫 | grant:老冤家;ellie:老友;sarah:恋人;kelly:女儿;hammond:一直在提醒的人
> 一身黑衣的混沌理论学家，从一开始就说这个公园一定会出事。“生命总会找到出路。”他说中了，一次又一次。
hammond | 约翰·哈蒙德 | John Hammond | 公园创始人 | Richard Attenborough | jp1 jp2 | #E0D8C0 | 英根公司;侏罗纪公园 | 口头禅:不惜一切代价;手杖:里面封着一只琥珀蚊子 | lex:外孙女;tim:外孙;wu:手下的科学家
> 白胡子、拄着琥珀手杖的老富翁，梦想让孩子们看到真正的恐龙。他“不惜一切代价”，代价却比他想的大。
lex | 莱克斯 | Lex Murphy | 哈蒙德的外孙女 | Ariana Richards | jp1 jp2 | #C08A6A | 侏罗纪公园 | 特长:电脑黑客（这是个 Unix 系统！）;饮食:素食者 | tim:弟弟;hammond:外公;grant:救下她的人
> 哈蒙德的外孙女，最后是她在控制室的电脑上救了大家。
tim | 提姆 | Tim Murphy | 哈蒙德的外孙 | Joseph Mazzello | jp1 jp2 | #6A8AA0 | 侏罗纪公园 | 最爱:恐龙、格兰特博士的书;趣事:被电网电飞 | lex:姐姐;grant:偶像
> 恐龙迷小男孩，看过格兰特写的每一本书。被霸王龙推下树、被电网电飞，坚强得不像个孩子。
muldoon | 罗伯特·马尔登 | Robert Muldoon | 猎场看守 | Bob Peck | jp1 | #6A6A3A | 侏罗纪公园 | 名台词:聪明的女孩（对迅猛龙说） | raptors:最懂也最怕的动物
> 公园的猎场看守，比谁都清楚迅猛龙有多聪明。“聪明的女孩……”
nedry | 丹尼斯·纳德里 | Dennis Nedry | 背叛公园的程序员 | Wayne Knight | jp1 | #8A7A5A | 侏罗纪公园 | 名台词:啊啊啊，你没说暗号！;道具:剃须膏罐里的胚胎 | dodgson:收买他的人;dilophosaurus:遇见的恐龙
> 公园的程序员，为了钱关掉了整个公园的电网。他在雨夜里遇到了一只会喷毒液的小恐龙。
arnold | 雷·阿诺德 | Ray Arnold | 总工程师 | Samuel L. Jackson | jp1 | #4A4A5A | 侏罗纪公园 | 标志:嘴里叼着烟;名台词:抓紧你们的屁股
> 一根接一根抽烟的总工程师，重启系统前说了句“抓紧你们的屁股”。
gennaro | 吉纳罗 | Donald Gennaro | 律师 | Martin Ferrero | jp1 | #8A8A6A | 投资方律师 | 结局:在马桶上被霸王龙吃掉
> 只关心钱的律师，霸王龙来的时候丢下孩子躲进了厕所。
wu | 吴博士 | Dr. Henry Wu | 首席遗传学家 | BD Wong | jp1 jw1 jw2 jw3 | #5A6A7A | 英根公司;生物合成 | 作品:所有恐龙、暴虐霸王龙、帝王暴龙;信条:从来就没有“自然”的恐龙 | hammond:老东家;masrani:老板;indominus:亲手设计的怪物;indoraptor:亲手设计的怪物;maisie:想研究的女孩
> 从第一部到最后一部的遗传学家，所有恐龙都出自他手。他造出的东西越来越可怕，最后连他自己也后悔了。
dodgson | 道奇森 | Lewis Dodgson | 生物合成公司老板 | Cameron Thor; Campbell Scott | jp1 jw3 | #4A5A4A | 生物合成公司 | 道具:剃须膏罐 | nedry:收买的人
> 当年收买纳德里偷胚胎的竞争对手，三十年后成了生物合成公司的掌门人。
# —— 失落的世界
sarah | 莎拉·哈丁 | Dr. Sarah Harding | 动物行为学家 | Julianne Moore | jp2 | #A06A3A | 古生物学家 | 专业:动物行为学;名场面:玻璃快要碎了的那场 | malcolm:恋人
> 马尔科姆的女朋友，研究恐龙育儿行为的科学家，第一个冲上了索纳岛。
nick | 尼克·范欧文 | Nick Van Owen | 摄影师兼环保人士 | Vince Vaughn | jp2 | #6A7A5A | 环保主义者 | 名场面:偷走霸王龙幼崽 | sarah:并肩冒险
> 跟着马尔科姆上岛的摄影师，暗中破坏了猎人们的营地。
eddie | 艾迪·卡尔 | Eddie Carr | 装备工程师 | Richard Schiff | jp2 | #8A7A6A | 马尔科姆的团队 | 发明:移动实验室拖车
> 负责装备的工程师，嘴上抱怨，危急时刻却拼了命救大家。
tembo | 罗兰·坦博 | Roland Tembo | 职业猎人 | Pete Postlethwaite | jp2 | #6A5A3A | 英根公司雇佣的猎人 | 目标:亲手猎一只雄性霸王龙 | ludlow:雇主
> 来自肯尼亚的职业猎人，来岛上只为了一个目标：猎杀一只雄性霸王龙。
ludlow | 彼得·路德洛 | Peter Ludlow | 哈蒙德的外甥 | Arliss Howard | jp2 | #5A5A6A | 英根公司 | 计划:把霸王龙运到圣地亚哥 | hammond:舅舅
> 夺走英根公司的哈蒙德外甥，把一只霸王龙运进了圣地亚哥。
kelly | 凯莉·马尔科姆 | Kelly Malcolm | 马尔科姆的女儿 | Vanessa Lee Chester | jp2 | #8A5A6A | 侏罗纪公园 | 特长:体操（踢飞迅猛龙） | malcolm:爸爸
> 马尔科姆的女儿，用体操动作把一只迅猛龙踢出了窗外。
# —— 侏罗纪公园3
kirby_p | 保罗·柯比 | Paul Kirby | 寻子的父亲 | William H. Macy | jp3 | #6A6A5A | 柯比一家 | 职业:卖瓷砖和浴缸的小老板 | amanda:前妻;eric:儿子
> 谎称自己是富豪，把格兰特骗上岛的老实人，其实只是想找回失踪的儿子。
amanda | 阿曼达·柯比 | Amanda Kirby | 寻子的母亲 | Téa Leoni | jp3 | #A06A5A | 柯比一家 | 特长:尖叫（嗓门很大） | kirby_p:前夫;eric:儿子
> 在岛上拿着扩音器大喊儿子名字，结果把恐龙全招来了。
eric | 埃里克·柯比 | Eric Kirby | 在岛上活了八周的男孩 | Trevor Morgan | jp3 | #6A8A5A | 柯比一家 | 生存技能:用霸王龙尿驱赶其他恐龙 | grant:偶像
> 在恐龙岛上独自活了八周的男孩，用格兰特的书活了下来。
billy | 比利·布伦南 | Billy Brennan | 格兰特的助手 | Alessandro Nivola | jp3 | #8A6A4A | 古生物学家 | 惹的祸:偷了两枚迅猛龙蛋 | grant:导师
> 格兰特的年轻助手，偷了迅猛龙蛋想换研究经费，差点害死所有人。
# —— 侏罗纪世界
owen | 欧文·格雷迪 | Owen Grady | 迅猛龙训练员 | Chris Pratt | jw1 jw2 jw3 | #6A7A4A | 侏罗纪世界;前海军 | 招牌动作:伸手安抚迅猛龙;座驾:摩托车 | claire:恋人;blue:亲手带大的迅猛龙;maisie:领养的女儿;barry:好兄弟
> 前海军，能和迅猛龙对视的训练员。他伸出手掌让四只迅猛龙安静下来的样子，成了新三部曲的标志。
claire | 克莱尔·迪林 | Claire Dearing | 公园运营总监 | Bryce Dallas Howard | jw1 jw2 jw3 | #C0603A | 侏罗纪世界;恐龙保护组织 | 名场面:穿着高跟鞋跑赢霸王龙;后来:恐龙保护组织创始人 | owen:恋人;zach:外甥;gray:外甥;maisie:领养的女儿;rexy:她点燃火把引来的帮手
> 一开始只把恐龙当“资产”的运营总监，穿着高跟鞋在丛林里跑了一整部。后来，她把一生都用来保护它们。
masrani | 西蒙·马斯拉尼 | Simon Masrani | 侏罗纪世界老板 | Irrfan Khan | jw1 | #8A6A3A | 马斯拉尼集团 | 爱好:自己开直升机（还没考到驾照） | wu:手下;claire:手下
> 继承哈蒙德梦想的亿万富翁，热情、天真，自己开着直升机去追逃跑的恐龙。
hoskins | 维克·霍斯金斯 | Vic Hoskins | 英根安保主管 | Vincent D'Onofrio | jw1 | #4A4A3A | 英根公司 | 计划:把迅猛龙变成武器 | owen:想利用的人
> 一心想把迅猛龙训练成军事武器的安保主管。
lowery | 洛厄里 | Lowery Cruthers | 控制室技术员 | Jake Johnson | jw1 | #8A8A6A | 侏罗纪世界 | 收藏:网上买的初代公园 T 恤;桌上:一堆恐龙玩具
> 控制室里的老员工，穿着初代侏罗纪公园的 T 恤，是整个公园最怀旧的人。
barry | 巴里 | Barry Sembène | 欧文的好兄弟 | Omar Sy | jw1 jw3 | #5A4A3A | 侏罗纪世界 | 工作:迅猛龙围场 | owen:好兄弟
> 欧文在迅猛龙围场的搭档，后来在马耳他再次登场。
zach | 扎克 | Zach Mitchell | 克莱尔的外甥 | Nick Robinson | jw1 | #5A6A8A | 侏罗纪世界 | 状态:叛逆期 | gray:弟弟;claire:姨妈
> 来公园度假的哥哥，叛逆期，最后成了保护弟弟的人。
gray | 格雷 | Gray Mitchell | 恐龙迷弟弟 | Ty Simpkins | jw1 | #6A8AA0 | 侏罗纪世界 | 最爱:恐龙知识 | zach:哥哥;claire:姨妈
> 背得出所有恐龙数据的小弟弟，在旧公园的游客中心修好了老吉普。
maisie | 梅茜·洛克伍德 | Maisie Lockwood | 克隆的女孩 | Isabella Sermon | jw2 jw3 | #A07A8A | 洛克伍德庄园 | 秘密:她是一个克隆人;决定:打开大门放走恐龙 | owen:养父;claire:养母;lockwood:外公（名义上）;blue:相似的命运
> 在洛克伍德庄园长大的小女孩，后来发现自己是一个克隆人。是她按下了按钮，让恐龙走进了人类世界。
lockwood | 本杰明·洛克伍德 | Benjamin Lockwood | 哈蒙德的老搭档 | James Cromwell | jw2 | #8A8A7A | 洛克伍德庄园 | 往事:和哈蒙德一起创造了克隆技术 | maisie:外孙女;mills:信任错的人
> 哈蒙德当年的合伙人，晚年住在庄园里，守着一个关于外孙女的秘密。
mills | 伊莱·米尔斯 | Eli Mills | 洛克伍德的管家 | Rafe Spall | jw2 | #4A4A5A | 洛克伍德庄园 | 计划:拍卖恐龙
> 表面替洛克伍德管事，背地里把恐龙卖给全世界的军火商。
franklin | 富兰克林 | Franklin Webb | 胆小的黑客 | Justice Smith | jw2 jw3 | #6A6AA0 | 恐龙保护组织 | 特长:IT、尖叫
> 恐龙保护组织的 IT 小哥，胆子小、尖叫声大。
zia | 齐亚 | Zia Rodriguez | 恐龙兽医 | Daniella Pineda | jw2 jw3 | #6A4A6A | 恐龙保护组织 | 职业:古生物兽医
> 恐龙保护组织的兽医，嘴硬心软，冒着生命危险给布鲁输血。
wheatley | 威特利 | Ken Wheatley | 雇佣兵头子 | Ted Levine | jw2 | #5A5A3A | 雇佣兵 | 爱好:拔恐龙的牙当纪念品
> 带队抓恐龙的雇佣兵，有个拔恐龙牙齿当战利品的坏习惯。
kayla | 凯拉·沃茨 | Kayla Watts | 走私飞行员 | DeWanda Wise | jw3 | #6A5A3A | 走私者 | 座驾:老式货运飞机
> 开货运飞机的走私者，后来决定站在正确的一边。
ramsay | 拉姆齐·科尔 | Ramsay Cole | 生物合成公司员工 | Mamoudou Athie | jw3 | #5A6A6A | 生物合成公司 | 角色:暗中帮助马尔科姆
> 生物合成公司的年轻员工，在公司内部悄悄帮助了科学家们。
soyona | 索约娜 | Soyona Santos | 恐龙走私商 | Dichen Lachman | jw3 | #4A3A4A | 黑市 | 手下:训练过的异特龙杀手
> 马耳他恐龙黑市的老大，用激光指示器让恐龙替她杀人。
# —— 重生
zora | 佐拉·贝内特 | Zora Bennett | 秘密行动专家 | Scarlett Johansson | jwr | #6A5A4A | 雇佣兵;重生小队 | 任务:从三种巨型恐龙身上采集血样 | duncan:多年老搭档;loomis:合作的科学家;krebs:雇主
> 接下一个看似不可能的任务的特工：从陆地、海洋和天空中最大的三种恐龙身上采血。
duncan | 邓肯·金凯德 | Duncan Kincaid | 船长 | Mahershala Ali | jwr | #4A5A6A | 重生小队 | 职业:船长 | zora:多年老搭档
> 带着船员深入禁区的老船长，沉稳可靠。
loomis | 亨利·卢米斯 | Dr. Henry Loomis | 古生物学家 | Jonathan Bailey | jwr | #7A6A4A | 古生物学家;重生小队 | 性格:单纯、热爱恐龙、会对着恐龙流泪 | zora:合作的特工;grant:他的偶像
> 真心热爱恐龙的古生物学家，第一次近距离看到泰坦龙时，激动得说不出话。
krebs | 马丁·克雷布斯 | Martin Krebs | 制药公司代表 | Rupert Friend | jwr | #5A5A5A | 帕克·詹宁斯制药 | 目的:用恐龙血研制心脏病药物
> 制药公司的代表，嘴上为了人类健康，心里只算钱。
reuben | 鲁本·德尔加多 | Reuben Delgado | 遇难的父亲 | Manuel Garcia-Rulfo | jwr | #6A5A3A | 德尔加多一家 | teresa:女儿;isabella:女儿
> 带着女儿们出海旅行的父亲，帆船被沧龙掀翻，困在了恐龙岛上。
teresa | 特蕾莎 | Teresa Delgado | 鲁本的大女儿 | Luna Blaise | jwr | #A06A6A | 德尔加多一家 | reuben:父亲;isabella:妹妹;xavier:男朋友
> 德尔加多家的大女儿，在岛上保护着妹妹。
isabella | 伊莎贝拉 | Isabella Delgado | 鲁本的小女儿 | Audrina Miranda | jwr | #C08A8A | 德尔加多一家 | 新朋友:一只小恐龙“多洛蕾斯” | reuben:父亲;teresa:姐姐
> 最小的女儿，在岛上偷偷养了一只小恐龙。
xavier | 泽维尔 | Xavier Dobbs | 特蕾莎的男朋友 | David Iacono | jwr | #6A6A5A | 德尔加多一家 | teresa:女朋友
> 特蕾莎的男朋友，一路上都很不靠谱，但还是尽力了。
# —— 白垩纪营地
darius | 达里厄斯 | Darius Bowman | 恐龙迷少年 | vo:Paul-Mikél Williams | cc ct | #4A6A9A | 白垩纪营地 | 最爱:恐龙知识（游戏高手）;偶像:去世的父亲 | brooklynn:伙伴;kenji:伙伴;yaz:伙伴;ben:伙伴;sammy:伙伴
> 赢下比赛来到侏罗纪世界营地的恐龙迷，是营地六人组里最懂恐龙的人。
brooklynn | 布鲁克林 | Brooklynn | 网红少女 | vo:Jenna Ortega; Kiersten Kelly | cc ct | #A06AA0 | 白垩纪营地 | 身份:网络博主;后来:调查记者 | darius:伙伴;kenji:恋人
> 坐拥百万粉丝的网络博主，在岛上从拍视频变成了寻找真相的人。
kenji | 健二 | Kenji Kon | 富二代 | vo:Ryan Potter | cc ct | #6A5A9A | 白垩纪营地 | 家世:父亲是马斯拉尼集团的大股东 | brooklynn:恋人;darius:伙伴
> 有钱又爱炫耀的富家少爷，嘴上没个正经，却会在关键时刻挺身而出。
yaz | 雅斯 | Yasmina Fadoula | 田径运动员 | vo:Kausar Mohammed | cc ct | #8A5A3A | 白垩纪营地 | 特长:跑步;性格:冷静、独立 | sammy:恋人;darius:伙伴
> 冷静独立的田径选手，跑得比迅猛龙还快。
ben | 本 | Ben Pincus | 胆小的男孩 | vo:Sean Giambrone | cc ct | #6A8A5A | 白垩纪营地 | 最好的朋友:小甲龙 Bumpy | bumpy:好朋友;darius:伙伴
> 一开始什么都怕的男孩，后来一个人在丛林里活了下来，还和一只小甲龙成了好朋友。
sammy | 萨米 | Sammy Gutierrez | 开朗的牧场女孩 | vo:Raini Rodriguez | cc ct | #C08A3A | 白垩纪营地 | 秘密:接受了公司的间谍任务 | yaz:恋人;darius:伙伴
> 最热情开朗的牧场女孩，背负着一个不能说的秘密。
bumpy | 小甲龙 | Bumpy | 本的甲龙 | - | cc ct | #A08A5A | 恐龙;白垩纪营地 | 物种:甲龙 | ben:最好的朋友
> 本从小照顾大的甲龙，脑袋上有个小包。
# —— 恐龙
rexy | 雷克西 | Rexy | 初代公园的霸王龙 | - | jp1 jw1 jw2 jw3 | #8A3A2A | 恐龙;顶级掠食者 | 物种:霸王龙;年代:白垩纪晚期;体长:约 12 米;名场面:游客中心里的“终极大吼” | indominus:并肩对抗的怪物;giga:宿敌;claire:放她出来的人
> 从第一部的雨夜里撞翻吉普车的那只霸王龙，三十年后依然是这座岛上的女王。
raptors | 迅猛龙 | Velociraptors | 聪明的猎手 | - | jp1 jp3 | #6A6A3A | 恐龙 | 物种:伶盗龙（电影里的体型是放大版）;特点:会开门、会群体狩猎 | muldoon:猎场看守;grant:研究它们的人
> 会转门把手、会设陷阱的猎手。电影里的迅猛龙比真实的大得多，聪明得也多。
blue | 布鲁 | Blue | 欧文的迅猛龙 | - | jw1 jw2 jw3 | #3E6A9A | 恐龙;迅猛龙小队 | 物种:伶盗龙;特征:身上的蓝色条纹;小队:布鲁、查理、德尔塔、回声 | owen:亲手带大她的人;maisie:相似的命运
> 欧文亲手带大的迅猛龙，四姐妹里的老大。后来，她生下了自己的孩子“小贝塔”。
indominus | 暴虐霸王龙 | Indominus Rex | 人造混种 | - | jw1 | #E0E0D8 | 恐龙;人造混种 | 基因:霸王龙、迅猛龙、墨鱼、树蛙等;能力:伪装、热感隐身、高智商 | wu:设计者;rexy:合力击败她的霸王龙;blue:被她拉拢又背叛
> 吴博士为了吸引游客造出的混种恐龙，聪明、残暴、会伪装。她从出生起就是孤独的。
indoraptor | 暴虐迅猛龙 | Indoraptor | 武器化的混种 | - | jw2 | #2A2A2E | 恐龙;人造混种 | 基因:暴虐霸王龙 + 迅猛龙;设计用途:用激光指示器攻击目标 | wu:设计者;maisie:潜入她卧室的怪物
> 为了卖给军火商而造的混种杀手，在洛克伍德庄园里爬上了梅茜的屋顶。
spinosaurus | 棘龙 | Spinosaurus | 背帆巨兽 | - | jp3 | #6A5A3A | 恐龙 | 年代:白垩纪;体长:约 15 米;特征:背上的帆、像鳄鱼的嘴
> 背上长着大帆的巨兽，第三部里打败了一只霸王龙。
giga | 南方巨兽龙 | Giganotosaurus | 地球史上最大的掠食者之一 | - | jw3 | #5A4A3A | 恐龙;顶级掠食者 | 年代:白垩纪晚期;体长:约 13 米 | rexy:宿敌
> 生物合成公司保护区里的霸主，和雷克西有一场宿命之战。
drex | 畸变霸王龙 | Distortus Rex | 变异的怪物 | - | jwr | #4A4A4A | 恐龙;变异体 | 来历:实验室里失败的变异体;特征:六条肢体、巨大的头颅
> 被遗弃的实验室里诞生的变异怪物，比任何恐龙都可怕。
mosasaurus | 沧龙 | Mosasaurus | 海洋霸主 | - | jw1 jw2 jw3 jwr | #3A5A7A | 远古海洋爬行动物 | 年代:白垩纪晚期;名场面:一口吞下一条大白鲨
> 侏罗纪世界最受欢迎的表演：从水里跃起，一口吞下一条大白鲨。
dilophosaurus | 双冠龙 | Dilophosaurus | 会喷毒液的小家伙 | - | jp1 jw3 | #6A8A3A | 恐龙 | 年代:侏罗纪早期;电影设定:颈部伞膜、喷毒（真实的双冠龙没有） | nedry:遇见的人
> 歪着头发出咕咕声、突然展开伞膜喷毒液的小恐龙——这个设定是电影的创造。
brachio | 腕龙 | Brachiosaurus | 温柔的巨人 | - | jp1 jp3 jw2 jw3 | #8A9A7A | 恐龙 | 年代:侏罗纪晚期;名场面:第一部里第一只出场的恐龙
> 整个系列第一只出场的恐龙，格兰特摘下墨镜看它的那一刻，成了影史经典。
trike | 三角龙 | Triceratops | 生病的三角龙 | - | jp1 jp2 jw3 | #8A6A4A | 恐龙 | 年代:白垩纪晚期 | ellie:为她诊病的人
> 艾莉为她诊病的那只三角龙，是格兰特小时候最喜欢的恐龙。
pteranodon | 无齿翼龙 | Pteranodon | 天空的猎手 | - | jp3 jw1 jw2 jw3 | #8A6A5A | 翼龙 | 年代:白垩纪
> 在第三部的鸟舍里第一次登场，在侏罗纪世界里冲出了笼子。
quetzal | 风神翼龙 | Quetzalcoatlus | 天空的巨人 | - | jw3 jwr | #7A6A5A | 翼龙 | 年代:白垩纪晚期;特点:有史以来最大的飞行动物之一
> 翼展超过十米的巨型翼龙，是重生小队要采血的三种巨兽之一。
titanosaurus | 泰坦龙 | Titanosaurus | 陆地巨兽 | - | jwr | #7A8A6A | 恐龙 | 特点:陆地上最大的恐龙之一
> 重生小队要采血的陆地巨兽，长颈伸向天空，像一座会走路的山。
stygi | 冥河龙 | Stygimoloch | 用脑袋撞墙的小家伙 | - | jw2 | #6A5A6A | 恐龙 | 年代:白垩纪晚期;特长:用头撞开一切
> 头顶长满尖刺的小恐龙，在庄园地下室里一头撞开了笼子。
therizino | 镰刀龙 | Therizinosaurus | 长着巨爪的植食者 | - | jw3 | #8A7A5A | 恐龙 | 年代:白垩纪晚期;特征:一米长的爪子
> 吃素的大家伙，却有着一米长的爪子，在冰湖边追了克莱尔一路。
compy | 美颌龙 | Compsognathus | 成群的小恐龙 | - | jp2 jw2 | #8A8A5A | 恐龙 | 体型:和鸡差不多
> 和鸡差不多大的小恐龙，一只不可怕，一群就可怕了。
"""

DECKS = """
og | 初代公园 | Jurassic Park Originals | 🦖 | grant ellie malcolm hammond lex tim
legacy | 传奇三人组 | The Legacy Trio | 🧬 | grant ellie malcolm
lostworld | 失落的世界 | The Lost World | 📷 | malcolm sarah nick eddie kelly tembo ludlow
isla | 柯比一家的求救 | Isla Sorna Rescue | 🛩 | grant kirby_p amanda eric billy
world | 侏罗纪世界 | Jurassic World | 🎢 | owen claire masrani lowery barry zach gray
dpg | 恐龙保护组织 | Dinosaur Protection Group | 🛡 | owen claire franklin zia maisie
greed | 贪婪的人们 | The Greedy | 💼 | nedry ludlow hoskins mills wheatley dodgson krebs
rebirth | 重生小队 | Rebirth Team | 🩸 | zora duncan loomis krebs
delgados | 德尔加多一家 | The Delgados | ⛵ | reuben teresa isabella xavier
camp | 白垩纪营地六人组 | Camp Fam | ⛺ | darius brooklynn kenji yaz ben sammy
apex | 顶级掠食者 | Apex Predators | 👑 | rexy indominus spinosaurus giga drex indoraptor
raptor | 迅猛龙 | Raptor Squad | 🦎 | raptors blue
skysea | 天空与深海 | Sky & Sea | 🌊 | pteranodon quetzal mosasaurus
gentle | 温柔的巨兽 | Gentle Giants | 🌿 | brachio trike titanosaurus bumpy therizino
hybrid | 人造混种 | Hybrids | 🧪 | indominus indoraptor drex wu
"""

RARE = {"UR": "grant ellie malcolm owen claire rexy blue"}
