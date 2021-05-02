import requests
from .errors import UnauthorizedRequest, BadRequest, LanguageNotSupported, LinkNotSupported


class Output:
    """
    The output of the executed script.
    """

    def __init__(self, output, statusCode, memory, cpuTime):
        self.output = output
        self.statusCode = statusCode
        self.memory = memory
        self.cpuTime = cpuTime


class Compiler:
    """
    Initialize the compiler which let you access the Jdoodle API.

    :param clientId: The clientId which you can get from https://jdoodle.com/compiler-api/
    :type clientId: str
    :param clientSecret: The clientSecret which you can get from https://jdoodle.com/compiler-api/
    :type clientSecret: str
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

    def _get_raw_link(self, link: str) -> str:
        if "pastebin" in link or "hastebin" in link:
            return f"{link[:link.find('.com')]}.com/raw{link[link.rfind('/'):]}"
        elif "textbin" in link:
            return f"{link[:link.find('.net')]}.net/raw{link[link.rfind('/'):]}"
        elif "pastie" in link:
            return f"{link}/raw"
        else:
            raise LinkNotSupported("Not able to fetch script.")

    def _read_link(self, link: str) -> str:
        raw_link = self._get_raw_link(link)
        r = requests.get(raw_link)
        return r.text

    def execute(self, script: str, language: str, link: bool = False, stdIn: str = None, versionIndex: int = None) -> Output:

        """
        Executes the provided script.

        :parameter script: The script to be executed. You can provide link of any code hosting site such as pastebin, hastebin, etc. (You've to set `link` parameter to `True`)
        :type script: str
        :parameter language: Language of the script.
        :type language: str
        :parameter link: Tell if a link of any code hosting site(like pastebin, hastebin, etc..) is provided in script parameter. Defaults to `False`. If `True` it takes the script as link and fetch the script from the link.
        :type link: bool
        :parameter stdIn: StdIn of script (If Any), defaults to `None`. In case of multiple inputs, they should be separated by `||` (double pipe).
        :type stdIn: str, optional
        :parameter versionIndex: Version Index of language, defaults to `0`.
        :type versionIndex: int, optional

        :returns: Returns an Output object with all it's attributes.
        :rtype: Output

        :raises: :class:`UnauthorizedRequest`: Raised if either your clientID or clientSecret is invalid.
        :raises: :class:`LanguageNotSupported`: Raised if wrong language code is provided.
        :raises: :class:`BadRequest`: Raised when invalid language or versionIndex is provided.
        :raises: :class:`LinkNotSupported`: Raised if the provided link isn't supported yet by pydoodle.

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
        link = True if script.startswith("https://") else link
        if link is not False:
            script = self._read_link(script)

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
                self.json["stdin"] = stdIn.replace("||", "\n")
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

        :returns: The number of credit spent(number of API calls) today.
        :rtype: int
        """
        json = {"clientId": self.clientID, "clientSecret": self.clientSecret}
        response = requests.post(url=self.usage_url, json=json)
        if response.status_code == 200:
            return response.json()['used']
        elif response.status_code == 401:
            raise UnauthorizedRequest(
                f"statusCode: {response.json()['statusCode']}, error: {response.json()['error']}\n"
                f"Either your clientID or clientSecret is invalid.")
