---
title: "Xin chào, Lần nữa - CS50x 2026"
pset: 6
draft: "false"
---

## Bài toán cần giải

Trong một tệp có tên là `hello.py` nằm trong thư mục `sentimental-hello`, hãy triển khai một chương trình yêu cầu người dùng nhập tên của họ, sau đó in ra `hello, so-and-so`, trong đó `so-and-so` là tên được cung cấp, chính xác như bạn đã làm trong [Problem Set 1](../../1/). Tuy nhiên, lần này chương trình của bạn phải được viết bằng ngôn ngữ Python!

Gợi ý

- Hãy nhớ rằng bạn có thể nhận một `str` từ người dùng bằng hàm `get_string`, hàm này được khai báo trong thư viện `cs50`.
- Hãy nhớ rằng bạn có thể in một `str` bằng hàm `print`.
- Hãy nhớ rằng bạn có thể tạo các chuỗi định dạng (formatted strings) trong Python bằng cách thêm tiền tố `f` vào trước chuỗi. Ví dụ, `f"{name}"` sẽ thay thế giá trị của biến `name` vào vị trí bạn viết `{name}`.

## Demo

## Cách kiểm tra

Mặc dù `check50` có sẵn cho bài toán này, bạn nên tự kiểm tra mã nguồn của mình trước cho từng trường hợp sau.

- Chạy chương trình với lệnh `python hello.py` và đợi thông báo nhập liệu. Nhập `David` và nhấn Enter. Chương trình của bạn sẽ in ra `hello, David`.
- Chạy chương trình với lệnh `python hello.py` và đợi thông báo nhập liệu. Nhập `Inno` và nhấn Enter. Chương trình của bạn sẽ in ra `hello, Inno`.
- Chạy chương trình với lệnh `python hello.py` và đợi thông báo nhập liệu. Nhập `Kamryn` và nhấn Enter. Chương trình của bạn sẽ in ra `hello, Kamryn`.

### Độ chính xác

```
check50 cs50/problems/2026/x/sentimental/hello
```

### Phong cách

```
style50 hello.py
```

## Cách nộp bài

Trong terminal của bạn, hãy thực hiện lệnh dưới đây để nộp bài làm, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/sentimental/hello
```
