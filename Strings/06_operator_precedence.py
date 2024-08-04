"""
Basic rules of arthimetic operators:
-----------------------------------

Operator precedence is a fancy term for the relative importance given to each of the operators.

Multiplication and division have higher precedence than addtion and subtraction, so those operations will
be performed first.


"""

# for example.

print(2+4/2-1*12)

# I who didn't pay attention in school while teaching operator's precedence will think that above
# expression will result in 24.

# but the actual answer is -8.
# because operators precedence comes into play.

print((((2 + 4) /2)-1)*12)

# In above expression we mitigated the operator precedence using ()paranthesis which normally have 
# highest precedence than all operators.

"""
In school we have different acronyms for operator precedence where as,

PEDMAS: Parantheses, Exponents, Multiplication\Division, Addtion/Subtraction. 
BEDMAS: Brackets, Exponents, Division/Multiplication, Addtion/Subtraction.
BODMAS: Brackets, Order, Division/Multiplication, Addtion/Subtraction.
BIDMAS: Brackets, Index, Division/Multiplication, Addtion/Subtraction.

Division, multiplication & Addtion, subtraction has same equal precedence.

Because multiplication, Division have equal precedence using these operators in expression are
evaluated from left to right.

""" 

