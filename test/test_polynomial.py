from polynomial import *

def test_generates_five_coefficients():
    assert len(generate_coefficients()) == 5

def test_coefficients_are_in_proper_range():
    d = np.array(generate_coefficients())
    assert (d >= -0.5).all()
    assert (d < 0.5).all()

def test_generates_evenly_spaced_x_values():
    x, y = generate_data(5, [1, 2, 0, 0, 1])
    assert (x == np.array([-5.0, -2.5, 0, 2.5, 5.0]).reshape(5, 1)).all()

def test_y_values_have_proper_range():
    x, y = generate_data(1000, [1, 2, 0, 0, 1])
    correct_y = 1 + 2 * x + x ** 4
    # The following are all extremely likely
    assert not (y == correct_y).any()
    assert (correct_y - 4 < y).all()
    assert (y < correct_y + 4).all()
