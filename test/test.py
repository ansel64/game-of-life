import pytest
import sys
sys.path.insert(1, '/Users/ksvni/Documents/Project/Python/game-of-life/src/')

import main
import error

# Test for stub
class Test_ParseForGrid:
    def test(self):
        a = [['0', '0', '0', '1', '0', '1', '0', '1'],
             ['0', '1', '0', '0', '0', '1', '0', '1'],
             ['0', '1', '0', '0', '0', '1', '1', '0'],
             ['0', '1', '0', '0', '0', '1', '1', '0'],
             ['0', '1', '0', '0', '0', '1', '1', '0'],
             ['0', '0', '0', '1', '0', '1', '0', '1'],
             ['0', '0', '0', '1', '0', '1', '0', '1'],
             ['0', '0', '0', '1', '0', '1', '0', '1']]

        assert main.parseForGrid('mock1.txt') == []
        assert main.parseForGrid('mock2.txt') == a
