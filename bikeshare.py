import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city = ''       #global variable

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # TO DO: get user input for month (all, january, february, ... , june
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    city_list = ("chicago", "new york city", "washington")
    month_list = ("all","january","feburary","march","april","may","june","july","august","september","october","november","december")
    days_list = ("all","saturday","sunday","monday","tuesday","wednesday","thursday","friday")

    valid = False
    while not valid:
        city = input('Name of the city to analyze(example;chicago, new york city, washington)?: ')
        city = city.lower()

        if city in city_list:
            valid = True
        else:
            print('Please enter a city from Chicago, New york city, washington')

    valid = False
    while not valid:
        month = input('\nName of the month to analyze? or all?(example;all, january, february, ... , june.\n')
        month = month.lower()
        if month not in month_list:
            print('uhhh oh something went wrong, try again a valid input')
        else:
            valid = True

    valid = False
    while not valid:
        day = input('\nName of the day to analyze(example;all, monday, tuesday, ... sunday)? or all?.\n')
        day = day.lower()
        if day not in days_list:
            print('uhhh oh something went wrong, try again a valid input')
        else:
            valid = True

    print('-'*40)
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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day of week'] = df['Start Time'].dt.weekday_name

    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day of week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    commmon_month = df['month'].mode()[0]
    print('The most common month is: ', commmon_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day of week'].mode()[0]
    print('The most common day of week is: ', common_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: ", common_start_station)

    # TO DO: display most commonly used end
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']
    print('The most combination of start station and end station trip is: {}'.format((df['combination'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel= df['Trip Duration'].sum()
    print("The total of trip duration is", total_travel)

    # TO DO: display mean travel time
    mean_travel= df['Trip Duration'].mean()
    print("The mean of trip duration is", mean_travel)

    # Also doing some additional work
    min_travel= df['Trip Duration'].min()
    print("The least trip duration is", min_travel)

    max_travel= df['Trip Duration'].max()
    print("The most trip duration is", max_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].nunique()
    print ('Number of user types are: ', user_types)

    count_of_user_types = df['User Type'].value_counts()
    print('Count of various user types are:\n', count_of_user_types)

    # TO DO: Display counts of gender, only applicable in case of Chicago & NYC
    try:
        gender_count = df['Gender'].nunique()
        print ('\nThe count of gender is: ', gender_count)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = int(df['Birth Year'].min())
        latest_birth = int(df['Birth Year'].max())
        common_birth = int(df['Birth Year'].mode()[0])

        print('Earliest birth year from the given fitered data is: {}\n'.format(earliest_birth))
        print('Most recent birth year from the given fitered data is: {}\n'.format(latest_birth))
        print('Most common birth year from the given fitered data is: {}\n'.format(common_birth))
    except KeyError:
        print("\nThe city of {} does not contain gender and birth year information! Therefore, parameters like gender count, earliest birth year, most recent birth year, and most commonn birth year are not available to be displayed...\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df):

    index1 = 0
    index2 = 5

    while True:
        raw_data = input('Would you like to see 5 rows of data?\nPlease select yes or no.').lower()
        if raw_data == 'yes':
            print(df.iloc[index1:index2])
            index1 += 5
            index2 += 5
        else:
            print('\n----------NOW SHOWING SOME ANALYTICS FROM THE DATASET------------\n')
            break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        show_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()