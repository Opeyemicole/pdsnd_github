import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all','january', 'february', 'march', 'april', 'may', 'june']

days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        try:
            city = str(input("Hello! kindly enter your city: ")).lower()
        except ValueError:
            print("Oops theres an error in your entry.")
            continue

        if city not in CITY_DATA:
            print("Kindly select Chicago/Washington/New york")
            continue
        else:
        #city inputs parsed,
        #exiting loop.
            break


    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input("Please enter the month: ")).lower()
        except ValueError:
            print("oops!, i didnt get that.")
            continue


        if month not in months:
            print("Please enter a month between january to june or all to apply no filters")


            continue
        else:

        #city inputs parsed,
        #exiting loop.
            break
    if month == 'all':
          print(months[1:])



    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input("Please enter the day: ")).lower()
        except ValueError:
            print("oops!, i didnt get that.")
            continue

        if day not in days:
            print("Please enter a day of the week or all to apply no filters")

            continue
        else:

         #city inputs parsed,
        #exiting loop.
            break
    if day == 'all':
        print(days[1:])

    print('+'*40)
    return city, month, day


    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)




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
    data = CITY_DATA[city]
    df = pd.read_csv(data)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                  'may': 5, 'june': 6}

         # filter by month to create the new dataframe
        df = df.loc[df['month'] == months[month]]



    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe

        days = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3,
                  'friday': 4, 'saturday': 5, 'sunday': 6}
        df = df.loc[df['day_of_week'] == days[day]]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is", common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is", common_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is", str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_used_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station:', commonly_used_start_station)

    # TO DO: display most commonly used end station
    commonly_used_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station:', commonly_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_combo = (df['Start Station'] + ' and ' + df['End Station']).mode()[0]
    print('The most frequent combination of start station and end station is', start_end_combo)



    df['start end station'] = df['Start Station'] + ' and ' + df['End Station']
    popular_start_end_station = df['start end station'].mode()[0]


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is:', str(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is:', str(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usertype_count = df['User Type'].value_counts()
    print('Count of user types in your selected data is:', usertype_count)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:                                            # checking to see if dataframe contains Gender column
        gender_count = df['Gender'].value_counts()
        print('The count of gender in your selected data is', str(gender_count))

    else:
        print("We currently dont have data for the selected gender")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:                                       # checking to see if dataframe contains Gender column
        earliest_birth = df['Birth Year'].min()
        print('Earliest year of birth is', int(earliest_birth))

        most_recent  = df['Birth Year'].max()
        print('Most recent year of birth is', int(most_recent))

        most_common = df['Birth Year'].mode()
        print('Most common year of birth is', int(most_common))


    else:
        print("TWe currently dont have data for the selected birth year")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):

    while True:
        choice=['yes','no']
        data_display= input("Would you like to view individual trip data (5 entries)? Type 'yes' or 'no'\n").lower()
        if data_display in choice:
            if data_display=='yes':
                start=0
                end=5
                data = df.iloc[start:end,:9]
                print(data)
            break
        else:
            print("Please enter a valid response")
    if  data_display=='yes':
            while True:
                data_displayII= input("Would you like to view more trip data? Type 'yes' or 'no'\n").lower()
                if data_displayII in choice:
                    if data_displayII=='yes':
                        start+=5
                        end+=5
                        data = df.iloc[start:end,:9]
                        print(data)
                    else:
                        break
                else:
                    print("Please enter a valid response")



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
