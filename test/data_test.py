import sys
import unittest

import numpy as np

sys.path.append('../src/')

from data import image_dataset, template_dataset

image_size = 16
num_image = 5
labels = 3
# 適当に生成した画像ベクトル
data = np.random.rand(image_size, image_size, num_image)
label = np.random.randint(0, labels, (num_image))


class TestDatasets(unittest.TestCase):
    def test_imagedataset(self):
        dataset = image_dataset(data, label)
        print("test of dataset length")
        self.assertEqual(num_image, len(dataset))

    def test_dataset(self):
        dataset = image_dataset(data, label)
        print('test returned data and label')
        image, image_label = dataset.__getitem__(0)
        self.assertEqual(image.shape, (image_size, image_size))
        self.assertEqual(image_label.size(0), 1)

    def test_error(self):
        print('test of dataset which size is not enough')
        dummy = np.random.rand(image_size, image_size)
        with self.assertRaises(ValueError):
            dataset = image_dataset(data=dummy, label=label)

    def test_empty_labels(self):
        dataset = image_dataset(data)
        print('test empty labels')
        image_data = dataset.__getitem__(0)
        self.assertEqual(image_data.shape, (image_size, image_size))


if __name__ == '__main__':
    unittest.main()
