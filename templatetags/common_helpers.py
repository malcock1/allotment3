from django.template.defaulttags import register

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)

@register.filter
def trunc_chars(string,i):
	return string[:i]