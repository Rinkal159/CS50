months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")

        if "/" in date:
            month = int(date[0 : date.find("/")])
            day = int(date[date.find("/") + 1 : date.rfind("/")])
            year = int(date[date.rfind("/") + 1 : ])

        else:
            if "," not in date:
                raise Exception
                
            date = date.replace(",", "").split(" ")

            if(date[0].title() not in months):
                raise Exception

            month = int(months.index(date[0].title()) + 1)
            day = int(date[1])
            year = int(date[2])

        if day > 31 or day <= 0 or month <= 0 or month > 12:
            raise Exception
        break

    except Exception:
        pass

print(f"{year}-{month:02d}-{day:02d}")
