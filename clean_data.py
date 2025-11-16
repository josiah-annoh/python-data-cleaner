import pandas as pd

def clean_csv(input_file, output_file):
    df = pd.read_csv(input_file)
    df = df.dropna(how='all')
    df.columns = df.columns.str.strip()
    df = df.sort_values(by=df.columns[0])
    df = df.reset_index(drop=True)
    df.to_csv(output_file, index=False)
    print(f"Cleaned file saved as: {output_file}")

if __name__ == "__main__":
    clean_csv("raw_data.csv", "cleaned_data.csv")

