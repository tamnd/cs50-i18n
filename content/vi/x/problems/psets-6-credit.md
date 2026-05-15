---
title: "Thẻ tín dụng - CS50x 2026"
pset: 6
draft: "false"
---

## Bài toán cần giải

Trong một tệp có tên là `credit.py` nằm trong thư mục `sentimental-credit`, hãy viết một chương trình yêu cầu người dùng nhập số thẻ tín dụng và sau đó báo cáo (thông qua hàm `print`) xem đó là số thẻ American Express, MasterCard hay Visa hợp lệ, chính xác như bạn đã làm trong [Problem Set 1](../../1/). Lần này chương trình của bạn phải được viết bằng ngôn ngữ Python!

## Demo

## Yêu cầu kỹ thuật

- Để chúng tôi có thể tự động hóa một số bài kiểm tra mã nguồn của bạn, chúng tôi yêu cầu dòng đầu ra cuối cùng của chương trình phải là `AMEX\n` hoặc `MASTERCARD\n` hoặc `VISA\n` hoặc `INVALID\n`, không thừa không thiếu.
- Để đơn giản, bạn có thể giả định rằng đầu vào của người dùng sẽ hoàn toàn là chữ số (tức là không có dấu gạch ngang, như trên thẻ thực tế).
- Tốt nhất nên sử dụng `get_int` hoặc `get_string` từ thư viện của CS50 để nhận đầu vào của người dùng, tùy thuộc vào cách bạn quyết định triển khai bài này.

## Gợi ý

- Có thể sử dụng biểu thức chính quy (regular expressions) để xác thực đầu vào của người dùng. Ví dụ, bạn có thể sử dụng mô-đun [`re`](https://docs.python.org/3/library/re.html) của Python để kiểm tra xem đầu vào của người dùng có thực sự là một chuỗi các chữ số có độ dài chính xác hay không.

## Cách kiểm tra

Mặc dù `check50` có sẵn cho bài toán này, bạn nên tự kiểm tra mã nguồn của mình trước cho từng trường hợp sau.

- Chạy chương trình với lệnh `python credit.py` và đợi thông báo nhập liệu. Nhập `378282246310005` và nhấn Enter. Chương trình của bạn sẽ in ra `AMEX`.
- Chạy chương trình với lệnh `python credit.py` và đợi thông báo nhập liệu. Nhập `371449635398431` và nhấn Enter. Chương trình của bạn sẽ in ra `AMEX`.
- Chạy chương trình với lệnh `python credit.py` và đợi thông báo nhập liệu. Nhập `5555555555554444` và nhấn Enter. Chương trình của bạn sẽ in ra `MASTERCARD`.
- Chạy chương trình với lệnh `python credit.py` và đợi thông báo nhập liệu. Nhập `5105105105105100` và nhấn Enter. Chương trình của bạn sẽ in ra `MASTERCARD`.
- Chạy chương trình với lệnh `python credit.py` và đợi thông báo nhập liệu. Nhập `4111111111111111` và nhấn Enter. Chương trình của bạn sẽ in ra `VISA`.
- Chạy chương trình với lệnh `python credit.py` và đợi thông báo nhập liệu. Nhập `4012888888881881` và nhấn Enter. Chương trình của bạn sẽ in ra `VISA`.
- Chạy chương trình với lệnh `python credit.py` và đợi thông báo nhập liệu. Nhập `1234567890` và nhấn Enter. Chương trình của bạn sẽ in ra `INVALID`.

### Độ chính xác

```
check50 cs50/problems/2026/x/sentimental/credit
```

### Phong cách

```
style50 credit.py
```

## Cách nộp bài

Trong terminal của bạn, hãy thực hiện lệnh dưới đây để nộp bài làm, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/sentimental/credit
```
