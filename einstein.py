def main():
    m = int(input("type mass: "))
    print(energy(m))

def energy(mass_kgs):
    c = 300000000
    return mass_kgs * c**2

main()
