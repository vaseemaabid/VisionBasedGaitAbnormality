import pandas as pd

data = {
    "Stride_Length": [45, 50, 48, 52, 47],
    "Step_Time": [1.2, 1.1, 1.3, 1.0, 1.25]
}

df = pd.DataFrame(data)

print("Extracted Features:")
print(df)
