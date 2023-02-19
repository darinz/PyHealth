from abc import ABC

import torch
import torch.nn as nn
import torch.nn.functional as F


class KGE(nn.Module):
    """ Abstract class for Knowledge Graph Embedding models

    Args:
        e_num: the number of entities in the dataset.
        r_num: the number of relations in the dataset.
        e_dim: the hidden embedding size for entity.
        r_dim: the hidden embedding size for relation.


    """


    def __init__(
        self,
        e_num,
        r_num,
        e_dim,
        r_dim,
        
    ):
        super().__init__()