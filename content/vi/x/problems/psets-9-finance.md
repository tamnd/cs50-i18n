title: "C$50 Finance - CS50x 2026"
pset: 9
draft: false
---

Triển khai một trang web mà qua đó người dùng có thể “mua” và “bán” cổ phiếu, tương tự như hình dưới đây.

![C$50 Finance](finance_2024.png)

## Bối cảnh

Nếu bạn chưa rõ việc mua và bán cổ phiếu (tức là cổ phần của một công ty) có nghĩa là gì, hãy truy cập [vào đây](https://www.investopedia.com/articles/basics/06/invest1000.asp) để xem hướng dẫn.

Bạn sắp triển khai C$50 Finance, một ứng dụng web giúp bạn quản lý danh mục đầu tư cổ phiếu. Công cụ này không chỉ cho phép bạn kiểm tra giá cổ phiếu thực tế và giá trị danh mục đầu tư, mà còn cho phép bạn mua (thực ra là “mua” giả lập) và bán (thực ra là “bán” giả lập) cổ phiếu bằng cách truy vấn giá cổ phiếu.

Thực tế, có những công cụ (một trong số đó là IEX) cho phép bạn tải xuống báo giá cổ phiếu thông qua API (giao diện lập trình ứng dụng) của họ bằng các URL như `https://api.iex.cloud/v1/data/core/quote/nflx?token=API_KEY`. Lưu ý cách ký hiệu của Netflix (NFLX) được nhúng trong URL này; đó là cách IEX biết dữ liệu của ai cần trả về. Liên kết đó thực tế sẽ không trả về bất kỳ dữ liệu nào vì IEX yêu cầu bạn sử dụng API key, nhưng nếu có, bạn sẽ thấy phản hồi ở định dạng JSON (JavaScript Object Notation) như thế này:

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

Lưu ý rằng, giữa các dấu ngoặc nhọn là danh sách các cặp khóa-giá trị được ngăn cách bằng dấu phẩy, với dấu hai chấm ngăn cách mỗi khóa và giá trị tương ứng. Chúng ta sẽ làm điều gì đó rất tương tự với API cơ sở dữ liệu cổ phiếu của riêng mình.

Bây giờ, hãy chuyển sự chú ý sang việc lấy mã nguồn phân phối của bài toán này!

## Bắt đầu

Đăng nhập vào [cs50.dev](https://cs50.dev/), nhấp vào cửa sổ terminal của bạn và thực hiện lệnh `cd`. Bạn sẽ thấy dấu nhắc terminal của mình giống như bên dưới:

```
$
```

Tiếp theo, hãy thực thi lệnh

```python
wget https://cdn.cs50.net/2026/x/psets/9/finance.zip
```

để tải tệp ZIP có tên `finance.zip` vào codespace của bạn.

Sau đó thực hiện

```
unzip finance.zip
```

để tạo một thư mục có tên `finance`. Bạn không còn cần tệp ZIP nữa, vì vậy bạn có thể thực hiện lệnh

```
rm finance.zip
```

và trả lời “y” rồi nhấn Enter tại dấu nhắc để xóa tệp ZIP bạn đã tải xuống.

Bây giờ hãy gõ

```bash
cd finance
```

sau đó nhấn Enter để di chuyển vào (tức là mở) thư mục đó. Dấu nhắc của bạn bây giờ sẽ giống như bên dưới.

```
finance/ $
```

Thực hiện lệnh `ls`, bạn sẽ thấy một vài tệp và thư mục:

```
app.py  finance.db  helpers.py  requirements.txt  static/  templates/
```

Nếu bạn gặp bất kỳ rắc rối nào, hãy làm lại các bước tương tự và xem liệu bạn có thể xác định mình đã sai ở đâu không!

### Chạy ứng dụng

Khởi động máy chủ web tích hợp của Flask (bên trong thư mục `finance/`):

```bash
$ flask run
```

Truy cập URL được `flask` đưa ra để xem mã nguồn phân phối đang hoạt động. Tuy nhiên, lúc này bạn sẽ chưa thể đăng nhập hoặc đăng ký!

Trong thư mục `finance/`, chạy lệnh `sqlite3 finance.db` để mở `finance.db` bằng `sqlite3`. Nếu bạn chạy lệnh `.schema` trong dấu nhắc SQLite, hãy lưu ý cách `finance.db` đi kèm với một bảng có tên là `users`. Hãy xem cấu trúc (tức là schema) của nó. Lưu ý rằng theo mặc định, người dùng mới sẽ nhận được $10.000 tiền mặt. Nhưng nếu bạn chạy lệnh `SELECT * FROM users;`, thì vẫn chưa có bất kỳ người dùng nào (tức là các hàng) trong đó để duyệt.

Một cách khác để xem `finance.db` là sử dụng chương trình có tên phpLiteAdmin. Nhấp vào `finance.db` trong trình duyệt tệp của codespace, sau đó nhấp vào liên kết hiển thị bên dưới dòng chữ “Please visit the following link to authorize GitHub Preview”. Bạn sẽ thấy thông tin về chính cơ sở dữ liệu, cũng như bảng `users`, giống như bạn đã thấy trong dấu nhắc `sqlite3` với lệnh `.schema`.

### Tìm hiểu mã nguồn

#### `app.py`

Mở tệp `app.py`. Ở đầu tệp là một loạt các lệnh import, trong đó có mô-đun SQL của CS50 và một vài hàm bổ trợ (helper functions). Chúng ta sẽ nói thêm về chúng sớm thôi.

Sau khi cấu hình [Flask](https://flask.palletsprojects.com/en/stable/), hãy lưu ý cách tệp này vô hiệu hóa việc lưu bộ nhớ đệm (caching) của các phản hồi (miễn là bạn đang ở chế độ debug, đây là chế độ mặc định trong codespace code50), để tránh trường hợp bạn thay đổi một tệp nào đó nhưng trình duyệt của bạn không nhận ra. Tiếp theo, hãy lưu ý cách nó cấu hình [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) với một "filter" tùy chỉnh là `usd`, một hàm (được định nghĩa trong `helpers.py`) giúp định dạng các giá trị dưới dạng đô la Mỹ (USD) dễ dàng hơn. Sau đó, nó cấu hình thêm cho Flask để lưu trữ [sessions](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions) trên hệ thống tệp cục bộ (tức là đĩa cứng) thay vì lưu trữ chúng bên trong các cookie (được ký số), vốn là mặc định của Flask. Tệp sau đó cấu hình mô-đun SQL của CS50 để sử dụng `finance.db`.

Sau đó là một loạt các route, trong đó chỉ có hai route được triển khai đầy đủ: `login` và `logout`. Trước tiên hãy đọc qua phần triển khai của `login`. Lưu ý cách nó sử dụng `db.execute` (từ thư viện của CS50) để truy vấn `finance.db`. Và lưu ý cách nó sử dụng `check_password_hash` để so sánh mã băm (hash) mật khẩu của người dùng. Ngoài ra, hãy lưu ý cách `login` “ghi nhớ” rằng người dùng đã đăng nhập bằng cách lưu trữ `user_id` của họ (một số nguyên INTEGER) vào `session`. Bằng cách đó, bất kỳ route nào trong tệp này đều có thể kiểm tra xem người dùng nào, nếu có, đang đăng nhập. Cuối cùng, lưu ý rằng khi người dùng đăng nhập thành công, `login` sẽ chuyển hướng (redirect) về `"/"`, đưa người dùng đến trang chủ của họ. Trong khi đó, hãy lưu ý cách `logout` chỉ đơn giản là xóa sạch `session`, giúp người dùng đăng xuất một cách hiệu quả.

Lưu ý cách hầu hết các route được “trang trí” (decorate) bằng `@login_required` (một hàm cũng được định nghĩa trong `helpers.py`). Decorator đó đảm bảo rằng, nếu người dùng cố gắng truy cập bất kỳ route nào trong số đó, họ sẽ được chuyển hướng đến `login` trước để đăng nhập.

Cũng lưu ý rằng hầu hết các route hỗ trợ cả GET và POST. Mặc dù vậy, hầu hết chúng (hiện tại!) chỉ trả về một "lời xin lỗi" (apology), vì chúng chưa được triển khai.

#### `helpers.py`

Tiếp theo, hãy xem qua `helpers.py`. À, đây là phần triển khai của hàm `apology`. Lưu ý cách cuối cùng nó render một template có tên `apology.html`. Nó cũng định nghĩa bên trong chính nó một hàm khác là `escape`, được sử dụng đơn giản để thay thế các ký tự đặc biệt trong lời xin lỗi. Bằng cách định nghĩa `escape` bên trong `apology`, chúng ta đã giới hạn phạm vi của hàm trước chỉ trong hàm sau; không có hàm nào khác có thể (hoặc cần) gọi nó.

Tiếp theo trong tệp là `login_required`. Đừng lo lắng nếu hàm này hơi khó hiểu, nhưng nếu bạn từng thắc mắc làm thế nào một hàm có thể trả về một hàm khác, thì đây là một ví dụ!

Sau đó là `lookup`, một hàm mà khi nhận vào một ký hiệu `symbol` (ví dụ: NFLX), nó sẽ trả về báo giá cổ phiếu của một công ty dưới dạng một `dict` với ba khóa: `name` có giá trị là một chuỗi `str`; `price` có giá trị là một số thực `float`; và `symbol` có giá trị là một chuỗi `str` đã được chuẩn hóa (viết hoa), bất kể ký hiệu đó được viết hoa như thế nào khi truyền vào `lookup`. Lưu ý rằng đây không phải là giá "thời gian thực" nhưng chúng có thay đổi theo thời gian, giống như trong thế giới thực!

Cuối cùng trong tệp là `usd`, một hàm ngắn đơn giản giúp định dạng một số `float` thành USD (ví dụ: `1234.56` được định dạng thành `$1,234.56`).

#### `requirements.txt`

Tiếp theo, hãy xem nhanh `requirements.txt`. Tệp đó chỉ đơn giản chỉ định các gói (packages) mà ứng dụng này sẽ phụ thuộc vào.

#### `static/`

Liếc qua thư mục `static/`, bên trong đó là tệp `styles.css`. Đó là nơi chứa một số mã CSS ban đầu. Bạn có thể tự do thay đổi nó theo ý muốn.

#### `templates/`

Bây giờ hãy nhìn vào thư mục `templates/`. Trong `login.html` về cơ bản chỉ là một biểu mẫu HTML, được tạo kiểu với [Bootstrap](https://getbootstrap.com/). Trong khi đó, `apology.html` là một template cho lời xin lỗi. Nhớ lại rằng hàm `apology` trong `helpers.py` nhận vào hai đối số: `message`, được truyền cho `render_template` dưới dạng giá trị của `bottom`, và tùy chọn là `code`, được truyền cho `render_template` dưới dạng giá trị của `top`. Hãy xem trong `apology.html` cách các giá trị đó cuối cùng được sử dụng! Và [đây là lý do](https://github.com/jacebrowning/memegen) 0:-)

Cuối cùng là `layout.html`. Nó lớn hơn bình thường một chút, nhưng chủ yếu là vì nó đi kèm với một thanh điều hướng "navbar" đẹp mắt và thân thiện với thiết bị di động, cũng dựa trên Bootstrap. Lưu ý cách nó định nghĩa một block có tên `main`, bên trong đó các template (bao gồm `apology.html` và `login.html`) sẽ được đưa vào. Nó cũng bao gồm hỗ trợ cho [message flashing](https://flask.palletsprojects.com/en/1.1.x/quickstart/#message-flashing) của Flask để bạn có thể chuyển tiếp thông báo từ route này sang route khác cho người dùng xem.

## Yêu cầu kỹ thuật

### `register`

Hoàn thành việc triển khai `register` sao cho nó cho phép người dùng đăng ký tài khoản thông qua một biểu mẫu.

- Yêu cầu người dùng nhập tên người dùng (username), được triển khai dưới dạng một trường văn bản có `name` là `username`. Hiển thị lời xin lỗi nếu đầu vào của người dùng để trống hoặc tên người dùng đã tồn tại.
  
  - Lưu ý rằng [`cs50.SQL.execute`](https://cs50.readthedocs.io/libraries/cs50/python/#cs50.SQL) sẽ gây ra ngoại lệ `ValueError` nếu bạn cố gắng `INSERT` một tên người dùng trùng lặp vì chúng ta đã tạo một `UNIQUE INDEX` trên `users.username`. Vì vậy, hãy đảm bảo sử dụng `try` và `except` để xác định xem tên người dùng đã tồn tại hay chưa.
- Yêu cầu người dùng nhập mật khẩu, được triển khai dưới dạng một trường văn bản có `name` là `password`, và sau đó nhập lại chính mật khẩu đó, được triển khai dưới dạng một trường văn bản có `name` là `confirmation`. Hiển thị lời xin lỗi nếu một trong hai đầu vào để trống hoặc mật khẩu không khớp.
- Gửi đầu vào của người dùng qua phương thức `POST` tới `/register`.
- `INSERT` người dùng mới vào bảng `users`, lưu trữ mã băm (hash) mật khẩu của người dùng chứ không phải chính mật khẩu đó. Băm mật khẩu của người dùng bằng [`generate_password_hash`](https://werkzeug.palletsprojects.com/en/2.3.x/utils/#werkzeug.security.generate_password_hash). Rất có thể bạn sẽ muốn tạo một template mới (ví dụ: `register.html`) tương tự như `login.html`.

Khi bạn đã triển khai `register` chính xác, bạn sẽ có thể đăng ký tài khoản và đăng nhập (vì `login` và `logout` đã hoạt động sẵn)! Và bạn sẽ có thể thấy các hàng dữ liệu của mình qua phpLiteAdmin hoặc `sqlite3`.

### `quote`

Hoàn thành việc triển khai `quote` sao cho nó cho phép người dùng tra cứu giá hiện tại của một cổ phiếu.

- Yêu cầu người dùng nhập ký hiệu của cổ phiếu, được triển khai dưới dạng một trường văn bản có `name` là `symbol`.
- Gửi đầu vào của người dùng qua phương thức `POST` tới `/quote`.
- Rất có thể bạn sẽ muốn tạo hai template mới (ví dụ: `quote.html` và `quoted.html`). Khi người dùng truy cập `/quote` qua GET, hãy render một trong những template đó, bên trong đó phải là một biểu mẫu HTML gửi đến `/quote` qua POST. Để phản hồi cho một yêu cầu POST, `quote` có thể render template thứ hai đó, nhúng vào bên trong nó một hoặc nhiều giá trị từ hàm `lookup`.

### `buy`

Hoàn thành việc triển khai `buy` sao cho nó cho phép người dùng mua cổ phiếu.

- Yêu cầu người dùng nhập ký hiệu cổ phiếu, được triển khai dưới dạng một trường văn bản có `name` là `symbol`. Hiển thị lời xin lỗi nếu đầu vào để trống hoặc ký hiệu không tồn tại (theo giá trị trả về của `lookup`).
- Yêu cầu người dùng nhập số lượng cổ phiếu, được triển khai dưới dạng một trường văn bản có `name` là `shares`. Hiển thị lời xin lỗi nếu đầu vào không phải là một số nguyên dương.
- Gửi đầu vào của người dùng qua phương thức `POST` tới `/buy`.
- Sau khi hoàn tất, hãy chuyển hướng người dùng về trang chủ.
- Rất có thể bạn sẽ muốn gọi hàm `lookup` để tra cứu giá hiện tại của cổ phiếu.
- Rất có thể bạn sẽ muốn `SELECT` số tiền mặt mà người dùng hiện có trong bảng `users`.
- Thêm một hoặc nhiều bảng mới vào `finance.db` để theo dõi việc mua hàng. Lưu trữ đủ thông tin để bạn biết ai đã mua cái gì, với giá bao nhiêu và khi nào.
  
  - Sử dụng các kiểu dữ liệu SQLite phù hợp.
  - Định nghĩa các chỉ mục `UNIQUE` cho bất kỳ trường nào cần là duy nhất.
  - Định nghĩa các chỉ mục (không phải `UNIQUE`) cho bất kỳ trường nào bạn sẽ sử dụng để tìm kiếm (như qua lệnh `SELECT` với `WHERE`).
- Hiển thị lời xin lỗi, mà không hoàn thành việc mua, nếu người dùng không đủ khả năng mua số lượng cổ phiếu đó với giá hiện tại.
- Bạn không cần lo lắng về tình trạng tranh chấp (race conditions) hoặc sử dụng các giao dịch (transactions).

Khi bạn đã triển khai `buy` chính xác, bạn sẽ có thể thấy các giao dịch mua của người dùng trong (các) bảng mới của mình thông qua phpLiteAdmin hoặc `sqlite3`.

### `index`

Hoàn thành việc triển khai `index` sao cho nó hiển thị một bảng HTML tóm tắt cho người dùng hiện đang đăng nhập: họ sở hữu những cổ phiếu nào, số lượng cổ phiếu sở hữu, giá hiện tại của mỗi cổ phiếu và tổng giá trị của mỗi khoản nắm giữ (tức là số lượng cổ phiếu nhân với giá). Đồng thời hiển thị số dư tiền mặt hiện tại của người dùng cùng với tổng giá trị tài sản (tức là tổng giá trị cổ phiếu cộng với tiền mặt).

- Rất có thể bạn sẽ muốn thực hiện nhiều lệnh `SELECT`. Tùy thuộc vào cách bạn triển khai (các) bảng của mình, bạn có thể thấy các lệnh [GROUP BY](https://www.google.com/search?q=SQLite%20GROUP%20BY), [HAVING](https://www.google.com/search?q=SQLite%20HAVING), [SUM](https://www.google.com/search?q=SQLite%20SUM), và/hoặc [WHERE](https://www.google.com/search?q=SQLite%20WHERE) hữu ích.
- Rất có thể bạn sẽ muốn gọi hàm `lookup` cho mỗi cổ phiếu.

### `sell`

Hoàn thành việc triển khai `sell` sao cho nó cho phép người dùng bán bớt cổ phiếu (mà họ đang sở hữu).

- Yêu cầu người dùng nhập ký hiệu cổ phiếu, được triển khai dưới dạng một menu `select` có `name` là `symbol`. Hiển thị lời xin lỗi nếu người dùng không chọn cổ phiếu hoặc nếu (vì lý do nào đó sau khi gửi) người dùng không sở hữu bất kỳ cổ phiếu nào của công ty đó.
- Yêu cầu người dùng nhập số lượng cổ phiếu, được triển khai dưới dạng một trường văn bản có `name` là `shares`. Hiển thị lời xin lỗi nếu đầu vào không phải là số nguyên dương hoặc nếu người dùng không sở hữu nhiều cổ phiếu đến vậy.
- Gửi đầu vào của người dùng qua phương thức `POST` tới `/sell`.
- Sau khi hoàn tất, hãy chuyển hướng người dùng về trang chủ.
- Bạn không cần lo lắng về tình trạng tranh chấp (race conditions) hoặc sử dụng các giao dịch (transactions).

### `history`

Hoàn thành việc triển khai `history` sao cho nó hiển thị một bảng HTML tóm tắt tất cả các giao dịch của người dùng từ trước đến nay, liệt kê từng hàng một cho mọi lần mua và mọi lần bán.

- Đối với mỗi hàng, hãy làm rõ xem cổ phiếu đó được mua hay bán và bao gồm ký hiệu cổ phiếu, giá (mua hoặc bán), số lượng cổ phiếu đã mua hoặc bán, cùng với ngày và giờ diễn ra giao dịch.
- Bạn có thể cần sửa đổi bảng bạn đã tạo cho `buy` hoặc bổ sung thêm một bảng khác. Hãy cố gắng giảm thiểu sự dư thừa dữ liệu.

### Dấu ấn cá nhân

Triển khai ít nhất một dấu ấn cá nhân tùy chọn:

- Cho phép người dùng thay đổi mật khẩu của họ.
- Cho phép người dùng nạp thêm tiền mặt vào tài khoản của họ.
- Cho phép người dùng mua thêm cổ phiếu hoặc bán bớt cổ phiếu mà họ đã sở hữu thông qua chính trang `index`, mà không cần phải gõ ký hiệu cổ phiếu một cách thủ công.
- Triển khai một số tính năng khác có quy mô tương đương.

## Hướng dẫn chi tiết

## Kiểm chứng

Hãy đảm bảo kiểm tra ứng dụng web của bạn một cách thủ công, ví dụ như bằng cách:

- Đăng ký một người dùng mới và xác minh rằng trang danh mục đầu tư của họ tải đúng thông tin,
- Yêu cầu báo giá bằng một ký hiệu cổ phiếu hợp lệ,
- Mua một loại cổ phiếu nhiều lần, xác minh rằng danh mục đầu tư hiển thị đúng tổng số,
- Bán tất cả hoặc một phần của một loại cổ phiếu, một lần nữa xác minh danh mục đầu tư, và
- Xác minh rằng trang lịch sử hiển thị tất cả các giao dịch cho người dùng đã đăng nhập của bạn.

Đồng thời kiểm tra một số trường hợp sử dụng bất thường, ví dụ như:

- Nhập các chuỗi ký tự chữ cái vào các biểu mẫu chỉ yêu cầu số,
- Nhập số 0 hoặc số âm vào các biểu mẫu chỉ yêu cầu số dương,
- Nhập các giá trị dấu phẩy động vào các biểu mẫu chỉ yêu cầu số nguyên,
- Cố gắng chi tiêu nhiều tiền mặt hơn số tiền người dùng có,
- Cố gắng bán nhiều cổ phiếu hơn số cổ phiếu người dùng có,
- Nhập một ký hiệu cổ phiếu không hợp lệ, và
- Bao gồm các ký tự có khả năng gây nguy hiểm như `'` và `;` trong các truy vấn SQL.

Bạn cũng có thể kiểm tra tính hợp lệ của mã HTML của mình bằng cách nhấp vào nút **I ♥ VALIDATOR** ở chân trang của mỗi trang, nút này sẽ gửi mã HTML của bạn tới [validator.w3.org](https://validator.w3.org/).

Khi đã hài lòng, để kiểm tra mã của bạn với `check50`, hãy thực hiện lệnh dưới đây.

```
check50 cs50/problems/2026/x/finance
```

Lưu ý rằng `check50` sẽ kiểm tra toàn bộ chương trình của bạn. Nếu bạn chạy nó **trước khi** hoàn thành tất cả các hàm được yêu cầu, nó có thể báo lỗi ở các hàm thực tế đã đúng nhưng lại phụ thuộc vào các hàm khác chưa xong.

## Phong cách lập trình

```
style50 app.py
```

## Giải pháp của đội ngũ giảng viên

Bạn có thể tự do tạo kiểu cho ứng dụng của riêng mình theo cách khác, nhưng đây là giao diện giải pháp của đội ngũ giảng viên!

[https://finance.cs50.net/](https://finance.cs50.net/)

Hãy thoải mái đăng ký tài khoản và trải nghiệm thử. **Đừng** sử dụng mật khẩu mà bạn dùng trên các trang web khác.

Bạn **có thể** xem mã HTML và CSS của đội ngũ giảng viên để tham khảo.

## Gợi ý

- Để định dạng một giá trị dưới dạng giá trị đô la Mỹ (với số xu được liệt kê đến hai chữ số thập phân), bạn có thể sử dụng filter `usd` trong các template Jinja của mình (in các giá trị là `{{ value | usd }}` thay vì `{{ value }}`).
- Bên trong `cs50.SQL` là phương thức `execute` có đối số đầu tiên phải là một chuỗi `str` mã SQL. Nếu chuỗi đó chứa các tham số dấu hỏi mà các giá trị cần được liên kết vào, các giá trị đó có thể được cung cấp dưới dạng các tham số được đặt tên bổ sung cho `execute`. Xem phần triển khai của `login` để biết một ví dụ như vậy. Giá trị trả về của `execute` như sau:
  
  - Nếu `str` là một lệnh `SELECT`, thì `execute` trả về một `list` gồm không hoặc nhiều đối tượng `dict`, bên trong là các khóa và giá trị đại diện cho các trường và ô của bảng tương ứng.
  - Nếu `str` là một lệnh `INSERT`, và bảng được chèn dữ liệu vào có chứa một `PRIMARY KEY` tự động tăng, thì `execute` trả về giá trị của khóa chính của hàng mới được chèn.
  - Nếu `str` là một lệnh `DELETE` hoặc `UPDATE`, thì `execute` trả về số hàng đã bị xóa hoặc cập nhật bởi lệnh `str`.
- Lưu ý rằng `cs50.SQL` sẽ ghi lại vào cửa sổ terminal bất kỳ truy vấn nào bạn thực hiện thông qua `execute` (để bạn có thể xác nhận xem chúng có đúng như dự định hay không).
- Đảm bảo sử dụng các tham số liên kết bằng dấu hỏi (tức là một [paramstyle](https://www.python.org/dev/peps/pep-0249/#paramstyle) có tên là `named`) khi gọi phương thức `execute` của CS50, ví dụ như `WHERE ?`. **Không** sử dụng f-strings, [`format`](https://docs.python.org/3/library/functions.html#format) hoặc `+` (tức là nối chuỗi), để tránh nguy cơ bị tấn công SQL injection.
- Nếu (và chỉ khi) đã thành thạo SQL, bạn có thể sử dụng [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/index.html) hoặc [Flask-SQLAlchemy](https://flask-sqlalchemy.readthedocs.io/en/stable/) (tức là [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/latest/index.html)) thay vì `cs50.SQL`.
- Lưu ý rằng mặc dù bạn có thể xác thực các giá trị được nhập trong biểu mẫu HTML, nhưng những người dùng am hiểu có thể bỏ qua chúng. Hãy đảm bảo rằng bạn cũng đang xác thực các giá trị ở phía máy chủ (server-side). Tương tự như vậy, nếu bạn đã chọn sử dụng JavaScript trong giải pháp của mình, hãy đảm bảo rằng ứng dụng của bạn vẫn hoạt động nếu người dùng đã tắt JavaScript.
- Bạn có thể thêm các tệp tĩnh bổ sung vào thư mục `static/`.
- Nếu thêm các hàm bổ sung trong `helpers.py`, hãy đảm bảo không mở kết nối cơ sở dữ liệu mới. Nếu một hàm bổ trợ yêu cầu sử dụng cơ sở dữ liệu, hãy truyền nó vào như một tham số thay vì khởi tạo lại kết nối.
- Rất có thể bạn sẽ muốn tham khảo [tài liệu của Jinja](https://jinja.palletsprojects.com/en/3.1.x/) khi triển khai các template của mình.
- Bạn **có thể** nhờ người khác dùng thử (và cố gắng gây ra lỗi) trên trang web của mình.
- Bạn có thể thay đổi tính thẩm mỹ của trang web, thông qua các nguồn như:
  
  - [bootswatch.com](https://bootswatch.com/),
  - [getbootstrap.com/docs/5.1/content](https://getbootstrap.com/docs/5.1/content/),
  - [getbootstrap.com/docs/5.1/components](https://getbootstrap.com/docs/5.1/components/), và/hoặc
  - [memegen.link](https://memegen.link/).
- Bạn có thể thấy [tài liệu của Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) và [tài liệu của Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/) hữu ích!

## Câu hỏi thường gặp

### ImportError: No module named ‘application’

Theo mặc định, `flask` tìm kiếm một tệp có tên `app.py` trong thư mục làm việc hiện tại của bạn (vì chúng ta đã định cấu hình giá trị của `FLASK_APP`, một biến môi trường, là `app.py`). Nếu thấy lỗi này, rất có thể bạn đã chạy `flask` ở sai thư mục!

### OSError: \[Errno 98] Address already in use

Nếu khi chạy `flask`, bạn thấy lỗi này, rất có thể bạn (vẫn) đang chạy `flask` ở một tab khác. Hãy nhớ tắt tiến trình đó, ví dụ bằng tổ hợp phím Ctrl-C, trước khi khởi động lại `flask`. Nếu bạn không có bất kỳ tab nào như vậy, hãy thực thi lệnh `fuser -k 8080/tcp` để tắt bất kỳ tiến trình nào (vẫn) đang lắng nghe trên cổng TCP 8080.

## Cách nộp bài

Trong terminal của bạn, hãy thực hiện lệnh dưới đây để nộp bài làm của mình, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/finance
```

### Tại sao bài nộp của tôi vượt qua check50, nhưng lại hiển thị “No results” trong Gradebook sau khi chạy submit50?

Trong một số trường hợp, `submit50` có thể không chấm điểm bài làm do (1) định dạng không nhất quán trong tệp `app.py` của bạn, và/hoặc (2) các tệp bổ sung không cần thiết được nộp cùng với bài tập. Để khắc phục những vấn đề này, hãy chạy lệnh `style50 app.py` trong thư mục `finance`. Xử lý bất kỳ vấn đề nào được phát hiện. Tiếp theo, hãy kiểm tra nội dung thư mục `finance` của bạn. Xóa các tệp không liên quan, chẳng hạn như flask sessions hoặc các tệp khác không phải là một phần trong quá trình triển khai bài tập của bạn. Sau đó, chạy lại `check50` để đảm bảo bài nộp của bạn vẫn hoạt động tốt. Cuối cùng, chạy lại lệnh `submit50` ở trên. Kết quả của bạn sẽ xuất hiện trong [Gradebook](https://cs50.me/cs50x) của bạn sau vài phút.

Xin lưu ý rằng nếu có điểm số bằng số bên cạnh bài nộp finance của bạn trong khu vực `submissions` của [Gradebook](https://cs50.me/cs50x), thì quy trình được thảo luận ở trên không áp dụng cho bạn. Có khả năng bạn chưa đáp ứng đầy đủ các yêu cầu của bài tập và nên dựa vào `check50` để biết thêm manh mối về những việc còn lại cần làm.
