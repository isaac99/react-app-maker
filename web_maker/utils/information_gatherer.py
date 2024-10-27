import prompts

class WebAppInformation():
    def __init__(self):
        self.name = None
        self.description = None
        self.author = None
        self.version = None
        self.license = None
        self.keywords = None
        self.homepage = None
        self.repository = None
        self.bugs = None
        self.dependencies = None
        self.devDependencies = None
        self.scripts = None
        self.main = None
        self.module = None
        self.bin = None
        self.types = None
        self.files = None

    def get_filenames(self):
        return self.files
    
    def set_filenames(self, files):
        self.files = files