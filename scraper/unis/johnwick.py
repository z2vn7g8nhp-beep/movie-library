U = dict(id="wick", n="疾速追杀", en="John Wick", short="WICK",
         tag="人们不停地问我是不是回来了……是的，我回来了。大陆酒店、高桌会和一只小狗引发的一切。",
         theme=["#B8902E", "#D8D0C0", "#0C0A0A"], timeline=True, wd=["Q106544377"])
ORDER = 21

WORKS = """
## main | 正传 | John Wick
jw1 | John Wick | 2014 | 疾速追杀 | tl=1 tll=第一章
jw2 | John Wick: Chapter 2 | 2017 | 疾速追杀2 | tl=2 tll=第二章·紧接上一部
jw3 | John Wick: Chapter 3 - Parabellum | 2019 | 疾速追杀3 | tl=3 tll=第三章·一小时后
jw4 | John Wick: Chapter 4 | 2023 | 疾速追杀4 | tl=4 tll=第四章
## world | 疾速追杀的世界 | From the World of John Wick
ballerina | Ballerina | 2025 | 疾速追杀：芭蕾杀姬 | x tl=3.5 tll=第三章与第四章之间
continental | The Continental | 2023 | 大陆酒店 | ty=ms x tl=0 tll=1975_年·纽约
"""

CHARS = """
john | 约翰·威克 | John Wick | 疾速追杀 · 巴巴亚嘎 | Keanu Reeves | jw1 jw2 jw3 jw4 ballerina | #2A2A2E | 前杀手;罗斯卡罗马 | 外号:巴巴亚嘎（俄罗斯童话里的女巫，其实他是“去杀巴巴亚嘎的人”）;出身:白俄罗斯，本名贾丁·约维诺维奇;传说:用一支铅笔干掉了三个人;最爱:亡妻、小狗、那辆 1969 年的野马 | helen:亡妻;daisy:亡妻留下的小狗;dog:后来的狗;winston:老朋友;charon:最尊重的人;caine:老友与对手;sofia:欠他人情的人;viggo:旧老板
> 一个为了爱情金盆洗手的传奇杀手。妻子病逝后，她留下的小狗被人杀了——于是整个地下世界都知道，约翰·威克回来了。
helen | 海伦 | Helen Wick | 约翰的妻子 | Bridget Moynahan | jw1 jw2 jw4 | #C8B8A0 | 平民 | 留下的:一只小狗、一段录像 | john:丈夫;daisy:送给约翰的小狗
> 让约翰放下枪的女人。她病逝前，给他订了一只小狗，让他不至于一个人。
daisy | 黛西 | Daisy | 海伦送的小猎犬 | - | jw1 | #C9A07A | 狗狗 | 品种:比格犬 | john:主人;helen:送它的人
> 海伦留给约翰的小比格犬，带着一张卡片来到他身边。它是整个系列的起点。
dog | 比特犬 | The Dog | 约翰的新伙伴 | - | jw1 jw2 jw3 jw4 | #8A7A6A | 狗狗 | 品种:比特犬;来历:约翰从宠物医院领走的 | john:主人
> 第一部结尾约翰从宠物医院带走的比特犬，后来跟着他跑遍了整个系列。没有名字，但全世界都在担心它的安危。
winston | 温斯顿 | Winston Scott | 纽约大陆酒店经理 | Ian McShane | jw1 jw2 jw3 jw4 ballerina | #5A4A3A | 大陆酒店 | 规则:在大陆酒店里不准做“生意”;口头禅:乔纳森 | john:老朋友;charon:最信任的左右手;winston_y:年轻时的自己;adjudicator:与之周旋的人
> 纽约大陆酒店的经理，优雅、老辣，总叫约翰“乔纳森”。他和约翰之间是友谊，也是生意。
charon | 卡戎 | Charon | 大陆酒店礼宾 | Lance Reddick | jw1 jw2 jw3 jw4 ballerina | #3A3A4A | 大陆酒店 | 职位:礼宾;特点:永远彬彬有礼、关键时刻举枪就打 | winston:老板;john:最尊重的客人;charon_y:年轻时的自己
> 大陆酒店永远彬彬有礼的礼宾，约翰最尊重的人之一。演员兰斯·瑞迪克在第四部上映前离世，这是他最后的角色之一。
bowery | 鲍厄里国王 | The Bowery King | 地下情报网之王 | Laurence Fishburne | jw2 jw3 jw4 | #6A5A4A | 地下世界 | 手下:伪装成流浪汉的情报网;宠物:鸽子 | john:帮过他的人
> 统治纽约地下流浪汉情报网的国王，养着一屋子鸽子。演员和基努·里维斯在《黑客帝国》里是一对。
viggo | 维戈·塔拉索夫 | Viggo Tarasov | 俄罗斯黑帮老大 | Michael Nyqvist | jw1 | #4A4A4A | 塔拉索夫家族 | 名台词:约翰不是巴巴亚嘎，他是你派去杀巴巴亚嘎的人 | iosef:不争气的儿子;john:旧部下
> 约翰的前老板，知道儿子惹了谁之后，第一反应是“哦”。
iosef | 约瑟夫 | Iosef Tarasov | 维戈的儿子 | Alfie Allen | jw1 | #6A6A6A | 塔拉索夫家族 | 惹的祸:偷了约翰的车、杀了他的狗 | viggo:父亲
> 偷车杀狗的黑帮少爷，他不知道自己惹的是谁。演员是《权力的游戏》里的席恩。
marcus | 马库斯 | Marcus | 老狙击手 | Willem Dafoe | jw1 | #6A6A5A | 杀手 | john:暗中守护的老朋友
> 约翰的老朋友，接下了杀他的悬赏，却一直在暗中保护他。
perkins | 珀金斯 | Ms. Perkins | 违规的女杀手 | Adrianne Palicki | jw1 | #5A3A4A | 杀手 | 违反:大陆酒店规则
> 在大陆酒店里动手的女杀手，坏了规矩。
aurelio | 奥雷里奥 | Aurelio | 修车铺老板 | John Leguizamo | jw1 jw2 | #6A5A3A | 地下世界 | john:老朋友
> 修车铺老板，一眼认出被偷的野马是约翰的，当场揍了约瑟夫。
santino | 桑蒂诺 | Santino D'Antonio | 意大利黑手党 | Riccardo Scamarcio | jw2 | #4A3A3A | 卡莫拉;高桌会 | 手里:约翰的血誓章 | ares:保镖;john:被他逼着还人情的人
> 拿着约翰欠下的“血誓章”上门讨债的意大利黑帮少爷。
ares | 阿瑞斯 | Ares | 手语保镖 | Ruby Rose | jw2 | #5A5A6A | 杀手 | 特点:只用手语交流 | santino:效忠的老板
> 桑蒂诺的哑巴保镖，只用手语说话，冷酷利落。
cassian | 卡西安 | Cassian | 保镖 | Common | jw2 | #4A4A5A | 杀手 | 名场面:和约翰在台阶上一路打下去 | john:不打不相识
> 被约翰杀了雇主的保镖，两人从楼梯打到地铁。
sofia | 索菲亚 | Sofia Al-Azwar | 卡萨布兰卡大陆酒店经理 | Halle Berry | jw3 | #6A4A3A | 大陆酒店 | 伙伴:两只比利时马犬;欠约翰:一枚血誓章 | john:欠他人情的人;sofiadogs:她的狗狗
> 卡萨布兰卡大陆酒店的经理，带着两只训练有素的比利时马犬，和约翰一起杀出了重围。
sofiadogs | 马犬双子 | Sofia's Dogs | 索菲亚的比利时马犬 | - | jw3 | #8A6A4A | 狗狗 | 品种:比利时马犬;特长:精准咬住敌人的要害 | sofia:主人
> 索菲亚的两只比利时马犬，一个手势就能扑倒一屋子敌人。整部第三部最受欢迎的角色。
adjudicator | 仲裁人 | The Adjudicator | 高桌会的代表 | Asia Kate Dillon | jw3 | #6A6A7A | 高桌会 | 职责:惩罚违反规则的人
> 高桌会派来的仲裁人，冷静地审判每一个帮过约翰的人。
zero | 零 | Zero | 寿司店主兼杀手 | Mark Dacascos | jw3 | #5A5A5A | 杀手 | 特点:约翰的头号粉丝 | john:最崇拜的人，也是要杀的人
> 白天做寿司、晚上杀人的杀手头子，见到约翰激动得像个粉丝。
director | 导演 | The Director | 罗斯卡罗马的首领 | Anjelica Huston | jw3 ballerina | #5A3A5A | 罗斯卡罗马 | 身份:芭蕾舞团兼杀手学校的主人 | john:她养大的孩子;eve:她的学生
> 罗斯卡罗马的女首领，在剧院里训练芭蕾舞者，也训练杀手。约翰就是在这里长大的。
elder | 长老 | The Elder | 高桌会之上的人 | Saïd Taghmaoui | jw3 | #8A7A5A | 高桌会 | 住处:撒哈拉沙漠深处
> 高桌会之上的人，住在沙漠深处。约翰为了见他，在沙漠里走到快死。
caine | 凯恩 | Caine | 盲人杀手 | Donnie Yen | jw4 | #5A5A6A | 杀手;高桌会 | 特点:双目失明、用手杖剑、门上挂铃铛;牵挂:女儿 | john:老友与对手;marquis:逼他出手的人
> 甄子丹饰演的盲人杀手，约翰的老朋友。他被高桌会拿女儿要挟，只能接下杀约翰的任务。
marquis | 格拉蒙侯爵 | Marquis de Gramont | 高桌会的新贵 | Bill Skarsgård | jw4 | #6A5A6A | 高桌会 | 风格:法式奢华、残忍 | caine:利用的人;john:决斗对手
> 傲慢的法国侯爵，代表高桌会追杀约翰，最后和约翰在圣心堂前决斗。
koji | 岛津浩二 | Koji Shimazu | 大阪大陆酒店经理 | Hiroyuki Sanada | jw4 | #4A4A4A | 大陆酒店 | john:老朋友;akira:女儿;caine:老朋友
> 大阪大陆酒店的经理，为了朋友不惜关上酒店大门。
akira | 明 | Akira | 浩二的女儿 | Rina Sawayama | jw4 | #8A3A5A | 大陆酒店 | 武器:弓、刀 | koji:父亲
> 浩二的女儿，大阪大陆酒店的礼宾，弓刀双绝。
killa | 基拉 | Killa | 柏林黑帮老大 | Scott Adkins | jw4 | #6A6A4A | 地下世界 | 造型:胖、金牙、戴假体
> 柏林地下世界的胖老大，约翰在赌桌上和他赌命。
tracker | 无名氏 | Mr. Nobody | 带狗的赏金猎人 | Shamier Anderson | jw4 | #6A5A3A | 赏金猎人 | 伙伴:一只比利时马犬 | john:悬赏目标
> 牵着一只马犬的赏金猎人，一直在等约翰的悬赏涨到“值得出手”。
eve | 伊芙·马卡罗 | Eve Macarro | 芭蕾杀姬 | Ana de Armas | ballerina | #A06A7A | 罗斯卡罗马 | 训练:芭蕾 + 杀手;动机:为父报仇 | director:老师;john:传说中的人
> 罗斯卡罗马培养出来的芭蕾舞者兼杀手，为了给父亲报仇踏进了约翰的世界。
pine | 丹尼尔·派恩 | Daniel Pine | 逃离邪教的男人 | Norman Reedus | ballerina | #5A5A4A | 平民 | eve:并肩作战
> 想带女儿逃离邪教的父亲。
chancellor | 大臣 | The Chancellor | 杀手邪教的首领 | Gabriel Byrne | ballerina | #4A3A3A | 邪教 | eve:复仇对象
> 一个隐藏在小镇里的杀手邪教首领，伊芙的杀父仇人。
winston_y | 温斯顿 | Winston Scott | 年轻的温斯顿 | Colin Woodell | continental | #5A4A3A | 1975 年 | winston:后来的自己;charon_y:伙伴;cormac:死对头
> 1975 年的温斯顿，还是个在伦敦混日子的年轻人，被迫回到纽约面对大陆酒店的主人。
charon_y | 卡戎 | Charon | 年轻的卡戎 | Ayomide Adegun | continental | #3A3A4A | 1975 年;大陆酒店 | charon:后来的自己;winston_y:伙伴
> 年轻时的卡戎，那时候他还是大陆酒店的门童。
cormac | 科马克 | Cormac O'Connor | 大陆酒店的前主人 | Mel Gibson | continental | #4A4A3A | 1975 年;大陆酒店 | winston_y:死对头
> 七十年代掌控纽约大陆酒店的暴君。
"""

DECKS = """
continental | 大陆酒店 | The Continental | 🏨 | winston charon john koji akira sofia
hightable | 高桌会 | The High Table | 🪙 | adjudicator elder marquis santino winston
dogs | 狗狗们 | The Good Dogs | 🐶 | daisy dog sofiadogs
ruska | 罗斯卡罗马 | Ruska Roma | 🩰 | director john eve
tarasov | 塔拉索夫家族 | The Tarasovs | 🚗 | viggo iosef marcus perkins aurelio
assassins | 杀手同行 | Fellow Assassins | 🗡 | caine tracker zero ares cassian killa
friends | 约翰的老朋友们 | Old Friends | 🤝 | winston charon bowery marcus aurelio sofia caine koji
seventies | 1975 | The Continental 1975 | 🕺 | winston_y charon_y cormac
winstons | 两代温斯顿 | Two Winstons | 🥃 | winston_y winston
charons | 两代卡戎 | Two Charons | 🛎 | charon_y charon
"""

RARE = {"UR": "john winston charon"}
