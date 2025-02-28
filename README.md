# Number to Words Conversion for Indian Rupees

This repository contains a Python function to convert numeric values into their word representation in Indian Rupees.
This Python script converts any given number into Indian Rupees (INR) in words, following the Indian numbering system. It supports numbers with or without decimals and formats the output with commas after **Crore**, **Lakh**, and **Thousand** as per the Indian convention.

---

## Python Script

Use the below Python Code

```bash

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
    
    inr_words = number_to_words(rupees)
    paise_words = number_to_words(paise)
    
    if paise > 0:
        return f"Rupees {inr_words} and {paise_words} Paise Only"
    else:
        return f"Rupees {inr_words} Only"

```

# Using Python Code in Office 365 Excel

To use the Python code for converting numbers to words in Indian Rupees in Office 365 Excel, follow these steps:

1. **Run the Script**:
   - Copy the above python script.

   - In the formulabar type : =PY(
       ![image](https://github.com/user-attachments/assets/6217e427-f6bf-461c-99ed-fa0871203174)

   - =PY(`<paste the script>` 
          ![image](https://github.com/user-attachments/assets/5c3264e4-4d60-45b3-9c6d-41440136deff)

   - Then, Press Ctrl + Enter as shown in the screenshot.
     
   - Now you can now call the `convert_to_inr` function from your Excel cells.

3. **Using the Function in Excel**:
   - In a cell, you can use the function like this:
     ```excel
     =PY(convert_to_inr(xl("A3"))
     ```
   - Replace `A3` with the cell reference containing the number you want to convert.

4. **Screenshot**:

     ![image](https://github.com/user-attachments/assets/34f62081-672a-42f6-a1e5-20311553ceca)
       

## How the Function Works

### `number_to_words(num)`

This function converts a given number into its word representation in English, specifically formatted for the Indian numbering system.

#### Components:
- **Lists for Units, Teens, and Tens**:
  - `units`: Words for numbers 0-9.
  - `teens`: Words for numbers 10-19.
  - `tens`: Words for multiples of ten from 10 to 90.

- **`convert_chunk(n)`**:
  - Converts smaller chunks of the number into words.
  - Handles different ranges:
    - Less than 10: Uses `units` list.
    - Between 10 and 19: Uses `teens` list.
    - Multiples of ten: Uses `tens` list.
    - Hundreds: Combines `units` and `convert_chunk` for the remainder.
    - Thousands, Lakhs, Crores: Recursively calls `convert_chunk` for larger chunks.

- **Main Function Logic**:
  - If the number is 0, it returns "Zero".
  - Otherwise, it calls `convert_chunk(num)` to get the word representation and strips any extra spaces.

---

### `convert_to_inr(number)`

This function converts a numeric value into its word representation in Indian Rupees.

#### Steps:
1. **Remove Commas**:
   - Removes any commas from the input number.

2. **Split into Rupees and Paise**:
   - Splits the number into rupees and paise if there is a decimal point.
   - Converts both parts into words using `number_to_words`.

3. **Return the Result**:
   - Constructs the final string in the format "Rupees X and Y Paise Only" or "Rupees X Only" if there are no paise.

---

## Code Structure

### `number_to_words(num)`

- **Lists for Units, Teens, and Tens**:
  - `units`: Contains words for numbers 0-9.
  - `teens`: Contains words for numbers 10-19.
  - `tens`: Contains words for multiples of ten from 10 to 90.

- **`convert_chunk(n)`**:
  - Converts smaller chunks of the number into words.
  - Handles different ranges:
    - Less than 10: Uses `units` list.
    - Between 10 and 19: Uses `teens` list.
    - Multiples of ten: Uses `tens` list.
    - Hundreds: Combines `units` and `convert_chunk` for the remainder.
    - Thousands, Lakhs, Crores: Recursively calls `convert_chunk` for larger chunks.

### `convert_to_inr(number)`

- **Remove Commas**:
  - Removes commas from the input number using `str.replace`.

- **Split into Rupees and Paise**:
  - Splits the number into rupees and paise if there is a decimal point.
  - Converts both parts into words using `number_to_words`.

- **Return the Result**:
  - Constructs the final string in the format "Rupees X and Y Paise Only" or "Rupees X Only" if there are no paise.

---

## Explanation of the Code Flow Diagram

1. **Start**:
   - The program begins execution.

2. **Input Number**:
   - The user provides a number as input (e.g., `15123456789.13`).

3. **Remove Commas from Input**:
   - The program removes commas (`,`) from the input for processing.

4. **Has Decimal?**:
   - The program checks if the input number has a decimal point (`.`).

5. **Split into Rupees and Paise**:
   - If the number has a decimal, it is split into **rupees** and **paise**.

6. **Set Paise to 0**:
   - If the number does not have a decimal, **paise** is set to `0`.

7. **Call `convert_to_inr` Function**:
   - The `convert_to_inr` function is called to handle the conversion.

8. **Call `number_to_words` Function for Rupees**:
   - The `number_to_words` function is called to convert the **rupees** part into words.

9. **Call `convert_chunk` Function**:
   - The `convert_chunk` function is called recursively to break down the number into smaller parts.

10. **Break Down Rupees**:
    - The rupees are broken down into **crore**, **lakh**, **thousand**, **hundred**, **tens**, and **units**.

11. **Map Numbers to Words**:
    - The program uses lists (`units`, `teens`, `tens`) to map numbers to their corresponding words.

12. **Add Commas**:
    - Commas are added after **crore**, **lakh**, and **thousand** for better readability.

13. **Return Rupees in Words**:
    - The `number_to_words` function returns the rupees in words.

14. **Call `number_to_words` Function for Paise**:
    - The `number_to_words` function is called to convert the **paise** part into words.

15. **Return Paise in Words**:
    - The `number_to_words` function returns the paise in words.

16. **Combine Rupees and Paise Words**:
    - The words for **rupees** and **paise** are combined into a single string.

17. **Output Final Result**:
    - The final result is displayed in the format:
      ```
      Rupees One Thousand Five Hundred Twelve Crore, Thirty Four Lakh, Fifty Six Thousand, Seven Hundred Eighty Nine and Thirteen Paise Only
      ```

18. **End**:
    - The program terminates.

---

## Code Flow Diagram

```mermaid
flowchart TD
    A[Start] --> B[Input Number]
    B --> C[Remove Commas from Input]
    C --> D{Has Decimal?}
    D -->|Yes| E[Split into Rupees and Paise]
    D -->|No| F[Set Paise to 0]
    E --> G[Call convert_to_inr Function]
    F --> G
    G --> H[Call number_to_words Function for Rupees]
    H --> I[Call convert_chunk Function]
    I --> J[Break Down Rupees into Crore, Lakh, Thousand, Hundred, Tens, Units]
    J --> K[Map Numbers to Words using Lists]
    K --> L[Add Commas after Crore, Lakh, Thousand]
    L --> M[Return Rupees in Words]
    M --> N[Call number_to_words Function for Paise]
    N --> O[Return Paise in Words]
    O --> P[Combine Rupees and Paise Words]
    P --> Q[Output Final Result]
    Q --> R[End]
