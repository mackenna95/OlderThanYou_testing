def test_limits_function():
    from number_manipulation import NumberManipulation
    import pytest

    pytest.raises(TypeError, NumberManipulation, (1, 2, 3))
    #with pytest.raises(TypeError):
    #    return_limits((1, 2, 3))
    pytest.raises(ValueError, NumberManipulation, [])
    #with pytest.raises(ValueError):
    #    return_limits([])
    pytest.raises(TypeError, NumberManipulation, [1, 's'])
    #with pytest.raises(TypeError):
    #    return_limits([1, 's'])

    output = NumberManipulation([5])
    assert output.limits == (5,5)
    #output = return_limits([5])
    #assert output == (5, 5)

    #output = NumberManipulation([-1, -3, 4, 0, 2])
    #assert output.limits == (-3, 4)
    #output = return_limits([-1, -3, 4, 0, 2])
    #assert output == (-3, 4)

    #tolerance = 0.00000001
    #output = NumberManipulation([3.3, -5.7, 9, -6.7])
    #assert output.limits[0] + 6.7 < tolerance
    #assert output.limits[1] - 9 < tolerance
    
    #output = return_limits([3.3, -5.7, 9, -6.7])
    #assert output[0] + 6.7 < tolerance
    #assert output[1] - 9 < tolerance
    #comment for travis

    pass
