# 基础通识

## 基本概念

1. 定义：AI，即人工智能，是一种模拟人类智能过程的技术。它包括学习（获取信息并规则以使用信息）、推理（使用规则来达到近似或确定的结论）和自我修正。
2. 应用领域
   * 专家系统
   * 自然语言处理
   * 语音识别
   * 机器视觉
   * 机器人技术
3. 图灵测试：一种模拟人类对话的技术，主要用于测试机器的智能程度。

## 技术发展

1. 四次浪潮
   * 符号主义：以符号处理为基础，旨在模拟人类的思维过程
   * 机器学习与神经网络：
   * 深度学习：可以处理非结构化复杂数据
   * GPT&大型预训练模型
2. 机器学习
   * 机器学习是人工智能领域的一个核心分支，通过从数据中学习模式和规律，使计算机能够进行预测和决策。
   * 监督学习、非监督学习和强化学习是机器学习的不同方法。
   * 支持向量机是一种复杂的分类技术，在处理高维数据时表现出色。
   * 风险预测和推荐系统是机器学习在金融领域的应用。
3. 深度学习
   * 深度学习是机器学习的子集，利用多层神经网络模拟人类学习过程。
   * 卷积神经网络和递归神经网络是两种常见的深度学习架构，分别适用于图像数据和序列数据。
   * Pytorch和TensorFlow是两种流行的深度学习框架，广泛应用于视觉、语音和围棋等领域。
4. 大模型
   * 大模型是指具有大量参数和强大计算能力的人工智能模型，能够处理和分析大规模数据集。
   * 大模型技术中出现的技术突破包括attention机制和transformer框架，提高了模型的学习效率和能力。
   * 大模型在生成式AI中的应用场景包括文本生成、图像生成和视频制作等，推动了人工智能在娱乐艺术和媒体行业中的应用。

## 数学基础

## 认知树立

1. AI并不会抢走你的饭碗，时代只会淘汰不会使用AI的人。

# 机器学习

## 概述

1. 机器学习

   * 从数据中自动分析获取模型，并利用模型对未知数据进行预测。
   * 数据集构成
     * 特征值+目标值
     * 每一组数据称为一组样本
     * 有些数据集可以没有目标值

   ![](https://whymechen.oss-cn-chengdu.aliyuncs.com/image/202501042059353.png)

2. 算法分类

   * 监督（supervised learning）学习（预测）： 输入数据**有特征有标签**，即有标准答案
     * 分类问题（目标值为类别）：k-近邻算法、贝叶斯分类、决策树与随机森林、逻辑回归
     * 回归问题（目标值为连续性数据）： 线性回归、岭回归
   * 无监督（unsupervised learning）学习）：输入数据**有特征无标签**，即无标准答案
     * 聚类：k-means

3. 开发流程

   * 获取数据
   * 数据处理
   * 特征工程
   * 机器学习算法训练 -> 得到模型
   * 模型评估
   * 应用

4. 常用库&框架

   * scikit-learn
   * pytorch
   * tensorflow
   * caff2
   * chainer

## 数据集

1. 数据集划分
   * **训练数据集**： 用于训练，构建模型
   * **测试数据集**：用于评估模型模型
2. 常用数据集
   * kaggle：https://www.kaggle.com/datasets
   * UCI数据集：https://archive.ics.uci.edu/
   * scikit-learn

## 特征工程

1. 简介：**使用专业背景知识和技巧处理数据**，使特征能在机器学习算法上发挥更好的作用。
2. 特征抽取：**将任意数据（如文本、图像）转换为可用于机器学习的数字特征**
   * 特征值化是为了计算机更好理解数据
   * 字典特征提取（特征离散化）
   * 文本特征提取
   * 图像特征提取
3. 特征预处理：通过一些转换函数将特征数据转换成更加适合算法模型的特征数据过程。
   * 归一化、标准化
   * 归一化和统一化的意义在于量纲统一
4. 特征降维
   * 特征选择：数据中包含冗余或相关变量，旨在从原有特征中找出主要特征。
     * 过滤式（Filter）：主要探究特征本身特点、特征与特征和目标值之间关联
       * 方差选择法：低方差特征过滤
       * 相关系数
     * 嵌入式（Embedded）：算法自动选择特征
       * 决策树：信息熵、信息增益
       * 正则化：L1、L2
       * 深度学习：卷积

## 工具&库

### Scikit-learn

#### 简介

* 一个用于 Python 编程语言的开源机器学习库
* 提供了一套高效的工具，用于数据挖掘、数据分析和机器学习应用的开发
* 主要通过简单易用的接口，封装了各种常见的机器学习算法，方便用户进行模型训练和预测
* 提供了大量的经典机器学习算法，包括但不限于：
  - 分类算法：如支持向量机 (SVM)、k 最近邻 (k-NN)、决策树、随机森林、逻辑回归等。
  - 回归算法：如线性回归、岭回归、Lasso回归等。
  - 聚类算法：如 K-means、DBSCAN、层次聚类等。
  - 降维算法：如主成分分析 (PCA)、线性判别分析 (LDA) 等。
  - 模型选择：如交叉验证、网格搜索等。

#### 数据集获取与使用

`sklearn.datasets` 提供了多种数据集加载方法，包括经典数据集、生成的假数据集和在线数据集等。通过 `sklearn.datasets` 模块可以直接加载这些数据集，返回的是一个 `Bunch` 对象，类似于一个字典，包含了特征、目标标签等数据。

常用内置数据集：

- `load_iris()`：鸢尾花数据集（常用于分类）
- `load_digits()`：手写数字数据集（常用于分类）
- `load_boston()`：波士顿房价数据集（常用于回归）
- `load_wine()`：红酒数据集（常用于分类）
- `load_breast_cancer()`：乳腺癌数据集（常用于分类）

常用生成数据集：

- `make_classification()`：生成分类数据集
- `make_regression()`：生成回归数据集
- `make_blobs()`：生成聚类数据集
- `make_moons()`：生成月亮形状的分类数据集
- `make_circles()`：生成圆形的分类数据集

常用在线数据集：

- `fetch_20newsgroups()`：20个新闻组数据集（文本分类）
- `fetch_openml()`：从 OpenML 加载任意数据集（支持各种数据集）

~~~python
"""
加载内置数据集
"""
from sklearn.datasets import load_iris, load_digits, load_boston

# 加载Iris数据集
iris = load_iris()
print(iris.keys())  # 查看数据集包含的字段
print(iris['data'].shape)  # 特征数据的形状
print(iris['target'].shape)  # 标签数据的形状

# 加载Digits数据集
digits = load_digits()
print(digits['data'].shape)  # 特征数据的形状
print(digits['target'].shape)  # 标签数据的形状

# 加载Boston房价数据集
boston = load_boston()
print(boston['data'].shape)  # 特征数据的形状
print(boston['target'].shape)  # 标签数据的形状
~~~

#### 特征提取&预处理

特征提取是将原始数据转换为适用于机器学习算法的格式的过程。常见的特征提取技术包括从文本、图像等非结构化数据中提取特征。Scikit-learn 提供了多种工具来进行特征提取，特征提取的方法可以根据数据的类型选择：

- 对于**文本数据**，常用的特征提取方法包括 `CountVectorizer` 和 `TfidfVectorizer`。
- 对于**图像数据**，可以使用 `extract_patches_2d` 提取图像块作为特征。
- 对于**数值数据**，可以使用标准化（`StandardScaler`）或归一化（`MinMaxScaler`）等方法来处理数据。

##### 字典特征提取

`sklearn` 中的 `DictVectorizer` 类专门用于将字典数据转换为稀疏矩阵格式。每个字典的键值对将被转化为特征的列，而字典的值则是该特征的值。该方法适用于处理每个样本包含不同键的情况，常见于处理类别数据。

~~~python
from sklearn.feature_extraction import DictVectorizer

# 示例字典数据
data = [
    {'color': 'red', 'price': 100},
    {'color': 'blue', 'price': 150},
    {'color': 'green', 'price': 200}
]

# 初始化 DictVectorizer
vectorizer = DictVectorizer(sparse=False)

# 将字典数据转换为特征矩阵
X = vectorizer.fit_transform(data)

print(X)
print(vectorizer.get_feature_names_out())

~~~

##### 文本特征提取

在文本处理中，通常我们需要将文本数据转换为数值特征，常见的做法是使用 `CountVectorizer` 和 `TfidfVectorizer`。这两种方法是最常用的文本特征提取方法。

`CountVectorizer`（词频向量化）将文本数据转换为词频矩阵（Term Frequency Matrix），每一行代表一个文档，每一列代表一个词（单词），每个单元格的值是该词在该文档中的出现频率。

```python
from sklearn.feature_extraction.text import CountVectorizer

# 示例文本数据
documents = [
    "I love programming in Python",
    "Python is a great programming language",
    "I love data science and machine learning"
]

# 创建 CountVectorizer 对象
vectorizer = CountVectorizer()

# 转换文本为词频矩阵，拟合模型，然后将文本数据转换为词频矩阵
X = vectorizer.fit_transform(documents)

# 查看词汇表（特征名），获取词汇表中包含的所有词汇
print("Feature names:", vectorizer.get_feature_names_out())

# 输出转换后的词频矩阵
print("Feature matrix:\n", X.toarray())
```

`TfidfVectorizer`（TF-IDF 向量化） 使用 TF-IDF（Term Frequency-Inverse Document Frequency）方法来表示文本数据。与词频矩阵不同，TF-IDF 考虑了单词在文档集中的重要性，通过降低常见词汇的权重来提高稀有但有意义的词的权重，**适合用于分类**。`TfidfVectorizer` 会自动计算每个单词的 TF-IDF 值，**用来衡量每个单词在文档中的重要性**。

词频（TF）：某一个给定词语在该文件中出现的频率。

逆向文档频率（IDF）：常见的计算 IDF 的公式是
$$
IDF = log\frac{N}{DF} 
$$
，其中`N`是文档的总数，`DF`是包含特定词汇的文档的数量。

```python
from sklearn.feature_extraction.text import TfidfVectorizer

# 创建 TfidfVectorizer 对象
tfidf_vectorizer = TfidfVectorizer()

# 转换文本为TF-IDF矩阵
X_tfidf = tfidf_vectorizer.fit_transform(documents)

# 查看词汇表（特征名）
print("Feature names:", tfidf_vectorizer.get_feature_names_out())

# 输出转换后的TF-IDF矩阵
print("TF-IDF matrix:\n", X_tfidf.toarray())
```

`TfidfTransformer` 是另一种文本特征提取工具，它将词频矩阵（如通过 `CountVectorizer` 获得的矩阵）转换为 TF-IDF 矩阵。

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# 创建 CountVectorizer 和 TfidfTransformer 对象
count_vectorizer = CountVectorizer()
tfidf_transformer = TfidfTransformer()

# 转换文本数据为词频矩阵
count_matrix = count_vectorizer.fit_transform(documents)

# 将词频矩阵转换为 TF-IDF 矩阵
tfidf_matrix = tfidf_transformer.fit_transform(count_matrix)

# 查看转换后的 TF-IDF 矩阵
print("TF-IDF matrix:\n", tfidf_matrix.toarray())
```

##### 图像特征提取

Scikit-learn 提供了 `sklearn.feature_extraction.image` 模块来从图像中提取特征。常见的任务是将图像转换为固定大小的特征矩阵，用于机器学习模型。

`extract_patches_2d` 可以从图像中提取固定大小的图像块。

```python
from sklearn.feature_extraction.image import extract_patches_2d
from skimage import data

# 加载示例图像（可以是灰度图像）
image = data.astronaut()

# 提取 5x5 的图像块
patches = extract_patches_2d(image, patch_size=(5, 5))

# 查看提取到的图像块的形状
print("Number of patches:", patches.shape[0])
print("Shape of each patch:", patches.shape[1:])
```

##### 数值特征提取

对于传统的结构化数据，通常我们会使用一些方法对数值特征进行标准化、归一化、缩放等处理，以便更好地适应机器学习模型。Scikit-learn 提供了多种预处理工具来进行特征提取。

`StandardScaler`（特征缩放） 是一种常用的特征缩放方法，会根据训练集的均值和标准差对数据进行标准化处理，使得每个特征的均值为 0，方差为 1。它通过去除均值并缩放到单位方差来标准化特征。

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

# 示例数据
X = np.array([[1, 2], [3, 4], [5, 6]])

# 创建 StandardScaler 对象
scaler = StandardScaler()

# 拟合并转换数据
X_scaled = scaler.fit_transform(X)

# 查看标准化后的数据
print("Scaled features:\n", X_scaled)
```

`MinMaxScaler`（特征归一化） 将特征缩放到指定的最小值和最大值（通常是 [0, 1] 之间），适用于需要特征按比例缩放的情况。

```python
from sklearn.preprocessing import MinMaxScaler

# 创建 MinMaxScaler 对象
scaler = MinMaxScaler()

# 拟合并转换数据
X_normalized = scaler.fit_transform(X)

# 查看归一化后的数据
print("Normalized features:\n", X_normalized)
```

#### 特征选择

# 深度学习

## 概述

1. 行业应用
   * 视觉：人脸识别技术
   * 语音：语音识别、舆情分析

## 框架

### PyTorch

官网：http://pytorch.org/

PyTorch由 Facebook开发，以其直观 的API和动态计算图而受到研究人员的青睐。它支持 GPU加速，适用于快速原型开发。
PyTorch以其易用性和灵活性而著称，特别适合于研究和开发，当需要频繁更改模型时尤其有用。

### Tensorflow

官网：http://tensorflow.org/

TensorFlow由Google开发，以其强大的扩展性和生产环境的支持而广泛应用于工业界。TensorFlow不仅支持深度学习，还支持广泛的机器学习算法。
TensorFlow则在大规模部署和生产环境中更为流行，特别是当需要高效的模型服务和分布式训练时。

## 应用

### 图像识别

### 自然语言处理（NLP）

### 推荐系统

# 大模型

参考：

* https://www.bilibili.com/video/BV1D7o9YJEYx/?spm_id_from=333.1007.tianma.2-2-4.click&vd_source=fabefd3fabfadb9324761989b55c26ea

## 概述

1. 定义

   大模型是指那些具有**大量参数和强大计算能力**的人工智能模型。这些模型通常由数十亿甚至数千亿个参数构成，能够处理和分析大规模的数据集。大模型在模式识别、自然语言处理和生成任务方面表现出色，因为它们可以捕捉到复杂的数据特征和关系。GPT系列是大模型的典型代表，它们通过大规模的数据预训练，能够执行多种语言理解和生成任务。

2. 作用

   **大模型的应用推动了人工智能从单纯的数据处理走向创意和艺术的领域，拓宽了人工智能在娱乐艺术和媒体行业中的应用。这些创新不仅展示了技术的进步，还促进了人类与机器之间交互方式的转变。**

3. 特点

4. 应用场景

   * 生成式AI：理解分析数据生成新的文本、图像、音乐等
     * 智能写作
     * 智能阅读助手

5. 类型

   * 内容
     * 判别式模型（Discriminative AI）：专注于学习输入数据的特征与标签之间的关系，适用于分类任务，但对数据要求和计算资源较高。
     * 生成式模型（Gen AI）：可以学习数据的潜在分布，适用于生成新的数据实例，但对数据要求更高，需要更多的样本和计算量。
       * 语言类Gen AI的典型代表-大语言模型（通义千问）
       * 图像类Gen AI的典型代表-潜在扩散模型（Stable Diffusion）
     
     > 在二分类任务中，判别式模型性能一般不如生成式模型，但生成式模型在分类任务上具有更高的准确率。
   * 提问
     * 指令模型
     * 推理模型

6. 主流大模型

   * GPT
     * 取 Transformer的 Decoder搭建的纯 Decoder 架构 
   * LLaMA2
     * 主流的开源模型架构
     * 在 GPT的基础上改进了位置编码、注意力计算和激活函数
     * 具有强大的指令理解和文本生成能力
   * 通义千问
     * 阿里开源的大语言模型
     * 基于 LLaMA 结构进行中文预训练+指令微调
     * 在多个数据集上展现出接近 GPT-4 的水平
   
7. 学习思路

   * 了解常见大模型及其各自特点
   * 学习如何使用各类大模型应用
   * 学习如何快速搭建开发大模型应用
   
8. AI外部能力接入

   * 视觉派：以屏幕识别为主，模拟人类操作。典型代表有：`OmniParser`、`CogAgent`
   * 软件派：直接从底层编写程序、调用程序、调用功能、执行操作。典型代表有：`Function calling`、`LangChain`、`AutoGpt`
   
9. 相关概念

   * promot：提示词，可以分为系统提示词（角色、性格、背景、语气）和用户提示词
   * agent：在模型、工具和用户之间进行协调的程序
   * FunctionCalling
   * MCP：

### Transformer

1. 简介

   * Transformer是目前 LLM 的基础架构
   * 几乎所有 LLM 都是基于 Transformer架构搭建的
   * 自然语言处理领域的绝对主流

2. 应用（基于 Transformer架构的模型）

   | 模型大类          | 代表模型             |
   | ----------------- | -------------------- |
   | 自回归模型        | GPT、LLaMA、通义千问 |
   | 自编码模型        | BERT、MacBERT        |
   | 编码器-解码器模型 | T5                   |
   | 通用语言模型      | GLM                  |

## Promot

### 简介

1. 本质：**提示词的本质就是表达。或者说如何提出好问题，如何提好问题**
2. 关键问题：
   * 是否理清了脑海中的想法
   * 是否能够通过文字准确传达这个想法
3. 使用技巧
   * 可以使用**乔哈里视窗**给AI提供足够多的背景信息
   * 可以视情况而定是否指定AI的思考步骤
   * 适时进行追问、提出意见和辩驳
   * 可以一定程度使用提示词模板，提高提问效率，比如角色设定、思维链提示、给定示例等（Deepseek R1可以最相关与设定）

### 使用

1. 提问范式：你是谁+背景信息+目标
2. 注意事项
   * 上下文记忆有限
   * 输出长度有限
   * 适时开启新对话

### 案例

1. 创建prompt

   我想让你成为我的 Prompt 创作者。你的目标是帮助我创建最佳的 Prompt，这个 Prompt 将由你ChatGPT 使用。你将遵循以下过程:
   1.首先，你会问我 Prompt 是关于什么的。我会告诉你，但我们需要通过不断的重复来改进它，通过则进行下一步。
   2.根据我的输入，你会创建三个部分:
   	a)修订后的 Prompt(你编写修订后的 Prompt，应该清晰、精确、易于理解)

   ​	b)建议(你提出建议，哪些细节应该包含在 Prompt 中，以使其更好)
   ​	c)问题(你提出相关问题，询问我需要哪些额外信息来改进Prompt)

   3.你提供的修订后的 Prompt 应该采用我发出请求的形式，最后由ChatGPT 执行
   4.我们将继续这个迭代过程，我会提供更多的信息，你会更新“修订后的Prompt”部分的请求，直到它完整为止。

2. 用prompt寻求最佳解决方案

   你需要应用连续问题解决系统 (CPSS)来通过不断重复寻找我的问题，并通过深度解析后提供解决方案。

   CPSS的工作原理如下:
   1.你将采用六个步骤的问题解决过程来评估我的初始问题:

   ​	1)确定问题 

   ​	2)定目标

   ​	3)生成决方案(最多3个)

   ​	4)评估并选择解决方案

   ​	5)实施解决方案 

   ​	6)下一个问题

   2.在“生成解决方案”的步骤中，应列出最多3个解决方案，在“评估和选择解决方案”的步骤中，应提供精确和具体的解决方案。在“实施解决方案”的步骤中，应提供所选解决方案付诸实施的具体方法。

   3.“下一个问题"部分应包含你可以向我提出的最重要的问题，以获取进一步的信息，这些信息对于问题解决过程的继续非常重要。每个问题的数量最多为3个。
   4.你的回答应该简洁明了，使用Markdown格式撰写，其中每个步骤的名称以粗体显示，并且所有文字包括标签的字体大小应具有一致性。
   5.在你回答了我的第一个问题之后，CPSS过程的下一个迭代开始。
   6,系统将整合我的最后一个回答，并通过每个迭代逐渐提供更加深入的回答，你可以通过向我提出新的问题来引导它。
   你的第一个回答应该只是一个问候，提醒对方你是一个连续问题解决系统(CPSS)。不要在第一个回答中开始CPSS过程，你的第一个回答只包括问候和要求提出的要解决的问题。之后，我会为你提供信息，请在你的下一个回答中开始CPSS过程。

3. “新技能”学习prompt

   > 公式：赋子身份 + 设定目标 + 高效阅读 + 规避错误 + 学习评测

   * 举例：以学习”投资理财“为案例

     你是投资理财领域的专家，我计划学习投资理财技能，希望你成为我的导师;请回答“是”，并保持静默状态以示确认。

     ___

     如果我希望在两周内能够初步掌握投资理财技能，并应用在实际工作生活中，请为我制定一个详细的两周学习计划表;我可以每周学习5天，每天学习90分钟。

     ___

     我是一个初学者，请帮我列出最适合我的10部投资理财类书籍，以及推荐理由。

     ___

     我相信人们学习投资理财知识，会经常犯一些错误，请为我列举出学习过程中，可能遇见的常见问题或易犯错误都有哪些?

     ___

     你是我的投资理财课程导师，我是一名初学者，你可以测试我一些关于投资理财的知识吗?

## ChatGPT

官网：https://openai.com/

### 简介

1. ChatGPT：OpenAI在2022年11月30日发布的一款全新聊天机器人模型。
2. 特点
   * 对话方式进行交互
3. 应用场景
   * 代码相关：代码优化，程序解释，代码生成
   * 职业相关：创作短故事、产品设计
   * 日常生活相关：语言翻译等

### 使用

> 使用ChatGPT的目标不是直接获得答案，而是聚焦诉求，然后通过GPT个性化输出，提供更加完善全面的问题解决思路和方案。

参考：[ChatGPT从入门到进阶教程合集](https://www.bilibili.com/video/BV158411r73U?spm_id_from=333.1245.0.0)

提问格式：

> 指令词（instruction）+背景（context）+输入（input）+输出要求（output indicators）

1. 指令词：精准任务或命令
   * 例如:“简述”、“解解”、“翻译”、“总结或“润色”等
2. 背景：补充信息
   * 例如:简述一篇讲解世界名画的文章，是写给小学生还是艺术系的大学生?
   * 角度：
     * 职业/角色
     * 具体兴趣
     * 价值观/原则
     * 学习风格
     * 个人背景
     * 目标
     * 偏好
     * 主要语言
     * 专业知识
     * 沟通风格
3. 输入：输入数据或具体内容
   * 例如:将所有的评论内容，提炼出30个关键词
4. 输出
   * 例如:“用50字以内简述”或“请按以下格式回答:步骤一、步骤二。..”
   * 角度：
     * 回复格式：列表、表格、markdown
     * 语气
     * 详细程度
     * 建议类型
     * 问题类型
     * 资源参考核查
     * 批判性思维
     * 创意水平
     * 解决问题方法
     * 偏见意识
     * 语言偏好

## DeepSeek

> R1是从“操作手册”到“使用手册”的转变

官网：https://www.deepseek.com/

参考：

* https://alidocs.dingtalk.com/i/nodes/NkDwLng8ZQ6mY37xSYq72wyXJKMEvZBY?utm_scene=team_space
* https://www.bilibili.com/video/BV1uqKGeZEy1?spm_id_from=333.1245.0.0

推荐三方服务平台：

* 秘塔搜索
* 硅基流动
* 腾讯元宝

## 智能体

Java+SpringAI/LangChain/LangChain4J+MCP==>AI智能项目落地

1. MCP：
   * Agent与其他工具间的交互，调用外部工具、API、访问数据库、执行代码等
2. A2A：
   * Agent与Agent（或用户)之间交互，理解其他Agent的意图、协同完成任务，与用户进行自然对话

## MCP

1. 概念

# AI应用

## 语言类

### ChatGPT+

### 基础办公应用

1. ChatDOC
   * 网址：https://chatdoc.com/
2. ChatExcel
3. ChatPPT
   * 网址：https://www.chat-ppt.com/
4. ChatPDF

## 图像类

参考：

* https://www.bilibili.com/read/cv22159609/
* https://www.bilibili.com/read/cv21362202/

### Stable Diffusion

参考：

* https://www.bilibili.com/video/BV1iM4y1y7oA
* [万字保姆级教程！Stable Diffusion完整入门指南](https://baijiahao.baidu.com/s?id=1765945330332903494&wfr=spider&for=pc)

1. 简介

   Stable Difusion(稳定扩散)是一款于2022年发布的基于 difusion技术的**文本到图像生成深度学习模型**，主要由 StabilityAI 公司开发并开源。该模型主要用于根据文本描述生成详细的图像，同时也可应用于其他任务，如修复图像、扩展图像以及生成图像到图像的转换。

   Stable Difusion是当下最为流行的扩散模型，代码和模型权重已经开源，并且可以在大多数配备至少4GBVRAM的消费级硬件上运行。当前围绕着stable Difusi0n已,经形成了一套流行而成大的图像生成社区，涌现出许多优秀的第三方模型。Stable Difusi0n共有多个版本，其中最流行的是 SD1.5模型，目前模型编号已经更新到Srable Diffusi0nⅪ，它拥有更高的质量和生成分辩率。

2. 扩散模型

   Difusion Model(扩散模型)是一类生成式模型，和 VAE(变分自编码器),GAN(生成对抗网络)等生成网络不同的是，扩散模型在前向阶段对图做逐步施加噪声，直至图像被破坏变成完全的高斯噪声(训练时)，然后在逆向阶段学习从高斯噪声还原为原始图像(推理时)。

   由于扩散模型能够很好的根据引导信息还原图像，现如今扩散模型已经应用于各种生成任务，如图、语音、3D形状和图形合成。具体来说，扩散模型的前向阶段在原始图像上逐步增加噪声，每一步得到的只和上一步的结果以及时间步和引导信息(如文字orompt)相关，直至变为纯高斯噪声；而逆向阶段则是不断去除噪声的过程，首先给定高斯噪声通过逐步去噪，直至最终将原图像恢复出来。模型训练完成后，只要给定高斯随机噪声,就可以生成一张从未见过的图像。

### Midjourney

### LibLibAI

LibLibAI：https://www.liblib.art/

## 应用开发

开源项目：[AIFlowy](https://gitee.com/aiflowy/aiflowy)

AI应用搭建的核心组成部分，包括foundational model和AI tools。

1. model选用与获取：在主流的模型榜单和开源的测评平台，了解了当前最流行的模型和其评分指标，如下是常用的model获取平台：
   * [Huggingface](https://huggingface.co/)（镜像：https://hf-mirror.com/）
   * [OpenCompass](https://opencompass.org.cn/home)
   * [魔搭ModelScope](https://modelscope.cn/home)
2. 常用评测指标
   * ARC：ARC 数据集包含 7,787 个科学考试问题，这些问题来自各种来源，包括与 AI2 附属的研究合作伙伴提供的科学问题。这些问题是仅文本的英语语言考试问题，跨越了多个年级水平。
   * Hello swag：HellaSwag 是一个用于评估常识自然语言推理的挑战性数据集，它对于目前的最先进的模型来说非常困难，但是对于人类来说却很容易(>95%的准确率)。它包含了70000个多选问题，每个问题都有一个场景和四个可能的结局，要求选择最合理的结局。
   * MMLU：MMLU 是一个庞大的多任务数据集，由各种学科的多项选择顺组成。其涵盖了人文学科、社会科学、自然科学和其他对某些人学习很重要的领域。其中包括57个任务，包括初等数学、美国历史、计算机科学、法律等等。为了在这个测试中达到高准确度，模型必须具有广泛的世界知识和问题解决能力。
   * TruthfulQA：TruthfulQA是一个用于衡量语言模型在回答问题时是否真实的基准。该基准包括817个问题，涵盖了38个类别，包括健康、法律、金融和政治等领域。这些问题是作者精心设计的，一些人类可能会因为错误的信念或误解而回答错误。根据研究，最好的模型在58%的问题上回答是真实的，而人类的表现是94%。
3. 应用范式
   * 小模型应用开发范式
     * 准备数据
     * 配置模型
     * 模型训练（输入、损失、训练）：数据打标、监督学习、模型微调、模型评估、模型部署
   * 大模型应用开发范式：以LLM为中心
     * LLM的局限性
       * 知识时效性受限：如何让LLM能够获取最新的知识
       * 专业能力有限：如何打造垂域大模型
       * 定制化成本高：如何打造个人专属的LLM应用
     * Pretrain-Finetune范式
     * RAG--检索增强生成

### Streamlit

# Java + AI

### 一、基础框架类



1. Spring AI Alibaba简介：阿里云推出的Java AI开发框架，基于Spring AI构建，无缝集成通义系列大模型，提供高阶API抽象和云原生支持，适合快速构建企业级AI应用[⁠⁣ ⁠⁣](https://www.jianshu.com/p/06709e66b6cd)[2](https://www.jianshu.com/p/06709e66b6cd)[⁠⁣ ⁠⁣](https://www.cnblogs.com/alisystemsoftware/p/18506747)[13](https://www.cnblogs.com/alisystemsoftware/p/18506747) 。特点：支持模型微调、RAG（检索增强生成）、本地部署等，是Java领域对接大模型的最佳实践[⁠⁣ ⁠⁣](https://m.bilibili.com/video/BV11MdAY8EpP/)[10](https://m.bilibili.com/video/BV11MdAY8EpP/)[⁠⁣ ⁠⁣](https://www.cnblogs.com/alisystemsoftware/p/18506747)[13](https://www.cnblogs.com/alisystemsoftware/p/18506747) 。
2. Spring AI定位：Spring生态的AI工程化框架，提供统一的API接口，简化AI功能集成（如自然语言处理、图像分析）[⁠⁣ ⁠⁣](https://javaguide.cn/open-source-project/machine-learning.html)[1](https://javaguide.cn/open-source-project/machine-learning.html)[⁠⁣ ⁠⁣](https://m.bilibili.com/video/BV11MdAY8EpP/)[10](https://m.bilibili.com/video/BV11MdAY8EpP/) 。适用场景：结合Spring Boot开发智能Web服务或自动化工具[⁠⁣ ⁠⁣](https://javaguide.cn/open-source-project/machine-learning.html)[1](https://javaguide.cn/open-source-project/machine-learning.html)[⁠⁣ ⁠⁣](https://m.bilibili.com/video/BV11MdAY8EpP/)[10](https://m.bilibili.com/video/BV11MdAY8EpP/) 。

------



### 二、深度学习与模型开发



1. Deep Java Library (DJL)背景：由Amazon开发的高性能开源库，支持加载和训练PyTorch、TensorFlow等主流框架的模型，提供Java原生API[⁠⁣ ⁠⁣](https://developer.baidu.com/article/details/3350266)[3](https://developer.baidu.com/article/details/3350266)[⁠⁣ ⁠⁣](https://bbs.huaweicloud.com/blogs/446098)[9](https://bbs.huaweicloud.com/blogs/446098) 。应用：适合图像识别、自然语言处理任务，支持本地与云端模型部署[⁠⁣ ⁠⁣](https://bbs.huaweicloud.com/blogs/446098)[9](https://bbs.huaweicloud.com/blogs/446098)[⁠⁣ ⁠⁣](https://www.atguigu.com/news/17110)[16](https://www.atguigu.com/news/17110) 。
2. Jlama特点：Meta开源的Java深度学习库，专为模型训练和推理设计，提供丰富的工具链，支持动态计算图[⁠⁣ ⁠⁣](https://m.blog.csdn.net/2301_78858041/article/details/146203984)[15](https://m.blog.csdn.net/2301_78858041/article/details/146203984) 。优势：适合需要高性能计算的场景（如IoT数据分析）[⁠⁣ ⁠⁣](https://m.php.cn/faq/915152.html)[7](https://m.php.cn/faq/915152.html)[⁠⁣ ⁠⁣](https://m.blog.csdn.net/2301_78858041/article/details/146203984)[15](https://m.blog.csdn.net/2301_78858041/article/details/146203984) 。
3. Deeplearning4j (DL4J)功能：分布式深度学习框架，支持神经网络构建、GPU加速，与Hadoop/Spark生态集成，适合大数据分析场景[⁠⁣ ⁠⁣](https://baijiahao.baidu.com/s?id=1826268182279762561)[8](https://baijiahao.baidu.com/s?id=1826268182279762561)[⁠⁣ ⁠⁣](https://m.blog.csdn.net/qq_29581535/article/details/147124176)[12](https://m.blog.csdn.net/qq_29581535/article/details/147124176)[⁠⁣ ⁠⁣](https://m.php.cn/faq/830705.html)[18](https://m.php.cn/faq/830705.html) 。

------



### 三、机器学习与数据处理



1. Weka定位：经典的开源机器学习库，提供分类、聚类、回归等算法，内置数据预处理工具，适合入门级AI开发[⁠⁣ ⁠⁣](https://m.php.cn/faq/823650.html)[4](https://m.php.cn/faq/823650.html)[⁠⁣ ⁠⁣](https://m.php.cn/faq/893311.html)[6](https://m.php.cn/faq/893311.html)[⁠⁣ ⁠⁣](https://m.php.cn/faq/830705.html)[18](https://m.php.cn/faq/830705.html) 。学习价值：结合Java实现数据挖掘全流程，如用户行为分析、推荐系统[⁠⁣ ⁠⁣](https://m.php.cn/faq/823650.html)[4](https://m.php.cn/faq/823650.html)[⁠⁣ ⁠⁣](https://m.php.cn/faq/893311.html)[6](https://m.php.cn/faq/893311.html) 。
2. Apache Mahout适用场景：面向大规模数据集的机器学习，支持分布式计算，与Hadoop集成，适合推荐算法开发[⁠⁣ ⁠⁣](https://m.php.cn/faq/830705.html)[18](https://m.php.cn/faq/830705.html) 。

------



### 四、工具库与扩展



1. OpenCV for Java功能：计算机视觉核心库，支持图像处理、人脸检测、视频分析等，常与DJL或TensorFlow结合实现AI视觉应用[⁠⁣ ⁠⁣](https://developer.baidu.com/article/details/3350266)[3](https://developer.baidu.com/article/details/3350266)[⁠⁣ ⁠⁣](http://www.atguigu.com/news/17092)[11](http://www.atguigu.com/news/17092) 。
2. TensorFlow for Java特点：Google官方提供的Java接口，支持模型推理和有限训练，适合已有Python模型需迁移到Java的场景[⁠⁣ ⁠⁣](https://m.php.cn/faq/823650.html)[4](https://m.php.cn/faq/823650.html)[⁠⁣ ⁠⁣](https://m.php.cn/faq/813197.html)[17](https://m.php.cn/faq/813197.html) 。
3. LangChain4j用途：专为Java设计的AI应用开发工具链，支持RAG、多模态提示工程（MCP），适合构建智能问答系统[⁠⁣ ⁠⁣](https://m.bilibili.com/video/BV11MdAY8EpP/)[10](https://m.bilibili.com/video/BV11MdAY8EpP/) 。

## LangChain4j

Github：[langchain4j/langchain4j: Java version of LangChain](https://github.com/langchain4j/langchain4j)

文档：[LangChain4j | LangChain4j](https://docs.langchain4j.dev/)

中文文档：[介绍 | LangChain4j 中文文档](https://docs.langchain4j.info/intro)

# 路线&资源

## 书籍

* 《机器学习》- 周志华
* 《统计学方法》- 李航
* 《深度学习》

## 资源

* [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners)
* [huggingface/transformers](https://github.com/huggingface/transformers/tree/main/examples)
* [Stanford CS324 LLM Course](https://github.com/mlfoundations/cs324)
* [OpenBMB/Tutorials](https://github.com/OpenBMB/Tutorials)
* [full-stack-deep-learning/llm-bootcamp](https://github.com/full-stack-deep-learning/llm-bootcamp)
* [deeplearning-ai LLM Courses](https://github.com/deeplearning-ai)
* [microsoft/LLM-Practical-Guide](https://github.com/microsoft/LLM-Practical-Guide)
* [动手学大模型应用开发](https://github.com/datawhalechina/llm-universe)
* [AI Agents for Beginners - A Course](https://github.com/microsoft/ai-agents-for-beginners)
* [开源大模型食用指南](https://github.com/datawhalechina/self-llm)
* https://machinelearningmastery.com/

| 项目名称                      | 特点                           | 核心内容                            | 适用阶段   | 项目地址                                                     |
| ----------------------------- | ------------------------------ | ----------------------------------- | ---------- | ------------------------------------------------------------ |
| HuggingFace Transformers      | 官方多模态教程，Colab集成      | 文本分类/生成、模型微调与部署       | 入门到进阶 | [Github](https://github.com/huggingface/transformers)        |
| Stanford CS324                | 顶尖高校课程，理论实践结合     | Transformer实现、RLHF技术、推理优化 | 系统学习   | [Github](https://github.com/mlfoundations/cs324)             |
| OpenBMB Tutorials             | 中文大模型技术栈，国产模型实践 | MiniGPT实现、分布式训练、高效微调   | 中文开发者 | [Github](https://github.com/OpenBMB/Tutorials)               |
| LLM Bootcamp                  | 全栈开发训练营，真实业务场景   | RAG优化、多模型路由、知识问答系统   | 工程化实践 | [Github](https://github.com/full-stack-deep-learning/llm-bootcamp) |
| DeepLearning.AI Short Courses | 吴恩达团队短课，Jupyter实践    | Prompt工程、模型微调、系统构建      | 快速上手   | [Github](https://github.com/deeplearning-ai)                 |
| LLM Practical Guide           | 企业级方案，Azure集成          | 架构设计模式、成本控制、安全防护    | 企业部署   | [Github](https://github.com/microsoft/LLM-Practical-Guide)   |
| Prompt Engineering Guide      | 系统化提示手册，领域模板       | 基础技巧→高级模式→自修正策略        | 全阶段     | [Github](https://github.com/dair-ai/Prompt-Engineering-Guide) |
| AI For Beginners              | 微软12周课程，多语言支持       | 大模型专题+伦理讨论+行业应用        | 系统入门   | [Github](https://github.com/microsoft/AI-For-Beginners)      |

项目选择建议：

1. **快速上手** → 从 **HuggingFace教程** 或 **DeepLearning.AI短课** 开始
2. **系统学习** → **Stanford CS324** 或 **微软12周课程**
3. **中文友好** → **OpenBMB教程** 或 **datawhalechina项目**
4. **企业实践** → **LLM Bootcamp** 或 **微软实用指南**

~~~mermaid
graph TD
    A[学习目标] --> B{方向选择}
    B -->|理论研究| C[Stanford CS324]
    B -->|应用开发| D[LLM Bootcamp]
    B -->|中文场景| E[OpenBMB]
    C --> F[精读论文+复现代码]
    D --> G[构建RAG系统]
    E --> H[领域模型微调]
~~~



## 社区

* [Huggingface](https://huggingface.co/)：Hugging Face作为一个开源社区，为机器学习领域的专家和爱好者提供了一个共享、探索和合作的平台，推动着机器学习技术的发展和进步。在HuggingFace开源社区上我们可以找到模型各个指标的榜单排名。
  * [镜像](https://hf-mirror.com/)
  * [使用教程](https://www.bilibili.com/video/BV1KTQcYUEeT/?t=9&spm_id_from=333.1007.tianma.1-2-2.click&vd_source=fabefd3fabfadb9324761989b55c26ea)
* [OpenCompass](https://opencompass.org.cn/home)：Opencompass 是一款开源、高效、全面的评测大模型体系及开放平台。提供完整开源可复现的评测框架，支持站式评测。
* [魔搭ModelScope](https://modelscope.cn/home)

## 路线

* https://developer.aliyun.com/learning/roadmap/ai
* https://www.bilibili.com/opus/367926006888018872?from=articleDetail

三大阶段：

* 基础技能
* 大模型技术
* 工程化实践

1. Python快速掌握
   * 重点库：NumPy/Pandas（数据处理）、Requests（API调用）、FastAPI/Flask（Web服务）
2. 机器学习基础
   * 核心概念：监督学习/非监督学习、评估指标、特征工程
   * 实践工具：Scikit-learn（用Python实现经典算法）
3. 深度学习基础
   * 核心框架：PyTorch（动态图更符合Java开发者思维）
   * 关键实践：手写数字识别、简单文本分类
4. Transformer架构
   * 核心突破：Self-Attention机制、位置编码
   * 实践建议：用PyTorch实现简化版Transformer
5. 大模型生态&微调
   * 商业API：OpenAI GPT系列、文心一言API调用
   * 开源模型：LLaMA2微调、LoRA/P-Tuning高效微调、ChatGLM本地部署
   * 工具链：LangChain（应用开发框架）
   * 实践项目：使用Alpaca数据集微调LLaMA
6. 模型服务化
   * 部署方案：
     * Triton Inference Server（高并发场景）
     * FastAPI+Transformer（轻量级服务）
     * 性能优化：模型量化（bitsandbytes）、注意力优化（FlashAttention）
   * 架构设计
     * Java工程化集成：
       * Spring Boot对接Python服务（gRPC/HTTP）
       * 分布式推理集群管理（结合Java微服务经验）
     * 扩展方案：
       * 模型版本管理（MLflow）
       * 请求编排（Cadence/Temporal工作流引擎）