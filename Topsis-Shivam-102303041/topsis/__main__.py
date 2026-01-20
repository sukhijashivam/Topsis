import pandas as pd
import math


def main():
    # Take inputs
    input_file = input("Enter input CSV file name: ")
    weight_str = input("Enter weights (comma separated): ")
    impact_str = input("Enter impacts (comma separated): ")
    output_file = input("Enter output file name: ")

    # Read CSV file
    try:
        df = pd.read_csv(input_file)
    except:
        print("Error: File not found")
        return

    # Check columns
    if df.shape[1] < 3:
        print("Error: Input file must contain at least 3 columns")
        return

    data = df.iloc[:, 1:]

    # Check numeric values
    try:
        data = data.astype(float)
    except:
        print("Error: From 2nd to last columns must contain numeric values only")
        return

    # Process weights and impacts
    weights = weight_str.split(",")
    impacts = impact_str.split(",")

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        print("Error: Number of weights, impacts and criteria columns must be same")
        return

    try:
        weights = [float(w) for w in weights]
    except:
        print("Error: Weights must be numeric")
        return

    for im in impacts:
        if im not in ["+", "-"]:
            print("Error: Impacts must be + or -")
            return

    # Step 1: Normalization
    norm = data.copy()
    for j in range(data.shape[1]):
        s = 0
        for i in range(data.shape[0]):
            s += data.iloc[i, j] ** 2
        root = math.sqrt(s)
        for i in range(data.shape[0]):
            norm.iloc[i, j] = data.iloc[i, j] / root

    # Step 2: Apply weights
    for j in range(norm.shape[1]):
        for i in range(norm.shape[0]):
            norm.iloc[i, j] *= weights[j]

    # Step 3: Ideal best and worst
    best, worst = [], []
    for j in range(norm.shape[1]):
        col = list(norm.iloc[:, j])
        if impacts[j] == "+":
            best.append(max(col))
            worst.append(min(col))
        else:
            best.append(min(col))
            worst.append(max(col))

    # Step 4: Distance calculation
    d_plus, d_minus = [], []
    for i in range(norm.shape[0]):
        p, n = 0, 0
        for j in range(norm.shape[1]):
            p += (norm.iloc[i, j] - best[j]) ** 2
            n += (norm.iloc[i, j] - worst[j]) ** 2
        d_plus.append(math.sqrt(p))
        d_minus.append(math.sqrt(n))

    # Step 5: Topsis score
    scores = []
    for i in range(len(d_plus)):
        scores.append(d_minus[i] / (d_plus[i] + d_minus[i]))

    # Ranking
    df["Topsis Score"] = scores
    df["Rank"] = df["Topsis Score"].rank(ascending=False).astype(int)

    # Save output
    df.to_csv(output_file, index=False)
    print("TOPSIS calculation completed successfully")


if __name__ == "__main__":
    main()
    
__version__ = "0.1.0"
