U = dict(id="madmax", n="疯狂的麦克斯", en="Mad Max", short="WASTELAND",
         tag="见证我！从澳大利亚公路上的警察，到荒原上燃烧的战争钻机。",
         theme=["#D0702E", "#E8C890", "#1A100A"], timeline=True, wd=["Q3275141"])
ORDER = 19

WORKS = """
## max | 麦克斯三部曲 | The Mel Gibson Era
mm1 | Mad Max | 1979 | 疯狂的麦克斯 | tl=1 tll=文明崩溃前夕
mm2 | The Road Warrior | 1981 | 疯狂的麦克斯2 | tl=2 tll=末日之后
mm3 | Mad Max: Beyond Thunderdome | 1985 | 疯狂的麦克斯3：超越雷霆 | tl=3 tll=末日十五年后
## wasteland | 荒原传奇 | The Wasteland Saga
fur | Furiosa: A Mad Max Saga | 2024 | 疯狂的麦克斯：狂暴女神 | tl=4 tll=狂暴之路之前的十五年
fr | Mad Max: Fury Road | 2015 | 疯狂的麦克斯4：狂暴之路 | tl=5 tll=不死老乔的城堡
"""

CHARS = """
max | 麦克斯 | Max Rockatansky | 梅尔·吉布森版 | Mel Gibson | mm1 mm2 mm3 | #6A5A3A | 前公路巡警;荒原流浪者 | 座驾:V8 截击者;往事:失去了妻儿;伙伴:一条澳洲牧牛犬 | goose:搭档;jessie:妻子;toecutter:仇人;feralkid:救下的野孩子;gyro:不打不相识;interceptor:座驾;max_h:另一个麦克斯
> 澳大利亚公路上的巡警，失去家人后开着黑色截击者，消失在了荒原尽头。从此他只是一个“路过的人”，却一次又一次救了别人。
max_h | 麦克斯 | Max Rockatansky | 汤姆·哈迪版 | Tom Hardy | fr | #5A5A4A | 荒原流浪者;血袋 | 状态:被抓去当“血袋”;特点:几乎不说话、被幻觉困扰 | furiosa_t:并肩逃亡的战友;nux:从敌人到朋友;max:另一个麦克斯
> 被战争男孩抓去当“血袋”的流浪者，嘴上戴着铁笼，整部电影说不到几句话。最后，他告诉芙莉欧萨，往回走。
furiosa_t | 芙莉欧萨 | Imperator Furiosa | 查理兹·塞隆版 · 将军 | Charlize Theron | fr | #8A6A4A | 不死老乔的将军;来自绿色之地 | 军衔:将军（统帅）;座驾:战争钻机;特点:机械左臂、额头抹着机油 | max_h:并肩逃亡的战友;joe:背叛的主人;splendid:护送的人;furiosa_a:年轻时的自己;warrig:座驾
> 剃着光头、额头抹黑的独臂女将军，开着战争钻机带五个妻子逃离城堡。她想回家，回到那个叫“绿色之地”的地方。
furiosa_a | 芙莉欧萨 | Furiosa | 安雅·泰勒-乔伊版 · 少女时代 | Anya Taylor-Joy; Alyla Browne | fur | #9A7A4A | 绿色之地;不死老乔的城堡 | 往事:小时候被抓离家乡;誓言:回家，报仇 | dementus:杀母仇人;jack:导师与心上人;mary:母亲;joe:城堡的主人;furiosa_t:后来的自己
> 小时候被掳出绿色之地的女孩，在荒原上熬了十五年。她一直记着回家的路，也记着仇人的脸。
joe | 不死老乔 | Immortan Joe | 城堡的统治者 | Hugh Keays-Byrne; Lachy Hulme | fur fr | #D0D0C0 | 城堡;军阀 | 特征:呼吸面罩、白色身体、骷髅牙;控制:水源;口头禅:不要沉迷于水 | splendid:最宠爱的妻子;rictus:儿子;nux:崇拜他的战争男孩;furiosa_t:背叛他的将军
> 掌控水源的城堡统治者，戴着骷髅牙呼吸面罩，被战争男孩们当成神。
nux | 纳克斯 | Nux | 战争男孩 | Nicholas Hoult | fr | #E0E0D0 | 战争男孩 | 梦想:光荣战死、进入英灵殿;口头禅:见证我！;特点:喷银漆、脖子上的肿瘤叫拉里和巴里 | joe:崇拜的人;capable:让他重新想活下去的人;max_h:他的血袋
> 一心想光荣战死的战争男孩，往嘴上喷银漆、大喊“见证我”。后来他遇到一个红发女孩，第一次想活下去。
dementus | 迪门图斯 | Dementus | 摩托军团首领 | Chris Hemsworth | fur | #8A6A3A | 摩托军团;军阀 | 座驾:三辆摩托拉的战车;标志:破泰迪熊、白斗篷;特点:话多、爱演讲 | furiosa_a:被他掳走的女孩;joe:争夺地盘的对手
> 拿着破泰迪熊、坐着摩托战车的军阀，滔滔不绝、疯得彻底。他是芙莉欧萨所有仇恨的起点。
jack | 禁卫军杰克 | Praetorian Jack | 战争钻机驾驶员 | Tom Burke | fur | #5A5A4A | 不死老乔的城堡 | 职业:战争钻机的禁卫军司机 | furiosa_a:学徒与心上人
> 教芙莉欧萨开战争钻机的沉默老兵，也是荒原上少有的好人。
mary | 玛丽·贾巴萨 | Mary Jabassa | 芙莉欧萨的母亲 | Charlee Fraser | fur | #6A7A4A | 绿色之地 | 武器:狙击步枪 | furiosa_a:女儿
> 为了追回女儿，独自骑马穿越荒原的母亲。
toecutter | 剪趾者 | Toecutter | 飞车党首领 | Hugh Keays-Byrne | mm1 | #6A4A3A | 飞车党 | max:复仇对象
> 第一部里的飞车党老大，演员正是后来的不死老乔。
goose | 古斯 | Jim Goose | 麦克斯的搭档 | Steve Bisley | mm1 | #6A6A3A | 公路巡警 | max:搭档
> 麦克斯在巡警队的搭档，骑摩托的热血汉子。
jessie | 杰西 | Jessie Rockatansky | 麦克斯的妻子 | Joanne Samuel | mm1 | #A08A6A | 平民 | max:丈夫
> 麦克斯的妻子，和他有一个刚出生的孩子。
humungus | 洪麦格斯 | Lord Humungus | 荒原之王 | Kjell Nilsson | mm2 | #6A6A5A | 掠夺者 | 特征:冰球面具、肌肉
> 戴着冰球面具的掠夺者首领，自称“荒原之王”。
wez | 维兹 | Wez | 洪麦格斯的手下 | Vernon Wells | mm2 | #8A3A3A | 掠夺者 | 造型:红色莫西干头
> 顶着红色莫西干头的狂暴摩托手。
feralkid | 野孩子 | Feral Kid | 会扔回旋镖的孩子 | Emil Minty | mm2 | #A08A5A | 荒原 | 武器:金属回旋镖;后来:北方部落的首领（第二部的旁白） | max:救下他的人
> 不说话、扔着金属回旋镖的野孩子。多年后，他成了讲述麦克斯传说的人。
gyro | 旋翼机长 | Gyro Captain | 开旋翼机的骗子 | Bruce Spence | mm2 mm3 | #8A7A5A | 荒原 | 座驾:旋翼机;第三部:飞行员杰迪代亚 | max:不打不相识
> 开着小旋翼机的瘦高个，满嘴跑火车，最后救了大家。
aunty | 安蒂·恩缇缇 | Aunty Entity | 巴特镇的统治者 | Tina Turner | mm3 | #C8B07A | 巴特镇 | 造型:锁子甲长裙、蓬松卷发 | max:被她扔进雷霆圆顶的人
> 统治巴特镇的女王，蒂娜·特纳一身锁子甲，还唱了主题曲。
masterblaster | 大师与爆破手 | Master Blaster | 地下城的主人 | Angelo Rossitto; Paul Larsson | mm3 | #6A6A6A | 巴特镇 | 组合:侏儒“大师”骑在巨人“爆破手”肩上
> 坐在巨人肩上的侏儒“大师”，控制着巴特镇的能源。
doof | 吉他手 | The Doof Warrior | 喷火吉他战士 | iOTA | fr | #C83A2A | 战争男孩 | 武器:会喷火的双颈吉他;座驾:挂满音箱的战车
> 被绑在一面音箱墙前、弹着喷火吉他的战士，为整支车队演奏战歌。这个角色的存在，就是荒原的浪漫。
rictus | 瑞克图斯 | Rictus Erectus | 不死老乔的儿子 | Nathan Jones | fur fr | #8A8A7A | 城堡 | 体型:巨人;特点:心智像个孩子 | joe:父亲
> 不死老乔的大块头儿子，力大无穷，心智像个小孩。
slit | 斯利特 | Slit | 战争男孩 | Josh Helman | fr | #5A5A4A | 战争男孩 | 特点:嘴角被割开 | nux:搭档
> 和纳克斯一起开车的战争男孩，嘴角被割开了一道。
scrotus | 斯克罗特斯 | Scrotus | 不死老乔的儿子 | Josh Helman | fur | #6A6A5A | 城堡 | joe:父亲
> 不死老乔的另一个儿子，暴戾凶残。
splendid | 斯普兰迪德 | The Splendid Angharad | 最宠爱的妻子 | Rosie Huntington-Whiteley | fr | #E0D0C0 | 五位妻子 | 口号:我们不是东西！ | joe:她逃离的人;furiosa_t:救她的人
> 不死老乔最宠爱的妻子，怀着身孕挡在姐妹们前面。“我们不是东西！”
toast | 托斯特 | Toast the Knowing | 五位妻子 | Zoë Kravitz | fr | #8A6A5A | 五位妻子
> 五位妻子里最清醒也最强硬的一个。
capable | 凯普勒 | Capable | 五位妻子 | Riley Keough | fr | #C8603A | 五位妻子 | 特征:红发 | nux:让他想活下去的人
> 红发的妻子，在战争钻机里遇见了躲起来的纳克斯。
cheedo | 奇多 | Cheedo the Fragile | 五位妻子 | Courtney Eaton | fr | #E0B0A0 | 五位妻子
> 五位妻子里最年轻、最胆小的一个，最后却最勇敢。
dag | 达格 | The Dag | 五位妻子 | Abbey Lee | fr | #D0C0A0 | 五位妻子 | 特点:总说些奇怪的话
> 五位妻子里说话神神叨叨的一个，在路上和老婆婆们学会了种子的意义。
peopleeater | 食人者 | The People Eater | 天然气城的主人 | John Howard; Lee Perry | fur fr | #8A6A5A | 天然气城 | joe:盟友
> 天然气城的胖统治者，乳头上夹着夹子，满脑子算账。
bulletfarmer | 子弹农夫 | The Bullet Farmer | 子弹农场的主人 | Richard Carter | fr | #6A5A3A | 子弹农场 | joe:盟友
> 掌控子弹农场的军阀，后来被打瞎了眼，在夜里乱开枪。
valkyrie | 瓦尔基里 | The Valkyrie | 绿色之地的女孩 | Megan Gale | fr | #8A9A7A | 绿色之地 | furiosa_t:同乡
> 绿色之地的女战士，赤身站在电塔上引诱敌人。
history | 历史人 | The History Man | 记住一切的人 | George Shevtsov | fur | #8A8A7A | 迪门图斯的人 | 身上:纹满了旧世界的知识
> 把旧世界的知识纹在身上的老人。
interceptor | 截击者 | V8 Interceptor | 麦克斯的车 | - | mm1 mm2 fr | #2A2A2A | 座驾 | 型号:1973 福特猎鹰 XB GT;特点:引擎盖上的增压器 | max:主人
> 麦克斯的黑色福特猎鹰，引擎盖上突出一个增压器，是荒原上最有名的车。
warrig | 战争钻机 | The War Rig | 移动的堡垒 | - | fur fr | #6A4A3A | 座驾 | 构造:油罐车 + 推土机 + 雪佛兰半挂车头;任务:往返于城堡、天然气城和子弹农场 | furiosa_t:驾驶员;jack:驾驶员
> 一辆开起来像战舰的巨型油罐车，两代芙莉欧萨都开过它。
"""

DECKS = """
maxes | 两代麦克斯 | Two Maxes | 🛣 | max max_h
furiosas | 两代芙莉欧萨 | Two Furiosas | 🦾 | furiosa_a furiosa_t
wives | 五位妻子 | The Five Wives | 💍 | splendid toast capable cheedo dag
warboys | 战争男孩 | War Boys | 💀 | nux slit doof rictus
citadel | 城堡与盟友 | The Citadel | 🏰 | joe rictus scrotus peopleeater bulletfarmer
fury | 狂暴之路 | Fury Road | 🔥 | max_h furiosa_t nux joe doof splendid
saga | 狂暴女神 | Furiosa | 🧸 | furiosa_a dementus jack mary history joe
old | 老麦克斯的旅程 | The Road | 🐕 | max goose jessie toecutter feralkid gyro
thunderdome | 超越雷霆 | Beyond Thunderdome | ⚡ | max aunty masterblaster gyro
rides | 荒原座驾 | Wasteland Rides | 🚛 | interceptor warrig
green | 绿色之地 | The Green Place | 🌱 | furiosa_t furiosa_a mary valkyrie
"""

RARE = {"UR": "max max_h furiosa_t furiosa_a"}
