import GenerateMonthlyPayslip as g

def test_calculate_annual_income_tax_integer():
    test_annual_salary_cases = [ 
        60000, 180010, 180000, 
        80010, 80000, 40010, 40000, 
        20010, 20000, 10, 0 
    ]
    expected_annual_tax_results = [
        6000, 40004, 40000,
        10003, 10000, 2002, 2000,
        1, 0, 0, 0
    ]
    for i in range(len(test_annual_salary_cases)):
        assert expected_annual_tax_results[i] == int(g.calculate_annual_income_tax(annual_salary=test_annual_salary_cases[i]))

def test_calculate_annual_income_tax_decimal():
    test_annual_salary_cases = [
        180000, 199999, 200000, 199999.49, 180000.50, 190000.51,
        80000, 179999, 130000, 100000.4, 90000.51, 80000.6,
        40000, 79999, 60000, 70000.44, 40000.67, 50000.99,
        20000, 39999, 30000, 30000.3, 20000.33, 25000.8,
        0, 19999, 1, 0.1, 0.01, 19998.99
    ]
    expected_annual_tax_results = [
        4, 4, 4, 4, 4, 4,
        3, 3, 3, 3, 3, 3,
        2, 2, 2, 2, 2, 2,
        1, 1, 1, 1, 1, 1,
        0, 0, 0, 0, 0, 0
    ]
    for i in range(len(test_annual_salary_cases)):
        salary = test_annual_salary_cases[i]
        tax_rate = g.calculate_annual_income_tax(annual_salary=salary+1) - g.calculate_annual_income_tax(annual_salary=salary) 
        assert expected_annual_tax_results[i] == round(10*tax_rate)

def test_caculate_pay_slip_integer():
    test_annual_salary_cases = [
        60000,
        77777,
        180000,
        99999,
        80000,
        45000,
        32767,
        40000,
        20012,
        20000,
        19999,
        10,
        0
    ]
    expected_pay_slip_results = [
        {'gross_monthly_income': 5000, 'monthly_income_tax': 500, 'net_monthly_income': 4500},
        {'gross_monthly_income': 6481, 'monthly_income_tax': 796, 'net_monthly_income': 5685},
        {'gross_monthly_income': 15000, 'monthly_income_tax': 3333, 'net_monthly_income': 11667},
        {'gross_monthly_income': 8333, 'monthly_income_tax': 1333, 'net_monthly_income': 7000},
        {'gross_monthly_income': 6667, 'monthly_income_tax': 833, 'net_monthly_income': 5833},
        {'gross_monthly_income': 3750, 'monthly_income_tax': 250, 'net_monthly_income': 3500},
        {'gross_monthly_income': 2731, 'monthly_income_tax': 106, 'net_monthly_income': 2624},
        {'gross_monthly_income': 3333, 'monthly_income_tax': 167, 'net_monthly_income': 3167},
        {'gross_monthly_income': 1668, 'monthly_income_tax': 0, 'net_monthly_income': 1668},
        {'gross_monthly_income': 1667, 'monthly_income_tax': 0, 'net_monthly_income': 1667},
        {'gross_monthly_income': 1667, 'monthly_income_tax': 0, 'net_monthly_income': 1667},
        {'gross_monthly_income': 1, 'monthly_income_tax': 0, 'net_monthly_income': 1},
        {'gross_monthly_income': 0, 'monthly_income_tax': 0, 'net_monthly_income': 0}
    ]
    for i in range(len(test_annual_salary_cases)):
        pay_slip = g.caculate_pay_slip(annual_salary=test_annual_salary_cases[i], rounding_digits=0)
        for key in pay_slip:
            assert expected_pay_slip_results[i][key] == pay_slip[key]

def test_caculate_pay_slip_decimal():
    test_annual_salary_cases = [
        60000,
        77777,
        180000.4,
        80000.53,
        0.00,
        99999.99,
        30000.01,
        20000.50
    ]
    expected_pay_slip_results = [
       {'gross_monthly_income': 5000.0, 'monthly_income_tax': 500.0, 'net_monthly_income': 4500.0},
       {'gross_monthly_income': 6481.42, 'monthly_income_tax': 796.28, 'net_monthly_income': 5685.13},
       {'gross_monthly_income': 15000.03, 'monthly_income_tax': 3333.35, 'net_monthly_income': 11666.69},
       {'gross_monthly_income': 6666.71, 'monthly_income_tax': 833.35, 'net_monthly_income': 5833.36},
       {'gross_monthly_income': 0.0, 'monthly_income_tax': 0.0, 'net_monthly_income': 0.0},
       {'gross_monthly_income': 8333.33, 'monthly_income_tax': 1333.33, 'net_monthly_income': 7000.0},
       {'gross_monthly_income': 2500.0, 'monthly_income_tax': 83.33, 'net_monthly_income': 2416.67},
       {'gross_monthly_income': 1666.71, 'monthly_income_tax': 0.0, 'net_monthly_income': 1666.7},
    ]
    for i in range(len(test_annual_salary_cases)):
        pay_slip = g.caculate_pay_slip(annual_salary=test_annual_salary_cases[i], rounding_digits=2)
        for key in pay_slip:
            assert round(abs(100*(expected_pay_slip_results[i][key] - pay_slip[key]))) <= 1
