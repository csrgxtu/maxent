## 囚徒困境
## 摘要
囚徒困境（Prisoner's Dilemma）是博弈论的非零和博弈中具代表性的例子，反映个人最佳选择并非团体最佳选择。或者说在一个群体中，个人做出理性选择却往往导致集体的非理性。虽然困境本身只属模型性质，但现实中的价格竞争、环境保护等方面，也会频繁出现类似情况。

单次发生的囚徒困境，和多次重复的囚徒困境结果不会一样。

在重复的囚徒困境中，博弈被反复地进行。因而每个参与者都有机会去“惩罚”另一个参与者前一回合的不合作行为。这时，合作可能会作为均衡的结果出现。欺骗的动机这时可能被受到惩罚的威胁所克服，从而可能导向一个较好的、合作的结果。作为反复接近无限的数量，纳什均衡趋向于帕累托最优。

囚徒困境的主旨为，囚徒们彼此合作，坚不吐实，可为全体带来最佳利益（无罪开释），但在无法沟通的情况下，因为出卖同伙可为自己带来利益（缩短刑期），也因为同伙把自己招出来可为他带来利益，因此彼此出卖虽违反最佳共同利益，反而是自己最大利益所在。但实际上，执法机构不可能设立如此情境来诱使所有囚徒招供，因为囚徒们必须考虑刑期以外之因素（出卖同伙会受到报复等），而无法完全以执法者所设立之利益（刑期）作考量。

## 经典的囚徒困境
1950年，由就职于兰德公司的梅里尔·弗勒德（Merrill Flood）和梅尔文·德雷希尔（Melvin Dresher）拟定出相关困境的理论，后来由顾问艾伯特·塔克（Albert Tucker）以囚徒方式阐述，并命名为“囚徒困境”。经典的囚徒困境如下：  
警方逮捕甲、乙两名嫌疑犯，但没有足够证据指控二人有罪。于是警方分开囚禁嫌疑犯，分别和二人见面，并向双方提供以下相同的选择：

* 若一人认罪并作证检控对方（相关术语称“背叛”对方），而对方保持沉默，此人将即时获释，沉默者将判监10年。
* 若二人都保持沉默（相关术语称互相“合作”），则二人同样判监半年。
* 若二人都互相检举（互相“背叛”），则二人同样判监5年。

用表格概述如下：

![table1](https://raw.githubusercontent.com/csrgxtu/maxent/master/static/img/prison1.png)

## 解说
如同博弈论的其他例证，囚徒困境假定每个参与者（即“囚徒”）都是利己的，即都寻求最大自身利益，而不关心另一参与者的利益。参与者某一策略所得利益，如果在任何情况下都比其他策略要低的话，此策略称为“严格劣势”，理性的参与者绝不会选择。另外，没有任何其他力量干预个人决策，参与者可完全按照自己意愿选择策略。

囚徒到底应该选择哪一项策略，才能将自己个人的刑期缩至最短？两名囚徒由于隔绝监禁，并不知道对方选择；而即使他们能交谈，还是未必能够尽信对方不会反口。就个人的理性选择而言，检举背叛对方所得刑期，总比沉默要来得低。试设想困境中两名理性囚徒会如何作出选择：
* 若对方背叛指控我，我也要指控对方才能得到较低的刑期，所以也是会选择背叛。
* 若对方沉默、我背叛会让我获释，所以会选择背叛。

二人面对的情况一样，所以二人的理性思考都会得出相同的结论——选择背叛。背叛是两种策略之中的支配性策略。因此，这场博弈中唯一可能达到的纳什均衡，就是双方参与者都背叛对方，结果二人同样服刑5年。

这场博弈的纳什均衡，显然不是顾及团体利益的帕累托最优解决方案。以全体利益而言，如果两个参与者都合作保持沉默，两人都只会被判刑半年，总体利益更高，结果也比两人背叛对方、判刑5年的情况较佳。但根据以上假设，二人均为理性的个人，且只追求自己个人利益。均衡状况会是两个囚徒都选择背叛，结果二人判监均比合作为高，总体利益较合作为低。这就是“困境”所在。例子有效地证明了：非零和博弈中，帕累托最优和纳什均衡是互相冲突的。

## 固定局数的囚徒困境
概括而言囚徒困境进行第一次后会出现以下两种情况：

甲在第一次中被乙指控，即会在第二次指控乙，最终导致，甲即时获释，乙服刑10年或二人同服刑2年这两种情况。

双方均保持沉默，即会建立互信的关系，最终导致，二人同服刑半年。

但互信的关系并非牢不可破，这一点也可以被利用，即甲，乙在第一次中共同选择沉默而赢得对方的信任，但甲或乙中的一人在获得对方的信任后指控对方而获得自身最大的利益即自身即时获释，但对方将服刑10年。这是一个以牺牲对方利益而获得自身最大利益的一种策略。

假设，两个囚徒均欲利用此策略，并将局数推演为十次，那么就会出现如下的情况：在第一局到第九局的过程中双方均会保持沉默，以期望建立互信关系，并在第十局指控对方，这将最终导致，二人同服刑5年。

再一次假设，双方都明确对方会使用与自己同样的策略，即知道对方会在第十局中指控自己，这样，在第九局时两者间的信任关系的建立即是没有意义的，如此类推，第八局到第一局中信任关系的建立也是没有意义的，即是十局都会互相背叛，也就是纳什均衡。也可推论，在如此的情况下，只有在囚徒困境的局数在不肯定的情况下（即双方均不知道进行的局数），才会出现互相保持沉默以获得信任关系的现象。

## 一般形式
整理囚徒困境的基本博弈结构，可更清楚地分析囚徒困境。实验经济学常用这种博弈的一般形式分析各种论题。以下是实现一般形式的其中一例：

有两个参与者和一个庄家。参与者每人有一式两张卡片，各印有“合作”和“背叛”。参与者各把一张卡片文字面朝下，放在庄家面前。文字面朝下排除了参与者知道对方选择的可能性1。然后，庄家翻开两个参与者卡片，根据以下规则支付利益：
* 一人背叛、一人合作：背叛者得5分（背叛诱惑），合作者0分（受骗支付）。
* 二人都合作：各得3分（合作报酬）。
* 二人都背叛：各得1分（背叛惩罚）。

若以T（Temptation）=背叛诱惑，R（Reward）=合作报酬，P（Punishment）=背叛惩罚，S（Suckers）=受骗支付，以个人选择得分而言，可得出以下不等式。

T>R>P>S
（解：从5>3>1>0获得以上不等式）

若以整体获分而言，将得出以下不等式。
2R>T+S或2R>2P
（解：2×3>5+0或2×3>2x1；合作2人共得6分，比起互相背叛的共得2分及单独背叛的共得5分，显然合作获分比背叛高。合作在团体而言是支配性策略。）

而重复博弈或重复的囚徒困境将会使参与者从注重T>R>P>S转变成注重2R>T+S。就是说将使参与者脱离困境。 以上理论是道格拉斯·霍夫施塔特创建的。

## 现实的例子
上述例子可能显得不甚自然，但现实中，无论是人类社会或大自然都可以找到类似囚徒困境的例子，将结果划成同样的支付矩阵。社会科学中的经济学、政治学和社会学，以及自然科学的动物行动学、进化生物学等学科，都可以用囚徒困境分析，模拟生物面对无止境的囚徒困境博弈。囚徒困境可以广为使用，说明这种博弈的重要性。以下为各界例子：

### 政治学例子：军备竞赛
在政治学中，两国之间的军备竞赛可以用囚徒困境来描述。两国都可以声称有两种选择：增加军备（背叛）、或是达成削减武器协议（合作）。两国都无法肯定对方会遵守协议，因此两国最终会倾向增加军备。似乎自相矛盾的是，虽然增加军备会是两国的“理性”行为，但结果却显得“非理性”（例如会对经济造成损坏等）。这可视作遏制理论的推论，就是以强大的军事力量来遏制对方的进攻，以达到和平。

### 经济学例子：关税战
两个国家，在关税上可以有以两个选择:
* 提高关税，以保护自己的商品。（背叛）
* 与对方达成关税协定，降低关税以利各自商品流通。（合作)

当一国因某些因素不遵守关税协定，而独自提高关税（背叛）时，另一国也会作出同样反应（亦背叛），这就引发了关税战，两国的商品失去了对方的市场，对本身经济也造成损害（共同背叛的结果）。然后二国又重新达成关税协定。（重复博弈的结果是将发现共同合作利益最大。）

### 商业例子：广告战
商业活动中亦会出现各种囚徒困境例子。以广告竞争为例。

两个公司互相竞争，二公司的广告互相影响，即一公司的广告较被顾客接受则会夺取对方的部分收入。但若二者同时期发出质量类似的广告，收入增加很少但成本增加。但若不提高广告质量，生意又会被对方夺走。

此二公司可以有二选择：
* 互相达成协议，减少广告的开支。（合作）
* 增加广告开支，设法提升广告的质量，压倒对方。（背叛）

若二公司不信任对方，无法合作，背叛成为支配性策略时，二公司将陷入广告战，而广告成本的增加损害了二公司的收益，这就是陷入囚徒困境。在现实中，要二互相竞争的公司达成合作协议是较为困难的，多数都会陷入囚徒困境中。

### 自行车赛例子
自行车赛事的比赛策略也是一种博弈，而其结果可用囚徒困境的研究成果解释。例如每年都举办的环法自行车赛中有以下情况：选手们在到终点前的路程常以“大队伍”（法语：peloton） 方式前进，他们采取这策略是为了令自己不至于太落后，又出力适中。而最前方的选手在迎风时是最费力的，所以选择在前方是最差的策略。通常会发生这样的情况，大家起先都不愿意向前（共同背叛），这使得全体速度很慢，而后通常会有二或多位选手骑到前面，然后一段时间内互相交换最前方位置，以分担风的阻力（共同合作），使得全体的速度有所提升，而这时如果前方的其中一人试图一直保持前方位置（背叛），其他选手以及大队伍就会赶上（共同背叛）。而通常的情况是，在最前面次数最多的选手（合作）通常会到最后被落后的选手赶上（背叛），因为后面的选手骑在前面选手的冲流之中，比较不费力。

## 与囚徒困境相关的各事件
### 异想
威廉·庞德斯通（William Poundstone）在他的著作中，以一新西兰的例子来说明囚徒困境。在新西兰，报亭既无管理员也不上锁，买报纸的人自行放下钱后拿走报纸。当然某些人可能取走报纸却不付钱（背叛），但由于大家认识到如果每个人都偷窃报纸（共同背叛）会造成以后不方便的有害结果，这种情形很少发生。这例子特别之处是新西兰人并没有被任何其他因素影响而能脱离囚徒困境。并没有任何人特别去注意报亭，人们守规则是为了避免共同背叛带来的恶果。这种避免囚徒困境的大家共同的推理或想法被称为“异想（magical thinking）”.

### “认罪减刑”不可行
囚徒困境的结论是许多国家中认罪减刑（英文：plea bargain）被禁止的原因之一。囚徒困境带来的结论是：如果有二个罪犯，其中一人犯罪而另外一人是无辜的，犯罪者会为了减刑坦白一切甚至冤枉清白者（单独背叛）。最糟糕的情况是，如果他们二人都被判入狱，坦白的犯罪者刑期少，坚持无罪的冤枉者刑期反而更多。

### 公用品悲剧
现实的博弈参与者不只一方，会有多方参与的囚徒困境。加勒特·詹姆斯·哈丁（Garrett James Hardin）的公用品悲剧就是一例：“公用品悲剧是指凡是属于最多数人的公共财产常常是最少受人照顾的事物”，例如渔业，公海中的鱼是属于公共的，而在本身不滥捕其他人也滥捕的思想下，渔民会没有节制的大捞特捞，结果海洋生态破坏，渔民的生计也受影响（共同背叛的结果）。但是，多方囚徒困境的提法有待商榷，因为其总是可以被分解为一组组经典的二方囚徒困境。就是说只有二方的囚徒困境，没有多方的。所谓多方的囚徒困境只是由多个二方囚徒困境混杂在一起而形成的错觉。

## 重复的囚徒困境
美国政治学家罗伯特·阿克塞尔罗德（Robert Marshall Axelrod）在其著作《合作的进化》（The Evolution of Cooperation）中，探索了经典囚徒困境情景的一个扩展，并把它称作“重复的囚徒困境”（IPD）。在这个博弈中，参与者必须反复地选择他们彼此相关的策略，并且记住他们以前的对抗。阿克塞尔罗德邀请全世界的学术同行来设计计算机策略，并在一个重复囚徒困境竞赛中互相竞争。参赛的程序的差异广泛地存在于这些方面：算法的复杂性、最初的对抗、宽恕的能力等等。

阿克塞尔罗德发现，当这些对抗被每个选择不同策略的参与者一再重复了很长时间之后，从利己的角度来判断，最终“贪婪”策略趋向于减少，而比较“利他”策略更多地被采用。他用这个博弈来说明，通过自然选择，一种利他行为的机制可能从最初纯粹的自私机制进化而来。

最佳确定性策略被认为是“以牙还牙”，这是俄裔美籍数学心理学家阿纳托尔·拉波波特（Anatol Rapoport）开发并运用到锦标赛中的方法。它是所有参赛程序中最简单的，只包含了四行BASIC语言，并且赢得了比赛。这个策略只不过是在重复博弈的开头合作，然后，采取你的对手前一回合的策略。更好些的策略是“宽恕地以牙还牙”。当你的对手背叛，在下一回合中你无论如何要以小概率（大约是1%-5%）时而合作一下。这是考虑到偶尔要从循环背叛的受骗中复原。当错误传达被引入博弈时，“宽恕地以牙还牙”是最佳的。这意味着有时你的动作被错误地传达给你的对手：你合作但是你的对手听说你背叛了。

通过分析高分策略，阿克塞尔罗德指定了策略获得成功的几个必要条件。

友善：最重要的条件是策略必须“友善”，这就是说，不要在对手背叛之前先背叛。几乎所有的高分策略都是友善的。因此，完全自私的策略仅仅出于自私的原因，也永远不会首先打击其对手。

报复：但是，阿克斯洛德主张，成功的策略必须不是一个盲目乐观者。要始终报复。一个非报复策略的例子是始终合作。这是一个非常糟糕的选择，因为“下流”策略将残酷地剥削这样的傻瓜。

宽恕：成功策略的另一个品质是必须要宽恕。虽然它们不报复，但是如果对手不继续背叛，它们会一再退却到合作。这停止了报复和反报复的长期进行，最大化了得分点数。

不嫉妒：最后一个品质是不嫉妒，就是说不去争取得到高于对手的分数（对于“友善”的策略来说这也是不可能的，也就是说“友善”的策略永远无法得到高于对手的分数）。

因此，阿克塞尔罗德得到一种给人以乌托邦印象的结论，认为自私的个人为了其自私的利益会趋向友善、宽恕和不嫉妒。阿克塞尔罗德关于重复囚徒困境的研究的重要结论之一，是友善的家伙能先完成交易。

重新考虑经典的囚徒困境一节中给定的军备竞赛模型：结论是，只是理性策略增进了军事力量，似乎两个国家都宁可花费其GDP在枪炮而不是黄油上。有趣的是，企图说明对抗国家实际上以这种方式（在“重复囚徒困境假定”下的不同时期，军费支出在“高”和“低”之间反复）竞赛的尝试，却经常表明假定的军备竞赛并没有如预想的那样出现。（例如希腊人和土耳其人的军费支出，看来并不像遵循“以牙还牙”的重复囚徒困境式的军备竞赛，却更可能是被其国内的政策所驱使。）这可能是一次性博弈和重复性博弈中的理性行为不同的例子。

对一次性囚徒困境博弈来说，最佳（点数最大化的）策略是简单地背叛；正如前面解释的，无论对手的行动可能是什么，这都是真实的。但是，在重复的囚徒困境博弈中，最佳策略依赖于可能的对手的策略，和他们怎样对背叛和合作作出反应。例如，考虑这样一个人群，那里每个人每次都背叛，除了一个人是遵循以牙还牙策略。这个人处于一种轻微的不利地位，因为第一回合的损失。在这样的人群中，对这个人来说最佳策略就是每次都背叛。在一个有一定的百分比的总背叛者而剩下的则是以牙还牙者的人群中，对个人来说的最佳策略依赖于这个百分比和博弈的长度。

一般有两种方法得到最佳策略：
* 贝叶斯纳什均衡：如果对抗策略的统计分布能被确定（例如，50％以牙还牙，50％一直合作），就能从数学上获得最佳的相对策略[4]。
* 已经有了人群的蒙特卡罗模拟，在这里低分个人消失了，高分个人一再被生产出来（一种获得最佳策略的天才算法）。决赛人群中的算法合成通常依赖于初赛人群中的算法合成。

尽管以牙还牙始终被认为是最可靠的基本策略，但是在重复囚徒困境的20周年纪念赛中，来自英国南安普敦大学的一个小组（由尼古拉斯·詹宁斯（Nicholas Jennings）领导[1]，包括了拉蒂普·达什（Rajdeep Dash）、萨瓦帕里·拉姆琼（Sarvapali Ramchurn）、亚历克斯·罗杰斯（Alex Rogers）斯和皮鲁克里士南·维特林根（Perukrishnen Vytelingum））介绍了一个新的策略，这个策略证明了它比以牙还牙更成功。这个策略依赖于程序之间的合作，为单一程序中获得了最高的点数。南安普敦大学提交了60个程序参与竞赛，这些程序的开头被设计成通过一组5到10个的动作去彼此识别。一旦这些识别被作出，一个程序将总是合作，其他程序则总是背叛，保证背叛者得到最大的点数。如果程序识别出它在操作一个非南安普敦参与者，这程序将持续地背叛，企图去最小化竞争程序的得分。结果[5]，这个策略以获得前3位结束了竞赛，也得到了大量接近底部的位置。虽然这个策略显著地证明了比以牙还牙有效，但是这是因为利用了下述事实：在这个特殊的竞赛中，多重通道是被允许的。在一方只能控制单一参与者的竞赛中，以牙还牙确实是更好的策略。

如果重复囚徒困境将被精确地重复N次，已知N是一个常数，那么会产生另一个有趣的事实。纳什均衡就是每次都背叛。这很容易用归纳法证明。你也可以在最后的回合背叛，既然你的对手将没有机会惩罚你。因此，你们都将在最后的回合背叛。这时，你可以在倒数第二回合中背叛，既然最后一回无论你做什么，你的对手都将背叛。依此类推。为了合作以保持请求，这时未来必须对两个参与者来说是不确定的。一个解决方案是让博弈总次数N变成随机的。对未来的预期必须是无法确定的长度。

另一个单独的案例是“永不停止”的囚徒困境。这个博弈被重复很多次，而且你的分数是一个平均数（当然是用计算机计算的）。

囚徒困境博弈是某些人类合作和信任理论的基础。假定囚徒困境能够模拟需要信任的两人之间的交流，群体的合作行为可以用有多个参与者的、重复博弈的变体来模拟。这从而引起了许许多多学者经久不衰的兴趣。1975年，格罗夫曼（Grofman）和普尔（Pool）估计，致力于这方面研究的学术文章，数量超过2000篇。

## 学习心理学和博弈论
当博弈参与者能学会估计其他参与者背叛的可能性，他们自身的行为就为他们关于其他人的经验所影响。简单的统计显示，总体上，缺乏经验的参与者与其他参与者的互动，或者是典型的好，或者是典型的坏。如果他们在这些经验的基础上行动，（通过更多的背叛或合作，否则）他们可能在未来的交易中受损。随着经验逐渐丰富，他们获得了对背叛可能性的更真实的印象，变得更成功地参与博弈。不成熟的参与者经历的早期交易对他们未来参与的影响，可能比这些交易对成熟的参与者的影响要大得多。这个原理部分地解释了，为什么年轻人的成长经验这么具有影响力，以及为什么他们特别容易被欺负，有时他们本身最后也成为欺凌弱小者。

群体中背叛的可能性，可以被合作的经验所削弱[6]，因为先前的博弈建立了信任。因此自我牺牲行为可以，例如，加强团体的道德品质。如果团体很小，积极行为更可能以互相肯定的方式——鼓励这个团体中的个人继续合作——得到反馈。这与相似的困境有关：鼓励那些你将援助的人，从可能使他们处于危险的境地的行为中得到满足。这类方法主要在互惠利他主义、群选择、血缘选择和道德哲学的研究中涉及。


## 参考文献
[囚徒困境](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma)


## Prisoner's dilemma
The prisoner's dilemma is a standard example of a game analyzed in game theory that shows why two completely "rational" individuals might not cooperate, even if it appears that it is in their best interests to do so. It was originally framed by Merrill Flood and Melvin Dresher working at RAND in 1950. Albert W. Tucker formalized the game with prison sentence rewards and named it, "prisoner's dilemma" (Poundstone, 1992), presenting it as follows:

Two members of a criminal gang are arrested and imprisoned. Each prisoner is in solitary confinement with no means of communicating with the other. The prosecutors lack sufficient evidence to convict the pair on the principal charge. They hope to get both sentenced to a year in prison on a lesser charge. Simultaneously, the prosecutors offer each prisoner a bargain. Each prisoner is given the opportunity either to: betray the other by testifying that the other committed the crime, or to cooperate with the other by remaining silent. The offer is:

* If A and B each betray the other, each of them serves 2 years in prison
* If A betrays B but B remains silent, A will be set free and B will serve 3 years in prison (and vice versa)
* If A and B both remain silent, both of them will only serve 1 year in prison (on the lesser charge)

It is implied that the prisoners will have no opportunity to reward or punish their partner other than the prison sentences they get, and that their decision will not affect their reputation in the future. Because betraying a partner offers a greater reward than cooperating with him, all purely rational self-interested prisoners would betray the other, and so the only possible outcome for two purely rational prisoners is for them to betray each other.[1] The interesting part of this result is that pursuing individual reward logically leads both of the prisoners to betray, when they would get a better reward if they both kept silent. In reality, humans display a systematic bias towards cooperative behavior in this and similar games, much more so than predicted by simple models of "rational" self-interested action.[2][3][4][5] A model based on a different kind of rationality, where people forecast how the game would be played if they formed coalitions and then they maximize their forecasts, has been shown to make better predictions of the rate of cooperation in this and similar games given only the payoffs of the game.[6]

An extended "iterated" version of the game also exists, where the classic game is played repeatedly between the same prisoners, and consequently, both prisoners continuously have an opportunity to penalize the other for previous decisions. If the number of times the game will be played is known to the players, then (by backward induction) two classically rational players will betray each other repeatedly, for the same reasons as the single shot variant. In an infinite or unknown length game there is no fixed optimum strategy, and Prisoner's Dilemma tournaments have been held to compete and test algorithms.

The prisoner's dilemma game can be used as a model for many real world situations involving cooperative behaviour. In casual usage, the label "prisoner's dilemma" may be applied to situations not strictly matching the formal criteria of the classic or iterative games: for instance, those in which two entities could gain important benefits from cooperating or suffer from the failure to do so, but find it merely difficult or expensive, not necessarily impossible, to coordinate their activities to achieve cooperation.

Both cannot communicate, they are separated in two individual rooms. The normal game is shown below:

Here, regardless of what the other decides, each prisoner gets a higher reward by betraying the other ("defecting"). The reasoning involves an argument by dilemma: B will either cooperate or defect. If B cooperates, A should defect, because going free is better than serving 1 year. If B defects, A should also defect, because serving 2 years is better than serving 3. So either way, A should defect. Parallel reasoning will show that B should defect.

In traditional game theory, some very restrictive assumptions on prisoner behaviour are made. It is assumed that both understand the nature of the game, and that despite being members of the same gang, they have no loyalty to each other and will have no opportunity for retribution or reward outside the game. Most importantly, a very narrow interpretation of "rationality" is applied in defining the decision-making strategies of the prisoners. Given these conditions and the payoffs above, prisoner A will betray prisoner B. The game is symmetric, so Prisoner B should act the same way. Since both "rationally" decide to defect, each receives a lower reward than if both were to stay quiet. Traditional game theory results in both players being worse off than if each chose to lessen the sentence of his accomplice at the cost of spending more time in jail himself.

The structure of the traditional Prisoners’ Dilemma can be generalized from its original prisoner setting. Suppose that the two players are represented by the colors, red and blue, and that each player chooses to either "Cooperate" or "Defect".

If both players cooperate, they both receive the reward R for cooperating. If both players defect, they both receive the punishment payoff P. If Blue defects while Red cooperates, then Blue receives the temptation payoff T, while Red receives the "sucker's" payoff, S. Similarly, if Blue cooperates while Red defects, then Blue receives the sucker's payoff S, while Red receives the temptation payoff T.

This can be expressed in normal form: and to be a prisoner's dilemma game in the strong sense, the following condition must hold for the payoffs: T > R > P > S

The payoff relationship R > P implies that mutual cooperation is superior to mutual defection, while the payoff relationships T > R and P > S imply that defection is the dominant strategy for both agents. That is, mutual defection is the only strong Nash equilibrium in the game (i.e. the only outcome from which each player could only do worse by unilaterally changing strategy). The dilemma then is that mutual cooperation yields a better outcome than mutual defection but it is not the rational outcome because from a self-interested perspective, the choice to cooperate, at the individual level, is irrational.

The "donation game"[7] is a form of prisoner's dilemma in which cooperation corresponds to offering the other player a benefit b at a personal cost c with b > c. Defection means offering nothing. The payoff matrix is thus Note that 2R>T+S (i.e. 2(b-c)>b-c) which qualifies the donation game to be an iterated game (see next section).

The donation game may be applied to markets. Suppose X grows oranges, Y grows apples. The marginal utility of an apple to the orange-grower X is b, which is higher than the marginal utility (c) of an orange, since X has a surplus of oranges and no apples. Similarly, for apple-grower Y, the marginal utility of an orange is b while the marginal utility of an apple is c. If X and Y contract to exchange an apple and an orange, and each fulfills their end of the deal, then each receive a payoff of b-c. If one "defects" and does not deliver as promised, the defector will receive a payoff of b, while the cooperator will lose c. If both defect, then neither one gains or loses anything.

If two players play prisoners' dilemma more than once in succession and they remember previous actions of their opponent and change their strategy accordingly, the game is called iterated prisoners' dilemma.

In addition to the general form above, the iterative version also requires that 2R > T + S, to prevent alternating cooperation and defection giving a greater reward than mutual cooperation.

The iterated prisoners' dilemma game is fundamental to some theories of human cooperation and trust. On the assumption that the game can model transactions between two people requiring trust, cooperative behaviour in populations may be modeled by a multi-player, iterated, version of the game. It has, consequently, fascinated many scholars over the years. In 1975, Grofman and Pool estimated the count of scholarly articles devoted to it at over 2,000. The iterated prisoners' dilemma has also been referred to as the "Peace-War game".[8]

If the game is played exactly N times and both players know this, then it is always game theoretically optimal to defect in all rounds. The only possible Nash equilibrium is to always defect. The proof is inductive: one might as well defect on the last turn, since the opponent will not have a chance to later retaliate. Therefore, both will defect on the last turn. Thus, the player might as well defect on the second-to-last turn, since the opponent will defect on the last no matter what is done, and so on. The same applies if the game length is unknown but has a known upper limit.

Unlike the standard prisoners' dilemma, in the iterated prisoners' dilemma the defection strategy is counter-intuitive and fails badly to predict the behavior of human players. Within standard economic theory, though, this is the only correct answer. The superrational strategy in the iterated prisoners' dilemma with fixed N is to cooperate against a superrational opponent, and in the limit of large N, experimental results on strategies agree with the superrational version, not the game-theoretic rational one.

For cooperation to emerge between game theoretic rational players, the total number of rounds N must be random, or at least unknown to the players. In this case 'always defect' may no longer be a strictly dominant strategy, only a Nash equilibrium. Amongst results shown by Robert Aumann in a 1959 paper, rational players repeatedly interacting for indefinitely long games can sustain the cooperative outcome.

Interest in the iterated prisoners' dilemma (IPD) was kindled by Robert Axelrod in his book The Evolution of Cooperation (1984). In it he reports on a tournament he organized of the N step prisoners' dilemma (with N fixed) in which participants have to choose their mutual strategy again and again, and have memory of their previous encounters. Axelrod invited academic colleagues all over the world to devise computer strategies to compete in an IPD tournament. The programs that were entered varied widely in algorithmic complexity, initial hostility, capacity for forgiveness, and so forth.

Axelrod discovered that when these encounters were repeated over a long period of time with many players, each with different strategies, greedy strategies tended to do very poorly in the long run while more altruistic strategies did better, as judged purely by self-interest. He used this to show a possible mechanism for the evolution of altruistic behaviour from mechanisms that are initially purely selfish, by natural selection.

The winning deterministic strategy was tit for tat, which Anatol Rapoport developed and entered into the tournament. It was the simplest of any program entered, containing only four lines of BASIC, and won the contest. The strategy is simply to cooperate on the first iteration of the game; after that, the player does what his or her opponent did on the previous move. Depending on the situation, a slightly better strategy can be "tit for tat with forgiveness." When the opponent defects, on the next move, the player sometimes cooperates anyway, with a small probability (around 1–5%). This allows for occasional recovery from getting trapped in a cycle of defections. The exact probability depends on the line-up of opponents.

By analysing the top-scoring strategies, Axelrod stated several conditions necessary for a strategy to be successful.

** Nice **, The most important condition is that the strategy must be "nice", that is, it will not defect before its opponent does (this is sometimes referred to as an "optimistic" algorithm). Almost all of the top-scoring strategies were nice; therefore, a purely selfish strategy will not "cheat" on its opponent, for purely self-interested reasons first.

** Retaliating **, However, Axelrod contended, the successful strategy must not be a blind optimist. It must sometimes retaliate. An example of a non-retaliating strategy is Always Cooperate. This is a very bad choice, as "nasty" strategies will ruthlessly exploit such players.

** Forgiving **, Successful strategies must also be forgiving. Though players will retaliate, they will once again fall back to cooperating if the opponent does not continue to defect. This stops long runs of revenge and counter-revenge, maximizing points.

** Non-envious **, The last quality is being non-envious, that is not striving to score more than the opponent.

The optimal (points-maximizing) strategy for the one-time PD game is simply defection; as explained above, this is true whatever the composition of opponents may be. However, in the iterated-PD game the optimal strategy depends upon the strategies of likely opponents, and how they will react to defections and cooperations. For example, consider a population where everyone defects every time, except for a single individual following the tit for tat strategy. That individual is at a slight disadvantage because of the loss on the first turn. In such a population, the optimal strategy for that individual is to defect every time. In a population with a certain percentage of always-defectors and the rest being tit for tat players, the optimal strategy for an individual depends on the percentage, and on the length of the game.

In the strategy called Pavlov, win-stay, lose-switch, If the last round outcome was P,P, a Pavlov player switches strategy the next turn, which means P,P would be considered as a failure to cooperate.[citation needed] For a certain range of parameters[specify], Pavlov beats all other strategies by giving preferential treatment to co-players which resemble Pavlov.


Deriving the optimal strategy is generally done in two ways:
* Bayesian Nash Equilibrium: If the statistical distribution of opposing strategies can be determined (e.g. 50% tit for tat, 50% always cooperate) an optimal counter-strategy can be derived analytically.[9]
* Monte Carlo simulations of populations have been made, where individuals with low scores die off, and those with high scores reproduce (a genetic algorithm for finding an optimal strategy). The mix of algorithms in the final population generally depends on the mix in the initial population. The introduction of mutation (random variation during reproduction) lessens the dependency on the initial population; empirical experiments with such systems tend to produce tit for tat players (see for instance Chess 1988), but no analytic proof exists that this will always occur.

Although tit for tat is considered to be the most robust basic strategy, a team from Southampton University in England (led by Professor Nicholas Jennings and consisting of Rajdeep Dash, Sarvapali Ramchurn, Alex Rogers, Perukrishnen Vytelingum) introduced a new strategy at the 20th-anniversary iterated prisoners' dilemma competition, which proved to be more successful than tit for tat. This strategy relied on collusion between programs to achieve the highest number of points for a single program. The university submitted 60 programs to the competition, which were designed to recognize each other through a series of five to ten moves at the start.[10] Once this recognition was made, one program would always cooperate and the other would always defect, assuring the maximum number of points for the defector. If the program realized that it was playing a non-Southampton player, it would continuously defect in an attempt to minimize the score of the competing program. As a result,[11] this strategy ended up taking the top three positions in the competition, as well as a number of positions towards the bottom.

This strategy takes advantage of the fact that multiple entries were allowed in this particular competition and that the performance of a team was measured by that of the highest-scoring player (meaning that the use of self-sacrificing players was a form of minmaxing). In a competition where one has control of only a single player, tit for tat is certainly a better strategy. Because of this new rule, this competition also has little theoretical significance when analysing single agent strategies as compared to Axelrod's seminal tournament. However, it provided the framework for analysing how to achieve cooperative strategies in multi-agent frameworks, especially in the presence of noise. In fact, long before this new-rules tournament was played, Richard Dawkins in his book The Selfish Gene pointed out the possibility of such strategies winning if multiple entries were allowed, but he remarked that most probably Axelrod would not have allowed them if they had been submitted. It also relies on circumventing rules about the prisoners' dilemma in that there is no communication allowed between the two players, which the Southampton programs arguably did with their opening "ten move dance" to recognize one another; this only reinforces just how valuable communication can be in shifting the balance of the game.

In a stochastic iterated prisoner's dilemma game, strategies are specified by in terms of "cooperation probabilities".[12] In an encounter between player X and player Y, X 's strategy is specified by a set of probabilities P of cooperating with Y. P is a function of the outcomes of their previous encounters or some subset thereof. If P is a function of only their most recent n encounters, it is called a "memory-n" strategy. A memory-1 strategy is then specified by four cooperation probabilities: P=\{P_{cc},P_{cd},P_{dc},P_{dd}\}, where P_{ab} is the probability that X will cooperate in the present encounter given that the previous encounter was characterized by (ab). For example, if the previous encounter was one in which X cooperated and Y defected, then P_{cd} is the probability that X will cooperate in the present encounter. If each of the probabilities are either 1 or 0, the strategy is called deterministic. An example of a deterministic strategy is the "tit for tat" strategy written as P={1,0,1,0}, in which X responds as Y did in the previous encounter. Another is the win–stay, lose–switch strategy written as P={1,0,0,1}, in which X responds as in the previous encounter, if it was a "win" (i.e. cc or dc) but changes strategy if it was a loss (i.e. cd or dd). It has been shown that for any memory-n strategy there is a corresponding memory-1 strategy which gives the same statistical results, so that only memory-1 strategies need be considered.[12]

If we define P as the above 4-element strategy vector of X and Q=\{Q_{cc},Q_{cd},Q_{dc},Q_{dd}\} as the 4-element strategy vector of Y, a transition matrix M may be defined for X whose ij th entry is the probability that the outcome of a particular encounter between X and Y will be j given that the previous encounter was i, where i and j are one of the four outcome indices: cc, cd, dc, or dd. For example, from X 's point of view, the probability that the outcome of the present encounter is cd given that the previous encounter was cd is equal to M_{cd,cd}=P_{cd}(1-Q_{dc}). (Note that the indices for Q are from Y 's point of view: a cd outcome for X is a dc outcome for Y.) Under these definitions, the iterated prisoner's dilemma qualifies as a stochastic process and M is a stochastic matrix, allowing all of the theory of stochastic processes to be applied.[12]

One result of stochastic theory is that there exists a stationary vector v for the matrix M such that v\cdot M=v. Without loss of generality, it may be specified that v is normalized so that the sum of its four components is unity. The ij th entry in M^n will give the probability that the outcome of an encounter between X and Y will be j given that the encounter n steps previous is i. In the limit as n approaches infinity, M will converge to a matrix with fixed values, giving the long-term probabilities of an encounter producing j which will be independent of i. In other words, the rows of M^\infty will be identical, giving the long-term equilibrium result probabilities of the iterated prisoners dilemma without the need to explicitly evaluate a large number of interactions. It can be seen that v is a stationary vector for M^n and particularly M^\infty, so that each row of M^\infty will be equal to v. Thus the stationary vector specifies the equilibrium outcome probabilities for X. Defining S_x=\{R,S,T,P\} and S_y=\{R,T,S,P\} as the short-term payoff vectors for the {cc,cd,dc,dd} outcomes (From X 's point of view), the equilibrium payoffs for X and Y can now be specified as s_x=v\cdot S_x and s_y=v\cdot S_y, allowing the two strategies P and Q to be compared for their long term payoffs.

Most work on the iterated prisoners' dilemma has focused on the discrete case, in which players either cooperate or defect, because this model is relatively simple to analyze. However, some researchers have looked at models of the continuous iterated prisoners' dilemma, in which players are able to make a variable contribution to the other player. Le and Boyd[16] found that in such situations, cooperation is much harder to evolve than in the discrete iterated prisoners' dilemma. The basic intuition for this result is straightforward: in a continuous prisoners' dilemma, if a population starts off in a non-cooperative equilibrium, players who are only marginally more cooperative than non-cooperators get little benefit from assorting with one another. By contrast, in a discrete prisoners' dilemma, tit for tat cooperators get a big payoff boost from assorting with one another in a non-cooperative equilibrium, relative to non-cooperators. Since nature arguably offers more opportunities for variable cooperation rather than a strict dichotomy of cooperation or defection, the continuous prisoners' dilemma may help explain why real-life examples of tit for tat-like cooperation are extremely rare in nature (ex. Hammerstein[17]) even though tit for tat seems robust in theoretical models.

Players cannot seem to coordinate mutual cooperation, thus often get locked into the inferior yet stable strategy of defection. In this way, iterated rounds facilitate the evolution of stable strategies.[18] Iterated rounds often produce novel strategies, which have implications to complex social interaction. One such strategy is win-stay lose-shift. This strategy outperforms a simple Tit-For-Tat strategy - that is, if you can get away with cheating, repeat that behavior, however if you get caught, switch.[19]

The prisoner setting may seem contrived, but there are in fact many examples in human interaction as well as interactions in nature that have the same payoff matrix. The prisoner's dilemma is therefore of interest to the social sciences such as economics, politics, and sociology, as well as to the biological sciences such as ethology and evolutionary biology. Many natural processes have been abstracted into models in which living beings are engaged in endless games of prisoner's dilemma. This wide applicability of the PD gives the game its substantial importance.

In environmental studies, the PD is evident in crises such as global climate-change. It is argued all countries will benefit from a stable climate, but any single country is often hesitant to curb CO2 emissions. The immediate benefit to an individual country to maintain current behavior is perceived to be greater than the purported eventual benefit to all countries if behavior was changed, therefore explaining the impasse concerning climate-change in 2007.[20]

An important difference between climate-change politics and the prisoner's dilemma is uncertainty; the extent and pace at which pollution can change climate is not known. The dilemma faced by government is therefore different from the prisoner's dilemma in that the payoffs of cooperation are unknown. This difference suggests that states will cooperate much less than in a real iterated prisoner's dilemma, so that the probability of avoiding a possible climate catastrophe is much smaller than that suggested by a game-theoretical analysis of the situation using a real iterated prisoner's dilemma.[21]

Osang and Nandy provide a theoretical explanation with proofs for a regulation-driven win-win situation along the lines of Michael Porter's hypothesis, in which government regulation of competing firms is substantial.[22]

Cooperative behavior of many animals can be understood as an example of the prisoner's dilemma. Often animals engage in long term partnerships, which can be more specifically modeled as iterated prisoner's dilemma. For example, guppies inspect predators cooperatively in groups, and they are thought to punish non-cooperative inspectors by tit for tat strategy.[citation needed]

In addiction research / behavioral economics, George Ainslie points out[24] that addiction can be cast as an intertemporal PD problem between the present and future selves of the addict. In this case, defecting means relapsing, and it is easy to see that not defecting both today and in the future is by far the best outcome, and that defecting both today and in the future is the worst outcome. The case where one abstains today but relapses in the future is clearly a bad outcome—in some sense the discipline and self-sacrifice involved in abstaining today have been "wasted" because the future relapse means that the addict is right back where he started and will have to start over (which is quite demoralizing, and makes starting over more difficult). The final case, where one engages in the addictive behavior today while abstaining "tomorrow" will be familiar to anyone who has struggled with an addiction. The problem here is that (as in other PDs) there is an obvious benefit to defecting "today", but tomorrow one will face the same PD, and the same obvious benefit will be present then, ultimately leading to an endless string of defections.

John Gottman in his research described in "the science of trust" defines good relationships as those where partners know not to enter the (D,D) cell or at least not to get dynamically stuck there in a loop.

Advertising is sometimes cited as a real-example of the prisoner’s dilemma. When cigarette advertising was legal in the United States, competing cigarette manufacturers had to decide how much money to spend on advertising. The effectiveness of Firm A’s advertising was partially determined by the advertising conducted by Firm B. Likewise, the profit derived from advertising for Firm B is affected by the advertising conducted by Firm A. If both Firm A and Firm B chose to advertise during a given period, then the advertising cancels out, receipts remain constant, and expenses increase due to the cost of advertising. Both firms would benefit from a reduction in advertising. However, should Firm B choose not to advertise, Firm A could benefit greatly by advertising. Nevertheless, the optimal amount of advertising by one firm depends on how much advertising the other undertakes. As the best strategy is dependent on what the other firm chooses there is no dominant strategy, which makes it slightly different from a prisoner's dilemma. The outcome is similar, though, in that both firms would be better off were they to advertise less than in the equilibrium. Sometimes cooperative behaviors do emerge in business situations. For instance, cigarette manufacturers endorsed the making of laws banning cigarette advertising, understanding that this would reduce costs and increase profits across the industry.[citation needed][25] This analysis is likely to be pertinent in many other business situations involving advertising.[citation needed]

Without enforceable agreements, members of a cartel are also involved in a (multi-player) prisoners' dilemma.[26] 'Cooperating' typically means keeping prices at a pre-agreed minimum level. 'Defecting' means selling under this minimum level, instantly taking business (and profits) from other cartel members. Anti-trust authorities want potential cartel members to mutually defect, ensuring the lowest possible prices for consumers.

Two competing athletes have the option to use an illegal and/or dangerous drug to boost their performance. If neither athlete takes the drug, then neither gains an advantage. If only one does, then that athlete gains a significant advantage over their competitor (reduced only by the legal and/or medical dangers of having taken the drug). If both athletes take the drug, however, the benefits cancel out and only the drawbacks remain, putting them both in a worse position than if neither had used doping.[27]
