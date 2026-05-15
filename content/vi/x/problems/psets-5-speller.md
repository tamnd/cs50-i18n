title: "Speller - CS50x 2026"
pset: 5
draft: false
---

## Bài toán cần giải quyết

Trong bài toán này, bạn sẽ triển khai một chương trình kiểm tra chính tả của một tệp tin, tương tự như ví dụ dưới đây, bằng cách sử dụng bảng băm (hash table).

## Demo

## Mã nguồn phân phối

Đối với bài toán này, bạn sẽ mở rộng chức năng của mã nguồn được cung cấp bởi đội ngũ CS50.

Tải mã nguồn phân phối

Đăng nhập vào [cs50.dev](https://cs50.dev/), nhấp vào cửa sổ terminal và thực hiện lệnh `cd` một mình. Bạn sẽ thấy dấu nhắc lệnh của terminal trông giống như dưới đây:

```
$
```

Tiếp theo thực hiện lệnh

```python
wget https://cdn.cs50.net/2026/x/psets/5/speller.zip
```

để tải tệp ZIP có tên `speller.zip` vào codespace của bạn.

Sau đó thực hiện lệnh

```
unzip speller.zip
```

để tạo một thư mục có tên `speller`. Bạn không còn cần tệp ZIP nữa, vì vậy bạn có thể thực hiện lệnh

```
rm speller.zip
```

và phản hồi bằng “y” rồi nhấn Enter tại dấu nhắc để xóa tệp ZIP bạn đã tải xuống.

Bây giờ gõ

```bash
cd speller
```

sau đó nhấn Enter để di chuyển vào (tức là mở) thư mục đó. Dấu nhắc lệnh của bạn bây giờ sẽ giống như dưới đây.

```
speller/ $
```

Thực hiện lệnh `ls` một mình, và bạn sẽ thấy một vài tệp và thư mục:

```
dictionaries/  dictionary.c  dictionary.h  keys/  Makefile  speller.c  speller50  texts/
```

Nếu bạn gặp bất kỳ rắc rối nào, hãy thực hiện lại các bước tương tự và xem liệu bạn có thể xác định mình đã sai ở đâu không!

## Bối cảnh

**Với nhiều tệp tin trong chương trình này, việc đọc toàn bộ phần này trước khi bắt đầu là rất quan trọng. Khi đó, bạn sẽ biết mình cần làm gì và làm như thế nào!**

Về lý thuyết, với đầu vào có kích thước *n*, một thuật toán có thời gian chạy là *n* là “tương đương tiệm cận”, xét theo *O*, với một thuật toán có thời gian chạy là *2n*. Thật vậy, khi mô tả thời gian chạy của một thuật toán, chúng ta thường tập trung vào số hạng chủ đạo (tức là có ảnh hưởng lớn nhất) (tức là *n* trong trường hợp này, vì *n* có thể lớn hơn nhiều so với 2). Tuy nhiên, trong thế giới thực, thực tế là *2n* tạo cảm giác chậm gấp đôi so với *n*.

Thử thách dành cho bạn là triển khai một chương trình kiểm tra chính tả nhanh nhất có thể! Tuy nhiên, khi nói đến “nhanh nhất”, chúng ta đang nói về thời gian thực tế (“wall-clock”), chứ không phải thời gian tiệm cận.

Trong `speller.c`, chúng tôi đã tập hợp một chương trình được thiết kế để kiểm tra chính tả một tệp tin sau khi tải một từ điển các từ từ đĩa vào bộ nhớ. Trong khi đó, từ điển đó được triển khai trong một tệp có tên là `dictionary.c`. (Nó có thể chỉ được triển khai trong `speller.c`, nhưng khi các chương trình trở nên phức tạp hơn, việc chia chúng thành nhiều tệp thường rất tiện lợi.) Trong khi đó, các nguyên mẫu cho các hàm trong đó không được định nghĩa trong chính `dictionary.c` mà thay vào đó là trong `dictionary.h`. Bằng cách đó, cả `speller.c` và `dictionary.c` đều có thể `#include` tệp này. Thật không may, chúng tôi chưa kịp triển khai phần tải (load). Hoặc phần kiểm tra (check). Cả hai (và một chút nữa) chúng tôi dành lại cho bạn! Nhưng trước tiên, hãy cùng tham quan một vòng.

### Tìm hiểu mã nguồn

#### `dictionary.h`

Mở `dictionary.h`, bạn sẽ thấy một số cú pháp mới, bao gồm một vài dòng đề cập đến `DICTIONARY_H`. Không cần lo lắng về những dòng đó, nhưng nếu tò mò, những dòng đó chỉ đảm bảo rằng, mặc dù `dictionary.c` và `speller.c` (mà bạn sẽ thấy sau đây) đều `#include` tệp này, `clang` sẽ chỉ biên dịch nó một lần.

Tiếp theo, hãy chú ý cách chúng tôi `#include` một tệp có tên là `stdbool.h`. Đó là tệp mà `bool` được định nghĩa. Trước đây bạn không cần nó vì Thư viện CS50 đã `#include` tệp đó cho bạn.

Cũng lưu ý việc chúng tôi sử dụng `#define`, một “chỉ thị tiền xử lý” định nghĩa một “hằng số” gọi là `LENGTH` có giá trị là `45`. Đó là một hằng số theo nghĩa là bạn không thể (vô tình) thay đổi nó trong mã nguồn của chính mình. Trên thực tế, `clang` sẽ thay thế bất kỳ lần đề cập nào đến `LENGTH` trong mã nguồn của bạn bằng chính xác giá trị `45`. Nói cách khác, nó không phải là một biến, chỉ là một thủ thuật tìm và thay thế.

Cuối cùng, hãy lưu ý các nguyên mẫu cho năm hàm: `check`, `hash`, `load`, `size`, và `unload`. Hãy để ý cách ba trong số đó nhận một con trỏ làm đối số, theo ký hiệu `*`:

```js
bool check(const char *word);
unsigned int hash(const char *word);
bool load(const char *dictionary);
```

Nhớ lại rằng `char *` là những gì chúng ta thường gọi là `string`. Vì vậy, ba nguyên mẫu đó về cơ bản chỉ là:

```js
bool check(const string word);
unsigned int hash(const string word);
bool load(const string dictionary);
```

Và `const`, trong khi đó, chỉ nói rằng những chuỗi đó, khi được truyền vào dưới dạng đối số, phải được giữ nguyên; bạn sẽ không thể thay đổi chúng, dù vô tình hay cố ý!

#### `dictionary.c`

Bây giờ hãy mở `dictionary.c`. Lưu ý cách chúng tôi đã định nghĩa một `struct` gọi là `node` ở đầu tệp để đại diện cho một nút trong bảng băm. Và chúng tôi đã khai báo một mảng con trỏ toàn cục, `table`, mảng này sẽ (sớm) đại diện cho bảng băm mà bạn sẽ sử dụng để theo dõi các từ trong từ điển. Mảng chứa `N` con trỏ nút, và chúng tôi đã đặt `N` bằng `26` cho đến hiện tại, để phù hợp với hàm `hash` mặc định như được mô tả bên dưới. Bạn có thể sẽ muốn tăng giá trị này tùy thuộc vào việc triển khai hàm `hash` của riêng bạn.

Tiếp theo, hãy lưu ý rằng chúng tôi đã triển khai `load`, `check`, `size`, và `unload`, nhưng chỉ ở mức tối thiểu, vừa đủ để mã nguồn có thể biên dịch. Cũng lưu ý rằng chúng tôi đã triển khai `hash` với một thuật toán mẫu dựa trên chữ cái đầu tiên của từ. Công việc của bạn, cuối cùng, là triển khai lại các hàm đó một cách thông minh nhất có thể để trình kiểm tra chính tả này hoạt động đúng như quảng cáo. Và phải nhanh!

#### `speller.c`

Được rồi, tiếp theo hãy mở `speller.c` và dành thời gian xem qua mã nguồn và các bình luận trong đó. Bạn sẽ không cần thay đổi bất cứ điều gì trong tệp này và bạn không cần hiểu toàn bộ nội dung của nó, nhưng hãy cố gắng nắm bắt chức năng của nó. Lưu ý cách thức, thông qua một hàm gọi là `getrusage`, chúng tôi sẽ “benchmarking” (tức là đo thời gian thực thi) các phần triển khai của bạn cho `check`, `load`, `size`, và `unload`. Cũng lưu ý cách chúng tôi truyền cho hàm `check`, từng từ một, nội dung của một số tệp cần kiểm tra chính tả. Cuối cùng, chúng tôi báo cáo từng lỗi chính tả trong tệp đó cùng với một loạt các số liệu thống kê.

Tiện đây, hãy lưu ý rằng chúng tôi đã định nghĩa cách sử dụng của `speller` là

```python
Usage: speller [dictionary] text
```

trong đó `dictionary` được giả định là một tệp chứa danh sách các từ viết thường, mỗi từ trên một dòng và `text` là tệp cần kiểm tra chính tả. Như các dấu ngoặc vuông gợi ý, việc cung cấp `dictionary` là tùy chọn; nếu đối số này bị bỏ qua, `speller` sẽ sử dụng `dictionaries/large` theo mặc định. Nói cách khác, chạy

```
./speller text
```

sẽ tương đương với việc chạy

```
./speller dictionaries/large text
```

trong đó `text` là tệp bạn muốn kiểm tra chính tả. Chỉ cần nói rằng, cách trước dễ gõ hơn! (Tất nhiên, `speller` sẽ không thể tải bất kỳ từ điển nào cho đến khi bạn triển khai `load` trong `dictionary.c`! Cho đến lúc đó, bạn sẽ thấy thông báo `Could not load`.)

Bên trong từ điển mặc định, xin lưu ý, có 143.091 từ, tất cả đều phải được tải vào bộ nhớ! Trên thực tế, hãy liếc qua tệp đó để hiểu cấu trúc và kích thước của nó. Lưu ý rằng mọi từ trong tệp đó đều xuất hiện ở dạng chữ thường (thậm chí, để đơn giản, cả danh từ riêng và từ viết tắt). Từ trên xuống dưới, tệp được sắp xếp theo thứ tự từ điển, chỉ có một từ trên mỗi dòng (mỗi dòng kết thúc bằng `\n`). Không có từ nào dài hơn 45 ký tự và không có từ nào xuất hiện nhiều hơn một lần. Trong quá trình phát triển, bạn có thể thấy hữu ích khi cung cấp cho `speller` một `dictionary` của riêng bạn chứa ít từ hơn nhiều, để tránh việc phải vất vả gỡ lỗi một cấu trúc khổng lồ trong bộ nhớ. Trong `dictionaries/small` là một từ điển như vậy. Để sử dụng nó, hãy thực hiện lệnh

```
./speller dictionaries/small text
```

trong đó `text` là tệp bạn muốn kiểm tra chính tả. Đừng tiếp tục cho đến khi bạn chắc chắn rằng mình hiểu cách thức hoạt động của chính `speller`!

Rất có thể bạn chưa dành đủ thời gian để xem qua `speller.c`. Hãy quay lại một bước và đọc lại nó một lần nữa!

#### `texts/`

Để bạn có thể kiểm tra phần triển khai `speller` của mình, chúng tôi cũng đã cung cấp cho bạn một loạt các văn bản, trong số đó có kịch bản phim *La La Land*, văn bản của Đạo luật Chăm sóc Sức khỏe Hợp túi tiền (Affordable Care Act), ba triệu byte từ Tolstoy, một số đoạn trích từ *The Federalist Papers* và Shakespeare, v.v. Để bạn biết những gì cần mong đợi, hãy mở và đọc lướt từng tệp đó, tất cả đều nằm trong thư mục có tên là `texts` bên trong thư mục `pset5` của bạn.

Bây giờ, như bạn đã biết từ việc đọc kỹ `speller.c`, đầu ra của `speller`, nếu được thực hiện với, chẳng hạn,

```
./speller texts/lalaland.txt
```

cuối cùng sẽ giống như dưới đây.

Dưới đây là một số đầu ra bạn sẽ thấy. Để cung cấp thông tin, chúng tôi đã trích dẫn một số ví dụ về “lỗi chính tả”. Và để không làm mất đi sự thú vị, chúng tôi đã tạm thời bỏ qua các số liệu thống kê của riêng mình.

```
MISSPELLED WORDS

[...]
AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
[...]
Shangri
[...]
fianc
[...]
Sebastian's
[...]

WORDS MISSPELLED:
WORDS IN DICTIONARY:
WORDS IN TEXT:
TIME IN load:
TIME IN check:
TIME IN size:
TIME IN unload:
TIME IN TOTAL:
```

`TIME IN load` đại diện cho số giây mà `speller` dành để thực hiện phần triển khai `load` của bạn. `TIME IN check` đại diện cho số giây mà `speller` dành, tổng cộng, để thực hiện phần triển khai `check` của bạn. `TIME IN size` đại diện cho số giây mà `speller` dành để thực hiện phần triển khai `size` của bạn. `TIME IN unload` đại diện cho số giây mà `speller` dành để thực hiện phần triển khai `unload` của bạn. `TIME IN TOTAL` là tổng của bốn phép đo đó.

**Lưu ý rằng những thời gian này có thể thay đổi đôi chút giữa các lần thực hiện `speller`, tùy thuộc vào những gì khác mà codespace của bạn đang thực hiện, ngay cả khi bạn không thay đổi mã nguồn của mình.**

Nhân tiện, để cho rõ ràng, bằng cách nói “sai chính tả”, chúng tôi đơn giản có nghĩa là một từ nào đó không có trong `dictionary` được cung cấp.

#### `Makefile`

Và cuối cùng, hãy nhớ rằng `make` tự động hóa việc biên dịch mã nguồn của bạn để bạn không phải thực thi `clang` theo cách thủ công cùng với một loạt các tham số. Tuy nhiên, khi các chương trình của bạn phát triển về kích thước, `make` sẽ không thể suy luận từ ngữ cảnh cách biên dịch mã nguồn của bạn nữa; bạn sẽ cần bắt đầu nói cho `make` biết cách biên dịch chương trình của mình, đặc biệt là khi chúng liên quan đến nhiều tệp nguồn (tức là `.c`), như trong trường hợp của bài toán này. Và vì vậy, chúng ta sẽ sử dụng một `Makefile`, một tệp cấu hình cho `make` biết chính xác những gì cần làm. Mở `Makefile`, bạn sẽ thấy bốn dòng:

1. Dòng đầu tiên yêu cầu `make` thực hiện các dòng tiếp theo bất cứ khi nào bạn thực hiện `make speller` (hoặc chỉ `make`).
2. Dòng thứ hai yêu cầu `make` cách biên dịch `speller.c` thành mã máy (tức là `speller.o`).
3. Dòng thứ ba yêu cầu `make` cách biên dịch `dictionary.c` thành mã máy (tức là `dictionary.o`).
4. Dòng thứ tư yêu cầu `make` liên kết `speller.o` và `dictionary.o` trong một tệp có tên là `speller`.

**Hãy chắc chắn biên dịch `speller` bằng cách thực hiện lệnh `make speller` (hoặc chỉ `make`). Thực hiện `make dictionary` sẽ không hoạt động!**

## Yêu cầu kỹ thuật

Được rồi, thử thách bây giờ dành cho bạn là triển khai, theo thứ tự, `load`, `hash`, `size`, `check`, và `unload` hiệu quả nhất có thể bằng cách sử dụng bảng băm sao cho `TIME IN load`, `TIME IN check`, `TIME IN size`, và `TIME IN unload` đều được giảm thiểu. Chắc chắn là không rõ ràng ngay cả ý nghĩa của việc được giảm thiểu là gì, vì các điểm chuẩn này chắc chắn sẽ thay đổi khi bạn cung cấp cho `speller` các giá trị khác nhau cho `dictionary` và cho `text`. Nhưng đó chính là thử thách, nếu không muốn nói là niềm vui, của bài toán này. Bài toán này là cơ hội để bạn thiết kế. Mặc dù chúng tôi khuyến khích bạn giảm thiểu không gian, nhưng kẻ thù cuối cùng của bạn là thời gian. Nhưng trước khi bạn bắt đầu, đây là một số yêu cầu từ chúng tôi.

- Bạn không được thay đổi `speller.c` hoặc `Makefile`.
- Bạn có thể thay đổi `dictionary.c` (và thực tế là phải thay đổi để hoàn thành phần triển khai `load`, `hash`, `size`, `check`, và `unload`), nhưng bạn không được thay đổi các khai báo (tức là các nguyên mẫu) của `load`, `hash`, `size`, `check`, hoặc `unload`. Tuy nhiên, bạn có thể thêm các hàm mới và các biến (cục bộ hoặc toàn cục) vào `dictionary.c`.
- Bạn có thể thay đổi giá trị của `N` trong `dictionary.c`, để bảng băm của bạn có thể có nhiều ngăn (bucket) hơn.
- Bạn có thể thay đổi `dictionary.h`, nhưng bạn không được thay đổi các khai báo của `load`, `hash`, `size`, `check`, hoặc `unload`.
- Phần triển khai `check` của bạn phải không phân biệt chữ hoa chữ thường. Nói cách khác, nếu `foo` có trong từ điển, thì `check` sẽ trả về true với bất kỳ kiểu viết hoa nào của nó; không từ nào trong số `foo`, `foO`, `fOo`, `fOO`, `fOO`, `Foo`, `FoO`, `FOo`, và `FOO` bị coi là sai chính tả.
- Ngoài vấn đề viết hoa, phần triển khai `check` của bạn chỉ nên trả về `true` cho các từ thực sự có trong `dictionary`. Hãy cẩn thận với việc mã hóa cứng các từ thông dụng (ví dụ: `the`), kẻo chúng tôi truyền cho phần triển khai của bạn một `dictionary` không có những từ đó. Hơn nữa, các dạng sở hữu cách duy nhất được phép là những từ thực sự có trong `dictionary`. Nói cách khác, ngay cả khi `foo` có trong `dictionary`, `check` vẫn nên trả về `false` nếu nhận được `foo's` mà `foo's` không có trong `dictionary`.
- Bạn có thể giả định rằng bất kỳ `dictionary` nào được truyền cho chương trình của bạn sẽ được cấu trúc chính xác như của chúng tôi, được sắp xếp theo thứ tự bảng chữ cái từ trên xuống dưới với mỗi từ trên một dòng, mỗi dòng kết thúc bằng `\n`. Bạn cũng có thể giả định rằng `dictionary` sẽ chứa ít nhất một từ, không từ nào dài hơn `LENGTH` ký tự (một hằng số được định nghĩa trong `dictionary.h`), không từ nào xuất hiện nhiều hơn một lần, mỗi từ sẽ chỉ chứa các ký tự chữ cái viết thường và có thể có dấu nháy đơn, và không từ nào bắt đầu bằng dấu nháy đơn.
- Bạn có thể giả định rằng `check` sẽ chỉ được truyền các từ chứa các ký tự chữ cái (viết hoa hoặc viết thường) và có thể có dấu nháy đơn.
- Trình kiểm tra chính tả của bạn chỉ có thể nhận `text` và tùy chọn là `dictionary` làm đầu vào. Mặc dù bạn có thể có ý định (đặc biệt là nếu bạn nằm trong số những người cảm thấy thoải mái hơn) “tiền xử lý” từ điển mặc định của chúng tôi để lấy ra một “hàm băm lý tưởng” cho nó, bạn không được lưu đầu ra của bất kỳ quá trình tiền xử lý nào như vậy vào đĩa để tải lại vào bộ nhớ trong các lần chạy tiếp theo của trình kiểm tra chính tả nhằm giành lợi thế.
- Trình kiểm tra chính tả của bạn không được để rò rỉ bất kỳ bộ nhớ nào. Hãy chắc chắn kiểm tra rò rỉ bằng `valgrind`.
- **Hàm băm bạn viết cuối cùng phải là của riêng bạn, không phải là hàm bạn tìm kiếm trên mạng.**

Được rồi, sẵn sàng chưa?

- Triển khai `load`.
- Triển khai `hash`.
- Triển khai `size`.
- Triển khai `check`.
- Triển khai `unload`.

## Gợi ý

Triển khai `load`

Hoàn thành hàm `load`. `load` nên tải từ điển vào bộ nhớ (cụ thể là vào một bảng băm!). `load` nên trả về `true` nếu thành công và `false` nếu ngược lại.

Hãy xem xét rằng bài toán này chỉ được cấu thành từ các bài toán nhỏ hơn:

1. Mở tệp từ điển
2. Đọc từng từ trong tệp
   
   1. Thêm từng từ vào bảng băm
3. Đóng tệp từ điển

Viết một số mã giả để nhắc nhở bản thân thực hiện chính xác điều đó:

```js
bool load(const char *dictionary)
{
    // Mở tệp từ điển

    // Đọc từng từ trong tệp

        // Thêm từng từ vào bảng băm

    // Đóng tệp từ điển
}
```

Trước tiên hãy xem xét cách mở tệp từ điển. [`fopen`](https://manual.cs50.io/3/fopen) là một lựa chọn tự nhiên. Bạn có thể sử dụng chế độ `r`, vì bạn chỉ cần *đọc* các từ từ tệp từ điển (không phải *viết* hoặc *thêm* chúng).

```js
bool load(const char *dictionary)
{
    // Mở tệp từ điển
    FILE *source = fopen(dictionary, "r");

    // Đọc từng từ trong tệp

        // Thêm từng từ vào bảng băm

    // Đóng tệp từ điển
}
```

Trước khi tiếp tục, bạn nên viết mã để kiểm tra xem tệp có được mở chính xác hay không. Điều đó tùy thuộc vào bạn! Tốt nhất là đảm bảo bạn đóng mọi tệp bạn mở, vì vậy bây giờ là thời điểm tốt để viết mã đóng tệp từ điển:

```js
bool load(const char *dictionary)
{
    // Mở tệp từ điển
    FILE *source = fopen(dictionary, "r");

    // Đọc từng từ trong tệp

        // Thêm từng từ vào bảng băm

    // Đóng tệp từ điển
    fclose(source);
}
```

Điều còn lại là đọc từng từ trong tệp và thêm từng từ vào bảng băm. Trả về `true` khi toàn bộ hoạt động thành công và `false` nếu nó thất bại. Hãy cân nhắc theo dõi video hướng dẫn của bài toán này và tiếp tục chia các bài toán phụ thành các bài toán nhỏ hơn nữa. Ví dụ: thêm từng từ vào bảng băm có thể chỉ là vấn đề triển khai một vài bước nhỏ hơn nữa:

1. Tạo không gian cho một nút bảng băm mới
2. Sao chép từ vào nút mới
3. Băm từ để lấy giá trị băm của nó
4. Chèn nút mới vào bảng băm (sử dụng chỉ số được chỉ định bởi giá trị băm của nó)

Tất nhiên, có nhiều cách để tiếp cận bài toán này, mỗi cách đều có sự đánh đổi về thiết kế riêng. Vì lý do đó, phần mã còn lại là tùy thuộc vào bạn!

Triển khai `hash`

Hoàn thành hàm `hash`. `hash` nên nhận một chuỗi, `word`, làm đầu vào và trả về một số nguyên dương (“unsigned int”).

Hàm băm được cung cấp cho bạn trả về một `int` trong khoảng từ 0 đến 25, bao gồm cả hai đầu, dựa trên ký tự đầu tiên của `word`. Tuy nhiên, có nhiều cách để triển khai một hàm băm ngoài việc sử dụng ký tự đầu tiên (hoặc các *ký tự* đầu tiên) của một từ. Hãy xem xét một hàm băm sử dụng tổng các giá trị ASCII hoặc độ dài của một từ. Một hàm băm tốt sẽ giảm thiểu “xung đột” (collision) và có sự phân bổ (phần lớn là!) đồng đều giữa các “ngăn” (bucket) của bảng băm.

Triển khai `size`

Hoàn thành hàm `size`. `size` nên trả về số lượng từ đã tải trong từ điển. Hãy xem xét hai cách tiếp cận cho bài toán này:

- Đếm từng từ khi bạn tải nó vào từ điển. Trả về số lượng đó khi `size` được gọi.
- Mỗi khi `size` được gọi, lặp lại qua các từ trong bảng băm để đếm chúng. Trả về số lượng đó.

Cách nào có vẻ hiệu quả nhất đối với bạn? Cho dù bạn chọn cách nào, chúng tôi sẽ để phần mã đó cho bạn tự quyết định.

Triển khai `check`

Hoàn thành hàm `check`. `check` nên trả về `true` nếu một từ nằm trong từ điển, ngược lại là `false`.

Hãy xem xét rằng bài toán này cũng được cấu thành từ các bài toán nhỏ hơn. Nếu bạn đã triển khai một bảng băm, việc tìm một từ chỉ mất một vài bước:

1. Băm từ để lấy giá trị băm của nó
2. Tìm kiếm bảng băm tại vị trí được chỉ định bởi giá trị băm của từ
   
   1. Trả về `true` nếu tìm thấy từ
3. Trả về `false` nếu không tìm thấy từ

Để so sánh hai chuỗi mà không phân biệt chữ hoa chữ thường, bạn có thể thấy [`strcasecmp`](https://man.cs50.io/3/strcasecmp) (được khai báo trong `strings.h`) hữu ích! Bạn cũng có thể muốn đảm bảo rằng hàm băm của mình không phân biệt chữ hoa chữ thường, sao cho `foo` và `FOO` có cùng một giá trị băm.

Triển khai `unload`

Hoàn thành hàm `unload`. Hãy chắc chắn `free` trong `unload` bất kỳ bộ nhớ nào mà bạn đã cấp phát trong `load`!

Nhớ lại rằng `valgrind` là người bạn tốt nhất mới của bạn. Biết rằng `valgrind` theo dõi các rò rỉ trong khi chương trình của bạn thực sự đang chạy, vì vậy hãy chắc chắn cung cấp các đối số dòng lệnh nếu bạn muốn `valgrind` phân tích `speller` trong khi bạn sử dụng một `dictionary` và/hoặc văn bản cụ thể, như dưới đây. Tuy nhiên, tốt nhất nên sử dụng một văn bản nhỏ, nếu không `valgrind` có thể mất khá nhiều thời gian để chạy.

```
valgrind ./speller texts/cat.txt
```

Nếu bạn chạy `valgrind` mà không chỉ định một văn bản (`text`) cho `speller`, phần triển khai `load` và `unload` của bạn sẽ không thực sự được gọi (và do đó không được phân tích).

Nếu không chắc chắn cách giải thích đầu ra của `valgrind`, chỉ cần yêu cầu `help50` trợ giúp:

```
help50 valgrind ./speller texts/cat.txt
```

## Video hướng dẫn

**Lưu ý rằng có 6 video trong danh sách phát này. [Mở trên YouTube](https://www.youtube.com/playlist?list=PLhQjrBD2T382T4b6jjwX_qbU23E_Unwcz).**

## Cách kiểm tra

Làm thế nào để kiểm tra xem chương trình của bạn có đưa ra các từ sai chính tả đúng hay không? Vâng, bạn có thể tham khảo các “đáp án” (answer keys) nằm trong thư mục `keys` bên trong thư mục `speller` của bạn. Chẳng hạn, bên trong `keys/lalaland.txt` là tất cả các từ mà chương trình của bạn *nên* coi là sai chính tả.

Do đó, bạn có thể chạy chương trình của mình trên một văn bản nào đó trong một cửa sổ, như dưới đây.

```
./speller texts/lalaland.txt
```

Và sau đó bạn có thể chạy giải pháp của đội ngũ giảng viên trên cùng một văn bản đó trong một cửa sổ khác, như dưới đây.

```
./speller50 texts/lalaland.txt
```

Và sau đó bạn có thể so sánh các cửa sổ bằng mắt cạnh nhau. Tuy nhiên, việc đó có thể nhanh chóng trở nên tẻ nhạt. Vì vậy, thay vào đó, bạn có thể muốn “chuyển hướng” (redirect) đầu ra chương trình của mình vào một tệp, như dưới đây.

```
./speller texts/lalaland.txt > student.txt
./speller50 texts/lalaland.txt > staff.txt
```

Sau đó, bạn có thể so sánh cả hai tệp cạnh nhau trong cùng một cửa sổ bằng một chương trình như `diff`, như dưới đây.

```
diff -y student.txt staff.txt
```

Ngoài ra, để tiết kiệm thời gian, bạn chỉ cần so sánh đầu ra của chương trình của mình (giả sử bạn đã chuyển hướng nó vào, ví dụ, `student.txt`) với một trong các đáp án mà không cần chạy giải pháp của giảng viên, như dưới đây.

```
diff -y student.txt keys/lalaland.txt
```

Nếu đầu ra chương trình của bạn khớp với đầu ra của giảng viên, `diff` sẽ xuất ra hai cột giống hệt nhau ngoại trừ, có lẽ, thời gian chạy ở dưới cùng. Tuy nhiên, nếu các cột khác nhau, bạn sẽ thấy dấu `>` hoặc `|` ở nơi chúng khác nhau. Ví dụ, nếu bạn thấy

```
MISSPELLED WORDS                                                MISSPELLED WORDS

TECHNO                                                          TECHNO
L                                                               L
                                                              > Thelonious
Prius                                                           Prius
                                                              > MIA
L                                                               L
```

điều đó có nghĩa là chương trình của bạn (có đầu ra nằm ở bên trái) không nghĩ rằng `Thelonious` hoặc `MIA` bị sai chính tả, mặc dù đầu ra của giảng viên (ở bên phải) thì có, như được ngụ ý bởi sự vắng mặt của, chẳng hạn, `Thelonious` ở cột bên trái và sự hiện diện của `Thelonious` ở cột bên phải.

Cuối cùng, hãy chắc chắn kiểm tra với cả từ điển mặc định lớn và nhỏ. Hãy cẩn thận đừng giả định rằng nếu giải pháp của bạn chạy thành công với từ điển lớn thì nó cũng sẽ chạy thành công với từ điển nhỏ. Đây là cách thử từ điển nhỏ:

```
./speller dictionaries/small texts/cat.txt 
```

### Độ chính xác

```
check50 cs50/problems/2026/x/speller
```

### Phong cách

```
style50 dictionary.c
```

## Giải pháp của đội ngũ giảng viên

Làm thế nào để đánh giá mã nguồn của bạn nhanh (và chính xác) đến mức nào? Vâng, như mọi khi, hãy thoải mái thử nghiệm với giải pháp của đội ngũ giảng viên, như dưới đây, và so sánh các con số của nó với của bạn.

```
./speller50 texts/lalaland.txt
```

## Cách nộp bài

Trong terminal của bạn, hãy thực hiện lệnh dưới đây để nộp bài làm của mình, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/speller
```
