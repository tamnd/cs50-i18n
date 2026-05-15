title: "Mario - CS50x 2026"
pset: 6
draft: false
---

![ảnh chụp màn hình Mario đang nhảy lên kim tự tháp](pyramid.png)

## Bài toán cần giải quyết

Trong một tệp có tên là `mario.py` trong một thư mục có tên là `sentimental-mario-less`, hãy viết một chương trình tái hiện lại một nửa kim tự tháp bằng cách sử dụng các dấu thăng (`#`) làm các khối gạch, chính xác như bạn đã làm trong [Bộ bài tập 1](../../../1/). Lần này chương trình của bạn phải được viết bằng Python!

## Demo

## Yêu cầu

- Để mọi thứ trở nên thú vị hơn, trước tiên hãy yêu cầu người dùng nhập chiều cao của nửa kim tự tháp bằng hàm `get_int`, là một số nguyên dương trong khoảng từ `1` đến `8` (bao gồm cả hai số này).
- Nếu người dùng không cung cấp một số nguyên dương không lớn hơn `8`, bạn nên yêu cầu họ nhập lại một lần nữa.
- Sau đó, tạo ra nửa kim tự tháp mong muốn (với sự trợ giúp của hàm `print` và một hoặc nhiều vòng lặp).
- Hãy lưu ý căn chỉnh góc dưới bên trái của nửa kim tự tháp sát với cạnh bên trái của cửa sổ terminal.

## Cách kiểm tra

Mặc dù `check50` đã có sẵn cho bài toán này, bạn nên tự kiểm tra mã của mình trước đối với mỗi trường hợp sau đây.

- Chạy chương trình của bạn bằng lệnh `python mario.py` và đợi yêu cầu nhập dữ liệu. Nhập `-1` và nhấn enter. Chương trình của bạn nên từ chối giá trị nhập này vì không hợp lệ, bằng cách yêu cầu người dùng nhập lại một số khác.
- Chạy chương trình của bạn bằng lệnh `python mario.py` và đợi yêu cầu nhập dữ liệu. Nhập `0` và nhấn enter. Chương trình của bạn nên từ chối giá trị nhập này vì không hợp lệ, bằng cách yêu cầu người dùng nhập lại một số khác.
- Chạy chương trình của bạn bằng lệnh `python mario.py` và đợi yêu cầu nhập dữ liệu. Nhập `1` và nhấn enter. Chương trình của bạn sẽ tạo ra kết quả như bên dưới. Hãy đảm bảo rằng kim tự tháp được căn lề vào góc dưới bên trái của terminal và không có khoảng trắng thừa ở cuối mỗi dòng.

```
#
```

- Chạy chương trình của bạn bằng lệnh `python mario.py` và đợi yêu cầu nhập dữ liệu. Nhập `2` và nhấn enter. Chương trình của bạn sẽ tạo ra kết quả như bên dưới. Hãy đảm bảo rằng kim tự tháp được căn lề vào góc dưới bên trái của terminal và không có khoảng trắng thừa ở cuối mỗi dòng.

```
 #
##
```

- Chạy chương trình của bạn bằng lệnh `python mario.py` và đợi yêu cầu nhập dữ liệu. Nhập `8` và nhấn enter. Chương trình của bạn sẽ tạo ra kết quả như bên dưới. Hãy đảm bảo rằng kim tự tháp được căn lề vào góc dưới bên trái của terminal và không có khoảng trắng thừa ở cuối mỗi dòng.

```
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

- Chạy chương trình của bạn bằng lệnh `python mario.py` và đợi yêu cầu nhập dữ liệu. Nhập `9` và nhấn enter. Chương trình của bạn nên từ chối giá trị nhập này vì không hợp lệ, bằng cách yêu cầu người dùng nhập lại một số khác. Sau đó, nhập `2` và nhấn enter. Chương trình của bạn sẽ tạo ra kết quả như bên dưới. Hãy đảm bảo rằng kim tự tháp được căn lề vào góc dưới bên trái của terminal và không có khoảng trắng thừa ở cuối mỗi dòng.

```
 #
##
```

- Chạy chương trình của bạn bằng lệnh `python mario.py` và đợi yêu cầu nhập dữ liệu. Nhập `foo` và nhấn enter. Chương trình của bạn nên từ chối giá trị nhập này vì không hợp lệ, bằng cách yêu cầu người dùng nhập lại một số khác.
- Chạy chương trình của bạn bằng lệnh `python mario.py` và đợi yêu cầu nhập dữ liệu. Đừng nhập gì cả và nhấn enter. Chương trình của bạn nên từ chối giá trị nhập này vì không hợp lệ, bằng cách yêu cầu người dùng nhập lại một số khác.

### Độ chính xác

```
check50 cs50/problems/2026/x/sentimental/mario/less
```

### Phong cách

```
style50 mario.py
```

## Cách nộp bài

Trong terminal của bạn, hãy thực thi lệnh dưới đây để nộp bài, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/sentimental/mario/less
```
