title: "Mario - CS50x 2026"
pset: 6
draft: "false"
---

![ảnh chụp màn hình Mario nhảy lên kim tự tháp](pyramids.png)

## Bài toán cần giải quyết

Trong một tệp có tên là `mario.py` tại một thư mục có tên là `sentimental-mario-more`, hãy viết một chương trình để tái tạo lại các nửa kim tự tháp sử dụng các dấu thăng (`#`) làm các khối gạch, giống hệt như những gì bạn đã làm trong [Bài tập 1](../../../1/). Lần này, chương trình của bạn phải được viết bằng Python!

## Demo

## Yêu cầu

- Để làm cho mọi thứ thú vị hơn, trước tiên hãy nhắc người dùng bằng hàm `get_int` để lấy chiều cao của nửa kim tự tháp, là một số nguyên dương trong khoảng từ `1` đến `8` (bao gồm cả hai số). (Chiều cao của các nửa kim tự tháp trong hình trên là `4`, chiều rộng của mỗi nửa kim tự tháp là `4`, với một khoảng trống có kích thước là `2` ngăn cách chúng).
- Nếu người dùng không cung cấp được một số nguyên dương không lớn hơn `8`, bạn nên yêu cầu họ nhập lại một lần nữa.
- Sau đó, tạo ra (với sự trợ giúp của hàm `print` và một hoặc nhiều vòng lặp) các nửa kim tự tháp mong muốn.
- Hãy cẩn thận căn chỉnh góc dưới bên trái của kim tự tháp với lề trái của cửa sổ terminal, đồng thời đảm bảo rằng có hai khoảng trắng giữa hai kim tự tháp và không có khoảng trắng thừa nào sau tập hợp các dấu thăng cuối cùng trên mỗi dòng.

## Cách kiểm tra

Mặc dù `check50` có sẵn cho bài toán này, nhưng bạn nên tự mình kiểm tra mã nguồn trước với mỗi trường hợp dưới đây.

- Chạy chương trình của bạn bằng lệnh `python mario.py` và đợi lời nhắc nhập dữ liệu. Nhập `-1` và nhấn enter. Chương trình của bạn nên từ chối đầu vào này vì không hợp lệ, bằng cách yêu cầu người dùng nhập lại một số khác.
- Chạy chương trình của bạn bằng lệnh `python mario.py` và đợi lời nhắc nhập dữ liệu. Nhập `0` và nhấn enter. Chương trình của bạn nên từ chối đầu vào này vì không hợp lệ, bằng cách yêu cầu người dùng nhập lại một số khác.
- Chạy chương trình của bạn bằng lệnh `python mario.py` và đợi lời nhắc nhập dữ liệu. Nhập `1` và nhấn enter. Chương trình của bạn sẽ tạo ra kết quả như bên dưới. Hãy chắc chắn rằng kim tự tháp được căn chỉnh về góc dưới bên trái của terminal và không có khoảng trắng thừa ở cuối mỗi dòng.

```
#  #
```

- Chạy chương trình của bạn bằng lệnh `python mario.py` và đợi lời nhắc nhập dữ liệu. Nhập `2` và nhấn enter. Chương trình của bạn sẽ tạo ra kết quả như bên dưới. Hãy chắc chắn rằng kim tự tháp được căn chỉnh về góc dưới bên trái của terminal và không có khoảng trắng thừa ở cuối mỗi dòng.

```
 #  #
##  ##
```

- Chạy chương trình của bạn bằng lệnh `python mario.py` và đợi lời nhắc nhập dữ liệu. Nhập `8` và nhấn enter. Chương trình của bạn sẽ tạo ra kết quả như bên dưới. Hãy chắc chắn rằng kim tự tháp được căn chỉnh về góc dưới bên trái của terminal và không có khoảng trắng thừa ở cuối mỗi dòng.

```
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########
```

- Chạy chương trình của bạn bằng lệnh `python mario.py` và đợi lời nhắc nhập dữ liệu. Nhập `9` và nhấn enter. Chương trình của bạn nên từ chối đầu vào này vì không hợp lệ, bằng cách yêu cầu người dùng nhập lại một số khác. Sau đó, nhập `2` và nhấn enter. Chương trình của bạn sẽ tạo ra kết quả như bên dưới. Hãy chắc chắn rằng kim tự tháp được căn chỉnh về góc dưới bên trái của terminal và không có khoảng trắng thừa ở cuối mỗi dòng.

```
 #  #
##  ##
```

- Chạy chương trình của bạn bằng lệnh `python mario.py` và đợi lời nhắc nhập dữ liệu. Nhập `foo` và nhấn enter. Chương trình của bạn nên từ chối đầu vào này vì không hợp lệ, bằng cách yêu cầu người dùng nhập lại một số khác.
- Chạy chương trình của bạn bằng lệnh `python mario.py` và đợi lời nhắc nhập dữ liệu. Không nhập gì cả và nhấn enter. Chương trình của bạn nên từ chối đầu vào này vì không hợp lệ, bằng cách yêu cầu người dùng nhập lại một số khác.

### Độ chính xác

```
check50 cs50/problems/2026/x/sentimental/mario/more
```

### Phong cách

```
style50 mario.py
```

## Cách nộp bài

Trong terminal của bạn, hãy thực thi lệnh dưới đây để nộp bài, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/sentimental/mario/more
```
