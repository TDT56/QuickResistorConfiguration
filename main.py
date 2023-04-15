# This script give different configurations of resistor to obtain the required value.
'''
Configuration of three resistors is calculated to give a resistance value close to the required value.

Example: 100||200-300

100||200||300

100-200-300
'''


E_1 = [1, 1.2, 2.2, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
E_2 = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]
E_3 = [100, 120, 150, 220, 270, 330, 390, 470, 560, 680, 820]
resistor_values_E = E_1 + E_2 + E_3

K_1 = [1, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
K_2 = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]
K_3 = [100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 820]
resistor_values_K = [x * 1000 for x in (K_1 + K_2 + K_3)]

finite_resistor_values = [1, 2200]


def values(resistors):
    print(resistors)


def process() -> object:
    print('The scripts description is at the top of this file.\n'
          '---------------------------------------------------\n')

    response = input("Type '1' to use the E and K resistor values or type '2' to use the finite_resistor_values\n"
                     "1 - E and K resistors\n"
                     "2 - Finite resistors\n")

    if response == '1':
        print('Selected E and K resistors')

    elif response == '2':
        print('Selected finite resistors')

    else:
        print('Invalid option!')


def finite_calculations():
    pass


def non_finite_calculations():
    pass


if __name__ == '__main__':
    process()