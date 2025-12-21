from time import sleep
from tqdm import tqdm
import os as os


# 115 if os.get_terminal_size().columns >= 129 else
def ft_tqdm(list: range) -> None:
    previousCharging = 0
    terminalWidth = os.get_terminal_size().columns
    chargingBarLen = terminalWidth - 41
    current = 0

    for i in list:
        ratioOfRange = int(i * 100 / list.stop) + 1
        ratioOfCharging = int(ratioOfRange * chargingBarLen / 100) + 1
        if current != ratioOfRange:
            current = ratioOfRange

        if ratioOfCharging != previousCharging:
            previousCharging = ratioOfCharging

        prctg = f"{ratioOfRange:>3}%"
        bar = f"{ratioOfCharging * '█'}"
        prog = f"{i + 1}/{list.stop}"
        if i == list.stop - 1:
            print(f"{prctg}|{bar}| {prog}")
        else:
            print(f"{prctg}|{bar}| {prog}", end="\r")
        yield

