U = dict(id="xmen", n="X 战警宇宙", en="X-Men · Fox Universe", short="X-MEN",
         tag="变种人的二十多年：从泽维尔天赋青年学校，到金刚狼最后的公路、死侍打破第四面墙。",
         theme=["#E0A92E", "#2B4C9C", "#0E1530"], timeline=True,
         wd=["Q2006869", "Q28865116", "Q28865118", "Q18286530", "Q29559108"])
ORDER = 10

WORKS = """
## orig | 初代三部曲 | The Original Trilogy
xm1 | X-Men | 2000 | X战警 | tl=2000
x2 | X2: X-Men United | 2003 | X战警2 | tl=2001
x3 | X-Men: The Last Stand | 2006 | X战警3：背水一战 | tl=2002
## wolv | 金刚狼三部曲 | The Wolverine Trilogy
origins | X-Men Origins: Wolverine | 2009 | 金刚狼 | tl=1979
wolv2 | The Wolverine | 2013 | 金刚狼2 | tl=2003
logan | Logan | 2017 | 金刚狼3：殊死一战 | tl=2029
## prequel | 新三部曲 | The Prequel Saga
fc | X-Men: First Class | 2011 | X战警：第一战 | tl=1962
dofp | X-Men: Days of Future Past | 2014 | X战警：逆转未来 | tl=1973
apoc | X-Men: Apocalypse | 2016 | X战警：天启 | tl=1983
dp | X-Men: Dark Phoenix | 2019 | X战警：黑凤凰 | tl=1992
## dp | 死侍 | Deadpool
dp1 | Deadpool | 2016 | 死侍 | tl=2016
dp2 | Deadpool 2 | 2018 | 死侍2：我爱我家 | tl=2018
dw | Deadpool & Wolverine | 2024 | 死侍与金刚狼 | tl=2024
## else | 外传 | Spin-off
nm | The New Mutants | 2020 | 新变种人 | x tl=2019
"""

CHARS = """
# —— 初代 X 战警
xavier_s | X 教授 | Professor X | 斯图尔特版 · 查尔斯·泽维尔 | Patrick Stewart | xm1 x2 x3 origins wolv2 dofp logan | #3D5BA8 | X战警;泽维尔学校校长;Ω级变种人 | 真名:查尔斯·泽维尔;能力:心灵感应、读心、控心;装备:脑波强化仪 Cerebro;座右铭:人类与变种人可以共存 | magneto_m:挚友与宿敌;xavier_m:年轻时的自己;wolverine:最放心不下的学生;jean_j:最得意的学生;x23:晚年同行的孩子
> 世界上最强的心灵感应者，创立泽维尔天赋青年学校，收留无处可去的变种孩子。他一辈子都在赌人类和变种人能和平共处，哪怕对手是最懂他的老朋友。
magneto_m | 万磁王 | Magneto | 麦克莱恩版 · 埃里克·兰谢尔 | Ian McKellen | xm1 x2 x3 wolv2 dofp | #8A2A4A | 变种人兄弟会首领;集中营幸存者 | 真名:埃里克·兰谢尔;能力:操控磁场与一切金属;装备:屏蔽心灵感应的头盔;信念:变种人不该再躲 | xavier_s:挚友与宿敌;mystique_r:最忠诚的部下;pyro:看中的年轻人;magneto_f:年轻时的自己
> 从奥斯维辛活下来的少年，长大后成了能掀起整座桥的磁力之王。他不相信人类会接纳变种人，宁可先下手为强。和查尔斯下了一辈子的棋。
wolverine | 金刚狼 | Wolverine | 罗根 · 休·杰克曼 | Hugh Jackman | xm1 x2 x3 origins fc wolv2 dofp apoc logan dw | #D1A72E | X战警;武器X计划;独行侠 | 真名:詹姆斯·豪利特（罗根）;能力:超强自愈、不老、野兽般的嗅觉;骨骼:艾德曼合金;招牌:三根爪子、雪茄、皮夹克 | xavier_s:像父亲一样的人;jean_j:放不下的人;rogue:像妹妹一样;sabretooth_l:同父异母的哥哥;x23:血脉相连的女儿;deadpool:被迫组队的搭档;yukio:日本的保镖
> 活了一百多年的变种人，骨头里被灌进了艾德曼合金，记忆却被抹得七零八落。嘴上说自己不是英雄，可每次有人需要他，他都回来了。
storm_b | 暴风女 | Storm | 哈莉·贝瑞版 · 奥罗罗·门罗 | Halle Berry | xm1 x2 x3 dofp | #8E9BB8 | X战警;泽维尔学校老师 | 真名:奥罗罗·门罗;能力:呼风唤雨、操控闪电;出身:肯尼亚 | xavier_s:恩师;cyclops_m:并肩作战的队友;nightcrawler_c:护送过的新人
> 能召唤风暴和闪电的女人，泽维尔学校里最温柔也最坚定的老师。教授不在的时候，是她把 X 战警撑起来。
jean_j | 琴·葛蕾 | Jean Grey | 詹森版 · 凤凰之力 | Famke Janssen | xm1 x2 x3 wolv2 dofp | #C2443A | X战警;凤凰之力宿主;泽维尔学校医生 | 能力:心灵感应、念力;另一面:黑凤凰;职业:医生 | cyclops_m:恋人;wolverine:暧昧的心动;xavier_s:恩师;jean_t:年轻时的自己
> 学校的医生，心灵感应和念力都强得惊人。教授在她心里锁住了一股连她自己都不知道的力量——凤凰。
cyclops_m | 镭射眼 | Cyclops | 马斯登版 · 斯科特·萨默斯 | James Marsden | xm1 x2 x3 dofp | #2E5BB0 | X战警;外勤队长 | 真名:斯科特·萨默斯;能力:眼睛射出冲击光束;装备:红宝石石英眼镜 | jean_j:恋人;wolverine:情敌兼队友;xavier_s:恩师
> X 战警的外勤队长，一摘下眼镜就会轰出毁灭性的光束。规矩、可靠，就是和金刚狼怎么都不对付——毕竟他们喜欢同一个人。
rogue | 罗刹女 | Rogue | 玛丽 · 安娜·帕奎因 | Anna Paquin | xm1 x2 x3 dofp | #3E8A5A | X战警;泽维尔学校学生 | 本名:玛丽;能力:皮肤接触即吸走对方的能力与生命力;标志:额前一缕白发 | wolverine:最信任的人;iceman:男朋友;magneto_m:曾想利用她的人
> 第一次亲吻男孩就让对方昏迷了三周的女孩。碰不得任何人，只好戴着手套离家出走，直到在路边搭上了金刚狼的车。
iceman | 冰人 | Iceman | 鲍比·德雷克 | Shawn Ashmore | xm1 x2 x3 dofp | #7FB6D8 | X战警;泽维尔学校学生 | 真名:鲍比·德雷克;能力:冰冻、全身化为冰 | rogue:女朋友;pyro:曾经的好兄弟;kitty:亲近的朋友
> 能让手里的饮料瞬间结冰的阳光少年。和罗刹女谈着一场“碰不到”的恋爱，也和火人从朋友变成了对手。
mystique_r | 魔形女 | Mystique | 罗梅金版 · 瑞雯 | Rebecca Romijn | xm1 x2 x3 fc | #2F6A9A | 变种人兄弟会 | 本名:瑞雯·达克霍姆;能力:随意变成任何人的样子;肤色:蓝色鳞片 | magneto_m:效忠的人;mystique_l:年轻时的自己
> 蓝色皮肤、能变成任何人的头号特工。万磁王最忠实的左右手，潜伏、伪装、近身格斗样样顶尖。
sabretooth_t | 剑齿虎 | Sabretooth | 泰勒·梅恩版 | Tyler Mane | xm1 dw | #8A6A3A | 变种人兄弟会 | 能力:野兽般的力气与爪牙
> 万磁王手下的野兽型变种人，高大凶猛，在自由女神像上和金刚狼打得天昏地暗。
toad | 蟾蜍 | Toad | 莫蒂默·汤因比 | Ray Park; Evan Jonigkeit | xm1 dofp | #6A8A3A | 变种人兄弟会 | 能力:超强跳跃、长舌头、黏液
> 舌头能甩出好几米的兄弟会成员，身手灵活，嘴也很贫。
kelly | 凯利议员 | Senator Kelly | 反变种人议员 | Bruce Davison | xm1 x2 | #6A6A7A | 人类;政客 | 主张:《变种人登记法案》
> 力推变种人登记法案的参议员，煽动着人们对变种人的恐惧，直到他自己也尝到了变成“异类”的滋味。

# —— 《X战警2》
nightcrawler_c | 夜行者 | Nightcrawler | 卡明版 · 科特·瓦格纳 | Alan Cumming | x2 | #3A3F8A | X战警;马戏团出身;虔诚的教徒 | 真名:科特·瓦格纳;能力:瞬间移动（留下一阵硫磺烟）;特征:蓝皮肤、尾巴、三指 | storm_b:带他回学校的人;nightcrawler_k:年轻时的自己
> 蓝色皮肤、带着尾巴的德国马戏团明星，“嗖”的一声就能瞬移。外表像小恶魔，心里却是最虔诚温柔的人。
stryker_c | 威廉·史崔克 | William Stryker | 布莱恩·考克斯版 | Brian Cox | x2 | #5A4A3A | 人类;军方科学家 | 身份:上校;执念:消灭所有变种人
> 军方科学家，金刚狼失去的记忆里一直有他的影子。为了消灭变种人，连自己的儿子都能利用。
deathstrike | 死亡女士 | Lady Deathstrike | 尤里子 | Kelly Hu | x2 | #6A2A3A | 史崔克的部下 | 能力:自愈、艾德曼合金长指甲
> 史崔克手下的沉默杀手，十根指甲全是艾德曼合金。和金刚狼在实验室里打了一场“同类之战”。
pyro | 火人 | Pyro | 约翰·阿勒代斯 | Aaron Stanford | x2 x3 dw | #D0602E | 泽维尔学校学生→兄弟会 | 本名:约翰·阿勒代斯;能力:操控火焰（但自己生不了火）;标志:随身的打火机 | iceman:曾经的好兄弟;magneto_m:新的领路人
> 冰人的室友，手里总在“咔嗒咔嗒”地玩打火机。看不惯学校的温吞，最后跟着万磁王走了。
colossus_d | 钢力士 | Colossus | 初代 · 彼得·拉斯普廷 | Daniel Cudmore | x2 x3 dofp | #8A9AAE | X战警 | 本名:彼得·拉斯普廷;能力:全身化为有机钢
> 泽维尔学校里话不多的俄罗斯大个子，一变身就成了钢铁之躯。经典招式“快球特快”就是把金刚狼扔出去。
# —— 《X战警3》
kitty | 幻影猫 | Kitty Pryde | 凯蒂·普赖德 | Elliot Page | x3 dofp | #8A6AB5 | X战警 | 本名:凯瑟琳·普赖德;能力:穿墙、相位穿透;未来:能把意识送回过去 | iceman:亲近的朋友;wolverine:送回过去的人;juggernaut_v:智取的对手
> 能穿过墙壁的女孩。在背水一战里和红坦克玩了一场“你追不到我”，在未来战争里是把金刚狼送回 1973 年的关键。
beast_g | 野兽 | Beast | 格拉默版 · 汉克·麦考伊 | Kelsey Grammer | x3 dofp | #3E4FA8 | X战警;变种人事务部部长 | 本名:汉克·麦考伊;能力:超强体能与敏捷;另一面:天才科学家、文质彬彬 | beast_h:年轻时的自己;xavier_s:老同学
> 蓝色毛发的天才科学家，当上了总统内阁的变种人事务部长。看起来像野兽，说起话来却比谁都斯文。
juggernaut_v | 红坦克 | Juggernaut | 维尼·琼斯版 · 凯恩·马可 | Vinnie Jones | x3 | #9A3A2E | 变种人兄弟会 | 本名:凯恩·马可;能力:一旦冲起来就停不下来 | kitty:被她耍了一路
> 一旦开始冲锋就什么都挡不住的大块头，墙壁在他面前跟纸一样。
angel_f | 天使 | Angel | 本·福斯特版 · 沃伦 | Ben Foster | x3 | #C9B88A | 变种人 | 本名:沃伦·沃辛顿三世;能力:一对洁白巨大的羽翼;家世:制药大亨之子 | archangel:年轻时的自己
> 从小背着一对翅膀长大的富家少爷，父亲想用“解药”把他变回普通人，他选择飞走。
leech | 水蛭 | Leech | 吉米 | Cameron Bright | x3 | #7A8A9A | 变种人 | 能力:让身边的变种人失去能力
> 一个安静的小男孩，只要靠近他，变种人的能力就会消失——“解药”就是从他身上提取的。
callisto | 卡莉斯托 | Callisto | 莫洛克族首领 | Dania Ramirez | x3 | #6A4A5A | 变种人兄弟会 | 能力:超级速度、感知其他变种人
> 能感应到其他变种人位置的街头首领，带着自己的人投奔了万磁王。
multipleman | 多重人 | Multiple Man | 詹姆斯·马德罗 | Eric Dane | x3 | #6A7A6A | 变种人兄弟会 | 能力:无限分身
> 一个人能变成一支军队的变种人，是万磁王眼里的“好帮手”。
moira_w | 莫伊拉 | Moira MacTaggert | 初代 · 遗传学家 | Olivia Williams | x3 | #8A6A5A | 人类;科学家 | 职业:遗传学家 | moira_b:另一个时间线的她
> 教授的老朋友，研究变种人基因的科学家。

# —— 武器 X
sabretooth_l | 剑齿虎 | Sabretooth | 施瑞伯版 · 维克多·克里德 | Liev Schreiber | origins | #7A4A2E | 武器X计划 | 本名:维克多·克里德;能力:自愈、利爪、野性;身份:罗根同父异母的哥哥 | wolverine:相依为命又反目的弟弟;stryker_d:效命的人
> 罗根的亲哥哥，两人并肩打过美国内战、两次世界大战和越战。可越往后，他越享受杀戮。
stryker_d | 威廉·史崔克 | William Stryker | 丹尼·休斯顿版 · 武器 X 计划 | Danny Huston | origins | #5A4A3A | 人类;军方 | 职位:少校;计划:武器 X | wolverine:亲手打造的武器
> 年轻时的史崔克，组建了一支变种人特种部队，又启动了把艾德曼合金灌进罗根骨头的“武器 X”。
stryker_j | 威廉·史崔克 | William Stryker | 赫尔曼版 · 青年史崔克 | Josh Helman | dofp apoc | #5A4A3A | 人类;军方 | 时间:七八十年代
> 新时间线里的史崔克，七十年代还是个年轻军官，八十年代已经开始抓变种人做实验。
deadpool_o | 武器 XI 号 | Weapon XI | 被缝上嘴的韦德 | Ryan Reynolds; Scott Adkins | origins | #6A2A2E | 武器X计划 | 能力:瞬移、光束、利刃、自愈（拼凑来的）;状态:嘴被缝上了 | deadpool:后来的自己（他坚持不认）
> 话痨雇佣兵韦德被改造成“变种人杀手”，嘴还被缝上了。后来的死侍对这段经历的评价是：不算数。
agentzero | 零号特工 | Agent Zero | 大卫·诺斯 | Daniel Henney | origins | #4A5A6A | 武器X计划 | 能力:百发百中的神枪手
> 史崔克特种部队里的神枪手，冷酷、精准，后来奉命追杀罗根。
wraith | 幽影 | Wraith | 约翰·雷斯 | will.i.am | origins | #6A6A8A | 武器X计划 | 能力:瞬间移动
> 特种部队的瞬移专家，退役后开了家拳击馆。
blob | 肥油 | The Blob | 弗雷德·杜克斯 | Kevin Durand | origins | #8A7A5A | 武器X计划 | 能力:刀枪不入的身躯
> 当年身手矫健的士兵，退役后胖成了一座山，变成了金刚狼的拳击沙袋。
bolt | 布拉德利 | Bolt | 克里斯·布拉德利 | Dominic Monaghan | origins | #6A7A9A | 武器X计划 | 能力:操控电力
> 小队里最温和的人，能控制一切带电的东西，离开队伍后躲进了马戏团。
gambit_k | 牌皇 | Gambit | 基奇版 · 雷米·勒博 | Taylor Kitsch | origins | #7A3A6A | 新奥尔良 | 本名:雷米·勒博;能力:给物体注入动能、扑克牌一扔就炸;武器:长棍 | wolverine:不打不相识
> 新奥尔良的赌徒兼小偷，手里的扑克牌一扔就爆炸。从史崔克的岛上逃出来的人，知道去哪儿找他。
kayla | 银狐 | Silver Fox | 凯拉·席尔维福克斯 | Lynn Collins | origins | #A0A8B4 | 变种人 | 能力:触摸催眠 | wolverine:加拿大山林里的恋人;emma_t:妹妹
> 罗根在加拿大山林里的恋人，给他讲了一个关于狼和月亮的故事，“金刚狼”这个名字由此而来。
emma_t | 艾玛 | Emma | 银狐的妹妹 | Tahyna Tozzi | origins | #C4CCDA | 变种人 | 能力:皮肤化为钻石 | kayla:姐姐
> 被史崔克关在岛上的女孩，能把皮肤变成钻石——很多人相信她就是年轻时的白皇后。
cyclops_t | 少年斯科特 | Young Cyclops | 被关在岛上的少年 | Tim Pocock | origins | #2E5BB0 | 变种人 | 能力:眼睛射出光束（还控制不住）
> 史崔克从高中抓走的少年，还没学会控制自己的眼睛。

# —— 金刚狼2（日本）
yukio | 雪绪 | Yukio | 罗根的日本保镖 | Rila Fukushima | wolv2 | #C23A5A | 变种人 | 能力:预见死亡;武器:武士刀 | wolverine:她叫他“保镖大人”;mariko:义姐妹
> 红发的日本少女，能看见别人死去的样子，也是一名武士刀高手。一路陪罗根在东京和长崎厮杀。
mariko | 真理子 | Mariko | 矢志田家的继承人 | Tao Okamoto | wolv2 | #8A6A7A | 人类;矢志田家族 | 身份:矢志田集团继承人 | wolverine:心意相通的人;yashida:祖父;shingen:父亲;yukio:义姐妹
> 矢志田家的孙女，表面上是被安排好婚事的大小姐，骨子里有着武士家族的刚强。
yashida | 矢志田 | Ichirō Yashida | 银武士 | Haruhiko Yamanouchi; Ken Yamamura | wolv2 | #9AA0AA | 人类;矢志田集团 | 往事:长崎原子弹那天被罗根救下;另一面:银武士 | wolverine:救命恩人;mariko:孙女
> 1945 年在长崎被罗根救下的日本军官，后来成了科技巨头。临终前，他请罗根来日本“道个别”。
viper | 蝰蛇 | Viper | 绿衣女医生 | Svetlana Khodchenkova | wolv2 | #4E8A3A | 变种人 | 能力:对一切毒素免疫，能制毒;特征:会蜕皮
> 自称医生的变种人，舌尖带毒，一次次换皮重生。
shingen | 矢志田信玄 | Shingen | 真理子的父亲 | Hiroyuki Sanada | wolv2 | #4A4A5A | 人类;矢志田家族 | 武器:武士刀 | mariko:女儿
> 真理子的父亲，冷硬的剑道高手，和罗根有一场武士刀对爪子的对决。
harada | 原田健一郎 | Harada | 黑衣忍者 | Will Yun Lee | wolv2 | #3A3A4A | 人类;忍者 | 武器:弓箭 | mariko:青梅竹马
> 一直暗中守护真理子的忍者首领，弓术出神入化。

# —— 金刚狼3
x23 | X-23 | X-23 | 劳拉 | Dafne Keen | logan dw | #5A5A6A | 变种人;X-23 实验体 | 本名:劳拉;能力:自愈、手脚各有艾德曼合金爪;性格:不爱说话、一出手就很凶 | wolverine:基因上的父亲;xavier_s:一路照顾她的爷爷
> 用金刚狼基因造出来的小女孩，手上两根爪、脚上一根爪。不怎么说话，一开打比谁都狠。
caliban | 卡利班 | Caliban | 追踪变种人的白化病人 | Stephen Merchant; Tómas Lemarquis | logan apoc | #C8C8C0 | 变种人 | 能力:感知并追踪变种人;弱点:怕阳光 | wolverine:同住的伙伴;xavier_s:照顾的病人
> 皮肤怕晒的变种人，能“闻到”别的变种人在哪儿。晚年和罗根一起照顾生病的查尔斯。
pierce | 唐纳德·皮尔斯 | Donald Pierce | 掠夺者首领 | Boyd Holbrook | logan | #6A6A5A | 人类;改造人;掠夺者 | 特征:机械手臂
> 带着机械手臂的雇佣兵头子，一路追捕劳拉和逃出来的孩子们。
rice | 赞德·莱斯 | Dr. Zander Rice | X-23 计划主持人 | Richard E. Grant | logan | #5A5A6A | 人类;科学家 | 计划:用变种人基因制造“孩子兵器”
> 用变种人基因造孩子当武器的科学家，冷静得可怕。
x24 | X-24 | X-24 | 没有灵魂的金刚狼 | Hugh Jackman | logan | #4A4A4A | 克隆体 | 来历:金刚狼的完美复制品;特征:只会杀戮 | wolverine:自己的复制品
> 用罗根基因培养的克隆体，年轻、强壮，却没有任何人性。是罗根最可怕的对手：另一个自己。

# —— 新三部曲（第一战）
xavier_m | 查尔斯 | Professor X | 麦卡沃伊版 · 年轻的泽维尔 | James McAvoy | fc dofp apoc dp | #4F6FC0 | X战警;泽维尔学校创办人 | 真名:查尔斯·泽维尔;能力:心灵感应;年轻时:牛津大学遗传学博士、爱搭讪 | magneto_f:挚友与宿敌;mystique_l:从小一起长大的妹妹;beast_h:最早的学生;moira_b:错过的人;xavier_s:老了以后的自己
> 年轻的查尔斯还没坐上轮椅，还会在酒吧用“变异”当搭讪话题。他第一次遇见埃里克，是在冰冷的海里把他拉了上来。
magneto_f | 万磁王 | Magneto | 法斯宾德版 · 年轻的埃里克 | Michael Fassbender | fc dofp apoc dp | #9A2A4A | 变种人兄弟会;复仇者 | 真名:埃里克·兰谢尔;能力:操控磁场;往事:追杀纳粹;招牌:那顶头盔 | xavier_m:挚友与宿敌;mystique_l:懂他的人;quicksilver:儿子;shaw:不共戴天的仇人;magneto_m:老了以后的自己
> 年轻的埃里克带着一枚硬币满世界追杀当年的纳粹医生。他和查尔斯之间，是这个系列最动人也最心碎的友情。
mystique_l | 魔形女 | Mystique | 劳伦斯版 · 瑞雯 | Jennifer Lawrence | fc dofp apoc dp | #3478B8 | 变种人;后来的 X 战警 | 本名:瑞雯·达克霍姆;能力:变形;口号:变种人且骄傲 | xavier_m:从小一起长大的“哥哥”;magneto_f:懂她的人;beast_h:恋人;mystique_r:未来的自己
> 小时候闯进泽维尔家厨房的蓝皮肤女孩，被查尔斯当成妹妹带大。她花了很长时间才敢以真面目示人。
beast_h | 野兽 | Beast | 霍尔特版 · 年轻的汉克 | Nicholas Hoult | fc dofp apoc dp | #3E4FA8 | X战警 | 本名:汉克·麦考伊;能力:抓握力超强的脚、后来全身变成蓝毛野兽;发明:黑鸟号、早期 Cerebro | mystique_l:恋人;xavier_m:挚友与校长;beast_g:老了以后的自己
> 中情局实验室里的天才少年，为了“治好”自己的大脚研究血清，结果变成了一身蓝毛。X 战警的喷气机和 Cerebro 都是他造的。
havok | 冲击波 | Havok | 亚历克斯·萨默斯 | Lucas Till | fc dofp apoc | #C7802E | X战警 | 本名:亚历克斯·萨默斯;能力:从身体放出环形能量冲击;家人:镭射眼的哥哥 | cyclops_s:弟弟;banshee:第一批同学
> 一放能量就会炸开一圈红光的年轻人，第一批 X 战警。他还有个后来也很有名的弟弟——斯科特。
banshee | 海妖 | Banshee | 肖恩·卡西迪 | Caleb Landry Jones | fc | #C9A04A | X战警 | 本名:肖恩·卡西迪;能力:超声波尖叫，还能借声波飞行 | havok:第一批同学
> 一开嗓就能震碎玻璃的红发少年，第一次“试飞”是从窗户里跳出去的。
darwin | 达尔文 | Darwin | 阿尔芒·穆尼奥斯 | Edi Gathegi | fc | #7A6A4A | X战警 | 能力:身体能为了活下去瞬间进化
> 能让身体随环境进化的出租车司机，第一批被招募的变种人之一。
angel_s | 天使 | Angel Salvadore | 萨尔瓦多 | Zoë Kravitz | fc | #8A5AA0 | 变种人→地狱火俱乐部 | 能力:蜻蜓翅膀、喷吐酸液
> 在脱衣舞俱乐部被查尔斯找到的女孩，背上有一对蜻蜓的翅膀。她最后选了另一边。
shaw | 塞巴斯蒂安·肖 | Sebastian Shaw | 地狱火俱乐部 | Kevin Bacon | fc | #6A5A3A | 地狱火俱乐部 | 能力:吸收能量再释放;往事:二战时的纳粹医生“施密特” | magneto_f:不共戴天的仇人;emma_j:左右手
> 二战时在集中营里逼埃里克觉醒能力的“施密特医生”。如今他操纵美苏两国，想用一场核战争让变种人统治世界。
emma_j | 白皇后 | Emma Frost | 艾玛·弗罗斯特 | January Jones | fc | #D8DDE8 | 地狱火俱乐部 | 能力:心灵感应、钻石之躯;标志:一身白 | shaw:效力的人
> 一身白衣的心灵感应者，能把身体变成钻石。肖身边最冷艳的一张牌。
azazel | 阿扎赛尔 | Azazel | 红皮肤的瞬移者 | Jason Flemyng | fc | #A02A2A | 地狱火俱乐部 | 能力:瞬间移动;特征:红皮肤、尾巴 | mystique_l:后来的漫画里，他们有个孩子
> 红皮肤、带尾巴的瞬移变种人，长得像传说里的恶魔。
riptide | 激流 | Riptide | 雅诺什·奎斯特 | Álex González | fc | #4A7A8A | 地狱火俱乐部 | 能力:制造龙卷风
> 一言不发的地狱火俱乐部成员，手一转就是一阵旋风。
moira_b | 莫伊拉 | Moira MacTaggert | 中情局特工 | Rose Byrne | fc apoc | #8A6A5A | 人类;中情局 | 职业:中情局探员 | xavier_m:心动又被抹去记忆的人;moira_w:另一个时间线的她
> 第一个把查尔斯带进中情局的特工。她和查尔斯之间有过心动，后来却被查尔斯亲手抹去了记忆。

# —— 逆转未来
quicksilver | 快银 | Quicksilver | 彼得·马克西莫夫 | Evan Peters | dofp apoc dp | #A8B4C4 | X战警 | 本名:彼得·马克西莫夫;能力:超音速奔跑;最爱:随身听、偷东西、打乒乓 | magneto_f:不敢相认的父亲;xavier_m:常被他救场的校长
> 跑得比子弹还快的少年。在五角大楼厨房里配着《Time in a Bottle》的那段慢动作，让无数人爱上了他。
trask | 玻利瓦尔·特拉斯克 | Bolivar Trask | 哨兵计划之父 | Peter Dinklage | dofp | #5A5A4A | 人类;特拉斯克工业 | 发明:哨兵机器人 | mystique_l:想刺杀他的人
> 发明哨兵机器人的科学家。他相信变种人是人类共同的敌人，正是他的研究让未来变成了地狱。
sentinel | 哨兵 | Sentinel | 能适应一切能力的机器人 | - | dofp | #4A4A5A | 机器人 | 来源:用魔形女的基因研发;能力:适应并克制任何变种能力
> 为猎杀变种人而造的巨型机器人。到了未来，它们能模仿任何能力，把世界变成了变种人的墓地。
bishop | 主教 | Bishop | 卢卡斯·毕肖普 | Omar Sy | dofp | #5A4A6A | X战警（未来） | 能力:吸收能量再射出
> 未来抵抗军的一员，能吸收哨兵的攻击再打回去。
blink | 闪烁 | Blink | 克拉丽斯·弗格森 | Fan Bingbing | dofp | #9A5AB0 | X战警（未来） | 能力:打开传送门 | sunspot:并肩战斗的队友
> 能凭空打开紫色传送门的女孩，未来战场上最灵活的一位。
sunspot | 太阳黑子 | Sunspot | 罗伯托·达·科斯塔 | Adan Canto | dofp | #D07A2E | X战警（未来） | 能力:吸收太阳能量，全身燃烧
> 能把自己变成一团太阳火焰的抵抗军战士。
warpath | 战迹 | Warpath | 詹姆斯·普劳德斯塔 | Booboo Stewart | dofp | #8A5A3A | X战警（未来） | 能力:超强感官与力量
> 能远远嗅到哨兵来袭的抵抗军战士。

# —— 天启
apocalypse | 天启 | Apocalypse | 恩·沙巴·努尔 | Oscar Isaac | apoc | #3A4A8A | 第一个变种人;古埃及的“神” | 能力:能把别人的能力据为己有;习惯:每次都召集四骑士 | magneto_f:选中的骑士;storm_s:选中的骑士;psylocke:选中的骑士;archangel:选中的骑士
> 世界上第一个变种人，在古埃及被奉为神明。沉睡了几千年后醒来，他看不惯这个“软弱”的世界，要推倒重来。
storm_s | 暴风女 | Storm | 希普版 · 少女奥罗罗 | Alexandra Shipp | apoc dp | #9AA6C4 | 天启四骑士→X战警 | 真名:奥罗罗·门罗;能力:呼风唤雨;少年时:开罗街头的小扒手 | apocalypse:选中她的人;mystique_l:她心里的英雄;storm_b:长大后的自己
> 开罗街头的小偷，崇拜着传说中的魔形女。被天启选中当了骑士，最后站到了 X 战警这边。
jean_t | 琴·葛蕾 | Jean Grey | 特纳版 · 少女琴 | Sophie Turner | apoc dp | #C23A3A | X战警;凤凰之力宿主 | 能力:心灵感应、念力;另一面:黑凤凰 | cyclops_s:恋人;xavier_m:恩师;jean_j:长大后的自己
> 总做噩梦的少女琴，力量大得连教授都害怕。在太空救援中，她吸收了一股宇宙能量——凤凰。
cyclops_s | 镭射眼 | Cyclops | 谢里丹版 · 少年斯科特 | Tye Sheridan | apoc dp | #2E5BB0 | X战警 | 能力:眼睛射出光束 | jean_t:恋人;havok:哥哥;nightcrawler_k:好兄弟;cyclops_m:长大后的自己
> 刚觉醒能力的少年斯科特，被哥哥送进泽维尔学校。和琴、科特、朱比丽一起翻墙去看《星战》。
nightcrawler_k | 夜行者 | Nightcrawler | 斯密特-麦菲版 · 少年科特 | Kodi Smit-McPhee | apoc dp | #3A3F8A | X战警 | 能力:瞬间移动 | cyclops_s:好兄弟;mystique_l:救他出来的人;nightcrawler_c:长大后的自己
> 被抓去地下格斗场的德国少年，害羞又善良，是新一代 X 战警里的开心果。
psylocke | 灵蝶 | Psylocke | 贝特西·布雷多克 | Olivia Munn | apoc | #7A3AA0 | 天启四骑士 | 能力:念力化成的紫色光刃;武器:能量长鞭 | apocalypse:效忠的人
> 能把念力凝成紫色光刃的女战士，被天启招为骑士之一。
archangel | 大天使 | Archangel | 汉迪版 · 沃伦 | Ben Hardy | apoc | #6A7A9A | 天启四骑士 | 本名:沃伦·沃辛顿三世;能力:钢铁之翼 | apocalypse:给了他新翅膀的人;angel_f:另一个时间线的自己
> 在地下格斗场折了翅膀的少年，被天启换上了一对金属羽翼。
jubilee | 朱比丽 | Jubilee | 李欢腾 | Lana Condor | apoc | #D0B03A | X战警（学生） | 能力:手上放出彩色火花 | cyclops_s:同学
> 爱逛商场、戴墨镜的学生，能放出烟花一样的能量火花。

# —— 黑凤凰
vuk | 维克 | Vuk | 外星族群“迪巴里”的首领 | Jessica Chastain | dp | #C8CCD4 | 外星人 | 目的:夺取凤凰之力
> 失去家园的外星人首领，盯上了琴体内的凤凰之力。

# —— 死侍
deadpool | 死侍 | Deadpool | 韦德·威尔逊 | Ryan Reynolds | dp1 dp2 dw | #B8232E | 雇佣兵;X战警见习生（自称） | 真名:韦德·威尔逊;能力:超强自愈;武器:双刀、双枪;特长:打破第四面墙、嘴贱 | vanessa:一生挚爱;wolverine:最想合作的人;colossus:想拉他进 X 战警的大哥;weasel:最好的朋友;blindal:室友;cable:不打不相识
> 为了治癌症接受改造，换来了不死之身和一张“牛油果脸”。贱、吵、会跟观众聊天——但他其实只想保护自己在乎的人。
vanessa | 凡妮莎 | Vanessa | 韦德的女朋友 | Morena Baccarin | dp1 dp2 dw | #B84A6A | 人类 | 职业:陪酒女;爱好:和韦德一起过所有节日 | deadpool:一生挚爱
> 韦德在酒吧遇见的另一个“怪人”。两人从一场比惨开始，过完了一整年的每一个节日。
weasel | 黄鼠狼 | Weasel | 酒保 | T.J. Miller | dp1 dp2 | #8A7A5A | 人类 | 职业:雇佣兵酒吧的酒保 | deadpool:最好的朋友
> 雇佣兵酒吧的酒保，韦德的损友，什么赌局都敢开。
blindal | 盲眼阿尔 | Blind Al | 韦德的室友 | Leslie Uggams | dp1 dp2 dw | #9A8A7A | 人类 | 爱好:组装宜家家具、和韦德互怼 | deadpool:室友
> 一位双目失明的老太太，是韦德的室友。嘴比韦德还毒，两人吵吵闹闹过日子。
dopinder | 杜宾达 | Dopinder | 出租车司机 | Karan Soni | dp1 dp2 dw | #C9803A | 人类 | 职业:出租车司机;梦想:当一名杀手 | deadpool:最爱的乘客
> 被韦德拉上车的印度裔司机，听完韦德的故事后，一心想当个“狠人”。
negasonic | 黑面少女弹头 | Negasonic Teenage Warhead | 埃莉 | Brianna Hildebrand | dp1 dp2 dw | #3A3A4A | X战警（见习） | 能力:全身爆发出核能冲击;性格:冷淡、不爱理人 | colossus:带她的导师;yukio_k:女朋友
> X 战警的见习生，脸比天还臭，一爆发就是一枚“人肉炸弹”。
colossus | 钢力士 | Colossus | 死侍版 · 彼得 | Stefan Kapičić; Andre Tricoteux | dp1 dp2 dw | #8A9AAE | X战警 | 能力:全身化为有机钢;性格:讲礼貌、热心、念叨规矩 | deadpool:想劝他从良;negasonic:带的见习生
> 一身钢铁的俄罗斯大个子，一直想把死侍劝进 X 战警，满嘴“英雄之道”。
ajax | 阿贾克斯 | Ajax | 弗朗西斯 | Ed Skrein | dp1 | #5A5A6A | 改造人 | 能力:感觉不到痛;弱点:真名叫“弗朗西斯” | deadpool:把他毁容的仇人
> 把韦德改造成死侍、又毁了他脸的人。他唯一的弱点是：被人喊真名。
angeldust | 天使尘 | Angel Dust | 克里斯蒂娜 | Gina Carano | dp1 | #6A4A5A | 改造人 | 能力:肾上腺素爆发后的怪力
> 阿贾克斯的帮手，一激动就力大无穷。
cable | 电索 | Cable | 来自未来的士兵 | Josh Brolin | dp2 | #7A8A9A | 时间旅行者 | 本名:内森·萨默斯;能力:念力、半机械身体;装备:巨型枪械、时间跳跃装置 | deadpool:不打不相识;firefist:追杀又放下的孩子
> 从未来穿越回来的独臂士兵，为了阻止一个改变他家庭命运的悲剧，要追杀一个孩子。
domino | 多米诺 | Domino | 运气就是能力 | Zazie Beetz | dp2 | #3A3A3A | X特攻队 | 本名:妮娜·瑟曼;能力:超强好运 | deadpool:吵着不信她的能力
> 自称“能力是运气好”的女人，被死侍嘲笑“这不算超能力”，然后一个人走完了全场最顺的一段路。
firefist | 火拳 | Firefist | 罗素 | Julian Dennison | dp2 | #D0602E | 变种人 | 本名:罗素·柯林斯;能力:双手喷火 | deadpool:想救下的孩子;cable:要追杀他的人
> 在变种人“矫正学校”受尽欺负的少年，愤怒的时候拳头会着火。
yukio_k | 雪绪 | Yukio | 死侍版 · 欢乐少女 | Shioli Kutsuna | dp2 dw | #D06A8A | X战警（见习） | 能力:操控电能;口头禅:Hi，Wade！ | negasonic:女朋友;deadpool:每次都开心打招呼
> 弹头的女朋友，永远元气满满地跟韦德打招呼，能用电光把敌人掀飞。
peter | 彼得 | Peter | 普通大叔 | Rob Delaney | dp2 dw | #8A8A7A | 人类;X特攻队 | 能力:没有;特长:看了招聘广告就来了 | deadpool:真心的好朋友
> 毫无超能力、只是看到广告就来应聘的普通大叔。后来成了韦德最真心的朋友之一。
blacktom | 黑汤姆 | Black Tom Cassidy | 冰盒监狱的狱友 | Jack Kesy | dp2 | #3A4A3A | 变种人 | 能力:操控植物
> 冰盒监狱里的狠角色，最后和红坦克一起越狱。
shatterstar | 破星 | Shatterstar | 外星人 | Lewis Tan | dp2 | #C9A0A0 | X特攻队 | 来历:莫约世界;自称:比人类更优越
> 号称来自外星的战士，比人类“更强”。他在 X 特攻队的首次任务里有一个非常难忘的结局。
bedlam | 狂人 | Bedlam | 杰西·艾肯 | Terry Crews | dp2 | #4A5A7A | X特攻队 | 能力:干扰电子设备
> 能让电器失灵的大块头，X 特攻队的首批成员。
zeitgeist | 时代精神 | Zeitgeist | 阿克塞尔 | Bill Skarsgård | dp2 | #6A8A3A | X特攻队 | 能力:吐酸液
> 能从嘴里喷强酸的队员，跳伞那天运气不太好。
vanisher | 隐形人 | Vanisher | 一直看不见的队员 | Brad Pitt | dp2 | #B8BCC4 | X特攻队 | 能力:隐身;趣事:真面目只出现了不到一秒
> X 特攻队里一直“在场但看不见”的成员。他的真面目，只闪现了一秒钟。
juggernaut_d | 红坦克 | Juggernaut | 死侍版 · 凯恩·马可 | Ryan Reynolds; Aaron W. Reed | dp2 dw | #9A3A2E | 变种人 | 能力:无法阻挡;特色:整个人都是 CGI
> 冰盒监狱里被锁着的巨人，一被放出来就把所有人吓坏了。
cassandra | 卡珊德拉·诺娃 | Cassandra Nova | X 教授的双胞胎妹妹 | Emma Corrin | dw | #5A4A6A | 虚空统治者 | 能力:心灵感应、把手伸进别人的脑袋;住处:虚空 | xavier_s:她从没被承认的哥哥
> 被丢进虚空的 X 教授双胞胎妹妹，一样秃头、一样心灵感应，却把力量用来统治被时间遗弃的地方。
paradox | 帕拉多克斯 | Mr. Paradox | 时间管理局探员 | Matthew Macfadyen | dw | #6A6A7A | 时间变异管理局 | 职位:中层管理
> 时间变异管理局的中层官员，打算用一台“时间剥离机”把死侍的宇宙删掉。
dogpool | 狗侍 | Dogpool | 死侍的狗狗变体 | - | dw | #C9803A | 死侍军团 | 特征:一身死侍制服、伸着舌头;真名:佩吉 | deadpool:另一个宇宙的自己
> 虚空里的狗狗版死侍，穿着小号战衣，舌头总是吐在外面。
gambit_c | 牌皇 | Gambit | 塔图姆版 · 被遗忘的那一个 | Channing Tatum | dw | #7A3A6A | 虚空抵抗军 | 能力:扑克牌爆炸;口音:浓得听不懂的新奥尔良腔 | x23:并肩作战;elektra:并肩作战
> 那部一直没拍成的《牌皇》电影的主角，终于在虚空里登场了，一口口音谁都听不懂。
elektra | 艾丽卡 | Elektra | 来自 2003 年的刺客 | Jennifer Garner | dw | #A3263A | 虚空抵抗军 | 武器:一对“筷子”般的短剑
> 来自老福克斯宇宙的女刺客，被时间遗忘之后在虚空里活了下来。
blade | 刀锋战士 | Blade | 吸血鬼猎人 | Wesley Snipes | dw | #2E2E2E | 虚空抵抗军 | 身份:日行者，半人半吸血鬼;武器:长刀
> 九十年代最酷的吸血鬼猎人，一身黑色皮衣，在虚空里继续拔刀。
johnny_e | 霹雳火 | Human Torch | 克里斯·埃文斯版 | Chris Evans | dw | #D5632B | 神奇四侠（福克斯版） | 能力:全身起火飞行;口头禅:烈火燃烧！ | deadpool:被他调侃
> 大家都以为他会以美国队长的身份出现……结果是福克斯版的霹雳火。
alioth | 阿利奥斯 | Alioth | 吞噬一切的虚空巨兽 | - | dw | #6A3A8A | 虚空 | 特征:烟雾般的巨兽，吞掉被遗弃的世界
> 盘踞在虚空里的巨大怪物，吞噬一切被时间遗弃的东西。
ladypool | 女侍 | Ladypool | 死侍军团 | Blake Lively | dw | #C23A5A | 死侍军团 | 特征:女版死侍
> 死侍军团里飒爽的女版死侍。
cavillrine | 卡维尔狼 | Cavillrine | 某个宇宙的金刚狼 | Henry Cavill | dw | #D1A72E | 金刚狼变体 | 彩蛋:演员是亨利·卡维尔
> 一个“特别帅”的金刚狼变体，只出现了几秒，全场尖叫。

# —— 新变种人
dani | 达妮·月星 | Danielle Moonstar | 幻影 | Blu Hunt | nm | #6A5AA0 | 新变种人 | 能力:把别人最深的恐惧变成现实 | rahne:彼此依靠的人;magik:针锋相对
> 一夜之间失去家园的夏延族女孩，被送进一座神秘的“医院”。她的能力，会把每个人心底的恐惧放出来。
magik | 魔法师 | Magik | 伊莉安娜·拉斯普廷 | Anya Taylor-Joy | nm | #C8B07A | 新变种人 | 能力:传送、召唤灵魂剑;伙伴:小紫龙 Lockheed;家人:钢力士的妹妹 | dani:针锋相对
> 嘴毒又孤傲的俄罗斯少女，手里能变出一把灵魂剑，肩上还常趴着一只小紫龙。
rahne | 狼毒 | Wolfsbane | 拉妮·辛克莱 | Maisie Williams | nm | #8A6A3A | 新变种人 | 能力:变身为狼 | dani:彼此依靠的人
> 能变成狼的苏格兰女孩，被严苛的信仰教得以自己为耻。
cannonball | 炮弹 | Cannonball | 山姆·格思里 | Charlie Heaton | nm | #C9803A | 新变种人 | 能力:像炮弹一样飞冲，冲击时刀枪不入
> 来自肯塔基矿区的男孩，一启动就像炮弹一样射出去。
sunspot_z | 太阳黑子 | Sunspot | 新变种人版 · 罗伯托 | Henry Zaga | nm | #D07A2E | 新变种人 | 能力:吸收太阳能量
> 巴西富家子弟，一点燃就停不下来。
reyes | 塞西莉亚·雷耶斯 | Dr. Cecilia Reyes | 医院的医生 | Alice Braga | nm | #6A7A8A | 变种人;埃塞克斯公司 | 能力:身体周围的力场
> 看管孩子们的医生，温和的笑容下藏着秘密。
"""

DECKS = """
og | 初代 X 战警 | The Original X-Men | ✖ | xavier_s wolverine storm_b jean_j cyclops_m rogue iceman
brotherhood | 变种人兄弟会 | Brotherhood of Mutants | 🧲 | magneto_m mystique_r sabretooth_t toad pyro juggernaut_v
firstclass | 第一战 | First Class | 🎓 | xavier_m magneto_f mystique_l beast_h havok banshee darwin angel_s
hellfire | 地狱火俱乐部 | Hellfire Club | 🔥 | shaw emma_j azazel riptide angel_s
weaponx | 武器 X 计划 | Team X | 🧪 | wolverine sabretooth_l stryker_d agentzero wraith blob bolt
horsemen | 天启四骑士 | Four Horsemen | 🐎 | apocalypse magneto_f storm_s psylocke archangel
newgen | 新一代 X 战警 | The New Class | ⭐ | jean_t cyclops_s nightcrawler_k storm_s quicksilver jubilee
future | 未来抵抗军 | Days of Future Past | ⏳ | xavier_s magneto_m wolverine kitty iceman colossus_d bishop blink sunspot warpath
pair_x | 两代 X 教授 | Two Charles | 🧠 | xavier_s xavier_m
pair_m | 两代万磁王 | Two Eriks | 🧲 | magneto_m magneto_f
pair_r | 两代魔形女 | Two Ravens | 💙 | mystique_r mystique_l
pair_j | 两代琴·葛蕾 | Two Jeans | 🔥 | jean_j jean_t
pair_c | 两代镭射眼 | Two Scotts | 🕶 | cyclops_m cyclops_s
pair_b | 两代野兽 | Two Hanks | 🐾 | beast_g beast_h
pair_s | 两代暴风女 | Two Ororos | ⚡ | storm_b storm_s
pair_n | 两代夜行者 | Two Kurts | 💨 | nightcrawler_c nightcrawler_k
strykers | 三代史崔克 | Three Strykers | 🎖 | stryker_c stryker_d stryker_j
japan | 金刚狼在日本 | The Wolverine | 🗾 | wolverine yukio mariko yashida shingen harada viper
logan | 最后的公路 | Logan | 🛻 | wolverine x23 xavier_s caliban
dpfam | 死侍的家人们 | Deadpool's Family | 🍕 | deadpool vanessa weasel blindal dopinder colossus negasonic yukio_k peter
xforce | X 特攻队 | X-Force | 🪂 | deadpool domino bedlam shatterstar zeitgeist vanisher peter
dpvillain | 死侍的冤家 | Deadpool's Rivals | 💀 | ajax angeldust cable juggernaut_d blacktom cassandra paradox
foxgems | 福克斯遗珠 | Fox Legends | 🎞 | gambit_c elektra blade johnny_e x23 pyro sabretooth_t
dpcorps | 死侍军团 | Deadpool Corps | 🦄 | deadpool dogpool ladypool deadpool_o
newmutants | 新变种人 | The New Mutants | 🌙 | dani magik rahne cannonball sunspot_z
villains | 变种人的敌人 | Enemies of Mutantkind | ⚔ | stryker_c trask sentinel rice pierce vuk
"""

COMIC = {"xavier_s": 527, "xavier_m": 527, "magneto_m": 423, "magneto_f": 423, "wolverine": 717, "cavillrine": 717,
         "storm_b": 638, "storm_s": 638, "jean_j": 517, "jean_t": 356, "cyclops_m": 196, "cyclops_s": 196, "cyclops_t": 196,
         "rogue": 567, "iceman": 339, "mystique_r": 480, "mystique_l": 480, "sabretooth_t": 570, "sabretooth_l": 570,
         "toad": 670, "pyro": 532, "colossus_d": 185, "colossus": 185, "kitty": 586, "nightcrawler_c": 490, "nightcrawler_k": 490,
         "juggernaut_v": 374, "juggernaut_d": 374, "angel_f": 24, "archangel": 40, "deathstrike": 400, "gambit_k": 274, "gambit_c": 274,
         "deadpool": 213, "deadpool_o": 213, "emma_j": 241, "emma_t": 241, "banshee": 61, "havok": 311, "azazel": 57, "shaw": 582,
         "quicksilver": 536, "bishop": 92, "blink": 115, "sunspot": 640, "sunspot_z": 640, "warpath": 707, "apocalypse": 35,
         "psylocke": 529, "jubilee": 372, "cable": 145, "domino": 227, "negasonic": 488, "multipleman": 478, "x23": 723,
         "rahne": 716, "cannonball": 148, "vanisher": 685, "shatterstar": 588, "blob": 119, "agentzero": 11, "callisto": 146,
         "beast_g": 75, "beast_h": 75, "angel_s": 26, "elektra": 238, "blade": 112, "johnny_e": 333}
FANDOM = {"wraith": "John Wraith (Earth-616)", "bolt": "Christopher Bradley (Earth-616)", "kayla": "Kayla Silverfox (Earth-616)",
          "yukio": "Yukio (Earth-616)", "yukio_k": "Yukio (Earth-616)", "mariko": "Mariko Yashida (Earth-616)",
          "viper": "Ophelia Sarkissian (Earth-616)", "shingen": "Shingen Yashida (Earth-616)",
          "harada": "Kenuichio Harada (Earth-616)", "caliban": "Caliban (Earth-616)", "pierce": "Donald Pierce (Earth-616)",
          "leech": "Leech (Earth-616)", "riptide": "Janos Quested (Earth-616)", "darwin": "Armando Muñoz (Earth-616)",
          "moira_b": "Moira MacTaggert (Earth-616)", "moira_w": "Moira MacTaggert (Earth-616)", "trask": "Bolivar Trask (Earth-616)",
          "sentinel": "Sentinels", "stryker_c": "William Stryker (Earth-616)", "stryker_d": "William Stryker (Earth-616)",
          "stryker_j": "William Stryker (Earth-616)", "kelly": "Robert Kelly (Earth-616)", "ajax": "Francis Freeman (Earth-616)",
          "angeldust": "Christina (Earth-616)", "firefist": "Russell Collins (Earth-616)", "blacktom": "Thomas Cassidy (Earth-616)",
          "bedlam": "Jesse Aaronson (Earth-616)", "zeitgeist": "Axel Cluney (Earth-616)", "cassandra": "Cassandra Nova (Earth-616)", "dogpool": "Dogpool (Earth-10330)", "ladypool": "Wanda Wilson (Earth-3010)",
          "alioth": "Alioth (Multiverse)", "dani": "Danielle Moonstar (Earth-616)", "magik": "Illyana Rasputina (Earth-616)",
          "reyes": "Cecilia Reyes (Earth-616)", "vanessa": "Vanessa Carlysle (Earth-616)", "weasel": "Jack Hammer (Earth-616)",
          "blindal": "Althea (Earth-616)", "rice": "Zander Rice (Earth-616)"}

RARE = {"UR": "wolverine xavier_s magneto_m deadpool xavier_m magneto_f"}
