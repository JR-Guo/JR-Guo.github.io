---
title: "Semi-SL method"
date: 2022-06-17T12:00:00-14:00
categories:
  - blog
tags:
  - SemiSL
  - Computer_Vision
---
引用自[别人的blog]
一般来说，半监督学习中的 unlabeled data 会使用全部训练数据集，即有标签的样本也会作为无标签样本来使用。

半监督学习中，labeled data 的标签都是给定的，而 unlabeled data 的标签都是不知道的。那么如何获得 unlabeled data 的人工标签（artificial label），MixMatch、UDA、ReMixMatch 和 FixMatch 的做法或多或少都不相同：

MixMatch：平均 K 次 weak augmentation（如 shifting 和 flipping）的 predictions ，然后经过 temperature sharpening；
UDA：一次 weak augmentation 的 prediction，然后经过 temperature sharpening；
ReMixMatch：一次 weak augmentation 的 prediction，然后经过 distribution alignment，最后经过 temperature sharpening；
FixMatch：一次 weak augmentation 的 prediction，然后 argmax 得到 hard label（pseudo label）。




MixMatch、UDA 和 ReMixMatch 通过 temperature sharpening 来间接利用 entropy minimization，而 FixMatch 通过 Pseudo label 来间接利用 entropy minimization。可以认为，只要通过得到 unlabeled data 的人工标签然后按照监督学习的方法（如 cross entropy loss）来训练的，都间接用到了 entropy minimization。因为人工标签都是 one-hot 或者近似 one-hot 的，如果 unlabeled data 的 prediction 近似人工标签，那么此时无标签数据的熵肯定也是较小的。

为什么这里叫做人工标签而不是伪标签？一般而言，在半监督中，伪标签（pseudo label）特指 hard label，即 one-hot 类型的或者通过 argmax 得到的。[4] 而 MixMatch、UDA、ReMixMatch 得到的人工标签并不是 hard label。

Entropy minimization 可以在计算 unlabeled data 部分的 loss 和 consistency regularization 一起实现。
temperature sharpening 和 pseudo label 都得到了 unlabeled data 的人工标签，当前者 temperature=0 时，两者相等。pseudo label 要比 temperature sharpening 要简单，因为少了一个 temperature 超参数。如果不考虑 entropy minimization，那么 temperature sharpening 和 pseudo label 其实都是不需要的，只需要两次随机注入 noise 的 unlabeled instance 输出近似，就可以保证 consistency regularization，如 Π-model。或者说，得到 unlabeled data 的人工标签，可以使得 entropy minimization 和 consistency regularization 通过一项 loss 来完成。


从 UDA 和 ReMixMatch 开始，strong augmentation 引入了半监督训练。UDA 使用了作者之前提出的 RandAugment 的 strong augmentation 方式，而 ReMixMatch 提出了一种 CTAugment。FixMatch 就把 UDA 和 ReMixMatch 中用到的 strong augmentation 都拿来用了一遍。

Conclusion: 
temperature sharpening 换成 pseudo label。【Fixmatch对比Mixmatch】


What is Temperature Sharpening?
Look at the MixMatch Paper. Page 4. Sharpening parts.



[别人的blog]: https://www.cnblogs.com/wuliytTaotao/p/12727922.html