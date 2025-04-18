# Dynamic Gated Adapter Mechanism

The `token_importance` variable in the `DynamicGatedAdapter` class represents the importance weights assigned to each token in the sequence for classification. Let me explain the mathematical formulation behind this mechanism.

## Mathematical Formulation

Given input hidden states $\mathbf{H} \in \mathbb{R}^{B \times L \times D}$ where $B$ is batch size, $L$ is sequence length, and $D$ is hidden dimension:

1. **CLS Token Extraction**:
   - $\mathbf{h_{cls}} = \mathbf{H}_{:,0,:} \in \mathbb{R}^{B \times D}$

2. **Gate Calculation**:
   - For each token $i$: $\mathbf{g}_i = \sigma(W_g[\mathbf{h_{cls}}; \mathbf{h}_i] + b_g)$
   - Where $[;]$ denotes concatenation and $\sigma$ is sigmoid

3. **Attention Fusion**:
   - $\mathbf{q} = W_q \mathbf{h_{cls}}$ 
   - $\mathbf{k}_i = W_k \mathbf{h}_i$
   - Attention scores: $\mathbf{a}_i = \mathbf{q} \cdot \mathbf{k}_i^T$
   - Attention weights: $\mathbf{\alpha}_i = \sigma(\mathbf{a}_i)$

4. **Final Gate Computation**:
   - $\mathbf{g}_i^{final} = \mathbf{g}_i \odot \mathbf{\alpha}_i \odot \mathbf{m}_i$
   - Where $\mathbf{m}_i$ is the attention mask and $\odot$ is element-wise multiplication

5. **Token Importance**:
   - $\mathbf{token\_importance}_i = \mathbf{g}_i^{final} \cdot \mathbf{c}_i$
   - Where $\mathbf{c}_i = 0$ if $i=0$ (CLS position), $1$ otherwise

6. **Final Representation**:
   - $\mathbf{z} = \mathbf{h_{cls}} + \sum_{i=1}^{L} \mathbf{h}_i \odot \mathbf{token\_importance}_i$

7. **Output Computation**:
   - $\mathbf{output} = W_{linear}(\text{Dropout}(\text{LayerNorm}(\mathbf{z})))$

The `token_importance` values allow the model to selectively incorporate information from different tokens, essentially learning which parts of the input are most relevant for the classification task.