U = dict(id="days28", n="惊变28天", en="28 Days Later", short="RAGE",
         tag="狂暴病毒爆发后的 28 天、28 周、28 年。英国被封锁，活下来的人各有各的疯狂。",
         theme=["#B8302E", "#C8C8B8", "#0E0E0C"], timeline=True, wd=["Q125679809"])
ORDER = 27

WORKS = """
## main | 系列 | The Rage Saga
d28 | 28 Days Later | 2002 | 惊变28天 | tl=0.08 tll=爆发后第_28_天
w28 | 28 Weeks Later | 2007 | 惊变28周 | tl=0.5 tll=爆发后第_28_周
y28 | 28 Years Later | 2025 | 惊变28年 | tl=28 tll=爆发后第_28_年
bt | 28 Years Later: The Bone Temple | 2026 | 28年后：人骨圣殿 | tl=28.2 tll=第_28_年·紧接上一部
"""

CHARS = """
jim | 吉姆 | Jim | 在医院醒来的快递员 | Cillian Murphy | d28 bt | #6A6A6A | 幸存者 | 职业:自行车快递员;名场面:独自走过空无一人的伦敦 | selena:并肩求生的人;frank:收留他的大叔;hannah:像妹妹一样
> 车祸昏迷了 28 天，醒来时整个伦敦已经空无一人。他穿着病号服走过威斯敏斯特桥的画面，是丧尸电影史上最经典的开场之一。
selena | 赛琳娜 | Selena | 果断的幸存者 | Naomie Harris | d28 | #4A4A5A | 幸存者 | 武器:砍刀;信条:有人被感染，就要在二十秒内动手 | jim:并肩求生的人;hannah:想保护的女孩
> 冷静、果断的幸存者，砍刀从不犹豫。可在冷硬的外表下，她最后还是选择了相信别人。
frank | 弗兰克 | Frank | 出租车司机 | Brendan Gleeson | d28 | #8A6A4A | 幸存者 | 座驾:黑色出租车;最爱:女儿汉娜 | hannah:女儿;jim:收留的人
> 带着女儿守在公寓里的出租车司机，乐观、温暖，带着大家开往曼彻斯特。
hannah | 汉娜 | Hannah | 弗兰克的女儿 | Megan Burns | d28 | #A08A7A | 幸存者 | frank:父亲;selena:保护她的人
> 弗兰克的女儿，在末世里努力保持天真的少女。
west | 韦斯特少校 | Major Henry West | 军营指挥官 | Christopher Eccleston | d28 | #4A5A4A | 军方 | 计划:让士兵们“有女人” | jim:对手
> 驻守曼彻斯特郊外的少校，他的“救援”比感染者更可怕。
don | 唐 | Don | 抛下妻子的丈夫 | Robert Carlyle | w28 | #6A5A4A | 幸存者 | 往事:在感染者冲进来时独自逃跑 | alice:妻子;tammy:女儿;andy:儿子
> 在感染者冲进屋时丢下妻子独自逃走的男人，这个选择追着他走完了整部电影。
alice | 爱丽丝 | Alice | 携带病毒却不发病的人 | Catherine McCormack | w28 | #8A7A8A | 幸存者 | 秘密:她对病毒免疫，但能传染 | don:丈夫
> 被丈夫抛下的妻子，奇迹般活了下来——她体内带着病毒，却不会发病。
tammy | 塔米 | Tammy | 姐姐 | Imogen Poots | w28 | #A08A6A | 幸存者 | andy:弟弟
> 回到伦敦的姐姐，带着弟弟偷偷溜出了安全区。
andy | 安迪 | Andy | 弟弟 | Mackintosh Muggleton | w28 | #6A8AA0 | 幸存者 | 特点:一只蓝眼一只棕眼 | tammy:姐姐
> 和妈妈一样一只蓝眼、一只棕眼的男孩，身上也许有治愈的希望。
doyle | 多伊尔 | Doyle | 美军狙击手 | Jeremy Renner | w28 | #4A5A6A | 美军 | scarlet:并肩作战;tammy:保护的孩子
> 违抗命令保护孩子们的美军狙击手。
scarlet | 斯嘉丽 | Scarlet | 军医 | Rose Byrne | w28 | #6A6A8A | 美军 | doyle:并肩作战
> 发现了孩子们身上秘密的军医。
spike | 斯派克 | Spike | 岛上的十二岁男孩 | Alfie Williams | y28 bt | #6A7A5A | 霍利岛 | 成长:第一次跟着父亲去大陆狩猎;心愿:找人救妈妈 | jamie:父亲;isla:母亲;kelson:找到的医生;jimmy:遇见的“吉米”
> 在与世隔绝的海岛上长大的男孩，第一次跟父亲跨过堤道踏上大陆。为了救病重的母亲，他独自带着她回到了那片土地。
jamie | 杰米 | Jamie | 斯派克的父亲 | Aaron Taylor-Johnson | y28 | #5A5A4A | 霍利岛 | 武器:弓箭 | spike:儿子;isla:妻子
> 岛上的猎人，带儿子去大陆完成“成人礼”。
isla | 艾拉 | Isla | 斯派克的母亲 | Jodie Comer | y28 | #8A7A7A | 霍利岛 | 状态:病重、意识时而混乱 | spike:儿子;jamie:丈夫
> 斯派克病重的母亲，时而清醒、时而恍惚，却从未停止爱她的儿子。
kelson | 凯尔森医生 | Dr. Ian Kelson | 人骨圣殿的主人 | Ralph Fiennes | y28 bt | #C8A87A | 大陆 | 作品:用白骨堆成的圣殿;特点:全身涂满碘酒 | spike:帮助的孩子;samson:奇特的关系
> 在大陆上独自生活了几十年的医生，用死者的骨头堆起一座圣殿。他是这个疯狂世界里最清醒的人。
jimmy | 吉米·克里斯托 | Sir Lord Jimmy Crystal | 吉米帮的首领 | Jack O'Connell | y28 bt | #C8A040 | 吉米帮 | 造型:金色假发、运动服;追随者:一群也都叫“吉米”的人 | spike:想拉进帮派的孩子
> 一群穿着运动服、戴着金色假发、全都叫“吉米”的帮派首领。他是二十八年后最诡异的存在。
erik | 埃里克 | Erik | 瑞典士兵 | Edvin Ryding | y28 | #6A7A8A | 北约士兵 | spike:短暂的同伴
> 船只失事后困在英国的瑞典士兵，对一切都很好奇。
samson | 参孙 | Samson | 阿尔法感染者 | Chi Lewis-Parry | y28 bt | #6A3A3A | 感染者;阿尔法 | 特点:高大、强壮、能把人头连着脊椎拔出来 | kelson:奇特的关系
> 进化出来的“阿尔法”感染者，高大得像巨人，是大陆上最可怕的东西。
infected | 感染者 | The Infected | 狂暴病毒 | - | d28 w28 y28 bt | #8A2A2A | 感染者 | 病毒:狂暴病毒;发作时间:十几秒;特点:跑得飞快、双眼血红
> 被狂暴病毒感染的人，十几秒内就会发狂，跑得飞快，双眼通红。它们不是丧尸——它们还活着。
"""

DECKS = """
days | 第 28 天 | 28 Days | 🚲 | jim selena frank hannah
weeks | 第 28 周 | 28 Weeks | 🚁 | don alice tammy andy doyle scarlet
years | 第 28 年 | 28 Years | 🏹 | spike jamie isla kelson erik
temple | 人骨圣殿 | The Bone Temple | 💀 | kelson spike jimmy samson
infected | 狂暴 | Rage | 🩸 | infected samson
"""

RARE = {"UR": "jim spike"}
