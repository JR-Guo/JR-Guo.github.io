---
title: "Multi Label criterion"
date: 2022-06-22T12:00:30-13:00
categories:
  - blog
tags:
  - Python
  - PyTorch
  - Computer Vision
---
Now, we are discussing the evaluation metrics for multi-label disease verifying.

Metrics play quite an important role in the field of Machine Learning or Deep Learning. We start the problems with metric selection as to know the baseline score of a particular model. In this blog, we look into the best and most common metrics for Multi-Label Classification and how they differ from the usual metrics.

1. Precision at k
2. Avg precision at k
3. Mean avg precision at k
4. Sampled F1 Score

(Precision at k (P@k):)
Given a list of actual classes and predicted classes, precision at k would be defined as the number of correct predictions considering only the top k elements of each class divided by k. The values range between 0 and 1.

(Average Precision at K (AP@k):)
It is defined as the average of all the precision at k for k =1 to k. To make it more clear let’s look at some code. The values range between 0 and 1.

(Mean Average Precision at K (MAP@k):)
The average of all the values of AP@k over the whole training data is known as MAP@k. This helps us give an accurate representation of the accuracy of whole prediction data. Here is some code for the same.

(F1 — Samples:)
This metric calculates the F1 score for each instance in the data and then calculates the average of the F1 scores. We will be using sklearn’s implementation of the same in the code.

per-class precision(CP), recall (CR), F1 (CF1) and the average overall precision (OP), recall (OR), F1 (OF1), under the setting that a
predicted label is positive if the output probability is greater
than 0.5. ()

We also report the mean average precision (mAP).
A detailed explanation of the metrics are shown in the Appendix. For fair comparisons to previous works, we also consider the setting where we evaluate the Top-3 predicted labels following. In general, `mAP``, OF1`, and `CF1` are the most important metrics.