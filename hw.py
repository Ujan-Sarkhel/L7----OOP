class Roman:
    def int_to_rom(self, num):
        if not (1 <= num <= 3999):
            return "Enter a number between 1 and 3999"
        
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        syms = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        roman_numeral = ""
        i = 0
        while num > 0:
            count = num // val[i]
            roman_numeral += syms[i] * count
            num -= val[i] * count
            i += 1
        return roman_numeral


if __name__ == "__main__":
    number = int(input("Enter an integer (1 to 3999): "))
    converter = Roman()
    result = converter.int_to_rom(number)
    print(f"Roman numeral: {result}")
