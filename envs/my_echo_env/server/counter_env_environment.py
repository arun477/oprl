# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""
My Echo Env Environment Implementation.

A simple test environment that echoes back messages sent to it.
Perfect for testing HTTP server infrastructure.
"""

from uuid import uuid4

from openenv.core.env_server.interfaces import Environment
from openenv.core.env_server.types import State

try:
    from ..models import CounterAction, CounterObservation
except ImportError:
    from models import CounterAction, CounterObservation


class CounterEnvironment(Environment):
    SUPPORTS_CONCURRENT_SESSIONS: bool = True

    def __init__(self):
        self._state = State(episode_id=str(uuid4()), step_count=0)
        self.count  = 0

    def reset(self) -> CounterObservation:
        self._state = State(episode_id=str(uuid4()), step_count=0)
        self.count = 0
        return CounterObservation(
            count=0,
            done=False,
            reward=0.0
        )
       

    def step(self, action: CounterAction) -> CounterObservation:
        self._state.step_count += 1
        if action.action == "increment":
            self.count += 1
        elif action.action == "decrement":
            self.count -= 1
        
        done = self.count == 10
        reward = 1.0 if done else 0.0
        
        return CounterObservation(
            count=self.count,
            done=done,
            reward=reward
        )
      

    @property
    def state(self) -> State:
        return self._state
      