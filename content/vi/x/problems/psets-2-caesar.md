title: "Caesar - CS50x 2026"
pset: 2
draft: "false"
---

![Caesar Cipher](cipher.jpg)

## Bài toán cần giải quyết

Tương truyền, Caesar (vâng, chính là Caesar đó) thường “mã hóa” (nghĩa là che giấu một cách có thể đảo ngược) các thông điệp mật bằng cách dịch chuyển mỗi chữ cái trong đó đi một số vị trí nhất định. Ví dụ, ông có thể viết A thành B, B thành C, C thành D, …, và quay vòng theo bảng chữ cái, Z thành A. Do đó, để nói HELLO với ai đó, Caesar có thể viết là IFMMP. Khi nhận được những thông điệp như vậy từ Caesar, người nhận sẽ phải “giải mã” chúng bằng cách dịch chuyển các chữ cái theo hướng ngược lại với cùng số vị trí đó.

Sự bí mật của “hệ mã hóa” này dựa trên việc chỉ Caesar và người nhận biết được một bí mật, đó là số vị trí mà Caesar đã dịch chuyển các chữ cái của mình (ví dụ: 1). Nó không đặc biệt an toàn theo tiêu chuẩn hiện đại, nhưng, này, nếu bạn có lẽ là người đầu tiên trên thế giới làm điều đó, thì nó khá là an toàn đấy!

Văn bản chưa mã hóa thường được gọi là *văn bản gốc* (plaintext). Văn bản đã mã hóa thường được gọi là *văn bản mã hóa* (ciphertext). Và bí mật được sử dụng được gọi là *khóa* (key).

Để rõ ràng hơn, dưới đây là cách mã hóa `HELLO` với khóa là \\(1\\) để tạo ra `IFMMP`:

| văn bản gốc  | `H`     | `E`     | `L`     | `L`     | `O`     |
|--------------|---------|---------|---------|---------|---------|
| \+ khóa      | \\(1\\) | \\(1\\) | \\(1\\) | \\(1\\) | \\(1\\) |
| = văn bản mã hóa | `I`     | `F`     | `M`     | `M`     | `P`     |

Nói một cách trang trọng hơn, thuật toán của Caesar (tức là mật mã) mã hóa các thông điệp bằng cách “xoay” mỗi chữ cái đi \\(k\\) vị trí. Cụ thể hơn, nếu \\(p\\) là văn bản gốc (tức là một thông điệp chưa mã hóa), \\(p\_i\\) là ký tự thứ \\(i\\) trong \\(p\\), và \\(k\\) là một khóa bí mật (tức là một số nguyên không âm), thì mỗi chữ cái \\(c\_i\\) trong văn bản mã hóa \\(c\\) được tính như sau:

\\\[c\_i = (p\_i + k)\\space\\%\\space26\\]

trong đó \\(\\%\\space26\\) ở đây có nghĩa là “số dư khi chia cho 26.” Công thức này có lẽ làm cho mật mã có vẻ phức tạp hơn thực tế, nhưng nó thực sự chỉ là một cách ngắn gọn để thể hiện thuật toán một cách chính xác. Thật vậy, để phục vụ cho việc thảo luận, hãy coi A (hoặc a) là \\(0\\), B (hoặc b) là \\(1\\), …, H (hoặc h) là \\(7\\), I (hoặc i) là \\(8\\), …, và Z (hoặc z) là \\(25\\). Giả sử Caesar chỉ muốn nói `Hi` với ai đó một cách bí mật bằng cách sử dụng khóa \\(k\\) là 3. Như vậy, văn bản gốc \\(p\\) của ông là `Hi`, trong trường hợp đó, ký tự đầu tiên của văn bản gốc \\(p\_0\\) là `H` (tức là 7), và ký tự thứ hai của văn bản gốc \\(p\_1\\) là `i` (tức là 8). Ký tự đầu tiên của văn bản mã hóa \\(c\_0\\) do đó là `K`, và ký tự thứ hai của văn bản mã hóa \\(c\_1\\) do đó là `L`. Bạn thấy hợp lý chứ?

Trong một tệp có tên là `caesar.c` trong một thư mục có tên là `caesar`, hãy viết một chương trình cho phép bạn mã hóa các thông điệp bằng mật mã Caesar. Tại thời điểm người dùng thực thi chương trình, họ sẽ quyết định, bằng cách cung cấp một tham số dòng lệnh (command-line argument), khóa sẽ là gì cho thông điệp bí mật mà họ sẽ cung cấp khi chạy chương trình. Chúng ta không nhất thiết phải giả định rằng khóa của người dùng sẽ luôn là một con số; tuy nhiên, bạn có thể giả định rằng, nếu nó là một con số, nó sẽ là một số nguyên dương.

## Demo

## Yêu cầu

Thiết kế và triển khai một chương trình, `caesar`, dùng để mã hóa các thông điệp bằng mật mã Caesar.

- Triển khai chương trình của bạn trong một tệp có tên là `caesar.c` trong một thư mục có tên là `caesar`.
- Chương trình của bạn phải chấp nhận một tham số dòng lệnh duy nhất, đó là một số nguyên không âm. Hãy gọi nó là \\(k\\) để tiện thảo luận.
- Nếu chương trình của bạn được thực thi mà không có bất kỳ tham số dòng lệnh nào hoặc có nhiều hơn một tham số dòng lệnh, chương trình của bạn nên in ra một thông báo lỗi tùy chọn (bằng `printf`) và trả về giá trị `1` từ `main` (thường biểu thị một lỗi) ngay lập tức.
- Nếu bất kỳ ký tự nào của tham số dòng lệnh không phải là một chữ số thập phân, chương trình của bạn nên in ra thông báo `Usage: ./caesar key` và trả về giá trị `1` từ `main`.
- Đừng giả định rằng \\(k\\) sẽ nhỏ hơn hoặc bằng 26. Chương trình của bạn nên hoạt động với tất cả các giá trị nguyên không âm của \\(k\\) nhỏ hơn \\(2^{31} - 26\\). Nói cách khác, bạn không cần lo lắng nếu chương trình của bạn bị lỗi nếu người dùng chọn một giá trị cho \\(k\\) quá lớn hoặc gần như quá lớn để vừa với một kiểu `int`. (Nhớ rằng kiểu `int` có thể bị tràn số). Nhưng, ngay cả khi \\(k\\) lớn hơn \\(26\\), các ký tự chữ cái trong đầu vào chương trình của bạn vẫn phải là ký tự chữ cái trong đầu ra. Ví dụ, nếu \\(k\\) là \\(27\\), `A` không được trở thành `\` mặc dù `\` cách `A` 27 vị trí trong bảng mã ASCII, theo [asciitable.com](https://www.asciitable.com/); `A` phải trở thành `B`, vì `B` cách `A` 27 vị trí, miễn là bạn quay vòng từ `Z` về `A`.
- Chương trình của bạn phải in ra `plaintext: ` (với hai khoảng trắng nhưng không có dòng mới) và sau đó nhắc người dùng nhập một chuỗi `string` văn bản gốc (sử dụng `get_string`).
- Chương trình của bạn phải in ra `ciphertext: ` (với một khoảng trắng nhưng không có dòng mới), theo sau là văn bản mã hóa tương ứng của văn bản gốc, với mỗi ký tự chữ cái trong văn bản gốc được “xoay” đi *k* vị trí; các ký tự không phải chữ cái phải được in ra mà không thay đổi.
- Chương trình của bạn phải giữ nguyên kiểu chữ: các chữ cái viết hoa, mặc dù được xoay, vẫn phải là chữ cái viết hoa; các chữ cái viết thường, mặc dù được xoay, vẫn phải là chữ cái viết thường.
- Sau khi in ra văn bản mã hóa, bạn nên in một dòng mới. Chương trình của bạn sau đó sẽ thoát bằng cách trả về `0` từ `main`.

## Lời khuyên

Bắt đầu như thế nào? Hãy tiếp cận bài toán này từng bước một.

### Mã giả

Đầu tiên, hãy thử viết hàm `main` trong tệp `caesar.c` để triển khai chương trình bằng mã giả, ngay cả khi bạn chưa (hoặc chưa!) chắc chắn cách viết nó bằng mã thực tế.

Gợi ý

Có nhiều cách để làm việc này, và đây chỉ là một trong số đó!

```c
int main(int argc, string argv[])
{
    // Đảm bảo chương trình được chạy với chỉ một tham số dòng lệnh

    // Đảm bảo mọi ký tự trong argv[1] đều là chữ số

    // Chuyển đổi argv[1] từ `string` sang `int`

    // Nhắc người dùng nhập văn bản gốc (plaintext)

    // Với mỗi ký tự trong văn bản gốc:

        // Xoay ký tự nếu nó là một chữ cái
}
```

Việc chỉnh sửa mã giả của chính bạn sau khi xem mã giả của chúng tôi là hoàn toàn bình thường, nhưng đừng chỉ sao chép/dán mã giả của chúng tôi vào bài làm của bạn!

### Đếm các tham số dòng lệnh

Dù mã giả của bạn là gì, trước tiên hãy chỉ viết mã C kiểm tra xem chương trình có được chạy với một tham số dòng lệnh duy nhất hay không trước khi thêm các chức năng khác.

Cụ thể, hãy sửa đổi hàm `main` trong `caesar.c` sao cho nếu người dùng không cung cấp tham số dòng lệnh nào, hoặc cung cấp từ hai tham số trở lên, hàm sẽ in ra `"Usage: ./caesar key\n"` và sau đó trả về `1`, kết thúc chương trình một cách hiệu quả. Nếu người dùng cung cấp chính xác một tham số dòng lệnh, chương trình sẽ không in gì và chỉ trả về `0`. Do đó, chương trình sẽ hoạt động như bên dưới.

```bash
$ ./caesar
Usage: ./caesar key
```

```bash
$ ./caesar 1 2 3
Usage: ./caesar key
```

```bash
$ ./caesar 1
```

Gợi ý

- Nhớ rằng bạn có thể in bằng `printf`.
- Nhớ rằng một hàm có thể trả về một giá trị bằng `return`.
- Nhớ rằng `argc` chứa số lượng tham số dòng lệnh được truyền vào chương trình, cộng với chính tên của chương trình đó.

### Kiểm tra khóa

Bây giờ chương trình của bạn (hy vọng là!) đang chấp nhận đầu vào như quy định, đã đến lúc thực hiện bước tiếp theo.

Thêm vào `caesar.c`, phía dưới hàm `main`, một hàm có tên là, ví dụ, `only_digits` nhận một `string` làm tham số và trả về `true` nếu `string` đó chỉ chứa các chữ số từ `0` đến `9`, ngược lại nó trả về `false`. Đảm bảo cũng thêm nguyên mẫu (prototype) của hàm phía trên `main` mặc định.

Gợi ý

- Có khả năng bạn sẽ muốn một nguyên mẫu như sau:
  
  ```
  bool only_digits(string s);
  ```
  
  Và đừng quên thêm `#include <cs50.h>` ở đầu tệp của bạn, để trình biên dịch nhận dạng được kiểu `string` (và `bool`).
- Nhớ rằng `string` chỉ là một mảng các ký tự `char`.
- Nhớ rằng `strlen`, được khai báo trong `string.h`, dùng để tính độ dài của một chuỗi `string`.
- Bạn có thể thấy `isdigit`, được khai báo trong `ctype.h`, rất hữu ích, theo [manual.cs50.io](https://manual.cs50.io/). Nhưng lưu ý rằng nó chỉ kiểm tra một ký tự `char` tại một thời điểm!

Sau đó, hãy sửa đổi `main` sao cho nó gọi hàm `only_digits` cho `argv[1]`. Nếu hàm đó trả về `false`, thì `main` nên in ra `"Usage: ./caesar key\n"` và trả về `1`. Ngược lại, `main` chỉ cần trả về `0`. Chương trình sẽ hoạt động như bên dưới:

```bash
$ ./caesar 42
```

```bash
$ ./caesar banana
Usage: ./caesar key
```

### Sử dụng khóa

Bây giờ hãy sửa đổi `main` sao cho nó chuyển đổi `argv[1]` thành một số nguyên `int`. Bạn có thể thấy `atoi`, được khai báo trong `stdlib.h`, rất hữu ích, theo [manual.cs50.io](https://manual.cs50.io/). Sau đó, sử dụng `get_string` để nhắc người dùng nhập văn bản gốc với thông báo `"plaintext: "`.

Tiếp theo, hãy triển khai một hàm có tên là, ví dụ, `rotate`, nhận một ký tự `char` và một số nguyên `int` làm đầu vào, và xoay ký tự đó đi bấy nhiêu vị trí nếu nó là một chữ cái (tức là, alphabetical), quay vòng từ `Z` về `A` (và từ `z` về `a`) nếu cần thiết. Nếu ký tự đó không phải là chữ cái, hàm sẽ trả về chính ký tự đó mà không thay đổi.

Gợi ý

- Có khả năng bạn sẽ muốn một nguyên mẫu như sau:
  
  ```
  char rotate(char c, int n);
  ```
  
  Một lệnh gọi hàm như
  
  ```
  rotate('A', 1)
  ```
  
  hoặc thậm chí
  
  ```
  rotate('A', 27)
  ```
  
  do đó sẽ trả về `'B'`. Và một lệnh gọi hàm như
  
  ```
  rotate('!', 13)
  ```
  
  sẽ trả về `'!'`.
- Nhớ rằng bạn có thể “ép kiểu” (cast) một cách rõ ràng một ký tự `char` sang kiểu `int` bằng `(int)`, và một số nguyên `int` sang kiểu `char` bằng `(char)`. Hoặc bạn có thể làm điều đó một cách ngầm định bằng cách coi kiểu này như kiểu kia.
- Có khả năng bạn sẽ muốn trừ giá trị ASCII của `'A'` cho bất kỳ chữ cái viết hoa nào, để coi `'A'` là `0`, `'B'` là `1`, v.v., trong khi thực hiện các phép tính số học. Sau đó cộng nó ngược trở lại khi hoàn tất.
- Có khả năng bạn sẽ muốn trừ giá trị ASCII của `'a'` cho bất kỳ chữ cái viết thường nào, để coi `'a'` là `0`, `'b'` là `1`, v.v., trong khi thực hiện các phép tính số học. Sau đó cộng nó ngược trở lại khi hoàn tất.
- Bạn có thể thấy một số hàm khác được khai báo trong `ctype.h` rất hữu ích, theo [manual.cs50.io](https://manual.cs50.io/).
- Có khả năng bạn sẽ thấy `%` hữu ích khi “quay vòng” về mặt số học từ một giá trị như `25` về `0`.

Sau đó, hãy sửa đổi `main` sao cho nó in ra `"ciphertext: "` và sau đó lặp qua từng ký tự `char` trong văn bản gốc của người dùng, gọi hàm `rotate` cho mỗi ký tự và in ra giá trị trả về của nó.

Gợi ý

- Nhớ rằng `printf` có thể in một ký tự `char` bằng cách sử dụng `%c`.
- Nếu bạn không thấy bất kỳ đầu ra nào khi gọi `printf`, có khả năng là do bạn đang in các ký tự nằm ngoài phạm vi ASCII hợp lệ từ 0 đến 127. Hãy thử in các ký tự tạm thời dưới dạng số (sử dụng `%i` thay vì `%c`) để xem bạn đang in những giá trị nào!

## Hướng dẫn

## Cách kiểm tra

### Độ chính xác

```
check50 cs50/problems/2026/x/caesar
```

Cách sử dụng `debug50`

Bạn muốn chạy `debug50`? Bạn có thể làm như sau, sau khi biên dịch mã của bạn thành công bằng `make`,

```
debug50 ./caesar KEY
```

trong đó `KEY` là khóa bạn đưa vào làm tham số dòng lệnh cho chương trình của mình. Lưu ý rằng việc chạy

```
debug50 ./caesar
```

sẽ (lý tưởng nhất!) khiến chương trình của bạn kết thúc bằng cách yêu cầu người dùng nhập khóa.

### Phong cách

```
style50 caesar.c
```

## Cách nộp bài

Trong terminal của bạn, hãy thực thi lệnh bên dưới để nộp bài làm của bạn, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/caesar
```
