def sleep_in(weekday, vacation):
    if weekday.lower()=='false' and vacation.lower()=='false':
        return True
    elif weekday.lower()=='true' and vacation.lower()=='false':
        return False
    elif weekday.lower()=='false' and vacation.lower()=='true':
        return True
wekday=input('Enter True if you are on a weekday and Enter False if you are not on Weekday: ')
vaction=input('Enter True if you are on Vacation and Enter False if you are not on Vacation: ')
sleep=sleep_in(weekday=wekday, vacation=vaction)
print(sleep)
