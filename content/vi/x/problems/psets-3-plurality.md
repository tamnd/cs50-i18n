---
title: "Plurality - CS50x 2026"
pset: 3
draft: false
---

## Bài toán cần giải quyết

Các cuộc bầu cử có đủ mọi hình thức và quy mô khác nhau. Tại Vương quốc Anh, [Thủ tướng](https://www.parliament.uk/education/about-your-parliament/general-elections/) được bổ nhiệm chính thức bởi quốc vương, người thường chọn lãnh đạo của đảng chính trị giành được nhiều ghế nhất trong Hạ viện. Hoa Kỳ sử dụng quy trình [Đại cử tri đoàn](https://www.archives.gov/federal-register/electoral-college/about.html) nhiều bước, trong đó công dân bỏ phiếu để quyết định cách mỗi tiểu bang phân bổ các Đại cử tri, những người sau đó sẽ bầu Tổng thống.

Tuy nhiên, có lẽ cách đơn giản nhất để tổ chức một cuộc bầu cử là thông qua một phương pháp thường được gọi là “plurality vote” (bầu chọn theo đa số tương đối, còn được gọi là “về đích đầu tiên” hoặc “người thắng lấy tất”). Trong bầu chọn plurality, mỗi cử tri được bỏ phiếu cho một ứng viên. Kết thúc cuộc bầu cử, ứng viên nào có số phiếu cao nhất sẽ được tuyên bố là người chiến thắng.

Trong bài toán này, bạn sẽ triển khai một chương trình mô phỏng cuộc bầu cử theo đa số tương đối (plurality), như mô tả dưới đây.

## Demo

## Mã phân phối

Trong bài toán này, bạn sẽ mở rộng chức năng của “mã phân phối” được cung cấp bởi đội ngũ CS50.

Tải mã phân phối

Đăng nhập vào [cs50.dev](https://cs50.dev/), nhấp vào cửa sổ terminal của bạn và thực thi lệnh `cd`. Bạn sẽ thấy dấu nhắc lệnh của terminal trông giống như dưới đây:

```
$
```

Tiếp theo, hãy thực thi

```python
wget https://cdn.cs50.net/2026/x/psets/3/plurality.zip
```

để tải một tệp ZIP có tên là `plurality.zip` vào codespace của bạn.

Sau đó, thực thi

```
unzip plurality.zip
```

để tạo một thư mục tên là `plurality`. Bạn không còn cần tệp ZIP nữa, vì vậy bạn có thể thực thi

```
rm plurality.zip
```

và trả lời “y” rồi nhấn Enter tại dấu nhắc để xóa tệp ZIP đã tải xuống.

Bây giờ hãy gõ

```bash
cd plurality
```

rồi nhấn Enter để di chuyển vào (tức là mở) thư mục đó. Dấu nhắc lệnh của bạn bây giờ sẽ giống như dưới đây.

```
plurality/ $
```

Nếu mọi việc thành công, bạn nên thực thi

```bash
ls
```

và thấy một tệp tên là `plurality.c`. Thực thi lệnh `code plurality.c` sẽ mở tệp nơi bạn sẽ nhập mã cho bài tập này. Nếu không, hãy xem lại các bước của mình và xem liệu bạn có thể xác định mình đã sai ở đâu không!

Hiểu mã nguồn trong `plurality.c`

Bất cứ khi nào bạn mở rộng chức năng của mã nguồn có sẵn, tốt nhất hãy đảm bảo rằng trước tiên bạn hiểu nó ở trạng thái hiện tại.

Trước tiên, hãy nhìn vào phần đầu của tệp. Dòng `#define MAX 9` là cú pháp được sử dụng ở đây có nghĩa là `MAX` là một hằng số (bằng `9`) có thể được sử dụng trong toàn bộ chương trình. Ở đây, nó đại diện cho số lượng ứng viên tối đa mà một cuộc bầu cử có thể có.

```
// Max number of candidates
#define MAX 9
```

Lưu ý rằng `plurality.c` sau đó sử dụng hằng số này để định nghĩa một mảng toàn cục—nghĩa là một mảng mà bất kỳ hàm nào cũng có thể truy cập.

```
// Array of candidates
candidate candidates[MAX];
```

Nhưng trong trường hợp này, `candidate` là gì? Trong `plurality.c`, một `candidate` là một `struct`. Mỗi `candidate` có hai trường: một `string` tên là `name` đại diện cho tên của ứng viên, và một `int` tên là `votes` đại diện cho số phiếu bầu mà ứng viên đó có.

```
// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;
```

Bây giờ, hãy xem chính hàm `main`. Hãy xem liệu bạn có thể tìm thấy nơi chương trình thiết lập một biến toàn cục `candidate_count` đại diện cho số lượng ứng viên trong cuộc bầu cử hay không.

```
// Number of candidates
int candidate_count;
```

Còn nơi nó sao chép các đối số dòng lệnh vào mảng `candidates` thì sao?

```c
// Populate array of candidates
candidate_count = argc - 1;
if (candidate_count > MAX)
{
    printf("Maximum number of candidates is %i\n", MAX);
    return 2;
}
for (int i = 0; i < candidate_count; i++)
{
    candidates[i].name = argv[i + 1];
    candidates[i].votes = 0;
}
```

Và nơi nó yêu cầu người dùng nhập số lượng cử tri?

```
int voter_count = get_int("Number of voters: ");
```

Sau đó, chương trình cho phép mỗi cử tri nhập một phiếu bầu, gọi hàm `vote` cho mỗi ứng viên được bầu. Cuối cùng, `main` gọi hàm `print_winner` để in ra người chiến thắng (hoặc những người chiến thắng) của cuộc bầu cử. Chúng tôi sẽ để bạn tự xác định đoạn mã thực hiện chức năng này.

Tuy nhiên, nếu bạn nhìn xuống phía dưới của tệp, bạn sẽ nhận thấy rằng các hàm `vote` và `print_winner` đã được để trống.

```c
// Update vote totals given a new vote
bool vote(string name)
{
    // TODO
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // TODO
    return;
}
```

Phần này là tùy bạn hoàn thiện! **Bạn không nên sửa đổi bất kỳ điều gì khác trong `plurality.c` ngoại trừ việc triển khai các hàm `vote` và `print_winner` (và việc thêm các tệp tiêu đề bổ sung, nếu bạn muốn).**

## Gợi ý

Nhấp vào các mục bên dưới để đọc một số lời khuyên!

Hoàn thành hàm `vote`

Tiếp theo, hãy hoàn thành hàm `vote`.

- Lưu ý rằng chữ ký của hàm `vote`, `bool vote(string name)`, cho thấy nó nhận một đối số duy nhất, một `string` tên là `name`, đại diện cho tên của ứng viên được bỏ phiếu.
- `vote` nên trả về một giá trị `bool`, trong đó `true` cho biết một phiếu bầu đã được bỏ thành công và `false` cho biết là không thành công.

Một cách để tiếp cận bài toán này là thực hiện các bước sau:

1. Duyệt qua từng ứng viên
   
   1. Kiểm tra xem tên của ứng viên có khớp với giá trị nhập vào, `name`, hay không
      
      1. Nếu đúng, hãy tăng số phiếu bầu của ứng viên đó và trả về `true`
      2. Nếu không, hãy tiếp tục kiểm tra
2. Nếu không có kết quả khớp sau khi kiểm tra từng ứng viên, hãy trả về `false`

Hãy viết một số mã giả để nhắc bạn thực hiện điều đó:

```sql
// Update vote totals given a new vote
bool vote(string name)
{
    // Iterate over each candidate
        // Check if candidate's name matches given name
            // If yes, increment candidate's votes and return true

    // If no match, return false
}
```

Tuy nhiên, việc triển khai mã nguồn thực tế sẽ dành cho bạn!

Hoàn thành hàm `print_winner`

Cuối cùng, hãy hoàn thành hàm `print_winner`.

- Hàm này nên in ra tên của ứng viên nhận được nhiều phiếu bầu nhất trong cuộc bầu cử, sau đó in một dòng mới.
- Cuộc bầu cử có thể kết thúc với kết quả hòa nếu có nhiều ứng viên cùng có số phiếu bầu tối đa. Trong trường hợp đó, bạn nên xuất tên của từng ứng viên chiến thắng, mỗi tên trên một dòng riêng biệt.

Bạn có thể nghĩ rằng một thuật toán sắp xếp sẽ giải quyết bài toán này tốt nhất: hãy tưởng tượng việc sắp xếp các ứng viên theo tổng số phiếu bầu của họ và in ra ứng viên (hoặc các ứng viên) đứng đầu. Tuy nhiên, hãy nhớ rằng việc sắp xếp có thể tốn kém: ngay cả Merge Sort, một trong những thuật toán sắp xếp nhanh nhất, cũng chạy trong \\(O(N \\space log(N))\\).

Hãy cân nhắc rằng bạn chỉ cần hai mẩu thông tin để giải quyết bài toán này:

1. Số phiếu bầu tối đa
2. Ứng viên (hoặc các ứng viên) có số phiếu bầu đó

Như vậy, một giải pháp tốt có thể chỉ yêu cầu hai lần tìm kiếm. Hãy viết một số mã giả để nhắc nhở bản thân thực hiện điều đó:

```c
// Print the winner (or winners) of the election
void print_winner(void)
{
    // Find the maximum number of votes

    // Print the candidate (or candidates) with maximum votes

}
```

Tuy nhiên, việc triển khai mã nguồn thực tế sẽ dành cho bạn!

## Hướng dẫn

## Cách kiểm tra

Hãy chắc chắn kiểm tra mã của bạn để đảm bảo nó xử lý được...

- Một cuộc bầu cử với bất kỳ số lượng ứng viên nào (tối đa là `MAX` là `9`)
- Bỏ phiếu cho một ứng viên bằng tên
- Các phiếu bầu không hợp lệ cho các ứng viên không có trong danh sách bầu cử
- In ra người chiến thắng của cuộc bầu cử nếu chỉ có một người
- In ra người chiến thắng của cuộc bầu cử nếu có nhiều người chiến thắng

### Độ chính xác

```
check50 cs50/problems/2026/x/plurality
```

### Phong cách

```
style50 plurality.c
```

## Cách nộp bài

Trong terminal của bạn, hãy thực thi lệnh dưới đây để nộp bài, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/plurality
```
