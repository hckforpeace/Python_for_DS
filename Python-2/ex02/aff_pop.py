import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def convert_column(col):
    """Convert a column with M/k/B suffixes to numeric values."""
    col = col.replace({"k": "e3", "M": "e6", "B": "e9"}, regex=True)
    return pd.to_numeric(col)


def main():
    data = load("population_total.csv")
    if data is not None:
        # Transpose
        data = data.T
        data = data.apply(convert_column)

        # Set type as integer
        data.index = data.index.astype(int)
        # Only take data from 1800 to 2050
        data = data.loc[1800:2050]

        # set plot
        data.plot(y=["Lebanon", "France"], kind="line",
                  color=["blue", "green"])

        # graph
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.yticks([0, 20e6, 40e6, 60e6], ["0", "20M", "40M", "60M"])
        plt.legend(loc="lower right")
        plt.show()


if __name__ == "__main__":
    main()
