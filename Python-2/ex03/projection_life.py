import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def main():
    gdp_data = load("income_per_person_\
gdppercapita_ppp_inflation_adjusted.csv")
    life_data = load("life_expectancy_years.csv")

    if gdp_data is not None and life_data is not None:
        gdp1900 = gdp_data["1900"]
        life1900 = life_data["1900"]

        combined = pd.DataFrame(
            {"Life Expectancy": life1900, "Gross Domestic product": gdp1900}
        )

        combined.plot(
            y="Life Expectancy", x="Gross Domestic product",
            kind="scatter", s=10
        )

        plt.xscale("log")
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
        plt.show()


if __name__ == "__main__":
    main()
