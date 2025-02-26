import pytest
from decision_tree import *

def test_detects_purity():
    d = [Datum(True)]
    assert impurity(d) == pytest.approx(0.0)

def test_detects_even_impurity():
    d = [Datum(True)] * 5 + [Datum(False)] * 5
    assert impurity(d) == pytest.approx(0.5)

def test_detects_uneven_impurity():
    d = [Datum(True)] * 3 + [Datum(False)]
    assert impurity(d) == pytest.approx(6/16)

def test_computes_split_cost():
    result = split_cost(data, 'Raining', False)
    assert result == pytest.approx(0.4857, abs=0.001)

def test_computes_uneven_split_cost():
    result = split_cost(data, 'Patrons', 'Some')
    assert result == pytest.approx(0.25, abs=0.001)

def test_finds_best_split():
    a, v = best_split(data)
    assert a == 'Patrons'
    assert v == 'Some'

def test_predicts_all_training_examples_correctly():
    tree = Tree(data)
    for d in data:
        assert tree.predict(d) == d.target
