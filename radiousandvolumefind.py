from radious import area_of_circle
from radious import volume_of_sphere

r=int(input("enter a number: "))
print(area_of_circle(r))
area_of_radious=area_of_circle(r)
vs=4/3*area_of_radious*r
print(vs)

volume_of_sphere(r)
print(volume_of_sphere(r))

