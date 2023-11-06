"""
===============================================
Tests for the installation without extra (StableBaselines3, torch, optuna, ...)
===============================================
tests based on test_agent.py and test_envs.py

"""


import pytest
import sys

import rlberry_research.agents as agents

from rlberry.utils.check_agent import (
    check_rl_agent,
    check_rlberry_agent,
)


FINITE_MDP_AGENTS = [
    agents.OptQLAgent,
    agents.PSRLAgent,
    agents.RLSVIAgent,
]


CONTINUOUS_STATE_AGENTS = [
    agents.RSUCBVIAgent,
    agents.RSKernelUCBVIAgent,
]


@pytest.mark.parametrize("agent", FINITE_MDP_AGENTS)
def test_finite_state_agent(agent):
    check_rl_agent(agent, env="discrete_state")
    check_rlberry_agent(agent, env="discrete_state")


@pytest.mark.xfail(sys.platform == "win32", reason="bug with windows???")
@pytest.mark.parametrize("agent", CONTINUOUS_STATE_AGENTS)
def test_continuous_state_agent(agent):
    check_rl_agent(agent, env="continuous_state")
    check_rlberry_agent(agent, env="continuous_state")
