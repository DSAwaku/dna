以下为我提出的想法

## review

Consider the paper [Accurate and General DNA Representations Emerge from Genome Foundation Models at Scale](https://www.biorxiv.org/content/biorxiv/early/2024/12/05/2024.12.01.625444.full.pdf), proposing **AIDO.DNA**, a large-scale pretrained DNA encoder model designed to learn accurate and general representations of genomic functions. The model is transformer architecture, applying MLM method and character-level tokenization to capture high-resolution single-nucleotide dependencies.  



## proposal

**AIDO.DNA** show its superior performance on the downstream tasks, but it can capture a short context length of 4k tokens at single-nucleotide resolution. But as the growth of context length, the accuracy and perplexity of AIDO.DNA model will become worse, that is it cannot handle long context. 

First, we intend to test PI,  GeNE in  [Context Length Extension via Generalized Extrapolation Scale](https://aclanthology.org/2024.findings-acl.249.pdf), YaRN in [YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/pdf/2309.00071), NTK-aware,  CLEX, several positional embedding method to enlarge the context length to about 16x compared with the original length. These positional embedding methods don't need to modify the architecture and enable to enhance the capability to handle long context via modification of PE layer and a simple fine-tuning. Hence, it is a low overhead experiment.

Maybe we can aggregate the advantage of the PE method above, and propose a novel PE method.
