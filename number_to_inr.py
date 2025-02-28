def number_to_words(num):
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
             "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", 
            "Eighty", "Ninety"]
    
    def convert_chunk(n):
        if n == 0:
            return ""
        elif n < 10:
            return units[n]
        elif 10 <= n < 20:
            return teens[n - 10]
        elif 20 <= n < 100:
            return tens[n // 10] + " " + convert_chunk(n % 10)
        elif 100 <= n < 1000:
            return units[n // 100] + " Hundred " + convert_chunk(n % 100)
        elif 1000 <= n < 100000:
            return convert_chunk(n // 1000) + " Thousand, " + convert_chunk(n % 1000)
        elif 100000 <= n < 10000000:
            return convert_chunk(n // 100000) + " Lakh, " + convert_chunk(n % 100000)
        elif 10000000 <= n:
            return convert_chunk(n // 10000000) + " Crore, " + convert_chunk(n % 10000000)
        return ""
    
    if num == 0:
        return "Zero"
    
    return convert_chunk(num).strip()

def convert_to_inr(number):
    # Remove commas from the input number
    number = str(number).replace(',', '')
    
    # Split into rupees and paise
    if '.' in number:
        rupees, paise = map(int, number.split('.'))
    else:
        rupees = int(number)
        paise = 0
    
    # Handle edge cases
    if rupees == 0 and paise == 0:
        return "No Rupees Only"
    elif rupees == 0:
        paise_words = number_to_words(paise)
        return f"Rupees {paise_words} Paise Only"
    else:
        inr_words = number_to_words(rupees)
        if paise > 0:
            paise_words = number_to_words(paise)
            return f"Rupees {inr_words} and {paise_words} Paise Only"
        else:
            return f"Rupees {inr_words} Only"
