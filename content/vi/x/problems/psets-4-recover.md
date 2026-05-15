---
title: "Khôi phục - CS50x 2026"
pset: 4
draft: false
---

![Ảnh đã khôi phục](recovered_image.png)

## Vấn đề cần giải quyết

Để chuẩn bị cho bài toán này, chúng tôi đã dành vài ngày qua để chụp ảnh quanh khuôn viên trường, tất cả đều được lưu trong máy ảnh kỹ thuật số dưới định dạng JPEG trên một thẻ nhớ. Thật không may, chúng tôi đã vô tình xóa sạch chúng! May mắn thay, trong thế giới máy tính, “xóa” thường không có nghĩa là thực sự biến mất mà giống như là “bị lãng quên” hơn. Mặc dù máy ảnh khẳng định rằng thẻ nhớ hiện đang trống rỗng, chúng tôi khá chắc chắn rằng điều đó không hoàn toàn đúng. Thực tế, chúng tôi hy vọng (à không, mong đợi!) bạn có thể viết một chương trình để khôi phục những bức ảnh đó cho chúng tôi!

Trong một tệp có tên `recover.c` nằm trong thư mục mang tên `recover`, hãy viết một chương trình để khôi phục các tệp JPEG từ một thẻ nhớ.

## Mã phân phối

Đối với bài toán này, bạn sẽ mở rộng chức năng của mã nguồn được cung cấp bởi đội ngũ CS50.

Tải xuống mã phân phối

Đăng nhập vào [cs50.dev](https://cs50.dev/), nhấp vào cửa sổ terminal của bạn và thực thi lệnh `cd`. Bạn sẽ thấy dấu nhắc (prompt) của cửa sổ terminal trông giống như dưới đây:

```
$
```

Tiếp theo, hãy thực thi

```python
wget https://cdn.cs50.net/2026/x/psets/4/recover.zip
```

để tải xuống tệp ZIP có tên `recover.zip` vào codespace của bạn.

Sau đó thực thi

```
unzip recover.zip
```

để tạo một thư mục có tên `recover`. Bạn không còn cần tệp ZIP nữa, vì vậy bạn có thể thực thi

```
rm recover.zip
```

và trả lời bằng chữ “y” rồi nhấn Enter tại dấu nhắc để xóa tệp ZIP đã tải xuống.

Bây giờ hãy gõ

```bash
cd recover
```

rồi nhấn Enter để di chuyển vào (tức là mở) thư mục đó. Dấu nhắc của bạn bây giờ sẽ trông giống như dưới đây.

```
recover/ $
```

Thực thi lệnh `ls`, bạn sẽ thấy hai tệp: `recover.c` và `card.raw`.

## Bối cảnh

Mặc dù JPEG phức tạp hơn BMP, nhưng JPEG có các “chữ ký” (signatures) - đó là các mẫu byte có thể giúp phân biệt chúng với các định dạng tệp khác. Cụ thể, ba byte đầu tiên của các tệp JPEG là

```
0xff 0xd8 0xff
```

tính từ byte đầu tiên đến byte thứ ba, từ trái qua phải. Trong khi đó, byte thứ tư có thể là `0xe0`, `0xe1`, `0xe2`, `0xe3`, `0xe4`, `0xe5`, `0xe6`, `0xe7`, `0xe8`, `0xe9`, `0xea`, `0xeb`, `0xec`, `0xed`, `0xee`, hoặc `0xef`. Nói cách khác, bốn bit đầu tiên của byte thứ tư là `1110`.

Rất có khả năng nếu bạn tìm thấy mẫu bốn byte này trên một thiết bị lưu trữ ảnh (ví dụ: thẻ nhớ của tôi), chúng sẽ đánh dấu điểm bắt đầu của một tệp JPEG. Thành thật mà nói, bạn có thể bắt gặp các mẫu này trên đĩa chỉ do ngẫu nhiên, vì vậy việc khôi phục dữ liệu không phải là một môn khoa học chính xác tuyệt đối.

May mắn thay, máy ảnh kỹ thuật số có xu hướng lưu trữ ảnh liên tiếp trên thẻ nhớ, theo đó mỗi bức ảnh được lưu ngay sau bức ảnh đã chụp trước đó. Do đó, điểm bắt đầu của một tệp JPEG thường đánh dấu điểm kết thúc của một tệp khác. Tuy nhiên, máy ảnh kỹ thuật số thường khởi tạo thẻ với hệ thống tệp FAT có “kích thước khối” (block size) là 512 byte (B). Điều này có nghĩa là các máy ảnh này chỉ ghi vào thẻ theo từng đơn vị 512 B. Một bức ảnh nặng 1 MB (tức là 1.048.576 B) do đó sẽ chiếm 1048576 ÷ 512 = 2048 “khối” trên thẻ nhớ. Nhưng một bức ảnh nhỏ hơn một byte (tức là 1.048.575 B) cũng chiếm dung lượng tương tự! Không gian lãng phí trên đĩa được gọi là “khoảng trống dư thừa” (slack space). Các điều tra viên pháp y máy tính thường kiểm tra khoảng trống dư thừa này để tìm tàn dư của các dữ liệu khả nghi.

Từ tất cả các chi tiết này, bạn - trong vai trò một điều tra viên - có thể viết một chương trình lặp qua một bản sao của thẻ nhớ, tìm kiếm chữ ký của các tệp JPEG. Mỗi khi tìm thấy một chữ ký, bạn có thể mở một tệp mới để ghi và bắt đầu điền vào tệp đó các byte từ thẻ nhớ, chỉ đóng tệp đó khi bạn bắt gặp một chữ ký khác. Hơn nữa, thay vì đọc từng byte một trên thẻ nhớ, bạn có thể đọc một lúc 512 byte vào một bộ đệm (buffer) để đạt hiệu suất cao hơn. Nhờ hệ thống FAT, bạn có thể tin tưởng rằng các chữ ký JPEG sẽ được “căn chỉnh theo khối” (block-aligned). Nghĩa là, bạn chỉ cần tìm kiếm các chữ ký đó trong bốn byte đầu tiên của một khối.

Tất nhiên, hãy nhận ra rằng các tệp JPEG có thể trải dài trên nhiều khối liên tiếp. Nếu không, sẽ không có tệp JPEG nào lớn hơn 512 B. Nhưng byte cuối cùng của một tệp JPEG có thể không nằm ở đúng điểm cuối của một khối. Hãy nhớ lại khả năng về khoảng trống dư thừa (slack space). Nhưng đừng lo lắng. Vì thẻ nhớ này còn mới khi tôi bắt đầu chụp ảnh, rất có thể nó đã được nhà sản xuất “lấp đầy số 0” (zeroed - tức là chứa toàn số 0), trong trường hợp đó bất kỳ khoảng trống dư thừa nào cũng sẽ được lấp đầy bởi số 0. Sẽ không sao nếu những số 0 dư thừa đó nằm ở cuối tệp JPEG mà bạn khôi phục; chúng vẫn có thể xem được bình thường.

Hiện tại, tôi chỉ có một chiếc thẻ nhớ, nhưng lại có rất nhiều bạn! Vì vậy, tôi đã tạo một “hình ảnh pháp y” (forensic image) của chiếc thẻ, lưu trữ nội dung của nó theo từng byte trong một tệp có tên `card.raw`. Để bạn không lãng phí thời gian lặp qua hàng triệu số 0 không cần thiết, tôi chỉ tạo hình ảnh của vài megabyte đầu tiên của thẻ nhớ. Tuy nhiên, cuối cùng bạn sẽ thấy rằng hình ảnh này chứa 50 tệp JPEG.

## Yêu cầu kỹ thuật

Triển khai một chương trình có tên `recover` để khôi phục các tệp JPEG từ một hình ảnh pháp y.

- Triển khai chương trình của bạn trong một tệp có tên `recover.c` trong thư mục có tên `recover`.
- Chương trình của bạn phải chấp nhận đúng một đối số dòng lệnh, đó là tên của hình ảnh pháp y mà từ đó cần khôi phục các tệp JPEG.
- Nếu chương trình không được thực thi với đúng một đối số dòng lệnh, nó sẽ nhắc nhở người dùng về cách sử dụng đúng, và hàm `main` sẽ trả về `1`.
- Nếu không thể mở hình ảnh pháp y để đọc, chương trình sẽ thông báo cho người dùng và hàm `main` sẽ trả về `1`.
- Mỗi tệp bạn tạo ra phải được đặt tên là `###.jpg`, trong đó `###` là một số thập phân có ba chữ số, bắt đầu từ `000` cho hình ảnh đầu tiên và tăng dần lên.
- Nếu chương trình của bạn sử dụng `malloc`, nó không được để xảy ra rò rỉ bộ nhớ.

## Gợi ý

Viết mã giả (pseudocode) trước khi bắt tay vào viết mã nguồn

Nếu bạn không chắc chắn cách giải quyết vấn đề lớn, hãy chia nhỏ nó thành các vấn đề nhỏ hơn mà bạn có thể giải quyết trước. Ví dụ, bài toán này thực chất chỉ là một vài vấn đề nhỏ:

1. Chấp nhận một đối số dòng lệnh duy nhất: tên của một thẻ nhớ
2. Mở thẻ nhớ
3. Trong khi vẫn còn dữ liệu để đọc trong thẻ nhớ
   
   1. Tạo các tệp JPEG từ dữ liệu

Hãy viết một số mã giả dưới dạng chú thích để nhắc bạn làm điều đó:

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Chấp nhận một đối số dòng lệnh duy nhất

    // Mở thẻ nhớ

    // Trong khi vẫn còn dữ liệu để đọc từ thẻ nhớ

        // Tạo các tệp JPEG từ dữ liệu
}
```

Chuyển đổi mã giả thành mã nguồn

Đầu tiên, hãy xem xét cách chấp nhận một đối số dòng lệnh duy nhất. Nếu người dùng sử dụng chương trình sai cách, bạn nên cho họ biết cách sử dụng đúng của chương trình.

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Chấp nhận một đối số dòng lệnh duy nhất
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Mở thẻ nhớ

    // Trong khi vẫn còn dữ liệu để đọc từ thẻ nhớ

        // Tạo các tệp JPEG từ dữ liệu
}
```

Bây giờ bạn đã kiểm tra cách sử dụng đúng, bạn có thể mở thẻ nhớ. Lưu ý rằng bạn có thể mở `card.raw` bằng mã lập trình với hàm `fopen`, như dưới đây.

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Chấp nhận một đối số dòng lệnh duy nhất
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Mở thẻ nhớ
    FILE *card = fopen(argv[1], "r");

    // Trong khi vẫn còn dữ liệu để đọc từ thẻ nhớ

        // Tạo các tệp JPEG từ dữ liệu
}
```

Tất nhiên, bạn nên kiểm tra để đảm bảo tệp đã được mở đúng cách! Nếu không, hãy thông báo cho người dùng và thoát chương trình: chúng tôi sẽ để phần này cho bạn tự thực hiện.

Tiếp theo, chương trình của bạn nên đọc dữ liệu từ thẻ đã mở cho đến khi không còn dữ liệu để đọc. Trong quá trình đó, chương trình của bạn nên khôi phục từng tệp JPEG từ `card.raw`, lưu mỗi tệp thành một tệp riêng biệt trong thư mục làm việc hiện tại của bạn.

Trước tiên, hãy xem xét cách đọc hết `card.raw`. Hãy nhớ rằng, để đọc dữ liệu từ một tệp, bạn cần lưu trữ tạm thời dữ liệu đó trong một “bộ đệm” (buffer). Và hãy nhớ thêm rằng `card.raw` lưu trữ dữ liệu theo các khối 512 byte. Do đó, bạn có thể sẽ muốn tạo một bộ đệm 512 byte để lưu trữ các khối dữ liệu khi bạn đọc chúng một cách tuần tự. Một cách để làm điều đó là sử dụng kiểu dữ liệu `uint8_t` từ thư viện `stdint.h`, kiểu dữ liệu này lưu trữ chính xác 8 bit (1 byte). Kiểu này được gọi là `uint8_t` vì nó lưu trữ một số nguyên không dấu/dương/không âm chiếm 8 bit không gian (tức là một byte).

```c
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Chấp nhận một đối số dòng lệnh duy nhất
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Mở thẻ nhớ
    FILE *card = fopen(argv[1], "r");

    // Tạo một bộ đệm cho một khối dữ liệu
    uint8_t buffer[512];

    // Trong khi vẫn còn dữ liệu để đọc từ thẻ nhớ

        // Tạo các tệp JPEG từ dữ liệu
}
```

Tuy nhiên, có lẽ *không* phải là ý tưởng tốt nhất khi sử dụng số 512 như một [“con số ma thuật” (magic number)](../../../shorts/magic_numbers/) ở đây. Rất có thể bạn có thể cải thiện thiết kế này hơn nữa!

Bây giờ, hãy xem xét cách đọc dữ liệu từ thẻ nhớ. Theo [trang hướng dẫn (manual page)](https://man.cs50.io/3/fread) của nó, hàm `fread` trả về số lượng byte mà nó đã đọc được, trong trường hợp này nó sẽ trả về `512` hoặc `0`, giả sử rằng `card.raw` chứa một số lượng các khối 512 byte. Để đọc mọi khối từ `card.raw`, sau khi mở nó bằng `fopen`, một vòng lặp như thế này là đủ.

```c
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Chấp nhận một đối số dòng lệnh duy nhất
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Mở thẻ nhớ
    FILE *card = fopen(argv[1], "r");

    // Tạo một bộ đệm cho một khối dữ liệu
    uint8_t buffer[512];

    // Trong khi vẫn còn dữ liệu để đọc từ thẻ nhớ
    while (fread(buffer, 1, 512, card) == 512)
    {
        // Tạo các tệp JPEG từ dữ liệu

    }
}
```

Bằng cách đó, ngay khi `fread` trả về `0` (về cơ bản là `false`), vòng lặp của bạn sẽ kết thúc.

Cuối cùng, việc xác định cách tạo các tệp JPEG bằng mã lập trình khi bạn tiếp tục đọc từ `card.raw` là tùy thuộc vào bạn. Đối với phần này, bạn có thể thấy phần [hướng dẫn (walkthrough)](#walkthrough) bên dưới hữu ích.

Hãy nhớ rằng chương trình của bạn nên đánh số các tệp mà nó xuất ra bằng cách đặt tên cho mỗi tệp là `###.jpg`, trong đó `###` là số thập phân có ba chữ số từ `000` trở lên. Hãy làm quen với hàm [`sprintf`](https://man.cs50.io/3/sprintf) và lưu ý rằng `sprintf` lưu trữ một chuỗi đã được định dạng tại một vị trí trong bộ nhớ. Với định dạng `###.jpg` được quy định cho tên tệp JPEG, bạn nên cấp phát bao nhiêu byte cho chuỗi đó? (Đừng quên ký tự kết thúc chuỗi NUL!)

Để kiểm tra xem các tệp JPEG mà chương trình của bạn tạo ra có chính xác hay không, chỉ cần nhấp đúp và xem thử! Nếu mỗi bức ảnh xuất hiện nguyên vẹn, thao tác của bạn có khả năng đã thành công!

Và tất nhiên, hãy nhớ dùng `fclose` để đóng mọi tệp bạn đã mở bằng `fopen`!

Giữ cho thư mục làm việc của bạn sạch sẽ

Rất có thể các tệp JPEG mà bản thảo đầu tiên của mã nguồn tạo ra sẽ không chính xác. (Nếu bạn mở chúng lên và không thấy gì, chúng có lẽ không đúng!) Hãy thực thi lệnh bên dưới để xóa tất cả các tệp JPEG trong thư mục làm việc hiện tại của bạn.

```
rm *.jpg
```

Nếu bạn không muốn bị yêu cầu xác nhận cho mỗi lần xóa, hãy thực thi lệnh bên dưới thay thế.

```
rm -f *.jpg
```

Chỉ cần cẩn thận với tham số `-f` đó, vì nó “ép buộc” (forces) việc xóa mà không hỏi lại bạn.

## Hướng dẫn chi tiết

## Cách kiểm tra

### Chạy chương trình

```
./recover card.raw
```

### Độ chính xác

```
check50 cs50/problems/2026/x/recover
```

### Phong cách lập trình

```
style50 recover.c
```

## Cách nộp bài

Trong cửa sổ terminal của bạn, hãy thực thi lệnh bên dưới để nộp bài, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/recover
```
