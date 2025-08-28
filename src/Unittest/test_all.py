import pytest  # type: ignore
from Data_Processor.Function_Selector import FunctionSelector
from Data_Processor.Test_Mapper import TestMapper

def test_function_selector_best_match():
    train = {"x": [1, 2, 3], "y1": [1, 2, 3]}
    ideal = {
        "x": [1, 2, 3],
        "y1": [1, 2, 3],   
        "y2": [10, 20, 30] }
    fs = FunctionSelector(train, ideal)
    selected = fs.select_best_ideal_function()
    max_dev = fs.get_max_deviations()
    assert selected["y1"] == "y1"
    assert max_dev["y1"] == 0

def test_mapper_mapping():
    train = {"x": [1, 2, 3], "y1": [1, 2, 3]}
    ideal = {"x": [1, 2, 3], "y1": [1, 2, 3]}
    test = {"x": [1, 2], "y": [1, 2]} 
    fs = FunctionSelector(train, ideal)
    selected = fs.select_best_ideal_function()
    max_dev = fs.get_max_deviations()
    mapper = TestMapper(test, ideal, selected, max_dev)
    results = mapper.map_test_data()
    assert len(results) == 2
    for r in results:
        assert r["ideal_function_no"] == "Y1"
        assert r["delta_y"] == 0
