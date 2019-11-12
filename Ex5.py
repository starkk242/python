formatter = '%r %r %r %r'

print formatter % (1,2,3,4)
print formatter % ("one","two","Three","Four")
print formatter % (formatter,formatter,formatter,formatter)

print formatter % (
  "I has this thing",
  "That you can type up right",
  "But you can sing",
  "So I said gn"
)