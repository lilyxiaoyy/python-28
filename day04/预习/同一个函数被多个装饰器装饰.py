def wrapper1(fn):
	def inner(*args, **kwargs):
		print("before wrapper1")
		ret = fn(*args, **kwargs)
		print("before wrapper1")
		return ret

	return inner


def wrapper2(fn):
	def inner(*args, **kwargs):
		print("before wrapper2")
		ret = fn(*args, **kwargs)
		print("before wrapper2")
		return ret

	return inner


def wrapper3(fn):
	def inner(*args, **kwargs):
		print("before wrapper3")
		ret = fn(*args, **kwargs)
		print("before wrapper3")
		return ret

	return inner


@wrapper1
@wrapper2
@wrapper3
def func():
	print("target function")


func()