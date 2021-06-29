import torch
import torch.nn as nn

from torch.utils.data import DataLoader, Dataset
from torch.utils.data.dataset import Subset

from sklearn.model_selection import train_test_split, KFold

import numpy as np


# これを継承していろいろなデータに対応したデータセットクラスを作っていきたい
class template_dataset(Dataset):
    def __init__(self,
                 data: np.ndarray = None,
                 label: np.ndarray = None) -> None:
        if data is None:
            raise ValueError("data is empty")
        self.data = data
        self.label = label

    def __len__(self) -> int:
        return self.data.shape[-1]


class image_dataset(template_dataset):
    def __init__(self,
                 data: np.ndarray = None,
                 label: np.ndarray = None,
                 transform=None):
        super().__init__(data, label)
        if transform is not None:
            self.transform = transform

    def __getitem__(self, index):
        image = self.data[index]
        label = self.label[index]
        if self.transform:
            image = self.transform(image)

        return image, label
