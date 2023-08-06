import typing as _tp
from ...utils import bits, right, bit_reverse_n2
from ...models import ParamOpts
from .tables import calc_lsbf, calc_msbf


_reflect = bit_reverse_n2


def lsbf_init(reflect, width, seed):
	# For the parameters to make sense in the normal usage, the seed has to
	# be reflected here because this algorithm corresponds to a reflection
	# of the input data, which is implemented by a reflection of the lookup
	# table for performance improvement i.e. all the intermediate CRC values
	# are reflected so the same has to be done for the seed
	reflect_width = reflect(width)
	seed = reflect_width(seed)

	def f():
		return seed
	return f


def lsbf_process(table, width):
	"""table-optimized least-significant-bit-first process [data]"""
	mask_width = bits(width)

	def f(value, data):
		# this can be unrolled via functools.reduce, but reduce is slower
		#  probably due to repeated function calls
		for c in data:
			value = mask_width & ((value >> 8) ^ table[0xff & (value ^ c)])
		return value

	return f


def lsbf_final(reflect, width, xorout, refout):
	"""table-optimized least-significant-bit-first final [crc value]"""
	reflect_width = reflect(width)

	if refout:
		def f(value):
			# this is a weird corner case where the output is reflected but the
			#  input isn't
			value = reflect_width(value)
			return value ^ xorout

	else:
		def f(value):
			return value ^ xorout

	return f


def lsbf(reflect, table, width, seed, xorout, refout):
	"""table-optimized least-significant-bit-first
		implies ref[lect]in[put]
		new data shifted in from msb of calculation register"""
	init = lsbf_init(reflect, width, seed)
	process = lsbf_process(table, width)
	final = lsbf_final(reflect, width, xorout, refout)

	def f(s: _tp.Iterable[int]) -> int:
		return final(process(init(), s))

	return init, process, final


def msbf_init(seed):
	def f():
		return seed
	return f


def msbf_process(table, width, refout):
	"""table-optimized most-significant-bit-first process [data]"""
	mask_width = bits(width)
	msb_lshift = width - 8
	shift = right(msb_lshift)

	if refout:
		# in the case of refout == True, msb_lshift > 0
		#  negative rshift causes exception
		def f(remainder, data):
			# this can be unrolled via functools.reduce, but reduce is slower
			for c in data:
				remainder = mask_width & ((remainder << 8) ^ table[(remainder >> msb_lshift) ^ c])
			return remainder

	else:
		def f(remainder, data):
			# this can be unrolled via functools.reduce, but reduce is slower
			for c in data:
				remainder = mask_width & ((remainder << 8) ^ table[shift(remainder) ^ c])
			return remainder

	def g(remainder, data):
		# this can be unrolled via functools.reduce, but reduce is slower
		for c in data:
			remainder = mask_width & ((remainder << 8) ^ table[shift(remainder) ^ c])
		return remainder

	return g


def msbf_final(reflect, width, xorout, refout):
	"""table-optimized least-significant-bit-first final [crc value]"""
	reflect_width = reflect(width)

	if refout:
		def f(remainder):
			remainder = reflect_width(remainder)
			return remainder ^ xorout

	else:
		def f(remainder):
			return remainder ^ xorout

	return f


def msbf(reflect, table, width, seed, xorout, refout):
	"""table-optimized least-significant-bit-first
		implies not ref[lect]in[put]
		new data shifted in from lsb of calculation register"""
	init = msbf_init(seed)
	process = msbf_process(table, width, refout)
	final = msbf_final(reflect, width, xorout, refout)

	def f(s: _tp.Iterable[int]) -> int:
		return final(process(init(), s))

	return init, process, final


def create(reflect, poly, width, seed, ref_in=True, ref_out=True, name="", xor_out=0xFFFFFF):
	"""Create a table-driven CRC calculation engine

	:param poly: polynomial
	:param width: polynomial width in bits
	:param seed: seed value for the CRC calculation to use
	:param ref_in:  reflect input bits
	:param ref_out: reflect output bits
	:param name: associate a name with this algorithm
	:param xor_out:  exclusive-or the output with this value
	:return:
	"""
	if ref_in:
		table = calc_lsbf(reflect, poly, width)
		params = table, name, width, poly, seed, xor_out, None, ref_in != ref_out
		algorithm = lsbf(*params)
	else:
		table = calc_msbf(poly, width)
		params = table, name, width, poly, seed, xor_out, ref_in, ref_out
		algorithm = msbf(params)
	return algorithm


"""
additional data needed
	table gen fns
		lsbf/msbf
	bitwise reverse fn
"""


class Engine(_tp.NamedTuple):
	init: _tp.Callable[[], int]
	process: _tp.Callable[[int, _tp.Iterable[int]], int]
	final: _tp.Callable[[int, ], int]


def get_keys(d: dict, keys):
	return (d.get(k, None) for k in keys)


def new(params):
	table, poly, width, init, xorout, refin, refout = get_keys(
		params,
		(ParamOpts.table, ParamOpts.poly, ParamOpts.width, ParamOpts.seed,
		 ParamOpts.xor, ParamOpts.refin, ParamOpts.refout)
	)

	reflect = _reflect

	if refin:
		if not table:
			table = calc_lsbf(reflect, poly, width)
		fns = lsbf(reflect, table, width, init, xorout, refin != refout)
	else:
		if not table:
			table = calc_msbf(poly, width)
		fns = msbf(reflect, table, width, init, xorout, refout)

	r = Engine(*fns)
	return r
