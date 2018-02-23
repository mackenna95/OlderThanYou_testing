def test_sum_function():
    import pytest
    from number_manipulation import NumberManipulation
    output = NumberManipulation([5])
    assert output.limits == 5
    #case_one = return_sum([5])
    output = NumberManipulation([3, 7, -2])
    assert output.limits == 8
    #case_two = return_sum([3, 7, -2])
    output = NumberManipulation([-6, -90, -40, 26])
    assert output.limits == -110
    #case_three = return_sum([-6, -90, -40, 26])
    tollerance = 0.00000001
    output = NumberManipulation([6.9, 3.2, -4])
    assert output.limits == - 6.1 < tollerance
    #case_four = return_sum([6.9, 3.2, -4])
    output = NumberManipulation([-3.2, -1.8, -9.36, -872])
    assert output.limits == + 886.36 < tollerance
    #case_five = return_sum([-3.2, -1.8, -9.36, -872])
    

    #assert case_one == 5
    #assert case_two == 8
    #assert case_three == -110
    # vertikoff - setting tollerance threshold here
    #tollerance = 0.00000001
    #assert case_four - 6.1 < tollerance
    #assert case_five + 886.36 < tollerance

    pytest.raises(TypeError, NumberManipulation, (8, "str"))
    #with pytest.raises(TypeError):
    #    return_sum(8, "str")
    pytest.raises(ValueError, NumberManipulation, [])
    #with pytest.raises(ValueError):
    #    return_sum([])
