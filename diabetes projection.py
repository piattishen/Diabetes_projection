import pandas as pd
from outcome_0 import smooth_functions_0
from outcome_1 import smooth_functions_1

try:
    Preg = int(input("Pregnancies(0-17):"))
    if Preg >= 0 and Preg <= 17:
        pass
    else:
        print("out of range")
        exit()
except ValueError:
    print("Input is not a valid number")
    exit()

try:
    Glu = int(input("Glucose(44-199):"))
    if Glu >= 44 and Glu <= 199:
        pass
    else:
        print("out of range")
        exit()
except ValueError:
    print("Input is not a valid number")
    exit()

try:
    Blo = int(input("BloodPressure(24-122):"))
    if Blo >= 24 and Blo <= 122:
        pass
    else:
        print("out of range")
        exit()
except ValueError:
    print("Input is not a valid number")
    exit()

try:
    Ski = int(input("SkinThickness(7-99):"))
    if Ski >= 7 and Ski <= 99:
        pass
    else:
        print("out of range")
        exit()
except ValueError:
    print("Input is not a valid number")
    exit()

try:
    Ins = int(input("Insulin(14-846):"))
    if Ins >= 14 and Ins <= 846:
        pass
    else:
        print("out of range")
        exit()
except ValueError:
    print("Input is not a valid number")
    exit()

try:
    Bmi = float(input("BMI(18.2-67.1):"))
    if Bmi >= 18.2 and Bmi <= 67.1:
        pass
    else:
        print("out of range")
        exit()
except ValueError:
    print("Input is not a valid number")
    exit()

try:
    Dpf = float(input("DiabetesPedigreeFunction(0.07-2.42):"))
    if Dpf >= 0.07 and Dpf <= 2.42:
        pass
    else:
        print("out of range")
        exit()
except ValueError:
    print("Input is not a valid number")
    exit()

try:
    Age = int(input("Age(21-81):"))
    if Age >= 21 and Age <= 81:
        pass
    else:
        print("out of range")
        exit()
except ValueError:
    print("Input is not a valid number")
    exit()


column_name = "Pregnancies"
if column_name in smooth_functions_1:
    f = smooth_functions_1[column_name]
    x_value = Preg # any point
    y_Preg_1 = f(x_value)
    print(f'Value at x={x_value} for {column_name}: {y_Preg_1}')

column_name = "Glucose"
if column_name in smooth_functions_1:
    f = smooth_functions_1[column_name]
    x_value = Glu # any point
    y_Glu_1 = f(x_value)
    print(f'Value at x={x_value} for {column_name}: {y_Glu_1}')

column_name = "BloodPressure"
if column_name in smooth_functions_1:
    f = smooth_functions_1[column_name]
    x_value = Blo # any point
    y_Blo_1 = f(x_value)
    print(f'Value at x={x_value} for {column_name}: {y_Blo_1}')

column_name = "SkinThickness"
if column_name in smooth_functions_1:
    f = smooth_functions_1[column_name]
    x_value = Ski # any point
    y_Ski_1 = f(x_value)
    print(f'Value at x={x_value} for {column_name}: {y_Ski_1}')

column_name = "Insulin"
if column_name in smooth_functions_1:
    f = smooth_functions_1[column_name]
    x_value = 50 # any point
    y_Ins_1 = f(x_value)
    print(f'Value at x={x_value} for {column_name}: {y_Ins_1}')

column_name = "BMI"
if column_name in smooth_functions_1:
    f = smooth_functions_1[column_name]
    x_value = Bmi # any point
    y_Bmi_1 = f(x_value)
    print(f'Value at x={x_value} for {column_name}: {y_Bmi_1}')

column_name = "DiabetesPedigreeFunction"
if column_name in smooth_functions_1:
    f = smooth_functions_1[column_name]
    x_value = Dpf # any point
    y_Dpf_1 = f(x_value)
    print(f'Value at x={x_value} for {column_name}: {y_Dpf_1}')

column_name = "Age"
if column_name in smooth_functions_1:
    f = smooth_functions_1[column_name]
    x_value = Age # any point
    y_Age_1 = f(x_value)
    print(f'Value at x={x_value} for {column_name}: {y_Age_1}')

column_name = "Pregnancies"
if column_name in smooth_functions_0:
    f = smooth_functions_1[column_name]
    x_value = Preg # any point
    y_Preg_0 = f(x_value)
    print(f'Value at x={x_value} for {column_name}: {y_Preg_0}')

column_name = "Glucose"
if column_name in smooth_functions_0:
    f = smooth_functions_1[column_name]
    x_value = Glu # any point
    y_Glu_0 = f(x_value)
    print(f'Value at x={x_value} for {column_name}: {y_Glu_0}')

column_name = "BloodPressure"
if column_name in smooth_functions_0:
    f = smooth_functions_1[column_name]
    x_value = Blo # any point
    y_Blo_0 = f(x_value)
    print(f'Value at x={x_value} for {column_name}: {y_Blo_0}')

column_name = "SkinThickness"
if column_name in smooth_functions_0:
    f = smooth_functions_1[column_name]
    x_value = Ski # any point
    y_Ski_0 = f(x_value)
    print(f'Value at x={x_value} for {column_name}: {y_Ski_0}')

column_name = "Insulin"
if column_name in smooth_functions_0:
    f = smooth_functions_1[column_name]
    x_value = 50 # any point
    y_Ins_0 = f(x_value)
    print(f'Value at x={x_value} for {column_name}: {y_Ins_0}')

column_name = "BMI"
if column_name in smooth_functions_0:
    f = smooth_functions_1[column_name]
    x_value = Bmi # any point
    y_Bmi_0 = f(x_value)
    print(f'Value at x={x_value} for {column_name}: {y_Bmi_0}')


column_name = "DiabetesPedigreeFunction"
if column_name in smooth_functions_0:
    f = smooth_functions_1[column_name]
    x_value = Dpf # any point
    y_Dpf_0 = f(x_value)
    print(f'Value at x={x_value} for {column_name}: {y_Dpf_0}')

column_name = "Age"
if column_name in smooth_functions_0:
    f = smooth_functions_1[column_name]
    x_value = Age # any point
    y_Age_0 = f(x_value)
    print(f'Value at x={x_value} for {column_name}: {y_Age_0}')

diabetes_df = pd.read_csv(r"./diabetes.csv")
n = len(diabetes_df)
n_1 = len(diabetes_df[diabetes_df["Outcome"] == 1])
n_0 = len(diabetes_df[diabetes_df["Outcome"] == 0])
# print(n)
# print(n_1)
# print(n_0)

# naive Bayes
P_1 = n_1 / n
P_Outcome1 = y_Preg_1 * y_Glu_1 * y_Blo_1 * y_Ski_1 * y_Ins_1 * y_Bmi_1 * y_Dpf_1 * y_Age_1
P_0 = n_0 / n
P_Outcome0 = y_Preg_0 * y_Glu_0 * y_Blo_0 * y_Ski_0 * y_Ins_0 * y_Bmi_0 * y_Dpf_0 * y_Age_0
P = (P_1*P_Outcome1) / (P_Outcome1*P_1 + P_Outcome0*P_0)
def float_to_percentage(number):
    percentage = number * 100
    return f"{percentage:.2f}%"
p = float_to_percentage(P)
print("the precentage you will get diabetes is:", p)