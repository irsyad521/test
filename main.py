import itertools

def generate_variations(word):
    # Menyimpan variasi password
    variations = set()
    
    # Mengganti huruf kecil dan kapital
    for case in itertools.product(*[(char.lower(), char.upper()) for char in word]):
        variations.add(''.join(case))
    
    # Menambahkan angka dan simbol
    for variation in list(variations):
        variations.add(variation + '123')   # Menambahkan angka
        variations.add(variation + '@!$')    # Menambahkan simbol
    
    return variations

# Kata dasar
word = "Cirebon"

# Menghasilkan variasi password
password_variations = generate_variations(word)

# Menyimpan hasil ke dalam file 'output.txt'
with open('output.txt', 'w') as output_file:
    for password in password_variations:
        output_file.write(password + '\n')

print("Variasi password telah disimpan dalam file 'output.txt'.")
