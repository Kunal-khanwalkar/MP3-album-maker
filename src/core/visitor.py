class SignatureOverride:
    def __init__(self):
        pass

    def re_wire(self, classes):
        for cls in classes:
            for method in cls.__methods__:
                if (!method.bind.exists()):
                    return
                setattr(cls, method.__name__, override)
                def override(params):
                        method.bind(params)
                        method.__call__(params)
