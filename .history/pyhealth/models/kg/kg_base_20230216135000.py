from abc import ABC

import torch
import torch.nn as nn
import torch.nn.functional as F


class KGE(nn.Module):
    """ Abstract class for Knowledge Graph Embedding models

    Args:
        


    """


    def __init__(
        self,
        e_num,
        r_num,
        e_dim,
        r_dim,
        
    ):
        super().__init__()