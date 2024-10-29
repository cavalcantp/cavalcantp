# singleton is a class that can only have one instance of it instanciated
# use cases: mainting single copy of app state
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # Create the instance
        return cls._instance

    def __init__(self):
        # Initialization code here (will not run multiple times)
        pass
# Example
class ApplicationState:
    instance = None
    def __init__(self):
        self.isLoggedIn = False
    
    @classmethod
    def getAppState(cls):
        if not cls.instance:
            cls.instance = ApplicationState()
        return cls.instance
    
if __name__ == "__main__":
    print(ApplicationState.instance)
    appState1 = ApplicationState.getAppState()
    print(appState1.isLoggedIn)
    print(ApplicationState.instance)

    appState2 = ApplicationState.getAppState()
    print(appState2.isLoggedIn)
    appState1.isLoggedIn = True

    print(appState1.isLoggedIn)
    print(appState2.isLoggedIn)

# Source: NeetCode