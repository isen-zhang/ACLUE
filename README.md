<img src="fig/ACLUE.png" align="right" width="250" />

# ACLUE---古汉语语言理解评估基准 


<h4 align="left">
    <p>
        <b>简体中文</b> |
        <a href="README_EN.md">English</a> 
    <p>
</h4>

<p align="left" style="display: flex; flex-direction: row; justify-content: center; align-items: center">
📄 <a href="https://arxiv.org/abs/2310.09550" target="_blank" style="margin-right: 15px; margin-left: 10px">论文</a> • 
🏆 <a href="#排行榜" target="_blank"  style="margin-left: 10px">排行榜</a> •
🤗 <a href="https://huggingface.co/datasets/tyouisen/aclue" target="_blank" style="margin-left: 10px">数据集</a> 
</p>

## 简介


Ancient Chinese Language Understanding Evaluation (**ACLUE**) 是一个面向古代汉语的评估基准，旨在帮助评估大型语言模型在古代汉语上的表现。基准由 15 个任务组成，涵盖了多个领域，句法、语义、推理和知识等。我们鼓励研究者使用 ACLUE 来测试和改进模型在古代汉语方面的能力。
ACLUE的任务取自人工挑选的公开资源和自动生成的古代汉语语料库，这些问题涵盖了从夏朝（公元前2070年）到明朝（公元1368年）的广泛时间范围。ACLUE在所有任务中都采用了多项选择题的形式。

## 排行榜 🏆

下表呈现了模型在 zero-shot 下的表现。如果您希望贡献您的模型结果，请与我们联系或直接提交拉取请求。

#### Zero-shot
| 模型                                                      |   词汇   |   句法   |   语义   |   推理   |   知识   |   平均值   |
|-----------|---------|-----------|----------|-----------|-----------|---------|
| [ChatGLM2-6B](https://huggingface.co/tiiuae/falcon-40b)   |   34.00   |   38.00   |   39.90   |   36.53   | **38.85** | **37.34** |
| [ChatGPT](https://openai.com/chatgpt)                     | **34.53** | **43.00** |   36.40   | **41.23** |   33.61   |   36.82   |
| [BLOOMZ-7B](https://github.com/bigscience-workshop/xmtf)  |   34.40   |   32.20   | **43.70** |   30.19   |   37.31   |   35.34   |
| [ChatGLM-6B](https://github.com/THUDM/GLM-130B)           |   32.80   |   36.60   |   30.50   |   34.59   |   32.81   |   33.23   |
| [Falcon-40B](https://huggingface.co/tiiuae/falcon-40b)    |   30.13   |   32.60   |   34.30   |   33.65   |   30.78   |   32.00   |
| [Baichuan-7B](https://github.com/baichuan-inc/baichuan-7B)|   28.00   |   32.20   |   32.80   |   30.40   |   34.56   |   31.75   |
| [LLaMA-65B](https://github.com/facebookresearch/llama)    |   28.33   |   33.00   |   29.60   |   29.10   |   27.56   |   28.76   |
| [MOSS-SFT-16B](https://github.com/OpenLMLab/MOSS)         |   28.00   |   24.00   |   27.50   |   27.42   |   24.34   |   26.29   |
| Random                                                    |   25.00   |   25.00   |   25.00   |   25.00   |   25.00   |   25.00   | 

对于每一类任务具体所含有的任务如下：

词汇（T1：古文单字多义，T2：通假字，T3：古汉语命名体识别），句法（T4：古文断句），语义（T5：对联，T6：古诗词上下句预测），推理（T7：古诗词质量评估，T8：古文阅读理解，T9：古诗词曲鉴赏，T10：诗词情感分类），知识（T11：古汉语知识，T12：国学常识，T13：医古文，T14：古代文学知识，T15：古音学）。

## 数据格式
数据集中的每个问题都是一个多项选择题，有4个选项，只有一个选项是正确答案。数据以逗号分隔的.csv文件形式存在。数据可以在以下位置找到：[data](data)。

这里是数据格式的示例：

```
“会当凌绝顶，一览众山小”是杜甫的名句，诗人登上了哪座山发出了这样的感慨？（）,五台山,黄山,泰山,衡山,C
```


## 数据
我们根据每个主题在[data/dev](data/dev)和[data/test](data/test)目录中提供了开发和测试数据集。


## 提示
我们在`src/utils`目录中提供了预处理代码。

以下是添加直接回答提示后的数据示例：

```
    以下是关于{古诗词曲鉴赏}的单项选择题，请直接给出正确答案的选项。
    题目：《木兰诗--北朝民歌》唧唧复唧唧,木兰当户织。不闻机杼声,唯闻女叹息。问女何所思,问女何所忆。女亦无所思,女亦无所忆。昨夜见军帖,可汗大点兵,军书十二卷,卷卷有爷名。阿爷无大儿,木兰无长兄,愿为市鞍马,从此替爷征。东市买骏马,西市买鞍鞯,南市买辔头,北市买长鞭。旦辞爷娘去,暮宿黄河边,不闻爷娘唤女声,但闻黄河流水鸣溅溅。旦辞黄河去,暮至黑山头,不闻爷娘唤女声,但闻燕山胡骑鸣啾啾。万里赴戎机,关山度若飞。朔气传金柝,寒光照铁衣。将军百战死,壮士十年归。归来见天子,天子坐明堂。策勋十二转,赏赐百千强。可汗问所欲,木兰不用尚书郎,愿驰千里足,送儿还故乡。爷娘闻女来,出郭相扶将;阿姊闻妹来,当户理红妆;小弟闻姊来,磨刀霍霍向猪羊。开我东阁门,坐我西阁床。脱我战时袍,著我旧时裳。当窗理云鬓,对镜帖花黄。出门看火伴,火伴皆惊忙:同行十二年,不知木兰是女郎。雄兔脚扑朔,雌兔眼迷离;双兔傍地走,安能辨我是雄雌?下列对这首诗的理解和分析,不正确的一项是 ()
    A.  《木兰诗》是南北朝时期的一首长篇叙事民歌,风格刚健质朴。全诗以“木兰是女郎”来构思木兰的传奇故事,富有浪漫色彩。
    B.  “愿为市鞍马”的“市”是“市场”的意思,“万里赴戎机”的“戎机”是“战事”的意思。
    C.  木兰“不用尚书郎”而愿“还故乡”固然有对家乡的眷恋,但也有自己女儿身秘密的因素。
    D.  “朔气传金柝,寒光照铁衣”运用对偶手法,描写了木兰在边塞艰苦的军旅生活。
    答案是：B
    

    ... [其他例子] 

    题目：《虞美人》李煜。春花秋月何时了？往事知多少。小楼昨夜又东风，故国不堪回首月明中。雕栏玉砌应犹在，只是朱颜改。问君能有几多愁？恰似一江春水向东流。对《虞美人》的赏析,不恰当的一项是（）
    A. 词作从眼前景物入手,生发联想和想像,追怀昔日帝王生活,描摹了一幅幅鲜活的画面,隐晦地表达出叛逆之情,惹恼了宋太宗,铸成了词人悲惨结局。
    B. 词作以实虚相间的手法来绘景、抒情、达意,忽而写眼前,忽而写想像。
    C. 《虞美人》乃李煜绝笔词
    D. 《虞美人》以其形式别致给人美感愉悦。
    答案是：

```

## 评估
我们使用的每个模型的评估代码位于[src](src)中，运行它们的代码列在[script](script)目录中。

## 引用

```
Zhang, Yixuan, and Haonan Li. "Can Large Langauge Model Comprehend Ancient Chinese? A Preliminary Test on ACLUE." Proceedings of the Ancient Language Processing Workshop. 2023.
```
## 许可证

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

本项目采用 [MIT License](https://lbesson.mit-license.org/).

[![CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

ACLUE数据集采用
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).


