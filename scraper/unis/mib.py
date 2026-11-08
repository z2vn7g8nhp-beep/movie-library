U = dict(id="mib", n="黑衣人", en="Men in Black", short="MIB",
         tag="他们是你最后的防线，抵御宇宙里的渣滓。看完记得被闪一下。",
         theme=["#3A3A44", "#C9D0D8", "#0A0A0E"], timeline=True, wd=["Q3305670"])
ORDER = 20

WORKS = """
## main | 正传 | Men in Black
mib1 | Men in Black | 1997 | 黑衣人 | tl=1997
mib2 | Men in Black II | 2002 | 黑衣人2 | tl=2002
mib3 | Men in Black 3 | 2012 | 黑衣人3 | tl=1969 tll=穿越回_1969_年
## intl | 全球追缉 | International
mibi | Men in Black: International | 2019 | 黑衣人：全球追缉 | tl=2019
"""

CHARS = """
agent_j | J 探员 | Agent J | 詹姆斯·爱德华兹 | Will Smith | mib1 mib2 mib3 | #3A3A44 | 黑衣人 | 本名:詹姆斯·达瑞尔·爱德华兹三世;出身:纽约警察;武器:“小蟋蟀”（看起来很小，威力很大）;名场面:招聘考试时选择射小女孩蒂芙尼 | agent_k:搭档、像父亲一样的人;agent_k_y:年轻时的搭档;zed:上司;frank:搭档狗狗;agent_o:上司
> 跑得比外星人还快的纽约警察，在一场奇怪的考试后穿上了黑西装。他和 K 一个话痨、一个冷面，是影史最好笑的搭档之一。
agent_k | K 探员 | Agent K | 汤米·李·琼斯版 | Tommy Lee Jones | mib1 mib2 mib3 | #4A4A54 | 黑衣人 | 特点:从不笑、开车超快;退休后:当邮局局长 | agent_j:搭档;agent_k_y:年轻时的自己;zed:老上司;laurel:心动的人;agent_o:旧情
> 面无表情的老探员，带 J 入行。他的神经闪光器闪掉了别人的记忆，也闪掉了自己的很多过去。
agent_k_y | 年轻的 K | Young Agent K | 乔什·布洛林版 · 1969 年 | Josh Brolin | mib3 | #4A4A54 | 黑衣人;1969 年 | 特点:那时候他还会笑 | agent_j:穿越来的搭档;agent_o:当年的心上人;griffin:能看见所有未来的朋友;agent_k:后来的自己
> 1969 年的 K，年轻、能干，那时候他还会笑。乔什·布洛林把汤米·李·琼斯模仿得惟妙惟肖。
zed | Z 局长 | Zed | 黑衣人总部负责人 | Rip Torn | mib1 mib2 | #6A6A6A | 黑衣人;总部 | agent_k:老部下;agent_j:部下
> 黑衣人总部的老局长，戴着耳机，冷静地看着全宇宙的外星人进出地球。
laurel | 劳蕾尔 | Laurel Weaver | 法医 → L 探员 | Linda Fiorentino | mib1 | #6A5A6A | 法医;黑衣人 | agent_k:心动的人;agent_j:搭档
> 停尸房里见过太多怪尸体的法医，最后成了 L 探员。
edgar | 臭虫埃德加 | Edgar the Bug | 套着人皮的巨型臭虫 | Vincent D'Onofrio | mib1 | #6A7A4A | 外星人;臭虫 | 特点:穿着一张不合身的农夫人皮、走路歪歪扭扭;喜欢:糖水
> 把一个农夫“穿”在身上的巨型外星臭虫，走起路来浑身别扭，嘴里还要喝糖水。
frank | 弗兰克 | Frank the Pug | 会说话的哈巴狗 | vo:Tim Blaney | mib1 mib2 | #C9A07A | 外星人;黑衣人 | 物种:伪装成哈巴狗的外星人;爱好:唱《Who Let the Dogs Out》 | agent_j:搭档
> 伪装成哈巴狗的外星人，嘴碎、爱唱歌，还当过 J 的临时搭档。
jeebs | 吉布斯 | Jeebs | 当铺老板 | Tony Shalhoub | mib1 mib2 | #8A7A5A | 外星人 | 特点:脑袋被打爆了还能长回来
> 卖违禁外星武器的当铺老板，脑袋被打掉了还能重新长出来。
worms | 虫虫帮 | The Worms | 爱喝咖啡的外星虫 | - | mib1 mib2 | #C9A040 | 外星人;黑衣人 | 爱好:咖啡、抽烟、看电视
> 住在总部休息室里的一群外星虫，喝咖啡、抽烟、八卦，后来还搬进了 J 的公寓。
serleena | 瑟琳娜 | Serleena | 维多利亚的秘密女模特 | Lara Flynn Boyle | mib2 | #5A3A5A | 外星人 | 真身:一团植物触手;伪装:内衣模特 | scrad:手下
> 伪装成内衣模特的外星植物怪物，来地球寻找一件叫“光芒”的东西。
scrad | 斯克拉德 | Scrad & Charlie | 双头外星人 | Johnny Knoxville | mib2 | #6A6A4A | 外星人 | 特点:一个身体两个脑袋 | serleena:老大
> 一个身体上长着两个脑袋的笨蛋外星人，一个负责犯傻，一个负责更傻。
laura | 劳拉 | Laura Vasquez | 披萨店女孩 | Rosario Dawson | mib2 | #8A5A5A | 披萨店;光芒公主 | 秘密:她自己就是“光芒” | agent_j:心动的人
> 披萨店里的女孩，J 不忍心闪掉她的记忆。她身上藏着整个故事的谜底。
boris | 动物鲍里斯 | Boris the Animal | 越狱的外星杀手 | Jemaine Clement | mib3 | #3A3A3A | 外星人;波格罗迪特人 | 口头禅:叫我鲍里斯就行，不要加“动物”;特点:手掌里会射出寄生虫 | agent_k_y:打断他胳膊的人
> 从月球监狱越狱的外星杀手，最讨厌别人叫他“动物”鲍里斯。
griffin | 格里芬 | Griffin | 能看见所有未来的外星人 | Michael Stuhlbarg | mib3 | #8A8AA0 | 外星人;阿卡迪亚人 | 能力:同时看见所有可能的未来 | agent_k_y:朋友
> 能同时看见所有可能未来的外星人，说话温柔又迷糊，是整部电影最温暖的角色。
agent_o | O 探员 | Agent O | 黑衣人局长 | Emma Thompson; Alice Eve | mib3 mibi | #6A6A8A | 黑衣人;局长 | agent_k:旧情;agent_m:招募的新人
> 继 Z 之后的黑衣人局长。年轻时，她和 K 之间有过一段说不清的心动。
agent_m | M 探员 | Agent M | 莫莉 | Tessa Thompson | mibi | #4A4A6A | 黑衣人;伦敦分部 | 本名:莫莉;来历:小时候亲眼见过黑衣人，没被闪掉记忆，花了二十年找上门 | agent_h:搭档;pawny:跟班;agent_o:招募她的人
> 小时候目睹黑衣人行动、没被闪掉记忆的女孩，长大后自己找上了门。
agent_h | H 探员 | Agent H | 伦敦分部的王牌 | Chris Hemsworth | mibi | #5A5A6A | 黑衣人;伦敦分部 | 特点:帅、运气好、有点自大 | agent_m:搭档;hight:导师;riza:前女友
> 伦敦分部最受欢迎的王牌探员，帅气、自信，最近却越来越不靠谱。
hight | 高 T | High T | 伦敦分部负责人 | Liam Neeson | mibi | #4A4A4A | 黑衣人;伦敦分部 | agent_h:得意门生
> 伦敦分部的负责人，当年和 H 一起在埃菲尔铁塔上击退了外星入侵。
pawny | 小兵 | Pawny | 袖珍外星战士 | vo:Kumail Nanjiani | mibi | #8A8A6A | 外星人 | 自称:M 的忠实仆人 | agent_m:效忠的女王
> 只有巴掌大的外星小兵，自称是 M 的忠诚骑士，嘴特别碎。
riza | 莉莎 | Riza | 星际军火商 | Rebecca Ferguson | mibi | #6A4A6A | 外星军火商 | 特点:有三条胳膊 | agent_h:前男友
> 三条胳膊的星际军火商，H 的前女友。
twins | 孪生外星人 | The Twins | 外星杀手兄弟 | Larry Bourgeois; Laurent Bourgeois | mibi | #8A8AA0 | 外星人;海弗 | 能力:化成能量体
> 一对穿着一样、动作同步的外星杀手兄弟，演员是现实中的街舞双胞胎。
"""

DECKS = """
partners | 搭档 | J & K | 🕶 | agent_j agent_k
time | 1969 | Back to 1969 | 🚀 | agent_j agent_k_y griffin boris agent_o
hq | 黑衣人总部 | MIB HQ | 🏢 | zed agent_k agent_j laurel frank worms
aliens | 外星访客 | Visitors | 👽 | edgar serleena scrad jeebs boris griffin pawny riza twins
london | 伦敦分部 | MIB London | 🇬🇧 | agent_m agent_h hight agent_o pawny
ks | 两代 K 探员 | Two Ks | ⏳ | agent_k agent_k_y
"""

RARE = {"UR": "agent_j agent_k"}
