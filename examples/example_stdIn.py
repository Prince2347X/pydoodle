import pydoodle

c = pydoodle.Compiler(clientId="client-id",
             clientSecret="client-secret")
with open(file="test2.py") as f:
    script = f.read()
    f.close()
result = c.execute(script=script, language="python3", stdIn="Hello World!")
print(result.output)
