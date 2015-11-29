## 隐马尔科夫模型（HMM）
### 介绍
我们通常都习惯寻找一个事物在一段时间里的变化模式（规律）。这些模式发生在很多领域，比如计算机中的指令序列，句子中的词语顺序和口语单词中的音素序列等等，事实上任何领域中的一系列事件都有可能产生有用的模式。

考虑一个简单的例子，有人试图通过一片海藻推断天气——民间传说告诉我们‘湿透的’海藻意味着潮湿阴雨，而‘干燥的’海藻则意味着阳光灿烂。如果它处于一个中间状态（‘有湿气’），我们就无法确定天气如何。然而，天气的状态并没有受限于海藻的状态，所以我们可以在观察的基础上预测天气是雨天或晴天的可能性。另一个有用的线索是前一天的天气状态（或者，至少是它的可能状态）——通过综合昨天的天气及相应观察到的海藻状态，我们有可能更好的预测今天的天气。

首先，我们将介绍产生概率模式的系统，如晴天及雨天间的天气波动.

然后，我们将会看到这样一个系统，我们希望预测的状态并不是观察到的——其底层系统是隐藏的。在上面的例子中，观察到的序列将是海藻而隐藏的系统将是实际的天气。

最后，我们会利用已经建立的模型解决一些实际的问题。对于上述例子，我们想知道：
* 给出一个星期每天的海藻观察状态，之后的天气将会是什么?
* 给定一个海藻的观察状态序列，预测一下此时是冬季还是夏季？直观地，如果一段时间内海藻都是干燥的，那么这段时间很可能是夏季，反之，如果一段时间内海藻都是潮湿的，那么这段时间可能是冬季。

### 生成模式
#### 1, 确定性模式
考虑一套交通信号灯，灯的颜色变化序列依次是红色-红色/黄色-绿色-黄色-红色。这个序列可以作为一个状态机器，交通信号灯的不同状态都紧跟着上一个状态。

注意每一个状态都是唯一的依赖于前一个状态，所以，如果交通灯为绿色，那么下一个颜色状态将始终是黄色——也就是说，该系统是确定性的。确定性系统相对比较容易理解和分析，因为状态间的转移是完全已知的。

#### 2, 非确定性模式
为了使天气那个例子更符合实际，加入第三个状态——多云。与交通信号灯例子不同，我们并不期望这三个天气状态之间的变化是确定性的，但是我们依然希望对这个系统建模以便生成一个天气变化模式（规律）。

一种做法是假设模型的当前状态仅仅依赖于前面的几个状态，这被称为马尔科夫假设，它极大地简化了问题。显然，这可能是一种粗糙的假设，并且因此可能将一些非常重要的信息丢失。

当考虑天气问题时，马尔科夫假设假定今天的天气只能通过过去几天已知的天气情况进行预测——而对于其他因素，譬如风力、气压等则没有考虑。在这个例子以及其他相似的例子中，这样的假设显然是不现实的。然而，由于这样经过简化的系统可以用来分析，我们常常接受这样的知识假设，虽然它产生的某些信息不完全准确。

一个马尔科夫过程是状态间的转移仅依赖于前n个状态的过程。这个过程被称之为n阶马尔科夫模型，其中n是影响下一个状态选择的（前）n个状态。最简单的马尔科夫过程是一阶模型，它的状态选择仅与前一个状态有关。这里要注意它与确定性系统并不相同，因为下一个状态的选择由相应的概率决定，并不是确定性的。

下图是天气例子中状态间所有可能的一阶状态转移情况：

对于有M个状态的一阶马尔科夫模型，共有M^2个状态转移，因为任何一个状态都有可能是所有状态的下一个转移状态。每一个状态转移都有一个概率值，称为状态转移概率——这是从一个状态转移到另一个状态的概率。所有的M^2个概率可以用一个状态转移矩阵表示。注意这些概率并不随时间变化而不同——这是一个非常重要（但常常不符合实际）的假设。

#### 3, 总结
我们尝试识别时间变化中的模式，并且为了达到这个目我们试图对这个过程建模以便产生这样的模式。我们使用了离散时间点、离散状态以及做了马尔科夫假设。在采用了这些假设之后，系统产生了这个被描述为马尔科夫过程的模式，它包含了一个pi向量（初始概率）和一个状态转移矩阵。关于假设，重要的一点是状态转移矩阵并不随时间的改变而改变——这个矩阵在整个系统的生命周期中是固定不变的。

### 隐藏模式
#### 1,马尔科夫过程的局限性
在某些情况下，我们希望找到的模式用马尔科夫过程描述还显得不充分。回顾一下天气那个例子，一个隐士也许不能够直接获取到天气的观察情况，但是他有一些水藻。民间传说告诉我们水藻的状态与天气状态有一定的概率关系——天气和水藻的状态是紧密相关的。在这个例子中我们有两组状态，观察的状态（水藻的状态）和隐藏的状态（天气的状态）。我们希望为隐士设计一种算法，在不能够直接观察天气的情况下，通过水藻和马尔科夫假设来预测天气。

一个更实际的问题是语音识别，我们听到的声音是来自于声带、喉咙大小、舌头位置以及其他一些东西的组合结果。所有这些因素相互作用产生一个单词的声音，一套语音识别系统检测的声音就是来自于个人发音时身体内部物理变化所引起的不断改变的声音。

一些语音识别装置工作的原理是将内部的语音产出看作是隐藏的状态，而将声音结果作为一系列观察的状态，这些由语音过程生成并且最好的近似了实际（隐藏）的状态。在这两个例子中，需要着重指出的是，隐藏状态的数目与观察状态的数目可以是不同的。一个包含三个状态的天气系统（晴天、多云、雨天）中，可以观察到4个等级的海藻湿润情况（干、稍干、潮湿、湿润）；纯粹的语音可以由80个音素描述，而身体的发音系统会产生出不同数目的声音，或者比80多，或者比80少。

在这种情况下，观察到的状态序列与隐藏过程有一定的概率关系。我们使用隐马尔科夫模型对这样的过程建模，这个模型包含了一个底层隐藏的随时间改变的马尔科夫过程，以及一个与隐藏状态某种程度相关的可观察到的状态集合。

#### 2, 隐马尔科夫模型
下图显示的是天气例子中的隐藏状态和观察状态。假设隐藏状态（实际的天气）由一个简单的一阶马尔科夫过程描述，那么它们之间都相互连接。

隐藏状态和观察状态之间的连接表示：在给定的马尔科夫过程中，一个特定的隐藏状态生成特定的观察状态的概率。这很清晰的表示了‘进入’一个观察状态的所有概率之和为1，在上面这个例子中就是Pr(Obs|Sun), Pr(Obs|Cloud) 及 Pr(Obs|Rain)之和.

除了定义了马尔科夫过程的概率关系，我们还有另一个矩阵，定义为混淆矩阵（confusion matrix），它包含了给定一个隐藏状态后得到的观察状态的概率。对于天气例子，混淆矩阵是：

#### 3, 总结
我们已经看到在一些过程中一个观察序列与一个底层马尔科夫过程是概率相关的。在这些例子中，观察状态的数目可以和隐藏状态的数码不同。

我们使用一个隐马尔科夫模型（HMM）对这些例子建模。这个模型包含两组状态集合和三组概率集合：

* 隐藏状态：一个系统的（真实）状态，可以由一个马尔科夫过程进行描述（例如，天气）。
* 观察状态：在这个过程中‘可视’的状态（例如，海藻的湿度）。
* pi向量：包含了（隐）模型在时间t=1时一个特殊的隐藏状态的概率（初始概率）。
* 状态转移矩阵：包含了一个隐藏状态到另一个隐藏状态的概率
* 混淆矩阵：包含了给定隐马尔科夫模型的某一个特殊的隐藏状态，观察到的某个观察状态的概率。

因此一个隐马尔科夫模型是在一个标准的马尔科夫过程中引入一组观察状态，以及其与隐藏状态间的一些概率关系。

### 隐马尔科夫模型
#### 1, 定义
一个隐马尔科夫模型是一个三元组（pi, A, B）。在状态转移矩阵及混淆矩阵中的每一个概率都是时间无关的——也就是说，当系统演化时这些矩阵并不随时间改变。实际上，这是马尔科夫模型关于真实世界最不现实的一个假设。

#### 2, 应用
　一旦一个系统可以作为HMM被描述，就可以用来解决三个基本问题。其中前两个是模式识别的问题：给定HMM求一个观察序列的概率（评估）；搜索最有可能生成一个观察序列的隐藏状态序列（解码）。第三个问题是给定观察序列生成一个HMM（学习）。

** 评估 **

考虑这样的问题，我们有一些描述不同系统的隐马尔科夫模型（也就是一些( pi,A,B)三元组的集合）及一个观察序列。我们想知道哪一个HMM最有可能产生了这个给定的观察序列。例如，对于海藻来说，我们也许会有一个“夏季”模型和一个“冬季”模型，因为不同季节之间的情况是不同的——我们也许想根据海藻湿度的观察序列来确定当前的季节。

我们使用前向算法（forward algorithm）来计算给定隐马尔科夫模型（HMM）后的一个观察序列的概率，并因此选择最合适的隐马尔科夫模型(HMM)。

　在语音识别中这种类型的问题发生在当一大堆数目的马尔科夫模型被使用，并且每一个模型都对一个特殊的单词进行建模时。一个观察序列从一个发音单词中形成，并且通过寻找对于此观察序列最有可能的隐马尔科夫模型（HMM）识别这个单词。

** 解码 **

另一个相关问题，也是最感兴趣的一个，就是搜索生成输出序列的隐藏状态序列。在许多情况下我们对于模型中的隐藏状态更感兴趣，因为它们代表了一些更有价值的东西，而这些东西通常不能直接观察到。

考虑海藻和天气这个例子，一个盲人隐士只能感觉到海藻的状态，但是他更想知道天气的情况，天气状态在这里就是隐藏状态。

我们使用Viterbi 算法（Viterbi algorithm）确定（搜索）已知观察序列及HMM下最可能的隐藏状态序列.

Viterbi算法（Viterbi algorithm）的另一广泛应用是自然语言处理中的词性标注。在词性标注中，句子中的单词是观察状态，词性（语法类别）是隐藏状态（注意对于许多单词，如wind，fish拥有不止一个词性）。对于每句话中的单词，通过搜索其最可能的隐藏状态，我们就可以在给定的上下文中找到每个单词最可能的词性标注。

** 学习 **
第三个问题，也是与HMM相关的问题中最难的，根据一个观察序列（来自于已知的集合），以及与其有关的一个隐藏状态集，估计一个最合适的隐马尔科夫模型（HMM），也就是确定对已知序列描述的最合适的（pi,A,B）三元组。

当矩阵A和B不能够直接被（估计）测量时，前向-后向算法（forward-backward algorithm）被用来进行学习（参数估计），这也是实际应用中常见的情况。

#### 3, 总结
由一个向量和两个矩阵(pi,A,B)描述的隐马尔科夫模型对于实际系统有着巨大的价值，虽然经常只是一种近似，但它们却是经得起分析的。隐马尔科夫模型通常解决的问题包括：

1, 对于一个观察序列匹配最可能的系统——评估，使用前向算法（forward algorithm）解决；

2, 对于已生成的一个观察序列，确定最可能的隐藏状态序列——解码，使用Viterbi 算法（Viterbi algorithm）解决；

3, 对于已生成的观察序列，决定最可能的模型参数——学习，使用前向-后向算法（forward-backward algorithm）解决。

### 前向算法
** 穷举搜索 **

给定隐马尔科夫模型，也就是在模型参数（pi, A, B)已知的情况下，我们想找到观察序列的概率。还是考虑天气这个例子，我们有一个用来描述天气及与它密切相关的海藻湿度状态的隐马尔科夫模型(HMM)，另外我们还有一个海藻的湿度状态观察序列。假设连续3天海藻湿度的观察结果是（干燥、湿润、湿透）——而这三天每一天都可能是晴天、多云或下雨，对于观察序列以及隐藏的状态，可以将其视为网格：

网格中的每一列都显示了可能的的天气状态，并且每一列中的每个状态都与相邻列中的每一个状态相连。而其状态间的转移都由状态转移矩阵提供一个概率。在每一列下面都是某个时间点上的观察状态，给定任一个隐藏状态所得到的观察状态的概率由混淆矩阵提供。

可以看出，一种计算观察序列概率的方法是找到每一个可能的隐藏状态，并且将这些隐藏状态下的观察序列概率相加。对于上面那个（天气）例子，将有3^3 = 27种不同的天气序列可能性，因此，观察序列的概率是：

用这种方式计算观察序列概率极为昂贵，特别对于大的模型或较长的序列，因此我们可以利用这些概率的时间不变性来减少问题的复杂度。

** 使用递归降低问题复杂度 **

给定一个隐马尔科夫模型（HMM），我们将考虑递归地计算一个观察序列的概率。我们首先定义局部概率（partial probability）,它是到达网格中的某个中间状态时的概率。然后，我们将介绍如何在t=1和t=n(>1)时计算这些局部概率。

由此可见，对于这些最终局部概率求和等价于对于网格中所有可能的路径概率求和，也就求出了给定隐马尔科夫模型(HMM)后的观察序列概率。

### 维特比算法
对于一个特殊的隐马尔科夫模型(HMM)及一个相应的观察序列，我们常常希望能找到生成此序列最可能的隐藏状态序列。

** 寻找最可能的隐藏状态序列 **

计算t=1时刻的局部概率delta‘s

我们计算的局部概率delta是作为最可能到达我们当前位置的路径的概率（已知的特殊知识如观察概率及前一个状态的概率）。当t=1的时候，到达某状态的最可能路径明显是不存在的；但是，我们使用t=1时的所处状态的初始概率及相应的观察状态k1的观察概率计算局部概率delta；

计算t>1时刻的局部概率delta‘s

回顾一下马尔科夫假设：给定一个状态序列，一个状态发生的概率只依赖于前n个状态。特别地，在一阶马尔可夫假设下，状态X在一个状态序列后发生的概率只取决于之前的一个状态，即

Pr (到达状态A最可能的路径) .Pr (X | A) . Pr (观察状态 | X)

与此相同，路径末端是AX的最可能的路径将是到达A的最可能路径再紧跟X。相似地，这条路径的概率将是：

这里，我们假设前一个状态的知识（局部概率）是已知的，同时利用了状态转移概率和相应的观察概率之积。然后，我们就可以在其中选择最大的概率了（局部概率delta）。

### 前向-后向算法
与HMM模型相关的“有用”的问题是评估（前向算法）和解码（维特比算法）——它们一个被用来测量一个模型的相对适用性，另一个被用来推测模型隐藏的部分在做什么（“到底发生了”什么）。可以看出它们都依赖于隐马尔科夫模型（HMM）参数这一先验知识——状态转移矩阵，混淆（观察）矩阵，以及pi向量（初始化概率向量）。

然而，在许多实际问题的情况下这些参数都不能直接计算的，而要需要进行估计——这就是隐马尔科夫模型中的学习问题。前向-后向算法就可以以一个观察序列为基础来进行这样的估计，而这个观察序列来自于一个给定的集合，它所代表的是一个隐马尔科夫模型中的一个已知的隐藏集合。

一个例子可能是一个庞大的语音处理数据库，其底层的语音可能由一个马尔可夫过程基于已知的音素建模的，而其可以观察的部分可能由可识别的状态（可能通过一些矢量数据表示）建模的，但是没有（直接）的方式来获取隐马尔科夫模型（HMM）参数。

前向-后向算法并非特别难以理解，但自然地比前向算法和维特比算法更复杂。由于这个原因，这里就不详细讲解前向-后向算法了（任何有关HMM模型的参考文献都会提供这方面的资料的）。

总之，前向-后向算法首先对于隐马尔科夫模型的参数进行一个初始的估计（这很可能是完全错误的），然后通过对于给定的数据评估这些参数的的价值并减少它们所引起的错误来重新修订这些HMM参数。从这个意义上讲，它是以一种梯度下降的形式寻找一种错误测度的最小值。

之所以称其为前向-后向算法，主要是因为对于网格中的每一个状态，它既计算到达此状态的“前向”概率（给定当前模型的近似估计），又计算生成此模型最终状态的“后向”概率（给定当前模型的近似估计）。 这些都可以通过利用递归进行有利地计算，就像我们已经看到的。可以通过利用近似的HMM模型参数来提高这些中间概率进行调整，而这些调整又形成了前向-后向算法迭代的基础。

### 总结
通常，模式并不是单独的出现，而是作为时间序列中的一个部分——这个过程有时候可以被辅助用来对它们进行识别。 在基于时间的进程中，通常都会使用一些假设——一个最常用的假设是进程的状态只依赖于前面N个状态——这样我们就有了一个N阶马尔科夫模型。 最简单的例子是N = 1。
存在很多例子，在这些例子中进程的状态（模式）是不能够被直接观察的，但是可以非直接地，或者概率地被观察为模式的另外一种集合——这样我们就可以定义一类隐马尔科夫模型——这些模型已被证明在当前许多研究领域，尤其是语音识别领域具有非常大的价值。

在实际的过程中这些模型提出了三个问题都可以得到立即有效的解决，分别是：
* 评估：对于一个给定的隐马尔科夫模型其生成一个给定的观察序列的概率是多少。 前向算法可以有效的解决此问题。
* 解码：什么样的隐藏（底层）状态序列最有可能生成一个给定的观察序列。 维特比算法可以有效的解决此问题。
* 学习：对于一个给定的观察序列样本，什么样的模型最可能生成该序列——也就是说，该模型的参数是什么。 这个问题可以通过使用前向-后向算法解决。

隐马尔科夫模型（HMM）在分析实际系统中已被证明有很大的价值；它们通常的缺点是过于简化的假设，这与马尔可夫假设相关——即一个状态只依赖于前一个状态，并且这种依赖关系是独立于时间之外的（与时间无关）。

## 参考文献
[Hidden Markov Models](http://www.comp.leeds.ac.uk/roger/HiddenMarkovModels/html_dev/main.html)

## Hidden Markov Models
Often we are interested in finding patterns which appear over a space of time. These patterns occur in many areas; the pattern of commands someone uses in instructing a computer, sequences of words in sentences, the sequence of phonemes in spoken words - any area where a sequence of events occurs could produce useful patterns.

Consider the simple example of someone trying to deduce the weather from a piece of seaweed - folklore tells us that `soggy' seaweed means wet weather, while `dry' seaweed means sun. If it is in an intermediate state (`damp'), then we cannot be sure. However, the state of the weather is not restricted to the state of the seaweed, so we may say on the basis of an examination that the weather is probably raining or sunny. A second useful clue would be the state of the weather on the preceding day (or, at least, its probable state) - by combining knowledge about what happened yesterday with the observed seaweed state, we might come to a better forecast for today.

This is typical of the type of system we will consider in this tutorial.
* First we will introduce systems which generate probabalistic patterns in time, such as the weather fluctuating between sunny and rainy.
* We then look at systems where what we wish to predict is not what we observe - the underlying system is hidden. In the above example, the observed sequence would be the seaweed and the hidden system would be the actual weather.
* We then look at some problems that can be solved once the system has been modeled. For the above example, we may want to know
* What the weather was for a week given each day's seaweed observation.
* Given a sequence of seaweed observations, is it winter or summer? Intuitively, if the seaweed has been dry for a while it may be summer, if it has been soggy for a while it might be winter.

## Deterministic Patterns
Consider a set of traffic lights; the sequence of lights is red - red/amber - green - amber - red. The sequence can be pictured as a state machine, where the different states of the traffic lights follow each other.

![pic1](http://www.comp.leeds.ac.uk/roger/HiddenMarkovModels/html_dev/gen_patterns/graphics/traffic-lights_anim.gif)

Notice that each state is dependent solely on the previous state, so if the lights are green, an amber light will always follow - that is, the system is deterministic. Deterministic systems are relatively easy to understand and analyse, once the transitions are fully known.

## Patterns generated by a hidden process
### When a Markov process may not be powerful enough
In some cases the patterns that we wish to find are not described sufficiently by a Markov process. Returning to the weather example, a hermit may perhaps not have access to direct weather observations, but does have a piece of seaweed. Folklore tells us that the state of the seaweed is probabalistically related to the state of the weather - the weather and seaweed states are closely linked. In this case we have two sets of states, the observable states (the state of the seaweed) and the hidden states (the state of the weather). We wish to devise an algorithm for the hermit to forecast weather from the seaweed and the Markov assumption without actually ever seeing the weather.

A more realistic problem is that of recognising speech; the sound that we hear is the product of the vocal chords, size of throat, position of tongue and several other things. Each of these factors interact to produce the sound of a word, and the sounds that a speech recognition system detects are the changing sound generated from the internal physical changes in the person speaking.

Some speech recognition devices work by considering the internal speech production to be a sequence of hidden states, and the resulting sound to be a sequence of observable states generated by the speech process that at best approximates the true (hidden) states. In both examples it is important to note that the number of states in the hidden process and the number of observable states may be different. In a three state weather system (sunny, cloudy, rainy) it may be possible to observe four grades of seaweed dampness (dry, dryish, damp,soggy); pure speech may be described by (say) 80 phonemes, while a physical speech system may generate a number of distinguishable sounds that is either more or less than 80.

In such cases the observed sequence of states is probabalistically related to the hidden process. We model such processes using a hidden Markov model where there is an underlying hidden Markov process changing over time, and a set of observable states which are related somehow to the hidden states.

## Hidden Markov Models
### Definition of a hidden Markov model
A hidden Markov model (HMM) is a triple (P,A,B).

![math.png](https://raw.githubusercontent.com/csrgxtu/maxent/master/static/img/math.png)

Each probability in the state transition matrix and in the confusion matrix is time independent - that is, the matrices do not change in time as the system evolves. In practice, this is one of the most unrealistic assumptions of Markov models about real processes.


## Forward Algorithm
### Finding the probability of an observed sequence
#### Exhaustive search for solution
We want to find the probability of an observed sequence given an HMM - that is, the parameters (P,A,B) are known. Consider the weather example; we have a HMM describing the weather and its relation to the state of the seaweed, and we also have a sequence of seaweed observations. Suppose the observations for 3 consecutive days are (dry,damp,soggy) - on each of these days, the weather may have been sunny, cloudy or rainy. We can picture the observations and the possible hidden states as a trellis.

![math2.png](https://raw.githubusercontent.com/csrgxtu/maxent/master/static/img/math2.png)

Each column in the trellis shows the possible state of the weather and each state in one column is connected to each state in the adjacent columns. Each of these state transitions has a probability provided by the state transition matrix. Under each column is the observation at that time; the probability of this observation given any one of the above states is provided by the confusion matrix.

It can be seen that one method of calculating the probability of the observed sequence would be to find each possible sequence of the hidden states, and sum these probabilities. For the above example, there would be 3^3=27 possible different weather sequences, and so the probability is

Pr(dry,damp,soggy | HMM) = Pr(dry,damp,soggy | sunny,sunny,sunny) + Pr(dry,damp,soggy | sunny,sunny ,cloudy) + Pr(dry,damp,soggy | sunny,sunny ,rainy) + . . . . Pr(dry,damp,soggy | rainy,rainy ,rainy)

Calculating the probability in this manner is computationally expensive, particularly with large models or long sequences, and we find that we can use the time invariance of the probabilities to reduce the complexity of the problem.

#### Reduction of complexity using recursion
We will consider calculating the probability of observing a sequence recursively given a HMM. We will first define a partial probability, which is the probability of reaching an intermediate state in the trellis. We then show how these partial probabilities are calculated at times t=1 and t=n (> 1).

Suppose throughout that the T-long observed sequence is
Consider the trellis below showing the states and first-order transitions for the observation sequence dry,damp,soggy;

We can calculate the probability of reaching an intermediate state in the trellis as the sum of all possible paths to that state.

For example, the probability of it being cloudy at t = 2 is calculated from the paths;

## Viterbi Algorithm
### Finding most probable sequence of hidden states
We often wish to take a particular HMM, and determine from an observation sequence the most likely sequence of underlying hidden states that might have generated it.

#### Exhaustive search for a solution
We can use a picture of the execution trellis to visualise the relationship between states and observations.

We can find the most probable sequence of hidden states by listing all possible sequences of hidden states and finding the probability of the observed sequence for each of the combinations. The most probable sequence of hidden states is that combination that maximises

Pr(observed sequence | hidden state combination).

For example, for the observation sequence in the trellis shown, the most probable sequence of hidden states is the sequence that maximises :

Pr(dry,damp,soggy | sunny,sunny,sunny), Pr(dry,damp,soggy | sunny,sunny,cloudy), Pr(dry,damp,soggy | sunny,sunny,rainy), . . . . Pr(dry,damp,soggy | rainy,rainy,rainy)

This approach is viable, but to find the most probable sequence by exhaustively calculating each combination is computationally expensive. As with the forward algorithm, we can use the time invariance of the probabilities to reduce the complexity of the calculation.

####  Reducing complexity using recursion
We will consider recursively finding the most probable sequence of hidden states given an observation sequence and a HMM. We will first define the partial probability  d, which is the probability of reaching a particular intermediate state in the trellis. We then show how these partial probabilities are calculated at t=1 and at t=n (> 1).

These partial probabilities differ from those calculated in the forward algorithm since they represent the probability of the most probable path to a state at time t, and not a total.

Consider the trellis below showing the states and first order transitions for the observation sequence dry,damp,soggy;

## Forward-Backward Algorithm
### Forward-backward algorithm
The `useful' problems assosciated with HMMs are those of evaluation and decoding - they permit either a measurement of a model's relative applicability, or an estimate of what the underlying model is doing (what `really happened'). It can be seen that they both depend upon foreknowledge of the HMM parameters - the state transition matrix, the observation matrix, and the P vector.

There are, however, many circumstances in practical problems where these are not directly measurable, and have to be estimated - this is the learning problem. The forward-backward algorithm permits this estimate to be made on the basis of a sequence of observations known to come from a given set, that represents a known hidden set following a Markov model.

An example may be a large speech processing database, where the underlying speech may be modelled by a Markov process based on known phonemes, and the obervations may be modelled as recognisable states (perhaps via some vector quantisation), but there will be no (straightforward) way of deriving empirically the HMM parameters.

The forward-backward algorithm is not unduly hard to comprehend, but is more complex in nature than the forward algorithm and the Viterbi algorithm. For this reason, it will not be presented here in full (any standard reference on HMMs will provide - see the Summary section).
In summary, the algorithm proceeds by making an initial guess of the parameters (which may well be entirely wrong) and then refining it by assessing its worth, and attempting to reduce the errors it provokes when fitted to the given data. In this sense, it is performing a form of gradient descent, looking for a minimum of an error measure.

It derives its name from the fact that, for each state in an execution trellis, it computes the `forward' probability of arriving at that state (given the current model approximation) and the `backward' probability of generating the final state of the model, again given the current approximation. Both of these may be computed advantageously by exploiting recursion, much as we have seen already. Adjustments may be made to the approximated HMM parameters to improve these intermediate probabilities, and these adjustments form the basis of the algorithm iterations.

## Summary
Frequently, patterns do not appear in isolation but as part of a series in time - this progression can sometimes be used to assist in their recognition. Assumptions are usually made about the time based process - a common assumption is that the process's state is dependent only on the preceding N states - then we have an order N Markov model. The simplest case is N=1.

Various examples exists where the process states (patterns) are not directly observable, but are indirectly, and probabalistically, observable as another set of patterns - we can then define a hidden Markov model - these models have proved to be of great value in many current areas of research, notably speech recognition.

Such models of real processes pose three problems that are amenable to immediate attack; these are :
* Evaluation : with what probability does a given model generate a given sequence of observations. The forward algorithm solves this problem efficiently.
* Decoding : what sequence of hidden (underlying) states most probably generated a given sequence of observations. The Viterbi algorithm solves this problem efficiently.
* Learning : what model most probably underlies a given sample of observation sequences - that is, what are the parameters of such a model. This problem may be solved by using the forward-backward algorithm.

HMMs have proved to be of great value in analysing real systems; their usual drawback is the over-simplification associated with the Markov assumption - that a state is dependent only on predecessors, and that this dependence is time independent.
