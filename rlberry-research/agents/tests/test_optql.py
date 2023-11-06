from rlberry_research.agents.optql import OptQLAgent
from rlberry_research.envs.finite import GridWorld


def test_optql():
    env = GridWorld(walls=(), nrows=5, ncols=5)
    agent = OptQLAgent(env, horizon=11, gamma=0.99, bonus_scale_factor=0.1)
    agent.fit(budget=50)
    agent.policy(env.observation_space.sample())
