import copy

class ord:
	def check(val):
		if type(val) == list:
			return all(ord.check(x) for x in val)
		return False
	def le(a, b):
		if a == []:
			return True
		if b == []:
			return False
		if a[0] == b[0]:
			return ord.le(a[1:],b[1:])
		if ord.le(a[0],b[0]):
			return True
		return False
	def str(a):
		if a == []:
			return "0"
		if len(a) == 1:
			return "\u03c9^"+ord.str(a[0])
		return "("+"+".join(ord.str([x]) for x in a)+")"
	def call(a,n):
		assert(type(n)==int and n >= 0)
		if a == []:
			return []
		if a[-1] == []:
			return a[:-1]
		if a[-1][-1] == []:
			return a[:-1] + [a[-1][:-1]]*n
		return a[:-1] + [ord.call(a[-1],n)]
	def __init__(self, *val):
		val = list(val)
		assert(ord.check(val))
		self.val = []
		curr_max = 0
		for a in val:
			if curr_max != 0 and ord.le(a,curr_max):
				self.val.append(curr_max)
				if a != curr_max:
					curr_max = 0
			curr_max = a
		if len(val) > 0:
			self.val.append(val[-1])
	def __le__(self,other):
		return ord.le(self.val,other.val)
	def __lt__(self,other):
		return ord.le(self.val,other.val) and self.val != other.val
	def __str__(self):
		res = ord.str(self.val).replace("\u03c9^0","1").replace("^1","")
		while res[0] == "(" and res[-1] == ")":
			res = res[1:-1]
		return res
	def __call__(self,n):
		return ord(*ord.call(self.val,n))
	def is_zero(self):
		return self.val == []
	def is_succ(self):
		return self.val[-1] == []
	def is_limit(self):
		return len(self.val) > 0 and self.val[-1] != []
	def is_finite(self):
		return self < ord([[]])
	def predec(self):
		assert(self.is_succ())
		return ord(*self.val[:-1])
	def __add__(self,other):
		assert(type(other)==ord)
		return ord(*(self.val+other.val))

def fgh_helper(a,n,k):
	if k > 1:
		return fgh_helper(a,fgh_helper(a,n,k-1),1)
	if a.is_zero():
		return n+1
	if k == 0:
		return n
	if a.is_succ():
		return fgh_helper(a.predec(),n,n)
	return fgh_helper(a(n),n,1)

omega = ord([[]])

# fast-growing hierarchy
def fgh(a,n):
	assert(type(a) == ord)
	assert(type(n) == int and n >= 0)
	return fgh_helper(a,n,1)

a = ord([],[])
n = 7
print("fgh(%s,%d) = %d" % (a,n,fgh(a,n)))
a = omega
n = 2
print("fgh(%s,%d) = %d" % (a,n,fgh(a,n)))
a = ord([])
b = omega
print("%s + %s = %s" % (a,b,a+b))
