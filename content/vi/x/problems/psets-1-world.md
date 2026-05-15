---
title: "Xin chào, Thế giới - CS50x 2026"
pset: 1
draft: "false"
---

## Bài toán cần giải

Nhờ Giáo sư [Brian Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan) (người đã dạy CS50 khi David theo học!), "hello, world" đã được triển khai bằng hàng trăm ngôn ngữ khác nhau. Hãy thêm phiên bản của bạn vào danh sách đó nhé!

Trong một tệp có tên là `hello.c`, nằm trong thư mục có tên là `world`, hãy triển khai một chương trình bằng ngôn ngữ C để in ra `hello, world\n`, và chỉ vậy thôi!

Gợi ý

Đây chính là mã nguồn thực tế mà bạn nên viết! (Một gợi ý khá "hời" đúng không?) Tuy nhiên, tốt nhất là bạn nên tự tay gõ lại thay vì sao chép/dán, để bắt đầu rèn luyện "trí nhớ cơ bắp" cho việc viết mã.

```c
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

## Demo

Dưới đây là bản demo về những gì sẽ xảy ra khi bạn biên dịch và thực thi chương trình của mình.

## Cách bắt đầu

Thực hiện lệnh `cd` một mình trong cửa sổ terminal của bạn. Bạn sẽ thấy dấu nhắc lệnh của terminal trông giống như dưới đây:

```
$
```

Tiếp theo, thực hiện lệnh

```bash
mkdir world
```

để tạo một thư mục có tên là `world` trong codespace của bạn.

Sau đó thực hiện lệnh

```bash
cd world
```

để chuyển thư mục vào thư mục đó. Bây giờ bạn sẽ thấy dấu nhắc terminal là `world/ $`. Lúc này bạn có thể thực hiện lệnh

```
code hello.c
```

để tạo một tệp có tên là `hello.c` để viết mã.

## Cách kiểm tra

Hãy nhớ rằng bạn có thể biên dịch `hello.c` bằng lệnh:

```
make hello
```

Nếu bạn không thấy thông báo lỗi, nghĩa là chương trình đã được biên dịch thành công! Bạn có thể xác nhận lại bằng lệnh

```bash
ls
```

Lệnh này sẽ liệt kê không chỉ `hello.c` (là mã nguồn) mà còn cả `hello` (là mã máy).

Nếu bạn thấy thông báo lỗi, hãy cố gắng sửa mã của mình và thử biên dịch lại. Tuy nhiên, nếu bạn không hiểu thông báo lỗi đó, hãy thử thực hiện lệnh

```
help50 make hello
```

để nhận lời khuyên.

Sau khi mã của bạn được biên dịch thành công, bạn có thể thực thi chương trình bằng lệnh:

```
./hello
```

### Độ chính xác

Thực hiện lệnh dưới đây để đánh giá độ chính xác của mã nguồn bằng `check50`, một chương trình dòng lệnh sẽ hiển thị các khuôn mặt cười khi mã của bạn vượt qua các bài kiểm tra tự động của CS50 và các khuôn mặt buồn khi không vượt qua!

```
check50 cs50/problems/2026/x/world
```

### Phong cách

Thực hiện lệnh dưới đây để đánh giá phong cách mã nguồn của bạn bằng `style50`, một chương trình dòng lệnh sẽ hiển thị các phần thêm vào (màu xanh lá cây) và các phần xóa đi (màu đỏ) mà bạn nên thực hiện để cải thiện phong cách chương trình. Nếu bạn gặp khó khăn khi nhìn các màu sắc đó, `style50` cũng hỗ trợ các [chế độ khác](https://cs50.readthedocs.io/style50/)!

```
style50 hello.c
```

## Cách nộp bài

Không cần nộp bài này! Đây chỉ là một bài tập thực hành thôi!
