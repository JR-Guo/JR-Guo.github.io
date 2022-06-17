---
title: "Semi-SL method"
date: 2022-06-17T12:00:00-14:00
categories:
  - blog
tags:
  - SemiSL
  - Computer_Vision
---
Refered from [Other's_Blog]

Generally, in Semi-supervised learning, we are proposed to present unlabeled data for whole datasets. As the result, we can used labeled data as unlabeled data for the same time.

During SSL, labeled data are fixed, but unlabeled data is unknown, So how can we obtain the artificial label through unlabeled data. In here, we discuss from 4 methods: MixMatch, UDA, ReMixMatch and FixMatch.

`MixMatch`: averaging `K` times of weak augmentation, such as shifting and fliping, during predicition and pass through temperature sharpening.
`UDA`: one weak augmentation prediction and pass through temperature sharpenging.
`ReMixMatch`: one weak augmentation and distribution alignment, and pass through temperature sharpening.
`FixMatch`: one weak augmentation + strong augmentation + argmax to obtain pseudo label. (Different from the other three methods)


`MixMatch`, `UDA` and `ReMixMatch` indirect use entropy minimization by conducting temeprature sharpening, but `FixMatch` use `Pseudo Label` to gain entropy minimization. We can think that unlabeled data are using supervised learning methods after getting artificial label to train the model and indirectly obtain entropy minimization. Becuase the artificial labels are one-hot or similar to one-hot labels. If unlabeled data's prediction is similar to artificial label. Then the entropy of unlabeled data is getting smaller.

Why is it called artificial labeling here instead of pseudo-labeling? Generally speaking, in semi-supervised, pseudo labels refer to hard labels, that is, one-hot type or obtained by argmax. The artificial labels obtained by MixMatch, UDA, and ReMixMatch are not hard labels.

Entropy minimization can be implemented together with consistency regularization in calculating the loss in the unlabeled data part.
Both temperature sharpening and pseudo label get artificial labels for unlabeled data, and both are equal when the former temperature=0. Pseudo label is simpler than temperature sharpening because there is one less temperature hyperparameter. If entropy minimization is not considered, then temperature sharpening and pseudo label are actually unnecessary. Only two random injections of noise are required to approximate the output of unlabeled instance, and consistency regularization can be guaranteed, such as Π-model. In other words, getting the artificial labels of unlabeled data can make entropy minimization and consistency regularization complete through a loss.


Beginning with UDA and ReMixMatch, strong augmentation introduces semi-supervised training. UDA uses the strong augmentation method of RandAugment proposed by the author before, while ReMixMatch proposes a CTAugment. FixMatch uses the strong augmentation used in UDA and ReMixMatch.

What is Temperature Sharpening?
Look at the MixMatch Paper. Page 4. Sharpening parts.



[Other's_Blog]: https://www.cnblogs.com/wuliytTaotao/p/12727922.html