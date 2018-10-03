# from __future__ import print_function
import os
import os.path
import numpy as np
import sys
if sys.version_info[0] == 2:
    import cPickle as pickle
else:
    import pickle

import torch.utils.data as data


class CSD08(data.Dataset):
    base_folder = 'csd08-batches-py'
    filename = "csd-08-python.tar.gz"
    # train_list = [
    #     ['data_batch_1', 'c99cafc152244af753f735de768cd75f'],
    #     ['data_batch_2', 'd4bba439e000b95fd0a9bffe97cbabec'],
    #     ['data_batch_3', '54ebc095f3ab1f0389bbae665268c751'],
    #     ['data_batch_4', '634d18415352ddfa80567beed471001a'],
    #     ['data_batch_5', '482c414d41f54cd18b22e5b47cb7c3cb'],
    # ]

    # test_list = [
    #     ['test_batch', '40351d587109b95175f43aff81a1287e'],
    # ]

    def __init__(self, root, train=True,
                 transform=None, target_transform=None,
                 train_list=[], test_list=[]):
        """
        root = ./data
        :param root:
        :param train:
        :param transform:
        :param target_transform:
        """
        self.root = os.path.expanduser(root)
        self.transform = transform
        self.target_transform = target_transform
        self.train = train  # training set or test set
        self.train_list = train_list
        self.test_list = test_list

        # if not self._check_integrity():
        #     raise RuntimeError('Dataset not found or corrupted.' +
        #                        ' You can use download=True to download it')

        # now load the picked numpy arrays
        if self.train:
            self.train_data = []
            self.train_labels = []
            for fentry in self.train_list:
                f = fentry[0]
                file = os.path.join(self.root, self.base_folder, f)
                fo = open(file, 'rb')
                if sys.version_info[0] == 2:
                    entry = pickle.load(fo)
                else:
                    entry = pickle.load(fo, encoding='latin1')
                self.train_data.append(entry['data'])
                if 'labels' in entry:
                    self.train_labels += entry['labels']
                else:
                    self.train_labels += entry['fine_labels']
                fo.close()

            # self.train_data = np.concatenate(self.train_data)
            # self.train_data = self.train_data.reshape((50000, 3, 32, 32))
            # self.train_data = self.train_data.transpose((0, 2, 3, 1))  # convert to HWC
        else:
            f = self.test_list[0][0]
            file = os.path.join(self.root, self.base_folder, f)
            fo = open(file, 'rb')
            if sys.version_info[0] == 2:
                entry = pickle.load(fo)
            else:
                entry = pickle.load(fo, encoding='latin1')
            self.test_data = entry['data']
            if 'labels' in entry:
                self.test_labels = entry['labels']
            else:
                self.test_labels = entry['fine_labels']
            fo.close()
            self.test_data = self.test_data.reshape((10000, 3, 32, 32))
            self.test_data = self.test_data.transpose((0, 2, 3, 1))  # convert to HWC

    def __getitem__(self, index):
        """
        Args:
            index (int): Index

        Returns:
            tuple: (image, target) where target is index of the target class.
        """
        if self.train:
            img, target = self.train_data[index], self.train_labels[index]
        else:
            img, target = self.test_data[index], self.test_labels[index]

        # doing this so that it is consistent with all other datasets
        # to return a PIL Image
        img = Image.fromarray(img)

        if self.transform is not None:
            img = self.transform(img)

        if self.target_transform is not None:
            target = self.target_transform(target)

        return img, target

    def __len__(self):
        if self.train:
            return len(self.train_data)
        else:
            return len(self.test_data)

    def __repr__(self):
        fmt_str = ""
        # fmt_str = 'Dataset ' + self.__class__.__name__ + '\n'
        # fmt_str += '    Number of datapoints: {}\n'.format(self.__len__())
        # tmp = 'train' if self.train is True else 'test'
        # fmt_str += '    Split: {}\n'.format(tmp)
        # fmt_str += '    Root Location: {}\n'.format(self.root)
        # tmp = '    Transforms (if any): '
        # fmt_str += '{0}{1}\n'.format(tmp, self.transform.__repr__().replace('\n', '\n' + ' ' * len(tmp)))
        # tmp = '    Target Transforms (if any): '
        # fmt_str += '{0}{1}'.format(tmp, self.target_transform.__repr__().replace('\n', '\n' + ' ' * len(tmp)))
        return fmt_str