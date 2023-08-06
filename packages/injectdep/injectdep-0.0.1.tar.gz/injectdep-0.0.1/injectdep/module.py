import inspect
from . import errors
from dataclasses import dataclass,field


@dataclass
class Module:
    """
        La clase módulo es un contenedor de dependencias
    """

    dependencies: dict = field(default_factory=dict)

    
    def get(self, name):
        if not name in self.dependencies:
            raise errors.DependencyNotFound(name)
        return self.dependencies[name]

    
    def register(self, dependency):
        self.dependencies[dependency.__name__] = dependency() if inspect.isclass(dependency) else dependency
        return dependency

    
    def mock_dependency(self, name, value):
        self.dependencies[name] = value

    
    def inject(self, func):
        args = inspect.getfullargspec(func).annotations

        injected_args = []

        for key in args:
            t = args[key]
            name = t.__name__
            dependency = self.get(name)
            injected_args.append(dependency)

        return lambda : func(*injected_args)
