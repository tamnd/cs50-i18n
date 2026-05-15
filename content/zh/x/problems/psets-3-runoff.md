---
title: "Runoff - CS50x 2026"
pset: 3
draft: false
---

## 问题待解

你已经了解了多数票选举（plurality elections），它遵循一个非常简单的确定选举获胜者的算法：每个投票者投一票，票数最多的候选人获胜。

但多数票选举确实有一些缺点。例如，在有三名候选人的选举中，如果投出以下选票，会发生什么？

![Five ballots, tie betweeen Alice and Bob](../fptp_ballot_1.png)

在这里，多数票选举将宣布 Alice 和 Bob 之间出现平局，因为两人各有两票。但这真的是正确的结果吗？

还有另一种投票系统，被称为排序复选制（ranked-choice voting system）。在排序复选制中，投票者可以投票给多名候选人。他们不仅是投票给自己的首选，还可以按偏好顺序列出候选人。因此，生成的选票可能如下所示。

![Five ballots, with ranked preferences](../ranked_ballot_1.png)

在这里，每位投票者除了指定他们的第一偏好候选人外，还指明了他们的第二和第三选择。现在，之前平局的选举就可以产生获胜者了。比赛最初在 Alice 和 Bob 之间打平，所以 Charlie 出局了。但选择 Charlie 的投票者更喜欢 Alice 而不是 Bob，因此这里可以宣布 Alice 为获胜者。

排序复选制还可以解决多数票选举的另一个潜在缺点。看看下面的选票。

![Nine ballots, with ranked preferences](../ranked_ballot_3.png)

谁应该赢得这次选举？在每位投票者仅选择其第一偏好的多数票选举中，Charlie 以四票获胜，而 Bob 只有三票，Alice 只有两票。但大多数投票者（9 人中的 5 人）会更喜欢 Alice 或 Bob，而不是 Charlie。通过考虑排序偏好，投票系统可能能够选出更符合投票者偏好的获胜者。

即时决选制（instant runoff system）就是这样一种排序复选制。在即时决选选举中，投票者可以根据自己的意愿对尽可能多的候选人进行排序。如果任何候选人获得了超过 50% 的第一偏好选票，该候选人即被宣布为选举获胜者。

如果没有候选人获得超过 50% 的选票，就会发生“即时决选”。得票数最少的候选人将从选举中被淘汰，任何最初选择该候选人为第一偏好的人，现在将考虑他们的第二偏好。为什么要这样做？实际上，这模拟了如果最不受欢迎的候选人最初没有参加选举会发生的情况。

该过程不断重复：如果没有候选人获得多数票，最后一名候选人将被淘汰，投票给他们的人将改为投票给他们的下一个偏好（且该偏好本身尚未被淘汰）。一旦有候选人获得多数票，该候选人即被宣布为获胜者。

听起来比多数票选举复杂一点，不是吗？但可以说它的好处是，作为一种选举系统，其获胜者能更准确地代表投票者的偏好。在一个名为 `runoff` 的文件夹中，创建一个名为 `runoff.c` 的文件，编写一个程序来模拟决选选举。

## 演示

## 分发代码

下载分发代码

登录 [cs50.dev](https://cs50.dev/)，点击终端窗口，并单独执行 `cd` 命令。你应该会发现终端窗口的提示符类似于以下内容：

```
$
```

接着执行

```python
wget https://cdn.cs50.net/2026/x/psets/3/runoff.zip
```

以便将名为 `runoff.zip` 的 ZIP 文件下载到你的 Codespace 中。

然后执行

```
unzip runoff.zip
```

以创建一个名为 `runoff` 的文件夹。你不再需要该 ZIP 文件，因此可以执行

```
rm runoff.zip
```

并在提示符处输入 “y” 后按回车键，以删除下载的 ZIP 文件。

现在输入

```bash
cd runoff
```

后按回车键进入（即打开）该目录。你的提示符现在应该类似于以下内容。

```
runoff/ $
```

如果一切顺利，你应该执行

```bash
ls
```

并看到一个名为 `runoff.c` 的文件。执行 `code runoff.c` 应该会打开该文件，你将在其中编写此问题集的代码。如果没有，请回顾你的步骤，看看是否能确定哪里出错了！

理解 `runoff.c` 中的代码

每当你准备扩展现有代码的功能时，最好先确保你理解它当前的状态。

首先看 `runoff.c` 的顶部。定义了两个常量：`MAX_CANDIDATES` 表示选举中的最大候选人数，`MAX_VOTERS` 表示选举中的最大投票者人数。

```
// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9
```

注意 `MAX_CANDIDATES` 被用来确定数组 `candidates` 的大小。

```
// Array of candidates
candidate candidates[MAX_CANDIDATES];
```

`candidates` 是一个 `candidate` 类型的数组。在 `runoff.c` 中，一个 `candidate` 是一个结构体（`struct`）。每个 `candidate` 都有一个 `string` 字段表示他们的名字 `name`，一个 `int` 表示他们当前拥有的票数 `votes`，以及一个名为 `eliminated` 的 `bool` 值，表示该候选人是否已从选举中被淘汰。数组 `candidates` 将跟踪选举中的所有候选人。

```
// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;
```

现在你可以更好地理解 `preferences` 这个二维数组了。数组 `preferences[i]` 将代表第 `i` 号投票者的所有偏好。整数 `preferences[i][j]` 将存储来自 `candidates` 数组的候选人索引，该候选人是投票者 `i` 的第 `j` 个偏好。

```
// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];
```

程序还有两个全局变量：`voter_count` 和 `candidate_count`。

```
// Numbers of voters and candidates
int voter_count;
int candidate_count;
```

现在来看 `main` 函数。注意在确定候选人数和投票者人数后，主投票循环开始，让每个投票者都有机会投票。当投票者输入他们的偏好时，会调用 `vote` 函数来记录所有偏好。如果在任何时候选票被判定为无效，程序将退出。

所有选票投完后，另一个循环开始：这个循环将不断进行决选过程，包括检查获胜者和淘汰最后一名候选人，直到产生获胜者。

这里的第一个调用是名为 `tabulate` 的函数，它应该查看所有投票者的偏好并计算当前的总票数，方法是查看每个投票者的首选且尚未被淘汰的候选人。接下来，`print_winner` 函数应该打印出获胜者（如果有的话）；如果有，程序结束。否则，程序需要确定当前仍在选举中的任何人获得的最低票数（通过调用 `find_min`）。如果结果显示选举中的每个人都以相同的票数持平（由 `is_tie` 函数确定），则宣布选举为平局；否则，通过调用 `eliminate` 函数，将最后一名（或多名）候选人从选举中淘汰。

如果你再往下看，你会看到剩下的函数——`vote`、`tabulate`、`print_winner`、`find_min`、`is_tie` 和 `eliminate`——都留给你去完成！**你只能修改 runoff.c 中的这些函数，不过如果你愿意，你可以在 runoff.c 顶部 `#include` 额外的头文件。**

## 提示

点击下面的折叠框阅读一些建议！

完成 `vote` 函数

完成 `vote` 函数。

- 该函数接受三个参数：`voter`、`rank` 和 `name`。
- 如果 `name` 与有效候选人的名字匹配，那么你应该更新全局 `preferences` 数组，以指明投票者 `voter` 将该候选人作为其 `rank` 偏好。请记住，`0` 是第一偏好，`1` 是第二偏好，依此类推。你可以假设没有两个候选人会有相同的名字。
- 如果偏好成功记录，函数应返回 `true`。否则，函数应返回 `false`。例如，当 `name` 不是候选人之一的名字时。

编写代码时，请参考以下提示：

- 回想一下，`candidate_count` 存储了选举中的候选人数。
- 回想一下，你可以使用 [`strcmp`](https://man.cs50.io/3/strcmp) 来比较两个字符串。
- 回想一下，`preferences[i][j]` 存储了作为第 `i` 位投票者的第 `j` 位排序偏好的候选人索引。

完成 `tabulate` 函数

完成 `tabulate` 函数。

- 该函数应更新决选此阶段每位候选人的票数 `votes`。
- 回想一下，在决选的每个阶段，每个投票者实际上都是投票给他们首选的、尚未被淘汰的候选人。

编写代码时，请参考以下提示：

- 回想一下，`voter_count` 存储了选举中的投票者人数，对于选举中的每个投票者，我们要计一张选票。
- 回想一下，对于投票者 `i`，他们的首选候选人由 `preferences[i][0]` 表示，第二选择由 `preferences[i][1]` 表示，依此类推。
- 回想一下，`candidate` 结构体有一个名为 `eliminated` 的字段，如果候选人已从选举中被淘汰，该字段将为 `true`。
- 回想一下，`candidate` 结构体有一个名为 `votes` 的字段，你可能需要为每个投票者首选的候选人更新该字段。
- 回想一下，一旦你为投票者的第一个未被淘汰的候选人投了票，你就应该停止，而不是继续查看他们的选票。你可以使用条件语句中的 `break` 提前跳出循环。

完成 `print_winner` 函数

完成 `print_winner` 函数。

- 如果任何候选人的票数超过半数，应打印其姓名，函数应返回 `true`。
- 如果还没有人赢得选举，函数应返回 `false`。

编写代码时，请参考以下提示：

- 回想一下，`voter_count` 存储了选举中的投票者人数。既然如此，你会如何表达赢得选举所需的票数？

完成 `find_min` 函数

完成 `find_min` 函数。

- 该函数应返回仍在选举中的任何候选人的最低票数总和。

编写代码时，请参考以下提示：

- 你可能需要遍历候选人，找到既仍在选举中又得票最少的候选人。在遍历候选人时，你应该记录哪些信息？

完成 `is_tie` 函数

完成 `is_tie` 函数。

- 该函数接受一个参数 `min`，它将是目前选举中任何人拥有的最低票数。
- 如果选举中剩余的每个候选人票数相同，函数应返回 `true`，否则返回 `false`。

编写代码时，请参考以下提示：

- 回想一下，如果仍在选举中的每个候选人票数相同，就会发生平局。还要注意，`is_tie` 函数接受一个参数 `min`，它是目前任何候选人拥有的最小票数。你如何利用 `min` 来判断选举是否为平局（或者相反，不是平局）？

完成 `eliminate` 函数

完成 `eliminate` 函数。

- 该函数接受一个参数 `min`，它将是目前选举中任何人拥有的最低票数。
- 该函数应淘汰得票数为 `min` 的一名（或多名）候选人。

## 讲解

## 如何测试

务必测试你的代码以确保它能处理……

- 包含任意数量候选人的选举（最多为 `MAX` 值 `9`）
- 通过名字为候选人投票
- 投给不在选票上的候选人的无效选票
- 如果只有一名获胜者，则打印选举获胜者
- 在所有剩余候选人平局的情况下不淘汰任何人

### 正确性

```
check50 cs50/problems/2026/x/runoff
```

### 风格

```
style50 runoff.c
```

## 如何提交

在终端中，执行以下命令以提交你的作品，并回答出现的提示。

```
submit50 cs50/problems/2026/x/runoff
```
