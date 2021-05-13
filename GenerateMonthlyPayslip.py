import sys

# Constants
MONTHS_PER_YEAR = 12
DEFAULT_TAX_RATES = [ (180000, 0.4), (80000, 0.3), (40000, 0.2), (20000, 0.1) ]
DEFAULT_ROUNDING_DIGITS = 2


def calculate_annual_income_tax(annual_salary, tax_rates=DEFAULT_TAX_RATES):
    annual_income_tax = 0.0
    for income_threshold, tax_rate in tax_rates:
        if annual_salary > income_threshold:
            annual_income_tax += (annual_salary-income_threshold) * tax_rate
            annual_salary = income_threshold
    return annual_income_tax

def round_number(num, rounding_digits=DEFAULT_ROUNDING_DIGITS):
    if(rounding_digits==0):
        return round(num)
    return round(num, rounding_digits)
    
def caculate_pay_slip(annual_salary, tax_rates=DEFAULT_TAX_RATES, rounding_digits=DEFAULT_ROUNDING_DIGITS):
    gross_monthly_income = annual_salary / MONTHS_PER_YEAR
    annual_income_tax = calculate_annual_income_tax(annual_salary=annual_salary)
    monthly_income_tax = annual_income_tax / MONTHS_PER_YEAR
    net_monthly_income = gross_monthly_income - monthly_income_tax
    return {
        'gross_monthly_income': round_number(gross_monthly_income, rounding_digits),
        'monthly_income_tax': round_number(monthly_income_tax, rounding_digits),
        'net_monthly_income': round_number(net_monthly_income, rounding_digits)
    }

if __name__ == "__main__":
    try:
        if len(sys.argv)!=3:
            raise Exception('Number of input arguments should be 2!')
        name = sys.argv[1]
        annual_salary = float(sys.argv[2])
        if(annual_salary<0):
            raise Exception('Annual salary shoule be non-negative!')
        pay_slip = caculate_pay_slip(annual_salary=annual_salary, rounding_digits=0)
        print(f'Monthly Payslip for: {name}')
        print(f'Gross Monthly Income: ${pay_slip["gross_monthly_income"]}')
        print(f'Monthly Income Tax: ${pay_slip["monthly_income_tax"]}')
        print(f'Net Monthly Income: ${pay_slip["net_monthly_income"]}')
    except ValueError:        
        print(f'{sys.argv[2]} is not an number!')
        print('Sample command: python3 GenerateMonthlyPayslip.py "Mary Song" 60000')
    except Exception as e:
        print(e)
        print('Sample command: python3 GenerateMonthlyPayslip.py "Mary Song" 60000')
