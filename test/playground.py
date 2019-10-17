from src.utils import dump_args


@dump_args
def test(a, b=4, c='blah-blah', *args, **kwargs):
    pass


test(1)
test(1, 3)
test(1, d=5)
test(1, 2, 3, 4, 5, d=6, g=12.9)
