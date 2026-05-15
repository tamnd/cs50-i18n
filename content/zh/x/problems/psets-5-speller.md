---
title: "Speller - CS50x 2026"
pset: 5
draft: false
---

## 待解决的问题

在这个问题中，你将使用哈希表 (hash table) 实现一个类似于下文所示的文件拼写检查程序。

## 演示

## 发行代码

在这个问题中，你将扩展 CS50 官方提供的代码功能。

下载发行代码

登录 [cs50.dev](https://cs50.dev/)，点击终端窗口，然后输入 `cd` 并回车。你应该会发现终端提示符如下所示：

```
$
```

接着执行

```python
wget https://cdn.cs50.net/2026/x/psets/5/speller.zip
```

以便将名为 `speller.zip` 的压缩包下载到你的 codespace 中。

然后执行

```
unzip speller.zip
```

来创建一个名为 `speller` 的文件夹。你不再需要这个 ZIP 文件了，所以可以执行

```
rm speller.zip
```

并在提示符下输入 “y” 后按回车，以删除下载的 ZIP 文件。

现在输入

```bash
cd speller
```

并按回车进入该目录。你的提示符现在应该如下所示：

```
speller/ $
```

执行 `ls`，你应该会看到一些文件和文件夹：

```
dictionaries/  dictionary.c  dictionary.h  keys/  Makefile  speller.c  speller50  texts/
```

如果你遇到任何问题，请重新执行这些步骤，看看能否发现哪里出错了！

## 背景

**考虑到该程序包含多个文件，在开始之前完整阅读本节内容非常重要。这样你就会知道要做什么以及如何去做！**

从理论上讲，对于规模为 *n* 的输入，运行时间为 *n* 的算法在 *O* 记号下与运行时间为 *2n* 的算法是“渐进等价”的。事实上，在描述算法的运行时间时，我们通常关注主导项（即影响力最大的项，在本例中为 *n*，因为 *n* 可能远大于 2）。但在现实世界中，事实是 *2n* 的运行感官比 *n* 慢一倍。

你面临的挑战是实现一个你所能做到的最快的拼写检查器！不过，我们这里说的“最快”是指实际的“墙上时钟”时间（实际运行时间），而不是渐进时间。

在 `speller.c` 中，我们编写了一个程序，旨在将字典单词从磁盘加载到内存后，对文件进行拼写检查。与此同时，该字典在名为 `dictionary.c` 的文件中实现。（它本来可以直接在 `speller.c` 中实现，但随着程序变得越来越复杂，将其拆分为多个文件通常更方便。）其中函数的原型并未定义在 `dictionary.c` 本身，而是在 `dictionary.h` 中。这样，`speller.c` 和 `dictionary.c` 都可以 `#include` 该文件。遗憾的是，我们还没来得及实现加载 (load) 部分和检查 (check) 部分。这两部分（以及更多内容）就留给你了！但首先，让我们先浏览一下代码。

### 理解代码

#### `dictionary.h`

打开 `dictionary.h`，你会看到一些新的语法，包括几行提到 `DICTIONARY_H` 的代码。无需担心这些，但如果你好奇的话，这些代码只是为了确保即使 `dictionary.c` 和 `speller.c`（稍后你会看到）都 `#include` 了这个文件，`clang` 也只会编译它一次。

接着注意我们如何 `#include` 一个名为 `stdbool.h` 的文件。这就是定义 `bool` 本身的文件。你以前不需要它，因为 CS50 库以前会为你自动包含它。

还要注意我们对 `#define` 的使用，这是一个“预处理指令”，定义了一个名为 `LENGTH` 且值为 `45` 的“常量”。它是常量，意味着你不能在代码中（无意中）更改它。事实上，`clang` 会把你代码中所有出现的 `LENGTH` 替换为字面量 `45`。换句话说，它不是一个变量，只是一个查找替换的技巧。

最后，注意五个函数的原型：`check`、`hash`、`load`、`size` 和 `unload`。注意其中三个函数接受指针作为参数（由 `*` 表示）：

```js
bool check(const char *word);
unsigned int hash(const char *word);
bool load(const char *dictionary);
```

回想一下，`char *` 就是我们以前所说的 `string`。所以这三个原型本质上就是：

```js
bool check(const string word);
unsigned int hash(const string word);
bool load(const string dictionary);
```

而 `const` 则表示这些字符串在作为参数传入时必须保持不变；你将无法（无论是无意还是有意地）更改它们！

#### `dictionary.c`

现在打开 `dictionary.c`。注意在文件顶部，我们定义了一个名为 `node` 的结构体 (`struct`)，它代表哈希表中的一个节点。我们还声明了一个全局指针数组 `table`，它（很快）将代表你用来跟踪字典中单词的哈希表。该数组包含 `N` 个节点指针，我们现在将 `N` 设置为 `26`，以匹配下文描述的默认 `hash` 函数。你可能会根据自己对 `hash` 的实现来调大这个值。

接下来，注意我们已经实现了 `load`、`check`、`size` 和 `unload`，但仅仅是初步实现，刚好能让代码通过编译。还要注意，我们实现了一个基于单词首字母的示例 `hash` 算法。你的任务最终是尽可能巧妙地重新实现这些函数，使这个拼写检查器能够如期工作，并且运行飞快！

#### `speller.c`

接下来，打开 `speller.c` 并花点时间查看其中的代码和注释。你不需要更改此文件中的任何内容，也不需要理解它的全部内容，但请尝试了解其功能。注意我们如何通过一个名为 `getrusage` 的函数来对你实现的 `check`、`load`、`size` 和 `unload` 进行“基准测试”（即计算执行时间）。还要注意我们如何将要进行拼写检查的文件内容逐个单词地传递给 `check`。最终，我们会报告该文件中的每个拼写错误以及一系列统计数据。

顺便注意一下，我们定义的 `speller` 用法如下：

```python
Usage: speller [dictionary] text
```

其中 `dictionary` 被假定为一个包含小写单词列表的文件（每行一个单词），而 `text` 是要进行拼写检查的文件。如括号所示，`dictionary` 是可选的；如果省略此参数，`speller` 将默认使用 `dictionaries/large`。换句话说，运行

```
./speller text
```

等同于运行

```
./speller dictionaries/large text
```

其中 `text` 是你希望进行拼写检查的文件。毋庸置疑，前者更容易输入！（当然，在你于 `dictionary.c` 中实现 `load` 之前，`speller` 将无法加载任何字典！在此之前，你会看到 `Could not load`。）

在默认字典中，有 143,091 个单词，所有这些单词都必须加载到内存中！事实上，你可以看一下那个文件，感受一下它的结构和大小。注意该文件中的每个单词都以小写形式出现（为了简单起见，甚至是专有名词和缩写词）。从上到下，该文件按字典序排序，每行只有一个单词（每个单词以 `\n` 结尾）。单词长度不超过 45 个字符，且没有重复单词。在开发过程中，你可能会发现为 `speller` 提供一个单词量少得多的自定义 `dictionary` 会很有帮助，以免你在调试内存中庞大的结构时感到吃力。`dictionaries/small` 就是这样一个字典。要使用它，请执行

```
./speller dictionaries/small text
```

其中 `text` 是你希望进行拼写检查的文件。在你确信自己理解了 `speller` 本身的工作原理之前，请不要继续！

很可能你并没有花足够的时间查看 `speller.c`。请回去再仔细过一遍！

#### `texts/`

为了让你测试 `speller` 的实现，我们还为你提供了一大堆文本，其中包括《爱乐之城》(La La Land) 的剧本、《平价医疗法案》的文本、来自托尔斯泰的三百万字节内容、一些《联邦党人文集》和莎士比亚的摘录等等。为了让你知道预期的结果，请浏览一下这些文件，它们都在 `pset5` 目录下的 `texts` 目录中。

现在，正如你仔细阅读 `speller.c` 后应该知道的那样，如果执行以下命令：

```
./speller texts/lalaland.txt
```

`speller` 的输出最终将类似于下面所示。

下面是你将看到的部分输出。为了说明情况，我们截取了一些“拼写错误”的例子。为了不破坏乐趣，我们暂时省略了自己的统计数据。

```
MISSPELLED WORDS

[...]
AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
[...]
Shangri
[...]
fianc
[...]
Sebastian's
[...]

WORDS MISSPELLED:
WORDS IN DICTIONARY:
WORDS IN TEXT:
TIME IN load:
TIME IN check:
TIME IN size:
TIME IN unload:
TIME IN TOTAL:
```

`TIME IN load` 代表 `speller` 执行你实现的 `load` 所花费的秒数。`TIME IN check` 代表 `speller` 总共执行你实现的 `check` 所花费的秒数。`TIME IN size` 代表 `speller` 执行你实现的 `size` 所花费的秒数。`TIME IN unload` 代表 `speller` 执行你实现的 `unload` 所花费的秒数。`TIME IN TOTAL` 是这四个测量值的总和。

**请注意，这些时间在多次执行 `speller` 时可能会有所波动，这取决于你的 codespace 正在运行的其他任务，即使你没有更改代码也是如此。**

顺便说一下，需要明确的是，所谓“拼写错误”，我们仅仅是指某个单词不在提供的 `dictionary` 中。

#### `Makefile`

最后，回想一下 `make` 会自动编译你的代码，这样你就不用手动执行带有大量开关参数的 `clang` 了。然而，随着你的程序规模增长，`make` 将无法再通过上下文推断如何编译你的代码；你需要开始告诉 `make` 如何编译你的程序，特别是当涉及多个源文件（即 `.c` 文件）时，如此题所示。因此，我们将利用 `Makefile`，这是一个告诉 `make` 具体该做什么的配置文件。打开 `Makefile`，你应该会看到四行代码：

1. 第一行告诉 `make`，当你执行 `make speller`（或仅仅是 `make`）时，执行后续行。
2. 第二行告诉 `make` 如何将 `speller.c` 编译为机器码（即 `speller.o`）。
3. 第三行告诉 `make` 如何将 `dictionary.c` 编译为机器码（即 `dictionary.o`）。
4. 第四行告诉 `make` 将 `speller.o` 和 `dictionary.o` 链接成一个名为 `speller` 的文件。

**请务必通过执行 `make speller`（或仅仅是 `make`）来编译 `speller`。执行 `make dictionary` 是行不通的！**

## 规格要求

好了，现在的挑战是按顺序实现 `load`、`hash`、`size`、`check` 和 `unload`，要求尽可能高效地使用哈希表，从而使 `TIME IN load`、`TIME IN check`、`TIME IN size` 和 `TIME IN unload` 最小化。可以肯定的是，最小化意味着什么并不显而易见，因为当你为 `speller` 输入不同的 `dictionary` 和 `text` 时，这些基准测试肯定会发生变化。但这正是这个问题的挑战所在，如果不是乐趣所在的话。这个问题是你设计的机会。虽然我们邀请你尽量减少空间占用，但你最终的敌人是时间。但在你开始之前，请看一些规格要求。

- 你不得修改 `speller.c` 或 `Makefile`。
- 你可以修改 `dictionary.c`（事实上，为了完成 `load`、`hash`、`size`、`check` 和 `unload` 的实现，你必须修改它），但你不得修改 `load`、`hash`、`size`、`check` 或 `unload` 的声明（即原型）。不过，你可以在 `dictionary.c` 中添加新的函数和（局部或全局）变量。
- 你可以更改 `dictionary.c` 中 `N` 的值，以便你的哈希表可以拥有更多的桶。
- 你可以修改 `dictionary.h`，但你不得修改 `load`、`hash`、`size`、`check` 或 `unload` 的声明。
- 你对 `check` 的实现必须是不区分大小写的。换句话说，如果 `foo` 在字典中，那么对于任何形式的大写，`check` 都应该返回 true；`foo`、`foO`、`fOo`、`fOO`、`fOO`、`Foo`、`FoO`、`FOo` 和 `FOO` 都不应被视为拼写错误。
- 撇开大小写不谈，你对 `check` 的实现应该只对确实在 `dictionary` 中的单词返回 `true`。注意不要硬编码常用词（例如 `the`），以免我们向你的实现传递一个没有这些词的 `dictionary`。此外，唯一允许的所有格形式是那些确实在 `dictionary` 中的。换句话说，即使 `foo` 在 `dictionary` 中，如果 `foo's` 不在 `dictionary` 中，对于给定的 `foo's`，`check` 应该返回 `false`。
- 你可以假设传递给程序的任何 `dictionary` 都将与我们的结构完全相同，从上到下按字母顺序排序，每行一个单词，每个单词以 `\n` 结尾。你还可以假设 `dictionary` 将至少包含一个单词，没有单词会超过 `LENGTH`（`dictionary.h` 中定义的常量）个字符，没有单词会出现超过一次，每个单词将仅包含小写字母字符和可能的撇号，并且没有单词会以撇号开头。
- 你可以假设 `check` 只会被传递包含（大写或小写）字母字符和可能的撇号的单词。
- 你的拼写检查器只能接受 `text` 和可选的 `dictionary` 作为输入。虽然你可能会倾向于（特别是那些基础较好的同学）对我们的默认字典进行“预处理”，以便为它推导出一个“理想的哈希函数”，但你不得将任何此类预处理的输出保存到磁盘上，以便在随后的拼写检查器运行中将其加载回内存，从而获得优势。
- 你的拼写检查器不得有任何内存泄漏。请务必使用 `valgrind` 检查泄漏。
- **你编写的哈希函数最终应该是你自己的，而不是你在网上搜索到的。**

好了，准备好了吗？

- 实现 `load`。
- 实现 `hash`。
- 实现 `size`。
- 实现 `check`。
- 实现 `unload`。

## 提示

实现 `load`

完成 `load` 函数。`load` 应该将字典加载到内存中（特别是加载到哈希表中！）。如果成功，`load` 应该返回 `true`，否则返回 `false`。

考虑到这个问题只是由更小的问题组成的：

1. 打开字典文件
2. 读取文件中的每个单词
   
   1. 将每个单词添加到哈希表中
3. 关闭字典文件

写一些伪代码来提醒自己这样做：

```js
bool load(const char *dictionary)
{
    // 打开字典文件

    // 读取文件中的每个单词

        // 将每个单词添加到哈希表中

    // 关闭字典文件
}
```

首先考虑如何打开字典文件。[`fopen`](https://manual.cs50.io/3/fopen) 是一个自然的选择。你可以使用 `r` 模式，因为你只需要从字典文件中*读取*单词（而不是*写入*或*追加*它们）。

```js
bool load(const char *dictionary)
{
    // 打开字典文件
    FILE *source = fopen(dictionary, "r");

    // 读取文件中的每个单词

        // 将每个单词添加到哈希表中

    // 关闭字典文件
}
```

在继续之前，你应该编写代码来检查文件是否正确打开。这取决于你！确保关闭你打开的每个文件也是最好的做法，所以现在是编写关闭字典文件代码的好时机：

```js
bool load(const char *dictionary)
{
    // 打开字典文件
    FILE *source = fopen(dictionary, "r");

    // 读取文件中的每个单词

        // 将每个单词添加到哈希表中

    // 关闭字典文件
    fclose(source);
}
```

剩下的就是读取文件中的每个单词并将每个单词添加到哈希表中。当整个操作成功时返回 `true`，如果失败则返回 `false`。考虑遵循本题的演练视频，继续将子问题分解为更小的问题。例如，将每个单词添加到哈希表可能只需要实现几个更小的步骤：

1. 为新的哈希表节点创建空间
2. 将单词复制到新节点中
3. 对单词进行哈希处理以获得其哈希值
4. 将新节点插入哈希表（使用其哈希值指定的索引）

当然，解决这个问题的方法不止一种，每种方法都有自己的设计权衡。因此，剩下的代码由你决定！

实现 `hash`

完成 `hash` 函数。`hash` 应该接受一个字符串 `word` 作为输入，并返回一个正的（“无符号”）`int`。

提供给你的哈希函数根据 `word` 的第一个字符返回 0 到 25（含）之间的 `int`。然而，除了使用单词的首字母（或*首批字符*）之外，还有许多实现哈希函数的方法。考虑使用 ASCII 值之和或单词长度的哈希函数。一个好的哈希函数可以减少“冲突”并在哈希表“桶”之间具有（大部分！）均匀的分布。

实现 `size`

完成 `size` 函数。`size` 应该返回加载到字典中的单词数量。考虑解决此问题的两种方法：

- 在将每个单词加载到字典中时对其进行计数。当调用 `size` 时返回该计数值。
- 每次调用 `size` 时，遍历哈希表中的单词以对它们进行计数。返回该计数值。

哪种对你来说最有效率？无论你选择哪一种，我们都会把代码留给你。

实现 `check`

完成 `check` 函数。如果单词在字典中，`check` 应该返回 `true`，否则返回 `false`。

考虑到这个问题也是由更小的问题组成的。如果你已经实现了一个哈希表，寻找一个单词只需要几个步骤：

1. 对单词进行哈希处理以获得其哈希值
2. 在单词哈希值指定的位置搜索哈希表
   
   1. 如果找到该单词，则返回 `true`
3. 如果未找到该单词，则返回 `false`

要不区分大小写地比较两个字符串，你可能会发现 [`strcasecmp`](https://man.cs50.io/3/strcasecmp)（在 `strings.h` 中声明）很有用！你可能还想确保你的哈希函数是不区分大小写的，这样 `foo` 和 `FOO` 具有相同的哈希值。

实现 `unload`

完成 `unload` 函数。务必在 `unload` 中 `free` 你在 `load` 中分配的任何内存！

回想一下，`valgrind` 是你最新的好朋友。要知道 `valgrind` 会在程序实际运行时监控泄漏，所以如果你想让 `valgrind` 在你使用特定的 `dictionary` 和/或文本时分析 `speller`，请务必提供命令行参数，如下所示。最好使用较小的文本，否则 `valgrind` 可能需要相当长的时间运行。

```
valgrind ./speller texts/cat.txt
```

如果你运行 `valgrind` 而不为 `speller` 指定 `text`，你的 `load` 和 `unload` 实现实际上不会被调用（因此也不会被分析）。

如果不确定如何解释 `valgrind` 的输出，尽管向 `help50` 寻求帮助：

```
help50 valgrind ./speller texts/cat.txt
```

## 演练视频

**请注意，此播放列表中有 6 个视频。[在 YouTube 上打开](https://www.youtube.com/playlist?list=PLhQjrBD2T382T4b6jjwX_qbU23E_Unwcz)。**

## 如何测试

如何检查你的程序是否输出了正确的拼写错误单词？好吧，欢迎你查阅 `speller` 目录下的 `keys` 目录中的“答案键”。例如，在 `keys/lalaland.txt` 中包含你的程序*应该*认为拼写错误的所有单词。

因此，你可以像下面这样在一个窗口中对某些文本运行你的程序。

```
./speller texts/lalaland.txt
```

然后你可以在另一个窗口中对同一文本运行官方提供的解决方案，如下所示。

```
./speller50 texts/lalaland.txt
```

然后你可以并排目测比较两个窗口。不过，这可能很快就会变得乏味。因此，你可能想将程序的输出“重定向”到一个文件中，如下所示。

```
./speller texts/lalaland.txt > student.txt
./speller50 texts/lalaland.txt > staff.txt
```

然后，你可以使用 `diff` 之类的程序在同一个窗口中并排比较这两个文件，如下所示。

```
diff -y student.txt staff.txt
```

或者，为了节省时间，你可以直接将程序的输出（假设你将其重定向到，例如 `student.txt`）与其中一个答案键进行比较，而无需运行官方解决方案，如下所示。

```
diff -y student.txt keys/lalaland.txt
```

如果你的程序输出与官方输出匹配，`diff` 将输出两列，这两列除了底部的运行时间外应该完全相同。但是，如果这两列不同，你会在它们不同的地方看到 `>` 或 `|`。例如，如果你看到

```
MISSPELLED WORDS                                                MISSPELLED WORDS

TECHNO                                                          TECHNO
L                                                               L
                                                              > Thelonious
Prius                                                           Prius
                                                              > MIA
L                                                               L
```

这意味着你的程序（其输出在左侧）不认为 `Thelonious` 或 `MIA` 拼写错误，尽管官方输出（在右侧）认为拼写错误，这可以从左侧列中缺少 `Thelonious` 而右侧列中存在 `Thelonious` 暗示出来。

最后，请务必使用默认的大字典和小字典进行测试。注意不要假设如果你的解决方案在大字典下成功运行，它也会在小字典下成功运行。以下是如何尝试小字典的方法：

```
./speller dictionaries/small texts/cat.txt 
```

### 正确性测试

```
check50 cs50/problems/2026/x/speller
```

### 代码风格测试

```
style50 dictionary.c
```

## 官方解答

如何评估你的代码有多快（以及是否正确）？好吧，一如既往，请随意尝试官方解决方案，如下所示，并将其数据与你的进行比较。

```
./speller50 texts/lalaland.txt
```

## 如何提交

在你的终端中，执行以下命令来提交你的工作，并回答随后出现的提示。

```
submit50 cs50/problems/2026/x/speller
```
