title: "Tideman - CS50x 2026"
pset: 3
draft: "false"
---

## Vấn đề cần giải quyết

Bạn đã biết về bầu cử theo đa số tương đối (plurality election), một thuật toán rất đơn giản để xác định người chiến thắng trong một cuộc bầu cử: mỗi cử tri có một phiếu bầu, và ứng cử viên nào có nhiều phiếu nhất sẽ thắng.

Nhưng bầu cử đa số tương đối có một số nhược điểm. Ví dụ, điều gì sẽ xảy ra trong một cuộc bầu cử với ba ứng cử viên và các lá phiếu dưới đây?

![Năm lá phiếu, hòa giữa Alice và Bob](../fptp_ballot_1.png)

Ở đây, bầu cử đa số tương đối sẽ công bố kết quả hòa giữa Alice và Bob, vì mỗi người có hai phiếu. Nhưng liệu đó có phải là kết quả đúng đắn?

Có một loại hệ thống bỏ phiếu khác được gọi là hệ thống bỏ phiếu xếp hạng lựa chọn (ranked-choice voting). Trong hệ thống này, cử tri có thể bầu cho nhiều hơn một ứng cử viên. Thay vì chỉ bầu cho lựa chọn hàng đầu, họ có thể xếp hạng các ứng cử viên theo thứ tự ưu tiên. Các lá phiếu kết quả có thể trông như hình bên dưới.

![Năm lá phiếu, với các lựa chọn xếp hạng](../ranked_ballot_1.png)

Tại đây, ngoài việc chỉ định ứng cử viên ưu tiên thứ nhất, mỗi cử tri còn cho biết lựa chọn thứ hai và thứ ba của họ. Và giờ đây, một cuộc bầu cử vốn bị hòa trước đó đã có thể tìm ra người chiến thắng. Cuộc đua ban đầu hòa giữa Alice và Bob. Nhưng cử tri chọn Charlie lại ưu tiên Alice hơn Bob, vì vậy Alice có thể được tuyên bố là người chiến thắng ở đây.

Bỏ phiếu xếp hạng lựa chọn cũng có thể giải quyết một nhược điểm tiềm tàng khác của bầu cử đa số tương đối. Hãy nhìn vào các lá phiếu sau.

![Chín lá phiếu, với các lựa chọn xếp hạng](../condorcet_1.png)

Ai nên thắng cuộc bầu cử này? Trong một cuộc bầu cử đa số tương đối mà mỗi cử tri chỉ chọn ưu tiên thứ nhất, Charlie thắng cuộc bầu cử này với bốn phiếu so với chỉ ba phiếu cho Bob và hai phiếu cho Alice. (Lưu ý rằng, nếu bạn quen thuộc với hệ thống bỏ phiếu vòng loại trực tiếp ngay lập tức - instant runoff voting, Charlie cũng thắng theo hệ thống đó). Tuy nhiên, Alice có thể lập luận một cách hợp lý rằng cô ấy nên là người chiến thắng thay vì Charlie: xét cho cùng, trong số chín cử tri, đa số (năm người trong số họ) ưu tiên Alice hơn Charlie, vì vậy hầu hết mọi người sẽ cảm thấy hài lòng hơn với Alice là người chiến thắng thay vì Charlie.

Trong cuộc bầu cử này, Alice được gọi là “người chiến thắng Condorcet”: người sẽ thắng trong bất kỳ cuộc đối đầu trực tiếp nào với một ứng cử viên khác. Nếu cuộc bầu cử chỉ có Alice và Bob, hoặc chỉ Alice và Charlie, Alice sẽ thắng.

Phương pháp bỏ phiếu Tideman (còn được gọi là “xếp hạng theo cặp” - ranked pairs) là một phương pháp bỏ phiếu xếp hạng lựa chọn đảm bảo tìm ra người chiến thắng Condorcet nếu có. Trong một tệp có tên `tideman.c` trong thư mục `tideman`, hãy tạo một chương trình để mô phỏng một cuộc bầu cử theo phương pháp bỏ phiếu Tideman.

## Bản demo

## Mã nguồn phân phối

Tải mã nguồn phân phối

Đăng nhập vào [cs50.dev](https://cs50.dev/), nhấp vào cửa sổ terminal và thực hiện lệnh `cd` một mình. Bạn sẽ thấy dấu nhắc lệnh của cửa sổ terminal trông giống như dưới đây:

```
$
```

Tiếp theo, thực hiện lệnh

```python
wget https://cdn.cs50.net/2026/x/psets/3/tideman.zip
```

để tải một tệp ZIP có tên `tideman.zip` vào codespace của bạn.

Sau đó thực hiện

```
unzip tideman.zip
```

để tạo một thư mục có tên `tideman`. Bạn không còn cần tệp ZIP nữa, vì vậy bạn có thể thực hiện

```
rm tideman.zip
```

và trả lời “y” rồi nhấn Enter tại dấu nhắc để xóa tệp ZIP đã tải xuống.

Bây giờ hãy nhập

```bash
cd tideman
```

theo sau là Enter để di chuyển vào (tức là mở) thư mục đó. Dấu nhắc lệnh của bạn bây giờ sẽ trông giống như dưới đây.

```
tideman/ $
```

Nếu mọi việc thành công, bạn nên thực hiện

```bash
ls
```

và thấy một tệp có tên `tideman.c`. Thực hiện `code tideman.c` sẽ mở tệp nơi bạn sẽ nhập mã của mình cho bài tập này. Nếu không, hãy xem lại các bước và xem liệu bạn có thể xác định mình đã sai ở đâu không!

## Bối cảnh

Nói một cách tổng quát, phương pháp Tideman hoạt động bằng cách xây dựng một “đồ thị” gồm các ứng cử viên, trong đó một mũi tên (tức là cạnh) từ ứng cử viên A đến ứng cử viên B cho biết rằng ứng cử viên A thắng ứng cử viên B trong một cuộc đối đầu trực tiếp. Đồ thị cho cuộc bầu cử trên sẽ trông như hình bên dưới.

![Chín lá phiếu, với các lựa chọn xếp hạng](../condorcet_graph_1.png)

Mũi tên từ Alice đến Bob có nghĩa là có nhiều cử tri ưu tiên Alice hơn Bob (5 người ưu tiên Alice, 4 người ưu tiên Bob). Tương tự, các mũi tên khác có nghĩa là có nhiều cử tri ưu tiên Alice hơn Charlie, và nhiều cử tri ưu tiên Charlie hơn Bob.

Nhìn vào đồ thị này, phương pháp Tideman cho biết người chiến thắng cuộc bầu cử phải là “nguồn” (source) của đồ thị (tức là ứng cử viên không có mũi tên nào hướng vào mình). Trong trường hợp này, nguồn là Alice — Alice là người duy nhất không có mũi tên nào hướng vào mình, nghĩa là không ai được ưu tiên hơn Alice trong đối đầu trực tiếp. Do đó, Alice được tuyên bố là người chiến thắng cuộc bầu cử.

Tuy nhiên, có khả năng khi vẽ các mũi tên, không có người chiến thắng Condorcet. Hãy xem xét các lá phiếu dưới đây.

![Chín lá phiếu, với các lựa chọn xếp hạng](../no_condorcet_1.png)

Giữa Alice và Bob, Alice được ưu tiên hơn Bob với tỷ lệ 7-2. Giữa Bob và Charlie, Bob được ưu tiên hơn Charlie với tỷ lệ 5-4. Nhưng giữa Charlie và Alice, Charlie được ưu tiên hơn Alice với tỷ lệ 6-3. Nếu chúng ta vẽ đồ thị ra, sẽ không có nguồn! Chúng ta có một chu trình các ứng cử viên, trong đó Alice thắng Bob, Bob thắng Charlie và Charlie thắng Alice (giống như trò chơi kéo-búa-bao). Trong trường hợp này, có vẻ như không có cách nào để chọn ra người chiến thắng.

Để xử lý vấn đề này, thuật toán Tideman phải cẩn thận để tránh tạo ra các chu trình trong đồ thị ứng cử viên. Thuật toán làm điều này như thế nào? Thuật toán sẽ khóa các cạnh mạnh nhất trước, vì đó được cho là những cạnh quan trọng nhất. Cụ thể, thuật toán Tideman quy định rằng các cạnh đối đầu nên được “khóa” (locked in) vào đồ thị từng cái một, dựa trên “độ mạnh” của chiến thắng (càng nhiều người ưu tiên một ứng cử viên hơn đối thủ của họ, chiến thắng đó càng mạnh). Miễn là cạnh đó có thể được khóa vào đồ thị mà không tạo thành chu trình, cạnh đó sẽ được thêm vào; nếu không, cạnh đó sẽ bị bỏ qua.

Điều này sẽ hoạt động như thế nào trong trường hợp các phiếu bầu ở trên? Chà, cách biệt chiến thắng lớn nhất cho một cặp là Alice thắng Bob, vì có 7 cử tri ưu tiên Alice hơn Bob (không có cuộc đối đầu trực tiếp nào khác có người thắng được ưu tiên bởi nhiều hơn 7 cử tri). Vì vậy, mũi tên Alice-Bob được khóa vào đồ thị đầu tiên. Cách biệt chiến thắng lớn tiếp theo là chiến thắng 6-3 của Charlie trước Alice, vì vậy mũi tên đó được khóa vào tiếp theo.

Tiếp theo là chiến thắng 5-4 của Bob trước Charlie. Nhưng hãy lưu ý: nếu chúng ta thêm một mũi tên từ Bob đến Charlie bây giờ, chúng ta sẽ tạo ra một chu trình! Vì đồ thị không thể cho phép chu trình, chúng ta nên bỏ qua cạnh này và không thêm nó vào đồ thị. Nếu còn nhiều mũi tên khác để xem xét, chúng ta sẽ xem xét tiếp theo, nhưng đó là mũi tên cuối cùng, vì vậy đồ thị đã hoàn thành.

Quá trình từng bước này được hiển thị bên dưới, với đồ thị cuối cùng ở bên phải.

![Chín lá phiếu, với các lựa chọn xếp hạng](../lockin.png)

Dựa trên đồ thị kết quả, Charlie là nguồn (không có mũi tên nào hướng về Charlie), vì vậy Charlie được tuyên bố là người chiến thắng cuộc bầu cử này.

Nói một cách trang trọng hơn, phương pháp bỏ phiếu Tideman bao gồm ba phần:

- **Tally** (Kiểm phiếu): Sau khi tất cả các cử tri đã cho biết tất cả các lựa chọn ưu tiên của họ, hãy xác định đối với mỗi cặp ứng cử viên, ai là ứng cử viên được ưu tiên hơn và với cách biệt bao nhiêu.
- **Sort** (Sắp xếp): Sắp xếp các cặp ứng cử viên theo thứ tự giảm dần của độ mạnh chiến thắng, trong đó độ mạnh chiến thắng được định nghĩa là số lượng cử tri ưu tiên ứng cử viên chiến thắng.
- **Lock** (Khóa): Bắt đầu với cặp mạnh nhất, lần lượt đi qua các cặp ứng cử viên theo thứ tự và “khóa” từng cặp vào đồ thị ứng cử viên, miễn là việc khóa cặp đó không tạo ra chu trình trong đồ thị.

Một khi đồ thị hoàn thành, nguồn của đồ thị (người không có cạnh nào hướng vào mình) là người chiến thắng!

## Hiểu đề bài

Hãy cùng xem qua tệp `tideman.c`.

Đầu tiên, hãy chú ý đến mảng hai chiều `preferences`. Số nguyên `preferences[i][j]` sẽ đại diện cho số lượng cử tri ưu tiên ứng cử viên `i` hơn ứng cử viên `j`.

Tệp cũng định nghĩa một mảng hai chiều khác, gọi là `locked`, đại diện cho đồ thị ứng cử viên. `locked` là một mảng boolean, vì vậy `locked[i][j]` mang giá trị `true` đại diện cho sự tồn tại của một cạnh hướng từ ứng cử viên `i` đến ứng cử viên `j`; `false` có nghĩa là không có cạnh. (Nếu bạn tò mò, cách biểu diễn đồ thị này được gọi là “ma trận kề” - adjacency matrix).

Tiếp theo là một `struct` có tên là `pair`, được sử dụng để đại diện cho một cặp ứng cử viên: mỗi cặp bao gồm chỉ số của ứng cử viên chiến thắng (`winner`) và chỉ số của ứng cử viên thua cuộc (`loser`).

Bản thân các ứng cử viên được lưu trữ trong mảng `candidates`, đây là một mảng các `string` đại diện cho tên của từng ứng cử viên. Ngoài ra còn có một mảng `pairs`, sẽ đại diện cho tất cả các cặp ứng cử viên (trong đó một người được ưu tiên hơn người kia) trong cuộc bầu cử.

Chương trình cũng có hai biến toàn cục: `pair_count` và `candidate_count`, đại diện cho số lượng các cặp và số lượng các ứng cử viên trong các mảng `pairs` và `candidates` tương ứng.

Bây giờ chuyển sang hàm `main`. Lưu ý rằng sau khi xác định số lượng ứng cử viên, chương trình lặp qua đồ thị `locked` và ban đầu đặt tất cả các giá trị thành `false`, điều đó có nghĩa là đồ thị ban đầu của chúng ta sẽ không có cạnh nào.

Tiếp theo, chương trình lặp qua tất cả các cử tri và thu thập các lựa chọn ưu tiên của họ vào một mảng gọi là `ranks` (thông qua lệnh gọi hàm `vote`), trong đó `ranks[i]` là chỉ số của ứng cử viên là lựa chọn ưu tiên thứ `i` của cử tri. Các xếp hạng này được truyền vào hàm `record_preference`, hàm này có nhiệm vụ lấy các xếp hạng đó và cập nhật biến toàn cục `preferences`.

Khi tất cả các phiếu bầu đã được thu thập, các cặp ứng cử viên sẽ được thêm vào mảng `pairs` thông qua lệnh gọi hàm `add_pairs`, được sắp xếp qua lệnh gọi hàm `sort_pairs` và được khóa vào đồ thị qua lệnh gọi hàm `lock_pairs`. Cuối cùng, `print_winner` được gọi để in ra tên người chiến thắng cuộc bầu cử!

Phía dưới trong tệp, bạn sẽ thấy các hàm `vote`, `record_preference`, `add_pairs`, `sort_pairs`, `lock_pairs`, và `print_winner` đang được để trống. Đó là nhiệm vụ của bạn!

## Yêu cầu kỹ thuật

Hoàn thành việc triển khai `tideman.c` sao cho nó mô phỏng một cuộc bầu cử Tideman.

- Hoàn thành hàm `vote`.
  
  - Hàm nhận các đối số `rank`, `name`, và `ranks`. Nếu `name` khớp với tên của một ứng cử viên hợp lệ, thì bạn nên cập nhật mảng `ranks` để cho biết rằng cử tri có ứng cử viên đó là lựa chọn ưu tiên thứ `rank` của họ (trong đó `0` là ưu tiên thứ nhất, `1` là ưu tiên thứ hai, v.v.)
  - Lưu ý rằng `ranks[i]` ở đây đại diện cho lựa chọn ưu tiên thứ `i` của người dùng.
  - Hàm sẽ trả về `true` nếu xếp hạng được ghi lại thành công và `false` nếu ngược lại (ví dụ, nếu `name` không phải là tên của một trong các ứng cử viên).
  - Bạn có thể giả định rằng không có hai ứng cử viên nào có cùng tên.
- Hoàn thành hàm `record_preferences`.
  
  - Hàm này được gọi một lần cho mỗi cử tri và nhận đối số là mảng `ranks` (lưu ý rằng `ranks[i]` là ưu tiên thứ `i` của cử tri, trong đó `ranks[0]` là ưu tiên thứ nhất).
  - Hàm nên cập nhật mảng toàn cục `preferences` để thêm các lựa chọn ưu tiên của cử tri hiện tại. Lưu ý rằng `preferences[i][j]` nên đại diện cho số lượng cử tri ưu tiên ứng cử viên `i` hơn ứng cử viên `j`.
  - Bạn có thể giả định rằng mọi cử tri sẽ xếp hạng tất cả các ứng cử viên.
- Hoàn thành hàm `add_pairs`.
  
  - Hàm nên thêm tất cả các cặp ứng cử viên mà ở đó một ứng cử viên được ưu tiên hơn vào mảng `pairs`. Một cặp ứng cử viên hòa nhau (không ai được ưu tiên hơn người kia) không nên được thêm vào mảng.
  - Hàm nên cập nhật biến toàn cục `pair_count` thành số lượng các cặp ứng cử viên. (Do đó, tất cả các cặp nên được lưu trữ giữa `pairs[0]` và `pairs[pair_count - 1]`, bao gồm cả hai đầu).
- Hoàn thành hàm `sort_pairs`.
  
  - Hàm nên sắp xếp mảng `pairs` theo thứ tự giảm dần của độ mạnh chiến thắng, trong đó độ mạnh chiến thắng được định nghĩa là số lượng cử tri ưu tiên ứng cử viên chiến thắng. Nếu nhiều cặp có cùng độ mạnh chiến thắng, bạn có thể giả định rằng thứ tự giữa chúng không quan trọng.
- Hoàn thành hàm `lock_pairs`.
  
  - Hàm nên tạo đồ thị `locked`, thêm tất cả các cạnh theo thứ tự giảm dần của độ mạnh chiến thắng miễn là cạnh đó không tạo ra chu trình.
- Hoàn thành hàm `print_winner`.
  
  - Hàm nên in ra tên của ứng cử viên là nguồn của đồ thị. Bạn có thể giả định rằng sẽ không có nhiều hơn một nguồn.

Bạn không nên thay đổi bất kỳ điều gì khác trong `tideman.c` ngoại trừ việc triển khai các hàm `vote`, `record_preferences`, `add_pairs`, `sort_pairs`, `lock_pairs`, và `print_winner` (và việc thêm các tệp tiêu đề bổ sung nếu bạn muốn). Bạn được phép thêm các hàm bổ sung vào `tideman.c`, miễn là bạn không thay đổi khai báo của bất kỳ hàm nào hiện có.

## Hướng dẫn chi tiết

## Cách kiểm tra

Hãy đảm bảo kiểm tra mã của bạn để chắc chắn rằng nó xử lý được…

- Một cuộc bầu cử với số lượng ứng cử viên bất kỳ (tối đa là `MAX` bằng `9`)
- Bỏ phiếu cho một ứng cử viên bằng tên
- Phiếu bầu không hợp lệ cho các ứng cử viên không có trong lá phiếu
- In ra người chiến thắng cuộc bầu cử

### Tính đúng đắn

```
check50 cs50/problems/2026/x/tideman
```

### Phong cách

```
style50 tideman.c
```

## Cách nộp bài

Trong terminal của bạn, thực hiện lệnh dưới đây để nộp bài làm của mình, trả lời các câu hỏi hiện ra sau đó.

```
submit50 cs50/problems/2026/x/tideman
```
