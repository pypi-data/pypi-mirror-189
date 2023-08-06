#! /usr/bin/python
# -*- coding: utf-8 -*-

import torch
import six
import abc
import numpy as np

__all__ = [
    'Accuracy',
    'Auc',
    'Precision',
    'Recall',
    'acc',
]


@six.add_metaclass(abc.ABCMeta)
class Metric(object):

    def __init__(self):
        pass

    @abc.abstractmethod
    def update(self, *args):
        raise NotImplementedError("function 'update' not implemented in {}.".format(self.__class__.__name__))

    @abc.abstractmethod
    def result(self):
        raise NotImplementedError("function 'reset' not implemented in {}.".format(self.__class__.__name__))

    @abc.abstractmethod
    def reset(self):
        raise NotImplementedError("function 'reset' not implemented in {}.".format(self.__class__.__name__))


class Accuracy(Metric):

    def __init__(self, topk=1):
        super(Accuracy, self).__init__()
        self.topk = topk
        self.reset()

    def update(self, y_pred, y_true):

        y_pred = torch.argsort(y_pred, dim=-1, descending=True)
        y_pred = y_pred[:, :self.topk]
        if (len(y_true.shape) == 1) or (len(y_true.shape) == 2 and y_true.shape[-1] == 1):
            y_true = torch.reshape(y_true, (-1, 1))
        elif y_true.shape[-1] != 1:
            y_true = torch.argmax(y_true, dim=-1, keepdim=True)
        correct = y_pred == y_true
        correct = correct.to(torch.float32)
        correct = correct.cpu().numpy()
        num_samples = np.prod(np.array(correct.shape[:-1]))
        num_corrects = correct[..., :self.topk].sum()
        self.total += num_corrects
        self.count += num_samples

    def result(self):
        return float(self.total) / self.count if self.count > 0 else 0.

    def reset(self):
        self.total = 0.0
        self.count = 0.0


class Auc(object):

    def __init__(
        self,
        curve='ROC',
        num_thresholds=4095,
    ):
        self.curve = curve
        self.num_thresholds = num_thresholds
        self.reset()

    def update(self, y_pred, y_true):
        if isinstance(y_true, torch.Tensor):
            y_true = y_true.cpu().numpy()
        elif not isinstance(y_pred, np.ndarray):
            raise TypeError("The y_true must be a numpy array or Tensor.")

        if isinstance(y_pred, torch.Tensor):
            y_pred = y_pred.cpu().numpy()
        elif not isinstance(y_pred, np.ndarray):
            raise TypeError("The y_pred must be a numpy array or Tensor.")

        for i, label in enumerate(y_true):
            value = y_pred[i, 1]  # positive probability
            bin_idx = int(value * self.num_thresholds)
            assert bin_idx <= self.num_thresholds
            if label:
                self._stat_pos[bin_idx] += 1.0
            else:
                self._stat_neg[bin_idx] += 1.0

    @staticmethod
    def trapezoid_area(x1, x2, y1, y2):
        return abs(x1 - x2) * (y1 + y2) / 2.0

    def result(self):
        tot_pos = 0.0
        tot_neg = 0.0
        auc = 0.0
        idx = self.num_thresholds
        while idx > 0:
            tot_pos_prev = tot_pos
            tot_neg_prev = tot_neg
            tot_pos += self._stat_pos[idx]
            tot_neg += self._stat_neg[idx]
            auc += self.trapezoid_area(tot_neg, tot_neg_prev, tot_pos, tot_pos_prev)
            idx -= 1

        return auc / tot_pos / tot_neg if tot_pos > 0.0 and tot_neg > 0.0 else 0.0

    def reset(self):
        """
        Reset states and result
        """
        _num_pred_buckets = self.num_thresholds + 1
        self._stat_pos = np.zeros(_num_pred_buckets)
        self._stat_neg = np.zeros(_num_pred_buckets)


class Precision(object):

    def __init__(self):
        self.reset()

    def update(self, y_pred, y_true):
        if isinstance(y_true, torch.Tensor):
            y_true = y_true.cpu().numpy()
        elif not isinstance(y_pred, np.ndarray):
            raise TypeError("The y_true must be a numpy array or Tensor.")

        if isinstance(y_pred, torch.Tensor):
            y_pred = y_pred.cpu().numpy()
        elif not isinstance(y_pred, np.ndarray):
            raise TypeError("The y_pred must be a numpy array or Tensor.")

        sample_num = y_true.shape[0]
        y_pred = np.rint(y_pred).astype('int32')

        for i in range(sample_num):
            pred = y_pred[i]
            label = y_true[i]
            if pred == 1:
                if pred == label:
                    self.tp += 1
                else:
                    self.fp += 1

    def result(self):

        ap = self.tp + self.fp
        return float(self.tp) / ap if ap != 0 else .0

    def reset(self):
        self.tp = 0
        self.fp = 0


class Recall(object):

    def __init__(self):
        self.reset()

    def update(self, y_pred, y_true):
        if isinstance(y_true, torch.Tensor):
            y_true = y_true.cpu().numpy()
        elif not isinstance(y_pred, np.ndarray):
            raise TypeError("The y_true must be a numpy array or Tensor.")

        if isinstance(y_pred, torch.Tensor):
            y_pred = y_pred.cpu().numpy()
        elif not isinstance(y_pred, np.ndarray):
            raise TypeError("The y_pred must be a numpy array or Tensor.")

        sample_num = y_true.shape[0]
        y_pred = np.rint(y_pred).astype('int32')

        for i in range(sample_num):
            pred = y_pred[i]
            label = y_true[i]
            if label == 1:
                if pred == label:
                    self.tp += 1
                else:
                    self.fn += 1

    def result(self):

        recall = self.tp + self.fn
        return float(self.tp) / recall if recall != 0 else .0

    def reset(self):
        self.tp = 0
        self.fn = 0


def acc(predicts, labels, topk=1):
    y_pred = torch.argsort(predicts, dim=-1, descending=True)
    y_pred = y_pred[:, :topk]
    if (len(labels.shape) == 1) or (len(labels.shape) == 2 and labels.shape[-1] == 1):
        y_true = torch.reshape(labels, (-1, 1))
    elif labels.shape[-1] != 1:
        y_true = torch.argmax(labels, dim=-1, keepdim=True)
    correct = y_pred == y_true
    correct = correct.to(torch.float32)
    correct = correct.cpu().numpy()
    num_samples = np.prod(np.array(correct.shape[:-1]))
    num_corrects = correct[..., :topk].sum()
    total = num_corrects
    count = num_samples
    return float(total) / count if count > 0 else 0.
