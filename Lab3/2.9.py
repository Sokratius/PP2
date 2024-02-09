def volume_of_sphere(cradius):
    radius = (4/3*3.14)*cradius**3
    return radius


radius = int(input('Enter the radius of sphere: '))
print(volume_of_sphere(radius))