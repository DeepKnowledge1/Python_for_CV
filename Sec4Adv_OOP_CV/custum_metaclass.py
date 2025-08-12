# https://www.godaddy.com/engineering/2018/12/20/python-metaclasses/
def abstractfunc(func):
    func.__isabstract__ = True
    return func


class MetaInterface(type):

    def __init__(cls, name, bases, namespace):
        for base in bases:
            must_implement = getattr(base, "abstract_methods", [])
            class_methods = getattr(cls, "all_methods", [])
            for method in must_implement:
                if method not in class_methods:
                    err_str = """Can't create abstract class {name}!
                    {name} must implement abstract method {method} of class {base_class}!""".format(
                        name=name, method=method, base_class=base.__name__
                    )
                    raise TypeError(err_str)
        """ Defining Your Own Rules  """

        if cls.__name__[0].isupper():
            """Create class only if First Letter is Capital"""

            for k, v in namespace.items():
                if hasattr(v, "__call__"):
                    if v.__name__[0] == "_" or v.__name__[0].islower():
                        """check name function starts with _ or lower case"""

                        if v.__doc__ is None:
                            """Check is User has provided Documentation"""
                            err_str = """Make sure to Provide Documentation check:
                                    method [{method}] of class {base_class}!""".format(
                                name=name, method=v.__name__, base_class=cls.__name__
                            )
                            raise TypeError(
                                err_str
                            )  # raise ValueError("Make sure to Provide Documentation check {}".format(v.__name__))
                        else:
                            """if function has Doccumentation pass"""

                            pass
                    else:
                        """function name starts with upper case throw error"""
                        err_str = """Function should start with Lower case:
                                    method [{method}] of class {base_class}!""".format(
                            name=name, method=v.__name__, base_class=cls.__name__
                        )
                        raise TypeError(
                            err_str
                        )  # raise ValueError("Make sure to Provide Documentation check {}".format(v.__name__))

                        # raise ValueError("Function should start with Lower case :{}".format(v.__name__))
        else:
            err_str = """Class [{name}] should start with Capital Letter!""".format(
                name=cls.__name__
            )
            raise TypeError(
                err_str
            )  # raise ValueError("Make sure to Provide Documentation check {}".format(v.__name__))

            # raise ValueError("Class Name  should start with Capital Letter :{} ".format(cls.__name__[0]))

    def __new__(metaclass, name, bases, namespace):
        namespace["abstract_methods"] = MetaInterface._get_abstract_methods(namespace)
        namespace["all_methods"] = MetaInterface._get_all_methods(namespace)
        cls = super().__new__(metaclass, name, bases, namespace)
        return cls

    def _get_abstract_methods(namespace):
        return [
            name
            for name, val in namespace.items()
            if callable(val) and getattr(val, "__isabstract__", False)
        ]

    def _get_all_methods(namespace):
        return [name for name, val in namespace.items() if callable(val)]
