from datetime import datetime, timedelta
def main():
       date_string = "2024-03-24"
    date_object = datetime.strptime(date_string, "%Y-%m-%d").date()
    print(f"1. String '{date_string}' converted to date: {date_object}")
    t1 = datetime(2024, 3, 24, 10, 0, 0)
    t2 = datetime(2024, 3, 24, 10, 5, 30)
    diff_seconds = (t2 - t1).total_seconds()
    print(f"2. Difference in seconds: {diff_seconds} seconds")    
    now = datetime.now()
    print(f"3. Current: {now.strftime('%Y-%m-%d %H:%M:%S')}, Day: {now.strftime('%A')}")
    target_date = datetime(2024, 3, 24)
    added_date = target_date + timedelta(days=7)
    subtracted_date = target_date - timedelta(days=7)
    print(f"4. Original: {target_date.date()} | +7 Days: {added_date.date()} | -7 Days: {subtracted_date.date()}")
    def count_weekends(start, end):
        weekends = 0
        current = start
        while current <= end:
            if current.weekday() >= 5:
                weekends += 1
            current += timedelta(days=1)
        return weekends

    start_date = datetime(2024, 3, 1).date()
    end_date = datetime(2024, 3, 31).date()
    weekend_days = count_weekends(start_date, end_date)
    print(f"5. Weekends between {start_date} and {end_date}: {weekend_days} days")

if __name__ == "__main__":
    main()
