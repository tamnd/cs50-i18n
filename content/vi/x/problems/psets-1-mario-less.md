title: "Mario - CS50x 2026"
pset: 1
draft: "false"
---

## Bài toán cần giải quyết

Gần cuối Thế giới 1-1 trong trò chơi [Super Mario Bros.](https://en.wikipedia.org/wiki/Super_Mario_Bros.) của Nintendo, Mario phải leo lên một kim tự tháp gạch căn lề phải, như hình dưới đây.

![ảnh chụp màn hình Mario nhảy lên một kim tự tháp căn lề phải](pyramid.png)

Trong một tệp có tên `mario.c` nằm trong thư mục `mario-less`, hãy triển khai một chương trình bằng ngôn ngữ C để tái tạo kim tự tháp đó, sử dụng các dấu thăng (`#`) làm gạch, như ví dụ dưới đây:

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

Nhưng hãy yêu cầu người dùng nhập một số nguyên `int` đại diện cho chiều cao thực tế của kim tự tháp, để chương trình cũng có thể xuất ra các kim tự tháp thấp hơn như hình dưới đây:

```
  #
 ##
###
```

Yêu cầu người dùng nhập lại, lặp đi lặp lại nếu cần, nếu giá trị họ nhập không lớn hơn 0 hoặc hoàn toàn không phải là một số nguyên `int`.

Gợi ý

- Hãy nhớ rằng bạn có thể lấy một số nguyên `int` từ người dùng bằng hàm `get_int`, vốn được khai báo trong thư viện `cs50.h`.
- Hãy nhớ rằng bạn có thể in một chuỗi `string` bằng hàm `printf`, vốn được khai báo trong thư viện `stdio.h`.

## Minh họa

## Lời khuyên

Viết mã nguồn mà bạn biết chắc chắn sẽ biên dịch được

Mặc dù chương trình này sẽ không thực hiện công việc gì, nhưng ít nhất nó phải biên dịch được bằng lệnh `make`!

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{

}
```

Viết mã giả (pseudocode) trước khi viết thêm mã nguồn

Nếu chưa chắc chắn về cách giải quyết chính bài toán, hãy chia nhỏ nó thành các vấn đề nhỏ hơn mà bạn có thể giải quyết trước. Chẳng hạn, bài toán này thực chất gồm hai vấn đề:

1. Yêu cầu người dùng nhập chiều cao của kim tự tháp
2. In ra một kim tự tháp có chiều cao đó

Vì vậy, hãy viết một số mã giả dưới dạng chú thích để nhắc nhở bạn thực hiện chính xác điều đó:

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Yêu cầu người dùng nhập chiều cao của kim tự tháp

    // In ra một kim tự tháp có chiều cao đó
}
```

Chuyển mã giả thành mã nguồn

Đầu tiên, hãy cân nhắc cách bạn có thể yêu cầu người dùng nhập chiều cao của kim tự tháp. Hãy nhớ rằng vòng lặp `do while` sẽ hữu ích khi bạn muốn thực hiện điều gì đó ít nhất một lần, và có thể lặp đi lặp lại, như trong ví dụ dưới đây:

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Yêu cầu người dùng nhập chiều cao của kim tự tháp
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // In ra một kim tự tháp có chiều cao đó
}
```

Thứ hai, hãy cân nhắc cách bạn có thể in một kim tự tháp có chiều cao đó, từ trên xuống dưới. Lưu ý rằng hàng đầu tiên nên có một viên gạch, hàng thứ hai nên có hai viên gạch, và cứ tiếp tục như vậy. Rất có thể bạn sẽ cần một vòng lặp, như ví dụ dưới đây, ngay cả khi chưa chắc chắn (ngay lúc này!) nên đặt gì vào trong vòng lặp đó. Vì vậy, hãy thêm một số mã giả dưới dạng chú thích vào lúc này:

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Yêu cầu người dùng nhập chiều cao của kim tự tháp
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // In ra một kim tự tháp có chiều cao đó
    for (int i = 0; i < n; i++)
    {
        // In hàng gạch
    }
}
```

Làm thế nào để in hàng gạch đó? Chà, chẳng phải sẽ rất tốt nếu có một hàm tên là `print_row` có thể thực hiện việc đó sao? Hãy giả sử rằng hàm đó tồn tại:

```c
#include <cs50.h>
#include <stdio.h>

void print_row(int bricks);

int main(void)
{
    // Yêu cầu người dùng nhập chiều cao của kim tự tháp
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // In ra một kim tự tháp có chiều cao đó
    for (int i = 0; i < n; i++)
    {
        // In hàng gạch
    }
}

void print_row(int bricks)
{
    // In hàng gạch
}
```

Sau đó, chúng ta có thể gọi hàm đó từ hàm `main`, như dưới đây:

```c
#include <cs50.h>
#include <stdio.h>

void print_row(int bricks);

int main(void)
{
    // Yêu cầu người dùng nhập chiều cao của kim tự tháp
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // In ra một kim tự tháp có chiều cao đó
    for (int i = 0; i < n; i++)
    {
        // In hàng gạch
        print_row(i + 1);
    }
}

void print_row(int bricks)
{
    // In hàng gạch
}
```

Tuy nhiên, tại sao lại là `i + 1`?

Bây giờ hãy cùng triển khai hàm `print_row`:

```c
#include <cs50.h>
#include <stdio.h>

void print_row(int bricks);

int main(void)
{
    // Yêu cầu người dùng nhập chiều cao của kim tự tháp
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // In ra một kim tự tháp có chiều cao đó
    for (int i = 0; i < n; i++)
    {
        // In hàng gạch
        print_row(i + 1);
    }
}

void print_row(int bricks)
{
    for (int i = 0; i < bricks; i++)
    {
        printf("#");
    }
    printf("\n");
}
```

Tuy nhiên, tại sao lại có `\n` ở cuối?

Thật không may, mã nguồn này in ra một kim tự tháp căn lề trái, nhưng bạn cần một kim tự tháp căn lề phải! Có lẽ chúng ta nên in một số khoảng trắng trước một số viên gạch để đẩy chúng sang bên phải? Hãy thay đổi hàm `print_row` như sau để nó có thể in cả hai:

```c
#include <cs50.h>
#include <stdio.h>

void print_row(int spaces, int bricks);

int main(void)
{
    // Yêu cầu người dùng nhập chiều cao của kim tự tháp
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // In ra một kim tự tháp có chiều cao đó
    for (int i = 0; i < n; i++)
    {
        // In hàng gạch
    }
}

void print_row(int spaces, int bricks)
{
    // In các khoảng trắng

    // In các viên gạch
}
```

Một số mã giả hiện vẫn còn trong cả hàm `main` và hàm `print_row`, phần đó chúng tôi dành lại cho bạn!

Và hãy cân nhắc xem liệu bạn có thể tách một phần mã nguồn trong hàm `main` thành một hàm `get_height` riêng hay không, hàm này cũng sẽ trả về số nguyên `int` mà bạn cần!

## Video hướng dẫn

Lưu ý rằng video hướng dẫn này quy định chương trình của bạn nên yêu cầu người dùng nhập chiều cao của kim tự tháp và yêu cầu nhập *lại* nếu người dùng nhập giá trị nhỏ hơn 1 hoặc lớn hơn 8. Tuy nhiên, bản đặc tả yêu cầu (specification) chỉ yêu cầu bạn hỏi lại người dùng nếu họ nhập giá trị nhỏ hơn 1.

## Cách kiểm thử

Mã nguồn của bạn có hoạt động đúng như quy định khi bạn nhập:

- `-1` hoặc các số âm khác?
- `0`?
- `1` hoặc các số dương khác?
- các chữ cái hoặc từ ngữ?
- không nhập gì cả, khi bạn chỉ nhấn Enter?

### Độ chính xác

```
check50 cs50/problems/2026/x/mario/less
```

### Phong cách lập trình

```
style50 mario.c
```

## Cách nộp bài

Trong terminal của bạn, hãy thực thi lệnh dưới đây để nộp bài, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/mario/less
```
