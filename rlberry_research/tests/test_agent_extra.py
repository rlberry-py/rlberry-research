import pytest
import rlberry_research.agents.torch as torch_agents
from rlberry.utils.check_agent import (
    check_rl_agent,
    check_rlberry_agent,
    check_vectorized_env_agent,
    check_hyperparam_optimisation_agent,
)

# from rlberry_scool.agents.features import FeatureMap
import sys


# No agent "FINITE_MDP" in extra
# FINITE_MDP_AGENTS = [
# ]


CONTINUOUS_STATE_AGENTS = [
    torch_agents.DQNAgent,
    torch_agents.MunchausenDQNAgent,
    torch_agents.REINFORCEAgent,
    torch_agents.PPOAgent,
    torch_agents.A2CAgent,
]

# Maybe add PPO ?
CONTINUOUS_ACTIONS_AGENTS = [torch_agents.SACAgent]


HYPERPARAM_OPTI_AGENTS = [
    torch_agents.PPOAgent,
    torch_agents.REINFORCEAgent,
    torch_agents.A2CAgent,
    torch_agents.SACAgent,
]


MULTI_ENV_AGENTS = [
    torch_agents.PPOAgent,
]

# No agent "FINITE_MDP" in extra
# @pytest.mark.parametrize("agent", FINITE_MDP_AGENTS)
# def test_finite_state_agent(agent):
#     check_rl_agent(agent, env="discrete_state")
#     check_rlberry_agent(agent, env="discrete_state")


@pytest.mark.xfail(sys.platform == "win32", reason="bug with windows???")
@pytest.mark.parametrize("agent", CONTINUOUS_STATE_AGENTS)
def test_continuous_state_agent(agent):
    check_rl_agent(agent, env="continuous_state")
    check_rlberry_agent(agent, env="continuous_state")


@pytest.mark.xfail(sys.platform == "win32", reason="bug with windows???")
@pytest.mark.parametrize("agent", CONTINUOUS_ACTIONS_AGENTS)
def test_continuous_action_agent(agent):
    check_rl_agent(agent, env="continuous_action")
    check_rlberry_agent(agent, env="continuous_action")


@pytest.mark.xfail(sys.platform == "win32", reason="bug with windows???")
@pytest.mark.parametrize("agent", MULTI_ENV_AGENTS)
def test_continuous_vectorized_env_agent(agent):
    check_vectorized_env_agent(agent, env="vectorized_env_continuous")


@pytest.mark.xfail(sys.platform == "win32", reason="bug with windows???")
@pytest.mark.parametrize("agent", HYPERPARAM_OPTI_AGENTS)
def test_hyperparam_optimisation_agent(agent):
    check_hyperparam_optimisation_agent(agent, env="continuous_state")
