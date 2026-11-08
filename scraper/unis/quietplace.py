U = dict(id="quiet", n="寂静之地", en="A Quiet Place", short="SHHH",
         tag="嘘。如果它们听见你，你就完了。",
         theme=["#6A7A6A", "#D8D8C8", "#0E120E"], timeline=True, wd=["Q111993071"])
ORDER = 25

WORKS = """
## main | 寂静之地 | A Quiet Place
day1 | A Quiet Place: Day One | 2024 | 寂静之地：入侵日 | tl=0 tll=入侵第一天·纽约
aqp1 | A Quiet Place | 2018 | 寂静之地 | tl=1 tll=入侵后第_89_天至第_472_天
aqp2 | A Quiet Place Part II | 2020 | 寂静之地2 | tl=2 tll=入侵后第_474_天
aqp3 | A Quiet Place Part III | 2027 | 寂静之地3 | tl=3
"""

CHARS = """
evelyn | 伊芙琳·艾伯特 | Evelyn Abbott | 艾伯特家的母亲 | Emily Blunt | aqp1 aqp2 | #8A6A5A | 艾伯特一家 | 名场面:在浴缸里无声分娩;武器:霰弹枪 | lee:丈夫;regan:女儿;marcus:儿子;beau:小儿子
> 在无声的世界里怀孕、生子的母亲。她在浴缸里咬着牙无声分娩的那一场，让整个影院都屏住了呼吸。
lee | 李·艾伯特 | Lee Abbott | 艾伯特家的父亲 | John Krasinski | aqp1 aqp2 | #5A6A5A | 艾伯特一家 | 特长:修收音机、在地下室研究怪物的弱点;趣事:演员也是导演，和饰演伊芙琳的艾米莉·布朗特是真夫妻 | evelyn:妻子;regan:一直想给她修好助听器的女儿
> 沉默的父亲，在地下室里一遍遍地给女儿改造助听器。他用手语说出了那句“我一直爱你”。
regan | 里根·艾伯特 | Regan Abbott | 失聪的女儿 | Millicent Simmonds | aqp1 aqp2 aqp3 | #8A7A5A | 艾伯特一家 | 特点:天生失聪（演员本人也是）;武器:助听器的高频噪音 | lee:父亲;marcus:弟弟;emmett:并肩前行的人
> 天生失聪的大女儿，一直以为父亲怪她。最后，是她发现了打败怪物的方法。演员本人也是听障人士。
marcus | 马库斯·艾伯特 | Marcus Abbott | 胆小的儿子 | Noah Jupe | aqp1 aqp2 aqp3 | #6A7A8A | 艾伯特一家 | regan:姐姐;evelyn:母亲
> 胆子小、心思细的儿子，在第二部里一点点长大。
beau | 博·艾伯特 | Beau Abbott | 最小的孩子 | Cade Woodward | aqp1 aqp2 | #A08A6A | 艾伯特一家 | 那件事:一只会响的玩具火箭 | regan:姐姐
> 艾伯特家最小的孩子，一只会响的玩具火箭……
emmett | 艾米特 | Emmett | 李的老朋友 | Cillian Murphy | aqp2 aqp3 | #5A5A5A | 幸存者 | 状态:失去了所有家人 | regan:并肩前行的人;evelyn:老朋友的妻子
> 失去家人后躲进废弃工厂的老邻居，被里根拉着重新走了出去。
sam | 萨米拉 | Samira | 绝症诗人 | Lupita Nyong'o | day1 | #6A4A6A | 幸存者;纽约 | 心愿:吃一块哈莱姆区的披萨;伙伴:猫咪弗罗多 | eric:陪她走完最后一程的人;frodo:她的猫
> 住在临终关怀医院的诗人，怪物来袭那天，她只想去吃一块小时候常吃的披萨。
eric | 埃里克 | Eric | 英国法学生 | Joseph Quinn | day1 | #6A6A8A | 幸存者;纽约 | 特点:怕得发抖，却一直跟着萨米拉 | sam:陪伴的人;frodo:一起逃命的猫
> 在纽约被吓坏的英国法学生，跟着萨米拉和她的猫穿过了半个曼哈顿。
frodo | 弗罗多 | Frodo | 萨米拉的猫 | - | day1 | #C8A07A | 猫 | 特长:从不乱叫、在怪物面前淡定得离谱 | sam:主人;eric:新朋友
> 萨米拉的服务猫，全片最淡定的角色，从头到尾一声没叫。
henri | 亨利 | Henri | 岛上的幸存者 | Djimon Hounsou | day1 aqp2 | #4A4A4A | 幸存者 | 后来:海岛社区的领袖
> 入侵日在纽约逃生的男人，一年多后成了海岛上幸存者社区的领袖。
reuben | 鲁本 | Reuben | 萨米拉的护工 | Alex Wolff | day1 | #6A5A5A | 临终关怀医院 | sam:照顾的病人
> 临终关怀医院里照顾萨米拉的护工。
deathangel | 死亡天使 | The Death Angels | 听觉猎手 | - | day1 aqp1 aqp2 aqp3 | #3A3A3A | 外星生物 | 特点:没有眼睛、听觉极其灵敏、刀枪不入的甲壳;弱点:高频声波、水
> 从天而降的盲眼怪物，听得见一根针掉在地上的声音。它们不会游泳，也受不了高频噪音。
"""

DECKS = """
abbotts | 艾伯特一家 | The Abbotts | 🌽 | evelyn lee regan marcus beau
dayone | 入侵第一天 | Day One | 🍕 | sam eric frodo henri reuben
together | 继续前行 | Part II | 📻 | regan marcus emmett evelyn henri
"""

RARE = {"UR": "evelyn regan"}
