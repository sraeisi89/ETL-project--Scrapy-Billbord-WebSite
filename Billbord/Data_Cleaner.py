import pandas as pd

def main():
    file = pd.read_csv("Data.csv", sep=",")
    file.drop_duplicates(subset=['name'], inplace=True)
    del file['ranking']
    file = file.sort_values('name')
    file.to_csv("Ultimate.csv", index=False)


if __name__ == "__main__":
    main()
