from ..utils import _REV8BITS
from ..tables import *


bitrevfn = bit_reverse_n2


# names
#  generic/standard
def msbf(params):
	"""
	Generic most-significant-bit-first non-table-driven CRC calculation, allows
	unusual (and probably not useful) combinations of parameters such as
	reflecting the input without reflecting the output
	"""

	table, name, width, poly, init, xorout, refin, refout, *_ = params
	mask = bits(width)
	msbit = 1 << (width - 1)
	msb_lshift = width - 8

	def f(data: bytes):
		crc = init
		for byte in data:
			if refin:
				reflect_byte = _REV8BITS[byte]
				byte = reflect_byte
			crc ^= byte << msb_lshift
			for _ in range(8):
				if crc & msbit:
					crc = (crc << 1) ^ poly
				else:
					crc <<= 1
			crc &= mask
		if refout:
			crc = bitrevn(width)(crc)
		return crc ^ xorout

	return f


# this is implemented in crcengine but we haven't quite got it to pass our
#  tests yet
def lsbf(params):
	"""
	General purpose CRC calculation using LSB algorithm. Mainly here for
	reference, since the other algorithms cover all useful calculation
	combinations
	"""

	table, name, width, _poly, init, xorout, refin, refout, *_ = params
	mask = bits(width)

	def f(data: bytes):
		crc = init
		if refin:
			poly = bitrevn(width)(_poly)
		else:
			poly = _poly
		for byte in data:
			if refin:
				byte = _REV8BITS[byte]
			crc ^= byte
			for _ in range(8):
				if crc & 1:
					crc = (crc >> 1) ^ poly
				else:
					crc >>= 1
			crc &= mask
		if refout:
			crc = bitrevn(width)(crc)
		return crc ^ xorout

	return f


def create_generic(
		poly, width, seed, ref_in=True, ref_out=True, name="", xor_out=0xFFFFFF
):
	"""Create generic non-table-driven CRC calculator

	:param poly: Polynomial
	:param width: calculator width in bits e.g. 32
	:param seed: calculation seed value
	:param ref_in: reflect incoming bits
	:param ref_out: reflect result bits
	:param name: name to assign to calculator
	:param xor_out: pattern to XOR into result
	:return: A CRC calculation engine
	"""
	params = None, name, width, poly, seed, xor_out, ref_in, ref_out
	algo = msbf(params)
	return algo


def create_generic_lsbf(
		poly, width, seed, ref_in=True, ref_out=True, name="", xor_out=0xFFFFFF
):
	"""Create a CRC calculation engine that uses the Least-significant first
	algorithm, but does not reflect the polynomial. If you use this, reflect
	the polynomial before passing it in"""
	params = None, name, width, poly, seed, xor_out, ref_in, ref_out
	algo = lsbf(params)
	return algo
