def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
test_function()

# при вызове вне функции def test_function(), результат NameError: name 'inner_function' is not defined.
# функция inner_function() вне области видимости