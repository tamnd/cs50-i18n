---
title: "C$50 金融 - CS50x 2026"
pset: 9
draft: false
---

实现一个允许用户“买入”和“卖出”股票的网站，如下所示。

![C$50 Finance](finance_2024.png)

## 背景

如果你不太确定买卖股票（即公司的股份）意味着什么，请点击[这里](https://www.investopedia.com/articles/basics/06/invest1000.asp)查看教程。

你即将实现 C$50 金融 (C$50 Finance)，这是一个用于管理股票投资组合的 Web 应用程序。这个工具不仅允许你检查真实股票的价格和投资组合的价值，还能让你通过查询股票价格来买入（好吧，是“买入”）和卖出（好吧，是“卖出”）股票。

事实上，有一些工具（其中一个叫做 IEX）允许你通过其 API（应用程序编程接口）使用类似 `https://api.iex.cloud/v1/data/core/quote/nflx?token=API_KEY` 的 URL 下载股票行情。注意 Netflix 的代码 (NFLX) 是如何嵌入到这个 URL 中的；这就是 IEX 知道要返回谁的数据的方式。由于 IEX 需要使用 API 密钥，该链接实际上不会返回任何数据，但如果返回了，你会看到如下 JSON (JavaScript Object Notation) 格式的响应：

```
{
  "avgTotalVolume":6787785,
  "calculationPrice":"tops",
  "change":1.46,
  "changePercent":0.00336,
  "close":null,
  "closeSource":"official",
  "closeTime":null,
  "companyName":"Netflix Inc.",
  "currency":"USD",
  "delayedPrice":null,
  "delayedPriceTime":null,
  "extendedChange":null,
  "extendedChangePercent":null,
  "extendedPrice":null,
  "extendedPriceTime":null,
  "high":null,
  "highSource":"IEX real time price",
  "highTime":1699626600947,
  "iexAskPrice":460.87,
  "iexAskSize":123,
  "iexBidPrice":435,
  "iexBidSize":100,
  "iexClose":436.61,
  "iexCloseTime":1699626704609,
  "iexLastUpdated":1699626704609,
  "iexMarketPercent":0.00864679844447232,
  "iexOpen":437.37,
  "iexOpenTime":1699626600859,
  "iexRealtimePrice":436.61,
  "iexRealtimeSize":5,
  "iexVolume":965,
  "lastTradeTime":1699626704609,
  "latestPrice":436.61,
  "latestSource":"IEX real time price",
  "latestTime":"9:31:44 AM",
  "latestUpdate":1699626704609,
  "latestVolume":null,
  "low":null,
  "lowSource":"IEX real time price",
  "lowTime":1699626634509,
  "marketCap":192892118443,
  "oddLotDelayedPrice":null,
  "oddLotDelayedPriceTime":null,
  "open":null,
  "openTime":null,
  "openSource":"official",
  "peRatio":43.57,
  "previousClose":435.15,
  "previousVolume":2735507,
  "primaryExchange":"NASDAQ",
  "symbol":"NFLX",
  "volume":null,
  "week52High":485,
  "week52Low":271.56,
  "ytdChange":0.4790450244167119,
  "isUSMarketOpen":true
}
```

注意在花括号之间是一个逗号分隔的键值对列表，冒号分隔每个键及其值。我们将使用我们自己的股票数据库 API 执行非常相似的操作。

现在让我们把注意力转向获取此问题的分发代码！

## 入门

登录 [cs50.dev](https://cs50.dev/)，点击终端窗口，然后执行 `cd`。你应该会发现终端窗口的提示符类似于下面这样：

```
$
```

接下来执行

```python
wget https://cdn.cs50.net/2026/x/psets/9/finance.zip
```

以便将名为 `finance.zip` 的 ZIP 文件下载到你的 codespace 中。

然后执行

```
unzip finance.zip
```

来创建一个名为 `finance` 的文件夹。你不再需要这个 ZIP 文件了，所以可以执行

```
rm finance.zip
```

并在提示符处输入 “y” 后按回车键来删除你下载的 ZIP 文件。

现在输入

```bash
cd finance
```

并按回车进入（即打开）该目录。你的提示符现在应该类似于下面这样。

```
finance/ $
```

单独执行 `ls`，你应该会看到一些文件和文件夹：

```
app.py  finance.db  helpers.py  requirements.txt  static/  templates/
```

如果你遇到任何困难，请再次按照这些步骤操作，看看是否能确定哪里出了问题！

### 运行

启动 Flask 内置的 Web 服务器（在 `finance/` 目录下）：

```bash
$ flask run
```

访问 `flask` 输出的 URL 以查看分发代码的运行情况。不过，你现在还不能登录或注册！

在 `finance/` 目录下，运行 `sqlite3 finance.db` 以使用 `sqlite3` 打开 `finance.db`。如果在 SQLite 提示符下运行 `.schema`，请注意 `finance.db` 带有一个名为 `users` 的表。查看其结构（即模式）。注意，默认情况下，新用户将获得 10,000 美元的现金。但如果你运行 `SELECT * FROM users;`，其中（目前！）还没有任何用户（即行）可以浏览。

查看 `finance.db` 的另一种方法是使用名为 phpLiteAdmin 的程序。在 codespace 的文件浏览器中点击 `finance.db`，然后点击“Please visit the following link to authorize GitHub Preview”文字下方显示的链接。你应该会看到有关数据库本身的信息，以及一个 `users` 表，就像你在 `sqlite3` 提示符中使用 `.schema` 看到的一样。

### 理解

#### `app.py`

打开 `app.py`。文件顶部是一堆导入，其中包括 CS50 的 SQL 模块和一些辅助函数。稍后会详细介绍这些内容。

在配置 [Flask](https://flask.palletsprojects.com/en/stable/) 之后，注意此文件如何禁用响应缓存（前提是你处于调试模式，codespace 默认处于此模式），以免你更改了某些文件但浏览器未察觉。接下来注意它如何使用自定义“过滤器” `usd` 配置 [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)，`usd` 是一个函数（定义在 `helpers.py` 中），可以更轻松地将数值格式化为美元 (USD)。然后，它进一步配置 Flask 将 [sessions](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions) 存储在本地文件系统（即磁盘）上，而不是像 Flask 默认那样存储在（经过数字签名的）cookie 中。该文件随后配置 CS50 的 SQL 模块以使用 `finance.db`。

此后是一堆路由，其中只有两个已完全实现：`login` 和 `logout`。首先阅读 `login` 的实现。注意它如何使用 `db.execute`（来自 CS50 的库）来查询 `finance.db`。并注意它如何使用 `check_password_hash` 来比较用户密码的哈希值。还要注意 `login` 如何通过在 `session` 中存储用户的 `user_id`（一个 INTEGER）来“记住”用户已登录。这样，此文件的任何路由都可以检查哪个用户（如果有的话）已登录。最后，注意一旦用户成功登录，`login` 将重定向到 `"/"`，将用户带到他们的主页。同时，注意 `logout` 如何简单地清除 `session`，从而有效地注销用户。

注意大多数路由是如何使用 `@login_required`（也是在 `helpers.py` 中定义的函数）进行“装饰”的。该装饰器确保如果用户尝试访问这些路由中的任何一个，他或她将首先被重定向到 `login` 以便登录。

还要注意大多数路由如何支持 GET and POST。即便如此，它们中的大多数（目前！）只是返回一个 “apology”（道歉页面），因为它们尚未实现。

#### `helpers.py`

接下来看看 `helpers.py`。啊，这里有 `apology` 的实现。注意它最终渲染了一个模板 `apology.html`。它还在内部定义了另一个函数 `escape`，用于替换道歉信息中的特殊字符。通过在 `apology` 内部定义 `escape`，我们将前者的作用域限制在后者；其他函数将无法（也无需）调用它。

文件中接下来是 `login_required`。如果这个函数有点晦涩难懂也没关系，但如果你曾经好奇过一个函数如何返回另一个函数，这就是一个例子！

此后是 `lookup` 函数，给定一个 `symbol`（例如 NFLX），它以包含三个键的 `dict` 形式返回公司的股票报价：`name`（值为 `str`）、`price`（值为 `float`）和 `symbol`（值为 `str`，股票代码的规范化（大写）版本，无论传入 `lookup` 时该代码如何大小写）。请注意，这些不是“实时”价格，但确实会随时间变化，就像在现实世界中一样！

文件中的最后一个是 `usd`，这是一个简短的函数，只需将 `float` 格式化为 USD（例如 `1234.56` 格式化为 `$1,234.56`）。

#### `requirements.txt`

接下来快速浏览一下 `requirements.txt`。该文件仅规定了此应用程序将依赖的包。

#### `static/`

也扫一眼 `static/`，里面有 `styles.css`。这是一些初始 CSS 存放的地方。你可以根据需要随意修改它。

#### `templates/`

现在看 `templates/`。`login.html` 基本上就是一个使用 [Bootstrap](https://getbootstrap.com/) 样式化的 HTML 表单。与此同时，在 `apology.html` 中是一个道歉模板。回想一下 `helpers.py` 中的 `apology` 接受两个参数：`message`（作为 `bottom` 的值传递给 `render_template`）和可选的 `code`（作为 `top` 的值传递给 `render_template`）。在 `apology.html` 中注意这些值最终是如何被使用的！[这就是原因](https://github.com/jacebrowning/memegen) 0:-)

最后是 `layout.html`。它比平时大一点，但这主要是因为它带有一个漂亮的、适合移动设备的“navbar”（导航栏），也是基于 Bootstrap 的。注意它如何定义一个块 `main`，模板（包括 `apology.html` 和 `login.html`）将放入其中。它还包括对 Flask [message flashing](https://flask.palletsprojects.com/en/1.1.x/quickstart/#message-flashing) 的支持，以便你可以将消息从一个路由转发到另一个路由供用户查看。

## 规范

### `register`

完成 `register` 的实现，使其允许用户通过表单注册账户。

- 要求用户输入用户名，实现为 `name` 为 `username` 的文本字段。如果用户输入为空或用户名已存在，则渲染 apology。
  
  - 注意，如果你尝试 `INSERT` 重复的用户名，[`cs50.SQL.execute`](https://cs50.readthedocs.io/libraries/cs50/python/#cs50.SQL) 将抛出 `ValueError` 异常，因为我们在 `users.username` 上创建了 `UNIQUE INDEX`（唯一索引）。因此，请务必使用 `try` 和 `except` 来确定用户名是否已存在。
- 要求用户输入密码，实现为 `name` 为 `password` 的文本字段，然后再次输入相同的密码，实现为 `name` 为 `confirmation` 的文本字段。如果任一输入为空或密码不匹配，则渲染 apology。
- 通过 `POST` 将用户的输入提交到 `/register`。
- 将新用户 `INSERT` 到 `users` 中，存储用户密码的哈希值，而不是密码本身。使用 [`generate_password_hash`](https://werkzeug.palletsprojects.com/en/2.3.x/utils/#werkzeug.security.generate_password_hash) 对用户密码进行哈希处理。你可能想要创建一个与 `login.html` 非常相似的新模板（例如 `register.html`）。

一旦你正确实现了 `register`，你应该能够注册账户并登录（因为 `login` 和 `logout` 已经可以工作了）！你应该能够通过 phpLiteAdmin 或 `sqlite3` 看到你的数据行。

### `quote`

完成 `quote` 的实现，使其允许用户查找股票的当前价格。

- 要求用户输入股票代码，实现为 `name` 为 `symbol` 的文本字段。
- 通过 `POST` 将用户的输入提交到 `/quote`。
- 你可能想要创建两个新模板（例如 `quote.html` 和 `quoted.html`）。当用户通过 GET 访问 `/quote` 时，渲染其中一个模板，模板内应该包含一个通过 POST 提交到 `/quote` 的 HTML 表单。在响应 POST 时，`quote` 可以渲染第二个模板，在其中嵌入来自 `lookup` 的一个或多个值。

### `buy`

完成 `buy` 的实现，使其能够让用户买入股票。

- 要求用户输入股票代码，实现为 `name` 为 `symbol` 的文本字段。如果输入为空或代码不存在（根据 `lookup` 的返回值），则渲染 apology。
- 要求用户输入股份数量，实现为 `name` 为 `shares` 的文本字段。如果输入不是正整数，则渲染 apology。
- 通过 `POST` 将用户的输入提交到 `/buy`。
- 完成后，将用户重定向到主页。
- 你可能需要调用 `lookup` 来查询股票的当前价格。
- 你可能需要 `SELECT` 用户当前在 `users` 中有多少现金。
- 在 `finance.db` 中添加一个或多个新表，以便记录购买情况。存储足够的信息，以便你知道谁在什么时间以什么价格买了什么。
  
  - 使用适当的 SQLite 类型。
  - 在任何应该是唯一的字段上定义 `UNIQUE` 索引。
  - 在任何你将用于搜索的字段上定义（非 `UNIQUE`）索引（例如通过带有 `WHERE` 的 `SELECT`）。
- 如果用户负担不起当前价格下的股份数量，则渲染 apology，不完成购买。
- 你不需要担心竞态条件（或使用事务）。

一旦你正确实现了 `buy`，你应该能够在 phpLiteAdmin 或 `sqlite3` 中通过新表看到用户的购买记录。

### `index`

完成 `index` 的实现，使其以 HTML 表格的形式汇总当前登录用户所持有的股票、持股数量、每只股票的当前价格以及每项持仓的总价值（即股份乘以价格）。同时显示用户当前的现金余额以及总资产（即股票总价值加上现金）。

- 你可能需要执行多个 `SELECT`。根据你实现表的方式，你可能会对 [GROUP BY](https://www.google.com/search?q=SQLite%20GROUP%20BY)、[HAVING](https://www.google.com/search?q=SQLite%20HAVING)、[SUM](https://www.google.com/search?q=SQLite%20SUM) 和/或 [WHERE](https://www.google.com/search?q=SQLite%20WHERE) 感兴趣。
- 你可能需要为每只股票调用 `lookup`。

### `sell`

完成 `sell` 的实现，使其能够让用户卖出股票（他或她拥有的股票）。

- 要求用户输入股票代码，实现为 `name` 为 `symbol` 的 `select` 菜单。如果用户未能选择股票，或者（一旦提交后）用户并不拥有该股票的任何股份，则渲染 apology。
- 要求用户输入股份数量，实现为 `name` 为 `shares` 的文本字段。如果输入不是正整数，或者用户没有那么多该股票的股份，则渲染 apology。
- 通过 `POST` 将用户的输入提交到 `/sell`。
- 完成后，将用户重定向到主页。
- 你不需要担心竞态条件（或使用事务）。

### `history`

完成 `history` 的实现，使其以 HTML 表格的形式汇总用户有史以来的所有交易，逐行罗列每一次买入和每一次卖出。

- 对于每一行，明确标注股票是买入还是卖出，并包含股票代码、（买入或卖出）价格、买入或卖出的股份数量以及交易发生的日期和时间。
- 你可能需要修改你为 `buy` 创建的表或补充一个额外的表。尽量减少冗余。

### 个性化功能

实现至少一个你自选的个性化功能：

- 允许用户更改密码。
- 允许用户向其账户添加额外现金。
- 允许用户通过 `index` 页面直接买入更多股份或卖出已持有的股份，而无需手动输入股票代码。
- 实现其他类似难度的功能。

## 演示视频

## 测试

请务必手动测试你的 Web 应用程序，例如：

- 注册新用户并验证其投资组合页面是否加载了正确的信息，
- 使用有效的股票代码请求报价，
- 多次购买同一只股票，验证投资组合是否显示正确的总额，
- 卖出全部或部分股票，再次验证投资组合，
- 验证你的历史记录页面是否显示了登录用户的所有交易。

还要测试一些异常用法，例如：

- 在预期为数字的表单中输入字母字符串，
- 在预期为正数的表单中输入零或负数，
- 在预期为整数的表单中输入浮点值，
- 尝试花费超出用户拥有的现金，
- 尝试卖出超出用户拥有的股份，
- 输入无效的股票代码，
- 在 SQL 查询中包含像 `'` 和 `;` 这样可能存在风险的字符。

你还可以通过点击每个页面底部的 **I ♥ VALIDATOR** 按钮来检查 HTML 的有效性，这会将你的 HTML 提交给 [validator.w3.org](https://validator.w3.org/)。

满意后，执行以下命令使用 `check50` 测试你的代码。

```
check50 cs50/problems/2026/x/finance
```

请注意，`check50` 将对你的整个程序进行整体测试。如果你在完成所有必需的功能**之前**运行它，它可能会在实际上正确但依赖于其他功能的函数上报错。

## 风格

```
style50 app.py
```

## 工作人员的解决方案

欢迎你以不同的风格装饰你自己的应用程序，但这里是工作人员的解决方案看起来的样子！

[https://finance.cs50.net/](https://finance.cs50.net/)

随意注册一个账户并试玩。**不要**使用你在其他网站上使用的密码。

查看工作人员的 HTML 和 CSS 是**合理的**。

## 提示

- 要将数值格式化为美元价值（列出两位小数的角和分），你可以在 Jinja 模板中使用 `usd` 过滤器（打印数值为 `{{ value | usd }}` 而不是 `{{ value }}`。
- 在 `cs50.SQL` 中有一个 `execute` 方法，其第一个参数应该是 SQL 的 `str`。如果该 `str` 包含问号参数，则可以将这些值作为额外的命名参数提供给 `execute`。请参阅 `login` 的实现以获取此类示例。`execute` 的返回值如下：
  
  - 如果 `str` 是 `SELECT`，则 `execute` 返回一个包含零个或多个 `dict` 对象的 `list`，其中键和值分别代表表的字段和单元格。
  - 如果 `str` 是 `INSERT`，且插入数据的表包含自动增量的 `PRIMARY KEY`，则 `execute` 返回新插入行的主键值。
  - 如果 `str` 是 `DELETE` 或 `UPDATE`，则 `execute` 返回由 `str` 删除或更新的行数。
- 回想一下，`cs50.SQL` 会将你通过 `execute` 执行的任何查询记录到终端窗口（以便你可以确认它们是否符合预期）。
- 在调用 CS50 的 `execute` 方法时，请务必使用问号绑定参数（即 `named` 类型的 [paramstyle](https://www.python.org/dev/peps/pep-0249/#paramstyle)），例如 `WHERE ?`。**不要**使用 f-strings、[`format`](https://docs.python.org/3/library/functions.html#format) 或 `+`（即拼接），以免面临 SQL 注入攻击风险。
- 如果（且仅当）已经熟悉 SQL，欢迎你使用 [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/index.html) 或 [Flask-SQLAlchemy](https://flask-sqlalchemy.readthedocs.io/en/stable/)（即 [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/latest/index.html)）而不是 `cs50.SQL`。
- 回想一下，虽然你可以验证在 HTML 表单中输入的值，但精明的用户可能会绕过这些验证。请务必在服务器端也验证这些值。同样地，如果你在解决方案中选择了使用 JavaScript，请确保如果用户禁用了 JavaScript，你的应用程序仍然可以运行。
- 欢迎你在 `static/` 中添加额外的静态文件。
- 如果在 `helpers.py` 中添加额外的函数，请确保不要开启新的数据库连接。如果辅助函数需要使用数据库，请将其作为参数传入，而不是重新实例化连接。
- 在实现模板时，你可能需要查阅 [Jinja 文档](https://jinja.palletsprojects.com/en/3.1.x/)。
- 请他人试用你的网站（并尝试触发错误）是**合理的**。
- 欢迎你通过以下方式改变网站的美学风格：
  
  - [bootswatch.com](https://bootswatch.com/)、
  - [getbootstrap.com/docs/5.1/content](https://getbootstrap.com/docs/5.1/content/)、
  - [getbootstrap.com/docs/5.1/components](https://getbootstrap.com/docs/5.1/components/)、和/或
  - [memegen.link](https://memegen.link/)。
- 你可能会发现 [Flask 文档](https://flask.palletsprojects.com/en/1.1.x/quickstart/)和 [Jinja 文档](https://jinja.palletsprojects.com/en/2.11.x/templates/)很有帮助！

## 常见问题解答 (FAQs)

### ImportError: No module named ‘application’

默认情况下，`flask` 在当前工作目录中查找名为 `app.py` 的文件（因为我们已将环境变量 `FLASK_APP` 的值配置为 `app.py`）。如果看到此错误，说明你可能在错误的目录中运行了 `flask`！

### OSError: \[Errno 98] Address already in use

如果在运行 `flask` 时看到此错误，说明你可能已经在另一个标签页中运行了 `flask`。在再次启动 `flask` 之前，请务必结束另一个进程，例如使用 ctrl-c。如果你没有打开任何其他此类标签页，请执行 `fuser -k 8080/tcp` 以结束仍在监听 TCP 端口 8080 的任何进程。

## 如何提交

在你的终端中，执行以下命令提交你的工作，并回答出现的提示。

```
submit50 cs50/problems/2026/x/finance
```

### 为什么我的提交通过了 check50，但在运行 submit50 后，我的成绩单中显示 “No results”（无结果）？

在某些情况下，由于 (1) `app.py` 文件中的格式不一致，和/或 (2) 提交问题集时包含了额外的不需要的文件，`submit50` 可能会不给作业评分。要解决这些问题，请在 `finance` 文件夹中运行 `style50 app.py`。解决所有暴露出来的问题。接下来，检查 `finance` 文件夹的内容。删除多余的文件，例如 flask session 文件或其他不属于问题集实现的文件。此外，再次运行 `check50` 以确保你的提交仍然可以正常运行。最后，再次运行上面的 `submit50` 命令。你的结果将在几分钟内出现在你的 [成绩单](https://cs50.me/cs50x) 中。

请注意，如果你的 [成绩单](https://cs50.me/cs50x) 的 `submissions` 区域中 finance 提交旁边有数字分数，则上述程序不适用于你。很可能你还没有完全满足问题集的要求，应该依靠 `check50` 来寻找剩余工作的线索。
