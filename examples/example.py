import pydoodle

c = pydoodle.Compiler(clientId="client-id",
                      clientSecret="client-secret")
with open(file="test1.py") as f:
    script = f.read()
    f.close()
result = c.execute(script=script, language="python3")
usage = c.usage()
print(usage, result.output, sep='\n')
