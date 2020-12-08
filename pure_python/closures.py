
def html_tag(tag):
    def wrap_text(text):
        return '<' + tag + '>' + text + '</' + tag + '>'

    return wrap_text

wrap_h1 = html_tag('h1')
print(wrap_h1('Big heading'))

wrap_h6 = html_tag('h6')
print(wrap_h6('Small heading'))
