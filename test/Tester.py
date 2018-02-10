import inspect


class Tester(object):

    def __init__(self, class_name):
        self.test_methods = self.__get_test_methods(class_name)

    def __get_test_methods(self, class_name):
        class_member_tuples = inspect.getmembers(class_name, predicate=inspect.isroutine)
        test_methods = [x[0] for x in class_member_tuples if x[0].startswith('test')]
        return test_methods

    def run(self):
        for test_method in self.test_methods:
            eval('self.{}()'.format(test_method))
        print('Success!')
