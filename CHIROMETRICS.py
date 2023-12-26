# File: CHIROMETRICS.py
# Author: Darling Ngoh
# Date:12/26/23

"""
Prog Description(CHIROMETRICS version 0.01):
    It is difficult to make accurate decisions without having a basic understanding of Clinic
    numbers. This program helps you to know where the PI practice is struggling,
    and where you need to focus your attention. I implore you to know your Personal Injury Clinic KPIs.

PROLOG:
    Reference parameters needed:
    pt visit dates, medpay, attorney info

    What questions can bring greater insights?
    Exploration:
    What is the monthly average for New PI patients?
    Who is the top referral firm, avg referrals, and how many thus far?
    What percentage of the clinics pi pt’s have med pay?

    Visualization:
    Visualize attorney relationships, what are the number of referrals monthly
    Visualize the annual patient visits month-to-month
    Visualize pt with med pay vs pt without medpay, month-to-month and annual

    Recommendations given parameters with spreadsheet data inputs:
        Date: *ONLY date format, either 1/2 or 1-2 format accepted
        Medpay: *ONLY binary option of Yes/No accepted
        Attorney: *ONLY input attorney name/law firm or between the three similar options
                        - 'No Atty', 'No Atty yet', 'Unattached'
"""

import pandas as pd
# import math (*only if needed)
import matplotlib.pyplot as plt

# global variables
global max_month
global min_month
global max_text
global min_text
global atty_dict
global attorney_summary_text
global medpay_percentage
global medpay_percentage_info
global unattached_cases_info
global atty_dict
global max_atty
global second_atty



# initialize csv file into pandas dataframe for sorting and exploration
# specify the file path and columns to be selected, for this report only {visit date, medpay, attorney} info needed
relevant_param = ['Date', 'Medpay', 'Attorney']
file_name = '2023 New PI Patient Log - Test Data.csv'
HealthInfo = pd.read_csv(file_name, usecols=relevant_param)

# set condition to remove months from 2023 new pi visit dates column so only dates remain
condition = (HealthInfo['Date'].str.contains('1')) | (HealthInfo['Date'].str.contains('2')) |\
             (HealthInfo['Date'].str.contains('3')) | (HealthInfo['Date'].str.contains('4')) |\
            (HealthInfo['Date'].str.contains('5')) | (HealthInfo['Date'].str.contains('6')) |\
            (HealthInfo['Date'].str.contains('7')) | (HealthInfo['Date'].str.contains('8')) |\
            (HealthInfo['Date'].str.contains('9'))

# save new dataframe without months inbetween visit dates given rows
sorted_HealthInfo = HealthInfo[condition]
#print(sorted_HealthInfo)

# save visit dates in relevant list for numerical analysis
January = []
February = []
March = []
April = []
May = []
June = []
July = []
August = []
September = []
October = []
November = []
December = []
for char in sorted_HealthInfo['Date']:
    if char[0] == '2':
        February.append(char)
    elif char[0] == '3':
        March.append(char)
    elif char[0] == '4':
        April.append(char)
    elif char[0] == '5':
        May.append(char)
    elif char[0] == '6':
        June.append(char)
    elif char[0] == '7':
        July.append(char)
    elif char[0] == '8':
        August.append(char)
    elif char[0] == '9':
        September.append(char)
    elif char[:2] == '10':
        October.append(char)
    elif char[:2] == '11':
        November.append(char)
    elif char[:2] == '12':
        December.append(char)
    else:
        January.append(char)


# What is the monthly average for New PI patients?
avg_monthly_pi = (len(January) + len(February) + len(March) + len(April) + len(May) +
                  len(June) + len(July) + len(August) + len(September) + len(October) +
                  len(November) + len(December)) // 12
#print(avg_monthly_pi)

tot_annual_pi_volume = (len(January) + len(February) + len(March) + len(April) + len(May) +
                        len(June) + len(July) + len(August) + len(September) + len(October) +
                        len(November) + len(December))

# structure new pi visit dates and month as value and key set in dictionary
monthly_visit_dict = {'January': January, 'February': February, 'March': March, 'June': June,
                      'July': July, 'August': August, 'September': September, 'October': October,
                      'November': November, 'December': December}
#print(monthly_visit_dict)

# test function to display month with corresponding # of pt new pi visits
def display_monthly_visit_num ():
    for key2, val in monthly_visit_dict.items():
        print(key2, len(val))
#display_monthly_visit_num()


# what is the month with the highest pi's and how many
def highest_month():
    counter = 0
    global max_month
    global max_text
    for key in monthly_visit_dict: # keep track of key
        if len(monthly_visit_dict[key]) > counter:
            counter = len(monthly_visit_dict[key])
            max_month = key
    max_text = f'Your HIGHEST month for new PI patients was {max_month.upper()} with {counter} new visits.'
    #print(max_text)


highest_month()


# what is the month with the lowest pi's and how much
def lowest_month():
    counter = 1000  # arbitrary benchmark for finding minimum monthly visits
    global min_month
    global min_text
    for key in monthly_visit_dict:  # iterate through monthly dictionary values and find minimum monthly visits
        if len(monthly_visit_dict[key]) < counter:
            counter = len(monthly_visit_dict[key])
            min_month = key
    min_text = f'Your LOWEST month for new PI patients was {min_month.upper()} with {counter} visits.'
    # print(min_text)


lowest_month()


# What percentage of the clinics pi pt’s have med pay?
def find_medpay_percentage():
    global medpay_percentage
    global medpay_percentage_info

    condition_for_medpay = (sorted_HealthInfo['Medpay'].str.contains('Y') | sorted_HealthInfo['Medpay'].str.contains('y'))
    number_of_medpay_pts = (sorted_HealthInfo[condition_for_medpay])
    medpay_percentage = (len(number_of_medpay_pts)/len(sorted_HealthInfo))*100

    medpay_percentage_info = (f'Percentage of PI patients this year with MEDPAY: {medpay_percentage:.1f}%\n'
                              f'Out of {len(sorted_HealthInfo)} annual new PI patients, only '
                              f'{len(number_of_medpay_pts)} had Medpay.')


find_medpay_percentage()


# Who is the top referral firm, avg referrals, and how many thus far?
def attorney_info():
    global atty_dict
    global unattached_cases_info
    global atty_dict
    atty_dict = {}
    # create a dataframe without missing attorney data row
    has_attorney_info = sorted_HealthInfo['Attorney'].dropna(axis=0)

    # find number of New PI pts that didn't have attorney documentation
    not_documented_count = len(sorted_HealthInfo['Attorney']) - len(has_attorney_info)
    # update not found count value in dictionary for key NAN
    atty_dict['not found'] = not_documented_count

    # iterate through set, add each attorney as a unique key in the dictionary with matching count of terms found
    for atty in has_attorney_info:
        base_case = has_attorney_info.str.contains(atty)
        count_attorney_term = has_attorney_info[base_case]
        atty_dict[atty] = len(count_attorney_term)

    # display attorney information dictionary
    #for key, term in atty_dict.items():
        #if term > 2:
            #print(key, term)

    # find number of unattached cases by searching count of terms surrounding 'no atty yet'/'no atty'
    unattached_cases = (0 + atty_dict['Unattached'])
    unattached_cases_info = (f'TOTAL # of UNATTACHED CASES: {unattached_cases} '
                             f'(*classified using results for "no atty/unattached" cases*)\n')

    #number of unique attorneys
    unique_atty_sum = []
    for val in atty_dict:
        if val != 'not found':
            if val != 'Unattached':
                unique_atty_sum.append(val)

    # who is the highest attorney referral and how many?
    def highest_atty():
        global attorney_summary_text
        global max_atty
        counter = 0
        # count_track = []
        max_atty = ''
        for name in atty_dict:  # keep track of key
            # count_track.append(atty_dict[name])
            if name != 'not found':
                if name != 'No Atty':
                    if name != 'Unattached':
                        if name != 'No Atty yet':
                            if atty_dict[name] > counter:
                                counter = atty_dict[name]
                                max_atty = name

        # find 2nd top attorney referral
        global second_atty
        counter2 = 0
        second_atty = ''
        for second in atty_dict:
            if second != 'not found':
                if second != max_atty:
                    if second != 'No Atty':
                        if second != 'Unattached':
                            if second != 'No Atty yet':
                                if atty_dict[second] > counter2:
                                    counter2 = atty_dict[second]
                                    second_atty = second

        # find percentage for top 2 attorney referrals given overall new PI volume thus far
        top2_atty_percentage = (counter + counter2) / len(sorted_HealthInfo) * 100

        # display relevant attorney relationship information
        attorney_summary_text = (f'ANNUAL ATTORNEY RELATIONSHIP SUMMARY:\n'
                                 f'DISCLAIMER...given the current dataset, \n{not_documented_count}'
                                 f' new PI patients not documented as having an attorney or unattached\n'
                                 f'---------------------------------------------------------'
                                 f'------------------------------\n'
                                 f'Total # of unique attorneys this year: {len(unique_atty_sum)}\n'
                                 f'Your HIGHEST referral was from {max_atty.upper()} with {counter} new PI referrals.\n'
                                 f'Your 2nd HIGHEST referral was from {second_atty.upper()} with {counter2} '
                                 f'new PI referrals.\n\nTogether, your top two attorney referrals {max_atty.upper()} \n'
                                 f'and {second_atty.upper()} have sent ' 
                                 f'{counter2 + counter} combined new PI referrals.\nThis makes up roughly '
                                 f'{top2_atty_percentage:.1f}% of your PI volume.')


        #print(attorney_summary_text)

        # 80/20 rule for future development...display the top 20% attorneys providing 80% of clinics business
        '''
        80/20 RULE aka Pareto Principle
        1) find length of unique attorney list
        2) multiply number of unique attorneys by .20 which is 20% to get number of attys driving 80% 
            of clinics PI business
        
        3) create function to loop through dictionary of unique attorneys and number of referrals to find top
            20% attorney firms and their relevant referral count 
                - Loop range is determined by 20% of total number of atty referrals
                - this algorithm should result in a list of the clinics top PI law firms driving 80% of their traffic
                    as this should be the 20% that should be optimized for the atomic network effects
        '''

    highest_atty()


attorney_info()


'''
    Visualization:
    Visualize attorney relationships, what are the number of referrals monthly
    Visualize the annual patient visits month-to-month
    Visualize pt with med pay vs pt without medpay, month-to-month and annual
'''

# data for months and number of PI visits
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']
numVisits_perMonth = [len(January), len(February), len(March), len(April), len(May),
                      len(June), len(July), len(August), len(September), len(October),
                      len(November), len(December)]

# data for attorney info
attorneys = atty_dict
atty_name = []
atty_num_referrals = []

# iterate and add relevant attorney names with corresponding referral counts
for key, value in attorneys.items():
    atty_name.append(key)
    atty_num_referrals.append(value)


# create subplots for annual pi visits, other 2 are attorney relationships, and medpay charts
def visualize_annual_pi_report():
    plt.subplot(3, 1, 1)

    # create bar graph for monthly pi visits
    plt.bar(months, numVisits_perMonth)

    # add value labels on top of the bars
    for i, value in enumerate(numVisits_perMonth):
        plt.text(i, value + 0.5, str(value), ha='center', va='bottom')

    #info text
    info_text = (f'Program Name: CHIROMETRICS.io\n'
                 f'Algorithm author: Darling Ngoh\n'
                 f'Contact: darlingngoh@gmail.com\n'
                 f'File in use: {file_name}')

    plt.text(len(months)+1, max(numVisits_perMonth) + 7, info_text, color='red', fontsize=8, ha='right', va='bottom')

    # include summary text
    summary_text = (f'ANNUAL PI VISITS SUMMARY:\n'
                    f'TOTAL # of PI visits thus far: {tot_annual_pi_volume}\n'
                    f'{unattached_cases_info}'
                    f'{max_text}\n{min_text}\nAverage monthly PI visits: {avg_monthly_pi}')
    plt.text(-2, max(numVisits_perMonth) + 4, summary_text, fontsize=11, ha='left', va='bottom')


    # set plot title and labels
    plt.title('2023 Annual PI Patient Visits')
    plt.xlabel('Months')
    plt.ylabel('# of New PI patients')

    # choose subplots for medpay chart
    no_medpay = (100 - medpay_percentage) # find percentage of those without medpay
    annual_medpay_results = [medpay_percentage, no_medpay]

    # create pie chart for medpay
    result = ['HAD MEDPAY', 'DID NOT HAVE MEDPAY']
    plt.subplot(3, 1, 2)
    plt.pie(annual_medpay_results, labels=result, autopct='%1.1f%%', startangle=90)

    # include summary text
    summary_text_medpay = f'{medpay_percentage_info}'
    plt.text(-8, max([0, 0]), summary_text_medpay, fontsize=11, ha='left', va='bottom')

    # choose bar chart for attorney
    plt.subplot(3, 1, 3)
    plt.bar(atty_name, atty_num_referrals)

    # add value labels on top of the bars
    for i, val in enumerate(atty_num_referrals):
        plt.text(i, val + 0.5, str(val), ha='center', va='bottom')

    # include summary text
    summary_text_atty = attorney_summary_text
    plt.text(len(atty_name)-13, max(atty_num_referrals)+2, summary_text_atty, fontsize=11, ha='left', va='bottom')

    # set plot title and labels
    plt.title('2023 Attorney Referral Relationships')
    plt.xticks(rotation=45)  # adjust the rotation angle as needed
    plt.xlabel('')
    plt.ylabel('# of New PI referrals')

    # display plot
    plt.show()

#driver code
def driver():
    print('\nWelcome to CHIROMETRICS, the simple software for effective Chiropractic PI Reports! ---v.01')
    print(f'File in dataset: "{file_name}"\n\n')
    user_input = input(f'Enter Y to generate your report or N to exit: ').upper()

    if user_input == 'Y':
        visualize_annual_pi_report()
    else:
        print('Thank you for your time and have a great day!')


driver()
