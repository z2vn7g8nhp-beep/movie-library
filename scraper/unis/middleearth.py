U = dict(id="mearth", n="中土世界", en="Middle-earth", short="MIDDLE-EARTH",
         tag="一枚戒指，统御众戒。从袋底洞出发，去孤山，去魔多，再回到夏尔。",
         theme=["#B8902E", "#E8DCC0", "#1A160E"], timeline=True, wd=["Q26214973", "Q190214", "Q74331"])
ORDER = 13

WORKS = """
## lotr | 指环王三部曲 | The Lord of the Rings
fotr | The Lord of the Rings: The Fellowship of the Ring | 2001 | 指环王1：护戒使者 | tl=3018
ttt | The Lord of the Rings: The Two Towers | 2002 | 指环王2：双塔奇兵 | tl=3019
rotk | The Lord of the Rings: The Return of the King | 2003 | 指环王3：王者无敌 | tl=3019.5
## hobbit | 霍比特人三部曲 | The Hobbit
hob1 | The Hobbit: An Unexpected Journey | 2012 | 霍比特人1：意外之旅 | tl=2941
hob2 | The Hobbit: The Desolation of Smaug | 2013 | 霍比特人2：史矛革之战 | tl=2941.4
hob3 | The Hobbit: The Battle of the Five Armies | 2014 | 霍比特人3：五军之战 | tl=2941.8
## else | 外传 | Tales
rohirrim | The Lord of the Rings: The War of the Rohirrim | 2024 | 指环王：洛汗之战 | x tl=2758
"""

CHARS = """
# —— 护戒远征队
frodo | 佛罗多 | Frodo Baggins | 持戒人 | Elijah Wood | fotr ttt rotk hob1 | #4E7A9A | 霍比特人;护戒远征队;持戒人 | 家:夏尔·袋底洞;武器:刺叮剑;护身:秘银甲;生日:9 月 22 日（和比尔博同一天） | sam:最忠诚的伙伴;bilbo_h:叔叔;gandalf:引路人;gollum:向导，也是另一个自己;aragorn:守护他的游侠
> 袋底洞的年轻霍比特人，从叔叔比尔博那里继承了一枚戒指，也继承了整个中土的命运。他走进了最黑暗的地方，回来时已经不再是原来的自己。
sam | 山姆 | Samwise Gamgee | 永远的伙伴 | Sean Astin | fotr ttt rotk | #6A8A3A | 霍比特人;护戒远征队;持戒人（短暂） | 职业:园丁;最爱:土豆、种花;名场面:背着佛罗多爬上末日火山;后来:夏尔镇长 | frodo:最重要的人;rosie:心上人;gollum:始终不信任的人
> 佛罗多的园丁，一路上不肯离开半步。“我背不动戒指，但我能背你。”很多人说，他才是这个故事真正的英雄。
merry | 梅里 | Merry Brandybuck | 雄鹿地的霍比特人 | Dominic Monaghan | fotr ttt rotk | #8A6A3A | 霍比特人;护戒远征队;洛汗骠骑 | 后来:成为洛汗的骑士;搭档:皮平 | pippin:形影不离;eowyn:并肩冲锋;theoden:效忠的国王;treebeard:说动他出战
> 皮平的好兄弟，聪明又机灵。在帕兰诺平原上，他和伊欧温一起面对了戒灵之王。
pippin | 皮平 | Pippin Took | 图克家的捣蛋鬼 | Billy Boyd | fotr ttt rotk | #A07A3A | 霍比特人;护戒远征队;刚铎卫兵 | 后来:刚铎王城卫兵;名场面:在迪耐瑟面前唱歌、点燃烽火 | merry:形影不离;gandalf:常被他敲脑袋;denethor:效忠的宰相
> 最爱闯祸的霍比特人，从偷农夫的胡萝卜到往井里扔石头，样样都干过。后来，他点燃了召唤盟友的烽火。
gandalf | 甘道夫 | Gandalf | 灰袍 / 白袍巫师 | Ian McKellen | fotr ttt rotk hob1 hob2 hob3 | #8A8A9A | 伊斯塔尔（巫师）;护戒远征队;白道会 | 真身:迈雅;别称:灰袍甘道夫、白袍甘道夫、米斯兰迪尔;武器:格拉姆德凛剑、法杖;坐骑:影疾;名台词:你不能过去！ | frodo:托付重任的孩子;bilbo_f:拉去冒险的人;aragorn:看好的王;saruman:昔日上司;shadowfax:坐骑;balrog:在桥上的对决;radagast:同僚
> 戴着尖帽子、抽着烟斗的巫师，最爱烟火和霍比特人。他在摩瑞亚的桥上挡住了炎魔，然后以白袍之姿归来。
aragorn | 阿拉贡 | Aragorn | 大步佬 · 埃莱萨王 | Viggo Mortensen | fotr ttt rotk | #4A5A4A | 人类;护戒远征队;刚铎国王 | 别名:大步佬、埃莱萨;身份:伊西尔杜的继承人;武器:安督利尔（重铸的纳希尔圣剑）;年龄:八十多岁（杜内丹人很长寿） | arwen:一生挚爱;frodo:守护的人;legolas:挚友;gimli:挚友;boromir:战友;elrond:岳父;isildur:先祖
> 北方的游侠，满身风尘。他是刚铎王位的继承人，却一直害怕自己会重蹈先祖的覆辙。最后，他戴上王冠，对霍比特人说：你们不必向任何人鞠躬。
legolas | 莱戈拉斯 | Legolas | 黑森林王子 | Orlando Bloom | fotr ttt rotk hob2 hob3 | #C9B87A | 精灵;护戒远征队 | 身份:瑟兰迪尔之子、黑森林王子;武器:长弓、双刀;名场面:滑盾牌下台阶、单人放倒猛犸 | gimli:从互看不顺眼到生死之交;aragorn:挚友;thranduil:父亲;tauriel:心动过的人
> 金发的精灵王子，眼神好、箭术神、动作帅，滑着盾牌下楼梯的画面风靡了一整代人。
gimli | 金雳 | Gimli | 格罗因之子 | John Rhys-Davies | fotr ttt rotk | #8A4A2A | 矮人;护戒远征队 | 父亲:格罗因;武器:双刃战斧;最在意:和莱戈拉斯比谁杀的敌人多;心动:凯兰崔尔的三根头发 | legolas:从互看不顺眼到生死之交;aragorn:挚友;galadriel:仰慕的夫人;gloin:父亲
> 脾气火爆的矮人，和精灵本来是世仇。走完这一路，他成了莱戈拉斯最好的朋友，还向凯兰崔尔要了三根头发。
boromir | 波罗米尔 | Boromir | 刚铎的长子 | Sean Bean | fotr | #6A3A3A | 人类;护戒远征队;刚铎 | 父亲:宰相迪耐瑟;武器:剑、盾、刚铎号角 | faramir:弟弟;aragorn:最后认了他做王;denethor:父亲
> 刚铎宰相的长子，骄傲而勇敢。戒指在他耳边低语，他犯了错，又用生命弥补了。
# —— 夏尔与布理
bilbo_h | 比尔博 | Bilbo Baggins | 霍姆版 · 老比尔博 | Ian Holm | fotr rotk hob1 | #8A6A4A | 霍比特人;持戒人 | 著作:《去而复返》;生日:111 岁那天消失在宴会上 | frodo:侄子;bilbo_f:年轻时的自己;gandalf:老朋友
> 111 岁生日宴会上戴上戒指凭空消失的老霍比特人，从此去了瑞文戴尔写书。
bilbo_f | 比尔博 | Bilbo Baggins | 弗里曼版 · 年轻的比尔博 | Martin Freeman | hob1 hob2 hob3 | #9A7A4A | 霍比特人;索林的队伍;持戒人 | 职业（自封）:飞贼;武器:刺叮剑;拿手:猜谜、偷东西;最怕:没吃上第二顿早餐 | thorin:并肩冒险的人;gandalf:把他拉出门的巫师;gollum:猜谜对手;smaug:隔着金山聊天的龙;bilbo_h:老了以后的自己
> 本来只想在家喝茶的霍比特人，被巫师和十三个矮人拉上了冒险之路。在迷雾山脉的黑暗里，他捡到了一枚戒指。
rosie | 罗西 | Rosie Cotton | 山姆的心上人 | Sarah McLeod | fotr rotk | #C08A6A | 霍比特人 | 工作:绿龙酒馆 | sam:恋人
> 山姆暗恋多年的姑娘，后来成了他的妻子。
butterbur | 黄油菊 | Barliman Butterbur | 跃马客栈老板 | David Weatherley | fotr | #8A7A5A | 人类;布理 | 店:跃马客栈
> 布理跃马客栈的老板，健忘又热心，差点误了甘道夫的大事。
# —— 精灵
galadriel | 凯兰崔尔 | Galadriel | 罗瑞恩的夫人 | Cate Blanchett | fotr ttt rotk hob1 hob3 | #E0D8B0 | 精灵;白道会;罗斯洛立安 | 持有:精灵三戒之一·能雅;送给佛罗多:埃兰迪尔之星;能力:读心与预见 | celeborn:丈夫;elrond:亲家;frodo:赠礼的人;gimli:被他的真诚打动;gandalf:老友
> 中土最古老也最强大的精灵之一。她拒绝了戒指的诱惑，选择“衰退，西渡，仍是凯兰崔尔”。
elrond | 埃尔隆德 | Elrond | 瑞文戴尔之主 | Hugo Weaving | fotr ttt rotk hob1 hob3 | #6A6A8A | 精灵;白道会;瑞文戴尔 | 持有:精灵三戒之一·维雅;往事:亲眼看着伊西尔杜没有毁掉戒指 | arwen:女儿;aragorn:看着长大的人;galadriel:亲家;isildur:旧日遗憾
> 瑞文戴尔的主人，主持了决定戒指命运的会议。三千年前，他就站在末日火山里。
arwen | 阿尔温 | Arwen | 暮星 | Liv Tyler | fotr ttt rotk | #6A5A8A | 精灵;瑞文戴尔 | 别称:暮星;选择:放弃永生;名场面:策马渡河、召来洪水 | aragorn:一生挚爱;elrond:父亲
> 埃尔隆德的女儿，为了和阿拉贡在一起，放弃了精灵的永生。
haldir | 哈尔迪尔 | Haldir | 罗瑞恩边境守卫 | Craig Parker | fotr ttt | #B8A87A | 精灵;罗斯洛立安 | 带领:精灵援军驰援圣盔谷
> 罗瑞恩的边境守卫队长，带着精灵弓箭手来到圣盔谷，兑现了古老的盟约。
celeborn | 凯勒鹏 | Celeborn | 罗瑞恩之主 | Marton Csokas | fotr rotk | #B0B0A0 | 精灵;罗斯洛立安 | galadriel:妻子
> 凯兰崔尔的丈夫，罗斯洛立安的精灵之王。
thranduil | 瑟兰迪尔 | Thranduil | 森林精灵王 | Lee Pace | hob1 hob2 hob3 | #C9C0A0 | 精灵;黑森林 | 坐骑:巨鹿;最爱:白色宝石;特点:眼神傲慢、动作优雅 | legolas:儿子;thorin:宿怨;tauriel:麾下卫队长
> 黑森林的精灵王，骑着一头大角鹿，傲慢、美丽又冷漠。他和矮人之间有几百年的旧怨。
tauriel | 陶瑞尔 | Tauriel | 黑森林卫队长 | Evangeline Lilly | hob2 hob3 | #6A8A3A | 精灵;黑森林 | 武器:弓、双短刀;性格:不愿袖手旁观 | kili:心动的人;legolas:青梅竹马;thranduil:效忠的国王
> 电影原创的女精灵卫队长，红发、勇敢，不肯看着外面的世界被黑暗吞噬。
# —— 洛汗与刚铎
theoden | 希优顿 | Théoden | 洛汗国王 | Bernard Hill | ttt rotk | #8A6A2A | 人类;洛汗 | 名场面:帕兰诺平原的冲锋（“死亡！”）;坐骑:雪鬃 | eowyn:外甥女;eomer:外甥;wormtongue:蛊惑他的人;merry:收为侍从
> 被萨鲁曼蛊惑多年的洛汗国王，从昏沉中醒来后带领骠骑冲向了帕兰诺平原。
eowyn | 伊欧温 | Éowyn | 洛汗的盾女 | Miranda Otto | ttt rotk rohirrim | #C9B87A | 人类;洛汗 | 名台词:我不是男人！;名场面:斩杀戒灵之王;后来:嫁给法拉米尔 | eomer:哥哥;theoden:舅舅;faramir:后来的爱人;merry:并肩冲锋;aragorn:曾经仰慕的人
> 洛汗的公主，不甘心只守在家里。她女扮男装上了战场，说出了那句“我不是男人”。
eomer | 伊奥梅尔 | Éomer | 洛汗骠骑统领 | Karl Urban | ttt rotk | #6A6A3A | 人类;洛汗 | 后来:洛汗国王 | eowyn:妹妹;theoden:舅舅;aragorn:并肩作战
> 洛汗的骠骑统领，被放逐后仍带着人马赶来支援。
wormtongue | 巧言 | Gríma Wormtongue | 格里玛 | Brad Dourif | ttt | #3A3A3A | 人类;萨鲁曼的爪牙 | 本名:格里玛 | saruman:效忠的人;theoden:蛊惑的国王;eowyn:觊觎的人
> 蜷在希优顿王座旁的阴沉谋士，暗中替萨鲁曼做事。
faramir | 法拉米尔 | Faramir | 刚铎次子 | David Wenham | ttt rotk | #4A5A6A | 人类;刚铎 | 职责:伊希利恩游侠队长;性格:温和、清醒 | boromir:哥哥;denethor:偏心的父亲;eowyn:后来的爱人;frodo:放走的人
> 波罗米尔的弟弟，一直得不到父亲的认可。戒指就在眼前，他选择了放手。
denethor | 迪耐瑟 | Denethor | 刚铎宰相 | John Noble | rotk | #4A4A4A | 人类;刚铎 | 秘密:用真知晶石看到了绝望的未来 | boromir:最爱的长子;faramir:不被看重的次子;pippin:收下的卫兵
> 刚铎的宰相，丧子之痛和绝望把他逼疯了。
isildur | 伊西尔杜 | Isildur | 第一位持戒人 | Harry Sinclair | fotr | #6A6A5A | 人类;努门诺尔 | 往事:用断剑砍下索伦的手指，却没毁掉戒指 | elrond:劝他毁戒的人;aragorn:后代
> 三千年前砍下索伦手指的人类国王，却没舍得毁掉那枚戒指。
deagol | 德阿戈 | Déagol | 找到戒指的人 | Thomas Robins | rotk | #8A7A5A | 史图尔人（霍比特人的远亲） | 往事:在河底捡到了戒指 | gollum:表亲
> 在钓鱼时从河底捡到戒指的史图尔人，他的表亲斯米戈尔想要它当“生日礼物”。
kingdead | 亡灵之王 | King of the Dead | 背誓者之王 | Paul Norell | rotk | #8AA0A0 | 亡灵大军 | 誓言:曾背弃伊西尔杜，被诅咒不得安息 | aragorn:召唤他们的王
> 背弃誓言而被诅咒的亡灵之王，等待伊西尔杜的继承人来解除诅咒。
# —— 魔多与艾辛格
sauron | 索伦 | Sauron | 魔眼 · 死灵法师 | Benedict Cumberbatch | fotr ttt rotk hob2 hob3 | #C0402A | 迈雅;黑暗魔君 | 形态:烈焰魔眼、死灵法师;铸造:至尊魔戒;据点:巴拉多 | gollum:被戒指吸引来的人;saruman:被他收服的巫师;witchking:最强的仆从
> 至尊魔戒的铸造者，失去肉身后化作塔顶燃烧的魔眼，日夜搜寻他的戒指。
saruman | 萨鲁曼 | Saruman | 白袍巫师 | Christopher Lee | fotr ttt hob1 hob3 | #E0E0E0 | 伊斯塔尔（巫师）;白道会首领 | 据点:艾森加德·欧尔桑克塔;军队:强兽人 | gandalf:昔日同僚;sauron:被他收服;wormtongue:爪牙;lurtz:造出的强兽人
> 白道会之首，被真知晶石里的索伦慢慢收服，在艾森加德砍光森林、造出了一支强兽人大军。
gollum | 咕噜 | Gollum | 斯米戈尔 | Andy Serkis | fotr ttt rotk hob1 | #8A9A7A | 史图尔人;持戒人 | 本名:斯米戈尔;口头禅:我的宝贝;最爱:生鱼;两个人格:咕噜与斯米戈尔 | frodo:他的“主人”;sam:死对头;bilbo_f:猜谜对手;deagol:表亲
> 被戒指折磨了五百年的可怜生物，嘴里一直念着“我的宝贝”。他的身体里住着两个人：凶狠的咕噜，和还记得阳光的斯米戈尔。
witchking | 戒灵之王 | Witch-king of Angmar | 安格玛巫王 | Lawrence Makoare | fotr rotk | #2E2E3A | 戒灵;魔多 | 预言:没有男人能杀死他;坐骑:戒灵兽 | sauron:主人;eowyn:斩杀他的女人;nazgul:麾下九骑
> 九戒灵之首，传说“没有男人能杀死他”——伊欧温摘下了头盔。
nazgul | 戒灵 | Nazgûl | 九骑士 | - | fotr ttt rotk hob2 hob3 | #1E1E28 | 戒灵;魔多 | 来历:曾是戴上九枚人戒的人类国王;弱点:火、水
> 戴上九枚人戒的人类国王，被索伦奴役成没有形体的黑骑士，在夏尔的路上追杀佛罗多。
lurtz | 勒茨 | Lurtz | 第一个强兽人 | Lawrence Makoare | fotr | #3A3A2A | 强兽人;艾辛格 | 武器:长弓
> 萨鲁曼在地底造出的第一个强兽人，射倒了波罗米尔。
gothmog | 戈斯莫格 | Gothmog | 魔多大军副统帅 | Lawrence Makoare | rotk | #4A4A3A | 半兽人;魔多 | 指挥:围攻米那斯提力斯
> 面目扭曲的半兽人统帅，带兵围攻刚铎王城。
shelob | 希洛布 | Shelob | 巨型蜘蛛 | - | rotk | #2A2A2A | 古老的生物 | 巢穴:奇立斯乌苟;克星:埃兰迪尔之星、刺叮剑
> 盘踞在魔多入口的巨型蜘蛛，咕噜把佛罗多引进了她的巢穴。
balrog | 炎魔 | Balrog | 都林的克星 | - | fotr | #C0402A | 迈雅;古老的恶魔 | 武器:火鞭、火焰之剑;对决:在凯萨督姆桥上对上甘道夫 | gandalf:桥上的对手
> 沉睡在摩瑞亚深处的远古恶魔，在凯萨督姆桥上被甘道夫拦住：“你不能过去！”
# —— 生物
treebeard | 树须 | Treebeard | 恩特 | vo:John Rhys-Davies | ttt rotk | #6A7A4A | 恩特;范贡森林 | 种族:恩特（树人）;口头禅:别着急;特点:说话很慢 | merry:说动他出战的霍比特人;pippin:说动他出战的霍比特人
> 范贡森林里最古老的树人，说话慢吞吞，开个会要好几天。看到被砍光的森林，他终于怒了。
shadowfax | 影疾 | Shadowfax | 万马之王 | - | fotr ttt rotk | #E8E8E8 | 米亚拉斯马 | 特点:能听懂人话、日行千里 | gandalf:主人
> 洛汗的万马之王，只听甘道夫的召唤，白得像一道光。
eagle | 大鹰 | The Eagles | 风王关赫 | - | fotr rotk hob1 hob3 | #8A6A4A | 大鹰 | 首领:风王关赫;名场面:每次关键时刻都会出现 | gandalf:老朋友
> 中土的大鹰，每到最危急的关头，都会从天而降。
# —— 霍比特人：索林的队伍
thorin | 索林·橡木盾 | Thorin Oakenshield | 山下之王 | Richard Armitage | hob1 hob2 hob3 | #3A4A6A | 矮人;都林一族;索林的队伍 | 身份:孤山的王位继承人;武器:兽咬剑、橡木枝盾;执念:阿肯宝钻 | bilbo_f:从轻视到信任;fili:外甥;kili:外甥;balin:老友与谋士;thranduil:宿怨;azog:血仇;thror:祖父
> 流亡的矮人王子，带着十二个矮人去夺回被巨龙占据的故乡。骄傲、坚韧，也差点被金子吞没了心。
balin | 巴林 | Balin | 索林的谋士 | Ken Stott | hob1 hob2 hob3 | #E0E0E0 | 矮人;索林的队伍 | 特点:白胡子、最年长、最温和 | dwalin:弟弟;thorin:效忠的王;bilbo_f:最早接纳他的矮人
> 队伍里最年长、最温厚的矮人，第一个真心接纳了比尔博。
dwalin | 德瓦林 | Dwalin | 光头勇士 | Graham McTavish | hob1 hob2 hob3 | #4A3A3A | 矮人;索林的队伍 | 特点:光头、纹身、指虎 | balin:哥哥;thorin:挚友
> 光头、满身纹身的狠角色，第一个敲开袋底洞大门的矮人。
fili | 菲力 | Fíli | 索林的外甥 | Dean O'Gorman | hob1 hob2 hob3 | #C9A04A | 矮人;都林一族;索林的队伍 | 武器:一身藏满的飞刀 | kili:弟弟;thorin:舅舅
> 索林的大外甥，金发辫子，身上藏着数不清的飞刀。
kili | 奇力 | Kíli | 索林的外甥 | Aidan Turner | hob1 hob2 hob3 | #4A3A2A | 矮人;都林一族;索林的队伍 | 武器:弓;特点:最年轻、没什么胡子 | fili:哥哥;thorin:舅舅;tauriel:心动的人
> 最年轻的矮人，弓箭手，和精灵陶瑞尔之间有一段说不清的心动。
dori | 多瑞 | Dori | 最强壮的矮人 | Mark Hadlow | hob1 hob2 hob3 | #8A7A6A | 矮人;索林的队伍 | 发型:精心编织的辫子 | nori:弟弟;ori:弟弟
> 三兄弟里的大哥，讲究、爱操心，力气最大。
nori | 诺瑞 | Nori | 星形发型的小偷 | Jed Brophy | hob1 hob2 hob3 | #8A5A3A | 矮人;索林的队伍 | 发型:星星形状 | dori:哥哥;ori:弟弟
> 发型像颗星星，手脚不太干净。
ori | 欧瑞 | Ori | 队伍里的书记员 | Adam Brown | hob1 hob2 hob3 | #9A8A6A | 矮人;索林的队伍 | 武器:弹弓;爱好:写日记 | dori:哥哥;nori:哥哥
> 温和羞涩的小弟弟，带着弹弓和日记本。
oin | 欧因 | Óin | 医者 | John Callen | hob1 hob2 hob3 | #8A8A7A | 矮人;索林的队伍 | 随身:助听喇叭 | gloin:弟弟
> 队伍里的医者，耳朵不好，总拿着一只喇叭。
gloin | 格罗因 | Glóin | 金雳的父亲 | Peter Hambleton | hob1 hob2 hob3 | #9A4A2A | 矮人;索林的队伍 | 儿子:金雳;钱包里:老婆儿子的画像 | oin:哥哥;gimli:儿子
> 红胡子的矮人，钱包里放着老婆和“小金雳”的画像。
bifur | 比弗 | Bifur | 头里嵌着斧头的矮人 | William Kircher | hob1 hob2 hob3 | #6A5A4A | 矮人;索林的队伍 | 特点:脑袋里嵌着一截斧头，只会说古矮人语 | bofur:堂弟;bombur:堂弟
> 头上嵌着一截半兽人斧头的矮人，只会说古矮人语。
bofur | 波弗 | Bofur | 戴耳帽的矿工 | James Nesbitt | hob1 hob2 hob3 | #8A6A3A | 矮人;索林的队伍 | 特点:耳罩帽、爱唱歌 | bombur:弟弟;bilbo_f:聊得来的朋友
> 戴耳罩帽、爱说笑的矿工，是比尔博最聊得来的矮人。
bombur | 庞伯 | Bombur | 最胖的矮人 | Stephen Hunter | hob1 hob2 hob3 | #C08A4A | 矮人;索林的队伍 | 特长:吃;名场面:木桶漂流时滚着打半兽人 | bofur:哥哥
> 胖得像个球的厨师，木桶漂流那场滚着撞翻了一排半兽人。
# —— 霍比特人：其他
smaug | 史矛革 | Smaug | 最后的巨龙 | vo:Benedict Cumberbatch | hob1 hob2 hob3 | #B8402A | 巨龙 | 占据:孤山·埃瑞博;弱点:胸口缺了一片鳞;爱好:睡在金山上、听人恭维 | bilbo_f:隔着金山聊天的飞贼;bard:射中它的人;thorin:夺走他家园的龙
> 占据孤山六十年的巨龙，睡在金山上，傲慢、聪明、爱听恭维。他和比尔博那场对话，是整个系列最精彩的戏之一。
bard | 巴德 | Bard the Bowman | 长湖镇的弓箭手 | Luke Evans | hob2 hob3 | #4A5A5A | 人类;长湖镇 | 身份:河谷邦吉瑞安的后裔;武器:黑箭 | smaug:射杀的巨龙;master:看不惯的镇长;thorin:盟友又对峙
> 长湖镇的撑船人，养着三个孩子。他手里那支黑箭，射穿了巨龙的胸口。
azog | 阿佐格 | Azog | 苍白半兽人 | Manu Bennett | hob1 hob2 hob3 | #D0D0C8 | 半兽人;古达巴德 | 特征:苍白皮肤、一只铁爪 | thorin:血仇;bolg:儿子
> 苍白的半兽人首领，和索林一族有血海深仇，一只手被换成了铁钩。
bolg | 博格 | Bolg | 阿佐格之子 | John Tui; Lawrence Makoare | hob2 hob3 | #6A5A5A | 半兽人;古达巴德 | azog:父亲;legolas:对手
> 阿佐格的儿子，和莱戈拉斯在乌鸦岭上打了一场。
radagast | 拉达加斯特 | Radagast | 褐袍巫师 | Sylvester McCoy | hob1 hob2 hob3 | #8A6A3A | 伊斯塔尔（巫师）;白道会 | 坐骑:兔子拉的雪橇;特点:头上有鸟粪、帽子里住着鸟 | gandalf:同僚
> 住在森林里的褐袍巫师，坐着兔子拉的雪橇到处跑，头发里还有鸟窝。
beorn | 比翁 | Beorn | 换皮人 | Mikael Persbrandt | hob2 hob3 | #6A4A2A | 换皮人 | 能力:变成巨熊;最讨厌:矮人和半兽人（后者更讨厌）
> 会变成巨熊的换皮人，收留了索林的队伍一晚，后来在五军之战里从天而降。
master | 长湖镇镇长 | Master of Lake-town | 贪婪的镇长 | Stephen Fry | hob2 hob3 | #8A6A5A | 人类;长湖镇 | 最爱:钱 | alfrid:跟班;bard:眼中钉
> 肥头大耳的长湖镇镇长，只关心钱和自己。
alfrid | 阿尔弗里德 | Alfrid | 镇长的跟班 | Ryan Gage | hob2 hob3 | #6A6A4A | 人类;长湖镇 | master:主子
> 镇长的狗腿子，危急关头穿女装逃跑。
dain | 丹恩·铁足 | Dáin Ironfoot | 铁丘陵之主 | Billy Connolly | hob3 | #8A3A2A | 矮人;铁丘陵 | 坐骑:战猪;武器:战锤 | thorin:堂兄
> 骑着战猪赶来的矮人领主，暴脾气、大嗓门。
thror | 瑟罗尔 | Thrór | 山下之王 | Jeffrey Thomas | hob1 | #C9A040 | 矮人;都林一族 | 病:龙病（对黄金的执念） | thorin:孙子
> 索林的祖父，孤山昔日的国王，被黄金迷了心。
goblinking | 半兽人大王 | The Great Goblin | 迷雾山脉的地精王 | Barry Humphries | hob1 | #8A7A5A | 地精;迷雾山脉 | 特征:下巴上挂着一个肉瘤
> 迷雾山脉地底的地精王，挺着大肚子，下巴上挂着个大肉瘤。
trolls | 三巨怪 | The Three Trolls | 伯特、汤姆和威廉 | - | hob1 | #6A7A6A | 食人妖 | 弱点:太阳一出来就变成石头 | gandalf:用日出骗倒他们的人
> 想把矮人做成炖菜的三个食人妖，吵着吵着，太阳出来了。
# —— 洛汗之战
helm | 圣盔·锤手 | Helm Hammerhand | 洛汗的古王 | Brian Cox | rohirrim | #8A6A3A | 人类;洛汗 | 传说:圣盔谷就是以他命名 | hera:女儿;wulf:宿敌
> 洛汗第九代国王，力大无穷，赤手空拳就能打死人。圣盔谷就是以他的名字命名的。
hera | 希拉 | Héra | 圣盔之女 | Gaia Wise | rohirrim | #A07A4A | 人类;洛汗 | 特点:骑马、自由、不肯被安排婚事 | helm:父亲;wulf:儿时玩伴
> 圣盔王的女儿，比谁都爱自由。家族危难时，她扛起了整个洛汗。
wulf | 伍尔夫 | Wulf | 黑蛮地之主 | Luke Pasqualino | rohirrim | #5A4A4A | 人类;黑蛮地 | 执念:为父复仇 | hera:儿时玩伴;helm:宿敌
> 希拉的儿时玩伴，为父报仇，带着大军围攻洛汗。
"""

DECKS = """
fellowship | 护戒远征队 | The Fellowship | 💍 | frodo sam merry pippin gandalf aragorn legolas gimli boromir
hobbits | 四个霍比特人 | The Four Hobbits | 🍄 | frodo sam merry pippin
company | 索林的队伍 | Thorin and Company | 🪓 | thorin balin dwalin fili kili dori nori ori oin gloin bifur bofur bombur bilbo_f gandalf
durin | 都林一族 | Line of Durin | 👑 | thror thorin fili kili dain
bearers | 持戒人 | Ring-bearers | 🔥 | isildur deagol gollum bilbo_h frodo sam
bilbos | 两代比尔博 | Two Bilbos | 📖 | bilbo_h bilbo_f
council | 白道会 | The White Council | 🕊 | gandalf saruman galadriel elrond radagast
wizards | 巫师 | The Istari | 🧙 | gandalf saruman radagast
elves | 精灵 | The Elves | 🍃 | galadriel elrond arwen legolas thranduil tauriel haldir celeborn
rohan | 洛汗 | Rohan | 🐎 | theoden eowyn eomer wormtongue shadowfax
gondor | 刚铎 | Gondor | 🌳 | aragorn boromir faramir denethor isildur
mordor | 魔多与艾辛格 | Mordor & Isengard | 👁 | sauron saruman witchking nazgul lurtz gothmog wormtongue
monsters | 中土的怪物 | Monsters of Middle-earth | 🐉 | smaug balrog shelob trolls goblinking azog
fiveArmies | 五军之战 | Battle of Five Armies | ⚔ | thorin bard thranduil dain azog bolg beorn
laketown | 长湖镇 | Lake-town | 🛶 | bard master alfrid
helmsdeep | 圣盔谷之战 | Helm's Deep | 🛡 | aragorn legolas gimli theoden eomer haldir
oldrohan | 洛汗之战 | War of the Rohirrim | 🏔 | helm hera wulf
loves | 跨越种族的爱 | Unlikely Loves | 💞 | aragorn arwen kili tauriel faramir eowyn sam rosie
creatures | 中土的生灵 | Creatures | 🦅 | treebeard shadowfax eagle beorn
"""

RARE = {"UR": "frodo sam gandalf aragorn legolas gollum bilbo_f thorin"}
