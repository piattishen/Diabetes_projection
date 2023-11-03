import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

diabetes_df = pd.read_csv(r"./diabetes.csv")
#print(diabetes_df.head())
#print(diabetes_df.shape)

outcome_proportions_0 = {}
def calculate_outcome_proportions_0(data_df, feature_column, start, end, step):
    outcome_proportions_0 = {}
    for i in range(int(end), int(start)-1, step):
        filtered_df = data_df[data_df["Outcome"] == 0]
        feature_proportion = len(filtered_df[filtered_df[feature_column] >= i]) / len(filtered_df)
        if feature_column not in outcome_proportions_0:
            outcome_proportions_0[feature_column] = {}
        outcome_proportions_0[feature_column][i] = feature_proportion
    return outcome_proportions_0

def generate_smooth_function(column_name, smooth_functions_0):
    def smooth_function(data_result, x_label, y_label):
        for key, value in data_result.items():
            x = np.array(list(value.keys()))
            y = np.array(list(value.values()))

            # Create interpolation function
            f = interp1d(x, y, kind='cubic')

            # Store interpolation functions in a dictionary using column names as keys
            smooth_functions_0[column_name] = f

            # Generate smooth data points
            x_smooth = np.linspace(min(x), max(x), 100)
            y_smooth = f(x_smooth)

            # Plot a smooth function curve
            plt.plot(x_smooth, y_smooth)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title(f'Smoothed Function for {column_name}')
            #plt.show()

    return smooth_function
smooth_functions_0 = {}
df0 = diabetes_df
preg_max = df0["Pregnancies"].max()
preg_min = df0["Pregnancies"].min()
# print(preg_max) # 17
# print(preg_min) # 0
df0_result = calculate_outcome_proportions_0(df0, "Pregnancies", preg_min, preg_max, -1)
#print(df0_result)
# line_chart(df0_result, "weeks", "weeks number in all")
smooth_function_for_Preg = generate_smooth_function("Pregnancies", smooth_functions_0)
f = smooth_function_for_Preg(df0_result, "weeks", "weeks number in all")
# print(type(smooth_functions_0))

# # column_name = "Pregnancies"
# # if column_name in smooth_functions_0:
# #     f = smooth_functions_0[column_name]
# #     x_value = 0 # any point
# #     y_value = f(x_value)
# #     print(f'Value at x={x_value} for {column_name}: {y_value}')
outcome_proportions_0.update(df0_result)

df1 = diabetes_df[diabetes_df['Glucose'] != 0]
Glu_max = df1["Glucose"].max()
Glu_min = df1["Glucose"].min()
# print(Glu_max) # 199
# print(Glu_min) # 44
df1_result = calculate_outcome_proportions_0(df1, 'Glucose', Glu_min, Glu_max, -10)
smooth_function_for_Glu = generate_smooth_function("Glucose", smooth_functions_0)
f = smooth_function_for_Glu(df1_result, "glucose level", "this level number in all")
# column_name = "Glucose"
# if column_name in smooth_functions_0:
#     f = smooth_functions_0[column_name]
#     x_value = 88 # any point
#     y_value = f(x_value)
#     print(f'Value at x={x_value} for {column_name}: {y_value}')
outcome_proportions_0.update(df1_result)

df2 = diabetes_df[diabetes_df['BloodPressure'] != 0]
Blo_max = df2["BloodPressure"].max()
Blo_min = df2["BloodPressure"].min()
# print(Blo_max) # 122
# print(Blo_min) # 24
df2_result = calculate_outcome_proportions_0(df2, "BloodPressure", Blo_min, Blo_max, -10)
smooth_function_for_Blo = generate_smooth_function("BloodPressure", smooth_functions_0)
f = smooth_function_for_Blo(df2_result, "mmHg", "this level number in all")
outcome_proportions_0.update(df2_result)

df3 = diabetes_df[diabetes_df['SkinThickness'] != 0]
Ski_max = df3["SkinThickness"].max()
Ski_min = df3["SkinThickness"].min()
# print(Ski_max) # 99
# print(Ski_min) # 7
df3_result = calculate_outcome_proportions_0(df3, "SkinThickness", Ski_min, Ski_max, -5)
smooth_function_for_Ski = generate_smooth_function("SkinThickness", smooth_functions_0)
f = smooth_function_for_Ski(df3_result, "mm", "this level number in all")
outcome_proportions_0.update(df3_result)

# i think insulin will not be 0
df4 = diabetes_df[diabetes_df['Insulin'] != 0]
Ins_max = df4["Insulin"].max()
Ins_min = df4["Insulin"].min()
# print(Ins_max) # 846
# print(Ins_min) # 14
df4_result = calculate_outcome_proportions_0(df4, "Insulin", Ins_min, Ins_max, -20)
smooth_function_for_Ins = generate_smooth_function("Insulin", smooth_functions_0)
f = smooth_function_for_Ins(df4_result, "mg/ml", "this level number in all")
outcome_proportions_0.update(df4_result)

df5 = diabetes_df[diabetes_df['BMI'] != 0]
BMI_max = df5["BMI"].max()
BMI_min = df5["BMI"].min()
# print(BMI_max) # 67.1
# print(BMI_min) # 18.2
df5_result = calculate_outcome_proportions_0(df5, "BMI", BMI_min, BMI_max, -5)
# print(df5_result)
#line_chart(df5_result, "BMI", "precentage in all")
smooth_function_for_BMI = generate_smooth_function("BMI", smooth_functions_0)
f = smooth_function_for_BMI(df5_result, "bmi", "this level number in all")
# column_name = "BMI"
# if column_name in smooth_functions_0:
#     f = smooth_functions_0[column_name]
#     x_value = 33 # any point
#     y_value = f(x_value)
#     print(f'Value at x={x_value} for {column_name}: {y_value}')
outcome_proportions_0.update(df5_result)

df6 = diabetes_df[diabetes_df['DiabetesPedigreeFunction'] != 0]
DPF_max = df6["DiabetesPedigreeFunction"].max()
DPF_min = df6["DiabetesPedigreeFunction"].min()
# print(DPF_max) # 2.42
# print(DPF_min) # 0.07

def DPF_proportions(data_df, feature_column, start, end):
    i = end
    outcome_proportions_0 = {}
    while i > start:
        i = round(i, 2)  
        filtered_df = data_df[data_df["Outcome"] == 0]
        feature_proportion = len(filtered_df[filtered_df[feature_column] >= i]) / len(filtered_df)
        if feature_column not in outcome_proportions_0:
            outcome_proportions_0[feature_column] = {}
        outcome_proportions_0[feature_column][i] = feature_proportion
        i -= 0.2
    return outcome_proportions_0

df6_result = DPF_proportions(df6, "DiabetesPedigreeFunction", DPF_min, DPF_max)
# print(df6_result)
# line_chart(df6_result, "DPF", "precentage in all")
smooth_function_for_Ins = generate_smooth_function("DiabetesPedigreeFunction", smooth_functions_0)
f = smooth_function_for_Ins(df6_result, "x", "this level number in all")
# column_name = "DiabetesPedigreeFunction"
# if column_name in smooth_functions_0:
#     f = smooth_functions_0[column_name]
#     x_value = 1.03 # any point
#     y_value = f(x_value)
#     print(f'Value at x={x_value} for {column_name}: {y_value}')
outcome_proportions_0["DiabetesPedigreeFunction"] = df6_result

df7 = diabetes_df[diabetes_df['Age'] != 0]
Age_max = df7["Age"].max()
Age_min = df7["Age"].min()
# print(Age_max) # 81
# print(Age_min) # 21
df7_result = calculate_outcome_proportions_0(df7, "Age", Age_min, Age_max, -5)
smooth_function_for_Age = generate_smooth_function("Age", smooth_functions_0)
f = smooth_function_for_Age(df7_result, "age", "this level number in all")
outcome_proportions_0.update(df7_result)

# print(outcome_proportions_0)
# print(smooth_functions_0)
