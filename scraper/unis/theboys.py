U = dict(id="theboys", n="黑袍宇宙", en="The Boys · Vought International", short="Vought",
         tag="超级英雄是一门生意。",
         theme=["#C1272D", "#F3E0C0", "#141017"])
ORDER = 22

# 一部剧拆成几季：ss=第几季，标记了那一季才点亮那一季的角色（看过全剧全部都算）
WORKS = """
## tb | 黑袍纠察队 | The Boys · 2019—2026
tb1 | The Boys | 2019 | 黑袍纠察队 | ty=s ss=1
tb2 | The Boys | 2019 | 黑袍纠察队 | ty=s ss=2
tb3 | The Boys | 2019 | 黑袍纠察队 | ty=s ss=3
tb4 | The Boys | 2019 | 黑袍纠察队 | ty=s ss=4
tb5 | The Boys | 2019 | 黑袍纠察队 | ty=s ss=5
## gv | V世代 | Gen V · Godolkin University
gv1 | Gen V | 2023 | V世代 | ty=s ss=1
gv2 | Gen V | 2023 | V世代 | ty=s ss=2
"""

CHARS = """
homelander | 祖国人 | Homelander | 七人众队长 · 沃特的头号超级英雄 | Antony Starr | tb1 tb2 tb3 tb4 tb5 gv1 | #1F4FA0 | 七人众;沃特 | 能力:飞行、热视线、刀枪不入、超级听力;出身:在沃特的实验室里长大，没有父母;口头禅:“我可以做任何我想做的事”;弱点:想被爱想疯了;名场面:喝牛奶 | butcher:死敌;ryan:儿子;soldierboy:生父;stormfront:恋人;starlight:最看不顺眼的队友;stillwell:“妈妈”一样的上司;ashley:吓破胆的公关
> 全世界最受爱戴的超级英雄，也是这部剧最可怕的人。笑容是公司设计过的，愤怒是真的。整部剧都在问一个问题：一个无所不能、却从没被爱过的人，会变成什么样。
butcher | 比利·布彻 | Billy Butcher | 黑袍纠察队队长 · 外号“屠夫” | Karl Urban | tb1 tb2 tb3 tb4 tb5 | #3A3A3A | 黑袍纠察队 | 口头禅:“Oi, cunt.”;武器:撬棍，以及什么都干得出来;执念:替妻子贝嘉向祖国人报仇;第三季:为了打败超人，自己也打了 V;软肋:贝嘉留下的孩子瑞恩 | homelander:死敌;becca:妻子;ryan:贝嘉的孩子;hughie:嘴上嫌弃、心里护着的小子;mm:老战友;mallory:旧上司
> 带着一身仇恨和一口伦敦脏话的屠夫。他讨厌所有超人，手段比反派还脏，却总在最后一刻，为了贝嘉留下的东西心软。
hughie | 休伊·坎贝尔 | Hughie Campbell | 电子产品店店员 → 黑袍纠察队 | Jack Quaid | tb1 tb2 tb3 tb4 tb5 | #6A8A5A | 黑袍纠察队 | 起因:女友在他手里被火车头撞没了;爱好:比利·乔尔;名场面:第一季把透明人炸成了碎片;第三季:为了能保护星光，打了临时 V | starlight:恋人;butcher:又怕又依赖的队长;atrain:仇人;frenchie:兄弟
> 一个普通到不能再普通的男孩，被卷进了超人的世界。他害怕、会哭、会犯傻，却一次次站到比自己强大一百倍的人面前。
starlight | 星光 | Starlight | 安妮·简纽瑞 · 七人众新人 | Erin Moriarty | tb1 tb2 tb3 tb4 tb5 | #E0B030 | 七人众;黑袍纠察队 | 能力:吸收和释放电光;出身:从小被妈妈当成超级英雄来培养;第一季:带着理想加入七人众，第一天就幻灭;后来:公开揭穿沃特，站到了抵抗的一边 | hughie:恋人;homelander:最大的敌人;maeve:后来彼此托付的前辈;deep:入队第一天就伤害她的人
> 怀着“我要拯救世界”的心愿进了七人众，第一天就看清了这家公司的真面目。她没有变成他们，而是成了黑袍纠察队在沃特内部的光。
mm | 母乳 | Mother's Milk | 黑袍纠察队的老兵 · 讲规矩的那一个 | Laz Alonso | tb1 tb2 tb3 tb4 tb5 | #5A4A3A | 黑袍纠察队 | 习惯:有强迫症，东西要摆整齐;身份:队里唯一有正常家庭的人;执念:士兵男孩毁了他的家 | butcher:老战友，也最常和他吵;frenchie:天天斗嘴的队友;soldierboy:家仇
> 队里最像大人的那一个：有家有女儿，想把事情做完然后回家。也正因为有要守护的人，他比谁都恨那些不受约束的超人。
frenchie | 法国佬 | Frenchie | 黑袍纠察队的武器专家 | Tomer Capone | tb1 tb2 tb3 tb4 tb5 | #4A6A8A | 黑袍纠察队 | 本事:什么都能造，什么都能弄到手;过去:当过雇佣兵，手上沾过血;心结:总觉得自己不配被原谅 | kimiko:最重要的人;hughie:兄弟;mm:斗嘴搭子
> 嘴上没个正经、背后一堆案底的法国人。他能用一堆垃圾拼出武器，也能为一个不会说话的女孩，把整个世界掀翻。
kimiko | 宫代纪美子 | Kimiko Miyashiro | 喜美子 · 不说话的超人 | Karen Fukuhara | tb1 tb2 tb3 tb4 tb5 | #A03A5A | 黑袍纠察队 | 能力:快速自愈、怪力;身世:小时候被人贩子拐走，注射了 V;沟通:用手语;名场面:第三季的歌舞幻想 | frenchie:最重要的人;butcher:收留她的人
> 被拐卖、被改造、被当成武器的女孩。她一句话都不说，却是队里最能打、也最温柔的人。
maeve | 梅芙女王 | Queen Maeve | 七人众的元老 | Dominique McElligott | tb1 tb2 tb3 | #8A6A3A | 七人众 | 能力:怪力、近乎不死;状态:对这份工作早就麻木了;第三季:为了拦住士兵男孩失去了能力，干脆假死，和女友离开了这一切 | homelander:老同事，也是最了解他的人;starlight:后来托付了后背的人
> 七人众里看得最透的人。她见过太多，也妥协了太多，直到有一天，决定为一件事再勇敢一次。
atrain | 火车头 | A-Train | 七人众 · 世界上跑得最快的人 | Jessie T. Usher | tb1 tb2 tb3 tb4 tb5 | #3A6AB0 | 七人众 | 能力:超高速;依赖:靠化合物 V 维持速度;黑历史:第一集撞死了休伊的女友 | hughie:欠了一条命的人;deep:七人众里的难兄难弟
> 怕被淘汰、怕被取代的速度者。他做过最坏的事，后来也慢慢学着去做一件对的事。
deep | 深海 | The Deep | 七人众 · 海洋之王 | Chace Crawford | tb1 tb2 tb3 tb4 tb5 | #2A7A8A | 七人众 | 能力:和海洋生物说话、水下呼吸;笑点:第四季和章鱼谈恋爱;黑历史:星光入队第一天就伤害了她 | starlight:伤害过的人;atrain:难兄难弟;homelander:想讨好的人
> 七人众里最可笑也最可悲的人：总想被认真对待，却一次次把自己活成了笑话。
noir | 玄色 | Black Noir | 七人众 · 不露脸的忍者 | Nathan Mitchell | tb1 tb2 tb3 tb4 | #2A2A30 | 七人众 | 能力:顶尖的格斗与潜行;秘密:面具下的脸、和士兵男孩的旧事;第四季:换了一个人穿上这身衣服 | homelander:沉默的队友;soldierboy:旧日的队长
> 永远不说话、永远戴着面具的七人众成员。直到第三季，大家才知道这身黑衣下面藏着什么。
translucent | 透明人 | Translucent | 七人众 · 能隐身的人 | Alex Hassell | tb1 | #7A8A9A | 七人众 | 能力:皮肤能隐形、坚不可摧;名场面:被黑袍纠察队关起来，最后被休伊炸了 | hughie:让他爆炸的人
> 第一季被黑袍纠察队抓住的超人，也让大家第一次知道：超人也是会死的。
stillwell | 玛德琳·斯蒂尔韦尔 | Madelyn Stillwell | 沃特副总裁 | Elisabeth Shue | tb1 | #8A5A6A | 沃特 | 本事:唯一管得住祖国人的人;手段:用“妈妈”一样的温柔拿捏他 | homelander:管不住的“孩子”;butcher:对手
> 沃特的高管，也是祖国人身边最像母亲的人。她以为自己能控制他。
stormfront | 风暴女 | Stormfront | 七人众新成员 · 网红英雄 | Aya Cash | tb2 | #B04A2A | 七人众 | 能力:操控雷电;人设:敢说真话的叛逆网红;真面目:活了很久的纳粹 | homelander:恋人;starlight:死对头;ryan:想拉拢的孩子
> 第二季空降七人众的网红英雄，说话够冲、粉丝够多。可她的过去，比任何人想象的都要黑暗。
soldierboy | 士兵男孩 | Soldier Boy | 二战时代的初代超级英雄 | Jensen Ackles | tb3 tb5 | #5A6A3A | 沃特 | 能力:力量、耐力，以及从胸口放出的能量冲击;来历:二战老兵，被俄国人冰封了几十年;身份:祖国人的生父 | homelander:儿子;mm:仇人;noir:旧部下;butcher:合作过的危险盟友
> 沃特的第一代招牌英雄，从冰封里醒来就一肚子火。一个满嘴 80 年代老派腔调的“爸爸”，比儿子还不好惹。
neuman | 维多利亚·纽曼 | Victoria Neuman | 国会议员 · 会爆头的政客 | Claudia Doumit | tb2 tb3 tb4 | #6A3A6A | 政界 | 能力:让人的头爆掉;公开身份:反超人的女议员;秘密:被沃特高层收养的超人 | hughie:第三季的上司;edgar:养父
> 在镜头前反对超人、在背地里自己就是超人的政客。整部剧最会演戏的人之一。
ryan | 瑞恩 | Ryan Butcher | 贝嘉和祖国人的儿子 | Cameron Crovetti | tb2 tb3 tb4 tb5 | #6A8AAA | 布彻家 | 能力:和父亲一样的力量;难题:该成为谁的孩子 | homelander:亲生父亲;butcher:继父;becca:妈妈
> 祖国人的儿子，被妈妈藏起来长大。两个“爸爸”都想要他，他得自己决定要成为什么样的人。
becca | 贝嘉·布彻 | Becca Butcher | 屠夫的妻子 | Shantel VanSanten | tb1 tb2 | #9A7A6A | 布彻家 | 过去:在沃特工作时被祖国人伤害;后来:独自把瑞恩藏起来养大 | butcher:丈夫;ryan:儿子;homelander:伤害她的人
> 屠夫心里最软的地方。她的离开让屠夫走上了复仇的路，她的孩子又一次次把屠夫拉回人间。
ashley | 阿什莉·巴雷特 | Ashley Barrett | 沃特的公关主管 | Colby Minifie | tb1 tb2 tb3 tb4 tb5 | #C08060 | 沃特 | 状态:永远在崩溃边缘;压力:掉头发 | homelander:最怕的老板;deep:想往上爬的同事
> 夹在祖国人和公司之间的公关，一边收拾烂摊子，一边一把一把地掉头发。
edgar | 斯坦·埃德加 | Stan Edgar | 沃特集团 CEO | Giancarlo Esposito | tb1 tb2 tb3 | #3A3A4A | 沃特 | 本事:唯一敢跟祖国人讲道理的人;信条:沃特是一家制药公司 | homelander:不听话的产品;neuman:养女
> 沃特真正的掌舵人，冷静、优雅、从不提高音量，祖国人在他面前也得收着点。
sage | 智者 | Sister Sage | 七人众 · 世界上最聪明的人 | Susan Heyward | tb4 tb5 | #6A4A8A | 七人众 | 能力:超级智力;角色:替祖国人谋划的军师 | homelander:被她操纵的人;firecracker:同盟
> 第四季加入七人众的“最聪明的人”。她太聪明了，聪明到知道怎样让祖国人做她想做的事。
firecracker | 爆竹 | Firecracker | 七人众 · 极右网红 | Valorie Curry | tb4 tb5 | #C03A3A | 七人众 | 能力:爆炸火花;身份:阴谋论网红;旧怨:和星光有一段少年时的过节 | starlight:死对头;homelander:狂热追随的人
> 靠煽动粉丝出名的网红英雄，对祖国人狂热、对星光恨之入骨。
mallory | 格蕾丝·马洛里 | Grace Mallory | 黑袍纠察队的创始人 · 前 CIA | Laila Robins | tb1 tb2 tb3 tb4 | #6A6A5A | 黑袍纠察队 | 身份:前 CIA 副局长;过去:最早组建黑袍纠察队的人 | butcher:旧部下;soldierboy:旧怨
> 黑袍纠察队的老上司。是她最早决定：得有人盯着这些超人。
marie | 玛丽·莫罗 | Marie Moreau | 戈德金大学新生 · 血液操控者 | Jaz Sinclair | gv1 gv2 | #9A1A2A | 戈德金大学 | 能力:操控血液;梦想:成为进入七人众的第一位黑人女性 | jordan:搭档与恋人;emma:室友;cate:朋友 → 复杂的关系
> 带着一段伤痛的过去，考进了培养超级英雄的戈德金大学。她以为自己来这里是为了成为英雄。
jordan | 乔丹·李 | Jordan Li | 戈德金大学的尖子生 | London Thor;Derek Luh | gv1 gv2 | #3A5A9A | 戈德金大学 | 能力:在两种性别形态之间切换，各有不同的能力;目标:排名第一 | marie:搭档与恋人;andre:室友
> 学校排名靠前的学生，有两种形态，两位演员。比谁都想赢，也比谁都想被真正看见。
andre | 安德烈·安德森 | Andre Anderson | 戈德金大学 · 磁力操控者 | Chance Perdomo | gv1 | #4A4A6A | 戈德金大学 | 能力:操控金属;父亲:超人英雄“极性”;好友:金童 | polarity:父亲;goldenboy:最好的朋友;cate:恋人
> 背负着父亲光环的学生。演员查斯·佩尔多莫在 2024 年意外离世，剧组在第二季里向他告别。
emma | 艾玛·迈耶 | Emma Meyer | 戈德金大学 · 会变小的女孩 | Lizze Broadway | gv1 gv2 | #C07A9A | 戈德金大学 | 能力:变大变小;外号:小蟋蟀 | marie:室友兼好友;sam:喜欢的人
> 玛丽的室友，能缩小也能变大。看起来最软，其实最勇敢。
cate | 凯特·邓拉普 | Cate Dunlap | 戈德金大学 · 能左右人心的人 | Maddie Phillips | gv1 gv2 | #8A6AAA | 戈德金大学 | 能力:碰到一个人就能操控他的想法;代价:用多了会流鼻血 | andre:恋人;goldenboy:前任;marie:朋友;sam:后来走到一起的人
> 学校里人缘最好的女孩。她的能力太方便，方便到连她自己都分不清，哪些选择是别人真心的。
sam | 山姆·里奥丹 | Sam Riordan | 金童的弟弟 | Asa Germann | gv1 gv2 | #5A7A4A | 戈德金大学 | 能力:刀枪不入、怪力;处境:被关在学校地下的“树林”里 | goldenboy:哥哥;emma:心上人;cate:后来走到一起的人
> 被关在学校地下的男孩，一身怪力，内心却还是个受了伤的孩子。
goldenboy | 金童 | Golden Boy | 路克·里奥丹 · 戈德金大学排名第一 | Patrick Schwarzenegger | gv1 | #D0A030 | 戈德金大学 | 能力:全身燃烧;身份:最有希望进七人众的学生 | sam:弟弟;andre:最好的朋友;cate:前任
> 学校的金字招牌，人人都以为他前途无量，没人想到这所学校的秘密会从他身上揭开。
shetty | 英迪拉·谢蒂 | Indira Shetty | 戈德金大学院长 | Shelley Conn | gv1 | #6A5A5A | 戈德金大学 | 身份:院长，也是沃特的人;目的:她有自己的复仇计划 | marie:想利用的学生;sam:地下“树林”的研究对象
> 温和体面的院长，背后经营着学校最不能见光的地方。
polarity | 极性 | Polarity | 安德烈的父亲 · 老牌英雄 | Sean Patrick Thomas | gv1 | #4A4A8A | 戈德金大学 | 能力:操控磁场;代价:能力用久了伤了身体 | andre:儿子
> 用了一辈子磁力的老英雄，希望儿子接班，也开始为这份能力付出代价。
cipher | 西弗 | Cipher | 戈德金大学第二季的新院长 | Hamish Linklater | gv2 | #3A3A3A | 戈德金大学 | 身份:新院长，神秘;方式:亲自“指导”玛丽 | marie:盯上的学生
> 第二季走马上任的新院长，笑眯眯地说着“我是来帮你的”，可没人知道他到底想要什么。
"""

DECKS = """
seven | 七人众 | The Seven | 🦅 | homelander starlight maeve atrain deep noir translucent
boys | 黑袍纠察队 | The Boys | 🧥 | butcher hughie mm frenchie kimiko
vought | 沃特集团 | Vought International | 🏢 | stillwell edgar ashley sage
newseven | 新七人众 | The New Seven | ⚡ | homelander stormfront sage firecracker deep atrain
family | 祖国人一家 | Homelander's Family | 🍼 | homelander soldierboy ryan
butchers | 布彻一家 | The Butchers | 🏠 | butcher becca ryan
supes | 超人搭档 | Hughie & Annie | 💛 | hughie starlight
frenchkim | 法国佬和喜美子 | Frenchie & Kimiko | 🎭 | frenchie kimiko
godolkin | 戈德金大学 | Godolkin University | 🎓 | marie jordan andre emma cate sam
"""

RARE = {"UR": "homelander butcher starlight hughie", "SSR": "kimiko frenchie mm maeve soldierboy marie jordan",
        "SR": "atrain deep noir stormfront neuman ryan sage emma cate andre sam goldenboy",
        "R": "translucent stillwell becca ashley edgar firecracker mallory shetty polarity cipher"}
