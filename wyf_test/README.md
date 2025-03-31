# 分类实验设计

DNA序列分类任务的实验配置，探索不同适配器架构适配在基因组和病毒序列识别任务上的工作。

## 实验概述

1. **病毒物种识别（Virus Species Identification）**：使用GUE数据集中的`virus_species_40`配置，包含40个分类类别。
2. **小鼠序列识别（Mouse Sequence Identification）**：使用GUE数据集中的`mouse_1`配置，包含二分类任务。

## 适配器架构比较

实验对比了四种不同的适配器架构：

1. **LinearTransformerAdapter**：在CLS token上应用Transformer层，在病毒数据集上使用，这因为病毒的变异往往和语义信息（病毒的感染部位、病毒的治病逻辑）无关，特定点位，特定序列的变异，导致传染力、杀伤力增强等等。使用Transformer可以绘制注意力热图，找到特定病毒的变异序列进行可视化。

2. **ResNet1DAdapter**：使用一维残差网络处理序列特征，在病毒数据集上使用，这因为病毒的变异往往和语义信息（病毒的感染部位、病毒的治病逻辑）无关，特定点位，特定序列的变异，导致传染力、杀伤力增强等等。如果能够成功使用ResNet1D，计算效率将大幅提高，适合直接应用于实际场景中的快速病毒分类任务。

3. **MLPPoolAdapter**：使用多层感知机配合CLS pooling策略，在老鼠数据集上使用。哺乳动物的识别，往往是整段的DNA语义信息。

4. **LinearCLSAdapter**：简单线性层配合CLS token特征提取。哺乳动物的识别，往往是整段的DNA语义信息。

## 问题

1. **Transformer层显存需求问题**：LinearTransformerAdapter使用了Transformer层结构，显存需求较大。原始Adapter的可调整参数较少，可能需要继承后进行进一步的个性化调整，以在保持性能的同时减少资源消耗。

2. **ResNet1D适配器限制**：ResNet1DAdapter在当前配置下无法正常使用，原因是它不接受1维以上的输出（`num_outputs`参数限制为1）。从代码注释可见，这个适配器主要是从RiNALMo项目移植而来，原本设计用于AIDO.RNA相关任务。若要在病毒分类任务（40个类别）中使用，需要对适配器进行改造，修改其输出层以支持多分类。


