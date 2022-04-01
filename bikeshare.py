import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


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
    city = input('Choose a city: Chicago, New York City or Washington ').lower()
    while (city not in ['chicago', 'new york city', 'washington']):
        city = input('We only have data for 3 cities! Please choose between- Chicago, New York City, or Washington: ').lower()
    else:
    # TO DO: get user input for month (all, january, february, ... , june)
        month = input('Please select a month, January, February, March, April, May, June, or choose all: ').lower()
        while (month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']):
            month = input('Please choose between- January, February, March, April, May, June or all: ').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        else:
            day = input('Please select a day of the week, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or choose all: ').lower()
            while (day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']):
                day = input('Please choose between- Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all: ').lower()
            else:
                print('Great! Now, let\'s explore {} in {} on {}!'.format(city, month, day))
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
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour

    if month != 'all':
        months= ['january', 'february', 'march', 'april', 'may', 'june']
        month= months.index(month)+1
        df=df[df['month']==month]

    if day != 'all':
        df=df[df['day']==day.title()]

    return df
    city, month,day = get_filters()
    df=load_data(city,month,day)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print('Most Popular month: ', popular_month)
    # TO DO: display the most common day of week
    popular_day=df['day'].mode()[0]
    print('Most Popular day: ', popular_day)
    # TO DO: display the most common start hour
    popular_hour=df['hour'].mode()[0]
    print('Most Popular Start Hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]
    print('Most Popular Start Station: ', most_common_start_station)
    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print('Most Popular End Station: ', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip']=df['Start Station'] + " to " + df['End Station']
    most_common_trip=df['trip'].mode()[0]
    print('The most common trip is ', most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time_min = total_travel_time / 60
    print('Total travel time in minutes: ', total_travel_time_min.round(1))
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    mean_travel_time_min=mean_travel_time / 60
    print('Mean travel time in minutes: ', mean_travel_time_min.round(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print (user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print (gender_count)
    else:
        print('No gender data exists')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year']
        print ('The earliest birth year is ', int(birth_year.min()))
        print ('The most recent birth year is ', int(birth_year.max()))
        print ('The most common birth year is ', int(birth_year.mode()[0]))
    else:
        print('No birth year data exists')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Asks user if they would like to see data 5 lines at a time. """
    i = 0
    raw = input("Would you like to see the first 5 rows of data? Please type 'yes' or 'no'.").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("Would you like to see more data? Type 'yes' or 'no'.").lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
        print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
