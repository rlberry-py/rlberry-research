#
# Checks if numba is installed.
# -> If so, use numba.jit
# -> Otherwise, define numba_jit as a dummy decorator.
#
import rlberry.check_packages as check_packages

try:
    from numba import jit

    numba_jit = jit(nopython=True)
except:

    def numba_jit(func, **options):
        """This decorator does not modify the decorated function."""
        return func
