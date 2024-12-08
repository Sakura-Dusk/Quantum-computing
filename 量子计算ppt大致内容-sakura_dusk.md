

你们可以讲的东西：

在经典情况下的概率模型，张量积与狄拉克符号

量子态与计算基态，局部观测，纠缠态，纯态与混合态，密度矩阵的性质

## 引入

### 叠加态

$|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$

其中  $\alpha,\beta$ 不是概率，而是振幅，满足的是 $\alpha^2+\beta^2=1$，所以其实两个的概率是 $|\alpha|^2,|\beta|^2$



为什么要这么表示？而不是 $p|0\rangle+(1-p)|1\rangle$

因为这样的表示方法更好的表示了量子比特的物理特性：相位信息，量子门操作，量子纠缠中就是振幅的联合

所以其实概率只是它振幅导出的一个结果。



而我们其实注意到 $\alpha,\beta$ 可以是复数而不仅是实数，所以概率不是简单的平方而是取其模后平方。

那为啥是复数呢？因为量子有不确定性原理和干涉现象，要用复数才能表示清楚。



不确定性原理：

粒子的位置与动量不能同时被准确测量。具体来说，当我们尝试更精确地测量粒子的位置时，对其动量的干扰就会增加，反之亦然。

举例：有一个光子源，它可以发射单个光子，这些光子通过两个紧挨着的小缝（双缝）投射到一个屏幕上。光子在屏幕上形成了干涉条纹，这是波动性的体现，说明光子像波一样通过两个缝隙并发生干涉。

如果我们想测量光子究竟通过了哪一个缝隙（即测量位置），我们可以在每个缝隙旁边放置一个光子探测器。这样，每当光子通过缝隙时，探测器就会记录下光子通过的具体缝隙。

但是，当我们使用探测器测量光子通过哪个缝隙时，我们实际上是在与光子发生相互作用。这样其实会改变光子的动量，光子与探测器之间的碰撞会传递动量给光子，那我就无法测准光子测量之前的动量。

不过复数就可以很好的对其进行表示，比如实部虚部分别表示能量和动量，或者位置和动量。



干涉现象：

物理的干涉大家都知道：当两束光线相遇时，它们会根据光的波动性质发生干涉现象，形成明暗相间的干涉条纹。

而量子力学中，粒子也有波动性，所以两个量子相遇的时候也会有干涉，而粒子之间的相位关系在干涉的时候是重要的，所以我们需要用复数来表示出它们的相位关系。



### 布洛赫球（Bloch球）

现在我们知道一个混合态可以表示成 $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$，而 $\alpha,\beta$ 又是复数，那我们考虑想复数一样弄了个二维平面表示，给这个混合态也一个三维立体表示，于是就得到了布洛赫球。

![image-20241208132936416](C:\Users\Sakura\AppData\Roaming\Typora\typora-user-images\image-20241208132936416.png)

那这样一个纯态的量子态就可以对应到球面上的一个点。

## 如何改变量子态

现在我们已经基本了解有关量子的状态，那我们来考虑如何改变他的状态。



那首先我们先不考虑过程，直接考虑结果。

那我们可以沿用前面的方法，一个 $2^n\times 1$ 的向量，变成了另一个 $2^n\times 1$ 的向量，这就是变化。

那稍微考虑一下过程，我们如果能知道之前每个量子态的振幅在这个改变中可能变成的量子态和概率，那我们把所有的东西列出来成为一个 $2^n\times 2^n$ 的矩阵，那是不是把原来的向量乘上这个矩阵，就得到了结果向量。



那其实对量子很多的操作我们都可以用这种矩阵的形式表示出来：

比如一个观测操作，举个简单的例子，如果 $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$，我去观测它让它变成了 $|0\rangle$，那我们可以用这么一个矩阵来表示：

$\begin{bmatrix}1&0\\0&0\end{bmatrix}\begin{bmatrix}\alpha\\ \beta\end{bmatrix}=\begin{bmatrix}\alpha\\ 0\end{bmatrix}$

好像不太对？归一化：

$\begin{bmatrix}\frac{1}{\alpha}&0\\0&0\end{bmatrix}\begin{bmatrix}\alpha\\ \beta\end{bmatrix}=\begin{bmatrix}1\\ 0\end{bmatrix}$



再举个例子，非门，就是把 $|1\rangle$ 变成 $|0\rangle$，$|0\rangle$ 变成 $|1\rangle$，那类似的我们也可以列出一个矩阵来表示：

$\begin{bmatrix}0&1\\1&0\end{bmatrix}\begin{bmatrix}\alpha\\ \beta\end{bmatrix}=\begin{bmatrix}\beta\\\alpha\end{bmatrix}$



我们不妨来看看这两个操作和矩阵的特点。

你会发现，第一个操作是不可逆的，因为你无法通过你观测一次的结果得到原本它的量子态。但是第二个操作是可逆的，你可以通过结果来知道你原本是哪个量子态。

那对应到矩阵，我们就发现一个是不可逆矩阵，一个是可逆矩阵。

那我们再注意到一点，我们前面说到了造这个矩阵我们要归一化，那对应到矩阵上，其实是矩阵的行列式绝对值为 $1$。

最后如果我们要保持量子间的相位关系，我们让内积不变，那其实就是我们要 $UU^†=I$，而这个就是酉矩阵的定义。（$U^†$ 是 $U$ 的伴随矩阵，可以理解为转置矩阵和共轭矩阵的叠加）

### 量子门与酉矩阵

而对于经典的门电路，是输入两个经典位、而只输出一个经典位，这个过程是熵增的、不可逆的——也就是说，**不能由输出推知输入**。

而量子门不会造成信息的丢失。量子门的本质是**酉矩阵**，只要得到这个量子门的共轭转置矩阵就能恢复原来的量子态



一些基本的酉矩阵：

$I=\begin{bmatrix}1&0\\0&1\end{bmatrix}$

$NOT=\begin{bmatrix}0&1\\1&0\end{bmatrix}$

$R_\theta=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}$

$H=\frac{1}{\sqrt{2}}\begin{bmatrix}1&1\\1&-1\end{bmatrix}$

$H$ 叫做哈达玛变换，他的特别之处在于可以让计算基态进入叠加态：

$H|0\rangle=\frac{1}{\sqrt{2}}|0\rangle+\frac{1}{\sqrt{2}}|1\rangle$

$H|1\rangle=\frac{1}{\sqrt{2}}|0\rangle-\frac{1}{\sqrt{2}}|1\rangle$

量子门的作用就是改变状态，那我们如果能刻画出各种逻辑运算的量子门，就代表可以用它来进行编程了。



在布洛赫球上三个维度的转角度：

![image-20241208180248709](C:\Users\Sakura\AppData\Roaming\Typora\typora-user-images\image-20241208180248709.png)

![](C:\Users\Sakura\AppData\Roaming\Typora\typora-user-images\image-20241208180300425.png)

![image-20241208180314361](C:\Users\Sakura\AppData\Roaming\Typora\typora-user-images\image-20241208180314361.png)

受控非门：（当第一个量子位为0时，不对第二量子位操作；否则，将第二量子位取非操作）

![image-20241208180022508](C:\Users\Sakura\AppData\Roaming\Typora\typora-user-images\image-20241208180022508.png)

TOFFOLI 门：如果前两个量子位都是 $|1⟩$ ，托福利门就会翻转第三个量子位。

![image-20241208180408904](C:\Users\Sakura\AppData\Roaming\Typora\typora-user-images\image-20241208180408904.png)



### 由输入输出构造量子门

当然，操作类型的千变万化，我们的量子门也就千变万化，但如果给我们输入和输出，我们可以推出量子门的矩阵形式。

因为各计算基态之间是正交的，那对于一个 $n$ 位的量子门，我把 $2^n$ 个计算基态的输出输出都试一遍：

$|base_i\rangle=|i\rangle\rightarrow |result_i\rangle$

那我们就可以用内积算出这个量子门：

$U=\sum\limits_{i=0}^{2^n-1}|result_i\rangle\langle i|$



我们可以来简单证明它是对的：

对于任何计算基态 $|j\rangle$，有 $U|j\rangle=\sum\limits_{i=0}^{2^n-1}|result_i\rangle\langle i|j\rangle=|result_j\rangle\langle j|j\rangle=|result_j\rangle$

那对于任何一个叠加态他可以表示成基态的线性组合，那输出也是对应输出的同样的线性组合。

$U|\psi\rangle=\displaystyle U\sum_{j=0}^{2^n-1}a_j|j\rangle=\sum_{j=0}^{2^n-1}a_j|result_j\rangle$

最后我们验证一下 $U$ 是否满足酉矩阵的性质：

$\begin{aligned}    U^\dagger U&=\displaystyle\sum_{i=0}^{2^n-1}\sum_{j=0}^{2^n-1}|i\rangle\langle result_i|result_j\rangle\langle j|\\    &=\sum_{i=0}^{2^n-1}|i\rangle\langle result_i|result_i\rangle\langle i|\\    &=\sum_{i=0}^{2^n-1}|i\rangle\langle i|\\    &=I \end{aligned}$

所以 $U$ 的确是酉矩阵。

## 应用

我们的应用是依据量子态观测结果的随机性，来造一个随机数生成函数。

首先我们想利用一个量子比特生成一个 $0/1$ 的随机数。

pyqpanda 是一个量子机器学习库，可以实现各种各样的量子计算相关操作，比如它自己内部有很多常用的量子门，你也可以自己造一些量子门。他可以帮你计算一个量子态所有状态的概率，帮你去观测某个量子态，等等。

那我们就用 Python 中使用这个库，生成一个量子比特，用哈达玛变换把这个初始是基态的比特变为叠加态，然后再去观测它，实现 $0/1$ 的随机生成。



第二部是从 $0/1$ 到 $1\sim n$。

而为了保证等概率，我们不能简单的跑 $n$ 次 $0/1$ 把结果加和，因为结果的概率分布是二项分布，概率并非均等。

一种方法是考虑生成一个二进制串，那每一位都用 $0/1$ 概率生成，那 $0\sim 2^n-1$ 的生成概率就是均等的了。

但这只能使用与 $n=2^k,k\in \N_+$ 的情况，但很多时候 $k$ 不是整数。

我们不妨找到最小的 $k$ 满足 $2^k\geqslant n$，生成 $1\sim 2^k$ 的数，如果生成的数 $>n$，那我们就再用同样的方法生成一次，直到生成的数在 $1\sim n$ 范围内。

为什么这样是允许的？

因为每次落到 $1\sim n$ 的概率是 $\frac{n}{2^k}$，而我们有 $2^{k-1}<n\leqslant 2^k$，则根据简单的概率计算我们得到期望要生成的次数是 $\frac{2^k}{n}<2$，所以我们总能在较少的生成次数内得到符合条件的结果。