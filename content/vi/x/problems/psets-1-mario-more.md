---
title: "Mario - CS50x 2026"
pset: 1
draft: "false"
---

## Vấn đề cần giải quyết

Gần đầu Thế giới 1-1 trong trò chơi Super Mario Brothers của Nintendo, Mario phải nhảy qua các hình kim tự tháp xếp liền kề nhau bằng các khối gạch, như hình bên dưới.

![ảnh chụp màn hình Mario nhảy qua các kim tự tháp liền kề](pyramids.png)

Trong một tệp có tên `mario.c` nằm trong thư mục có tên `mario-more`, hãy triển khai một chương trình bằng C để tái tạo kim tự tháp đó, sử dụng các dấu thăng (`#`) làm gạch, như dưới đây:

```
   #  #
  ##  ##
 ###  ###
####  ####
```

Và hãy cho phép người dùng quyết định độ cao của kim tự tháp bằng cách trước tiên yêu cầu họ nhập một số nguyên dương (`int`) trong khoảng từ 1 đến 8.

Ví dụ

Dưới đây là cách chương trình có thể hoạt động nếu người dùng nhập `8` khi được yêu cầu:

```bash
$ ./mario
Height: 8
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########

```

Dưới đây là cách chương trình có thể hoạt động nếu người dùng nhập `4` khi được yêu cầu:

```bash
$ ./mario
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

Dưới đây là cách chương trình có thể hoạt động nếu người dùng nhập `2` khi được yêu cầu:

```bash
$ ./mario
Height: 2
 #  #
##  ##
```

Và dưới đây là cách chương trình có thể hoạt động nếu người dùng nhập `1` khi được yêu cầu:

```bash
$ ./mario
Height: 1
#  #
```

Nếu người dùng không nhập một số nguyên dương trong khoảng từ 1 đến 8, chương trình sẽ yêu cầu người dùng nhập lại cho đến khi hợp lệ:

```bash
$ ./mario
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

Lưu ý rằng chiều rộng của "khoảng trống" giữa các kim tự tháp liền kề bằng chiều rộng của hai dấu thăng, bất kể chiều cao của kim tự tháp là bao nhiêu.

### Hướng dẫn

### Cách kiểm thử mã của bạn

Mã của bạn có hoạt động như quy định khi bạn nhập vào:

- `-1` (hoặc các số âm khác)?
- `0`?
- `1` đến `8`?
- `9` hoặc các số dương khác?
- chữ cái hoặc từ?
- không có đầu vào nào cả, khi bạn chỉ nhấn Enter?

Bạn cũng có thể thực thi lệnh bên dưới để đánh giá tính chính xác của mã nguồn bằng `check50`. Nhưng hãy nhớ tự biên dịch và kiểm thử nó nữa nhé!

```
check50 cs50/problems/2026/x/mario/more
```

Thực thi lệnh bên dưới để đánh giá phong cách lập trình (style) của bạn bằng `style50`.

```
style50 mario.c
```

## Cách nộp bài

Trong terminal của bạn, hãy thực thi lệnh bên dưới để nộp bài làm của mình, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/mario/more
```
