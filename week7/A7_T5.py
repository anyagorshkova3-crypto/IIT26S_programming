WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",)
DELIMITER = ";"

from dataclasses import dataclass

@dataclass
class TIMESTAMP:
    weekday: str = "Monday"
    hour: str = "05"
    consumption: float = 69.0
    price: float = 0.09

@dataclass
class DAY_USAGE:
    weekday: str = ""
    usage: float = 0.0
    cost: float = 0.0

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

def parseRows(PRows: list[str], PTimestamps: list[TIMESTAMP]) ->None:
    for i in PRows:
        row = i.split(DELIMITER)
        t = TIMESTAMP()
        t.weekday = row[0]
        t.hour = row[1]
        t.consumption = float(row[2])
        t.price = float(row[3])
        PTimestamps.append(t)

def analyseTimestamps(PTimestamps: list[TIMESTAMP], PDayUsages:list[DAY_USAGE]) ->None:
    print("Analysing timestamps.")
    for i in WEEKDAYS:
        t = DAY_USAGE()
        t.weekday = i
        PDayUsages.append(t)
    for ts in PTimestamps:
        day = PDayUsages[WEEKDAYS.index(ts.weekday)]
        day.usage += ts.consumption
        day.cost += ts.price * ts.consumption
    #print(PDayUsages)
    return None

def displayResults(PDayUsages: list[DAY_USAGE]) -> None:
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for i in PDayUsages:
        print(f' - {i.weekday} usage {i.usage:.2f} kWh, cost {i.cost:.2f} €')
    print("### Electricity consumption summary ###")
    return None

def main() -> None:
    print("Program starting.")
    rows = []
    dayUsages = []
    file_name = input("Insert filename: ")
    readFile(file_name, rows)
    timestamps = []
    parseRows(rows, timestamps)
    analyseTimestamps(timestamps, dayUsages)
    displayResults(dayUsages)
    rows.clear()
    timestamps.clear()
    dayUsages.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()