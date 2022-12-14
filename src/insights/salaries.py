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
    if type(job['max_salary']) != int or type(job['min_salary']) != int:
        raise ValueError('max and min salary must be a number')
    if int(job['min_salary']) > int(job['max_salary']):
        raise ValueError('min salary can not be greather than max salary')
    return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
