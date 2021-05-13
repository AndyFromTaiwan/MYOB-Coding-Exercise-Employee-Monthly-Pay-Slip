# MYOB Coding Exercise: Employee Monthly Pay Slip
MYOB-Coding-Exercise-Employee-Monthly-Pay-Slip  
├── .gitignore  
├── conftest.py                # for pytest  
├── GenerateMonthlyPayslip.py  #  implementation  
├── README.md  
└── tests                      # pytest unit-test cases  

## Usage
$ python3 GenerateMonthlyPayslip.py {name} {annual salary}  
e.g. $ python3 GenerateMonthlyPayslip.py Mary 77777  
  
If name contains more than one word, the name argument should be quoted.  
e.g. $ python3 GenerateMonthlyPayslip.py "Mary Song" 60000  

## Assumptions
1) Only accepts two input arguments (first for name, second for annual salary).  
   All number of arguments other than 2 cases will not be processed.  
2) The annual salary argument can accept any format if it can be converted into a decimal number.  
   e.g. 6e5, 100000.53, 60000.0 are valid arguments
3) By default, all numbers in the generated pay slip will be rounded into integers.
   However, the prcision of rounding digits is configurable in caculate_pay_slip function as an optional argument.
4) The generated pay slip is displayed via standard output.  
   e.g.  
   Monthly Payslip for: Mary Song  
   Gross Monthly Income: $5000  
   Monthly Income Tax: $500  
   Net Monthly Income: $4500  
   
## Testing
$ pytest tests  
4 test cases to test annual income tax calculation and generated pay slips 
on both integer and decimal outputs.  

## Design Overview
1) Configurable tax rates and precision of numerical result rounding.  
2) Use exception handling to prevent invalid input arguments.  
