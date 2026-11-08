U = dict(id="billted", n="比尔和泰德", en="Bill & Ted", short="EXCELLENT!",
         tag="Be excellent to each other. 两个搞摇滚的笨蛋，坐着电话亭穿越历史，拯救未来。",
         theme=["#3E7AC8", "#E8C850", "#14182A"], wd=["Q4907852"])
ORDER = 28

WORKS = """
## main | 电影 | The Films
bt1 | Bill & Ted's Excellent Adventure | 1989 | 比尔和泰德历险记
bt2 | Bill & Ted's Bogus Journey | 1991 | 比尔和泰德畅游鬼门关
bt3 | Bill & Ted Face the Music | 2020 | 比尔和泰德寻歌记
## anim | 动画剧集 | Animated Series
bts | Bill & Ted's Excellent Adventures | 1990 | 比尔和泰德历险记 动画版 | ty=s x
"""

CHARS = """
bill | 比尔 | Bill S. Preston, Esq. | 狂野种马吉他手 | Alex Winter | bt1 bt2 bt3 bts | #3E7AC8 | 狂野种马乐队 | 口头禅:Excellent!（太棒了！）;乐队:狂野种马（Wyld Stallyns）;未来:他们的音乐会拯救全人类 | ted:最好的朋友;rufus:来自未来的导师;missy:继母（尴尬）;thea:女儿
> 圣迪马斯高中的摇滚少年，历史课要不及格了。没人想到，他和泰德的乐队会在七百年后成为人类文明的基石。
ted | 泰德 | Ted "Theodore" Logan | 狂野种马吉他手 | Keanu Reeves | bt1 bt2 bt3 bts | #6A5AA0 | 狂野种马乐队 | 口头禅:Party on, dudes!;最怕:被老爸送去阿拉斯加军校 | bill:最好的朋友;rufus:来自未来的导师;billie:女儿
> 年轻时的基努·里维斯，一脸天真地说着“Party on, dudes!”。他和比尔是一对永远在一起的傻瓜。
rufus | 鲁弗斯 | Rufus | 来自 2688 年的导师 | George Carlin | bt1 bt2 bts | #4A4A5A | 未来 | 座驾:时光电话亭;身份:未来世界派来帮助他们的人 | bill:学生;ted:学生
> 从 2688 年坐着电话亭来的导师，负责让这两个笨蛋通过历史考试——因为整个未来都靠他们。
death | 死神 | Death | 被比尔和泰德赢下的死神 | William Sadler | bt2 bt3 | #3A3A4A | 冥界;后来:乐队贝斯手 | 弱点:游戏（打战舰、大富翁、扭扭乐都输了）;口头禅:你们可以拿走我的命……不对 | bill:赢了他的人;ted:赢了他的人
> 想带走比尔和泰德的死神，结果在战舰棋、大富翁和扭扭乐上连输，最后加入了乐队弹贝斯。
missy | 米西 | Missy | 比尔的继母 | Amy Stock-Poynton | bt1 bt2 bt3 | #C08A8A | 圣迪马斯 | 关系:先后嫁给了比尔的爸爸和泰德的爸爸 | bill:继子
> 只比比尔大几岁的继母，比尔每次见她都很尴尬。
napoleon | 拿破仑 | Napoleon Bonaparte | 被拐来的皇帝 | Terry Camilleri | bt1 | #3A5A8A | 历史人物 | 现代体验:保龄球、冰淇淋、水上乐园 | bill:绑他来的人
> 被比尔和泰德“借”到 1988 年的拿破仑，在圣迪马斯迷上了保龄球和巨无霸冰淇淋。
socrates | 苏格拉底 | Socrates | 哲学家 | Tony Steedman | bt1 | #E0D8C8 | 历史人物 | 比尔和泰德叫他:So-crates（苏-克雷茨）
> 被比尔和泰德叫成“苏-克雷茨”的哲学家。
billythekid | 比利小子 | Billy the Kid | 西部亡命徒 | Dan Shor | bt1 | #8A6A3A | 历史人物 | socrates:搭档
> 西部最有名的亡命徒，和苏格拉底组成了奇妙的搭档。
freud | 弗洛伊德 | Sigmund Freud | 心理学家 | Rod Loomis | bt1 | #5A4A3A | 历史人物
> 在商场里给少女做心理分析的弗洛伊德。
beethoven | 贝多芬 | Ludwig van Beethoven | 作曲家 | Clifford David | bt1 | #6A6A8A | 历史人物 | 名场面:在商场的电子琴区大秀琴技
> 在商场电子琴专卖店里一秀琴技、引来一群围观的贝多芬。
joan | 圣女贞德 | Joan of Arc | 法国英雄 | Jane Wiedlin | bt1 | #8A8AA0 | 历史人物 | 现代体验:健身操课
> 在健身房带起有氧操的圣女贞德。
lincoln | 林肯 | Abraham Lincoln | 美国总统 | Robert V. Barron | bt1 | #3A3A3A | 历史人物 | 名台词:Be excellent to each other, and party on, dudes!
> 在演讲台上说出“Be excellent to each other”的林肯总统。
genghis | 成吉思汗 | Genghis Khan | 蒙古大汗 | Al Leong | bt1 | #8A5A3A | 历史人物 | 现代体验:在运动用品店大闹一场
> 在运动用品店里拿着棒球棍大闹的成吉思汗。
evilbots | 邪恶机器人 | Evil Bill & Ted | 机器人版比尔和泰德 | Alex Winter; Keanu Reeves | bt2 | #6A6A6A | 未来反派 | 任务:杀掉比尔和泰德、毁掉他们的未来 | nomolos:造出他们的人
> 未来坏人造出的机器人比尔和泰德，长得一模一样，坏得一模一样。
nomolos | 德·诺莫洛斯 | Chuck De Nomolos | 未来的反派 | Joss Ackland | bt2 | #4A4A4A | 未来 | 目的:阻止狂野种马改变世界
> 未来世界里讨厌摇滚、想改写历史的坏人。
station | 斯泰森 | Station | 火星科学家 | - | bt2 | #C8C0A0 | 外星人 | 特点:两个小外星人合体成一个高个子
> 天堂里找来的火星科学家，两个小家伙合体成一个，帮比尔和泰德造出了好机器人。
thea | 西娅 | Thea Preston | 比尔的女儿 | Samara Weaving | bt3 | #C8A06A | 下一代 | 特点:和爸爸一模一样的说话方式 | bill:爸爸;billie:最好的朋友
> 比尔的女儿，说话、动作和年轻的比尔一模一样。
billie | 比莉 | Billie Logan | 泰德的女儿 | Jack Haven | bt3 | #6A5AA0 | 下一代 | 特点:简直就是年轻的泰德 | ted:爸爸;thea:最好的朋友
> 泰德的女儿，活脱脱一个年轻的泰德。她和西娅去历史里组了一支终极乐队。
kelly | 凯莉 | Kelly | 鲁弗斯的女儿 | Kristen Schaal | bt3 | #8A6AA0 | 未来 | rufus:父亲
> 鲁弗斯的女儿，来接两个中年大叔写出那首“拯救宇宙的歌”。
dennis | 丹尼斯 | Dennis Caleb McCoy | 没自信的杀手机器人 | Anthony Carrigan | bt3 | #8A8AA0 | 未来 | 性格:玻璃心
> 被派来杀比尔和泰德的机器人，却特别玻璃心。
"""

DECKS = """
stallyns | 狂野种马 | Wyld Stallyns | 🎸 | bill ted
history | 历史人物天团 | Historical Figures | 📜 | napoleon socrates billythekid freud beethoven joan lincoln genghis
afterlife | 死神与导师 | Death & Rufus | 💀 | death rufus station
nextgen | 下一代 | The Daughters | 🎤 | thea billie kelly
bogus | 鬼门关之旅 | Bogus Journey | 🤖 | evilbots nomolos death station
"""

RARE = {"UR": "bill ted"}
