title: "Âm lượng - CS50x 2026"
pset: 4
draft: "false"
---

![WAV file waveform](wav_file.png)

## Vấn đề cần giải quyết

[Tệp WAV](https://docs.fileformat.com/audio/wav/) là một định dạng tệp phổ biến để biểu diễn âm thanh. Tệp WAV lưu trữ âm thanh dưới dạng một chuỗi các "mẫu" (samples): các con số biểu thị giá trị của một tín hiệu âm thanh tại một thời điểm cụ thể. Tệp WAV bắt đầu bằng một "phần tiêu đề" (header) dài 44 byte chứa thông tin về chính tệp đó, bao gồm kích thước tệp, số lượng mẫu trên mỗi giây và kích thước của mỗi mẫu. Sau phần tiêu đề, tệp WAV chứa một chuỗi các mẫu, mỗi mẫu là một số nguyên 2 byte (16-bit) duy nhất biểu thị tín hiệu âm thanh tại một thời điểm cụ thể.

Việc thay đổi tỉ lệ giá trị của mỗi mẫu theo một hệ số nhất định sẽ có tác dụng thay đổi âm lượng của âm thanh. Ví dụ, nhân mỗi giá trị mẫu với 2.0 sẽ làm tăng gấp đôi âm lượng của âm thanh gốc. Trong khi đó, nhân mỗi mẫu với 0.5 sẽ làm giảm âm lượng xuống còn một nửa.

Trong một tệp có tên là `volume.c` nằm trong thư mục có tên là `volume`, hãy viết một chương trình để thay đổi âm lượng của một tệp âm thanh.

## Demo

## Mã nguồn phân phối

Đối với bài toán này, bạn sẽ mở rộng chức năng của mã nguồn do đội ngũ CS50 cung cấp.

Tải mã nguồn phân phối

Đăng nhập vào [cs50.dev](https://cs50.dev/), nhấp vào cửa sổ terminal và thực hiện lệnh `cd`. Bạn sẽ thấy lời nhắc của cửa sổ terminal giống như dưới đây:

```
$
```

Tiếp theo, thực hiện lệnh

```python
wget https://cdn.cs50.net/2026/x/psets/4/volume.zip
```

để tải một tệp ZIP có tên là `volume.zip` vào codespace của bạn.

Sau đó thực hiện

```
unzip volume.zip
```

để tạo một thư mục có tên là `volume`. Bạn không còn cần tệp ZIP nữa, vì vậy bạn có thể thực hiện

```
rm volume.zip
```

và phản hồi bằng "y" rồi nhấn Enter tại lời nhắc để xóa tệp ZIP bạn đã tải xuống.

Bây giờ hãy nhập

```bash
cd volume
```

rồi nhấn Enter để di chuyển vào (tức là mở) thư mục đó. Lời nhắc của bạn bây giờ sẽ giống như dưới đây.

```
volume/ $
```

Nếu mọi việc thành công, bạn nên thực hiện

```bash
ls
```

và thấy một tệp có tên là `volume.c`. Thực hiện `code volume.c` sẽ mở tệp nơi bạn sẽ nhập mã của mình cho bài tập này. Nếu không, hãy xem lại các bước của bạn và xem liệu bạn có thể xác định mình đã sai ở đâu không!

## Chi tiết triển khai

Hoàn thành việc triển khai `volume.c`, sao cho nó thay đổi âm lượng của một tệp âm thanh theo một hệ số nhất định.

- Chương trình nên chấp nhận ba đối số dòng lệnh. Đối số thứ nhất là `input`, đại diện cho tên của tệp âm thanh gốc. Đối số thứ hai là `output`, đại diện cho tên của tệp âm thanh mới sẽ được tạo ra. Đối số thứ ba là `factor`, là lượng mà âm lượng của tệp âm thanh gốc sẽ được thay đổi tỉ lệ.
  
  - Ví dụ, nếu `factor` là `2.0`, thì chương trình của bạn nên tăng gấp đôi âm lượng của tệp âm thanh trong `input` và lưu tệp âm thanh mới được tạo vào `output`.
- Chương trình của bạn trước tiên nên đọc phần tiêu đề từ tệp đầu vào và ghi phần tiêu đề đó vào tệp đầu ra.
- Sau đó, chương trình của bạn nên đọc phần còn lại của dữ liệu từ tệp WAV, mỗi lần một mẫu 16-bit (2-byte). Chương trình của bạn nên nhân mỗi mẫu với `factor` và ghi mẫu mới vào tệp đầu ra.
  
  - Bạn có thể giả định rằng tệp WAV sẽ sử dụng các giá trị có dấu 16-bit làm mẫu. Trong thực tế, các tệp WAV có thể có số bit trên mỗi mẫu khác nhau, nhưng chúng ta sẽ giả định các mẫu 16-bit cho bài toán này.
- Chương trình của bạn, nếu có sử dụng `malloc`, không được để xảy ra rò rỉ bộ nhớ.

## Gợi ý

Hiểu mã trong `volume.c`

Trước tiên, hãy lưu ý rằng `volume.c` đã được thiết lập để nhận ba đối số dòng lệnh: `input`, `output`, và `factor`.

- `main` nhận cả một số nguyên `argc` và một mảng các `char *` (các chuỗi!), `argv`.
- Nếu `argc`, số lượng đối số tại dòng lệnh bao gồm cả chính chương trình, không bằng 4, chương trình sẽ in ra cách sử dụng đúng và thoát với mã trạng thái 1.

```c
int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // ...
}
```

Tiếp theo, `volume.c` sử dụng [`fopen`](https://manual.cs50.io/3/fopen) để mở hai tệp được cung cấp làm đối số dòng lệnh.

- Tốt nhất là nên kiểm tra xem kết quả của việc gọi `fopen` có là `NULL` hay không. Nếu có, tệp đó đã không được tìm thấy hoặc không thể mở được.

```c
// Open files and determine scaling factor
FILE *input = fopen(argv[1], "r");
if (input == NULL)
{
    printf("Could not open file.\n");
    return 1;
}

FILE *output = fopen(argv[2], "w");
if (output == NULL)
{
    printf("Could not open file.\n");
    return 1;
}
```

Sau đó, các tệp này được đóng bằng `fclose`. Bất cứ khi nào bạn gọi `fopen`, sau đó bạn nên gọi `fclose`!

```
// Close files
fclose(input);
fclose(output);
```

Tuy nhiên, trước khi đóng các tệp, hãy lưu ý rằng chúng ta có một vài mục TODO.

```python
// TODO: Copy header from input file to output file

// TODO: Read samples from input file and write updated data to output file
```

Rất có thể bạn sẽ cần biết hệ số để thay đổi tỉ lệ âm lượng, đó là lý do tại sao `volume.c` đã chuyển đổi đối số dòng lệnh thứ ba thành một số thực `float` cho bạn!

```
float factor = atof(argv[3]);
```

Sao chép tiêu đề WAV từ tệp đầu vào sang tệp đầu ra

TODO đầu tiên của bạn là sao chép tiêu đề tệp WAV từ `input` và ghi nó vào `output`. Tuy nhiên, trước tiên, bạn sẽ cần tìm hiểu về một vài kiểu dữ liệu đặc biệt.

Cho đến nay, chúng ta đã thấy một số kiểu dữ liệu khác nhau trong C, bao gồm `int`, `bool`, `char`, `double`, `float`, và `long`. Tuy nhiên, bên trong một tệp tiêu đề có tên là `stdint.h` là các khai báo của một số kiểu dữ liệu *khác* cho phép chúng ta xác định rất chính xác kích thước (tính bằng bit) và dấu (có dấu hoặc không dấu) của một số nguyên. Có hai kiểu dữ liệu cụ thể sẽ hữu ích cho chúng ta khi làm việc với các tệp WAV:

- `uint8_t` là một kiểu lưu trữ một số nguyên không dấu (tức là không âm) 8-bit (do đó có số `8`!). Chúng ta có thể coi mỗi byte trong phần tiêu đề của tệp WAV là một giá trị `uint8_t`.
- `int16_t` là một kiểu lưu trữ một số nguyên có dấu (tức là dương hoặc âm) 16-bit. Chúng ta có thể coi mỗi mẫu âm thanh trong tệp WAV là một giá trị `int16_t`.

Bạn có thể sẽ muốn tạo một mảng các byte để lưu trữ dữ liệu từ phần tiêu đề tệp WAV mà bạn sẽ đọc từ tệp đầu vào. Sử dụng kiểu `uint8_t` để đại diện cho một byte, bạn có thể tạo một mảng gồm `n` byte cho phần tiêu đề của mình với cú pháp như

```
uint8_t header[n];
```

thay thế `n` bằng số lượng byte. Sau đó, bạn có thể sử dụng `header` làm đối số cho [`fread`](https://manual.cs50.io/3/fread) hoặc [`fwrite`](https://manual.cs50.io/3/fwrite) để đọc vào hoặc ghi từ phần tiêu đề.

Hãy nhớ rằng phần tiêu đề của tệp WAV luôn dài chính xác 44 byte. Lưu ý rằng `volume.c` đã xác định sẵn cho bạn một biến có tên là `HEADER_SIZE`, bằng với số byte trong phần tiêu đề.

Dưới đây là một gợi ý khá lớn, nhưng đây là cách bạn có thể hoàn thành TODO này!

```sql
// Copy header from input file to output file
uint8_t header[HEADER_SIZE];
fread(header, HEADER_SIZE, 1, input);
fwrite(header, HEADER_SIZE, 1, output);
```

Ghi dữ liệu đã cập nhật vào tệp đầu ra

TODO tiếp theo của bạn là đọc các mẫu từ `input`, cập nhật các mẫu đó và ghi các mẫu đã cập nhật vào `output`. Khi đọc tệp, người ta thường tạo một "bộ đệm" (buffer) để lưu trữ tạm thời dữ liệu. Tại đó, bạn có thể sửa đổi dữ liệu và — khi nó đã sẵn sàng — ghi dữ liệu của bộ đệm vào một tệp mới.

Hãy nhớ rằng chúng ta có thể sử dụng kiểu `int16_t` để đại diện cho một mẫu của tệp WAV. Để lưu trữ một mẫu âm thanh, bạn có thể tạo một biến bộ đệm với cú pháp như:

```sql
// Create a buffer for a single sample
int16_t buffer;
```

Sau khi đã có bộ đệm cho các mẫu, giờ đây bạn có thể đọc dữ liệu vào đó, mỗi lần một mẫu. Hãy thử sử dụng `fread` cho nhiệm vụ này! Bạn có thể sử dụng `&buffer`, địa chỉ của `buffer`, làm đối số cho `fread` hoặc `fwrite` để đọc vào hoặc ghi từ bộ đệm. (Hãy nhớ rằng toán tử `&` được sử dụng để lấy địa chỉ của biến.)

```sql
// Create a buffer for a single sample
int16_t buffer;

// Read single sample into buffer
fread(&buffer, sizeof(int16_t), 1, input);
```

Bây giờ, để tăng (hoặc giảm) âm lượng của một mẫu, bạn chỉ cần nhân nó với một hệ số nào đó.

```sql
// Create a buffer for a single sample
int16_t buffer;

// Read single sample into buffer
fread(&buffer, sizeof(int16_t), 1, input);

// Update volume of sample
buffer *= factor;
```

Và cuối cùng, bạn có thể ghi mẫu đã cập nhật đó vào `output`:

```sql
// Create a buffer for a single sample
int16_t buffer;

// Read single sample from input into buffer
fread(&buffer, sizeof(int16_t), 1, input);

// Update volume of sample
buffer *= factor;

// Write updated sample to new file
fwrite(&buffer, sizeof(int16_t), 1, output);
```

Chỉ có một vấn đề: bạn sẽ cần *tiếp tục* đọc một mẫu vào bộ đệm của mình, cập nhật âm lượng của nó và ghi mẫu đã cập nhật vào tệp đầu ra chừng nào vẫn còn mẫu để đọc.

- May mắn thay, theo tài liệu hướng dẫn, `fread` sẽ trả về số lượng đơn vị dữ liệu được đọc thành công. Bạn có thể thấy điều này hữu ích để kiểm tra khi nào bạn đã đọc đến cuối tệp!
- Hãy nhớ rằng không có lý do gì bạn không thể gọi `fread` bên trong điều kiện của một vòng lặp `while`. Ví dụ, bạn có thể thực hiện một lệnh gọi `fread` như sau:
  
  ```
  while (fread(...))
  {
  
  }
  ```

Đây là một gợi ý khá rõ ràng, nhưng hãy xem bên dưới để biết cách giải quyết bài toán này một cách hiệu quả:

```sql
// Create a buffer for a single sample
int16_t buffer;

// Read single sample from input into buffer while there are samples left to read
while (fread(&buffer, sizeof(int16_t), 1, input) != 0)
{
    // Update volume of sample
    buffer *= factor;

    // Write updated sample to new file
    fwrite(&buffer, sizeof(int16_t), 1, output);
}
```

Bởi vì phiên bản C bạn đang sử dụng coi các giá trị khác không là `true` và các giá trị bằng không là `false`, bạn có thể đơn giản hóa cú pháp trên thành như sau:

```sql
// Create a buffer for a single sample
int16_t buffer;

// Read single sample from input into buffer while there are samples left to read
while (fread(&buffer, sizeof(int16_t), 1, input))
{
    // Update volume of sample
    buffer *= factor;

    // Write updated sample to new file
    fwrite(&buffer, sizeof(int16_t), 1, output);
}
```

## Hướng dẫn giải chi tiết

Bạn không chắc chắn về cách giải quyết?

## Cách kiểm tra

Chương trình của bạn nên hoạt động theo các ví dụ bên dưới.

```bash
$ ./volume input.wav output.wav 2.0
```

Khi bạn nghe `output.wav` (bằng cách giữ phím Control và nhấp vào `output.wav` trong trình duyệt tệp, chọn **Download**, sau đó mở tệp trong trình phát âm thanh trên máy tính của bạn), nó sẽ to gấp đôi so với `input.wav`!

```bash
$ ./volume input.wav output.wav 0.5
```

Khi bạn nghe `output.wav`, nó sẽ có âm lượng chỉ bằng một nửa so với `input.wav`!

### Độ chính xác

```
check50 cs50/problems/2026/x/volume
```

### Phong cách lập trình

```
style50 volume.c
```

## Cách nộp bài

Trong terminal của bạn, hãy thực hiện lệnh dưới đây để nộp bài làm của bạn, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/volume
```
