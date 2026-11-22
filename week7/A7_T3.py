WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

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

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    # Append results to the PResults list
    # Initialise helper list 
    WeekdayTimestampAmount: list[int] = [0, 0, 0, 0, 0, 0, 0]
    for i in PRows:
        for j in WEEKDAYS:
            if i.startswith(j):
                WeekdayTimestampAmount[WEEKDAYS.index(j)] +=1
    for i in range(len(WeekdayTimestampAmount)):
        PResults.append(' - ' + str(WEEKDAYS[i]) + ' ' + str(WeekdayTimestampAmount[i]) + ' stamps')
    WeekdayTimestampAmount.clear()
    #print(PResults)
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for i in PResults:
        print(i)
    print("### Timestamp analysis ###")
    return None

def main() -> None:
    print("Program starting.")
    rows = []
    results = []
    file_name = input("Insert filename: ")
    readFile(file_name, rows)
    analyseTimestamps(rows, results)
    displayResults(results)
    rows.clear()
    results.clear()
    print("Program ending.")
    return None

main()