from primes import create_primes_list
# , calc_lines, create_matrix_prime


# Test qty of primes within a specific range for accuracy. Tests pass
def test_prime_list_qty():
    assert create_primes_list(10) == 4
    assert create_primes_list(100) == 25
    assert create_primes_list(1000) == 168
    assert create_primes_list(10000) == 1229
    assert create_primes_list(100000) == 9592
    # assert create_primes_list(10) == 5    Used to fail test



# def test_row_inclusive_range():
#     assert calc_lines(2000, 54) == 38
#     assert calc_lines(5000, 54) == 93
#     assert calc_lines(2000, 18) == 112
#     assert calc_lines(5000, 18) == 277
#     assert calc_lines(2000, 27) == 75
#     assert calc_lines(5000, 27) == 186
#     assert calc_lines(2000, 36) == 56
#     assert calc_lines(5000, 36) == 139

   
     