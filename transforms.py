def transform1(a, b):
    """y = ax + b"""
    def f(x):
        return a*x + b
    return f