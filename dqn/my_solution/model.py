import torch
import torch.nn as nn
import torch.nn.functional as F


class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super().__init__()
        self.seed = torch.manual_seed(seed)
        hs = 256
        self.net = nn.Sequential(
            nn.Linear(state_size, hs),
            nn.ReLU(),
            nn.Linear(hs, hs),
            nn.ReLU(),
            nn.Linear(hs, action_size),
        )

    def forward(self, state):
        """Build a network that maps state -> action values."""
        return self.net(state)