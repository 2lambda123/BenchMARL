#  Copyright (c) Meta Platforms, Inc. and affiliates.
#
#  This source code is licensed under the license found in the
#  LICENSE file in the root directory of this source tree.
#

from dataclasses import dataclass, MISSING


@dataclass
class TaskConfig:
    task: str = MISSING
    num_good: int = MISSING
    num_adversaries: int = MISSING
    num_obstacles: int = MISSING
    max_cycles: int = MISSING
