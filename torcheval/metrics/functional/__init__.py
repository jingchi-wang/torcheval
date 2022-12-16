# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from torcheval.metrics.functional.aggregation import auc, mean, sum, throughput
from torcheval.metrics.functional.classification import (
    binary_accuracy,
    binary_auprc,
    binary_auroc,
    binary_binned_precision_recall_curve,
    binary_confusion_matrix,
    binary_f1_score,
    binary_normalized_entropy,
    binary_precision,
    binary_precision_recall_curve,
    binary_recall,
    binary_recall_at_fixed_precision,
    multiclass_accuracy,
    multiclass_auprc,
    multiclass_auroc,
    multiclass_binned_precision_recall_curve,
    multiclass_confusion_matrix,
    multiclass_f1_score,
    multiclass_precision,
    multiclass_precision_recall_curve,
    multiclass_recall,
    multilabel_accuracy,
    multilabel_auprc,
    multilabel_precision_recall_curve,
    multilabel_recall_at_fixed_precision,
    topk_multilabel_accuracy,
)
from torcheval.metrics.functional.ranking import (
    click_through_rate,
    frequency_at_k,
    hit_rate,
    num_collisions,
    reciprocal_rank,
    weighted_calibration,
)
from torcheval.metrics.functional.regression import mean_squared_error, r2_score
from torcheval.metrics.functional.text import (
    perplexity,
    word_error_rate,
    word_information_preserved,
)


__all__ = [
    "auc",
    "binary_auprc",
    "binary_auroc",
    "binary_accuracy",
    "binary_confusion_matrix",
    "binary_normalized_entropy",
    "binary_precision",
    "binary_precision_recall_curve",
    "binary_binned_precision_recall_curve",
    "binary_recall",
    "binary_recall_at_fixed_precision",
    "binary_f1_score",
    "click_through_rate",
    "frequency_at_k",
    "hit_rate",
    "mean",
    "mean_squared_error",
    "multiclass_accuracy",
    "multiclass_auprc",
    "multiclass_auroc",
    "multiclass_binned_precision_recall_curve",
    "multiclass_confusion_matrix",
    "multiclass_f1_score",
    "multiclass_precision",
    "multiclass_precision_recall_curve",
    "multiclass_recall",
    "multilabel_accuracy",
    "multilabel_auprc",
    "multilabel_precision_recall_curve",
    "multilabel_recall_at_fixed_precision",
    "num_collisions",
    "perplexity",
    "topk_multilabel_accuracy",
    "r2_score",
    "reciprocal_rank",
    "sum",
    "throughput",
    "weighted_calibration",
    "word_error_rate",
    "word_information_preserved",
]
