from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences('data/jobs.csv', 'Python') == 1639
    assert count_ocurrences('data/jobs.csv', 'JAVASCRIPT') == 122
    assert count_ocurrences('data/jobs.csv', 'xablau') == 0
