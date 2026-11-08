U = dict(id="conjuring", n="招魂宇宙", en="The Conjuring Universe", short="CONJURING",
         tag="根据沃伦夫妇的真实案件改编。那个房间里锁着的每一件东西，都有一个故事。",
         theme=["#8A6A4A", "#D8C8A8", "#0E0C0A"], timeline=True, wd=["Q104771487"])
ORDER = 23

WORKS = """
## main | 招魂正传 | The Conjuring
c1 | The Conjuring | 2013 | 招魂 | tl=1971
c2 | The Conjuring 2 | 2016 | 招魂2 | tl=1977
c3 | The Conjuring: The Devil Made Me Do It | 2021 | 招魂3 | tl=1981
c4 | The Conjuring: Last Rites | 2025 | 招魂4：最终仪式 | tl=1986
## annabelle | 安娜贝尔 | Annabelle
an2 | Annabelle: Creation | 2017 | 安娜贝尔2：诞生 | tl=1955
an1 | Annabelle | 2014 | 安娜贝尔 | tl=1967
an3 | Annabelle Comes Home | 2019 | 安娜贝尔3：回家 | tl=1972
## nun | 修女 | The Nun
nun | The Nun | 2018 | 修女 | tl=1952
nun2 | The Nun II | 2023 | 修女2 | tl=1956
## else | 外传 | Spin-off
llorona | The Curse of La Llorona | 2019 | 哭泣的女人 | x tl=1973
"""

CHARS = """
ed | 艾德·沃伦 | Ed Warren | 恶魔学家 | Patrick Wilson | c1 c2 c3 c4 an3 | #6A5A4A | 沃伦夫妇;超自然调查员 | 身份:教会认可的恶魔学家;爱好:弹吉他唱猫王的歌;家里:一间锁着各种邪物的藏品室 | lorraine:一生挚爱;judy:女儿
> 教会认可的恶魔学家，和妻子一起调查了上万起灵异案件。他在《招魂2》里抱着吉他唱《Can't Help Falling in Love》的那一幕，是整个系列最温柔的时刻。
lorraine | 罗琳·沃伦 | Lorraine Warren | 灵媒 | Vera Farmiga | c1 c2 c3 c4 an3 | #8A7A9A | 沃伦夫妇;灵媒 | 能力:能看见和感应灵体;最怕:预见到艾德的死亡 | ed:一生挚爱;judy:女儿;valak:一次次纠缠她的恶魔
> 能看见“另一边”的灵媒，冷静又温柔。她最大的恐惧，不是恶魔，而是失去艾德。
judy | 茱蒂·沃伦 | Judy Warren | 沃伦夫妇的女儿 | Mckenna Grace; Sterling Jerins; Mia Tomlinson | c1 c2 an3 c4 | #C8A08A | 沃伦家 | 能力:继承了母亲的灵视 | ed:父亲;lorraine:母亲;annabelle:她家藏品室里的“客人”;tony:男朋友
> 沃伦夫妇的独生女，从小就和藏品室一墙之隔。她继承了妈妈的能力，也继承了那份勇敢。
tony | 托尼·斯佩拉 | Tony Spera | 茱蒂的男朋友 | Ben Hardy | c4 | #5A5A6A | 沃伦家 | 职业:警察 | judy:女朋友
> 茱蒂的男朋友，一个普通的警察，被卷进了沃伦家的最后一案。
annabelle | 安娜贝尔 | Annabelle | 史上最邪门的娃娃 | - | an2 an1 an3 c1 | #C8B8A0 | 邪物;沃伦藏品室 | 来历:木偶师马林斯为女儿做的娃娃;现在:锁在沃伦家的玻璃柜里，柜上写着“绝对不要打开”;真相:娃娃本身只是一个“通道” | judy:藏品室里的邻居;mullins:做她的人
> 一个笑容诡异的瓷娃娃，被锁在沃伦家的玻璃柜里，柜子上写着：“绝对不要打开”。她自己没有灵魂，却是恶魔最好的通道。
valak | 修女瓦拉克 | Valak | 恶魔修女 | Bonnie Aarons | c2 nun nun2 | #2A2A2E | 恶魔 | 形象:黑袍修女、苍白的脸、黄色眼睛;来历:罗马尼亚圣卡塔修道院 | lorraine:一次次纠缠的人;irene:宿敌
> 以修女形象出现的恶魔，在罗琳的画里、走廊的尽头，一次又一次地出现。
irene | 艾琳修女 | Sister Irene | 见习修女 | Taissa Farmiga | nun nun2 | #8A8AAA | 修女 | 特点:能看见异象;趣事:演员是罗琳·沃伦扮演者的亲妹妹 | valak:宿敌;burke:同行的神父;frenchie:朋友
> 被派往罗马尼亚调查修女自杀案的见习修女。演员是维拉·法梅加的亲妹妹。
burke | 伯克神父 | Father Burke | 调查神迹的神父 | Demián Bichir | nun | #4A4A4A | 神父 | 往事:一次失败的驱魔 | irene:同行的修女
> 梵蒂冈派来调查的神父，背负着一次驱魔失败的阴影。
frenchie | 法国佬 | Frenchie | 送货小伙 | Jonas Bloquet | nun nun2 | #8A6A4A | 平民 | 本名:莫里斯;秘密:他身上的东西 | irene:朋友
> 给修道院送货的法裔小伙子，第一个发现修女尸体的人。他的故事一直延伸到了《招魂》第一部。
carolyn | 卡罗琳·佩伦 | Carolyn Perron | 被附身的母亲 | Lili Taylor | c1 | #8A7A6A | 佩伦一家 | 案件:罗德岛哈里斯维尔农舍 | roger:丈夫;bathsheba:附身于她的女巫
> 搬进罗德岛老农舍的五个女儿的妈妈，身上莫名出现淤青。
roger | 罗杰·佩伦 | Roger Perron | 佩伦家的父亲 | Ron Livingston | c1 | #6A6A5A | 佩伦一家 | carolyn:妻子
> 卡罗琳的丈夫，一家人的支柱。
bathsheba | 拔示巴 | Bathsheba | 农舍里的女巫 | Joseph Bishara | c1 | #3A3A3A | 恶灵 | 来历:1863 年把孩子献祭给恶魔的女巫
> 1863 年住在那座农舍里的女巫，诅咒了之后所有的住户。
crooked | 扭曲人 | The Crooked Man | 童谣里的高个子 | Javier Botet | c2 | #4A4A4A | 恶灵 | 来历:一个八音盒里的童谣
> 从八音盒童谣里走出来的高个子怪物，走路像扭曲的木偶。
peggy | 佩吉·霍奇森 | Peggy Hodgson | 恩菲尔德的单亲妈妈 | Frances O'Connor | c2 | #8A7A6A | 霍奇森一家 | 案件:伦敦恩菲尔德闹鬼事件 | janet:女儿
> 伦敦恩菲尔德的单亲妈妈，独自带着四个孩子住在闹鬼的房子里。
janet | 珍妮特·霍奇森 | Janet Hodgson | 被附身的女孩 | Madison Wolfe | c2 | #A08A7A | 霍奇森一家 | 被附身:老人比尔·威尔金斯 | peggy:妈妈;billwilkins:附身她的老人
> 被死去的老人附身的十一岁女孩，恩菲尔德案的中心。
billwilkins | 比尔·威尔金斯 | Bill Wilkins | 恩菲尔德的老人 | Bob Adrian | c2 | #6A6A6A | 恶灵 | 名台词:这是我的房子！ | janet:附身的女孩
> 死在那张椅子上的老人，一直坚称：“这是我的房子！”
arne | 阿恩·约翰逊 | Arne Johnson | 第一个以“恶魔附身”辩护的被告 | Ruairi O'Connor | c3 | #5A6A6A | 案件当事人 | 案件:美国历史上第一起以恶魔附身作辩护的谋杀案 | debbie:女朋友
> 美国历史上第一个声称“是恶魔让我做的”的谋杀案被告。
debbie | 黛比·格拉策尔 | Debbie Glatzel | 阿恩的女朋友 | Sarah Catherine Hook | c3 | #A07A6A | 案件当事人 | arne:男朋友
> 阿恩的女朋友，她的弟弟最先被附身。
occultist | 神秘女巫 | The Occultist | 诅咒的施咒人 | Eugenie Bondurant | c3 | #3A3A4A | 邪教 | 手段:放置诅咒图腾
> 在暗中下诅咒的邪教女巫，是《招魂3》里真正的敌人。
mia | 米娅·福姆 | Mia Form | 安娜贝尔的第一个主人 | Annabelle Wallis | an1 | #C8A08A | 福姆一家 | 趣事:演员的名字也叫安娜贝尔 | john:丈夫;annabelle:丈夫送她的娃娃
> 丈夫送了她一个古董娃娃当礼物，从此家里不得安宁。
john | 约翰·福姆 | John Form | 医学生丈夫 | Ward Horton | an1 | #6A6A7A | 福姆一家 | mia:妻子
> 米娅的丈夫，那个娃娃就是他买的。
perez | 佩雷斯神父 | Father Perez | 帮助过很多人的神父 | Tony Amendola | an1 an2 llorona | #6A5A4A | 神父 | 特点:串起了好几部电影
> 在好几部电影里出现的老神父，是招魂宇宙里的“串场人物”。
janice | 珍妮丝 | Janice | 孤儿院的女孩 | Talitha Bateman | an2 | #8A7A8A | 孤儿 | 状态:患过小儿麻痹，拄着拐杖 | linda:最好的朋友;annabelle:找到的娃娃
> 腿脚不便的孤儿，在马林斯家的禁闭房间里找到了那个娃娃。
linda | 琳达 | Linda | 珍妮丝的好朋友 | Lulu Wilson | an2 | #A08A6A | 孤儿 | janice:最好的朋友
> 珍妮丝最好的朋友，发誓一定要保护她。
mullins | 塞缪尔·马林斯 | Samuel Mullins | 木偶师 | Anthony LaPaglia | an2 | #6A5A4A | 马林斯一家 | 往事:失去了女儿比，向“任何东西”祈求她回来 | esther:妻子;annabelle:亲手做的娃娃
> 做出安娜贝尔娃娃的木偶师，失去女儿后向任何力量祈祷她回来——有东西回应了。
esther | 埃丝特·马林斯 | Esther Mullins | 木偶师的妻子 | Miranda Otto | an2 | #8A7A7A | 马林斯一家 | mullins:丈夫
> 马林斯的妻子，一直戴着半张面具躲在卧室里。
charlotte | 夏洛特修女 | Sister Charlotte | 带孤儿们的修女 | Stephanie Sigman | an2 nun | #6A6A8A | 修女
> 带着孤儿们搬进马林斯家的修女。
maryellen | 玛丽·艾伦 | Mary Ellen | 茱蒂的保姆 | Madison Iseman | an3 | #C08A7A | 沃伦家 | judy:照顾的孩子;daniela:好朋友
> 沃伦夫妇出差那晚来照顾茱蒂的保姆。
daniela | 丹妮拉 | Daniela Rios | 打开柜子的人 | Katie Sarife | an3 | #8A6A6A | 平民 | 动机:想和死去的父亲说话 | maryellen:好朋友
> 保姆的好朋友，为了和死去的父亲说上一句话，偷偷打开了藏品室——然后打开了那个柜子。
ferryman | 摆渡人 | The Ferryman | 藏品室里的邪物 | - | an3 | #3A3A3A | 邪物;沃伦藏品室 | 规则:死者眼上放硬币
> 沃伦藏品室里的一件邪物，等着收死人眼睛上的硬币。
llorona | 哭泣的女人 | La Llorona | 拉丁美洲传说里的女鬼 | Marisol Ramirez | llorona | #E0E0E0 | 恶灵 | 传说:溺死了自己的孩子，从此游荡找孩子
> 墨西哥传说里的哭泣女鬼，溺死了自己的孩子，永远在找新的孩子。
anna | 安娜·泰特-加西亚 | Anna Tate-Garcia | 社工妈妈 | Linda Cardellini | llorona | #8A6A5A | 平民 | 职业:社工 | llorona:纠缠她孩子的女鬼
> 一位独自带着两个孩子的社工，被哭泣的女人盯上了。
"""

DECKS = """
warrens | 沃伦一家 | The Warrens | ✝ | ed lorraine judy tony
artifacts | 藏品室 | The Artifact Room | 🔒 | annabelle valak crooked ferryman bathsheba
demons | 恶灵图鉴 | Book of Demons | 👁 | bathsheba annabelle valak crooked billwilkins occultist llorona
nun | 修女传 | The Nun | ⛪ | irene burke frenchie valak charlotte
dollkeepers | 安娜贝尔的主人们 | Annabelle's Keepers | 🎎 | mullins esther janice linda mia john judy
cases | 沃伦夫妇的案子 | The Warren Files | 📁 | carolyn roger peggy janet arne debbie
babysit | 那一晚的沃伦家 | Annabelle Comes Home | 🕯 | judy maryellen daniela annabelle ferryman
"""

RARE = {"UR": "ed lorraine annabelle valak"}
