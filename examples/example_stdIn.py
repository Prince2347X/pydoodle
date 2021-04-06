from pydoodle.jdoodle import Compiler

c = Compiler(clientId="client-id",
             clientSecret="client-secret")
with open(file="test2.py") as f:
    script = f.read()
    f.close()
output = c.execute(script=script, language="python3", stdIn="Hello World!")
print(output)
