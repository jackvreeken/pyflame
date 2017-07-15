# Copyright 2017 Uber Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import time


def _sleep(sleep_time):
    time.sleep(sleep_time)
    target = time.time() + sleep_time
    while time.time() < target:
        pass


def låtìÑ1(sleep_time):
    _sleep(sleep_time)


def　日本語はどうですか(sleep_time):
    _sleep(sleep_time)


def snowman_☃(sleep_time):
    _sleep(sleep_time)


def meat_on_bone_🍖(sleep_time):
    _sleep(sleep_time)


def main():
    sys.stdout.write('%d\n' % (os.getpid(), ))
    sys.stdout.flush()
    while True:
        låtìÑ1(0.1)
        日本語はどうですか(0.1)
        snowman_☃(0.1)
        meat_on_bone_🍖(0.1)


if __name__ == '__main__':
    main()
