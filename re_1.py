#-*- coding: utf-8 -*
import re
content = 'Hello 1234356 is a number. Regex String'
#result = re.match('^Hello (\d+).*String$',content)
#result = re.match('.*(\d+).*',content)
result = re.match('.*?(\d+).*',content)
if result:
    print(result.group(1))

