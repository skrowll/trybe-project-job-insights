from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    salary_list = []
    for job in jobs:
        if (job['max_salary'] != '' and job['max_salary'] != 'invalid'):
            salary_list.append(int(job['max_salary']))
    return max(salary_list)


def get_min_salary(path: str) -> int:
    jobs = read(path)
    salary_list = []
    for job in jobs:
        if (job['min_salary'] != '' and job['min_salary'] != 'invalid'):
            salary_list.append(int(job['min_salary']))
    return min(salary_list)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if 'max_salary' not in job or 'min_salary' not in job:
        raise ValueError('max and min salary are required')
    if (
        not str(job['max_salary']).isdigit()
        or not str(job['min_salary']).isdigit()
      ):
        raise ValueError('max and min salary must be a number')
    if int(job['min_salary']) > int(job['max_salary']):
        raise ValueError('min salary can not be greather than max salary')
    if not str(salary).lstrip('-').isdigit():
        raise ValueError('salary can not be negative')
    return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    jobs_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list.append(job)
        except Exception:
            continue
    return jobs_list
