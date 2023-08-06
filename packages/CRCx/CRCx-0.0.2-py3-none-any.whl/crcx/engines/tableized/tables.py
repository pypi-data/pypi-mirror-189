from ...utils import bits


def calc_msbf_sequential(poly, width):
	"""Generate a CRC table calculating each entry.
	Mainly for demonstration and test, since calculate_msb_table() is
	much more efficient at calculating the same information
	:return: Generated table
	"""
	def f():
		msb_lshift = width - 8
		ms_bit = 1 << (width - 1)
		mask = bits(width)
		# table = 256 * [0]
		yield 0
		for n in range(1, 256):
			crc = n << msb_lshift
			for _ in range(8):
				if crc & ms_bit:
					crc = (crc << 1) ^ poly
				else:
					crc <<= 1
			# table[n] = crc & mask
			yield crc & mask
	return tuple(f())


def calc_msbf(poly, width):
	"""Calculate a CRC lookup table for the selected algorithm definition
	:return: list of CRC values
	"""
	ms_bit = 1 << (width - 1)
	mask = bits(width)
	# Preallocate entries to 0
	table = 256 * [0]
	# this is essentially the '1' shifted left by the number of
	# bits necessary for it to reach the msbit of the remainder value
	crc = ms_bit
	# i is the index of the table that is being computed this loop
	i = 1
	while i <= 128:
		# Each (1<<n) must have the polynomial applied to it n+1 times
		# since 1 must be shifted left 7 times before a non-zero bit is in
		# the msb, there are no more shifts to be done
		# 2 requires 6 shifts for a non-zero bit in the msbit, so the msbit
		# test (and conditional polynomial xor) is applied once more
		# 4 requires 5 shifts for a non-zero bit in the msbit, so the
		# the msb test is applied three times.
		# We take advantage of this property by reusing the result for n
		# in the calculation of the result for 2n
		if crc & ms_bit:
			crc = (crc << 1) ^ poly
		else:
			crc <<= 1
		crc &= mask
		# because all operations are xors the following holds:
		# table[i ^ j] == table[i] ^ table[j]
		# The result for n can be combined with all the results for 0..(n-1)
		# to determine the (n+1)..(2n-1) th entries without any further
		# calculation
		# since i is a power of 2 and always larger than j
		# i + j == i ^ j
		for j in range(0, i):
			table[i + j] = table[j] ^ crc
		i <<= 1
	return tuple(table)


def calc_lsbf(reflect, poly, width):
	"""Calculate a CRC lookup table for the selected algorithm definition
	producing a table that can be used for the lsbit algorithm

	:return: table of reflected
	"""
	table = 256 * [0]
	crc = 1
	# i is the index of the table that is being computed this loop
	# the lsb table contains an implicit reflection of the data byte so
	# '1' is a reflected 128
	# The algorithm starts from this value because in an lsb-first VRV the poly
	#  will only be applied to it once, so we can compute it without iteration
	i = 0x80
	poly = reflect(width)(poly)
	# On iteration we compute index positions 128, 64, 32 ...
	# this can be done with a single application of the polynomial bit test
	# since we know only one bit is set. We re-use the value of index 2n to
	# calculate n
	while i > 0:
		# Apply the test for lsb set and the (reflected) polynomial
		# to bits shifting in from the left
		# so the first tests 0x80 >> 7, the second iteration re-uses this to
		# represent application 0x40 >> 6 and then applies the test again
		# for the remaining shift etc.
		if crc & 1:
			crc = (crc >> 1) ^ poly
		else:
			crc >>= 1
		# Having computed the value of a power of 2 entry, we can combine
		# it with the values from the (larger) power of 2 entries that have
		# been already calculated, this can be done because
		#  table[i + j] == table[i] ^ table[j]
		for j in range(0, 256, 2 * i):
			table[i + j] = crc ^ table[j]
		i >>= 1
	return tuple(table)
