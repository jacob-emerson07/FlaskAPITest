def calculate_tax(income, filingStatus):
    filing_tax_brackets = {"single": [(9999, .10), (49999, .15), (99999, .20)], 
                           "joint":  [(19999, .10), (99999, .15), (199999, .20)]}

    taxes = 0
    previous_bracket = 0
    for bracket_max, tax_rate in filing_tax_brackets[filingStatus]:
        if income == 0:
            break

        if income <= bracket_max-previous_bracket:
            taxes += int(income * tax_rate)
            income = 0
            break

        else:
            taxes += int((bracket_max-previous_bracket) * tax_rate)
            income -= (bracket_max - previous_bracket)
            previous_bracket = bracket_max
        
    if income > 0:
        taxes += int(income * .25)

    return taxes