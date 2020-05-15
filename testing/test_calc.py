import pytest
import yaml
import sys
sys.path.append("..")
from base.calc import Calc


def get_data_via(yamlfile):
    data = yaml.safe_load(open(yamlfile))
    return data

add_test_data = get_data_via("../datas/add_test.yaml")
div_test_data = get_data_via("../datas/div_test.yaml")

calctest = Calc()

class TestCalc:

    @pytest.mark.parametrize("a,b,sum",add_test_data["normal"])
    def test_add_normal(self,a,b,sum):
        assert sum == calctest.add(a,b)

    @pytest.mark.parametrize("a,b,div",div_test_data["normal"])
    def test_div_normal(self,a,b,div):
        print(round((div - calctest.div(a, b)), 4))
        assert abs(round((div - calctest.div(a,b)),4)) < 0.001




if __name__ == "__main__":
    pytest.main(["-vs"])


