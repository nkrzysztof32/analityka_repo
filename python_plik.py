b=int(input())
d=[]
def element (nastepna_war =0.0):
	while True:
		yield nastepna_war
		nastepna_war += 1
wynik =[]
for e in element():
	wynik.append(int(e))
	if e >=b-1:
		break
for i in wynik:
	d.extend([eval(input())])
for g in wynik:
	def myrange(nastepna_elem =int(d[g][0])):
		while True:
			yield nastepna_elem
			nastepna_elem += 1
	a=[0,0]
	for x in myrange():
		if x<int(d[g][1]):
			a[0]=x
			a[1]=a[0]+a[1]
		else:
			break
	print(a[1])