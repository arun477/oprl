# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""
Data models for the My Echo Env Environment.

The my_echo_env environment is a simple test environment that echoes back messages.
"""

from openenv.core.env_server.types import Action, Observation
from pydantic import Field


class CounterAction(Action):
    action: str = Field(..., description="'increment' or 'decrement'")

class CounterObservation(Observation):
    coutn: int = Field(default=0, description="current counter value")