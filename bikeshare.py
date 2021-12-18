import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def check_user_value(value_str, value_int):
    """Converts users string input to lower case and check for valid inputs

    Args:
        value_str str: user inputs
        value_int int: tracking int

    Returns:
        str: valid lower case
    """
    while True:
        value_entered = input(value_str).lower()
        try:
            if value_entered in ['chicago', 'new york city', 'washington'] and value_int == 0:
                break
            elif value_entered in ['january', 'february', 'march', 'april', 'may', 'june', 'all'] and value_int == 1:
                break
            elif value_entered in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'] and value_int == 2:
                break
            else:
                if value_int == 0:
                    print(
                        'wrong city entered.Please enter a valid city from the given list')
                if value_int == 1:
                    print(
                        'wrong month entered.Please enter a valid month from the given list')
                if value_int == 2:
                    print('day entered does not exist.Please enter a valid day')
        except ValueError:
            print('Input type does not match the given values')
    return value_entered


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
    city = check_user_value(
        'Enter a city from the given list: chicago, new york city or washington\n: ', 0)

    # TO DO: get user input for month (all, january, february, ... , june)
    month = check_user_value(
        "Enter a month from - (all, january, february, ... , june): ", 1)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = check_user_value(
        "which day of the week?(all, monday, tuesday, ... sunday): ", 2)

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: {}".format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print("The most common day of the week is: {}".format(
        df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print("The most common start hour is: {}".format(
        df['start hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is: {}".format(
        df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("The most commonly used end station is: {}".format(
        df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['frequent_route'] = df['Start Station'] + "," + df['End Station']
    print("The most frequent combination of start station and end station trip is: {}".format(
        df['frequent_route'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is: {}".format(
        df['Trip Duration'].sum()).round())

    # TO DO: display mean travel time

    print("The mean travel time is: {}".format(
        df['Trip Duration'].mean()).round())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
   print("Total user types is: {}".format(
        df['User Type'].value_counts().to_frame()))

   # TO DO: Display counts of gender
   if city != 'washington':
   print("Total counts of gender is: {}".format(
        df['Gender'].value_counts().to_frame()))

   # TO DO: Display earliest, most recent, and most common year of birth
   print("The earliest year of birth is: {}".format(
        int(df['Birth Year'].min())))
    print("The most recent year of bith is: {}".format(
        int(df['Birth Year'].max())))
    print("the most occuring year of bith is: {}".format(
        int(df['Birth Year'].mode()[0])))

   else:
        print("No gendery data for this city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """Displays raw data in chunks """
    # Prompt user whether the user wants to the raw data of the city to be displayed in chunks of five rows until no more
    # data available for dispaly
    print("\nRaw data is available in chunks of fives(5) rows")
    # get user input
    user_input = input(
        "Would like to display the data in rows of 5?, Please enter yes or no \n: ")
    if user_input.lower() == 'yes':
        value = 0
        while True:
            print(df.iloc[value:value+5])
            value += 5
            next_input = input(
                "Would you like to display more 5 rows of data?, yes or no\n: ")
            if next_input.lower() != 'yes':
                print("There is no more data to display.Thanks!")
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
