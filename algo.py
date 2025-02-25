# I am algo for the project .
import pandas as pd

def algo(amount, tenure, risk_factor):
    df_original = pd.read_csv('Data.csv')
    df = df_original.copy()

    last_date = df.columns[-1]

    rows_to_drop = []
    for i in range(len(df)):
        if amount < float(df.loc[i, str(last_date)]):
            rows_to_drop.append(i)
    df.drop(rows_to_drop, axis=0, inplace=True)
    df.reset_index(drop=True, inplace=True)

    per_list = []
    rf_list = []

    for i in range(len(df)):
        percentage_total = 0
        rf = 0
        nos = 0
        for j in range(1, len(df.columns) - tenure):
            next_tenure_data = df.iloc[i, (j + tenure)]
            current_tenure_data = df.iloc[i, j]

            if current_tenure_data != 0:
                percentage = (((next_tenure_data) - (current_tenure_data)) / (current_tenure_data)) * 100
                percentage_total += percentage
                nos += 1
                if percentage < 0:
                    rf = max(rf, -percentage)

        if nos > 0:
            percentage_total /= nos

        per_list.append(percentage_total)
        rf_list.append(rf)

    df["Percentage"] = per_list
    df["rf"] = rf_list

    df.fillna(0, inplace=True)

    rows_to_drop_rf = []
    for i in range(len(df)):
        if risk_factor < df.loc[i, "rf"]:
            rows_to_drop_rf.append(i)
    df.drop(rows_to_drop_rf, axis=0, inplace=True)
    df.reset_index(drop=True, inplace=True)

    df = df.sort_values(["Percentage", "rf"], ascending=[False, True])
    df.reset_index(drop=True, inplace=True)

    return df

#Ex:
# print(algo(10000, 2, 30))
