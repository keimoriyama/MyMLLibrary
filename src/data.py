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
    """
    expected input:
    size of data: (image_size, image_size, total_image_num)
    size of label: (total_image_num)
    """
    def __init__(self,
                 data: np.ndarray = None,
                 label: np.ndarray = None,
                 transform=None):
        if data.ndim < 3:
            raise ValueError(
                f"dimention of image data is expected 3 but got {data.ndim}")
        super().__init__(data, label)
        self.transform = transform

    def __getitem__(self, index):
        image = self.data[:, :, index]
        if self.label is not None:
            label = self.label[index]
            label = torch.tensor(label, dtype=torch.long).unsqueeze(0)
        if self.transform:
            image = self.transform(image)
        if self.label is not None:
            return image, label
        else:
            return image
