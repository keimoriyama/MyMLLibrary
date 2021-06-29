import sys
import unittest

import numpy as np

sys.path.append('../src/')

from data import image_dataset, template_dataset

image_size = 16
num_image = 5
labels = 3

data = np.random.rand(image_size, image_size, num_image)
label = np.random.randint(0, labels, (num_image))


class TestDatasets(unittest.TestCase):
    def test_imagedataset(self):
        dataset = image_dataset(data, label)
        print("test of dataset length")
        self.assertEqual(num_image, len(dataset))

    def test_error(self):
        print('test of empty dataset')
        with self.assertRaises(ValueError):
            dataset = image_dataset(label=labels)


if __name__ == '__main__':
    unittest.main()
