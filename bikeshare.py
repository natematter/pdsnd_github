import time
import pandas as pd
import numpy as np
# nm
START_TITLE = """
            _   _ ____    ____  _ _             _                    
           | | | / ___|  | __ )(_) | _____  ___| |__   __ _ _ __ ___ 
           | | | \___ \  |  _ \| | |/ / _ \/ __| '_ \ / _` | '__/ _ \\
           | |_| |___) | | |_) | |   <  __/\__ \ | | | (_| | | |  __\\
            \___/|____/  |____/|_|_|\_\___||___/_| |_|\__,_|_|  \___\
                                                                     
                              ____        _                           
                             |  _ \  __ _| |_ __ _                   
                             | | | |/ _` | __/ _` |
                             | |_| | (_| | || (_| |
                             |____/ \__,_|\__\__,_|
                                                   
"""

ALL_MONTHS = 'all'
ALL_DAYS = 'all'
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

TIME_MONTHS = ['january', 'feburary', 'march', 'april', 'may', 'june']

TIME_DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filter_city():
    """
    Helper function used to verify the city the user selects has DATA to analyze

    Returns:
        (str) city or None
    """
    print('The options to choose from are:')
    for city_option in CITY_DATA.keys():
        print(' <> ', city_option.title())

    print()
    choice = input('Enter city name: ')
    print()
    if choice.lower() in CITY_DATA.keys():
        return choice.lower()
    else:
        print('The city [', choice, '] is not an option at this time!\n')
        print('Please choose again.\n\n')
        return None

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city = None
    month = ALL_MONTHS
    day = ALL_DAYS
    print('Hello! Let\'s explore some US bikeshare data!')
    print()
    print('Please select a city from the options below:')
    while city == None:
        city = get_filter_city()

    print()
    print('Would you like to filter the data by month, day, or none (not at all)?')

    while True:
        print()
        # get user input for month (all, january, february, ... , june)
        time_choice = input('Enter time filter options [ month | day | all (no filter) ]: ')

        if time_choice.lower() == 'month':
            while True:
                print('Please select one of the following months:\n')
                for m in TIME_MONTHS:
                    print(' <> ', m.title())
                print()
                month_choice = input('Please enter the month name: ')
                if month_choice.lower() not in TIME_MONTHS:
                    print(month_choice, 'is not available!\n\n')
                else:
                    month = month_choice.lower()
                    break
            #break
        elif time_choice.lower() == 'day':
            while True:
                # get user input for day of week (all, monday, tuesday, ... sunday)
                print('Please select a specific day:\n')
                for d in TIME_DAYS:
                    print(' <> ', d.title())
                print()
                day_choice = input('Please enter the day name: ')
                if day_choice.lower() not in TIME_DAYS:
                    print(day_choice, 'is not available!\n\n')
                else:
                    day = day_choice.lower()
                    break
            #break
        elif time_choice.lower() == 'all':
            # No filters applied
            month = ALL_MONTHS 
            day = ALL_DAYS
        else:
            print('The option of', time_choice , 'is not available!')
            print('Defaulting to no filter!')

        print('-'*79)
        print('You have selected to filter the data with the following options:')
        print(' ==> City: {}'.format(city.title()))
        print(' ==> Months: {}'.format(month.title()))
        print(' ==> Days: {}'.format(day.title()))
        print()
        print('Would you like to continue with these settings?')
        refilter = input(' <> Enter yes to proceed with anaylsis or no to change filter settings: ')
        if refilter.lower() == 'yes':
            break

    print('-'*79)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # convert the End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month from Start Time to create new month column
    df['month'] = df['Start Time'].dt.month

    # extract day of week from Start Time to create new day column
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # extract the Start and End Station columns to create a route column
    df['route'] = 'FROM: ' + df['Start Station'] + ' TO: ' + df['End Station']

    # filter by month if applicable
    if month != ALL_MONTHS:
        # use the index of the months list to get the corresponding int
        month = TIME_MONTHS.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    if day != ALL_DAYS:
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        (dataframe) df - a pandas dataframe
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month is ==> ', TIME_MONTHS[most_common_month-1].title())
    print()

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day of the week is ==> {}'.format(most_common_day))
    print()

    # display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('Most common hour is ==> {}:00'.format(most_common_hour))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.

    Args:
        (dataframe) df - a pandas dataframe
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mc_start_station = df['Start Station'].mode()[0]
    print('Most popular start station is ==> {}'.format(mc_start_station))
    print()

    # display most commonly used end station
    mc_end_station = df['End Station'].mode()[0]
    print('Most popular end station is ==> {}'.format(mc_end_station))
    print()

    # display most frequent combination of start station and end station trip
    mc_route = df['route'].mode()[0]
    print('Most popular trip route ==> {}'.format(mc_route))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    Args:
        (dataframe) df - a pandas dataframe
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time in minutes
    total_duration = round(df['Trip Duration'].sum() / 60.0, 1)
    print('Total travel time is ==> {} (minutes)'.format(total_duration))
    print()

    # display mean travel time in minutes
    mean_duration = round(df['Trip Duration'].mean() / 60.0, 1)
    print('Mean travel time is ==> {} (minutes)'.format(mean_duration))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.

    Args:
        (dataframe) df - a pandas dataframe
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('Counts of User Types...\n')
    print(user_types_count)
    print()

    # Display counts of gender
    if 'Gender' in df.keys():
        gender_count = df['Gender'].value_counts()
        print('Counts of Gender...\n')
        print(gender_count)
        print()
    else:
        print('Gender not available in data set.\n')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.keys():
        print('Birth Year Info...\n')
        earliest_year = int(df['Birth Year'].min())
        print('Earliest Birth Year ==> {}'.format(earliest_year))
        latest_year = int(df['Birth Year'].max())
        print('Most Recent Birth Year ==> {}'.format(latest_year))
        mc_year = int(df['Birth Year'].mode()[0])
        print('Most Common Birth Year ==> {}'.format(mc_year))
    else:
        print('Birth Year not available in data set.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_raw_data(df):
    """Displays the raw data (5 rows at a time) of the DataFrame"""
    showraw = input('\nWould you like to see the raw data? Enter yes or no.\n')
    if showraw.lower() == 'yes':
        begin = 0
        end = 5
        print('-'*40)
        print(df.info())
        while True:
            print('-'*40)
            with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                print(df.iloc[begin:end])
            print('-'*40)
            moredata = input('\nShow more data? Enter yes or no.\n')
            if moredata.lower() != 'yes':
                break
            else:
                begin = end
                end += 5

def main():
    print('-'*79)
    print(START_TITLE)                                               
    print('-'*79)
    while True:
        try:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            get_raw_data(df)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        except KeyboardInterrupt:
            print('\n\nThanks for exploring US Bikeshare Data!\n\n')
            exit(0)


if __name__ == "__main__":
	main()

