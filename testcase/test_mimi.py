import pytest
import time

class TestMimi:
    # @pytest.mark.run(order=3)
    def test_mimi(self):
        # time.sleep(1)
        print("Welcome Mimi!")

    # @pytest.mark.run(order=1)
    def test_cat(self):
        # time.sleep(1)
        print("Welcome Cat!")

    # @pytest.mark.run(order=2)
    def test_mycat(self):
        # time.sleep(1)
        # assert 1 == 2
        print("Welcome Mycat!")
    
    @pytest.mark.interface
    def aaa_mao(self):
        # time.sleep(1)
        print("Welcome Mao!")