from django.forms import widgets


class InputMixin:
    template_name = "pretty/widgets/input.html"

    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {"class" : "input"}
        else:
            if "class" in attrs:
                attrs["class"] = "input" + " " + attrs["class"]
            else:
                attrs["class"] = "input" 
        super().__init__(attrs=attrs)


class CheckboxMixin:
    template_name = "pretty/widgets/checkbox.html"

    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {"class" : "checkbox"}
        else:
            if "class" in attrs:
                attrs["class"] = "checkbox" + " " + attrs["class"]
            else:
                attrs["class"] = "checkbox" 
        super().__init__(attrs=attrs)


class CheckboxInput(CheckboxMixin, widgets.CheckboxInput):
    template_name = "pretty/widgets/checkbox.html"


class TextInput(InputMixin, widgets.TextInput):
    template_name = "pretty/widgets/input.html"


class NumberInput(InputMixin, widgets.NumberInput):
    template_name = "pretty/widgets/number.html"


class EmailInput(InputMixin, widgets.EmailInput):
    template_name = "pretty/widgets/email.html"


class URLInput(InputMixin, widgets.URLInput):
    template_name = "pretty/widgets/url.html"


class PasswordInput(InputMixin, widgets.PasswordInput):
    template_name = "pretty/widgets/password.html"


class HiddenInput(InputMixin, widgets.HiddenInput):
    template_name = "pretty/widgets/hidden.html"


class MultipleHiddenInput(HiddenInput, widgets.HiddenInput):
    template_name = "pretty/widgets/hidden.html"


class FileInput(InputMixin, widgets.FileInput):
    template_name = "pretty/widgets/file.html"


class ClearableFileInput(InputMixin, widgets.ClearableFileInput):
    template_name = "pretty/widgets/file.html"


class Textarea(widgets.Textarea):
    template_name = "pretty/widgets/textarea.html"

    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {"class" : "textarea"}
        else:
            if "class" in attrs:
                attrs["class"] = "textarea" + " " + attrs["class"]
            else:
                attrs["class"] = "textarea" 
        super().__init__(attrs=attrs)



class DateTimeBaseInput(InputMixin, widgets.TextInput):
    pass


class DateInput(DateTimeBaseInput, widgets.DateInput):
    pass


class DateTimeInput(DateTimeBaseInput, widgets.DateTimeInput):
    pass


class TimeInput(DateTimeBaseInput, widgets.TimeInput):
    pass


class Select(widgets.Select):
    template_name = "pretty/widgets/select.html"
    option_template_name = "pretty/widgets/select_option.html"


class SelectMultiple(widgets.SelectMultiple):
    template_name = "pretty/widgets/select_multiple.html"
    option_template_name = "pretty/widgets/select_option.html"


class RadioSelect(widgets.RadioSelect):
    template_name = "pretty/widgets/radio.html"
    option_template_name = "pretty/widgets/radio_option.html"


class CheckboxSelectMultiple(widgets.CheckboxSelectMultiple):
    template_name = "pretty/widgets/checkbox_select.html"
    option_template_name = "pretty/widgets/checkbox_option.html"


class MultiWidget(widgets.MultiWidget):
    template_name = "pretty/widgets/multiwidget.html"
    

class SplitDateTimeWidget(widgets.SplitDateTimeWidget):
    template_name = "pretty/widgets/splitdatetime.html"


class SplitHiddenDateTimeWidget(widgets.SplitHiddenDateTimeWidget):
    template_name = "pretty/widgets/splithiddendatetime.html"


class SelectDateWidget(widgets.SelectDateWidget):
    template_name = "pretty/widgets/select_date.html"
