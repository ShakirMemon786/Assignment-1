from datetime import datetime,timedelta

current_datetime = datetime.now()

one_year_future_date = current_datetime + timedelta(days =365)

print('current date:',current_datetime)

print('one year from now date:',one_year_future_date)


three_days_before_date = current_dateTime - timedelta(days=3)

print('three days before date:',three_days_before_date)

