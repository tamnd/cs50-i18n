---
title: "趣闻问答 (Trivia) - CS50x 2026"
pset: 8
draft: false
---

编写一个网页，让用户回答趣闻问答题。

![screenshot of trivia questions](questions.png)

## 开始

打开 [cs50.dev](https://cs50.dev)。

首先点击终端窗口内部，然后执行 `cd` 命令。你会发现“提示符”类似于以下内容。

```
$
```

点击终端窗口，然后执行

```python
wget https://cdn.cs50.net/2025/fall/psets/8/trivia.zip
```

然后按回车键，以便在你的 codespace 中下载名为 `trivia.zip` 的压缩包。注意不要漏掉 `wget` 和后面 URL 之间的空格，以及其他任何字符！

现在执行

```
unzip trivia.zip
```

来创建一个名为 `trivia` 的文件夹。你不再需要这个 ZIP 文件了，所以可以执行

```
rm trivia.zip
```

并在提示符处输入 “y” 后按回车，以删除你下载的 ZIP 文件。

现在输入

```bash
cd trivia
```

然后按回车进入（即打开）该目录。你的提示符现在应该类似于以下内容。

```
trivia/ $
```

如果一切顺利，你应该执行

```bash
ls
```

你会看到一个 `index.html` 文件和一个 `styles.css` 文件。

如果你遇到任何困难，请再次按照这些步骤操作，看看能否找出出错的地方！

## 实现细节

使用 HTML、CSS 和 JavaScript 设计一个网页，让用户回答趣闻问答题。

- 在 `index.html` 的 “Part 1” 下方，使用 HTML 添加一个你自选的多选题。
  
  - 你应该使用 `h3` 标题作为题目文本。
  - 你应该为每个可能的选项设置一个 `button`。至少应该有三个选项，其中只有一个是正确的。
- 使用 JavaScript 添加逻辑，使按钮在用户点击时改变颜色。
  
  - 如果用户点击了错误答案的按钮，按钮应变为红色，且题目下方应出现文本显示 “Incorrect”。
  - 如果用户点击了正确答案的按钮，按钮应变为绿色，且题目下方应出现文本显示 “Correct!”。
- 在 `index.html` 的 “Part 2” 下方，使用 HTML 添加一个你自选的文本简答题。
  
  - 你应该使用 `h3` 标题作为题目文本。
  - 你应该使用 `input` 字段让用户输入答案。
  - 你应该使用一个 `button` 让用户确认他们的答案。
- 使用 JavaScript 添加逻辑，使文本框在用户确认答案时改变颜色。
  
  - 如果用户输入错误答案并按下确认按钮，文本框应变为红色，且题目下方应出现文本显示 “Incorrect”。
  - 如果用户输入正确答案并按下确认按钮，输入框应变为绿色，且题目下方应出现文本显示 “Correct!”。

此外，你还可以（可选）：

- 编辑 `styles.css` 来更改网页的 CSS 样式！
- 如果你愿意，可以在趣闻问答中添加更多的题目！

### 视频演示

这段视频是在课程仍在使用 CS50 IDE 编写代码时录制的。虽然界面可能与你的 codespace 不同，但两个环境的行为应该大体相似！

### 提示

- 使用 [`document.querySelector`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) 来查询单个 HTML 元素。
- 使用 [`document.querySelectorAll`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll) 来查询匹配查询条件的所有 HTML 元素。该函数返回所有匹配元素的数组。

不确定如何解决？

### 测试

这个项目没有 `check50`，因为实现方案会因你选择的题目而异！但请务必测试每道题的错误和正确回答，以确保你的网页做出相应反应。

在 `trivia` 目录下，在终端运行 `http-server` 来启动一个提供网页服务的 Web 服务器。

## 如何提交

在终端执行以下命令提交你的工作，并按提示回答问题。

```
submit50 cs50/problems/2026/x/trivia
```

想看官方解法吗？你可以在这里找到两种解题方法！

使用 JavaScript 创建事件监听器

```c
<!DOCTYPE html>

<html lang="en">
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
        <link href="styles.css" rel="stylesheet">
        <title>Trivia!</title>
        <script>

            // Wait for DOM content to load
            document.addEventListener('DOMContentLoaded', function() {

                // Get all elements with class "correct"
                let corrects = document.querySelectorAll('.correct');

                // Add event listeners to each correct button
                for (let i = 0; i < corrects.length; i++) {
                    corrects[i].addEventListener('click', function() {

                        // Set background color to green
                        corrects[i].style.backgroundColor = 'Green';

                        // Go to parent element of correct button and find the first element with class "feedback" which has that parent
                        corrects[i].parentElement.querySelector('.feedback').innerHTML = 'Correct!';
                    });
                }

                // When any incorrect answer is clicked, change color to red.
                let incorrects = document.querySelectorAll(".incorrect");
                for (let i = 0; i < incorrects.length; i++) {
                    incorrects[i].addEventListener('click', function() {

                        // Set background color to green
                        incorrects[i].style.backgroundColor = 'Red';

                        // Go to parent element of correct button and find the first element with class "feedback" which has that parent
                        incorrects[i].parentElement.querySelector('.feedback').innerHTML = 'Incorrect';
                    });
                }

                // Check free response submission
                document.querySelector('#check').addEventListener('click', function() {
                    let input = document.querySelector('input');
                    if (input.value === 'Switzerland') {
                        input.style.backgroundColor = 'green';
                        input.parentElement.querySelector('.feedback').innerHTML = 'Correct!';
                    }
                    else {
                        input.style.backgroundColor = 'red';
                        input.parentElement.querySelector('.feedback').innerHTML = 'Incorrect';
                    }
                });
            });
        </script>
    </head>
    <body>
        <div class="header">
            <h1>Trivia!</h1>
        </div>

        <div class="container">
            <div class="section">
                <h2>Part 1: Multiple Choice </h2>
                <hr>
                <h3>What is the approximate ratio of people to sheep in New Zealand?</h3>
                <button class="incorrect">6 people per 1 sheep</button>
                <button class="incorrect">3 people per 1 sheep</button>
                <button class="incorrect">1 person per 1 sheep</button>
                <button class="incorrect">1 person per 3 sheep</button>
                <button class="correct">1 person per 6 sheep</button>
                <p class="feedback"></p>
            </div>

            <div class="section">
                <h2>Part 2: Free Response</h2>
                <hr>
                <h3>In which country is it illegal to own only one guinea pig, as a lone guinea pig might get lonely?</h3>
                <input type="text"></input>
                <button id="check">Check Answer</button>
                <p class="feedback"></p>
            </div>
        </div>
    </body>
</html>
```

使用 HTML 创建事件监听器

```js
<!DOCTYPE html>

<html lang="en">
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
        <link href="styles.css" rel="stylesheet">
        <title>Trivia!</title>
        <script>
            function checkMultiChoice(event) {

                // Get the element which triggered the event
                let button = event.target;

                // Check if the element's inner HTML matches expected answer
                if (button.innerHTML == '1 person per 6 sheep') {
                    button.style.backgroundColor = 'Green';
                    button.parentElement.querySelector('.feedback').innerHTML = 'Correct!';
                }
                else {
                    button.style.backgroundColor = 'Red';
                    button.parentElement.querySelector('.feedback').innerHTML = 'Incorrect';
                }
            }

            function checkFreeResponse(event) {

                // Get the element which triggered the event
                let button = event.target;

                // Get the input element corresponding to the button
                let input = button.parentElement.querySelector('input');

                // Check for correct answer
                if (input.value === 'Switzerland') {
                    input.style.backgroundColor = 'Green';
                    input.parentElement.querySelector('.feedback').innerHTML = 'Correct!';
                }
                else {
                    input.style.backgroundColor = 'Red';
                    input.parentElement.querySelector('.feedback').innerHTML = 'Incorrect';
                }
            }
        </script>
    </head>
    <body>
        <div class="header">
            <h1>Trivia!</h1>
        </div>

        <div class="container">
            <div class="section">
                <h2>Part 1: Multiple Choice </h2>
                <hr>
                <h3>What is the approximate ratio of people to sheep in New Zealand?</h3>
                <button onclick="checkMultiChoice(event)">6 people per 1 sheep</button>
                <button onclick="checkMultiChoice(event)">3 people per 1 sheep</button>
                <button onclick="checkMultiChoice(event)">1 person per 1 sheep</button>
                <button onclick="checkMultiChoice(event)">1 person per 3 sheep</button>
                <button onclick="checkMultiChoice(event)">1 person per 6 sheep</button>
                <p class="feedback"></p>
            </div>

            <div class="section">
                <h2>Part 2: Free Response</h2>
                <hr>
                <h3>In which country is it illegal to own only one guinea pig, as a lone guinea pig might get lonely?</h3>
                <input type="text"></input>
                <button onclick="checkFreeResponse(event)">Check Answer</button>
                <p class="feedback"></p>
            </div>
        </div>
    </body>
</html>
```
