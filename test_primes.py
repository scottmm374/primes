from primes import create_primes_list


def test_prime_list_qty():
    assert create_primes_list(10) == 4
    assert create_primes_list(100) == 25
    assert create_primes_list(1000) == 168
    assert create_primes_list(10000) == 1229
    assert create_primes_list(100000) == 9592
    # assert create_primes_list(10) == 5    Used to fail test
   
     