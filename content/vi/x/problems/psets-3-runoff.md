---
title: "Runoff - CS50x 2026"
pset: 3
draft: false
---

## Bài toán cần giải quyết

Bạn đã biết về bầu cử theo đa số tương đối (plurality elections), hệ thống này tuân theo một thuật toán rất đơn giản để xác định người chiến thắng: mỗi cử tri được bỏ một phiếu, và ứng viên có nhiều phiếu nhất sẽ thắng cuộc.

Nhưng bầu cử đa số tương đối cũng có một số nhược điểm. Chẳng hạn, điều gì sẽ xảy ra trong một cuộc bầu cử với ba ứng viên và các lá phiếu được bỏ như dưới đây?

![Năm lá phiếu, hòa giữa Alice và Bob](../fptp_ballot_1.png)

Trong trường hợp này, bầu cử đa số tương đối sẽ tuyên bố kết quả hòa giữa Alice và Bob, vì mỗi người có hai phiếu. Nhưng liệu đó có phải là kết quả đúng đắn?

Có một loại hệ thống bỏ phiếu khác được gọi là hệ thống bỏ phiếu xếp hạng (ranked-choice voting system). Trong hệ thống này, cử tri có thể bỏ phiếu cho nhiều hơn một ứng viên. Thay vì chỉ chọn lựa chọn hàng đầu, họ có thể xếp hạng các ứng viên theo thứ tự ưu tiên. Kết quả là các lá phiếu có thể trông giống như hình dưới đây.

![Năm lá phiếu, với thứ tự ưu tiên xếp hạng](../ranked_ballot_1.png)

Ở đây, mỗi cử tri, ngoài việc chỉ định ứng viên ưu tiên thứ nhất, còn cho biết lựa chọn thứ hai và thứ ba của họ. Và giờ đây, một cuộc bầu cử trước đó vốn bị hòa có thể tìm ra người chiến thắng. Cuộc đua ban đầu bị hòa giữa Alice và Bob, nên Charlie bị loại khỏi cuộc chơi. Nhưng cử tri chọn Charlie lại ưu tiên Alice hơn Bob, vì vậy Alice có thể được tuyên bố là người chiến thắng tại đây.

Bỏ phiếu xếp hạng cũng có thể giải quyết một nhược điểm tiềm ẩn khác của bầu cử đa số tương đối. Hãy xem các lá phiếu sau đây.

![Chín lá phiếu, với thứ tự ưu tiên xếp hạng](../ranked_ballot_3.png)

Ai nên thắng cuộc bầu cử này? Trong bầu cử đa số tương đối mà mỗi cử tri chỉ chọn ưu tiên thứ nhất, Charlie thắng với bốn phiếu so với chỉ ba phiếu cho Bob và hai phiếu cho Alice. Nhưng đa số cử tri (5 trên 9 người) sẽ cảm thấy hài lòng hơn với Alice hoặc Bob thay vì Charlie. Bằng cách xem xét các lựa chọn xếp hạng, một hệ thống bỏ phiếu có thể chọn ra người chiến thắng phản ánh tốt hơn nguyện vọng của các cử tri.

Một hệ thống bỏ phiếu xếp hạng như vậy là hệ thống bầu cử chung kết tức thì (instant runoff system). Trong cuộc bầu cử này, cử tri có thể xếp hạng bao nhiêu ứng viên tùy thích. Nếu bất kỳ ứng viên nào có đa số tuyệt đối (hơn 50%) số phiếu ưu tiên thứ nhất, ứng viên đó sẽ được tuyên bố là người chiến thắng.

Nếu không có ứng viên nào có hơn 50% số phiếu, thì một cuộc "chung kết tức thì" (instant runoff) sẽ diễn ra. Ứng viên nhận được ít phiếu bầu nhất sẽ bị loại khỏi cuộc bầu cử, và bất kỳ ai ban đầu chọn ứng viên đó là ưu tiên thứ nhất thì giờ đây lựa chọn thứ hai của họ sẽ được xem xét. Tại sao lại làm theo cách này? Về cơ bản, điều này mô phỏng những gì sẽ xảy ra nếu ứng viên ít được yêu thích nhất không tham gia cuộc bầu cử ngay từ đầu.

Quá trình này lặp lại: nếu không có ứng viên nào đạt đa số tuyệt đối, ứng viên đứng cuối cùng sẽ bị loại, và bất kỳ ai đã bỏ phiếu cho họ sẽ chuyển sang bỏ phiếu cho lựa chọn ưu tiên tiếp theo (người mà chính họ cũng chưa bị loại). Khi một ứng viên đạt được đa số tuyệt đối, ứng viên đó sẽ được tuyên bố là người chiến thắng.

Nghe có vẻ phức tạp hơn một chút so với bầu cử đa số tương đối, phải không? Nhưng nó có ưu điểm là một hệ thống bầu cử mà người chiến thắng đại diện chính xác hơn cho sở thích của cử tri. Trong một tệp có tên `runoff.c` nằm trong thư mục `runoff`, hãy tạo một chương trình để mô phỏng một cuộc bầu cử chung kết tức thì.

## Demo

## Mã nguồn phân phối

Tải mã nguồn phân phối

Đăng nhập vào [cs50.dev](https://cs50.dev/), nhấp vào cửa sổ terminal và thực hiện lệnh `cd` một mình. Bạn sẽ thấy dấu nhắc lệnh của terminal trông giống như dưới đây:

```
$
```

Tiếp theo, thực hiện lệnh:

```python
wget https://cdn.cs50.net/2026/x/psets/3/runoff.zip
```

để tải tệp ZIP có tên `runoff.zip` vào codespace của bạn.

Sau đó thực hiện:

```
unzip runoff.zip
```

để tạo một thư mục có tên `runoff`. Bạn không cần tệp ZIP nữa, vì vậy bạn có thể chạy:

```
rm runoff.zip
```

và trả lời "y" sau đó nhấn Enter tại dấu nhắc để xóa tệp ZIP đã tải xuống.

Bây giờ gõ:

```bash
cd runoff
```

nhấn Enter để chuyển vào (mở) thư mục đó. Dấu nhắc lệnh của bạn bây giờ sẽ giống như sau.

```
runoff/ $
```

Nếu mọi việc thành công, bạn hãy thực hiện:

```bash
ls
```

và thấy một tệp tên là `runoff.c`. Thực hiện lệnh `code runoff.c` sẽ mở tệp nơi bạn sẽ nhập mã cho bài tập này. Nếu không, hãy xem lại các bước và xác định xem bạn đã làm sai ở đâu!

Hiểu mã nguồn trong `runoff.c`

Bất cứ khi nào bạn mở rộng chức năng của mã nguồn hiện có, tốt nhất là hãy chắc chắn rằng bạn đã hiểu trạng thái hiện tại của nó.

Hãy xem phần trên cùng của `runoff.c` trước. Hai hằng số được định nghĩa: `MAX_CANDIDATES` cho số lượng ứng viên tối đa và `MAX_VOTERS` cho số lượng cử tri tối đa trong cuộc bầu cử.

```
// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9
```

Lưu ý rằng `MAX_CANDIDATES` được sử dụng để xác định kích thước của một mảng, `candidates`.

```
// Array of candidates
candidate candidates[MAX_CANDIDATES];
```

`candidates` là một mảng gồm các `candidate`. Trong `runoff.c`, một `candidate` là một cấu trúc (`struct`). Mỗi `candidate` có một trường `string` cho `name` (tên), một `int` đại diện cho số lượng `votes` (phiếu bầu) họ hiện có, và một giá trị `bool` gọi là `eliminated` (đã bị loại) cho biết ứng viên đó đã bị loại khỏi cuộc bầu cử hay chưa. Mảng `candidates` sẽ theo dõi tất cả các ứng viên trong cuộc bầu cử.

```
// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;
```

Bây giờ bạn có thể hiểu rõ hơn về `preferences` (các ưu tiên), mảng hai chiều. Mảng `preferences[i]` sẽ đại diện cho tất cả các ưu tiên của cử tri số `i`. Số nguyên `preferences[i][j]` sẽ lưu trữ chỉ số (index) của ứng viên từ mảng `candidates`, người là lựa chọn ưu tiên thứ `j` của cử tri `i`.

```
// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];
```

Chương trình cũng có hai biến toàn cục: `voter_count` (số lượng cử tri) và `candidate_count` (số lượng ứng viên).

```
// Numbers of voters and candidates
int voter_count;
int candidate_count;
```

Bây giờ đến hàm `main`. Lưu ý rằng sau khi xác định số lượng ứng viên và số lượng cử tri, vòng lặp bỏ phiếu chính bắt đầu, cho mỗi cử tri cơ hội bỏ phiếu. Khi cử tri nhập các ưu tiên của họ, hàm `vote` được gọi để theo dõi tất cả các ưu tiên đó. Nếu tại bất kỳ thời điểm nào, lá phiếu bị coi là không hợp lệ, chương trình sẽ thoát.

Khi tất cả các phiếu bầu đã được thu thập, một vòng lặp khác bắt đầu: vòng lặp này sẽ tiếp tục lặp qua quá trình chung kết tức thì để kiểm tra người chiến thắng và loại ứng viên đứng cuối cùng cho đến khi có người thắng cuộc.

Lời gọi đầu tiên ở đây là tới một hàm có tên `tabulate`, hàm này sẽ xem xét tất cả các ưu tiên của cử tri và tính toán tổng số phiếu hiện tại bằng cách xem xét lựa chọn hàng đầu của mỗi cử tri đối với những ứng viên chưa bị loại. Tiếp theo, hàm `print_winner` sẽ in ra người chiến thắng nếu có; nếu có, chương trình kết thúc. Nếu không, chương trình cần xác định số phiếu ít nhất mà bất kỳ ai còn lại trong cuộc bầu cử nhận được (thông qua lời gọi hàm `find_min`). Nếu hóa ra tất cả mọi người trong cuộc bầu cử đều hòa với số phiếu bằng nhau (được xác định bởi hàm `is_tie`), cuộc bầu cử được tuyên bố là hòa; nếu không, ứng viên (hoặc các ứng viên) đứng cuối cùng sẽ bị loại khỏi cuộc bầu cử thông qua lời gọi hàm `eliminate`.

Nếu bạn nhìn xuống phía dưới tệp, bạn sẽ thấy phần còn lại của các hàm—`vote`, `tabulate`, `print_winner`, `find_min`, `is_tie`, và `eliminate`—đều đang chờ bạn hoàn thành! **Bạn chỉ nên sửa đổi các hàm này trong runoff.c, mặc dù bạn có thể thêm các tệp tiêu đề `#include` ở đầu runoff.c nếu muốn.**

## Gợi ý

Nhấp vào các mục bên dưới để đọc lời khuyên!

Hoàn thành hàm `vote`

Hoàn thành hàm `vote`.

- Hàm này nhận ba đối số: `voter`, `rank`, và `name`.
- Nếu `name` khớp với tên của một ứng viên hợp lệ, bạn nên cập nhật mảng preferences toàn cục để chỉ ra rằng cử tri `voter` có ứng viên đó là lựa chọn ưu tiên thứ `rank` của họ. Hãy nhớ rằng `0` là ưu tiên thứ nhất, `1` là ưu tiên thứ hai, v.v. Bạn có thể giả định rằng không có hai ứng viên nào có cùng tên.
- Nếu ưu tiên được ghi lại thành công, hàm sẽ trả về `true`. Ngược lại, hàm trả về `false`. Ví dụ, hãy xem xét khi `name` không phải là tên của một trong các ứng viên.

Khi viết mã, hãy cân nhắc các gợi ý sau:

- Hãy nhớ rằng `candidate_count` lưu trữ số lượng ứng viên trong cuộc bầu cử.
- Hãy nhớ rằng bạn có thể sử dụng [`strcmp`](https://man.cs50.io/3/strcmp) để so sánh hai chuỗi.
- Hãy nhớ rằng `preferences[i][j]` lưu trữ chỉ số của ứng viên là lựa chọn xếp hạng thứ `j` của cử tri thứ `i`.

Hoàn thành hàm `tabulate`

Hoàn thành hàm `tabulate`.

- Hàm này nên cập nhật số lượng `votes` của mỗi ứng viên ở giai đoạn này của cuộc bầu cử.
- Hãy nhớ rằng ở mỗi giai đoạn, mỗi cử tri thực sự bỏ phiếu cho ứng viên họ ưu tiên nhất mà chưa bị loại.

Khi viết mã, hãy cân nhắc các gợi ý sau:

- Hãy nhớ rằng `voter_count` lưu trữ số lượng cử tri trong cuộc bầu cử và với mỗi cử tri, chúng ta muốn đếm một lá phiếu.
- Hãy nhớ rằng đối với cử tri `i`, ứng viên lựa chọn hàng đầu của họ được đại diện bởi `preferences[i][0]`, lựa chọn thứ hai bởi `preferences[i][1]`, v.v.
- Hãy nhớ rằng cấu trúc `candidate` có một trường gọi là `eliminated`, trường này sẽ là `true` nếu ứng viên đó đã bị loại.
- Hãy nhớ rằng cấu trúc `candidate` có một trường gọi là `votes`, bạn có thể muốn cập nhật trường này cho ứng viên được ưu tiên của mỗi cử tri.
- Hãy nhớ rằng một khi bạn đã bỏ phiếu cho ứng viên chưa bị loại đầu tiên của cử tri, bạn sẽ muốn dừng lại ở đó, không tiếp tục xem xét các lựa chọn tiếp theo trong lá phiếu của họ. Bạn có thể thoát khỏi vòng lặp sớm bằng lệnh `break` bên trong một câu lệnh điều kiện.

Hoàn thành hàm `print_winner`

Hoàn thành hàm `print_winner`.

- Nếu bất kỳ ứng viên nào có hơn một nửa số phiếu bầu, tên của họ sẽ được in ra và hàm sẽ trả về `true`.
- Nếu chưa có ai thắng cuộc bầu cử, hàm nên trả về `false`.

Khi viết mã, hãy cân nhắc gợi ý này:

- Hãy nhớ rằng `voter_count` lưu trữ số lượng cử tri trong cuộc bầu cử. Dựa vào đó, làm thế nào bạn biểu diễn được số phiếu cần thiết để thắng cuộc bầu cử?

Hoàn thành hàm `find_min`

Hoàn thành hàm `find_min`.

- Hàm này nên trả về tổng số phiếu tối thiểu của bất kỳ ứng viên nào vẫn còn trong cuộc bầu cử.

Khi viết mã, hãy cân nhắc gợi ý này:

- Có thể bạn sẽ muốn lặp qua các ứng viên để tìm người vừa còn trong cuộc bầu cử vừa có số phiếu ít nhất. Bạn nên theo dõi thông tin gì khi lặp qua các ứng viên?

Hoàn thành hàm `is_tie`

Hoàn thành hàm `is_tie`.

- Hàm này nhận một đối số `min`, đó là số phiếu tối thiểu mà bất kỳ ai trong cuộc bầu cử hiện có.
- Hàm nên trả về `true` nếu mọi ứng viên còn lại trong cuộc bầu cử đều có cùng số phiếu, và trả về `false` nếu ngược lại.

Khi viết mã, hãy cân nhắc gợi ý này:

- Hãy nhớ rằng kết quả hòa xảy ra nếu mọi ứng viên còn lại trong cuộc bầu cử đều có cùng số phiếu. Cũng lưu ý rằng hàm `is_tie` nhận đối số `min`, là số phiếu nhỏ nhất mà bất kỳ ứng viên nào hiện có. Làm thế nào bạn có thể sử dụng `min` để xác định xem cuộc bầu cử có hòa hay không (hoặc ngược lại)?

Hoàn thành hàm `eliminate`

Hoàn thành hàm `eliminate`.

- Hàm này nhận một đối số `min`, đó là số phiếu tối thiểu mà bất kỳ ai trong cuộc bầu cử hiện có.
- Hàm nên loại bỏ ứng viên (hoặc các ứng viên) có số phiếu bằng `min`.

## Walkthrough

## Cách kiểm tra

Hãy đảm bảo kiểm tra mã của bạn để chắc chắn rằng nó xử lý được…

- Một cuộc bầu cử với bất kỳ số lượng ứng viên nào (tối đa là `MAX` là `9`)
- Bỏ phiếu cho một ứng viên bằng tên
- Phiếu bầu không hợp lệ cho các ứng viên không có tên trong lá phiếu
- In ra người chiến thắng nếu chỉ có một người
- Không loại bỏ bất kỳ ai trong trường hợp hòa giữa tất cả các ứng viên còn lại

### Tính chính xác

```
check50 cs50/problems/2026/x/runoff
```

### Phong cách trình bày

```
style50 runoff.c
```

## Cách nộp bài

Trong terminal của bạn, hãy thực hiện lệnh dưới đây để nộp bài làm, và trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/runoff
```
