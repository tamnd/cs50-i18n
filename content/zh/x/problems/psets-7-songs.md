---
title: "歌曲 - CS50x 2026"
pset: 7
draft: false
---

![Spotify Wrapped '22 Logo](wrapped.png)

## 待解决的问题

编写 SQL 查询，以回答有关 2018 年 [Spotify](https://en.wikipedia.org/wiki/Spotify) 上播放次数最多的 100 首歌曲数据库的问题。

## 演示

## 准备工作

在这个问题中，你将使用由 CS50 工作人员提供的数据库。

下载分发代码

打开 [VS Code](https://cs50.dev/)。

首先点击终端窗口内部，然后单独执行 `cd`。你应该会发现其“提示符”类似于下方内容。

```
$
```

点击终端窗口内部，然后执行

```python
wget https://cdn.cs50.net/2026/x/psets/7/songs.zip
```

然后按回车键，以便在你的 codespace 中下载一个名为 `songs.zip` 的 ZIP 文件。注意不要忽略 `wget` 和后面 URL 之间的空格，或者任何其他字符！

现在执行

```
unzip songs.zip
```

来创建一个名为 `songs` 的文件夹。你不再需要该 ZIP 文件，因此可以执行

```
rm songs.zip
```

并在提示符处输入 “y” 后按回车，以删除你下载的 ZIP 文件。

现在输入

```bash
cd songs
```

然后按回车，进入（即打开）该目录。你的提示符现在应该类似于下方内容。

```
songs/ $
```

如果一切顺利，你应该执行

```bash
ls
```

然后你会看到 8 个 .sql 文件、`songs.db` 和 `answers.txt`。

如果你遇到任何问题，请再次按照这些步骤操作，看看能否确定哪里出错了！

## 理解

为你提供的是一个名为 `songs.db` 的文件，这是一个 SQLite 数据库，存储了来自 [Spotify](https://developer.spotify.com/documentation/web-api/) 的关于歌曲及其艺术家的相关数据。该数据集包含 2018 年 Spotify 上播放次数最多的前 100 首歌曲。在终端窗口中，运行 `sqlite3 songs.db`，以便你可以开始对数据库执行查询。

首先，当 `sqlite3` 提示你提供查询时，输入 `.schema` 并按回车。这将输出用于生成数据库中每个表的 `CREATE TABLE` 语句。通过检查这些语句，你可以确定每个表中存在的列。

请注意，每个 `artist`（艺术家）都有一个 `id` 和一个 `name`（名称）。同样请注意，每首歌曲都有一个 `name`（名称）、一个 `artist_id`（对应于歌曲艺术家的 `id`），以及舞蹈性 (danceability)、能量 (energy)、音调 (key)、响度 (loudness)、词语含量 (speechiness，即音轨中语音的出现程度)、效价 (valence)、节奏 (tempo) 和歌曲时长 (duration，以毫秒为单位) 的值。

你面临的挑战是编写 SQL 查询，通过从一个或多个表中选择数据来回答各种不同的问题。完成之后，你将思考 Spotify 如何在他们的年度 [Spotify Wrapped (年度回顾)](https://en.wikipedia.org/wiki/Spotify_Wrapped) 活动中使用这些相同的数据来刻画听众的习惯。

## 实现细节

对于以下每个问题，你应该编写一个单一的 SQL 查询，输出每个问题指定的结果。你的回答必须采用单一 SQL 查询的形式，不过你可以在查询中嵌套其他查询。你**不应**假设任何特定歌曲或艺术家的 `id`：即使任何特定歌曲或人物的 `id` 不同，你的查询也应该是准确的。最后，每个查询应该只返回回答问题所必需的数据：例如，如果问题只要求你输出歌曲的名称，那么你的查询就不应该同时输出每首歌的节奏。

1. 在 `1.sql` 中，编写一个 SQL 查询，列出数据库中所有歌曲的名称。
   - 你的查询应该输出一张只有一列的表，显示每首歌曲的名称。
2. 在 `2.sql` 中，编写一个 SQL 查询，按节奏 (tempo) 递增顺序列出所有歌曲的名称。
   - 你的查询应该输出一张只有一列的表，显示每首歌曲的名称。
3. 在 `3.sql` 中，编写一个 SQL 查询，列出时长最长的 5 首歌曲的名称，按时长降序排列。
   - 你的查询应该输出一张只有一列的表，显示每首歌曲的名称。
4. 在 `4.sql` 中，编写一个 SQL 查询，列出舞蹈性 (danceability)、能量 (energy) 和效价 (valence) 均大于 0.75 的任何歌曲名称。
   - 你的查询应该输出一张只有一列的表，显示每首歌曲的名称。
5. 在 `5.sql` 中，编写一个 SQL 查询，返回所有歌曲的平均能量。
   - 你的查询应该输出一张只有一列、一行的表，包含平均能量。
6. 在 `6.sql` 中，编写一个 SQL 查询，列出 Post Malone 的歌曲名称。
   - 你的查询应该输出一张只有一列的表，显示每首歌曲的名称。
   - 你不应对 Post Malone 的 `artist_id` 做任何假设。
7. 在 `7.sql` 中，编写一个 SQL 查询，返回 Drake 的歌曲的平均能量。
   - 你的查询应该输出一张只有一列、一行的表，包含平均能量。
   - 你不应对 Drake 的 `artist_id` 做任何假设。
8. 在 `8.sql` 中，编写一个 SQL 查询，列出包含其他艺术家的歌曲名称。
   - 包含其他艺术家的歌曲在歌曲名称中会包含 “feat.”。
   - 你的查询应该输出一张只有一列的表，显示每首歌曲的名称。

## 提示

有关一些可能有所帮助的 SQL 语法，请参阅[此 SQL 关键字参考](https://www.w3schools.com/sql/sql_ref_keywords.asp)！

列出数据库中所有歌曲的名称

回想一下，要选择表中某一列的所有值，你可以使用 SQL 的 `SELECT` 关键字。`SELECT` 后面跟着你想要选择的列（或多个列），接着是 `FROM table`，其中 `table` 是你想要从中选择数据的表的名称。

那么，在 `1.sql` 中，尝试编写以下内容：

```sql
-- 数据库中的所有歌曲。
SELECT name
FROM songs;
```

按节奏递增顺序列出所有歌曲的名称

回想一下，SQL 有一个 `ORDER BY` 关键字，通过它你可以根据某一列的值对查询结果进行排序。例如，`ORDER BY tempo` 将根据 `tempo` 列对结果进行排序。

那么，在 `2.sql` 中，尝试编写以下内容：

```sql
-- 按节奏递增顺序排列的所有歌曲。
SELECT name
FROM songs
ORDER BY tempo;
```

列出时长最长的 5 首歌曲的名称，按时长降序排列

回想一下，`ORDER BY` 并不总是按升序排序。你可以通过在末尾添加 `DESC` 来指定结果按*降序*排序。例如，`ORDER BY duration_ms DESC` 将按时长降序排列结果。

另外回想一下，`LIMIT n` 可以指定你只需要匹配特定查询的前 \\(n\\) 行。例如，`LIMIT 5` 将仅返回查询的前五个结果。

那么，在 `3.sql` 中，尝试编写以下内容：

```sql
-- 时长最长的 5 首歌曲的名称，按时长降序排列。
SELECT name
FROM songs
ORDER BY duration_ms DESC
LIMIT 5;
```

列出舞蹈性、能量和效价均大于 0.75 的任何歌曲名称

回想一下，你可以使用 `WHERE` 子句在 SQL 中过滤结果，子句后面跟着一些通常用于测试行中列值的条件。

还要回想一下，SQL 的运算符功能与 C 语言的大致相同。例如，当左侧的值大于右侧的值时，`>` 的计算结果为“真 (true)”。你可以使用 `AND` 或 `OR` 将这些表达式连接在一起，形成一个更大的条件。

那么，在 `4.sql` 中，尝试编写以下内容：

```sql
-- 舞蹈性、能量和效价均大于 0.75 的任何歌曲名称。
SELECT name
FROM songs
WHERE danceability > 0.75 AND energy > 0.75 AND valence > 0.75;
```

查找所有歌曲的平均能量

回想一下，SQL 不仅支持选择特定行的关键字，还支持对这些行中的数据进行*聚合 (aggregate)*。特别是，你可能会发现 `AVG` 关键字（用于计算平均值）很有用。要聚合一列的结果，只需将聚合函数应用于该列。例如，`SELECT AVG(energy)` 将计算给定查询中 energy 列值的平均值。

那么，在 `5.sql` 中，尝试编写以下内容：

```sql
-- 所有歌曲的平均能量。
SELECT AVG(energy)
FROM songs;
```

列出 Post Malone 的歌曲名称

请注意，如果你在 sqlite 提示符下执行 `.schema songs`，`songs` 表中有歌曲名称，但没有艺术家名称！相反，`songs` 有一个 `artist_id` 列。那么，要列出 Post Malone 的歌曲名称，你首先需要确定 Post Malone 的艺术家 ID。

```sql
-- 确定 Post Malone 的艺术家 ID
SELECT id
FROM artists
WHERE name = 'Post Malone';
```

此查询返回 54。现在，你可以查询 `songs` 表中任何具有 Post Malone ID 的歌曲。

```sql
SELECT name
FROM songs
WHERE artist_id = 54;
```

但是，根据规范，你应该注意不要假设已知任何 ID。你可以通过*嵌套*你的两个查询来改进此查询的设计。

那么，在 `6.sql` 中，尝试编写以下内容：

```sql
-- Post Malone 的歌曲名称。
SELECT name
FROM songs
WHERE artist_id =
(
    SELECT id
    FROM artists
    WHERE name = 'Post Malone'
);
```

查找 Drake 的歌曲的平均能量

请注意，与之前的查询类似，你需要结合多个表才能成功运行此查询。你可以再次使用嵌套子查询，但也考虑另一种方法！

回想一下，你可以使用 SQL 的 `JOIN` 关键字将多个表合并为一个，只要你指定这些表中哪些列最终应该匹配即可。例如，以下查询连接了 `songs` 和 `artists` 表，指示 `songs` 表中的 `artist_id` 列和 `artists` 表中的 `id` 列应该匹配：

```sql
SELECT *
FROM songs
JOIN artists ON songs.artist_id = artists.id
```

合并这两个表后，只需过滤你的选择即可找到 Drake 歌曲的平均能量。

那么，在 `7.sql` 中，尝试编写以下内容：

```sql
-- Drake 的歌曲的平均能量
SELECT AVG(energy)
FROM songs
JOIN artists ON songs.artist_id = artists.id
WHERE artists.name = 'Drake';
```

列出包含其他艺术家的歌曲名称

对于此查询，请注意包含其他艺术家的歌曲通常会在其标题中提到 “feat.”。回想一下，SQL 的 `LIKE` 关键字可用于匹配具有特定短语（如 “feat.”！）的字符串。为此，你可以使用 `%`：这是一个通配符，可匹配任何字符序列。

那么，在 `8.sql` 中，尝试编写以下内容：

```sql
-- 包含其他艺术家的歌曲名称。
SELECT name
FROM songs
WHERE name LIKE '%feat.%';
```

## 步行演示

不确定如何解决？

## Spotify 年度回顾 (Spotify Wrapped)

[Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) 是一项向 Spotify 用户展示过去一年中播放次数最多的 100 首歌曲的功能。在 2021 年，Spotify Wrapped 为每位用户计算了一个[“音频光环 (Audio Aura)”](https://newsroom.spotify.com/2021-12-01/learn-more-about-the-audio-aura-in-your-spotify-2021-wrapped-with-aura-reader-mystic-michaela/)，即“根据 [他们的] 年度热门歌曲和艺术家所反映的 [他们的] 两种最主要的情绪读数”。假设 Spotify 通过查看一个人过去一年中前 100 首歌曲的平均能量、效价和舞蹈性来确定音频光环。在 `answers.txt` 中，思考以下问题：

- 如果 `songs.db` 包含了一位听众 2018 年的前 100 首歌曲，你会如何描述他们的“音频光环”？
- 假设一下，为什么你计算这种“光环”的方式可能不太能代表这位听众？你会提出哪些更好的计算这种“光环”的方法？

请务必将 `answers.txt` 连同你的每个 `.sql` 文件一起提交！

## 如何测试

### 正确性

```
check50 cs50/problems/2026/x/songs
```

## 如何提交

在你的终端中，执行以下命令来提交你的工作，并回答随后出现的提示。

```
submit50 cs50/problems/2026/x/songs
```
