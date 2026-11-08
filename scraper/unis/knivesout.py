U = dict(id="knives", n="利刃出鞘", en="A Knives Out Mystery", short="BLANC",
         tag="甜甜圈的洞里还有一个洞。私家侦探本诺特·布兰克，和三桩最离奇的谋杀案。",
         theme=["#8A3A3A", "#E0C8A0", "#140C0C"], wd=["Q115676286"])
ORDER = 30

WORKS = """
## main | 布兰克探案 | Benoit Blanc Mysteries
ko1 | Knives Out | 2019 | 利刃出鞘
ko2 | Glass Onion | 2022 | 利刃出鞘2：玻璃洋葱
ko3 | Wake Up Dead Man | 2025 | 利刃出鞘3：亡者归来
"""

CHARS = """
blanc | 本诺特·布兰克 | Benoit Blanc | 最后的绅士侦探 | Daniel Craig | ko1 ko2 ko3 | #8A6A3A | 私家侦探 | 口音:浓重的美国南方腔;名言:甜甜圈的洞里还有一个洞;爱好:看百老汇、玩游戏（很烂） | marta:最欣赏的人;helen:合作的委托人;jud:最后一案的搭档;phillip:伴侣
> 操着一口南方口音、说话绕来绕去的私家侦探。他看起来总是慢半拍，可每次都能找到“甜甜圈中间那个洞”。
marta | 玛尔塔·卡布雷拉 | Marta Cabrera | 不会撒谎的护士 | Ana de Armas | ko1 | #6A8AA0 | 斯龙比家 | 特点:一撒谎就会吐;职业:哈兰的私人护士 | harlan:最信任她的老人;blanc:欣赏她的侦探;ransom:最难缠的人
> 哈兰的私人护士，一说谎就会呕吐。她是这个贪婪家族里唯一真心对待老人的人。
ransom | 兰森 | Hugh Ransom Drysdale | 家族里的败家子 | Chris Evans | ko1 | #C8B8A0 | 斯龙比家 | 标志:那件米白色的麻花针织毛衣 | harlan:外公;linda:母亲;marta:最难缠的对手
> 斯龙比家的败家子外孙，穿着一件让全网疯狂的麻花毛衣，嘴毒又迷人。
harlan | 哈兰·斯龙比 | Harlan Thrombey | 推理小说大师 | Christopher Plummer | ko1 | #6A5A4A | 斯龙比家 | 职业:畅销推理小说作家;住处:一座像“妙探寻凶”棋盘一样的豪宅 | marta:最信任的人;ransom:外孙;linda:女儿;walt:儿子
> 八十五岁生日后的第二天早上被发现死在书房的推理小说大师。他留下的遗嘱，让全家人都炸了。
linda | 琳达 | Linda Drysdale | 哈兰的女儿 | Jamie Lee Curtis | ko1 | #8A6A6A | 斯龙比家 | 自称:白手起家（其实是爸爸借的钱） | richard:丈夫;ransom:儿子
> 自称白手起家的地产女王，其实启动资金是爸爸给的。
richard | 理查德 | Richard Drysdale | 琳达的丈夫 | Don Johnson | ko1 | #6A6A6A | 斯龙比家 | 秘密:出轨 | linda:妻子
> 琳达的丈夫，满口政治正确，私下里有外遇。
walt | 沃尔特 | Walt Thrombey | 哈兰的儿子 | Michael Shannon | ko1 | #5A5A5A | 斯龙比家 | 工作:管理父亲的出版公司 | harlan:父亲;jacob:儿子
> 管理父亲出版公司的儿子，一心想把书卖给流媒体。
joni | 乔妮 | Joni Thrombey | 哈兰的儿媳 | Toni Collette | ko1 | #A08A6A | 斯龙比家 | 职业:生活方式网红;秘密:重复领取学费 | meg:女儿
> 卖“生活方式”的网红儿媳，一直在偷偷多领学费。
meg | 梅格 | Meg Thrombey | 哈兰的孙女 | Katherine Langford | ko1 | #8A7A8A | 斯龙比家 | joni:母亲;marta:以为的朋友
> 看起来和玛尔塔是朋友的大学生孙女。
jacob | 雅各布 | Jacob Thrombey | 网上冲浪的少年 | Jaeden Martell | ko1 | #5A6A5A | 斯龙比家 | 外号:网络纳粹（家人这么叫他） | walt:父亲
> 整天抱着手机的少年，被家人戏称为“网络纳粹”。
elliott | 埃利奥特警探 | Lt. Elliott | 警探 | Lakeith Stanfield | ko1 | #4A4A5A | 警察 | blanc:合作的侦探
> 负责案子的警探，被布兰克的推理方式搞得一头雾水。
greatnana | 太奶奶 | Great Nana Wanetta | 斯龙比家的老奶奶 | K Callan | ko1 | #A09A9A | 斯龙比家 | 特点:不怎么说话，但什么都看见了
> 斯龙比家年纪最大的老奶奶，平时不说话，却看见了关键的那一幕。
miles | 迈尔斯·布朗 | Miles Bron | 科技亿万富翁 | Edward Norton | ko2 | #C8A040 | 阿尔法公司 | 住处:希腊私人岛屿上的玻璃洋葱;口头禅:颠覆者 | helen:眼中钉;claire:老朋友;lionel:老朋友;birdie:老朋友;duke:老朋友
> 在私人小岛上办“谋杀推理派对”的科技富豪，自称颠覆者，其实是个……还是看了再说吧。
helen | 海伦·布兰德 | Helen Brand | 安迪的双胞胎妹妹 | Janelle Monáe | ko2 | #3A3A5A | 委托人 | 身份:安迪·布兰德的双胞胎妹妹 | blanc:合作的侦探;miles:要揭穿的人
> 带着一个惊天秘密来到小岛的女人。她和布兰克一起，把玻璃洋葱一层层剥开。
claire | 克莱尔·德贝拉 | Claire Debella | 州长 | Kathryn Hahn | ko2 | #6A6A8A | 混蛋们 | 职位:康涅狄格州州长 | miles:靠山
> 正在竞选参议员的州长，靠迈尔斯的钱维持政治生命。
lionel | 莱昂内尔·图森 | Lionel Toussaint | 首席科学家 | Leslie Odom Jr. | ko2 | #4A5A6A | 混蛋们 | miles:老板
> 阿尔法公司的首席科学家，被迫为迈尔斯的危险项目背书。
birdie | 伯迪·乔 | Birdie Jay | 过气名模 | Kate Hudson | ko2 | #E0A0C0 | 混蛋们 | 特点:总是乱发推特得罪人 | peg:助理
> 过气超模，总在推特上口无遮拦，靠助理收拾烂摊子。
duke | 杜克·科迪 | Duke Cody | 男权主播 | Dave Bautista | ko2 | #4A4A3A | 混蛋们 | 随身:一把枪 | whiskey:女朋友
> 直播男子气概的网红，随身带枪。
whiskey | 威士忌 | Whiskey | 杜克的女朋友 | Madelyn Cline | ko2 | #C8A07A | 混蛋们 | duke:男朋友
> 杜克的女朋友，看起来只是陪衬，其实心里有自己的算盘。
peg | 佩格 | Peg | 伯迪的助理 | Jessica Henwick | ko2 | #6A5A6A | 助理 | birdie:老板
> 伯迪的助理，每天都在帮老板删推特。
derol | 德罗尔 | Derol | 岛上的怪人 | Noah Segan | ko2 | #8A8A6A | 岛民 | 特点:一直在泡澡、一直不说话;趣事:演员也演了第一部的瓦格纳警员
> 一直泡在岛上浴缸里的神秘男子，全片几乎没说话。
phillip | 菲利普 | Phillip | 布兰克的伴侣 | Hugh Grant | ko2 | #8A7A6A | 布兰克的家 | blanc:伴侣
> 布兰克的伴侣，只露了一面——演员是休·格兰特。
jud | 贾德·杜普伦蒂西 | Rev. Jud Duplenticy | 年轻的神父 | Josh O'Connor | ko3 | #4A4A5A | 天主教会 | 过去:当过拳击手 | blanc:合作的侦探;wicks:前辈神父
> 被派到小镇教区的年轻神父，曾经是个拳击手，被卷进了一桩“不可能的谋杀案”。
wicks | 威克斯神父 | Msgr. Jefferson Wicks | 小镇的主教 | Josh Brolin | ko3 | #5A3A3A | 天主教会 | 特点:控制欲极强 | jud:后辈;martha:忠实的追随者
> 掌控着小镇教区的神父，强势、霸道、信众众多。
martha | 玛莎·德拉克鲁瓦 | Martha Delacroix | 虔诚的信徒 | Glenn Close | ko3 | #6A6A6A | 教区 | wicks:追随的神父
> 教区里最虔诚的老信徒，对神父言听计从。
vera | 薇拉·德雷文 | Vera Draven | 律师 | Kerry Washington | ko3 | #6A4A5A | 教区 | cy:养子
> 教区里的律师，有一个想当网红的养子。
cy | 赛·德雷文 | Cy Draven | 想红的年轻人 | Daryl McCormack | ko3 | #5A6A7A | 教区 | vera:养母
> 一心想靠网络走红的年轻人。
nat | 纳特·夏普医生 | Dr. Nat Sharp | 小镇医生 | Jeremy Renner | ko3 | #6A6A5A | 教区
> 小镇上的医生，生活一团糟。
lee | 李·罗斯 | Lee Ross | 畅销书作家 | Andrew Scott | ko3 | #5A5A6A | 教区
> 落魄的畅销书作家，来教区寻找灵感。
geraldine | 杰拉尔丁·斯科特 | Geraldine Scott | 警察局长 | Mila Kunis | ko3 | #6A6A8A | 警察 | blanc:合作的侦探
> 小镇的警察局长，和布兰克一起调查案子。
simone | 西蒙娜·维瓦内 | Simone Vivane | 年轻的大提琴手 | Cailee Spaeny | ko3 | #8A7A8A | 教区 | 职业:大提琴手
> 因病无法演奏的大提琴手，把希望寄托在信仰上。
samson | 参孙·霍尔特 | Samson Holt | 教堂的管理员 | Thomas Haden Church | ko3 | #6A5A4A | 教区
> 沉默寡言的教堂管理员。
"""

DECKS = """
thrombey | 斯龙比一家 | The Thrombeys | 🔪 | harlan linda richard walt joni meg jacob ransom greatnana
disruptors | 玻璃洋葱的“混蛋们” | The Disruptors | 🧅 | miles claire lionel birdie duke whiskey
clients | 布兰克的搭档们 | Blanc's Partners | 🕵 | blanc marta helen jud
parish | 小镇教区 | The Parish | ⛪ | wicks jud martha vera cy nat lee simone samson
help | 身边的人 | The Help | 🧹 | marta peg derol greatnana
"""

RARE = {"UR": "blanc"}
