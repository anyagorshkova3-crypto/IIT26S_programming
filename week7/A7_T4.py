WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)
DELIMITER = ";"

from dataclasses import dataclass

@dataclass
class TIMESTAMP:
    weekday: str = "Monday"
    hour: str = "05"
    consumption: float = 69.0
    price: float = 0.09

def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PRows.clear()
    filehandler = open(PFilename, 'r', encoding='utf-8')
    # 2. Read filehandle line-by-line
    for line in filehandler:
        if line != '\n':
            PRows.append(line.strip())
    PRows.pop(0)
    #print(PRows)
    filehandler.close()
    return None

def analyseTimestamps(PRows: list[str], PTimestamps: list[TIMESTAMP]) ->None:
    for i in PRows:
        row = i.split(DELIMITER)
        t = TIMESTAMP()
        t.weekday = row[0]
        t.hour = row[1]
        t.consumption = float(row[2])
        t.price = float(row[3])
        PTimestamps.append(t)

def readTimestamps(PFilename: str, PTimestamps: list[TIMESTAMP]):
    rows = []
    readFile(PFilename, rows)
    analyseTimestamps(rows, PTimestamps)

def displayTimestamps(timestamps: list) -> None:
    print("Electricity usage:")
    for i in timestamps:
        print(f' - {i.weekday} {i.hour}:00, price {i.price:.2f}, consumption {i.consumption:.2f} kWh, total {i.price * i.consumption:.2f} €')
    return None

def main() -> None:
    print("Program starting.")
    rows = []
    results = []
    file_name = input("Insert filename: ")
    readFile(file_name, rows)
    timestamps = []
    analyseTimestamps(rows, timestamps)
    displayTimestamps(timestamps)
    rows.clear()
    results.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()