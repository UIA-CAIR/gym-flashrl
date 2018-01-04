from gym.envs.registration import register
import gym_flashrl.envs.flashrl_env


for env in dir(gym_flashrl.envs.flashrl_env):

    if "FlashRL" not in env or "Env" not in env:
        continue

    clazz_env = getattr(gym_flashrl.envs.flashrl_env, env)
    register(
        id=clazz_env.id,
        entry_point='gym_flashrl.envs:%s' % env
    )