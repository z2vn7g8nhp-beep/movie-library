U = dict(id="trek", n="星际迷航", en="Star Trek", short="STAR TREK",
         tag="太空，最后的边疆。进取号的三代舰桥成员，和他们几百年的星际航行。",
         theme=["#3E6AB5", "#E0C060", "#0A0E1A"], timeline=True, wd=["Q1102217"])
ORDER = 18

WORKS = """
## tos | 初代电影 | The Original Crew
st1 | Star Trek: The Motion Picture | 1979 | 星际旅行1：无限太空 | tl=2273
st2 | Star Trek II: The Wrath of Khan | 1982 | 星际旅行2：可汗怒吼 | tl=2285
st3 | Star Trek III: The Search for Spock | 1984 | 星际旅行3：石破天惊 | tl=2285.5
st4 | Star Trek IV: The Voyage Home | 1986 | 星际旅行4：抢救未来 | tl=2286
st5 | Star Trek V: The Final Frontier | 1989 | 星际旅行5：终极先锋 | tl=2287
st6 | Star Trek VI: The Undiscovered Country | 1991 | 星际旅行6：未来之城 | tl=2293
## tng | 下一代电影 | The Next Generation
gen | Star Trek: Generations | 1994 | 星际旅行7：斗转星移 | tl=2371
fc | Star Trek: First Contact | 1996 | 星际旅行8：第一类接触 | tl=2373
ins | Star Trek: Insurrection | 1998 | 星际旅行9：起义 | tl=2375
nem | Star Trek: Nemesis | 2002 | 星际旅行10：复仇女神 | tl=2379
## kelvin | 凯尔文时间线 | The Kelvin Timeline
st09 | Star Trek | 2009 | 星际迷航 | tl=2258 tll=凯尔文时间线·2258_年
stid | Star Trek Into Darkness | 2013 | 星际迷航2：暗黑无界 | tl=2259 tll=凯尔文时间线·2259_年
stb | Star Trek Beyond | 2016 | 星际迷航3：超越星辰 | tl=2263 tll=凯尔文时间线·2263_年
"""

CHARS = """
# —— 凯尔文时间线的舰桥
kirk_p | 詹姆斯·T·柯克 | James T. Kirk | 凯尔文版 · 克里斯·派恩 | Chris Pine | st09 stid stb | #C9A040 | 星际舰队;进取号舰长;凯尔文时间线 | 军衔:舰长;特点:冲动、自信、星际舰队学院史上唯一通过“小林丸测试”的人（作弊）;生日:出生在父亲牺牲的那一天 | spock_q:从死对头到最好的朋友;bones_u:最好的朋友;george:父亲;pike:引路人;kirk_s:另一个时间线的自己
> 出生那天父亲就牺牲在太空里的叛逆少年，被派克舰长一句话激进了星际舰队。年轻、莽撞、运气好得离谱，最后成了进取号的舰长。
spock_q | 斯波克 | Spock | 凯尔文版 · 扎克瑞·昆图 | Zachary Quinto | st09 stid stb | #3E6AB5 | 星际舰队;瓦肯人;进取号大副 | 血统:瓦肯人与人类的混血;手势:瓦肯举手礼;祝福语:生生不息，繁荣昌盛;擅长:逻辑、瓦肯神经掐 | kirk_p:最好的朋友;uhura_z:恋人;sarek_c:父亲;amanda_r:母亲;spock_n:年老的自己
> 一半瓦肯血统、一半人类血统的大副，用逻辑压住所有情绪。他的家园在他眼前毁灭，从那以后，他学着和自己的另一半相处。
bones_u | 伦纳德·麦考伊 | Leonard "Bones" McCoy | 凯尔文版 · 卡尔·厄本 | Karl Urban | st09 stid stb | #3E8A6A | 星际舰队;进取号首席医官 | 外号:骨头;口头禅:该死，吉姆，我是医生，不是……;特点:恐惧太空（真的） | kirk_p:最好的朋友;spock_q:斗嘴的对象;bones_k:另一个时间线的自己
> 离婚后只剩下“骨头”的医生，恐惧太空还非要上飞船。他和斯波克能从早吵到晚。
uhura_z | 乌胡拉 | Nyota Uhura | 凯尔文版 · 佐伊·索尔达娜 | Zoe Saldana | st09 stid stb | #B8302E | 星际舰队;通讯官 | 擅长:语言学（能听懂罗慕兰语三种方言）;名字:柯克花了好久才知道她的名 | spock_q:恋人;kirk_p:一开始被她嫌弃;uhura_n:另一个时间线的自己
> 进取号的通讯官，精通几十种外星语言，和斯波克之间有一段安静的恋爱。
scotty_p | 斯科特 | Montgomery "Scotty" Scott | 凯尔文版 · 西蒙·佩吉 | Simon Pegg | st09 stid stb | #B8302E | 星际舰队;轮机长 | 口音:苏格兰腔;发明:跨曲速传送公式;好友:基恩瑟 | keenser:形影不离的小助手;scotty_d:另一个时间线的自己
> 被流放到冰雪星球的天才轮机长，一句苏格兰腔“我给她加满动力了”，就是进取号最大的底气。
sulu_c | 苏鲁 | Hikaru Sulu | 凯尔文版 · 约翰·赵 | John Cho | st09 stid stb | #C9A040 | 星际舰队;舵手 | 擅长:击剑、驾驶 | sulu_t:另一个时间线的自己
> 进取号的舵手，击剑高手。在超越星辰里，他有一个丈夫和一个女儿。
chekov_y | 契诃夫 | Pavel Chekov | 凯尔文版 · 安东·叶尔钦 | Anton Yelchin | st09 stid stb | #C9A040 | 星际舰队;领航员 | 年龄:17 岁就上了舰桥;口音:俄罗斯腔（把 v 念成 w） | chekov_k:另一个时间线的自己
> 十七岁的天才领航员，俄罗斯口音把“胜利”念得像“汪利”。演员安东·叶尔钦在 2016 年离世，这个角色也永远停在了那里。
pike | 克里斯托弗·派克 | Christopher Pike | 进取号首任舰长 | Bruce Greenwood | st09 stid | #4A5A8A | 星际舰队;舰长、上将 | 名言:我敢说你做不到（激将法） | kirk_p:看好的年轻人;george:敬佩的人
> 在酒吧里把打架的柯克劝进星际舰队的人，柯克心里的第二个父亲。
george | 乔治·柯克 | George Kirk | 柯克的父亲 | Chris Hemsworth | st09 | #4A6A8A | 星际舰队;凯尔文号 | 名场面:当了 12 分钟舰长，救下 800 人 | kirk_p:儿子;winona:妻子
> 只当了十二分钟的舰长，用自己的命换回了八百条命，和刚出生的儿子。演员是还没成为雷神的克里斯·海姆斯沃斯。
winona | 薇诺娜·柯克 | Winona Kirk | 柯克的母亲 | Jennifer Morrison | st09 | #8A6A7A | 凯尔文号 | kirk_p:儿子;george:丈夫
> 在逃生舱里生下柯克的母亲。
sarek_c | 萨瑞克 | Sarek | 凯尔文版 · 斯波克的父亲 | Ben Cross | st09 | #5A6A5A | 瓦肯人;大使 | 名言:我娶你母亲，是因为我爱她 | spock_q:儿子;amanda_r:妻子
> 斯波克的瓦肯父亲，一辈子讲逻辑，却娶了一位人类女子。
amanda_r | 阿曼达 | Amanda Grayson | 凯尔文版 · 斯波克的母亲 | Winona Ryder | st09 | #8A7A8A | 人类 | spock_q:儿子;sarek_c:丈夫
> 斯波克的人类母亲，是他心里最柔软的部分。
nero | 尼禄 | Nero | 罗慕兰矿船船长 | Eric Bana | st09 | #3A4A3A | 罗慕兰人 | 飞船:纳拉达号;动机:为毁灭的母星复仇;造型:光头、面部纹身 | spock_n:复仇对象
> 从未来穿越回来的罗慕兰矿工，因为母星毁灭而疯狂。他的出现，改写了整条时间线。
khan_c | 可汗 | Khan | 凯尔文版 · 卷福 | Benedict Cumberbatch | stid | #2E2E3A | 基因优化人 | 化名:约翰·哈里森;特点:超人的力量与智慧、血液能复活生命 | kirk_p:对手;marcus:唤醒他的人;khan_m:另一个时间线的自己
> 被星际舰队唤醒的三百年前的超人，冷静、优雅、致命。他的血能让死人复生。
carol_a | 卡罗尔·马库斯 | Carol Marcus | 凯尔文版 · 武器专家 | Alice Eve | stid stb | #C9A080 | 星际舰队;科学官 | 父亲:马库斯上将 | marcus:父亲;carol_b:另一个时间线的自己
> 化名登上进取号的武器专家，马库斯上将的女儿。
marcus | 马库斯上将 | Admiral Marcus | 星际舰队上将 | Peter Weller | stid | #4A4A5A | 星际舰队 | 计划:对克林贡开战 | carol_a:女儿;khan_c:唤醒的人
> 想挑起和克林贡战争的上将，唤醒了一个不该唤醒的人。
manas | 马纳斯 | Manas | 克拉尔的副手 | Joe Taslim | stb | #4A4A5A | 外星人;克拉尔的部下 | 武器:双刃 | krall:主人;jaylah:仇人
> 克拉尔手下的头号打手，杀了杰拉的父亲。
keenser | 基恩瑟 | Keenser | 斯科特的小助手 | Deep Roy | st09 stid stb | #6A9A6A | 外星人 | 特点:个子小小、从不说话 | scotty_p:形影不离的老板
> 斯科特在冰雪星球上的小个子外星助手，几乎不说话，却总在最需要的时候出现。
jaylah | 杰拉 | Jaylah | 废品星的女战士 | Sofia Boutella | stb | #E0E0E0 | 外星人 | 住处:坠毁的富兰克林号;最爱:“公立学校男孩们”（她对披头士的理解）;特点:脸上的黑色纹路 | scotty_p:她喜欢的“蒙哥马利·斯科提”;krall:仇人
> 独自在坠毁飞船里活下来的外星女战士，最爱放“披头士”——她以为那是“公立学校男孩们”。
krall | 克拉尔 | Krall | 吸取生命的怪物 | Idris Elba | stb | #4A3A3A | 外星人 | 秘密:他曾经是星际舰队的人 | jaylah:仇人;kirk_p:对手
> 吸取别人生命力续命的异族首领，他和星际舰队之间有一段被遗忘的过去。
# —— 初代舰桥
kirk_s | 詹姆斯·T·柯克 | James T. Kirk | 初代 · 威廉·夏特纳 | William Shatner | st1 st2 st3 st4 st5 st6 gen | #C9A040 | 星际舰队;进取号舰长 | 名台词:可——汗！;飞船:进取号 NCC-1701 | spock_n:最好的朋友;bones_k:最好的朋友;khan_m:宿敌;carol_b:旧爱;david:儿子;picard:跨世代的相遇;kirk_p:另一个时间线的自己
> 最经典的柯克舰长，一声“可——汗！”喊进了流行文化。他跨越世代，在第七部里和皮卡德并肩。
spock_n | 斯波克 | Spock | 初代 · 伦纳德·尼莫伊 | Leonard Nimoy | st1 st2 st3 st4 st5 st6 st09 stid | #3E6AB5 | 星际舰队;瓦肯人 | 名言:多数人的需要高于少数人;手势:瓦肯举手礼;后来:作为“老斯波克”出现在凯尔文时间线 | kirk_s:最好的朋友;bones_k:斗嘴的对象;sarek_l:父亲;spock_q:年轻的另一个自己;nero:复仇者的目标
> 初代的斯波克，让“生生不息，繁荣昌盛”成了全世界都认识的手势。他在凯尔文时间线里，又见到了年轻的自己。
bones_k | 伦纳德·麦考伊 | Leonard "Bones" McCoy | 初代 · 德福雷斯特·凯利 | DeForest Kelley | st1 st2 st3 st4 st5 st6 | #3E8A6A | 星际舰队;首席医官 | 口头禅:他死了，吉姆 | kirk_s:最好的朋友;spock_n:斗嘴的对象（也曾背过斯波克的灵魂）
> 初代的“骨头”，刀子嘴豆腐心，在第三部里还替斯波克保管过灵魂。
uhura_n | 乌胡拉 | Nyota Uhura | 初代 · 尼切尔·尼科尔斯 | Nichelle Nichols | st1 st2 st3 st4 st5 st6 | #B8302E | 星际舰队;通讯官 | 意义:六十年代美国电视上最早的黑人女性主要角色之一
> 初代的通讯官，她的存在本身就是那个年代的一个突破。
scotty_d | 斯科特 | Montgomery "Scotty" Scott | 初代 · 詹姆斯·杜汉 | James Doohan | st1 st2 st3 st4 st5 st6 gen | #B8302E | 星际舰队;轮机长 | 名台词（被认为的）:把我传送上去，斯科提
> 初代的轮机长，什么不可能的维修，到他手里都能“再多撑一会儿”。
sulu_t | 苏鲁 | Hikaru Sulu | 初代 · 乔治·武井 | George Takei | st1 st2 st3 st4 st5 st6 | #C9A040 | 星际舰队;舵手→精益号舰长
> 初代的舵手，第六部里已经是精益号的舰长了。
chekov_k | 契诃夫 | Pavel Chekov | 初代 · 沃尔特·凯尼格 | Walter Koenig | st1 st2 st3 st4 st5 st6 gen | #C9A040 | 星际舰队;领航员 | 口头禅:这是俄罗斯人发明的
> 初代的领航员，什么都要说一句“这是俄罗斯人发明的”。
khan_m | 可汗 | Khan Noonien Singh | 初代 · 蒙塔尔班 | Ricardo Montalban | st2 | #6A4A3A | 基因优化人 | 往事:被柯克流放到荒凉星球十五年 | kirk_s:宿敌;khan_c:另一个时间线的自己
> 被柯克流放十五年的基因超人，带着复仇之心回来，引用着《白鲸》。
saavik | 萨维克 | Saavik | 瓦肯见习军官 | Kirstie Alley; Robin Curtis | st2 st3 st4 | #6A6A8A | 星际舰队;瓦肯人 | 测试:小林丸
> 第二部里挑战“小林丸测试”的瓦肯学员，两部里换了两位演员。
carol_b | 卡罗尔·马库斯 | Carol Marcus | 初代 · 创世计划科学家 | Bibi Besch | st2 | #C9A080 | 科学家 | 计划:创世装置 | kirk_s:旧爱;david:儿子;carol_a:另一个时间线的自己
> 研究“创世装置”的科学家，柯克的旧爱。
david | 大卫·马库斯 | David Marcus | 柯克的儿子 | Merritt Butrick | st2 st3 | #8A7A5A | 科学家 | kirk_s:父亲;carol_b:母亲
> 柯克从未相认的儿子，和母亲一起研究创世装置。
sarek_l | 萨瑞克 | Sarek | 初代 · 斯波克的父亲 | Mark Lenard | st3 st4 st6 | #5A6A5A | 瓦肯人;大使 | spock_n:儿子
> 初代里的瓦肯大使，斯波克严厉的父亲。
kruge | 克鲁格 | Kruge | 克林贡指挥官 | Christopher Lloyd | st3 | #6A3A2A | 克林贡人 | 宠物:一只像狗的怪兽 | kirk_s:对手
> 抢夺创世装置的克林贡指挥官，演员是《回到未来》里的布朗博士。
gillian | 吉莉安·泰勒 | Gillian Taylor | 鲸鱼保护者 | Catherine Hicks | st4 | #8A6A5A | 人类;1986 年 | 照顾的:两头座头鲸
> 1986 年旧金山水族馆的鲸鱼专家，被穿越来的进取号船员拉进了一场拯救未来的冒险。
sybok | 赛伯克 | Sybok | 斯波克的哥哥 | Laurence Luckinbill | st5 | #6A5A3A | 瓦肯人 | 能力:帮人释放内心的痛苦;信念:去宇宙中心寻找神 | spock_n:同父异母的弟弟
> 斯波克同父异母的哥哥，一个拥抱情感的瓦肯人，带着进取号去宇宙中心寻找“神”。
chang | 张将军 | General Chang | 克林贡将军 | Christopher Plummer | st6 | #5A3A2A | 克林贡人 | 特点:独眼、满口莎士比亚 | kirk_s:对手
> 戴着眼罩、开口就是莎士比亚的克林贡将军。
gorkon | 戈尔孔 | Gorkon | 克林贡总理 | David Warner | st6 | #6A4A3A | 克林贡人 | 愿望:和联邦和平共处
> 想和联邦讲和的克林贡总理。
valeris | 瓦莱里斯 | Valeris | 瓦肯军官 | Kim Cattrall | st6 | #8A8AA0 | 星际舰队;瓦肯人 | spock_n:导师
> 斯波克的学生，聪明的瓦肯军官，藏着一个秘密。
decker | 德克尔 | Willard Decker | 进取号新舰长 | Stephen Collins | st1 | #6A6A8A | 星际舰队 | ilia:旧爱
> 第一部里被柯克夺走指挥权的年轻舰长。
ilia | 伊利亚 | Ilia | 光头的领航员 | Persis Khambatta | st1 | #C08A6A | 德尔塔人 | decker:旧爱
> 来自德尔塔星的光头领航员。
# —— 下一代
picard | 让-吕克·皮卡德 | Jean-Luc Picard | 进取号-D 舰长 | Patrick Stewart | gen fc ins nem | #B8302E | 星际舰队;进取号舰长 | 口头禅:就这么办（Make it so）;最爱:伯爵茶，热的;往事:曾被博格同化为“洛卡特斯” | riker:大副与挚友;data:最信任的船员;borgqueen:宿敌;kirk_s:跨世代的相遇;shinzon:他的克隆体
> 优雅、博学、爱喝伯爵茶的舰长，一句“就这么办”就是命令。他曾被博格同化，那段记忆一直跟着他。
riker | 威廉·赖克 | William Riker | 大副 | Jonathan Frakes | gen fc ins nem | #6A4A3A | 星际舰队;大副 | 招牌:跨腿坐椅子、络腮胡;爱好:长号、扑克 | picard:舰长;troi:恋人
> 进取号的大副，留着胡子、跨腿坐椅子。他和迪安娜之间的感情，绕了很多年。
data | 达塔 | Data | 仿生人 | Brent Spiner | gen fc ins nem | #C9A040 | 星际舰队;仿生人 | 宠物:猫咪“斑点”;愿望:变成人类;装备:情感芯片 | picard:最敬重的舰长;geordi:最好的朋友;borgqueen:诱惑他的人
> 一心想变成人类的仿生人，养猫、写诗、研究笑话。在第七部里装上情感芯片后，他第一次体会到了害怕。
geordi | 乔迪·拉福吉 | Geordi La Forge | 总工程师 | LeVar Burton | gen fc ins nem | #C9A040 | 星际舰队;总工程师 | 特点:天生失明，戴着视觉增强器 VISOR（后来换成植入眼） | data:最好的朋友
> 天生失明的总工程师，戴着一副发光的“视觉增强器”，和达塔是最好的朋友。
worf | 沃夫 | Worf | 克林贡军官 | Michael Dorn | gen fc ins nem | #6A3A2A | 星际舰队;克林贡人 | 特点:星际舰队第一位克林贡军官;最爱:荣誉、梅子汁 | picard:舰长
> 星际舰队里第一位克林贡军官，把“荣誉”挂在嘴边，喝梅子汁。
crusher | 贝弗利·克拉舍 | Beverly Crusher | 首席医官 | Gates McFadden | gen fc ins nem | #C0603A | 星际舰队;首席医官 | picard:暧昧多年的老友
> 进取号的医生，和皮卡德之间有说不出口的感情。
troi | 迪安娜·特洛伊 | Deanna Troi | 心理顾问 | Marina Sirtis | gen fc ins nem | #6A4A8A | 星际舰队;贝塔佐伊德混血 | 能力:共情（感知他人情绪） | riker:恋人
> 能感知别人情绪的心理顾问，半个贝塔佐伊德人。
guinan | 盖南 | Guinan | 十前酒吧老板 | Whoopi Goldberg | gen nem | #8A5A3A | 埃尔-奥里安人 | 年龄:几百岁;特点:超大的帽子、能感知时间线的异常 | picard:老朋友
> 进取号酒吧的老板，戴着大帽子，活了几百岁，总能说出最智慧的话。
soran | 索兰博士 | Dr. Tolian Soran | 想回到“连结”的科学家 | Malcolm McDowell | gen | #5A5A6A | 埃尔-奥里安人 | 执念:回到能实现一切愿望的“连结” | picard:对手;kirk_s:对手
> 为了回到一个叫“连结”的天堂，不惜摧毁星球的科学家。
borgqueen | 博格女王 | Borg Queen | 博格集合体的意志 | Alice Krige | fc | #4A5A4A | 博格 | 名言:抵抗是徒劳的;特点:只有头和脊椎能和身体分离 | picard:宿敌;data:诱惑的对象
> 博格集合体的声音与意志，诱惑达塔，宣称“抵抗是徒劳的”。
cochrane | 泽弗兰·科克伦 | Zefram Cochrane | 曲速引擎发明者 | James Cromwell | fc | #8A7A5A | 人类;2063 年 | 成就:人类第一次曲速飞行，引来了瓦肯人的“第一类接触” | lily:搭档
> 发明曲速引擎的人，传说中的伟人，本人其实是个爱喝酒、怕出名的家伙。
lily | 莉莉·斯隆 | Lily Sloane | 科克伦的助手 | Alfre Woodard | fc | #6A5A4A | 人类;2063 年 | picard:被她骂醒的舰长
> 科克伦的助手，把被复仇冲昏头的皮卡德骂醒了。
ruafo | 鲁阿福 | Ru'afo | 索纳人首领 | F. Murray Abraham | ins | #8A6A6A | 索纳人 | 执念:不老的星球
> 靠整容维持年轻的索纳人首领，想夺取一颗能让人返老还童的星球。
shinzon | 辛宗 | Shinzon | 皮卡德的克隆体 | Tom Hardy | nem | #3A3A4A | 雷曼人;罗慕兰执政官 | 来历:用皮卡德的 DNA 克隆;飞船:弯刀号 | picard:另一个自己;viceroy:副手
> 用皮卡德的 DNA 造出来、在雷曼矿井里长大的克隆人。年轻的汤姆·哈迪演的。
viceroy | 总督 | The Viceroy | 辛宗的副手 | Ron Perlman | nem | #4A4A5A | 雷曼人 | shinzon:主人
> 辛宗身边的雷曼人副手，能用心灵感应入侵别人的意识。
"""

DECKS = """
kelvin | 凯尔文舰桥 | The Kelvin Crew | 🖖 | kirk_p spock_q bones_u uhura_z scotty_p sulu_c chekov_y
tos | 初代舰桥 | The Original Crew | 🚀 | kirk_s spock_n bones_k uhura_n scotty_d sulu_t chekov_k
tng | 下一代舰桥 | The Next Generation | ⭐ | picard riker data geordi worf crusher troi
kirks | 两代柯克 | Two Kirks | 🏅 | kirk_s kirk_p
spocks | 两代斯波克 | Two Spocks | 🖖 | spock_n spock_q
bones | 两代骨头 | Two Bones | 💉 | bones_k bones_u
khans | 两代可汗 | Two Khans | 🐅 | khan_m khan_c
trio | 柯克、斯波克与骨头 | The Big Three | 🔺 | kirk_p spock_q bones_u
vulcan | 瓦肯之家 | House of Sarek | 🌋 | spock_q sarek_c amanda_r spock_n sarek_l sybok
kirkfam | 柯克一家 | The Kirks | 🌟 | kirk_p george winona pike
klingon | 克林贡帝国 | Klingon Empire | ⚔ | worf kruge chang gorkon
contact | 第一类接触 | First Contact | 🛸 | borgqueen cochrane lily picard data
villains | 星际反派 | Villains | ☄ | khan_m khan_c nero krall shinzon soran ruafo chang
marcus | 马库斯一家 | The Marcuses | 💣 | carol_b david carol_a marcus
beyond | 超越星辰 | Beyond | 🌀 | jaylah krall manas keenser scotty_p
"""

RARE = {"UR": "kirk_p spock_q kirk_s spock_n picard data"}
