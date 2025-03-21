以下为我提出的想法

## review

Consider the paper [Accurate and General DNA Representations Emerge from Genome Foundation Models at Scale](https://www.biorxiv.org/content/biorxiv/early/2024/12/05/2024.12.01.625444.full.pdf), proposing **AIDO.DNA**, a large-scale pretrained DNA encoder model designed to learn accurate and general representations of genomic functions. The model is transformer architecture, applying MLM method and character-level tokenization to capture high-resolution single-nucleotide dependencies.  



## proposal

**AIDO.DNA** show its superior performance on the downstream tasks, but it can capture a short context length of 4k tokens at single-nucleotide resolution. But as the growth of context length, the accuracy for downstream task and perplexity of AIDO.DNA model will become worse, that is it cannot handle long context. 

First, we intend to test PI,  GeNE in  [Context Length Extension via Generalized Extrapolation Scale](https://aclanthology.org/2024.findings-acl.249.pdf), YaRN in [YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/pdf/2309.00071), NTK-aware,  CLEX, several positional embedding method to enlarge the context length to about 16x compared with the original length. These positional embedding methods don't need to modify the basic architecture and enable to enhance the capability to handle long context via modification of PE layer and a simple fine-tuning or no fine-tuning. Hence, it is a low overhead experiment.

Maybe we can aggregate the advantage of the PE method above, and propose a novel PE method. 

**Remark:** There is no papers applying the method (only need a simple fine-tuning based on pre-trained model, do not need to modify the architecture and pre-train it from scratch) to extend the length of input DNA sequence without loss of performance.



下面不是proposal内容

--------------------------------------------

主要论文[Accurate and General DNA Representations Emerge from Genome Foundation Models at Scale](https://www.biorxiv.org/content/biorxiv/early/2024/12/05/2024.12.01.625444.full.pdf)

代码库<https://github.com/genbio-ai/ModelGenerator/tree/1421cc0d189c9630cd1e06503378587dbdfc3016>

官方提供的数据库：

[dependency mapping](https://github.com/genbio-ai/ModelGenerator/tree/1421cc0d189c9630cd1e06503378587dbdfc3016/experiments/AIDO.DNA/dependency_mapping) 我想搞清楚，这个README说的`dependency mapping plot`图是什么意思，我之后会生成图

[sequence classification](https://github.com/genbio-ai/ModelGenerator/tree/1421cc0d189c9630cd1e06503378587dbdfc3016/experiments/AIDO.DNA/sequence_classification)

[zero shot variant effect prediction](https://github.com/genbio-ai/ModelGenerator/tree/1421cc0d189c9630cd1e06503378587dbdfc3016/experiments/AIDO.DNA/zeroshot_variant_effect_prediction)

--------------------

to: 诚

数据创新：根据上面的官方数据库的三个不同类型的数据，作为参考，找一些dna序列长度要求为4k - 64k之间的数据集, 当然dna序列长度和下游任务类型越丰富越好 

进一步创新（来自一个门外汉的构想）：官方提供了三种类型的实验，我看的懂sequence classification 一点点，但是dependency mapping对我来说还是很茫然。如果可以找到一些不一样的任务（不局限于DNA,RNA,不过最好不要设计蛋白质结构，这又有很多其他内容），大胆假设，不用担心模型能不能适配这个任务，然后我们去通过模型解决这个任务，又是一个很不错的创新（我猜）

------------------------------

训练实时监控：

我的网址<https://dna.bubulamb.lol>

监控的参数还需要调整

-----------------------------------
to: 一凡

config.yml加一个model配置项，可以选择自己的pe，我在我们的仓库<https://github.com/DSAwaku/ModelGenerator> fork了AIDO.DNA仓库，每次上传都要用在自己的分支

