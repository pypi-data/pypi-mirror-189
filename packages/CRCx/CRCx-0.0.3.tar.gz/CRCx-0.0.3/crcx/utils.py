import typing as _tp


def bits(n: int) -> int:
	return (1 << n) - 1


def left(n: int) -> _tp.Callable[[int, ], int]:
	if n < 0:
		n = -n

		def shift(x: int) -> int:
			return x >> n

	else:
		def shift(x: int) -> int:
			return x << n

	return shift


def right(n: int) -> _tp.Callable[[int, ], int]:
	if n < 0:
		n = -n

		def shift(x: int) -> int:
			return x << n

	else:
		def shift(x: int) -> int:
			return x >> n

	return shift


if __name__ == '__main__':
	a = right(1)(1)
	print(bin(a))


def logical_reverse(source: int, length: int):
	r = 0
	for i in reversed(range(length)):
		r |= (1 & source) << i
		source >>= 1
	return r


def bit_reverse_n2(n: int):
	def f(x: int) -> int:
		r = 0
		for i in reversed(range(n)):
			r |= (1 & x) << i
			x >>= 1
		return r
	return f


def norm(data):
	if isinstance(data, str):
		return (ord(c) for c in data)
	return data


def bit_reverse_byte(byte):
	"""Bit-bashing reversal of a byte"""
	result = 0
	for i in range(8):
		if byte & (1 << i):
			result |= 1 << (7 - i)
	return result & 0xFF


def bit_reverse_n(n) -> _tp.Callable[[int, ], int]:
	"""
	Mirror the bits in an integer
	"""

	def f(x: int) -> int:
		# This left shift will introduce zeroes in the least-significant bits, which
		# will be ignored 0 ms bits once we bit reverse
		x <<= (8 - n) & 7
		num_bytes = (n + 7) >> 3
		result = 0
		for _ in range(num_bytes):
			result <<= 8
			result |= _REV8BITS[x & 0xFF]
			x >>= 8
		return result

	return f


# Table of bit-reversed bytes, initialised on loading
_REV8BITS = [bit_reverse_byte(_n) for _n in range(256)]


def concat(*its):
	"""joins iterables together"""
	for it in its:
		yield from it


def apply(fns):
	def f(it):
		return (fn(x) for fn, x in zip(fns, it))
	return f


def order(*args, seq_t=tuple):
	def g(n: int, it: iter):
		r = seq_t(v for i, v in zip(range(n), it))
		while len(r):
			yield r
			r = seq_t(v for i, v in zip(range(n), it))

	def f(it: _tp.Iterable):
		it = iter(it)
		for n in args:
			it = g(n, it)
		return seq_t(it)

	return f


def hexpad(s: str, n: int):
	a, b = s[:2], s[2:]
	zeros = n - len(b)
	return f"{a}{''.join('0' for _ in range(zeros))}{b}"


def strjoin(it):
	return "".join(it)
