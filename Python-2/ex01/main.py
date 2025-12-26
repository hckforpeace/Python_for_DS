import matplotlib.pyplot as plt
from load_csv import load


def main():
    data = load("life_expectancy_years.csv")
    if data is not None:
        data = data.T
        print(data)
        data.plot(y="France", kind="line", title="France Life expectancy\
 projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()
        #


if __name__ == "__main__":
    main()
