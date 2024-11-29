from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter

code = '''
def hello_world():
    print("Hello, world!")
'''

with open('code.png', 'wb') as f:
    f.write(highlight(code, PythonLexer(), ImageFormatter(font_name='Courier New')))
