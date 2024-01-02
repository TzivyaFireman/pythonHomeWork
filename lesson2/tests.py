import pytest
import interesting


@pytest.mark.parametrize('num1,num2,result', [(1, 4, {1, 2, 3}), (5, 7, {5}), ('a', 4, [6, 7, 8, 9])])
def test_find_primes(num1, num2, result):
    assert interesting.find_primes(num1, num2) == result



@pytest.mark.parametrize('list1,result',[([1,3,2,8,7,56],[1,2,3,7,8,56]),('e',4) ])
def test_sort_list(list1, result):
    assert interesting.sort_list(list1) == result


@pytest.mark.sara
def test_sort_list():
    assert interesting.sort_list([1,3,2,8,7,56]) == [1,2,3,7,8,56]



