def func(x: float) -> float:
	return (x**2)-16

# A - pierwsza współrzędna boku położonego na osi X
# B - druga współrzędna boku położonego na osi X
# func - funkcja matematyczna, którą ograniczamy pole
# mid - środek boku |AB|
# sideX - długość boku położonego na osi X
# sideY - długość pionowego boku prostokąta 

def rect_area(A: float, B: float, func) -> float:
	mid = (A + B) / 2
	sideX = B - A
	sideY = func(mid)
	return sideX * sideY

# A - początek przedziału
# B - koniec przedziału
# n - dokładność wyniku (im większa wartość n, tym dokładniejszy wynik)
# func - funkcja matematyczna, którą ograniczamy pole

def func_area(A: float, B: float, func, n: int) -> float:
	area = 0
	sideX = (B - A) / n
	for i in range(0,n):
		area += rect_area(A + sideX * i, A + sideX * (i+1), func)
	return abs(area)

print(func_area(-4,4,func,1000000))
