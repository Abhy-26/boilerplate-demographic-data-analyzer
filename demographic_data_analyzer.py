
import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")
    race_count = df['race'].value_counts()
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    total_people = df.shape[0]
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)
    higher_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_edu_rich = higher_edu[higher_edu['salary'] == '>50K']
    lower_edu = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_edu_rich = lower_edu[lower_edu['salary'] == '>50K']
    higher_education_rich = round((higher_edu_rich.shape[0] / higher_edu.shape[0]) * 100, 1)
    lower_education_rich = round((lower_edu_rich.shape[0] / lower_edu.shape[0]) * 100, 1)
    min_work_hours = df['hours-per-week'].min()
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K']
    rich_percentage = round((rich_min_workers.shape[0] / min_workers.shape[0]) * 100, 1)
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    country_salary = country_salary.fillna(0)
    highest_earning_country = country_salary['>50K'].idxmax()
    highest_earning_country_percentage = round(country_salary['>50K'].max() * 100, 1)
    top_IN_occupation = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India for those who earn >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
