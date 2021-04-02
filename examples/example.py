import pydoodle

c = pydoodle.Compiler(clientId="client-id",
                      clientSecret="client-secret")
with open(file="examples/test.cpp") as f:
    script = f.read()
    f.close()
output = c.execute(script=script, language="cpp")
usage = c.usage()
print(usage, output, sep='\n')