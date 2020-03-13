import time
import calendar
import pandas as pd
import numpy as np
import uuid

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

month_name_to_num = {name: num for num, name in enumerate(calendar.month_name) if num}
day_name_to_num = {name: num for num, name in enumerate(calendar.day_name)}

day_num_to_name = {num: name for num, name in enumerate(calendar.day_name)}
month_num_to_name = {num: name for num, name in enumerate(calendar.month_name) if num}

print(month_name_to_num)
print(day_name_to_num)

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = 'aaa'
    month = 'bbb'
    day = 'ccc'

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while (len(city) == 0) or (city.lower() not in CITY_DATA):
        city = input('Please select a city (chicago, new york city, washington) : ').strip().lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    m_list = list(calendar.month_name[1:7])
    m_list.append('All')
    while month not in m_list:
        month = input('Please select a Month (all, january, february, ... , june) : ').strip().title()

    d_list = list(calendar.day_name)
    d_list.append('All')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in d_list:
        day = input('day of week (all, monday, tuesday, ... sunday) : ').strip().title()

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df["month_num"] = pd.DatetimeIndex(df["Start Time"]).month
    df["day_num"] = pd.DatetimeIndex(df["Start Time"]).dayofweek
    df["hour_num"] = pd.DatetimeIndex(df["Start Time"]).hour

    if month != 'All':
        df = df[df['month_num'] == month_name_to_num[str(month)]]

    if day != 'All':
        df = df[df['day_num'] == day_name_to_num[str(day)]]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('most common Month {} '.format(month_num_to_name[df["month_num"].value_counts().idxmax()]))

    # TO DO: display the most common day of week
    print('most common Day {} '.format(day_num_to_name[df["day_num"].value_counts().idxmax()]))

    # TO DO: display the most common start hour
    print('most common Hour {} '.format(df["hour_num"].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most commonly used start station {} '.format(df["Start Station"].value_counts().idxmax()))

    # TO DO: display most commonly used end station
    print('most commonly used end station {} '.format(df["End Station"].value_counts().idxmax()))

    # TO DO: display most frequent combination of start station and end station trip
    print('most frequent combination of start station and end station trip {} '
          .format(df.groupby(['Start Station','End Station']).size().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time {} '.format(df["Trip Duration"].sum()))

    # TO DO: display mean travel time
    print('mean travel time {} '.format(df["Trip Duration"].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types {} '.format(df["User Type"].nunique()))
    print('counts of user types {} '.format(df["User Type"].value_counts()))

    # TO DO: Display counts of gender
    print('counts of user types {} '.format(df["Gender"].value_counts()))

    # TO DO: Display earliest, most recent, and most common year of birth
    print('earliest year of birth {} '.format(df['Birth Year'].min()))
    print('most recent year of birth {} '.format(df['Birth Year'].max()))
    print('most common year of birth {} '.format(df["Birth Year"].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


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
