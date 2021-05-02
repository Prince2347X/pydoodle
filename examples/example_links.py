import pydoodle

c = pydoodle.Compiler(clientId="client-id",
                      clientSecret="client-secret") # which you'll get from https://jdoodle.com/compiler-api
result = c.execute(script="https://pastebin.com/vJFXrKX3", language="python3", link=True)  #NOTE: I've set the `link` parameter to True because I'm providing link in script parameter.
print(result.output)

