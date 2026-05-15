---
title: "Di truyền - CS50x 2026"
pset: 5
draft: false
---

## Bài toán cần giải

Nhóm máu của một người được quyết định bởi hai alen (nghĩa là các dạng khác nhau của một gen). Ba alen có thể có là A, B và O, trong đó mỗi người có hai alen (có thể giống nhau hoặc khác nhau). Mỗi phụ huynh sẽ truyền ngẫu nhiên một trong hai alen nhóm máu của mình cho con cái. Do đó, các tổ hợp nhóm máu có thể có là: OO, OA, OB, AO, AA, AB, BO, BA và BB.

Ví dụ, nếu một phụ huynh có nhóm máu AO và phụ huynh kia có nhóm máu BB, thì các nhóm máu có thể có của con sẽ là AB và OB, tùy thuộc vào việc alen nào được nhận từ mỗi phụ huynh. Tương tự, nếu một phụ huynh có nhóm máu AO và người kia là OB, thì các nhóm máu có thể có của con sẽ là AO, OB, AB và OO.

Trong một tệp có tên là `inheritance.c` nằm trong thư mục mang tên `inheritance`, hãy mô phỏng quá trình di truyền nhóm máu cho từng thành viên trong một gia đình.

## Demo

## Mã nguồn phân phối

Đối với bài toán này, bạn sẽ mở rộng chức năng của mã nguồn do đội ngũ nhân viên của CS50 cung cấp.

Tải mã nguồn phân phối

Đăng nhập vào [cs50.dev](https://cs50.dev/), nhấp vào cửa sổ terminal và thực hiện lệnh `cd` một mình. Bạn sẽ thấy dấu nhắc lệnh của terminal trông giống như dưới đây:

```
$
```

Tiếp theo, hãy thực hiện lệnh

```python
wget https://cdn.cs50.net/2026/x/psets/5/inheritance.zip
```

để tải tệp ZIP có tên `inheritance.zip` vào codespace của bạn.

Sau đó thực hiện

```
unzip inheritance.zip
```

để tạo một thư mục có tên `inheritance`. Bạn không còn cần tệp ZIP nữa, vì vậy bạn có thể thực hiện

```
rm inheritance.zip
```

và trả lời "y" sau đó nhấn Enter tại dấu nhắc để xóa tệp ZIP bạn đã tải xuống.

Bây giờ hãy nhập

```bash
cd inheritance
```

sau đó nhấn Enter để di chuyển vào (tức là mở) thư mục đó. Dấu nhắc lệnh của bạn bây giờ sẽ trông giống như dưới đây.

```
inheritance/ $
```

Thực hiện lệnh `ls` một mình, bạn sẽ thấy một tệp có tên `inheritance.c`.

Nếu bạn gặp bất kỳ rắc rối nào, hãy thực hiện lại các bước tương tự và xem liệu bạn có thể xác định mình đã sai ở đâu không!

## Chi tiết triển khai

Hoàn thành việc triển khai `inheritance.c`, sao cho nó tạo ra một gia đình với quy mô thế hệ được chỉ định và gán các alen nhóm máu cho mỗi thành viên trong gia đình. Thế hệ cũ nhất sẽ được gán các alen một cách ngẫu nhiên.

- Hàm `create_family` nhận một số nguyên (`generations`) làm đầu vào và nên cấp phát (thông qua `malloc`) một `person` cho mỗi thành viên trong gia đình với số thế hệ đó, trả về một con trỏ tới `person` ở thế hệ trẻ nhất.
  
  - Ví dụ, `create_family(3)` sẽ trả về một con trỏ tới một người có hai phụ huynh, trong đó mỗi phụ huynh cũng có hai phụ huynh.
  - Mỗi `person` nên được gán các `alleles`. Thế hệ cũ nhất nên có các alen được chọn ngẫu nhiên (bằng cách gọi hàm `random_allele`), và các thế hệ trẻ hơn nên thừa hưởng một alen (được chọn ngẫu nhiên) từ mỗi phụ huynh.
  - Mỗi `person` nên được gán các `parents`. Thế hệ cũ nhất nên có cả hai `parents` được đặt là `NULL`, và các thế hệ trẻ hơn nên có `parents` là một mảng gồm hai con trỏ, mỗi con trỏ trỏ đến một phụ huynh khác nhau.

## Gợi ý

Hiểu mã nguồn trong `inheritance.c`

Hãy xem qua mã nguồn phân phối trong `inheritance.c`.

Lưu ý định nghĩa của một kiểu dữ liệu có tên là `person`. Mỗi người có một mảng gồm hai `parents`, mỗi phụ huynh là một con trỏ tới một cấu trúc `person` khác. Mỗi người cũng có một mảng gồm hai `alleles`, mỗi alen là một kiểu `char` (có thể là `'A'`, `'B'`, hoặc `'O'`).

```
// Each person has two parents and two alleles
typedef struct person
{
    struct person *parents[2];
    char alleles[2];
}
person;
```

Bây giờ, hãy xem hàm `main`. Hàm bắt đầu bằng cách "seeding" (tức là cung cấp một số đầu vào ban đầu) cho bộ tạo số ngẫu nhiên, chúng ta sẽ sử dụng bộ tạo này sau để tạo các alen ngẫu nhiên.

```
// Seed random number generator
srandom(time(0));
```

Hàm `main` sau đó gọi hàm `create_family` để mô phỏng việc tạo các cấu trúc `person` cho một gia đình gồm 3 thế hệ (tức là một người, cha mẹ họ và ông bà họ).

```sql
// Create a new family with three generations
person *p = create_family(GENERATIONS);
```

Sau đó, chúng ta gọi `print_family` để in ra từng thành viên trong gia đình và nhóm máu của họ.

```
// Print family tree of blood types
print_family(p, 0);
```

Cuối cùng, hàm gọi `free_family` để giải phóng (`free`) bất kỳ bộ nhớ nào đã được cấp phát trước đó bằng `malloc`.

```
// Free memory
free_family(p);
```

Các hàm `create_family` và `free_family` được để lại cho bạn tự viết!

Hoàn thành hàm `create_family`

Hàm `create_family` nên trả về một con trỏ tới một `person` đã thừa hưởng nhóm máu của họ từ số lượng `generations` được đưa vào làm đầu vào.

- Trước hết, hãy lưu ý rằng bài toán này là một cơ hội tốt để áp dụng đệ quy.
  
  - Để xác định nhóm máu của người hiện tại, trước tiên bạn cần xác định nhóm máu của cha mẹ họ.
  - Để xác định nhóm máu của những cha mẹ đó, trước tiên bạn phải xác định nhóm máu của cha mẹ *họ*. Và cứ tiếp tục như vậy cho đến khi bạn đạt đến thế hệ cuối cùng mà bạn muốn mô phỏng.

Để giải quyết bài toán này, bạn sẽ tìm thấy một số TODO trong mã nguồn phân phối.

Đầu tiên, bạn nên cấp phát bộ nhớ cho một người mới. Hãy nhớ rằng bạn có thể sử dụng `malloc` để cấp phát bộ nhớ và `sizeof(person)` để lấy số byte cần cấp phát.

```c
// Allocate memory for new person
person *new_person = malloc(sizeof(person));
```

Tiếp theo, bạn nên kiểm tra xem còn thế hệ nào cần tạo hay không: tức là liệu `generations > 1`.

Nếu `generations > 1`, thì vẫn còn nhiều thế hệ cần được cấp phát. Chúng ta đã tạo ra hai phụ huynh mới, `parent0` và `parent1`, bằng cách gọi đệ quy `create_family`. Hàm `create_family` của bạn sau đó nên đặt các con trỏ phụ huynh của người mới mà bạn đã tạo. Cuối cùng, gán cả hai `alleles` cho người mới bằng cách chọn ngẫu nhiên một alen từ mỗi phụ huynh.

- Hãy nhớ rằng, để truy cập một biến thông qua con trỏ, bạn có thể sử dụng ký hiệu mũi tên. Ví dụ, nếu `p` là một con trỏ tới một người, thì một con trỏ tới phụ huynh đầu tiên của người này có thể được truy cập bằng `p->parents[0]`.
- Bạn có thể thấy hàm `random()` hữu ích cho việc gán các alen một cách ngẫu nhiên. Hàm này trả về một số nguyên nằm giữa `0` và `RAND_MAX`, hoặc `32767`. Cụ thể, để tạo một số giả ngẫu nhiên là `0` hoặc `1`, bạn có thể sử dụng biểu thức `random() % 2`.

```sql
// Create two new parents for current person by recursively calling create_family
person *parent0 = create_family(generations - 1);
person *parent1 = create_family(generations - 1);

// Set parent pointers for current person
new_person->parents[0] = parent0;
new_person->parents[1] = parent1;

// Randomly assign current person's alleles based on the alleles of their parents
new_person->alleles[0] = parent0->alleles[random() % 2];
new_person->alleles[1] = parent1->alleles[random() % 2];
```

Giả sử không còn thế hệ nào để mô phỏng. Tức là, `generations == 1`. Nếu vậy, sẽ không có dữ liệu phụ huynh cho người này. Cả hai phụ huynh của người mới của bạn nên được đặt thành `NULL`, và mỗi `allele` nên được tạo ngẫu nhiên.

```c
// Set parent pointers to NULL
new_person->parents[0] = NULL;
new_person->parents[1] = NULL;

// Randomly assign alleles
new_person->alleles[0] = random_allele();
new_person->alleles[1] = random_allele();
```

Cuối cùng, hàm của bạn nên trả về một con trỏ cho `person` đã được cấp phát.

```
// Return newly created person
return new_person;
```

Hoàn thành hàm `free_family`

Hàm `free_family` nên nhận đầu vào là một con trỏ tới một `person`, giải phóng bộ nhớ cho người đó, và sau đó giải phóng bộ nhớ một cách đệ quy cho tất cả tổ tiên của họ.

- Vì đây là một hàm đệ quy, trước tiên bạn nên xử lý trường hợp cơ sở (base case). Nếu đầu vào của hàm là `NULL`, thì không có gì để giải phóng, vì vậy hàm của bạn có thể trả về ngay lập tức.
- Nếu không, bạn nên giải phóng (`free`) cả hai phụ huynh của người đó một cách đệ quy trước khi giải phóng (`free`) đứa trẻ.

Dưới đây là một gợi ý khá chi tiết về cách thực hiện việc đó!

```c
// Free `p` and all ancestors of `p`.
void free_family(person *p)
{
    // Handle base case
    if (p == NULL)
    {
        return;
    }

    // Free parents recursively
    free_family(p->parents[0]);
    free_family(p->parents[1]);

    // Free child
    free(p);
}
```

### Hướng dẫn chi tiết (Walkthrough)

Bạn không chắc chắn về cách giải quyết?

## Cách kiểm tra

Sau khi chạy `./inheritance`, chương trình của bạn phải tuân thủ các quy tắc được mô tả trong phần bối cảnh. Đứa trẻ phải có hai alen, mỗi alen từ một phụ huynh. Mỗi phụ huynh phải có hai alen, mỗi alen từ một trong những phụ huynh của họ.

Ví dụ, trong ví dụ dưới đây, đứa trẻ ở Thế hệ 0 đã nhận được một alen O từ cả hai phụ huynh ở Thế hệ 1. Phụ huynh thứ nhất nhận được một alen A từ ông/bà thứ nhất và một alen O từ ông/bà thứ hai. Tương tự, phụ huynh thứ hai nhận được một alen O và một alen B từ ông bà của họ.

```bash
$ ./inheritance
Child (Generation 0): blood type OO
    Parent (Generation 1): blood type AO
        Grandparent (Generation 2): blood type OA
        Grandparent (Generation 2): blood type BO
    Parent (Generation 1): blood type OB
        Grandparent (Generation 2): blood type AO
        Grandparent (Generation 2): blood type BO
```

### Độ chính xác

```
check50 cs50/problems/2026/x/inheritance
```

### Phong cách

```
style50 inheritance.c
```

## Cách nộp bài

Trong terminal của bạn, hãy thực hiện lệnh dưới đây để nộp bài làm của bạn, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/inheritance
```
