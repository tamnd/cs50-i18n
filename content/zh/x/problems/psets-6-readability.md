---
title: "Readability - CS50x 2026"
pset: 6
draft: false
---

## 待解决的问题

在一个名为 `sentimental-readability` 的文件夹中创建一个名为 `readability.py` 的文件，编写一个程序，首先提示用户输入一段文本，然后根据 Coleman-Liau 公式输出该文本的年级水平（grade level），这与你在 [实验 2](../../2/) 中所做的一样，只不过这次你的程序应该用 Python 编写。

## 演示

## 要求

- 回想一下，Coleman-Liau 指数的计算公式为 `0.0588 * L - 0.296 * S - 15.8`，其中 `L` 是文本中每 100 个单词的平均字母数，`S` 是文本中每 100 个单词的平均句子数。
- 使用 CS50 库中的 `get_string` 来获取用户的输入，并使用 `print` 来输出你的答案。
- 你的程序应该统计文本中的字母数、单词数和句子数。你可以假设字母是任何从 `a` 到 `z` 的小写字符或从 `A` 到 `Z` 的大写字符；任何由空格分隔的字符序列都应计为一个单词；任何出现的句号、感叹号或问号都表示句子的结束。
- 你的程序应该输出 `"Grade X"`，其中 `X` 是由 Coleman-Liau 公式计算出的年级水平，四舍五入到最近的整数。
- 如果计算出的指数为 16 或更高（相当于或高于高年级本科生的阅读水平），你的程序应该输出 `"Grade 16+"`，而不是具体的指数。如果指数小于 1，你的程序应该输出 `"Before Grade 1"`。

## 如何测试

虽然此题目可以使用 `check50`，但我们鼓励你先针对以下每种情况自行测试代码。

- 运行你的程序 `python readability.py`，等待输入提示。输入 `One fish. Two fish. Red fish. Blue fish.` 并按回车。你的程序应该输出 `Before Grade 1`。
- 运行你的程序 `python readability.py`，等待输入提示。输入 `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` 并按回车。你的程序应该输出 `Grade 2`。
- 运行你的程序 `python readability.py`，等待输入提示。输入 `Congratulations! Today is your day. You're off to Great Places! You're off and away!` 并按回车。你的程序应该输出 `Grade 3`。
- 运行你的程序 `python readability.py`，等待输入提示。输入 `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` 并按回车。你的程序应该输出 `Grade 5`。
- 运行你的程序 `python readability.py`，等待输入提示。输入 `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` 并按回车。你的程序应该输出 `Grade 7`。
- 运行你的程序 `python readability.py`，等待输入提示。输入 `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` 并按回车。你的程序应该输出 `Grade 8`。
- 运行你的程序 `python readability.py`，等待输入提示。输入 `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` 并按回车。你的程序应该输出 `Grade 8`。
- 运行你的程序 `python readability.py`，等待输入提示。输入 `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` 并按回车。你的程序应该输出 `Grade 9`。
- 运行你的程序 `python readability.py`，等待输入提示。输入 `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` 并按回车。你的程序应该输出 `Grade 10`。
- 运行你的程序 `python readability.py`，等待输入提示。输入 `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` 并按回车。你的程序应该输出 `Grade 16+`。

### 正确性

```
check50 cs50/problems/2026/x/sentimental/readability
```

### 风格

```
style50 readability.py
```

## 如何提交

在你的终端中，执行以下命令来提交你的工作，并根据提示回答问题。

```
submit50 cs50/problems/2026/x/sentimental/readability
```
