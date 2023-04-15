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


def values(resistors):
    print(resistors)


if __name__ == '__main__':
    values(resistor_values_K)
