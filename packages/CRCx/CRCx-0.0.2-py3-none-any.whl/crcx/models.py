import typing as _tp
import enum as _en


class OldParams(_tp.NamedTuple):
	"""
	width, poly, init, xor_out, ref_in, ref_out
	name, width, poly, xorin, xorout, refin, refout
	"""
	width: int
	poly: int
	init: int
	xor_out: int
	ref_in: bool
	ref_out: bool
	check: int = None
	residue: int = None


class Params(_tp.NamedTuple):
	"""
	width, poly, init, xor_out, ref_in, ref_out
	name, width, poly, xorin, xorout, refin, refout
	"""
	name: str
	width: int
	poly: int
	init: int
	xor_out: int
	ref_in: bool
	ref_out: bool
	check: int = None
	residue: int = None


# class
class Engine:
	pass


class Table(_tp.NamedTuple):
	"""
	params, values
	"""
	params: Params
	values: tuple


class ParamOpts(_en.Enum):
	# description
	name = 0
	aliases = _en.auto()
	desc = _en.auto()
	# table
	table = _en.auto()
	# params
	width = _en.auto()
	poly = _en.auto()
	seed = _en.auto()  # init/seed
	xor = _en.auto()  # xorout/xor
	refin = _en.auto()
	refout = _en.auto()
	# checks
	check = _en.auto()
	residue = _en.auto()

	def __int__(self):
		return self.value

	def __str__(self):
		return self.name
