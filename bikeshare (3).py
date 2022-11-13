import time
import pandas as pd
import numpy as np
df=pd.read_csv("washington.csv")
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

 # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
def get_city():
   
    city = ''
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or'
                     ' Washington?\n')
        if city.lower() == 'chicago':
            return 'chicago.csv'
        elif city.lower() == 'new york':
            return 'new_york_city.csv'
        elif city.lower() == 'washington':
            return 'washington.csv'
        else:
            print('Sorry, I do not understand your input. Please input either '
                  'Chicago, New York, or Washington.')

 # TO DO: get user input for month (all, january, february, ... , june)
def get_month():
   
    month_input = ''
    months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
    while month_input.lower() not in months_dict.keys():
        month_input = input('\nWhich month? January, February, March, April,'
                            ' May, or June?\n')
        if month_input.lower() not in months_dict.keys():
            print('Sorry, I do not understand your input. Please type in a '
                  'month between January and June')
    month = months_dict[month_input.lower()]
    return ('2017-{}'.format(month), '2017-{}'.format(month + 1))

 # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
def get_day():
   
    this_month = get_month()[0]
    month = int(this_month[5:])
    valid_date = False
    while valid_date == False:    
        is_int = False
        day = input('\nWhich day? Please type your response as an integer.\n')
        while is_int == False:
            try:
                day = int(day)
                is_int = True
            except ValueError:
                print('Sorry, I do not understand your input. Please type your'
                      ' response as an integer.')
                day = input('\nWhich day? Please type your response as an integer.\n')
        try:
            start_date = datetime(2017, month, day)
            valid_date = True
        except ValueError as e:
            print(str(e).capitalize())
    end_date = start_date + timedelta(days=1)
    return (str(start_date), str(end_date))

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
   
    return df

def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

 # TO DO: display the most common month
def popular_month(df):
   
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['start_time'].dt.month.mode())
    most_pop_month = months[index - 1]
    print('The most popular month is {}.'.format(most_pop_month))


 # TO DO: display the most common day of week
def popular_day(df):
   
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
    index = int(df['start_time'].dt.dayofweek.mode())
    most_pop_day = days_of_week[index]
    print('The most popular day of week for start time is {}.'.format(most_pop_day))

# TO DO: display the most common start hour
def popular_hour(df):
   
    most_pop_hour = int(df['start_time'].dt.hour.mode())
    if most_pop_hour == 0:
        am_pm = 'am'
        pop_hour_readable = 12
    elif 1 <= most_pop_hour < 13:
        am_pm = 'am'
        pop_hour_readable = most_pop_hour
    elif 13 <= most_pop_hour < 24:
        am_pm = 'pm'
        pop_hour_readable = most_pop_hour - 12
    print('The most popular hour of day for start time is {}{}.'.format(pop_hour_readable, am_pm))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
   
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

 # TO DO: display most commonly used start station&   # TO DO: display most commonly used end station

def popular_stations(df):
   
    pop_start = df['start_station'].mode().to_string(index = False)
    pop_end = df['end_station'].mode().to_string(index = False)
    print('The most popular start station is {}.'.format(pop_start))
    print('The most popular end station is {}.'.format(pop_end))

 # TO DO: display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

 # TO DO: Display counts of user types
def users(df):
  
    subs = df.query('user_type == "Subscriber"').user_type.count()
    cust = df.query('user_type == "Customer"').user_type.count()
    print('There are {} Subscribers and {} Customers.'.format(subs, cust))

 # TO DO: Display counts of gender
def gender(df):
 
    male_count = df.query('gender == "Male"').gender.count()
    female_count = df.query('gender == "Male"').gender.count()
    print('There are {} male users and {} female users.'.format(male_count, female_count))

 # TO DO: Display earliest, most recent, and most common year of birth
def birth_years(df):
  
    earliest = int(df['birth_year'].min())
    latest = int(df['birth_year'].max())
    mode = int(df['birth_year'].mode())
    print('The oldest users are born in {}.\nThe youngest users are born in {}.'
          '\nThe most popular birth year is {}.'.format(earliest, latest, mode))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
