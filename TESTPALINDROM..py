from palindrome import is_palindrome

def test_for_palindrome_return_true():

	assert is_palindrome('dad') = true
	assert is_palindrome('12121 ') ==false
	assert is_palindrome('neveroddoreven')

def test_for_palindrome_return_false():

	assert is_palindrome('ball') = false
	assert is_palindrome("10111 ") ==false

def test_for_palindrome_return_false():

	assert is_palindrome('10') = false
	assert is_palindrome('10.5 ') ==false