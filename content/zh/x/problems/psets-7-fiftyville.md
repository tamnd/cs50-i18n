---
title: "Fiftyville - CS50x 2026"
pset: 7
draft: false
---

## 待解决的问题

CS50 Duck 被偷了！Fiftyville 镇请求你协助破解这起黄小鸭失窃案。当地警方认为窃贼偷走黄小鸭后不久，就在一名同谋的协助下乘飞机逃离了该镇。你的目标是查明：

- 窃贼是谁，
- 窃贼逃到了哪个城市，以及
- 协助窃贼逃跑的同谋是谁

你唯一知道的线索是：窃案**发生在 2025 年 7 月 28 日**，地点在 **Humphrey Street**。

你将如何揭开这个谜团？Fiftyville 警方调取了案发前后的镇上记录，并为你准备了一个 SQLite 数据库 `fiftyville.db`，其中包含镇上的各种数据表。你可以使用 SQL 的 `SELECT` 查询来访问你感兴趣的数据。仅使用数据库中的信息，你的任务就是破解谜底。

## 演示

## 入门

在本项目中，你将使用由 CS50 团队提供的数据库。

下载分发代码

登录 [cs50.dev](https://cs50.dev/)，点击终端窗口，然后执行 `cd` 命令。你应该会看到终端提示符如下所示：

```
$
```

接着执行

```python
wget https://cdn.cs50.net/2026/x/psets/7/fiftyville.zip
```

以便将名为 `fiftyville.zip` 的压缩包下载到你的 codespace 中。

然后执行

```
unzip fiftyville.zip
```

来创建一个名为 `fiftyville` 的文件夹。你不再需要这个 ZIP 文件了，因此可以执行

```
rm fiftyville.zip
```

并在提示符后输入 “y” 并回车，以删除下载的 ZIP 文件。

现在输入

```bash
cd fiftyville
```

并按回车进入（即打开）该目录。你的提示符现在应该类似于下方所示。

```
fiftyville/ $
```

直接执行 `ls`，你应该能看到以下几个文件：

```
answers.txt  fiftyville.db  log.sql
```

如果你遇到任何问题，请重新执行上述步骤，看看能否发现哪里出错了！

## 规范

对于这个问题，解决谜题的过程与揭开谜底本身同样重要。在 `log.sql` 中，记录你对数据库运行的所有 SQL 查询。在每个查询上方，使用注释（在 SQL 中，注释是以 `--` 开头的行）标记为什么要运行该查询以及你希望从中获取什么信息。你可以使用日志文件中的注释来记录解决谜题时的思路：最终，这个文件应该作为你识别窃贼过程的证据！

在编写查询时，你可能会发现其中一些变得相当复杂。为了保持查询的可读性，请参考 [sqlstyle.guide](https://www.sqlstyle.guide) 中的良好风格原则。其中 [缩进 (indentation)](https://www.sqlstyle.guide/#indentation) 部分可能会特别有帮助！

一旦你破解了谜题，请完成 `answers.txt` 中的每一行，填入窃贼的名字、窃贼逃往的城市以及协助其逃离的同谋的名字。（请确保不要更改文件中的任何现有文本，也不要向文件中添加任何其他行！）

最后，你应该提交 `log.sql` 和 `answers.txt` 两个文件。

## 视频演示

## 提示

- 执行 `sqlite3 fiftyville.db` 开始对数据库运行查询。
  
  - 在运行 `sqlite3` 时，执行 `.tables` 将列出数据库中的所有表。
  - 在运行 `sqlite3` 时，执行 `.schema TABLE_NAME`（其中 `TABLE_NAME` 是数据库中的表名）将显示创建该表所使用的 `CREATE TABLE` 命令。这对于了解要查询哪些列非常有帮助！
- 你可能会发现从 `crime_scene_reports` 表开始很有帮助。首先寻找与案发日期和地点相匹配的犯罪现场报告。
- 查看[此 SQL 关键字参考](https://www.w3schools.com/sql/sql_ref_keywords.asp)以了解一些可能有用的 SQL 语法！

## 如何测试

### 正确性

```
check50 cs50/problems/2026/x/fiftyville
```

## 如何提交

在终端中执行以下命令提交你的工作，并根据弹出的提示进行操作。

```
submit50 cs50/problems/2026/x/fiftyville
```
