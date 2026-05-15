title: "Trang chủ - CS50x 2026"
pset: 8
draft: false
---

Xây dựng một trang chủ đơn giản sử dụng HTML, CSS, và JavaScript.

## Bối cảnh

Internet đã cho phép thực hiện những điều tuyệt vời: chúng ta có thể sử dụng công cụ tìm kiếm để nghiên cứu bất cứ điều gì có thể tưởng tượng được, giao tiếp với bạn bè và các thành viên gia đình trên khắp thế giới, chơi trò chơi, tham gia các khóa học và nhiều điều khác nữa. Nhưng thực tế là hầu hết tất cả các trang web chúng ta truy cập đều được xây dựng dựa trên ba ngôn ngữ cốt lõi, mỗi ngôn ngữ phục vụ một mục đích hơi khác nhau:

1. HTML, hay *HyperText Markup Language*, được sử dụng để mô tả nội dung của trang web;
2. CSS, *Cascading Style Sheets*, được sử dụng để mô tả thẩm mỹ của trang web; và
3. JavaScript, được sử dụng để làm cho trang web có tính tương tác và sinh động.

Hãy tạo một trang chủ đơn giản giới thiệu về bản thân bạn, sở thích hoặc hoạt động ngoại khóa yêu thích của bạn, hoặc bất kỳ điều gì khác mà bạn quan tâm.

## Bắt đầu

Đăng nhập vào [cs50.dev](https://cs50.dev/), nhấp vào cửa sổ terminal của bạn và thực thi lệnh `cd` một mình. Bạn sẽ thấy dấu nhắc lệnh của cửa sổ terminal giống như dưới đây:

```
$
```

Tiếp theo, hãy thực thi

```python
wget https://cdn.cs50.net/2026/x/psets/8/homepage.zip
```

để tải xuống một tệp ZIP có tên là `homepage.zip` vào codespace của bạn.

Sau đó thực thi

```
unzip homepage.zip
```

để tạo một thư mục có tên là `homepage`. Bạn không còn cần tệp ZIP nữa, vì vậy bạn có thể thực thi

```
rm homepage.zip
```

và phản hồi bằng "y" sau đó nhấn Enter tại dấu nhắc để xóa tệp ZIP bạn đã tải xuống.

Bây giờ gõ

```bash
cd homepage
```

theo sau là Enter để chuyển vào (nghĩa là mở) thư mục đó. Dấu nhắc của bạn bây giờ sẽ giống như dưới đây.

```
homepage/ $
```

Thực thi `ls` một mình, và bạn sẽ thấy một vài tệp:

```
index.html  styles.css
```

Nếu bạn gặp bất kỳ rắc rối nào, hãy thực hiện lại các bước tương tự và xem liệu bạn có thể xác định mình đã sai ở đâu không! Bạn có thể bắt đầu một máy chủ ngay lập tức để xem trang web của mình bằng cách chạy

```
http-server
```

trong cửa sổ terminal. Sau đó, nhấn Command-click (nếu dùng Mac) hoặc Control-click (nếu dùng PC) vào liên kết đầu tiên xuất hiện:

```
http-server running on LINK
```

Trong đó LINK là địa chỉ máy chủ của bạn.

## Yêu cầu kỹ thuật

Triển khai trong thư mục `homepage` của bạn một trang web phải:

- Chứa ít nhất bốn trang `.html` khác nhau, ít nhất một trong số đó là `index.html` (trang chính của trang web của bạn), và phải có thể đi từ bất kỳ trang nào trên trang web của bạn đến bất kỳ trang nào khác bằng cách theo một hoặc nhiều siêu liên kết.
- Sử dụng ít nhất mười (10) thẻ HTML riêng biệt ngoài `<html>`, `<head>`, `<body>`, và `<title>`. Việc sử dụng một thẻ (ví dụ: `<p>`) nhiều lần vẫn chỉ tính là một (1) trong mười thẻ đó!
- Tích hợp một hoặc nhiều tính năng từ Bootstrap vào trang web của bạn. Bootstrap là một thư viện phổ biến (đi kèm với rất nhiều lớp CSS và hơn thế nữa) mà qua đó bạn có thể làm đẹp trang web của mình. Truy cập [tài liệu của Bootstrap](https://getbootstrap.com/docs/5.2/) để bắt đầu. Đặc biệt, bạn có thể thấy một số [thành phần của Bootstrap](https://getbootstrap.com/docs/5.2/components/) đáng quan tâm. Để thêm Bootstrap vào trang web của bạn, chỉ cần bao gồm
  
  ```
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
  ```
  
  vào phần `<head>` của các trang của bạn, bên dưới đó bạn cũng có thể bao gồm
  
  ```
  <link href="styles.css" rel="stylesheet">
  ```
  
  để liên kết tệp CSS của riêng bạn.
- Có ít nhất một tệp stylesheet do bạn tự tạo, `styles.css`, sử dụng ít nhất năm (5) bộ chọn (selector) CSS khác nhau (ví dụ: thẻ (`example`), lớp (`.example`), hoặc ID (`#example`)), và trong đó bạn sử dụng tổng cộng ít nhất năm (5) thuộc tính CSS khác nhau, chẳng hạn như `font-size`, hoặc `margin`; và
- Tích hợp một hoặc nhiều tính năng của JavaScript vào trang web của bạn để làm cho trang web tương tác hơn. Ví dụ, bạn có thể sử dụng JavaScript để thêm thông báo (alert), tạo hiệu ứng theo khoảng thời gian lặp lại, hoặc thêm tính tương tác cho các nút, menu thả xuống hoặc biểu mẫu. Hãy thoải mái sáng tạo!
- Đảm bảo rằng trang web của bạn trông đẹp mắt trên cả trình duyệt di động cũng như máy tính xách tay và máy tính để bàn.

Bạn cũng nên tạo một tệp văn bản, `specification.txt`, liệt kê 10 thẻ HTML và 5 thuộc tính CSS mà bạn đã sử dụng, cũng như mô tả ngắn gọn (một câu) về cách bạn đã chọn sử dụng JavaScript và Bootstrap.

## Kiểm thử

Nếu bạn muốn xem trang web của mình trông như thế nào khi đang thực hiện, bạn có thể chạy `http-server`. Nhấn Command-click hoặc Control-click vào liên kết đầu tiên do http-server cung cấp, liên kết này sẽ mở trang web của bạn trong một tab mới. Sau đó, bạn có thể làm mới tab chứa trang web của mình để xem những thay đổi mới nhất.

Cũng hãy nhớ rằng bằng cách mở Công cụ dành cho nhà phát triển (Developer Tools) trong Google Chrome, bạn có thể *giả lập* việc truy cập trang của mình trên thiết bị di động bằng cách nhấp vào biểu tượng hình điện thoại ở bên trái mục **Elements** trong cửa sổ công cụ dành cho nhà phát triển, hoặc khi tab Công cụ dành cho nhà phát triển đã được mở, bằng cách nhấn `Ctrl`+`Shift`+`M` trên PC hoặc `Cmd`+`Shift`+`M` trên Mac, thay vì cần phải truy cập trang web của bạn trên một thiết bị di động riêng biệt!

## Đánh giá

Không có `check50` cho bài tập này! Thay vào đó, độ chính xác của trang web của bạn sẽ được đánh giá dựa trên việc liệu bạn có đáp ứng các yêu cầu kỹ thuật như đã nêu ở trên hay không, và liệu mã HTML của bạn có đúng định dạng và hợp lệ hay không. Để đảm bảo các trang của bạn đạt yêu cầu, bạn có thể sử dụng [Dịch vụ Kiểm tra Mã nguồn (Markup Validation Service)](https://validator.w3.org/#validate_by_input) này, sao chép và dán trực tiếp mã HTML của bạn vào hộp văn bản được cung cấp. Hãy lưu ý loại bỏ bất kỳ cảnh báo hoặc lỗi nào do trình kiểm tra gợi ý trước khi nộp bài!

Cũng hãy xem xét:

- liệu thẩm mỹ của trang web có trực quan và đơn giản để người dùng điều hướng hay không;
- liệu CSS của bạn đã được tách ra thành các tệp CSS riêng biệt hay chưa; và
- liệu bạn đã tránh được việc lặp lại và dư thừa bằng cách "kế thừa" (cascading) các thuộc tính kiểu dáng từ các thẻ cha hay chưa.

Rất tiếc là `style50` không hỗ trợ các tệp HTML, vì vậy bạn có trách nhiệm thụt lề và căn chỉnh các thẻ HTML của mình một cách sạch sẽ. Cũng nên biết rằng bạn có thể tạo một chú thích HTML bằng:

```
<!-- Chú thích ở đây -->
```

nhưng việc chú thích mã HTML của bạn không bắt buộc như khi chú thích mã trong C hoặc Python. Bạn cũng có thể chú thích CSS của mình, trong các tệp CSS, bằng:

```
/* Chú thích ở đây */
```

## Gợi ý

Để có các hướng dẫn khá toàn diện về các ngôn ngữ được giới thiệu trong bài toán này, hãy xem các hướng dẫn sau:

- [HTML](https://www.w3schools.com/html/)
- [CSS](https://www.w3schools.com/css/)
- [JavaScript](https://www.w3schools.com/js/)

## Cách nộp bài

Trong terminal của bạn, thực thi lệnh dưới đây để nộp bài làm của bạn, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/homepage
```
