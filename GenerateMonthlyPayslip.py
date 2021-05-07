import sys

tax_rates = [ (180000, 0.4), (80000, 0.3), (40000, 0.2), (20000, 0.1) ]

def caculate_pay_slip(annual_salary):
    gross_monthly_income = round(annual_salary/12)
    annual_tax = 0.0    
    for income_threshold, tax_rate in tax_rates:
        if annual_salary > income_threshold:
            annual_tax += (annual_salary-income_threshold) * tax_rate
            annual_salary = income_threshold
    monthly_income_tax = round(annual_tax/12)
    net_monthly_income = gross_monthly_income - monthly_income_tax
    return {
        'gross_monthly_income': gross_monthly_income,
        'monthly_income_tax': monthly_income_tax,
        'net_monthly_income': net_monthly_income
    }

if __name__ == "__main__":
    try:
        if len(sys.argv)==3:
            name = sys.argv[1]
            annual_salary = int(sys.argv[2])
            pay_slip = caculate_pay_slip(annual_salary)
            print(f'Monthly Payslip for: {name}')
            print(f'Gross Monthly Income: ${pay_slip["gross_monthly_income"]}')
            print(f'Monthly Income Tax: ${pay_slip["monthly_income_tax"]}')
            print(f'Net Monthly Income: ${pay_slip["net_monthly_income"]}')
        else:
            print('Number of input arguments should be 2!')
            print('Sample command: python3 GenerateMonthlyPayslip.py "Mary Song" 60000')
    except ValueError:
        print(f'{sys.argv[2]} is not an integer!')
    except Exception as e:
        print(e)
