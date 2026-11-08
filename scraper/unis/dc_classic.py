U = dict(id="dcx", extend="dc", wiki="dc", wd=["Q2111133", "Q2158362", "Q12859908", "Q116545465"])

WORKS = """
## classic | 经典老片 | Classics
bm66 | Batman: The Movie | 1966 | 蝙蝠侠：电影版 | x
sm78 | Superman | 1978 | 超人 | x
sm2 | Superman II | 1980 | 超人2 | x
sm3 | Superman III | 1983 | 超人3 | x
sg84 | Supergirl | 1984 | 超级少女 | x
sm4 | Superman IV: The Quest for Peace | 1987 | 超人4：和平任务 | x
bm89 | Batman | 1989 | 蝙蝠侠 | x
bmr | Batman Returns | 1992 | 蝙蝠侠归来 | x
bmf | Batman Forever | 1995 | 永远的蝙蝠侠 | x
bmar | Batman & Robin | 1997 | 蝙蝠侠与罗宾 | x
cw04 | Catwoman | 2004 | 猫女 | x
const05 | Constantine | 2005 | 地狱神探 | x
smr | Superman Returns | 2006 | 超人归来 | x
gl11 | Green Lantern | 2011 | 绿灯侠 | x
"""

CHARS = """
# —— 已有角色补出场
batman_k | - | - | - | - | bm89 bmr | - | 蒂姆·伯顿版;哥谭 | 演员:迈克尔·基顿;名台词:I'm Batman（我是蝙蝠侠）;座驾:伯顿版蝙蝠车 | vicki:恋人;joker_n:宿敌;catwoman_p:心动的对手;alfred_g:管家
jorel | - | - | - | - | - | - | 氪星 | - | superman_c:儿子
aquaman | - | - | - | - | pm | - | 正义联盟;亚特兰蒂斯国王 | 真名:亚瑟·库瑞;武器:三叉戟;能力:和海洋生物对话、水下呼吸 | mera:妻子;atlanna:母亲;orm:同母异父的弟弟;manta:宿敌;vulko:老师
vandal | 范达尔 | Vandal | 《新蝙蝠侠》· 哥谭帮派少年 | Spike Fearn | batman | #5A4A4A | 哥谭;街头帮派 | 造型:涂着小丑妆的帮派少年;名场面:地铁站里被蝙蝠侠教训 | batman_p:被他教训的人
> 《新蝙蝠侠》开场那群涂着小丑脸的帮派少年之一，在地铁站里第一个尝到了“复仇”的拳头。
murk | 默克队长 | Captain Murk | 亚特兰蒂斯禁卫军队长 | Ludi Lin | aqua1 | #3E6E8A | 亚特兰蒂斯;禁卫军 | 效忠:奥姆国王 | orm:效忠的国王;aquaman:追捕的对象
> 奥姆麾下的亚特兰蒂斯禁卫军队长，奉命追捕海王。
superman_c | - | - | - | - | - | - | 正义联盟;氪星之子 | 真名:卡-艾尔 / 克拉克·肯特;能力:飞行、热视线、超级力量、冰冻呼吸;弱点:氪石;家:堪萨斯州斯莫维尔 | lois_a:一生挚爱;martha:养母;jonathan:养父;jorel:生父;batman_a:从对手到战友;zod:同族的宿敌;ww:正义联盟的战友
batman_a | - | - | - | - | - | - | 正义联盟;哥谭 | 真名:布鲁斯·韦恩;年龄:打击犯罪二十年的老蝙蝠;装备:机甲战衣、蝙蝠翼 | superman_c:从对手到战友;ww:并肩的伙伴;flash:最年轻的队友
ww | - | - | - | - | - | - | 正义联盟;天堂岛 | 真名:戴安娜·普林斯;武器:真言套索、弑神剑、手镯;出身:亚马逊人的公主 | trevor:一生挚爱;superman_c:正义联盟的战友;batman_a:并肩的伙伴;ares:宿敌;cheetah:曾经的朋友
flash | - | - | - | - | - | - | 正义联盟 | 真名:巴里·艾伦;能力:神速力;趣事:跑起来特别饿，一顿要吃一大堆 | batman_a:招募他的人;batman_k:另一个宇宙遇见的蝙蝠侠;supergirl_f:另一个宇宙的战友
cyborg | - | - | - | - | - | - | 正义联盟 | 真名:维克多·斯通;来历:被父亲用母盒救活的半机械人 | flash:年纪最小的两个队友
harley | - | - | - | - | - | - | X特遣队;猛禽小队 | 真名:哈琳·奎茵泽尔;前职业:阿卡姆疯人院的精神科医生;武器:棒球棍、木槌;宠物:土狼布鲁斯 | joker_l:前男友;deadshot:X特遣队的搭档;bloodsport:全员集结的队友;huntress:猛禽小队的姐妹
joker_h | - | - | - | - | - | - | 哥谭 | 名台词:为什么这么严肃？;造型:裂开的嘴角、晕开的白脸;信条:混乱 | batman_b:他眼里“完美的对手”;twoface:被他推向深渊的人
batman_b | - | - | - | - | - | - | 哥谭 | 真名:布鲁斯·韦恩;座驾:蝙蝠车“不倒翁”;训练:影武者联盟 | alfred_n:最像父亲的人;rachel:青梅竹马;joker_h:宿敌;ras:导师与敌人;catwoman_h:最后一起离开的人;lucius:装备供应商
batman_p | - | - | - | - | - | - | 哥谭 | 真名:布鲁斯·韦恩;自称:我是复仇;年份:成为蝙蝠侠的第二年 | catwoman_k:心动的人;riddler:对手;gordon_p:唯一信任的警察;alfred_p:管家;penguin:对手;vandal:被他教训的少年
catwoman_k | - | - | - | - | - | - | 哥谭 | 真名:赛琳娜·凯尔;最爱:猫（养了一屋子） | batman_p:心动的人;falcone:父亲
superman_d | - | - | - | - | - | - | 正义帮;氪星之子 | 真名:卡-艾尔 / 克拉克·肯特;最爱:小狗小氪;信念:善良本身就是一种朋克 | lois:恋人;krypto:他的狗;lex_h:宿敌;supergirl:堂妹;guy:合作的英雄
lois | - | - | - | - | - | - | 星球日报 | 特点:一针见血的采访 | superman_d:恋人;jimmy:同事;perry:主编
krypto | - | - | - | - | - | - | 超人一家 | 性格:不听话、会把超人拖着满天飞 | superman_d:照顾它的人;supergirl:真正的主人
peacemaker | - | - | - | - | - | - | X特遣队;第 11 小队 | 真名:克里斯托弗·史密斯;口号:为了和平，不惜一切;宠物:老鹰伊格利;标志:马桶盖一样的头盔 | eagly:他的老鹰;vigilante:最好的兄弟;harcourt:队友;bloodsport:较劲的对手;waller:上司
waller | - | - | - | - | - | - | 阿格斯 | 职位:X特遣队的幕后主人;手段:在队员脑袋里装炸弹 | peacemaker:手下;harley:手下
# —— 1966
batman_w | 蝙蝠侠 | Batman | 1966 版 · 亚当·韦斯特 | Adam West | bm66 | #6A6AA0 | 1966 电视版;哥谭 | 标志:灰蓝色紧身衣、画上去的眉毛;道具:蝙蝠驱鲨喷雾 | robin_w:搭档;joker_r:对手
> 最早走上大银幕的蝙蝠侠之一，一本正经地掏出“蝙蝠驱鲨喷雾”，是一代人心里最可爱的蝙蝠侠。
robin_w | 罗宾 | Robin | 1966 版 · 伯特·沃德 | Burt Ward | bm66 | #C8402E | 1966 电视版 | 口头禅:Holy ……, Batman!（圣什么什么啊，蝙蝠侠！） | batman_w:搭档
> 每句话都以“圣……啊，蝙蝠侠！”开头的少年神奇小子。
joker_r | 小丑 | The Joker | 1966 版 · 罗密欧 | Cesar Romero | bm66 | #5A9A5A | 1966 电视版 | 趣事:拒绝剃掉自己的小胡子，直接在上面涂了白粉 | batman_w:对手
> 1966 版的小丑，笑声尖利，还坚持留着小胡子——白粉直接涂在胡子上。
catwoman_m | 猫女 | Catwoman | 1966 版 · 梅里韦瑟 | Lee Meriwether | bm66 | #3A3A4A | 1966 电视版
> 1966 年电影版里的猫女，伪装成俄罗斯记者接近布鲁斯·韦恩。
penguin_m | 企鹅人 | The Penguin | 1966 版 · 梅雷迪思 | Burgess Meredith | bm66 | #4A4A5A | 1966 电视版 | 标志:单片眼镜、长烟嘴、雨伞
> 拿着雨伞、叼着长烟嘴、“哇哇”怪叫的企鹅人。
riddler_g | 谜语人 | The Riddler | 1966 版 · 戈申 | Frank Gorshin | bm66 | #5AAA4A | 1966 电视版
> 穿着问号紧身衣、笑得停不下来的谜语人。
# —— 伯顿与舒马赫
vicki | 维姬·维尔 | Vicki Vale | 摄影记者 | Kim Basinger | bm89 | #C8A06A | 哥谭 | 职业:摄影记者 | batman_k:恋人;joker_n:盯上她的疯子
> 来哥谭追蝙蝠侠新闻的摄影记者，被布鲁斯·韦恩和小丑同时盯上。
joker_n | 小丑 | The Joker | 伯顿版 · 杰克·尼科尔森 | Jack Nicholson | bm89 | #6A3A9A | 哥谭 | 本名:杰克·纳皮尔;名台词:你在苍白的月光下和魔鬼跳过舞吗？;来历:掉进化学池 | batman_k:宿敌;vicki:迷恋的人
> 掉进化学池后笑容永久定格的黑帮打手，在哥谭街头放着王子的歌跳舞、发钱、杀人。
alfred_g | 阿尔弗雷德 | Alfred | 伯顿 / 舒马赫版 · 迈克尔·高夫 | Michael Gough | bm89 bmr bmf bmar | #5A4A3A | 韦恩庄园 | batman_k:少爷;batman_v:少爷;batman_c:少爷
> 跨越四部的老管家，从基顿伺候到克鲁尼，从来没换过人。
gordon_h | 戈登局长 | Commissioner Gordon | 伯顿 / 舒马赫版 · 帕特·辛格 | Pat Hingle | bm89 bmr bmf bmar | #4A5A6A | 哥谭警局
> 四部里一直在点亮蝙蝠灯的老局长。
catwoman_p | 猫女 | Catwoman | 伯顿版 · 米歇尔·菲佛 | Michelle Pfeiffer | bmr | #2E2E36 | 哥谭 | 本名:赛琳娜·凯尔;造型:手缝的黑色皮衣;名台词:喵 | batman_k:心动的对手;shreck:害死她的老板;penguin_d:临时盟友
> 被老板推下楼的胆小秘书，被一群猫“救活”后，缝了一身黑皮衣，成了影史最性感的猫女之一。
penguin_d | 企鹅人 | The Penguin | 伯顿版 · 丹尼·德维托 | Danny DeVito | bmr | #3A3A3A | 哥谭下水道 | 本名:奥斯瓦尔德·科波特;身世:因畸形被父母扔进河里;部下:一群带火箭的企鹅 | shreck:合作伙伴;catwoman_p:临时盟友
> 一出生就被父母扔进下水道的畸形儿，被企鹅养大。他想要的，只是被这座城市接纳。
shreck | 马克斯·施莱克 | Max Shreck | 哥谭富商 | Christopher Walken | bmr | #5A5A5A | 哥谭 | catwoman_p:害了她的人;penguin_d:合作伙伴
> 道貌岸然的哥谭大亨，才是《蝙蝠侠归来》里真正的坏人。
batman_v | 蝙蝠侠 | Batman | 舒马赫版 · 方·基默 | Val Kilmer | bmf | #3A3A4A | 哥谭 | 心结:父母死去的那一晚 | robin_o:收留的少年;chase:心理医生恋人;riddler_c:对手;twoface_j:对手
> 在《永远的蝙蝠侠》里披上斗篷的方·基默，一个被童年阴影困住的布鲁斯。
twoface_j | 双面人 | Two-Face | 舒马赫版 · 汤米·李·琼斯 | Tommy Lee Jones | bmf | #8A3A6A | 哥谭 | 本名:哈维·登特;习惯:用硬币决定一切 | riddler_c:搭档
> 一半脸毁容、一半脸正常的前检察官，用一枚硬币决定生死。
riddler_c | 谜语人 | The Riddler | 舒马赫版 · 金·凯瑞 | Jim Carrey | bmf | #4AAA3A | 哥谭 | 本名:爱德华·尼格玛;发明:能吸取脑电波的盒子 | twoface_j:搭档;batman_v:曾经崇拜的老板
> 被布鲁斯·韦恩拒绝的发明家，金·凯瑞演得又疯又跳，满身问号。
robin_o | 罗宾 | Robin | 舒马赫版 · 克里斯·奥唐纳 | Chris O'Donnell | bmf bmar | #C8402E | 哥谭 | 本名:迪克·格雷森;出身:马戏团空中飞人 | batman_v:收留他的人;batman_c:搭档;batgirl:搭档
> 父母死在双面人手里的马戏团少年，被布鲁斯收留，成了罗宾。
chase | 蔡斯·梅里迪安 | Chase Meridian | 心理医生 | Nicole Kidman | bmf | #C8A0A0 | 哥谭 | batman_v:恋人
> 研究“双重人格”的心理医生，同时爱上了布鲁斯和蝙蝠侠。
batman_c | 蝙蝠侠 | Batman | 舒马赫版 · 乔治·克鲁尼 | George Clooney | bmar | #4A4A6A | 哥谭 | 趣事:战衣上有乳头;装备:蝙蝠信用卡 | robin_o:搭档;batgirl:搭档;alfred_g:病倒的管家
> 带着一张“蝙蝠信用卡”的乔治·克鲁尼，连他自己都拿这一版开过玩笑。
freeze | 急冻人 | Mr. Freeze | 维克多·弗里斯 | Arnold Schwarzenegger | bmar | #6AAAD0 | 哥谭 | 动机:救冰冻起来的病重妻子;台词风格:满口冰冷的双关语 | ivy:合作伙伴
> 为了救病重的妻子把自己变成冰人的科学家，满嘴“冰冷”的双关语。
ivy | 毒藤女 | Poison Ivy | 帕梅拉·艾斯利 | Uma Thurman | bmar | #4A9A4A | 哥谭 | 能力:毒吻、操控植物 | freeze:合作伙伴
> 被毒物泡过后能用一个吻杀人的植物学家，乌玛·瑟曼演得风情万种。
batgirl | 蝙蝠女 | Batgirl | 芭芭拉 | Alicia Silverstone | bmar | #6A4A8A | 哥谭 | 身份:阿尔弗雷德的外甥女 | robin_o:搭档
> 阿尔弗雷德的外甥女，骑着摩托加入了蝙蝠家族。
# —— 唐纳的超人
superman_r | 超人 | Superman | 克里斯托弗·里夫 | Christopher Reeve | sm78 sm2 sm3 sm4 | #2F5EB8 | 氪星之子;星球日报 | 伪装:戴眼镜、笨手笨脚的克拉克·肯特;名场面:接住坠落的直升机 | lois_k:恋人;lex_g:宿敌;zod_t:对手;jorel_b:生父;jimmy_m:同事
> 很多人心里永远的超人。戴上眼镜他是笨拙的克拉克，摘下眼镜他就是希望本身。
lois_k | 露易丝·莱恩 | Lois Lane | 唐纳版 · 玛戈·基德 | Margot Kidder | sm78 sm2 sm3 sm4 | #B44A5A | 星球日报 | 特点:风风火火、拼写很烂 | superman_r:恋人
> 风风火火、拼写很烂的王牌记者，第一次和超人夜空飞行的那一幕，浪漫得不像话。
lex_g | 莱克斯·卢瑟 | Lex Luthor | 唐纳版 · 金·哈克曼 | Gene Hackman | sm78 sm2 sm4 | #5A6A4A | 犯罪天才 | 住处:地铁站地下的豪宅;跟班:奥蒂斯 | superman_r:宿敌;otis:笨手下
> 住在地下豪宅里的“犯罪天才”，最大的爱好是地产，最大的敌人是超人。
jorel_b | 乔-艾尔 | Jor-El | 唐纳版 · 马龙·白兰度 | Marlon Brando | sm78 smr | #E0E0E0 | 氪星 | superman_r:儿子
> 在氪星毁灭前把儿子送往地球的科学家，马龙·白兰度一身白光。
jimmy_m | 吉米·奥尔森 | Jimmy Olsen | 唐纳版 · 马克·麦克卢尔 | Marc McClure | sm78 sm2 sm3 sm4 sg84 | #C9803A | 星球日报 | superman_r:同事
> 星球日报的年轻摄影师，五部里都是同一位演员。
perry_c | 佩里·怀特 | Perry White | 唐纳版 · 杰基·库珀 | Jackie Cooper | sm78 sm2 sm3 sm4 | #6A5A4A | 星球日报 | 职位:主编
> 星球日报脾气暴躁的老主编。
otis | 奥蒂斯 | Otis | 卢瑟的笨手下 | Ned Beatty | sm78 sm2 | #8A7A5A | 卢瑟的跟班 | lex_g:老板
> 卢瑟手下笨手笨脚的跟班，每次都把事情搞砸。
zod_t | 佐德将军 | General Zod | 唐纳版 · 特伦斯·斯坦普 | Terence Stamp | sm2 | #3A3A4A | 氪星罪犯;幻影地带 | 名台词:跪在佐德面前！ | ursa:部下;non:部下;superman_r:对手
> 被关进幻影地带的氪星将军，一句“跪在佐德面前！”成了经典。
ursa | 厄尔莎 | Ursa | 佐德的副手 | Sarah Douglas | sm2 | #4A3A4A | 氪星罪犯;幻影地带 | zod_t:效忠的将军
> 佐德身边冷酷的女副手。
non | 农 | Non | 不会说话的大块头 | Jack O'Halloran | sm2 | #4A4A4A | 氪星罪犯;幻影地带 | zod_t:效忠的将军
> 佐德手下不会说话的大块头。
supergirl_s | 超级少女 | Supergirl | 1984 版 · 海伦·斯莱特 | Helen Slater | sg84 | #C23A48 | 氪星 | 本名:卡拉·佐-艾尔
> 1984 年的超级少女，为了找回丢失的能量源来到地球。
superman_b | 超人 | Superman | 布兰登·罗斯 | Brandon Routh | smr | #2F5EB8 | 氪星之子 | 往事:离开地球五年后归来 | lois_b:旧爱;lex_s:宿敌
> 离开地球五年后回来的超人，发现露易丝已经写了一篇《为什么世界不需要超人》。
lois_b | 露易丝·莱恩 | Lois Lane | 归来版 · 凯特·波茨沃斯 | Kate Bosworth | smr | #B44A5A | 星球日报 | superman_b:旧爱
> 写下《为什么世界不需要超人》的露易丝，已经有了孩子和未婚夫。
lex_s | 莱克斯·卢瑟 | Lex Luthor | 归来版 · 凯文·史派西 | Kevin Spacey | smr | #5A6A4A | 犯罪天才 | 计划:用氪星水晶造一块新大陆 | superman_b:宿敌
> 刚出狱的卢瑟，想用氪星水晶造一片属于自己的大陆。
lois_a | 露易丝·莱恩 | Lois Lane | DCEU · 艾米·亚当斯 | Amy Adams | mos bvs jl zsjl | #B44A5A | 星球日报 | 特点:普利策奖记者 | superman_c:恋人;martha:未来的婆婆
> DCEU 里的露易丝，一开始就看穿了克拉克的秘密，是超人留在人间的锚。
# —— 绿灯侠、猫女、地狱神探
hal_r | 哈尔·乔丹 | Hal Jordan | 2011 版 · 瑞安·雷诺兹 | Ryan Reynolds | gl11 | #2F9A5A | 绿灯军团 | 职业:试飞员;戒指:绿灯戒（意志之力） | carol:恋人;sinestro_s:导师与对手;kilowog:教官
> 被外星戒指选中的试飞员，第一个戴上绿灯戒的地球人——后来的死侍演员对这部电影一直念念不忘地自嘲。
sinestro_s | 辛尼斯托 | Sinestro | 2011 版 · 马克·斯特朗 | Mark Strong | gl11 | #C9408A | 绿灯军团 | hal_r:看不起又认可的新人
> 绿灯军团里最强也最骄傲的战士，结尾戴上了一枚黄色的戒指。
carol | 卡罗尔·费里斯 | Carol Ferris | 哈尔的青梅竹马 | Blake Lively | gl11 | #C08A6A | 费里斯航空 | hal_r:恋人
> 航空公司老板的女儿，哈尔的青梅竹马。
hammond | 赫克托·哈蒙德 | Hector Hammond | 被感染的科学家 | Peter Sarsgaard | gl11 | #6A6A5A | 科学家 | 来历:被视差怪的力量感染，脑袋越来越大
> 被恐惧之力感染的科学家，脑袋越长越大。
kilowog | 基洛沃格 | Kilowog | 绿灯军团教官 | vo:Michael Clarke Duncan | gl11 | #6A8A6A | 绿灯军团 | 口头禅:菜鸟！（Poozer！） | hal_r:学生
> 绿灯军团的魔鬼教官，最爱喊新人“菜鸟”。
tomar | 托马尔-雷 | Tomar-Re | 绿灯军团 | vo:Geoffrey Rush | gl11 | #8A6A3A | 绿灯军团
> 长着鸟嘴的绿灯侠，第一个迎接哈尔来到奥阿星的人。
catwoman_hb | 猫女 | Catwoman | 2004 版 · 哈莉·贝瑞 | Halle Berry | cw04 | #3A3A4A | 猫女 | 本名:佩欣丝·菲利普斯
> 2004 年的“猫女”，和赛琳娜·凯尔不是同一个人，是被埃及猫救活的设计师佩欣丝。
constantine | 约翰·康斯坦丁 | John Constantine | 地狱神探 | Keanu Reeves | const05 | #3A3A3A | 驱魔人 | 能力:能看见天使与恶魔的真身;习惯:一根接一根抽烟;往事:曾自杀过，下了一趟地狱 | angela:搭档;gabriel:对手;lucifer:想亲自来收他的人;chas:小司机
> 一根接一根抽烟的驱魔人，能看见混在人间的天使和恶魔。他死过一次，知道地狱长什么样。
angela | 安吉拉·多德森 | Angela Dodson | 女警探 | Rachel Weisz | const05 | #6A5A6A | 洛杉矶警局 | 能力:和双胞胎妹妹一样能看见灵异 | constantine:搭档
> 双胞胎妹妹离奇死亡后找上康斯坦丁的女警探。
gabriel | 加百列 | Gabriel | 大天使 | Tilda Swinton | const05 | #E0E0E0 | 天使 | constantine:看不起的人
> 雌雄莫辨的大天使加百列，蒂尔达·斯文顿的经典角色之一。
lucifer | 路西法 | Lucifer | 撒旦 | Peter Stormare | const05 | #E0E0E0 | 地狱之主 | 名场面:一身白西装、赤脚、满身黑油 | constantine:想亲自来收的人
> 穿着白西装、光着脚、脚上沾着黑油的撒旦，只在结尾出场几分钟，却让人过目不忘。
chas | 查斯 | Chas Kramer | 康斯坦丁的司机 | Shia LaBeouf | const05 | #6A6A5A | 康斯坦丁的跟班 | constantine:老板
> 一心想当康斯坦丁学徒的出租车司机。
midnite | 午夜爸爸 | Papa Midnite | 中立酒吧老板 | Djimon Hounsou | const05 | #4A3A3A | 中立者 | constantine:老熟人
> 天堂与地狱之间中立酒吧的老板。
"""

DECKS = """
bats | 历代蝙蝠侠 | All the Batmen | 🦇 | batman_w batman_v batman_c
jokers | 历代小丑 | All the Jokers | 🃏 | joker_r joker_n
cats | 历代猫女 | All the Catwomen | 🐈‍⬛ | catwoman_m catwoman_p catwoman_hb
supermen | 历代超人 | All the Supermen | 🔰 | superman_r superman_b superman_c superman_d
loises | 历代露易丝 | All the Loises | 📰 | lois_k lois_b lois_a lois
lexes | 历代卢瑟 | All the Lexes | 🧠 | lex_g lex_s lex_e lex_h
zods | 两代佐德 | Two Zods | ⛓ | zod_t zod
jorels | 两代乔-艾尔 | Two Jor-Els | 💎 | jorel_b jorel
robins | 两代罗宾 | Two Robins | 🐦 | robin_w robin_o
alfreds | 历代阿尔弗雷德 | All the Alfreds | 🎩 | alfred_g alfred_n alfred_p
supergirls | 历代超级少女 | All the Supergirls | 💫 | supergirl_s supergirl_f supergirl
bm66 | 1966 年的哥谭 | Batman '66 | 💥 | batman_w robin_w joker_r catwoman_m penguin_m riddler_g
burton | 蒂姆·伯顿的哥谭 | Burton's Gotham | 🦇 | batman_k vicki joker_n catwoman_p penguin_d shreck alfred_g
schumacher | 霓虹哥谭 | Schumacher's Gotham | 💡 | batman_v batman_c robin_o batgirl twoface_j riddler_c freeze ivy chase
donner | 唐纳的超人 | Donner's Superman | 🌾 | superman_r lois_k lex_g jorel_b jimmy_m perry_c otis
phantom | 幻影地带三人组 | The Phantom Zone | 🌀 | zod_t ursa non
gl2011 | 2011 绿灯军团 | Green Lantern (2011) | 💚 | hal_r sinestro_s kilowog tomar carol hammond
hellblazer | 地狱神探 | Constantine | 🚬 | constantine angela gabriel lucifer chas midnite
"""

COMIC = {"batman_w": 70, "batman_v": 70, "batman_c": 70, "robin_w": 561, "robin_o": 561, "joker_r": 370, "joker_n": 370,
         "catwoman_m": 165, "catwoman_p": 165, "penguin_m": 514, "penguin_d": 514, "riddler_g": 558, "riddler_c": 558,
         "twoface_j": 678, "ivy": 522, "batgirl": 63, "alfred_g": 17, "superman_r": 644, "superman_b": 644, "lex_g": 405,
         "lex_s": 405, "zod_t": 278, "supergirl_s": 643, "hal_r": 306, "sinestro_s": 601, "kilowog": 388, "constantine": 367}
FANDOM = {"freeze": "Victor Fries (Prime Earth)", "vicki": "Vicki Vale (Prime Earth)", "gordon_h": "James Gordon (Prime Earth)",
          "lois_k": "Lois Lane (Prime Earth)", "lois_b": "Lois Lane (Prime Earth)", "lois_a": "Lois Lane (Prime Earth)",
          "jimmy_m": "James Olsen (Prime Earth)", "perry_c": "Perry White (Prime Earth)", "jorel_b": "Jor-El (Prime Earth)",
          "ursa": "Ursa (New Earth)", "non": "Non (New Earth)", "carol": "Carol Ferris (Prime Earth)",
          "hammond": "Hector Hammond (Prime Earth)", "tomar": "Tomar-Re (New Earth)", "angela": "Angela Dodson (Constantine)",
          "chas": "Chas Chandler (New Earth)", "midnite": "Papa Midnite (New Earth)", "lucifer": "Lucifer Morningstar (New Earth)",
          "gabriel": "Gabriel (New Earth)", "catwoman_hb": "Patience Phillips (Catwoman)"}
