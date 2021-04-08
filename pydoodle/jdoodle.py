import requests
from .errors import UnauthorizedRequest, BadRequest, LanguageNotSupported


class Output:
    def __init__(self, output, statusCode, memory, cpuTime):
        self.output = output
        self.statusCode = statusCode
        self.memory = memory
        self.cpuTime = cpuTime


class Compiler:
    """
    Initialize the compiler which let you access the Jdoodle API.

    Parameters
    ------------
    clientId: str
        The clientId to access the API which you can get from https://jdoodle.com/compiler-api
    clientSecret: str
        The clientSecret which you can get from https://jdoodle.com/compiler-api
    """
    def __init__(self, clientId: str, clientSecret: str):
        if not isinstance(clientId, str):
            raise TypeError
        elif not isinstance(clientSecret, str):
            raise TypeError
        self.clientID = clientId
        self.clientSecret = clientSecret
        self.headers = {'Content-Type': 'application/json; charset=UTF-8', }
        self.base_url = "https://api.jdoodle.com/v1/execute"
        self.usage_url = "https://api.jdoodle.com/v1/credit-spent"
        self.languages = ['ada', 'bash', 'bc', 'brainfuck', 'c', 'c-99', 'clisp', 'clojure', 'cobol', 'coffeescript',
                          'cpp', 'cpp17', 'csharp', 'd', 'dart', 'elixir', 'erlang', 'factor', 'falcon', 'fantom',
                          'forth', 'fortran', 'freebasic', 'fsharp', 'gccasm', 'go', 'groovy', 'hack', 'haskell',
                          'icon', 'intercal', 'java', 'jlang', 'kotlin', 'lolcode', 'lua', 'mozart', 'nasm', 'nemerle',
                          'nim', 'nodejs', 'objc', 'ocaml', 'octave', 'pascal', 'perl', 'php', 'picolisp', 'pike',
                          'prolog', 'python2', 'python3', 'r', 'racket', 'rhino', 'ruby', 'rust', 'scala', 'scheme',
                          'smalltalk', 'spidermonkey', 'sql', 'swift', 'tcl', 'unlambda', 'vbn', 'verilog',
                          'whitespace', 'yabasic']
        self.json = {}

    def execute(self, script: str, language: str, stdIn: str = None, versionIndex: int = None) -> Output:

        """
        Executes the provided script.

        Parameters
        -----------
        script: str
            The script to be executed.
        language: str
            Language of the script. See available languages here_.
        stdIn: str, optional
            stdIn of the script (If any), Defaults to ``None``. In case of multiple inputs, they should be separated by '\n'
        versionIndex: int, optional
            versionIndex of compiler representing the version. Defaults to ``0``. Check versionIndex representing the version here_.

        Returns
        -------
        Output
            An output object with all of it's attributes.

        Raises
        -------
        UnauthorizedRequest
            Raised if either your clientID or clientSecret is invalid.
        LanguageNotSupported
            Raised if wrong language code is provided.
        BadRequest
            Raised when invalid language or versionIndex is provided.

        """
        if not isinstance(script, str):
            raise TypeError
        elif language not in self.languages:
            raise LanguageNotSupported(
                f"{language} language isn't supported by jdoodle.com yet, or maybe you mis-spelled it.\n"
                f"List of supported languages: {self.languages}")
        if versionIndex is not None:
            if not isinstance(versionIndex, int):
                raise TypeError
        else:
            versionIndex = 0

        self.json = {"clientId": self.clientID,
                     "clientSecret": self.clientSecret,
                     "script": f"""{script}""",
                     "language": f"{language}",
                     "versionIndex": str(versionIndex)
                     }
        if stdIn is not None:
            if not isinstance(stdIn, str):
                raise TypeError
            else:
                self.json["stdin"] = stdIn
        response = requests.post(url=self.base_url, headers=self.headers, json=self.json)
        response_json = response.json()
        if response.status_code == 200:
            return Output(output=response_json['output'],
                          statusCode=response_json['statusCode'],
                          memory=response_json['memory'],
                          cpuTime=response_json['cpuTime'])
        else:
            error = response.json()
            if response.status_code == 401:
                raise UnauthorizedRequest(f"statusCode: {error['statusCode']}, error: {error['error']}\n"
                                          f"Either your clientID or clientSecret is invalid.")
            elif response.status_code == 400:
                raise BadRequest(f"statusCode: {error['statusCode']}, error: {error['error']}\n"
                                 f"Invalid versionIndex or language provided.")

    def usage(self) -> int:
        """
        Tells the number of credits spent today.
        """
        json = {"clientId": self.clientID, "clientSecret": self.clientSecret}
        response = requests.post(url=self.usage_url, json=json)
        if response.status_code == 200:
            return response.json()['used']
        elif response.status_code == 401:
            raise UnauthorizedRequest(
                f"statusCode: {response.json()['statusCode']}, error: {response.json()['error']}\n"
                f"Either your clientID or clientSecret is invalid.")
