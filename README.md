# CHIROMETRICS - Chiropractic PI Patient Reports
Welcome to CHIROMETRICS, the simple software for effective Chiropractic PI Reports! ---v.01
Since most chiropractors utilize spreadsheets and similar platforms to keep track of patient data and journeys, I decided to create a simple program that explores these spreadsheets, analyzes the data and brings forth a visual report along with relevant PI..
...metrics for the clinic.

Prog Description(CHIROMETRICS version 0.01):
It is difficult to make accurate decisions without having a basic understanding of Clinic
numbers. This program helps you to know where the PI practice is struggling,
and where you need to focus your attention. I implore you to know your Personal Injury Clinic KPIs.

PROLOG:
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

****CODE OVERVIEW AND FUTURE UPDATE NOTES:****
First ere's an overview of the code:

1) **Data Loading and Cleaning:**
The script reads a CSV file named ******.csv** using the **pandas** library.
It extracts relevant columns: 'Date', 'Medpay', and 'Attorney'.
The **Date** column is filtered to retain only rows with valid date formats.

2) **Data Analysis:**
The script calculates the monthly average for new PI patients.
It identifies the month with the highest and lowest number of new PI patients.
The percentage of PI patients with Medpay is calculated.

3) **Attorney Analysis:**
The script analyzes attorney-related data, counting the number of new PI patients referred by each attorney.
It identifies the top two attorneys with the highest referrals.

4) **Data Visualization:**
The script uses **matplotlib** to create visualizations:
A bar graph depicting the annual patient visits month-to-month.
A pie chart illustrating the percentage of patients with Medpay.
A bar graph presenting the relationship with attorneys and their referral counts.

5) **User Interaction:**
The script prompts the user to generate a report by entering 'Y' or exit by entering 'N'.
The user's choice determines whether the visualizations are displayed.

**Future updates notes:**
User Interface: Consider developing a graphical user interface (GUI) to make it more user-friendly.
Export Options: Allow users to export visualizations and reports in various formats (PDF, Excel, etc.).
Integration with Other Software: Explore possibilities for integrating this tool with other chiropractic clinic management software.
Include more advance features and insights
