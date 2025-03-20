## 架构参数

**vocab.txt**

```
# vocab.txt
[PAD]
[MASK]
[CLS]
[SEP]
[UNK]
A
G
C
T
U
N
[BOS]
[EOS]
[UNUSED1]
[UNUSED2]
[UNUSED3]
```

## aido_dna_300m

**gue_core_promoter_all.yml**

**modelgenerator.tasks.SequenceClassification**

**modelgenerator.adapters.LinearCLSAdapter**

**modelgenerator.data.GUEClassification**

**class = 2**

[**config file**](./experiments/test1/gue_core_promoter_all.yaml)

```
==================== RNABertEmbedding ====================

RNABertEmbeddings(
  (word_embeddings): Embedding(16, 1024, padding_idx=0)
  (dropout): Dropout(p=0.0, inplace=False)
)
```
```
==================== RNABertEncoder ====================

RNABertEncoder(
  (layer): ModuleList(
    (0-23): 24 x RNABertLayer(
      (attention): RNABertAttention(
        (ln): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self): RNABertSelfAttention(
          (query): Linear(in_features=1024, out_features=1024, bias=True)
          (key): Linear(in_features=1024, out_features=1024, bias=True)
          (value): Linear(in_features=1024, out_features=1024, bias=True)
          (dropout): Dropout(p=0.0, inplace=False)
        )
        (output): RNABertSelfOutput(
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (dropout): Dropout(p=0.0, inplace=False)
        )
      )
      (ln): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
      (mlp): RNABertMLP(
        (up_proj): Linear(in_features=1024, out_features=2688, bias=True)
        (down_proj): Linear(in_features=2688, out_features=1024, bias=True)
        (gate_proj): Linear(in_features=1024, out_features=2688, bias=True)
        (intermediate_act_fn): SiLU()
      )
      (output): RNABertOutput(
        (dropout): Dropout(p=0.0, inplace=False)
      )
    )
  )
  (ln): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
)
```
```
==================== RNABertPooler ====================

None
```

`class RNABertModel(RNABertPreTrainedModel):` is basic model

