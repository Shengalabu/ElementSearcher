import os
import time

def clear_console():
        os.system('cls')
        
def delay(seconds):
    time.sleep(seconds)

def print_details(atomic_mass, standard_state, electron_configuration, oxidation_states, electronegativity,
                  atomic_radius,
                  ionization_energy, electron_affinity, melting_point, boiling_point, density, year_discovered):
    print("Atomic Mass:", atomic_mass,
          "\nStandard State:", standard_state,
          "\nElectron Configuration:", electron_configuration,
          "\nOxidation States:", oxidation_states,
          "\nElectronegativity (Pauling Scale):", electronegativity,
          "\nAtomic Radius (van der Waals):", atomic_radius,
          "\nIonization Energy:", ionization_energy,
          "\nElectron Affinity:", electron_affinity,
          "\nMelting Point:", melting_point,
          "\nBoiling Point:", boiling_point,
          "\nDensity:", density,
          "\nYear Discovered:", year_discovered)
    ask_user_to_continue()

def ask_user_to_continue():
    delay(0.5)
    print("-------------------------------")
    print("Would you like to search again?")
    user_input = input("(y/n): ").lower()
    print(user_input)
    if user_input == "y":
        clear_console()
        show_menu()
    if user_input == "n":
        close_app()
    print("Invalid input | resuming program")
    delay(1)
    show_menu()

def close_app():
    clear_console()
    print("Closing App.")
    delay(0.25)
    clear_console()
    print("Closing App..")
    delay(0.2)
    clear_console()
    print("Closing App..")
    delay(0.1)
    clear_console()
    quit()

def check_element(user_input, atomic_symbol, atomic_number, atomic_name):
    if (user_input == atomic_symbol.lower()) or (user_input == atomic_number.lower()) or (
            user_input == atomic_name.lower()):
        print("---------- ELEMENT DETAILS ----------")
        print("Atomic Name:", atomic_name)
        print("Atomic Symbol:", atomic_symbol)
        print("Atomic Number:", atomic_number)

        return True
    if user_input == "x":
        close_app()

def main_menu():
    count = 1
    periodic_table_elements = {
        "H": "Hydrogen", "He": "Helium", "Li": "Lithium", "Be": "Beryllium", "B": "Boron", "C": "Carbon",
        "N": "Nitrogen", "O": "Oxygen", "F": "Fluorine", "Ne": "Neon", "Na": "Sodium", "Mg": "Magnesium",
        "Al": "Aluminum", "Si": "Silicon", "P": "Phosphorus", "S": "Sulfur", "Cl": "Chlorine", "Ar": "Argon",
        "K": "Potassium", "Ca": "Calcium", "Sc": "Scandium", "Ti": "Titanium", "V": "Vanadium", "Cr": "Chromium",
        "Mn": "Manganese", "Fe": "Iron", "Co": "Cobalt", "Ni": "Nickel", "Cu": "Copper", "Zn": "Zinc",
        "Ga": "Gallium", "Ge": "Germanium", "As": "Arsenic", "Se": "Selenium", "Br": "Bromine", "Kr": "Krypton",
        "Rb": "Rubidium", "Sr": "Strontium", "Y": "Yttrium", "Zr": "Zirconium", "Nb": "Niobium", "Mo": "Molybdenum",
        "Tc": "Technetium", "Ru": "Ruthenium", "Rh": "Rhodium", "Pd": "Palladium", "Ag": "Silver", "Cd": "Cadmium",
        "In": "Indium", "Sn": "Tin", "Sb": "Antimony", "Te": "Tellurium", "I": "Iodine", "Xe": "Xenon", "Cs": "Cesium",
        "Ba": "Barium", "La": "Lanthanum", "Ce": "Cerium", "Pr": "Praseodymium", "Nd": "Neodymium", "Pm": "Promethium",
        "Sm": "Samarium", "Eu": "Europium", "Gd": "Gadolinium", "Tb": "Terbium", "Dy": "Dysprosium", "Ho": "Holmium",
        "Er": "Erbium", "Tm": "Thulium", "Yb": "Ytterbium", "Lu": "Lutetium", "Hf": "Hafnium", "Ta": "Tantalum",
        "W": "Tungsten", "Re": "Rhenium", "Os": "Osmium", "Ir": "Iridium", "Pt": "Platinum", "Au": "Gold",
        "Hg": "Mercury", "Tl": "Thallium", "Pb": "Lead", "Bi": "Bismuth", "Po": "Polonium", "At": "Astatine",
        "Rn": "Radon", "Fr": "Francium", "Ra": "Radium", "Ac": "Actinium", "Th": "Thorium", "Pa": "Protactinium",
        "U": "Uranium", "Np": "Neptunium", "Pu": "Plutonium", "Am": "Americium", "Cm": "Curium", "Bk": "Berkelium",
        "Cf": "Californium", "Es": "Einsteinium", "Fm": "Fermium", "Md": "Mendelevium", "No": "Nobelium", "Lr": "Lawrencium",
        "Rf": "Rutherfordium", "Db": "Dubnium", "Sg": "Seaborgium", "Bh": "Bohrium", "Hs": "Hassium", "Mt": "Meitnerium",
        "Ds": "Darmstadtium", "Rg": "Roentgenium", "Cn": "Copernicium", "Nh": "Nihonium", "Fl": "Flerovium", "Mc": "Moscovium",
        "Lv": "Livermorium", "Ts": "Tennessine", "Og": "Oganesson"
    }
    print("////////// THE PERDIODIC TABLE //////////")
    delay(0.5)
    for key, value in periodic_table_elements.items():
        print(count,f":{key} :{value}")
        delay(0.01)
        count += 1
    show_menu()
        
def show_menu():
    print("[[[[[[[[[[[ ELEMENT SEARCHER ]]]]]]]]]]]")
    print("Type 'x' to exit")
    search_element(input("Search for an element (Symbol, Number, Name): ").lower())

def search_element(user_input):
    clear_console()
    if check_element(user_input, "H", "1", "Hydrogen"):
        print_details("1.0080 u", "Gas", "1s1", "+1, -1", "2.2", "120 pm", "13.598 eV", "0.754 eV", "13.81 K",
                      "20.28 K", "0.00008988 g/cm³", " 1766")
    if check_element(user_input, "He", "2", "Helium"):
        print_details("4.00260 u", "Gas", "1s2", "0", "None", "140 pm", "13.598 eV", "None", "0.95 K",
                      "4.22 K", "0.0001785 g/cm³", "1766")
    if check_element(user_input, "li", "3", "lithium"):
        print_details("7.0 u", "Solid", "[He]2s^1", "+1", "0.98", "182 pm", "5.392 eV", "  0.618 eV", "453.65 K",
                      "1615 K", "0.534 g/cm³", "1817")
    if check_element(user_input, "Be", "4", "Beryllium"):
        print_details("9.012183 u", "Solid", "[He]2s2", "+2", "1.57", "153 pm", "9.323 eV", "None", "1560 K",
                      "2744 K", "1.85 g/cm³", "1798")
    if check_element(user_input, "B", "5", "Boron"):
        print_details("10.81 u", "Solid", "[He]2s22p1", "+3", "2.04", "192 pm", "8.298 eV", "0.277 eV", "2348 K",
                      "4273 K", "2.37 g/cm³", "1808")
    if check_element(user_input, "C", "6", "Carbon"):
        print_details("12.011 u", "Solid", "[He]2s22p2", "+4, +2, -4", "2.55", "170 pm", "11.260 eV", "1.263 eV", "3823 K",
                      "4098 K", "2.2670 g/cm³", "Ancient")
    if check_element(user_input, "N", "7", "Nitrogen"):
        print_details("14.007 u", "Gas", "[He]2s22p3", "+5, +4, +3, +2, +1, -1, -2, -3", "3.04", "155 pm", "14.534 eV", "None", "63.15 K",
                      "77.36 K", "0.0012506 g/cm³", "1772")
    if check_element(user_input, "O", "8", "Oxygen"):
        print_details("15.999 u", "Gas", "[He]2s22p4", "-2", "3.44", "152 pm", "13.618 eV", "1.461 eV", "54.36 K",
                      "90.2 K", "0.001429 g/cm³", "1774")
    if check_element(user_input, "F", "9", "Fluorine"):
        print_details("18.99840316 u", "Gas", "[He]2s22p5", "-1", "3.98", "135 pm", "17.423 eV", "3.339 eV", "53.53 K",
                      "85.03 K", "0.001696 g/cm³", "1670")
    if check_element(user_input, "Ne", "10", "Neon"):
        print_details("20.180 u", "Gas", "[He]2s22p6", "0", "None", "154 pm", "21.565 eV", "None", "24.56 K",
                      "27.07 K", "0.0008999 g/cm³", "1898")
    if check_element(user_input, "Na", "11", "Sodium"):
        print_details("22.9897693 u", "Solid", "[Ne]3s1", "+1", "0.93", "227 pm", "5.139 eV", "0.548 eV", "370.95 K",
                      "1156 K", "0.97 g/cm³", "1807")
    if check_element(user_input, "Mg", "12", "Magnesium"):
        print_details("24.305 u", "Solid", "[Ne]3s2", "+2", "1.31", "173 pm", "7.646 eV", "None", "923 K",
                      "1363 K", "1.74 g/cm³", "1808")
    if check_element(user_input, "Al", "13", "Aluminum"):
        print_details("26.981538 u", "Solid", "[Ne]3s23p1", "+3", "1.61", "184 pm", "5.986 eV", "0.441 eV", "933.437 K",
                      "2792 K", "2.70 g/cm³", "Ancient")
    if check_element(user_input, "Si", "14", "Silicon"):
        print_details("28.085 u", "Solid", "[Ne]3s23p2", "+4, +2, -4", "1.9", "210 pm", "8.152 eV", "1.385 eV", "1687 K",
                      "3538 K", "2.3296 g/cm³", "1854")
    if check_element(user_input, "P", "15", "Phosphorus"):
        print_details("30.97376200 u", "Solid", "[Ne]3s23p3", "+5, +3, -3", "2.19", "180 pm", "10.487 eV", "0.746 eV", "317.3 K",
                      "553.65 K", "1.82 g/cm³", "1669")
    if check_element(user_input, "S", "16", "Sulfur"):
        print_details("32.07 u", "Solid", "[Ne]3s23p4", "+6, +4, -2", "2.58", "180 pm", "10.360 eV", "2.077 eV", "388.36 K",
                      "717.75 K", "2.067 g/cm³", "Ancient")
    if check_element(user_input, "Cl", "17", "Chlorine"):
        print_details("35.45 u", "Gas", "[Ne]3s23p5", "+7, +5, +1, -1", "3.16", "175 pm", "12.968 eV", "3.617 eV", "171.65 K",
                      "239.11 K", "0.003214 g/cm³", "1774")
    if check_element(user_input, "Ar", "18", "Argon"):
        print_details("39.9 u", "Gas", "[Ne]3s23p6", "0", "None", "188 pm", "15.760 eV", "None", "83.8 K",
                      "87.3 K", "0.0017837 g/cm³", "1894")
    if check_element(user_input, "K", "19", "Potassium"):
        print_details("39.0983 u", "Solid", "[Ar]4s1", "+1", "0.82", "275 pm", "4.341 eV", "0.501 eV", "336.53 K",
                      "1032 K", "0.89 g/cm³", "1807")
    if check_element(user_input, "Ca", "20", "Calcium"):
        print_details("40.08 u", "Solid", "[Ar]4s2", "+2", "1", "231 pm", "6.113 eV", "None", "1115 K",
                      "1757 K", "1.54 g/cm³", "Ancient")

    if check_element(user_input, "Sc", "21", "Scandium"):
        print_details("44.95591 u", "Solid", "[Ar]4s23d1", "+3", "1.36", "211 pm", "6.561 eV", "0.188 eV", "1814 K",
                      "3109 K", "2.99 g/cm³", "1879")
        return
    if check_element(user_input, "Ti", "22", "Titanium"):
        print_details("47.867 u", "Solid", "[Ar]4s23d2", "+4, +3, +2", "1.54", "187 pm", "6.828 eV", "0.079 eV", "1941 K",
                      "3560 K", "4.5 g/cm³", "1791")
        return
    if check_element(user_input, "V", "23", "Vanadium"):
        print_details("50.9415 u", "Solid", "[Ar]4s23d3", "+5, +4, +3, +2", "1.63", "179 pm", "6.746 eV", "0.525 eV", "2183 K",
                      "3680 K", "6.0 g/cm³", "1801")
        return
    if check_element(user_input, "Cr", "24", "Chromium"):
        print_details("51.996 u", "Solid", "[Ar]3d54s1", "+6, +3, +2", "1.66", "189 pm", "6.767 eV", "0.666 eV", "2180 K",
                      "2944 K", "7.15 g/cm³", "1797")
        return
    if check_element(user_input, "Mn", "25", "Manganese"):
        print_details("54.93804 u", "Solid", "[Ar]4s23d5", "+7, +4, +3, +2", "1.55", "197 pm", "7.434 eV", "none", "1519 K",
                      "2334 K", "7.3 g/cm³", "1774")
        return
    if check_element(user_input, "Fe", "26", "Iron"):
        print_details(" 55.84 u", "Solid", "[Ar]4s23d6", "+3, +2", "1.83", "194 pm", "7.902 eV", "0.163 eV", "1811 K",
                      "3134 K", "7.874 g/cm³", "Ancient")
        return
    if check_element(user_input, "Co", "27", "Cobalt"):
        print_details("58.93319 u", "Solid", "[Ar]4s23d7", "+3, +2", "1.88", "192 pm", "7.881 eV", "0.661 eV", "1768 K",
                      "3200 K", "8.86 g/cm³", "1735")
        return
    if check_element(user_input, "Ni", "28", "Nickel"):
        print_details("58.693 u", "Solid", "[Ar]4s23d8", "+3, +2", "1.91", "163 pm", "7.640 eV", "1.156 eV", "1728 K",
                      "3186 K", "8.912 g/cm³", "1751")
        return
    if check_element(user_input, "Cu", "29", "Copper"):
        print_details("63.55 u", "Solid", "[Ar]4s13d10", "+2, +1", "1.9", "140 pm", "7.726 eV", "1.228 eV", "1357.77 K",
                      "2835 K", "8.933 g/cm³", "Ancient")
        return
    if check_element(user_input, "Zn", "30", "Zinc"):
        print_details("65.4 u", "Solid", "[Ar]4s23d10", "+2", "1.65", "139 pm", "9.394 eV", "none", "692.68 K",
                      "1180 K", "7.134 g/cm³", "1746")
        return
    if check_element(user_input, "Ga", "31", "Gallium"):
        print_details("69.723 u", "Solid", "[Ar]4s23d104p1", "+3", "1.81", "187 pm", "5.999 eV", "0.3 eV", "302.91 K",
                      "2477 K", "5.91 g/cm³", "1875")
        return
    if check_element(user_input, "Ge", "32", "Germanium"):
        print_details("72.63 u", "Solid", "[Ar]4s23d104p2", "+4, +2", "2.01", "211 pm", "7.900 eV", "1.35 eV", "1211.4 K",
                      "3106 K", "5.323 g/cm³", "1886")
        return
    if check_element(user_input, "As", "33", "Arsenic"):
        print_details("74.92159 u", "Solid", "[Ar]4s23d104p3", "+5, +3, -3", "2.18", "185 pm", "9.815 eV", "0.81 eV", "1090 K",
                      "887 K", "5.776 g/cm³", "Ancient")
        return
    if check_element(user_input, "Se", "34", "Selenium"):
        print_details("78.97 u", "Solid", "[Ar]4s23d104p4", "+6, +4, -2", "2.55", "190 pm", "9.752 eV", "2.021 eV", "493.65 K",
                      "958 K", "4.809 g/cm³", "1817")
        return
    if check_element(user_input, "Br", "35", "Bromine"):
        print_details("79.90 u", "Liquid", "[Ar]4s23d104p5", "+5, +1, -1", "2.96", "183 pm", "11.814 eV", "3.365 eV", "265.95 K",
                      "331.95 K", "3.11 g/cm³", "1826")
        return
    if check_element(user_input, "Kr", "36", "Krypton"):
        print_details("83.80 u", "Gas", "[Ar]4s23d104p6", "0", "3", "202 pm", "14.000 eV", "none", "115.79 K",
                      "119.93 K", "0.003733 g/cm³", "1898")
        return
    if check_element(user_input, "Rb", "37", "Rubidium"):
        print_details("85.468 u", "Solid", "[Kr]5s1", "+1", "0.82", "303 pm", "4.177 eV", "0.468 eV", "312.46 K",
                      "961 K", "1.53 g/cm³", "1861")
        return
    if check_element(user_input, "Sr", "38", "Strontium"):
        print_details("87.62 u", "Solid", "[Kr]5s2", "+2", "0.95", "249 pm", "5.695 eV", "none", "1050 K",
                      "1655 K", "2.64 g/cm³", "1790")
        return
    if check_element(user_input, "Y", "39", "Yttrium"):
        print_details("88.90584 u", "Solid", "[Kr]5s24d1", "+3", "1.22", "219 pm", "6.217 eV", "0.307 eV", "1795 K",
                      "3618 K", "4.47 g/cm³", "1794")
        return
    if check_element(user_input, "Z", "40", "Zirconium"):
        print_details("91.22 u", "Solid", "[Kr]5s24d2", "+4", "1.33", "186 pm", "6.634 eV", "0.426 eV", "2128 K",
                      "4682 K   ", "6.52 g/cm³", "1789")
    
    
    if check_element(user_input, "Nb", "41", "Niobium"):
        print_details("92.90637 u", "Solid", "[Kr]5s14d4", "+5, +3", "1.6", "207 pm", "6.759 eV", "0.893 eV", "2750 K",
                      "5017 K", "8.57 g/cm³", "1801")
        return
    if check_element(user_input, "Mo", "42", "Molybdenum"):
        print_details("95.95 u", "Solid", "[Kr]5s14d5", "+6", "2.16", "209 pm", "7.092 eV", "0.746 eV", "2896 K",
                      "4912 K", "10.2 g/cm³", "1778")
        return
    if check_element(user_input, "Tc", "43", "Technetium"):
        print_details("96.90636 u", "Solid", "[Kr]5s24d5", "+7, +6, +4", "1.9", "209 pm", "7.28 eV", "0.55 eV", "2430 K",
                      "4538 K", "11 g/cm³", "1937")
        return
    if check_element(user_input, "Ru", "44", "Ruthenium"):
        print_details("101.1 u", "Solid", "[Kr]5s14d7", "+3", "2.2", "207 pm", "7.361 eV", "1.05 eV", "2607 K",
                      "4423 K", "12.1 g/cm³", "1827")
        return
    if check_element(user_input, "Rh", "45", "Rhodium"):
        print_details("102.9055 u", "Solid", "[Kr]5s14d8", "+3", "2.28", "195 pm", "7.459 eV", "1.137 eV", "2237 K",
                      "3968 K", "12.4 g/cm³", "1803")
        return
    if check_element(user_input, "Pd", "46", "Palladium"):
        print_details("106.42 u", "Solid", "[Kr]4d10", "+3, +2", "2.2", "202 pm", "8.337 eV", "0.557 eV", "1828.05 K",
                      "3236 K", "12.0 g/cm³", "1803")
        return
    if check_element(user_input, "Ag", "47", "Silver"):
        print_details("107.868 u", "Solid", "[Kr]5s14d10", "+1", "1.93", "172 pm", "7.576 eV", "1.302 eV", "1234.93 K",
                      "2435 K", "10.501 g/cm³", "Ancient")
        return
    if check_element(user_input, "Cd", "48", "Cadmium"):
        print_details("112.41 u", "Solid", "[Kr]5s24d10", "+2", "1.69", "158 pm", "8.994 eV", "0", "594.22 K",
                      "1040 K", "8.69 g/cm³", "1817")
        return
    if check_element(user_input, "In", "49", "Indium"):
        print_details("114.818 u", "Solid", "[Kr]5s24d105p1", "+3", "1.78", "193 pm", "5.786 eV", "0.3 eV", "429.75 K",
                      "2345 K", "7.31 g/cm³", "1863")
        return
    if check_element(user_input, "Sn", "50", "Tin"):
        print_details("118.71 u", "Solid", "[Kr]5s24d105p2", "+4, +2", "1.96", "217 pm", "7.344 eV", "1.2 eV", "505.08 K",
                      "2875 K", "7.287 g/cm³", "Ancient")
        return
    if check_element(user_input, "Sb", "51", "Antimony"):
        print_details("121.760 u", "Solid", "[Kr]5s24d105p3", "+5, +3, -3", "2.05", "206 pm", "8.64 eV", "1.07 eV", "903.78 K",
                      "1860 K", "6.685 g/cm³", "Ancient")
        return
    if check_element(user_input, "Te", "52", "Tellurium"):
        print_details("127.6 u", "Solid", "[Kr]5s24d105p4", "+6, +4, -2", "2.1", "206 pm", "9.010 eV", "1.971 eV", "722.66 K",
                      "1261 K", "6.232 g/cm³", "1782")
        return
    if check_element(user_input, "I", "53", "Iodine"):
        print_details("126.9045 u", "Solid", "[Kr]5s24d105p5", "+7, +5, +1, -1", "2.66", "198 pm", "10.451 eV", "3.059 eV", "386.85 K",
                      "457.55 K", "4.93 g/cm³", "1811")
        return
    if check_element(user_input, "Xe", "54", "Xenon"):
        print_details("131.29 u", "Gas", "[Kr]5s24d105p6", "0", "2.6", "216 pm", "12.130 eV", "none", "161.36 K",
                      "165.03 K", "0.005887 g/cm³", "1898")
        return
    if check_element(user_input, "Cs", "55", "Cesium"):
        print_details("132.9054520 u", "Solid", "[Xe]6s1", "+1", "0.79", "343 pm", "3.894 eV", "0.472 eV", "301.59 K",
                      "944 K", "1.93 g/cm³", "1860")
        return
    if check_element(user_input, "Ba", "56", "Barium"):
        print_details("137.33 u", "Solid", "[Xe]6s2", "+2", "0.89", "268 pm", "5.212 eV", "none", "1000 K",
                      "2170 K", "3.62 g/cm³", "1808")
        return
    if check_element(user_input, "La", "57", "Lanthanum"):
        print_details("138.9055 u", "Solid", "[Xe]6s25d1", "+3", "1.1", "240 pm", "5.577 eV", "0.5 eV", "1191 K",
                      "3737 K", "6.15 g/cm³", "1839")
        return
    if check_element(user_input, "Ce", "58", "Cerium"):
        print_details("140.116 u", "Solid", "[Xe]6s24f15d1", "+4, +3", "1.12", "235 pm", "5.539 eV", "0.5 eV", "1071 K",
                      "3697 K", "6.770 g/cm³", "    1803")
        return
    if check_element(user_input, "Pr", "59", "Praseodymium"):
        print_details("140.90766 u", "Solid", "[Xe]6s24f3", "+3", "1.13", "239 pm", "5.464 eV", "none", "1204 K",
                      "3793 K", "6.77 g/cm³", "1885")
        return
    if check_element(user_input, "Nd", "60", "Neodymium"):
        print_details("144.24 u", "Solid", "[Xe]6s24f4", "+3", "1.14", "229 pm", "5.525 eV", "none", "1294 K",
                      "3347 K", "7.01 g/cm³", "1885")
        
        
    if check_element(user_input, "Nd", "61", "Neodymium"):
        print_details ("144.24 u", "Solid", "[Xe]6s24f4", "+3", "1.14", "229 pm", "5.525 eV", "None", "1294 K",
                      "3347 K", "7.01 g/cm³", "1885")

    if check_element(user_input, "Sm", "62", "Samarium"):
        print_details ("	150.4 u", "Solid", "[Xe]6s24f6", "+3,+2", "1.17", "229 pm", "5.644 eV", "None", "1315 K",
                      "2067 K", "7.52 g/cm³", "1879")

    if check_element(user_input, "Eu", "63", "Europium"):
        print_details ("151.964 u", "Solid", "[Xe]6s24f7", "+3, +2", "none", "233 pm", "5.670 eV", "None", "1095 K",
                      "1802 K", "5.24 g/cm³", "1901")

    if check_element(user_input, "Dd", "64", "Gadolinium"):
        print_details ("157.2 u", "Solid", "[Xe]6s24f75d1", "+3", "1.2", "237 pm", "6.150 eV", "None", "1586 K",
                      "3546 K", "7.90 g/cm³", "1880")

    if check_element(user_input, "Tb", "65", "Terbium"):
        print_details ("158.92535 u", "Solid", "[Xe]6s24f9", "+3", "none", "221 pm", "5.864 eV", "None", "1629 K",
                      "3503 K", "8.23 g/cm³", "1843")

    if check_element(user_input, "Dy", "66", "Dysprosium"):
        print_details ("	162.500 u", "Solid", "[Xe]6s24f10", "+3", "1.22", "229 pm", "5.939 eV", "None", "1685 K",
                      "2840 K", "8.55 g/cm³", "1886")

    if check_element(user_input, "Ho", "67", "Holmium"):
        print_details ("	164.93033 u", "Solid", "[Xe]6s24f11", "+3", "1.23", "	216 pm", "6.022 eV", "None", "1747 K",
                      "2973 K", "8.80 g/cm³", "1878")

    if check_element(user_input, "Er", "68", "Erbium"):
        print_details ("	167.26 u", "Solid", "[Xe]6s24f12", "+3", "1.24", "235 pm", "6.108 eV", "None", "1802 K",
                      "3141 K", "9.07 g/cm³", "1843")

    if check_element(user_input, "Tm", "69", "Thulium"):
        print_details ("168.93422 u", "Solid", "[Xe]6s24f13", "+3", "1.25", "227 pm", "6.184 eV", "None", "1818 K",
                      "2223 K", "9.32 g/cm³", "1879")

    if check_element(user_input, "Yb", "70", "Ytterbium"):
        print_details ("1173.05 u", "Solid", "[Xe]6s24f14", "+3,+2", "none", "242 pm", "6.254 eV", "None", "1092 K",
                      "1469 K", "6.90 g/cm³", "1878")

    if check_element(user_input, "Lu", "71", "Lutetium"):
        print_details ("174.9668 u", "Solid", "[Xe]6s24f145d1", "+3", "1.27", "221 pm", "5.426 eV", "None", "1936 K",
                      "3675 K", "9.84 g/cm³", "1907")

    if check_element(user_input, "Hf", "72", "Hafnium"):
        print_details ("178.49 u", "Solid", "[Xe]6s24f145d2", "+4", "1.3", "212 pm", "6.825 eV", "None", "2506 K",
                      "4876 K", "13.3 g/cm³", "1923")

    if check_element(user_input, "Ta", "73", "Tantalum"):
        print_details ("	180.9479 u", "Solid", "[Xe]6s24f145d3", "+5", "1.5", "217 pm", "7.89 eV", "0.322 eV", "3290 K",
                      "5731 K", "16.4 g/cm³", "1802")

    if check_element(user_input, "W", "74", "Tungsten"):
        print_details ("183.84 u", "Solid", "[Xe]6s24f145d4", "+6", "2.36", "	210 pm", "7.98 eV", "0.815 eV", "3695 K",
                      "5828 K", "19.3 g/cm³", "1783")

    if check_element(user_input, "Re", "75", "Rhenium"):
        print_details ("186.207 u", "Solid", "[Xe]6s24f145d5", "+7,+6,+4", "1.9", "217 pm", "7.88 eV", "0.15 eV", "3459 K",
                      "5869 K", "20.8 g/cm³", "1925")

    if check_element(user_input, "Os", "76", "Osmium"):
        print_details ("186.207 u", "Solid", "[Xe]6s24f145d6", "+4,+3", "2.2", "216 pm", "8.7 eV", "1.1 eV", "3306 K",
                      "5285 K", "22.57 g/cm³", "1803")

    if check_element(user_input, "Ir", "77", "Iridium"):
        print_details ("192.22 u", "Solid", "[Xe]6s24f145d7", "+4,+3", "2.2", "202 pm", "9.1 eV", "1.565 eV", "2719 K",
                      "4701 K", "22.42 g/cm³", "1803")

    if check_element(user_input, "Pt", "78", "Platinum"):
        print_details ("195.08 u", "Solid", "[Xe]6s14f145d9", "+4,+2", "2.28", "209 pm", "9 eV", "2.128 eV", "2041.55 K",
                      "4098 K", "21.46 g/cm³", "1735")

    if check_element(user_input, "Au", "79", "Gold"):
        print_details ("196.96657 u", "Solid", "[Xe]6s14f145d10", "+3,+1", "2.54", "166 pm", "9.226 eV", "2.309 eV", "1337.33 K",
                      "3129 K", "19.282 g/cm³", "Ancient")

    if check_element(user_input, "Hg", "80", "Mercury"):
        print_details("200.59 u", "Liquid", "[Xe]6s24f145d10", "+2, +1", "2", "209 pm", "10.438 eV", "None", "234.32 K",
                      "629.88 K", "13.5336 g/cm³", "Ancient")
    if check_element(user_input, "Tl", "81", "Thallium"):
        print_details("204.383 u", "Solid", "[Xe]6s24f145d106p1", "+3, +1", "1.62", "196 pm", "6.108 eV", "0.2 eV", "577 K",
                      "1746 K", "11.8 g/cm³", "1861")
    if check_element(user_input, "Pb", "82", "Lead"):
        print_details("207 u", "Solid", "[Xe]6s24f145d106p2", "+4, +2", "2.33", "202 pm", "7.417 eV", "0.36 eV", "600.61 K",
                      "2022 K", "11.342 g/cm³", "Ancient")
    if check_element(user_input, "Bi", "83", "Bismuth"):
        print_details("208.98040 u", "Solid", "[Xe]6s24f145d106p3", "+5, +3", "2.02", "207 pm", "7.289 eV", "   0.946 eV", "544.55 K",
                      "1837 K", "9.807 g/cm³", "1753")
    if check_element(user_input, "Po", "84", "Polonium"):
        print_details("208.98243 u", "Solid", "[Xe]6s24f145d106p4", "+4, +2", "2", "197 pm", "8.417 eV", "1.9 eV", "527 K",
                      "1235 K", "9.32 g/cm³", "1898")
    if check_element(user_input, "At", "85", "Astatine"):
        print_details("209.98715 u", "Solid", "[Xe]6s24f145d106p5", "7, 5, 3, 1, -1", "2.2", "202 pm", "9.5 eV", "2.8 eV", "575 K",
                      "None", "7 g/cm³", "1940")
    if check_element(user_input, "Rn", "86", "Radon"):
        print_details("222.01758 u", "Gas", "[Xe]6s24f145d106p6", "0", "None", "220 pm", "10.745 eV", "None", "202 K",
                      "211.45 K", "0.00973 g/cm³", "1900")
    if check_element(user_input, "Fr", "87", "Francium"):
        print_details("223.01973 u", "Solid", "[Rn]7s1", "+1", "0.7", "348 pm", "3.9 eV", "0.47 eV", "300 K",
                      "None", "None", "1939")
    if check_element(user_input, "Ra", "88", "Radium"):
        print_details("226.02541 u", "Solid", "[Rn]7s2", "+2", "0.9", "283 pm", "5.279 eV", "None", "973 K",
                      "1413 K", "5 g/cm³", "1898")
    if check_element(user_input, "At", "89", "Actinium"):
        print_details("227.02775 u", "Solid", "[Rn]7s26d1", "+3", "1.1", "260 pm", "5.17 eV", "None", "1324 K",
                      "3471 K", "10.07 g/cm³", "1899")
    if check_element(user_input, "Th", "90", "Thorium"):
        print_details("232.038 u", "Solid", "[Rn]7s26d2", "+4", "1.3", "237 pm", "6.08 eV", "None", "2023 K",
                      "5061 K", "11.72 g/cm³", "1828")
    if check_element(user_input, "Pa", "91", "Protactinium"):
        print_details("231.03588 u", "Solid", "[Rn]7s25f26d1", "+5 +4", "1.5", "243 pm", "5.89 eV", "None", "1845 K",
                      "None", "15.37 g/cm³", "1913")
    if check_element(user_input, "U", "92", "Uranium"):
        print_details("238.0289 u", "Solid", "[Rn]7s25f36d1", "+6 +5 +4 +3", "1.38", "240 pm", "6.194 eV", "None", "1408 K",
                      "4404 K", "18.95 g/cm³", "1789")
    if check_element(user_input, "Np", "93", "Neptunium"):
        print_details("237.048172 u", "Solid", "[Rn]7s25f46d1", "+6 +5 +4 +3", "1.36", "221 pm", "6.266 eV", "None", "917 K",
                      "4175 K", "20.25 g/cm³", "1940")
    if check_element(user_input, "Pu", "94", "Plutonium"):
        print_details("244.06420 u", "Solid", "[Rn]7s25f6", "+6 +5 +4 +3", "1.28", "243 pm", "6.06 eV", "None", "913 K",
                      "3501 K", "19.84 g/cm³", "1940")
    if check_element(user_input, "Am", "95", "Americium"):
        print_details("243.061380 u", "Solid", "[Rn]7s25f7", "+6 +5 +4 +3", "1.3", "244 pm", "5.993 eV", "None", "1449 K",
                      "2284 K", "13.69 g/cm³", "1944")
    if check_element(user_input, "Cm", "96", "Curium"):
        print_details("247.07035 u", "Solid", "[Rn]7s25f76d1", "+3", "1.3", "245 pm", "6.02 eV", "None", "1618 K",
                      "3400 K", "13.51 g/cm³", "1944")
    if check_element(user_input, "Bk", "97", "Berkelium"):
        print_details("247.07031 u", "Solid", "[Rn]7s25f9", "+4 +3", "1.3", "244 pm", "6.23 eV", "None", "1323 K",
                      "None", "14 g/cm³", "1949")
    if check_element(user_input, "Cf", "98", "Californium"):
        print_details("251.07959 u", "Solid", "[Rn]7s25f10", "+3", "1.3", "245 pm", "6.30 eV", "None", "1173 K",
                      "None", "None", "1950")
    if check_element(user_input, "Es", "99", "Einstenium"):
        print_details("252.0830 u", "Solid", "[Rn]7s25f11", "+3", "1.3", "245 pm", "6.42 eV", "None", "1133 K",
                      "None", "None", "1952")
    if check_element(user_input, "Fm", "100", "Fermium"):
        print_details(" 257.09511 u", "Solid", "[Rn]5f127s2", "+3", "1.3", "None", "6.50 eV", "None", "1800 K",
                      "None", "None", "1952")

    if check_element(user_input, "Md", "101", "Mendelevium"):
        print_details("258.09843 u", "Solid", "[Rn]7s25f13", "+3, +2", "1.3", "None", "6.58 eV", "None", "1100 K",
                      "None", "None", "1955")
    if check_element(user_input, "No", "102", "Nobelium"):
        print_details("259.10100 u", "Solid", "[Rn]7s25f14", "+3, +2", "1.3", "None", "6.65 eV", "None", "1100 K",
                      "None", "None", "1957")
    if check_element(user_input, "Lr", "103", "Lawrencium"):
        print_details("266.120 u", "Solid", "[Rn]7s25f146d1", "+3", "1.3", "None", "None", "None", "1900 K",
                      "None", "None", "1961")
    if check_element(user_input, "Rf", "104", "Rotherfordium"):
        print_details("267.122 u", "Solid", "[Rn]7s25f146d2", "+4", "None", "None", "None", "None", "None",
                      "None", "None", "1964")
    if check_element(user_input, "Db", "105", "Dubnium"):
        print_details("268.126 u", "Solid", "[Rn]7s25f146d3", "5, 4, 3", "None", "None", "None", "None", "None",
                      "None", "None", "1967")
    if check_element(user_input, "Sg", "106", "Seaborgium"):
        print_details("269.128 u", "Solid", "[Rn]7s25f146d4", "6, 5, 4, 3, 0", "None", "None", "None", "None", "None",
                      "None", "None", "1974")
    if check_element(user_input, "Bh", "107", "Bohrium"):
        print_details("270.133 u", "Solid", "[Rn]7s25f146d5", "7, 5, 4, 3", "None", "None", "None", "None", "None",
                      "None", "None", "1976")
    if check_element(user_input, "Hs", "108", "Hassium"):
        print_details("269.1336 u", "Solid", "[Rn]7s25f146d6", "8, 6, 5, 4, 3, 2", "None", "None", "None", "None","None",
                      "None", "None", "1984")
    if check_element(user_input, "Mt", "109", "Meitnerium"):
        print_details("277.154 u", "Solid", "[Rn]7s25f146d7", "9, 8, 6, 4, 3, 1", "None", "None", "None", "None","None",
                      "None", "None", "1982")
    if check_element(user_input, "Ds", "110", "Darmstadtium"):
        print_details("282.166 u", "Solid", "[Rn]7s25f146d8", "8, 6, 4, 2, 0", "None", "None", "None", "None", "None",
                      "None", "None", "1994")
    if check_element(user_input, "Rg", "111", "Roentgenium"):
        print_details("282.169 u", "Solid", "[Rn]7s25f146d9", "5, 3, 1, -1", "None", "None", "None", "None", "None",
                      "None", "None", "1994")
    if check_element(user_input, "Cn", "112", "Copernicium"):
        print_details("286.179 u", "Solid", "[Rn]7s25f146d10", "2, 1, 0", "None", "None", "None", "None", "None",
                      "None", "None", "1996")
    if check_element(user_input, "Nh", "113", "Nihonium"):
        print_details("286.182 u", "Solid", "[Rn]5f146d107s27p1", "None", "None", "None", "None", "None", "None",
                      "None", "None", "2004")
    if check_element(user_input, "Fl", "114", "Flerovium"):
        print_details("290.192 u", "Solid", "[Rn]7s27p25f146d10", "6, 4, 2, 1, 0", "None", "None", "None", "None","None",
                      "None", "None", "1998")
    if check_element(user_input, "Mc", "115", "Moscovium"):
        print_details("290.196 u", "Solid", "[Rn]7s27p35f146d10", "3, 1", "None", "None", "None", "None", "None",
                      "None", "None", "2003")
    if check_element(user_input, "Lv", "116", "Livermorium"):
        print_details("293.205 u", "Solid", "[Rn]7s27p45f146d10", "+4, +2, -2", "None", "None", "None", "None", "None",
                      "None", "None", "2000")
    if check_element(user_input, "Ts", "117", "Tennessine"):
        print_details("294.211 u", "Solid", "[Rn]7s27p55f146d10", "+5, +3, +1, -1", "None", "None", "None", "None","None",
                      "None", "None", "2010")
    if check_element(user_input, "Og", "118", "Oganesson"):
        print_details("295.216 u", "Gas", "[Rn]7s27p65f146d10", "+6, +4, +2. +1, 0, -1", "None", "None", "None", "None", "None",
                      "None", "None", "2006")
    
    clear_console()
    print("----- INVALID INPUT -----")
    delay(1.5)
    clear_console()
    show_menu()

main_menu()
