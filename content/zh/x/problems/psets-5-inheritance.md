---
title: "继承 - CS50x 2026"
pset: 5
draft: false
---

## 待解决的问题

一个人的血型由两个等位基因（即基因的不同形式）决定。三种可能的等位基因是 A、B 和 O，每个人都有两个（可能相同，也可能不同）。每个孩子的父母会随机将其两个血型等位基因中的一个传给孩子。因此，可能的血型组合包括：OO、OA、OB、AO、AA、AB、BO、BA 和 BB。

例如，如果父母一方的血型为 AO，另一方的血型为 BB，那么根据从每位家长那里获得的等位基因，孩子的可能血型将是 AB 和 OB。同样，如果父母一方的血型为 AO，另一方为 OB，那么孩子的可能血型将是 AO、OB、AB 和 OO。

在名为 `inheritance` 的文件夹中一个名为 `inheritance.c` 的文件中，模拟家庭中每个成员的血型继承。

## 演示

## 分发代码

对于这个问题，你将扩展 CS50 工作人员提供给你的代码的功能。

下载分发代码

登录 [cs50.dev](https://cs50.dev/)，点击终端窗口，并单独执行 `cd`。你应该会发现终端窗口的提示符如下所示：

```
$
```

接下来执行

```python
wget https://cdn.cs50.net/2026/x/psets/5/inheritance.zip
```

以便将名为 `inheritance.zip` 的 ZIP 文件下载到你的 codespace 中。

然后执行

```
unzip inheritance.zip
```

创建一个名为 `inheritance` 的文件夹。你不再需要该 ZIP 文件，因此可以执行

```
rm inheritance.zip
```

并在提示符处输入 “y” 后按 Enter 键，以删除下载的 ZIP 文件。

现在输入

```bash
cd inheritance
```

后按 Enter 键进入（即打开）该目录。你的提示符现在应该如下所示。

```
inheritance/ $
```

单独执行 `ls`，你应该会看到一个名为 `inheritance.c` 的文件。

如果你遇到任何问题，请再次按照这些步骤操作，看看能否确定哪里出错了！

## 实现细节

完成 `inheritance.c` 的实现，使其创建一个指定代数大小的家庭，并为每个家庭成员分配血型等位基因。最老的一代将随机分配等位基因。

- `create_family` 函数接收一个整数（`generations`）作为输入，并应为该代数家庭的每个成员分配（通过 `malloc`）一个 `person` 结构体，返回指向最年轻一代 `person` 的指针。
  
  - 例如，`create_family(3)` 应返回指向一个拥有父母的人的指针，而其父母也各自拥有父母。
  - 每个 `person` 都应分配有 `alleles`（等位基因）。最老的一代应随机选择等位基因（通过调用 `random_allele` 函数），而较年轻的一代应从每位父母那里（随机选择）继承一个等位基因。
  - 每个 `person` 都应分配有 `parents`。最老的一代其 `parents` 应都设为 `NULL`，而较年轻的一代其 `parents` 应是一个包含两个指针的数组，每个指针指向不同的父母。

## 提示

理解 `inheritance.c` 中的代码

查看 `inheritance.c` 中的分发代码。

注意名为 `person` 的类型的定义。每个人都有一个包含两个 `parents` 的数组，每个 `parents` 都是指向另一个 `person` 结构体的指针。每个人还有一个包含两个 `alleles` 的数组，每个 `alleles` 都是一个 `char`（要么是 `'A'`，要么是 `'B'`，或者是 `'O'`）。

```
// Each person has two parents and two alleles
typedef struct person
{
    struct person *parents[2];
    char alleles[2];
}
person;
```

现在，看看 `main` 函数。该函数首先为随机数生成器“播种”（即提供一些初始输入），我们稍后将使用它来生成随机等位基因。

```
// Seed random number generator
srandom(time(0));
```

然后，`main` 函数调用 `create_family` 函数，模拟为一个 3 代家庭（即一个人、他们的父母和他们的祖父母）创建 `person` 结构体。

```sql
// Create a new family with three generations
person *p = create_family(GENERATIONS);
```

接着，我们调用 `print_family` 来打印出每个家庭成员及其血型。

```
// Print family tree of blood types
print_family(p, 0);
```

最后，函数调用 `free_family` 来 `free`（释放）之前用 `malloc` 分配的任何内存。

```
// Free memory
free_family(p);
```

`create_family` 和 `free_family` 函数留给你来编写！

完成 `create_family` 函数

`create_family` 函数应返回指向一个 `person` 的指针，该人已从输入的 `generations` 代数中继承了血型。

- 首先注意，这个问题提供了使用递归的好机会。
  
  - 要确定当前人的血型，你需要先确定其父母的血型。
  - 要确定父母的血型，你必须先确定 *他们* 父母的血型。以此类推，直到达到你想要模拟的最后一代。

为了解决这个问题，你会在分发代码中找到几个 TODO。

首先，你应该为新成员分配内存。回想一下，你可以使用 `malloc` 分配内存，并使用 `sizeof(person)` 获取要分配的字节数。

```c
// Allocate memory for new person
person *new_person = malloc(sizeof(person));
```

接下来，你应该检查是否还有代数需要创建：即 `generations > 1` 是否成立。

如果 `generations > 1`，则还有更多代数需要分配。我们已经通过递归调用 `create_family` 创建了两个新父母 `parent0` 和 `parent1`。然后，你的 `create_family` 函数应设置你创建的新人的父母指针。最后，通过从每位父母中随机选择一个等位基因，为新人分配两个 `alleles`。

- 请记住，要通过指针访问变量，可以使用箭头符号。例如，如果 `p` 是指向一个人的指针，那么可以通过 `p->parents[0]` 访问指向此人第一位父母的指针。
- 你可能会发现 `random()` 函数对于随机分配等位基因很有用。此函数返回一个介于 `0` 和 `RAND_MAX`（即 `32767`）之间的整数。特别是，要生成一个为 `0` 或 `1` 的伪随机数，你可以使用表达式 `random() % 2`。

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

假设没有更多代数需要模拟了。也就是说，`generations == 1`。如果是这样，此人将没有父母数据。你的新人的两位父母都应设置为 `NULL`，并且每个 `allele` 都应随机生成。

```c
// Set parent pointers to NULL
new_person->parents[0] = NULL;
new_person->parents[1] = NULL;

// Randomly assign alleles
new_person->alleles[0] = random_allele();
new_person->alleles[1] = random_allele();
```

最后，你的函数应返回指向所分配的 `person` 的指针。

```
// Return newly created person
return new_person;
```

完成 `free_family` 函数

`free_family` 函数应接收指向 `person` 的指针作为输入，释放该人的内存，然后递归释放其所有祖先的内存。

- 既然这是一个递归函数，你首先应该处理基本情况（base case）。如果函数的输入是 `NULL`，那么就没有什么可释放的，因此你的函数可以立即返回。
- 否则，你应该在释放孩子之前，递归地 `free` 父母双方。

以下是一个相当大的提示，这里是具体的操作方法！

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

### 演练

不确定如何解决？

## 如何测试

运行 `./inheritance` 后，你的程序应遵守背景中描述的规则。孩子应该有两个等位基因，父母各传一个。父母也应该各有两个等位基因，分别来自他们的父母。

例如，在下面的示例中，第 0 代的孩子从第 1 代的两位父母那里都获得了一个 O 等位基因。第一位父母从第一位祖父母那里获得了一个 A，从第二位祖父母那里获得了一个 O。类似地，第二位父母从他们的祖父母那里获得了一个 O 和一个 B。

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

### 正确性

```
check50 cs50/problems/2026/x/inheritance
```

### 风格

```
style50 inheritance.c
```

## 如何提交

在你的终端中，执行以下命令提交你的作品，并根据提示回答问题。

```
submit50 cs50/problems/2026/x/inheritance
```
