from .coco import CocoDataset
from .registry import DATASETS


@DATASETS.register_module
class CloudsDataset(CocoDataset):

    CLASSES = ('fish', 'sugar', 'gravel', 'flower')
