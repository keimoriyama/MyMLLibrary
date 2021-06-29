import torch
import torch.nn as nn

from torch.utils.data import DataLoader, Dataset
from torch.utils.data.dataset import Subset

from sklearn.model_selection import train_test_split, KFold


# これを継承していろいろなデータに対応したデータセットクラスを作っていきたい
class template_dataset(Dataset):

    def __init__(self, data=None, label=None):
        if data is None:
            raise ValueError("data is empty")
        if label is None:
            raise ValueError('label is empty')
        self.data = data
        self.label = label
    
    def __len__(self):
        return len(self.data)
