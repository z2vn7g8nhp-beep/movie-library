U = dict(id="toys", n="玩具总动员", en="Toy Story", short="TOY STORY",
         tag="你有一个好朋友。从安迪的房间，到邦妮的书包，玩具们最怕的是被忘记。",
         theme=["#3E7AC8", "#F0C850", "#14202E"], wd=["Q2316015"])
ORDER = 22

WORKS = """
## main | 正传 | Toy Story
ts1 | Toy Story | 1995 | 玩具总动员
ts2 | Toy Story 2 | 1999 | 玩具总动员2
ts3 | Toy Story 3 | 2010 | 玩具总动员3
ts4 | Toy Story 4 | 2019 | 玩具总动员4
ts5 | Toy Story 5 | 2026 | 玩具总动员5
## spin | 外传 | Spin-off
ly | Lightyear | 2022 | 光年正传 | x
"""

CHARS = """
woody | 胡迪 | Woody | 牛仔警长 | vo:Tom Hanks | ts1 ts2 ts3 ts4 ts5 | #C9902E | 安迪的玩具;胡迪综合秀 | 身份:20 世纪 50 年代的牛仔玩偶;口头禅:我的靴子里有条蛇！;拉线语音:你是我最好的朋友;靴底:写着 ANDY | buzz:最好的朋友;andy:主人;bo:心上人;jessie:同一部动画里的伙伴;forky:负责照顾的新玩具;bonnie:后来的主人
> 安迪最爱的玩具，玩具们的主心骨。他最怕被替代、被遗忘，却一次又一次地把别人的“孩子”放在了自己前面。
buzz | 巴斯光年 | Buzz Lightyear | 太空骑警 | vo:Tim Allen | ts1 ts2 ts3 ts4 ts5 | #6AAA3A | 安迪的玩具;星际联盟（他以为的） | 口头禅:飞向宇宙，浩瀚无垠！;装备:激光（其实是个小灯）、可展开的翅膀;西班牙模式:第三部里被调成了 | woody:最好的朋友;jessie:心动的人;zurg:宿敌（他坚信的）;buzz_ly:电影里的原型
> 一开始坚信自己是真正太空骑警的玩具，直到在电视里看到自己的广告。从那以后，他学会了“优雅地坠落”。
jessie | 翠丝 | Jessie | 牛仔女孩 | vo:Joan Cusack | ts2 ts3 ts4 ts5 | #C83A3A | 胡迪综合秀;安迪的玩具 | 往事:被前主人艾米丽送走（《当她爱我时》）;口头禅:耶——哈！;最怕:被关进黑暗的箱子 | woody:胡迪综合秀的伙伴;bullseye:搭档;buzz:心动的人;pete:骗了她的人
> 红头发的牛仔女孩，元气满满。她曾被最爱的小主人送走，那首《当她爱我时》让无数人哭了。
bullseye | 红心 | Bullseye | 胡迪的马 | - | ts2 ts3 ts4 ts5 | #8A5A3A | 胡迪综合秀 | 特点:不会说话，开心了就舔人 | woody:主人;jessie:伙伴
> 胡迪的小马，不会说话，开心了就会像小狗一样舔人。
rex | 抱抱龙 | Rex | 胆小的霸王龙 | vo:Wallace Shawn | ts1 ts2 ts3 ts4 ts5 | #6AAA4A | 安迪的玩具 | 烦恼:手太短、怕自己不够吓人;特长:打电子游戏
> 一只总担心自己不够吓人的霸王龙玩具，胆子特别小。
hamm | 火腿 | Hamm | 小猪存钱罐 | vo:John Ratzenberger | ts1 ts2 ts3 ts4 ts5 | #E08AA0 | 安迪的玩具 | 特点:毒舌、爱看电视;假身份:邪恶的猪博士
> 爱吐槽的小猪存钱罐，肚子里有几枚硬币。
slinky | 弹簧狗 | Slinky Dog | 弹簧狗 | vo:Jim Varney; Blake Clark | ts1 ts2 ts3 ts4 ts5 | #C9903A | 安迪的玩具 | 特点:身子是弹簧，能拉很长;口音:南方腔
> 身体是一根弹簧的腊肠狗，忠心耿耿，关键时刻能伸长了救人。
potato | 蛋头先生 | Mr. Potato Head | 土豆头 | vo:Don Rickles | ts1 ts2 ts3 ts4 | #C9803A | 安迪的玩具 | 特点:五官能拆下来;脾气:暴躁 | mrspotato:妻子
> 五官可以随便拆装的土豆头，脾气暴躁，最疼老婆。
mrspotato | 蛋头太太 | Mrs. Potato Head | 土豆头太太 | vo:Estelle Harris | ts2 ts3 ts4 | #E09A6A | 安迪的玩具 | potato:丈夫
> 蛋头先生的太太，一只眼睛落在了安迪家，能看到远处发生的事。
bo | 牧羊女 | Bo Peep | 瓷娃娃牧羊女 | vo:Annie Potts | ts1 ts2 ts4 ts5 | #E0A0C0 | 安迪的玩具→无主玩具 | 武器:牧羊杖;伙伴:三头羊;后来:独自在外闯荡的“无主玩具” | woody:心上人;giggle:最好的朋友
> 原本住在台灯上的瓷娃娃，后来成了独自闯荡世界的“无主玩具”。她教会了胡迪，玩具也可以有另一种活法。
aliens | 三眼仔 | The Aliens | 抓娃娃机里的小外星人 | vo:Jeff Pidgeon | ts1 ts2 ts3 ts4 | #6ACA5A | 抓娃娃机 | 口头禅:爪子……;信仰:天上的爪子会选中我们 | potato:他们的“爸爸”
> 抓娃娃机里的三眼小绿人，崇拜那只“伟大的爪子”。
sarge | 军官 | Sarge | 绿色小兵队长 | vo:R. Lee Ermey | ts1 ts2 ts3 | #4A6A3A | 安迪的玩具 | 部队:一桶绿色塑料小兵
> 一桶塑料小兵的队长，执行侦察任务一丝不苟。
andy | 安迪 | Andy Davis | 玩具们的主人 | vo:John Morris | ts1 ts2 ts3 ts4 | #6A8AC0 | 人类 | 最爱:胡迪、巴斯;第三部:要去上大学了 | woody:最爱的玩具;buzz:最爱的玩具;bonnie:把玩具送给的女孩
> 玩具们的主人。第三部里他长大了，把胡迪交给邦妮时说的那段话，是整个系列最温柔的告别。
sid | 阿薯 | Sid Phillips | 隔壁的熊孩子 | vo:Erik von Detten | ts1 ts3 | #6A4A4A | 人类 | 爱好:拆玩具、拼怪玩具;后来:当了垃圾车司机（第三部彩蛋） | woody:吓坏他的玩具
> 住在隔壁、专门拆玩具做实验的熊孩子，最后被玩具们吓坏了。
pete | 臭皮老头 | Stinky Pete | 胡迪综合秀的探矿老头 | vo:Kelsey Grammer | ts2 | #8A7A5A | 胡迪综合秀 | 状态:从没被拆封过;梦想:进博物馆 | woody:想留住的人;jessie:骗了的人
> 一直没被拆封的探矿老头玩偶，看起来慈祥，其实一心想进博物馆，不惜让胡迪永远留下。
zurg | 札克大王 | Emperor Zurg | 巴斯的宿敌 | vo:Andrew Stanton | ts2 | #6A3A8A | 星际反派玩具 | 名台词:我是你父亲 | buzz:宿敌
> 巴斯的宿敌，在电梯里说出了那句“我是你父亲”。
al | 阿尔 | Al McWhiggin | 玩具店老板 | vo:Wayne Knight | ts2 | #8A6A4A | 人类 | 职业:“阿尔的玩具谷仓”老板;执念:把胡迪卖给日本博物馆
> 偷走胡迪的玩具店老板，打算把整套胡迪综合秀卖到日本。
wheezy | 吱吱 | Wheezy | 坏了喇叭的企鹅 | vo:Joe Ranft | ts2 ts4 | #4A4A6A | 安迪的玩具 | 特点:发声器坏了;名场面:修好后唱《你有一个好朋友》
> 发声器坏了被放在架子上的小企鹅，修好后唱了一首《你有一个好朋友》。
lotso | 勒索熊 | Lotso | 草莓味的熊 | vo:Ned Beatty | ts3 | #E07AA0 | 阳光幼儿园 | 特点:身上有草莓味;往事:被主人弄丢后又被替代 | bigbaby:手下;ken:手下
> 身上有草莓香味的粉色熊，阳光幼儿园的“老大”。他曾经被主人遗忘、被替代，于是不再相信任何人。
ken | 肯 | Ken | 时尚达人 | vo:Michael Keaton | ts3 | #6AAAD0 | 阳光幼儿园 | 最爱:衣服、芭比;名场面:一套套换衣服的时装秀 | barbie:一见钟情;lotso:老大
> 衣橱里有一百套衣服的肯，和芭比一见钟情。
barbie | 芭比 | Barbie | 芭比 | vo:Jodi Benson | ts2 ts3 | #E07AB0 | 安迪的玩具 | ken:男朋友
> 安迪妹妹的芭比，在第三部里和肯谈起了恋爱，还用一场“审问”把他拿下了。
bigbaby | 大宝宝 | Big Baby | 阳光幼儿园的大娃娃 | - | ts3 | #C8A08A | 阳光幼儿园 | 特点:一只眼睛半闭着
> 一只眼睛半闭的大娃娃，是勒索熊的打手，心里一直想念着从前的主人。
pricklepants | 刺刺裤先生 | Mr. Pricklepants | 爱演戏的刺猬 | vo:Timothy Dalton | ts3 ts4 | #8A6A4A | 邦妮的玩具 | 爱好:莎士比亚、即兴戏剧
> 穿着小皮裤、满口莎士比亚的刺猬，邦妮家的“戏剧大师”。
trixie | 翠克西 | Trixie | 三角龙 | vo:Kristen Schaal | ts3 ts4 | #6A8ADA | 邦妮的玩具 | 爱好:电脑游戏
> 邦妮家的蓝色三角龙，热爱电脑游戏。
dolly | 多莉 | Dolly | 邦妮的玩具管家 | vo:Bonnie Hunt | ts3 ts4 | #A06AA0 | 邦妮的玩具 | 职责:邦妮家玩具的领导
> 邦妮家的布娃娃，管着家里的所有玩具。
bonnie | 邦妮 | Bonnie Anderson | 新的小主人 | vo:Emily Hahn; Madeleine McGraw | ts3 ts4 ts5 | #E08A6A | 人类 | 作品:用一把叉子做出了叉叉 | woody:后来最喜欢的玩具之一;forky:亲手做的玩具;andy:把玩具交给她的人
> 安迪把玩具们交给的小女孩，想象力满满，用一把一次性叉子做出了叉叉。
forky | 叉叉 | Forky | 叉子做的玩具 | vo:Tony Hale | ts4 ts5 | #E0E0E0 | 邦妮的玩具 | 原材料:一次性叉勺、毛根、冰棒棍;口头禅:我是垃圾！ | bonnie:做他的人;woody:负责照顾他的人
> 一把被邦妮做成玩具的一次性叉勺，坚信自己是垃圾，一有机会就往垃圾桶里跳。
duke | 公爵卡布恩 | Duke Caboom | 加拿大特技摩托手 | vo:Keanu Reeves | ts4 ts5 | #E0E0E0 | 无主玩具 | 招牌:摆姿势;心结:没能像广告里那样飞跃
> 加拿大最伟大的特技摩托手（玩具），一说话就摆姿势。他的心结是：没能像广告里那样飞起来。
gabby | 嘉比嘉比 | Gabby Gabby | 古董店的娃娃 | vo:Christina Hendricks | ts4 | #E0A0A0 | 古董店 | 心愿:被一个孩子爱;缺陷:发声器坏了 | woody:她想要的发声器;bensons:手下的木偶
> 古董店里一直没被爱过的娃娃，发声器是坏的。她想要的只是一个孩子。
ducky | 达奇和兔兔 | Ducky & Bunny | 游乐场奖品 | vo:Keegan-Michael Key; Jordan Peele | ts4 | #E0D06A | 游乐场 | 特点:嘴上说要用眼神杀死你
> 游乐场里一直没被赢走的毛绒奖品，嘴上狠，心里怂。
giggle | 嘻嘻·麦克丁波斯 | Giggle McDimples | 迷你女警 | vo:Ally Maki | ts4 | #6A8AE0 | 无主玩具 | 身高:一厘米多一点 | bo:最好的朋友
> 只有手指头大的迷你女警，是牧羊女最好的朋友。
bensons | 本森木偶 | The Bensons | 腹语木偶 | - | ts4 | #6A5A4A | 古董店 | gabby:主人
> 嘉比嘉比手下的腹语木偶，一言不发，走路吓人。
lilypad | 莉莉帕 | Lilypad | 平板电脑 | vo:Greta Lee | ts5 | #6ACAAA | 科技产品 | 身份:玩具们最大的对手——电子产品
> 第五部的新对手：一台平板电脑。玩具们第一次要和屏幕争夺孩子的注意力。
buzz_ly | 巴斯光年 | Buzz Lightyear | 《光年正传》里的真·太空骑警 | vo:Chris Evans | ly | #6AAA3A | 星际联盟 | 设定:安迪 1995 年看的那部电影里的主角 | izzy:搭档;sox:机器猫;zurg_ly:宿敌;buzz:电影里的玩具原型
> 安迪当年看的那部电影里的主角——真正的太空骑警巴斯。一次失误让一整船人困在了外星球。
izzy | 伊奇·霍索恩 | Izzy Hawthorne | 新手队员 | vo:Keke Palmer | ly | #6A5A8A | 星际联盟 | 祖母:巴斯的搭档艾丽莎 | buzz_ly:搭档
> 巴斯老搭档的孙女，一心想当太空骑警，却害怕太空。
sox | 索克斯 | Sox | 机器猫 | vo:Peter Sohn | ly | #C9A07A | 机器宠物 | 特长:计算、修东西、催眠飞镖;口头禅:嗨，我是索克斯 | buzz_ly:主人
> 给巴斯做伴的机器猫，会算燃料、会修飞船，还会发射催眠飞镖。电影最大的明星。
alisha | 艾丽莎·霍索恩 | Alisha Hawthorne | 巴斯的老搭档 | vo:Uzo Aduba | ly | #6A6A8A | 星际联盟 | 口头禅:飞向宇宙，浩瀚无垠 | buzz_ly:搭档;izzy:孙女
> 巴斯最好的搭档，在巴斯每一次超光速试飞的间隙，过完了自己的一生。
zurg_ly | 札克 | Zurg | 《光年正传》版 | vo:James Brolin | ly | #6A3A8A | 机器人大军 | 秘密:他的真实身份 | buzz_ly:宿敌
> 带着机器人大军出现的札克，他的身份是整部电影最大的反转。
"""

DECKS = """
andy | 安迪的玩具 | Andy's Toys | 🧸 | woody buzz rex hamm slinky potato mrspotato bo sarge
roundup | 胡迪综合秀 | Woody's Roundup | 🤠 | woody jessie bullseye pete
besties | 最好的朋友 | You've Got a Friend | 🚀 | woody buzz
sunnyside | 阳光幼儿园 | Sunnyside Daycare | 🍓 | lotso ken bigbaby barbie
bonnie | 邦妮的玩具 | Bonnie's Toys | 🎒 | forky dolly pricklepants trixie bonnie
antique | 古董店与游乐场 | Second Chance Antiques | 🎡 | gabby bensons duke ducky giggle bo
kids | 孩子们 | The Kids | 🧒 | andy sid bonnie
lightyear | 光年正传 | Lightyear | 🐈 | buzz_ly izzy sox alisha zurg_ly
buzzes | 两个巴斯 | Two Buzzes | ✨ | buzz buzz_ly
villains | 反派们 | Villains | 😈 | pete zurg al lotso gabby lilypad
"""

RARE = {"UR": "woody buzz jessie"}
