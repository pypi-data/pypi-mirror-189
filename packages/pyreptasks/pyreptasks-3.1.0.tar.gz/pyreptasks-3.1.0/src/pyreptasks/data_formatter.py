from pyreptasks import Switch

## Definition of the class DataFormatter.
class DataFormatter:
    """
    This class allows to define a specific format for different fields in a direct way. Then, the object is able to convert some data string into the format specified by the fields, as well as to ensure that the data respects the fields constraints, otherwise it will throw an exception.

    An object of type DataFormatter does not need any argument during its declaration, as all the specifications will be done while adding fields and their formats to the object. All the data formatted, regardless of the choosen format, will delete innecesary spaces automatically (example: "   hello     world      " -> "hello world").

    METHODS:

     - add_field: This method allows the user to add a new field and the format it must respect to the object list 'fields'. Check the method description for detailed explanation.

     - delete_field: This method takes a field name as argument and remove the corresponding field from the object list 'fields', if it exists.

     - show_fields: This method returns a list containing the name of each field defined in the formatter.

     - field_format: This method takes the name of a field defined in the formatter as input and returns the format set for this field.

     - single_data_to_format: This method takes two arguments, the data to format and the field of which this data should be part. It returns the formatted data, following the formatting rules stablished by the field.

     - to_format: This method takes a list containing some data as argument. This list must contain one entry for each field defined in the formatter. The method returns a list containing all the formatted data.
    """

    def __init__(self):
        self.__fields = []

    def add_field(
        self,
        name: str,
        style: str = "",
        alphabetic_field: bool = False,
        int_field: bool = False,
        float_field: bool = False,
        alphanumeric_field: bool = False,
        admitted: dict = {},
        required: dict = {},
        length_range: list = [],
        value_range: list = [],
    ):
        """
        This method is used to add a new field and its desired format to the object.

        INPUTS:

        - name: <class 'str'> Contains the name of our field. Example: residence_country.

        - style: <class 'str'> Specification of how data must look. This option is just ignored when the field is numeric, as it does not make sense. The admitted values for this field are:

            - title: The first character of each substring will be a capital letter. The rest will be converted to lower case. Example: hello woRLd -> Hello World

            - capitalize: The first character will be a capital letter, the rest will be converted to lowe case. Example: hello woRLd -> Hello world

            - upper: The whole data will be converted to upper case. Example: hello woRLd -> HELLO WORLD

            - lower: The whole data will be converted to lowe case. Example: hello woRLd -> hello world

            - (empty string): This is the default case. The data will not be converted to any specific style.

        - alphabetic_field: <class 'bool'> Its default value is False. If it is activated, the formatter will ensure that non-alphabetic characters are not present in the data.

        - int_field: <class 'bool'> Its default value is False. If it is activated, the formatter will ensure that the field could be converted into an integer.

        - float_field: <class 'bool'> Its default value is False. If it is activated, the formatter will ensure that the field could be converted into a float number. The formatter will add .0 to the string if an integer is given.

        - alphanumeric_field: <class 'bool'> Its default value is False. If it is activated, the formatter will ensure that non-alphanumeric characters are not present in the data.

        - admitted: <class 'dict'> Only available for alphabetic and alphanumeric fields. Its default value is an empty dict. It should be formed by the single characters that the formatter must skip while checking if the introduced data fits in the field's format specification as keys, and their corresponding values will be the maximum times they are admitted. If there is not limit in the amount of this characters, the value must be True. For example, if the field should be formed by alphabetic characters but admitting spaces, dots,commas and '@' just once. To ensure the data fits this description, it might be done using alphabetic_field = True and admitted = {" ":True,".":True, ",":True, "@":1}

        - required: <class 'dict'> Not available for integer or float fields. Its default value is an empty dict. It may contain as keys:

            - Single character strings: Meaning that this character must be present in the string.

            - Two characters strings: Defining a range of characters, so the formatter checks that the string contains characters inside this range.

            - Tuples of single characters: Defining a set of characters, so the formatter checks that the string contains characters inside this tuple.

        The value of each key stands for the number of times the formatter has to check each key.

        - length_range: <class 'list'> This list contains lower and upper bounds on the data length. The formatter will ensure that the data respect these constraints. If an exact length is required, set both bounds equal to the desired length. The default value is an empty list, meaning that there is not any constraint to apply.

        - value_range: <class 'list'> Only available for integer or float fields. This list contains lower and upper bounds on the data value (only applied for numeric fields). The formatter will ensure that the data respect these constraints. If an exact value is required, set both bounds equal to the desired value. The default value is an empty list, meaning that there is not any constraint to apply.
        """
        ## Ensure that the introduced arguments fit the specifications.
        if name.__class__ != str:
            raise ValueError(
                "the name asigned to the field must be a string but {} given.".format(
                    name.__class__
                )
            )
        style_switch = Switch(
            {
                "title": str.title,
                "capitalize": str.capitalize,
                "upper": str.upper,
                "lower": str.lower,
                "": True,
            },
            use_default_case=True,
            default_case=False,
        )
        if style_switch.exec(style) == False:
            raise ValueError(
                "unrecognized style. Please read the class docs to check the valid styles."
            )
        if alphabetic_field.__class__ != bool:
            raise ValueError(
                "just_letter must be of type bool but {} given.".format(
                    alphabetic_field.__class__
                )
            )
        if int_field.__class__ != bool:
            raise ValueError(
                "int_field must be of type bool but {} given.".format(
                    int_field.__class__
                )
            )
        if float_field.__class__ != bool:
            raise ValueError(
                "float_field must be of type bool but {} given.".format(
                    float_field.__class__
                )
            )
        if alphanumeric_field.__class__ != bool:
            raise ValueError(
                "alphanumeric_field must be of type bool but {} given".format(
                    alphanumeric_field.__class__
                )
            )
        if [alphabetic_field, int_field, float_field, alphanumeric_field].count(
            True
        ) > 1:  ## Check that among these options there is at most one True.
            raise ValueError(
                "a field cannot be simultaneously alphabetic, integer, float and/or alphanumeric."
            )
        if admitted.__class__ != dict:
            raise ValueError(
                "admitted must be of type dict but {} given.".format(admitted.__class__)
            )
        if admitted != {} and not (alphabetic_field or alphanumeric_field):
            raise ValueError(
                "admitted must be an empty dictionary if the field is not declared as alphabetic or alphanumeric."
            )
        if False in [
            admitted_character.__class__ == str and len(admitted_character) == 1
            for admitted_character in admitted.keys()
        ]:
            raise ValueError("admitted keys must be formed by single characters.")
        if False in [
            admitted_value.__class__ == int or admitted_value == True
            for admitted_value in admitted.values()
        ]:
            raise ValueError(
                "admitted values must be integers (if the admitted character is limited to a certain amount) or True (if there is not any restriction)"
            )
        if required.__class__ != dict:
            raise ValueError(
                "required must be of type dict but {} was given.".format(
                    required.__class__
                )
            )
        if required != {} and (int_field or float_field):
            raise ValueError(
                "required must be an empty dict if the field is declared as integer or float."
            )
        if (
            False
            in [
                required_key.__class__ in [str, tuple]
                for required_key in required.keys()
            ]
            or False
            in [
                len(required_character) in [1, 2]
                for required_character in required.keys()
                if required_character.__class__ == str
            ]
            or False
            in [
                all(
                    [element.__class__ == str and len(element) == 1 for element in tupl]
                )
                for tupl in required.keys()
                if tupl.__class__ == tuple
            ]
            or False
            in [
                required_characters[0] <= required_characters[1]
                for required_characters in required.keys()
                if required_characters.__class__ == str
                and len(required_characters) == 2
            ]
        ):
            raise ValueError(
                "required keys must be strings of at most 2 characters or tuples containing single characters. If you provide a two-range string, make sure that the second character is greater than the first one."
            )
        if False in [value.__class__ == int for value in required.values()]:
            raise ValueError("required values must be integers.")
        if length_range.__class__ != list:
            raise ValueError(
                "length_range must be of type list but {} given.".format(
                    length_range.__class__
                )
            )
        if len(length_range) not in [0, 2] or False in [
            item.__class__ == int for item in length_range
        ]:
            raise ValueError(
                "length_range must be kept empty if no range needed. Otherwise introduce the lower and upper bound as integers."
            )
        if value_range.__class__ != list:
            raise ValueError(
                "value_range must be of type list but {} given.".format(
                    value_range.__class__
                )
            )
        if value_range != [] and not (int_field or float_field):
            raise ValueError(
                "value_range must be an empty list except if the field represents a number."
            )
        if len(value_range) not in [0, 2] or False in [
            item.__class__ in [int, float] for item in value_range
        ]:
            raise ValueError(
                "value_range must not be modified if there is not need of bounds in a numeric field. Otherwise introduce the lower and upper bound."
            )
        ## Creation of a new_field dictionary
        new_field = {}
        names = self.show_fields()
        if name in names:  ## Check that the introduced field is not duplicate.
            raise NameError("field already registered.")
        ## Adding parameters to the field...
        new_field["name"] = name
        new_field["alphabetic_field"] = alphabetic_field
        new_field["int_field"] = int_field
        new_field["float_field"] = float_field
        new_field["alphanumeric_field"] = alphanumeric_field
        ## If style, length_range or value_range parameters needed, add them to the field.
        if style_switch.exec(style).__class__ != bool:
            new_field["style"] = style_switch.exec(style)
        if len(admitted.keys()) > 0:
            new_field["admitted"] = admitted
        if len(required.keys()) > 0:
            new_field["required"] = required
        if len(length_range) == 2:
            new_field["length_range"] = length_range
        if len(value_range) == 2:
            new_field["value_range"] = value_range
        self.__fields.append(
            new_field
        )  ## Once the new field is ready, add it to the formatter.

    def delete_field(self, field_name: str):
        """
        This method is used to delete a field from the formatter.

        INPUTS:

        - field_name: <class 'str'> The name of the field to delete from the formatter. It must match one of the defined fields.
        """
        if field_name.__class__ != str:  ## Check that the field_name is well introduced
            raise ValueError(
                "field_name must be a string but {} given.".format(field_name.__class__)
            )
        names = self.show_fields()
        if field_name not in names:  ## Check that the selected field actually exists.
            raise NameError(
                "the field {} is not defined in the formatter. Please use the method 'show_fields' to check the defined methods.".format(
                    field_name
                )
            )
        self.__fields.pop(names.index(field_name))  ## Field deletion

    def show_fields(self):
        """
        This method returns a list with the names of the fields already defined in the formatter.

        OUTPUT:

        - <class 'list'> A list containing the name of the defined fields.
        """
        return [field["name"] for field in self.__fields]

    def field_format(self, field_name: str):
        """
        This method returns the format of the introduced field.

        INPUTS:

        - field_name: <class 'str'>. The name of the field whose format is to be returned.

        OUTPUT:

        <class 'dict'>. A dictionary containing the format of de specified field.
        """
        if field_name.__class__ != str:  ## Check that the field_name is well introduced
            raise ValueError(
                "field_name must be a string but {} given.".format(field_name.__class__)
            )
        names = self.show_fields()
        if field_name not in names:  ## Check that the selected field actually exists.
            raise NameError(
                "the field {} is not defined in the formatter. Please use the method 'show_fields' to check the defined methods.".format(
                    field_name
                )
            )
        return self.__fields[names.index(field_name)]

    def single_data_to_format(self, data: str, field_name: str):
        """
        This method format the introduced data respecting the format specified by the introduced field.

        INPUTS:

        - data: <class 'str'> The string of data to format.

        - field_name: <class 'str'> The name of the field whose format must be applied. It must match one of the defined fields.

        OUTPUT:
        - <class 'str'> The formatted data.
        """
        ## Check that the inputs are correct
        if field_name.__class__ != str:
            raise ValueError(
                "field_name must be a string but {} given.".format(field_name)
            )
        if data.__class__ != str:
            raise ValueError("data must be a string but {} given.".format(data))
        names = self.show_fields()
        if (
            field_name not in names
        ):  ## Check that the introduced field matches one of the defined fields.
            raise NameError(
                "the field {} is not defined in the formatter. Please use the method 'show_fields' to check the defined methods.".format(
                    field_name
                )
            )
        field = self.__fields[names.index(field_name)]
        ## Formatting data........
        if field["alphabetic_field"]:
            return self.__alpha_formatter(field, data)
        elif field["int_field"]:
            return self.__int_formatter(field, data)
        elif field["float_field"]:
            return self.__float_formatter(field, data)
        elif field["alphanumeric_field"]:
            return self.__alphanum_formatter(field, data)
        return self.__default_formatter(field, data)

    def to_format(self, data: list):
        """
        This method apply all the defined formats to a list containing the data to format.

        INPUTS:

        - data: <class 'list'> A list containing an entry for each defined field, the data to be formatted. It is mandatory that its length matches the length of the object list 'fields', as the first field's format will be applied to the first data entry, the second field's format will be applied to the second data entry, and so on.

        OUTPUT:

        - <class 'list'> A list containing all the formatted data. Example: fields = [field1, field2], data = [data_1, data_2] -> returns [field1.format(data_1), field2.format(data_2)]
        """
        ## Check that the introduced data is well-formed.
        if data.__class__ != list:
            raise ValueError(
                "the set of data to format must be a list but {} given.".format(
                    data.__class__
                )
            )
        if len(self.__fields) != len(data):
            raise ValueError(
                "the introduced data is not valid. The reason is likely that the formatter is waiting for a different amount of data, please use the method 'show_fields' to check which fields the formatter is waiting for."
            )
        ## Formatting data........
        for index in range(len(data)):
            if self.__fields[index]["alphabetic_field"]:
                data[index] = self.__alpha_formatter(self.__fields[index], data[index])
            elif self.__fields[index]["int_field"]:
                data[index] = self.__int_formatter(self.__fields[index], data[index])
            elif self.__fields[index]["float_field"]:
                data[index] = self.__float_formatter(self.__fields[index], data[index])
            elif self.__fields[index]["alphanumeric_field"]:
                data[index] = self.__alphanum_formatter(
                    self.__fields[index], data[index]
                )
            else:
                data[index] = self.__default_formatter(
                    self.__fields[index], data[index]
                )
        return data

    ## This private method gives format to the introduced data when it should be formed just by alphabetic characters.
    def __alpha_formatter(self, field, alpha_string: str):
        if (
            alpha_string.__class__ != str
        ):  ## Check that the introduced string is actually a string
            raise ValueError(
                "data to format must be a string but {} is {}.".format(
                    alpha_string, alpha_string.__class__
                )
            )
        alpha_string = self.__string_cleaner(alpha_string)  ## Cleaning the string..
        ## If we receive an empty string and it is admitted by the field format, nothing else to do.
        try:
            if field["length_range"][0] == 0 and len(alpha_string) == 0:
                return alpha_string
        except KeyError:
            pass
        ## Apply the specific format and check the data fits it.
        try:
            pure_string = self.__remove_admitted(
                field["admitted"], alpha_string
            )  ##The string once the admitted characters have been removed
        except KeyError:
            if not alpha_string.isalpha():
                raise ValueError(
                    "non-admitted character introduced in alphabetic field {}.".format(
                        field["name"]
                    )
                )
        else:
            if len(pure_string) == 0:
                raise ValueError(
                    "the introduced data does not contain any alphabetic character in alphabetic field {}.".format(
                        field["name"]
                    )
                )
            if not pure_string.isalpha():
                raise ValueError(
                    "non-admitted character introduced in alphabetic field {}.".format(
                        field["name"]
                    )
                )
        ## Check if the required characters have been included into the input data
        try:
            self.__check_required(field["required"], alpha_string)
        except KeyError:
            pass
        try:
            alpha_string = field["style"](alpha_string)
        except KeyError:
            pass
        try:
            if len(alpha_string) not in range(
                field["length_range"][0], field["length_range"][1] + 1
            ):
                raise ValueError("{} length out of range.".format(field["name"]))
        except KeyError:
            pass
        return alpha_string

    ## This private method gives format to the introduced data when it should represents an integer.
    def __int_formatter(self, field, digit_string: str):
        if (
            digit_string.__class__ != str
        ):  ## Check that the introduced string is actually a string
            raise ValueError(
                "data to format must be a string but {} is {}.".format(
                    digit_string, digit_string.__class__
                )
            )
        digit_string = self.__string_cleaner(
            digit_string
        )  ## Cleaning the string....have been removed
        ## If we receive an empty string and it is admitted by the field format, nothing else to do.
        try:
            if field["length_range"][0] == 0 and len(digit_string) == 0:
                return digit_string
        except KeyError:
            pass
        ## Apply the specific format and check the data fits it.
        try:
            int(digit_string)
        except ValueError:
            raise ValueError(
                "non-integer string introduced in numeric field {}.".format(
                    field["name"]
                )
            )
        try:
            if len(digit_string) not in range(
                field["length_range"][0], field["length_range"][1] + 1
            ):
                raise ValueError("{} length out of range.".format(field["name"]))
        except KeyError:
            pass
        try:
            if int(digit_string) not in range(
                field["value_range"][0], field["value_range"][1] + 1
            ):
                raise ValueError("{} value out of range.".format(field["name"]))
        except KeyError:
            pass
        return digit_string

    ## This private method gives format to the introduced data when it should represents a float number.
    def __float_formatter(self, field, digit_string: str):
        if (
            digit_string.__class__ != str
        ):  ## Check that the introduced string is actually a string
            raise ValueError(
                "data to format must be a string but {} is {}.".format(
                    digit_string, digit_string.__class__
                )
            )
        digit_string = self.__string_cleaner(digit_string)  ## Cleaning the string....
        ## If we receive an empty string and it is admitted by the field format, nothing else to do.
        try:
            if field["length_range"][0] == 0 and len(digit_string) == 0:
                return digit_string
        except KeyError:
            pass
        ## Apply the specific format and check the data fits it.
        if (
            digit_string.count(".") == 0
        ):  ## The string represent a float, so it needs a .
            digit_string += ".0"
        try:
            float(digit_string)
        except ValueError:
            raise ValueError(
                "non-float string introduced in float field {}.".format(field["name"])
            )
        try:
            if len(digit_string) not in range(
                field["length_range"][0], field["length_range"][1] + 1
            ):
                raise ValueError("{} length out of range.".format(field["name"]))
        except KeyError:
            pass
        try:
            if (
                float(digit_string) < field["value_range"][0]
                or float(digit_string) > field["value_range"][1]
            ):
                raise ValueError("{} value out of range.".format(field["name"]))
        except KeyError:
            pass
        return digit_string

    ## This private method gives format to the introduced data when it should be formed just by alphanumeric characters.
    def __alphanum_formatter(self, field, alphanum_string: str):
        if (
            alphanum_string.__class__ != str
        ):  ## Check that the introduced string is actually a string
            raise ValueError(
                "data to format must be a string but {} is {}.".format(
                    alphanum_string, alphanum_string.__class__
                )
            )
        alphanum_string = self.__string_cleaner(
            alphanum_string
        )  ## Cleaning the string...
        ## If we receive an empty string and it is admitted by the field format, nothing else to do.
        try:
            if field["length_range"][0] == 0 and len(alphanum_string) == 0:
                return alphanum_string
        except KeyError:
            pass
        ## Apply the specific format and check the data fits it.
        try:
            pure_string = self.__remove_admitted(
                field["admitted"], alphanum_string
            )  ##The string once the admitted characters have been removed
        except KeyError:
            if not alphanum_string.isalnum():
                raise ValueError(
                    "non-admitted character introduced in alphanumeric field {}.".format(
                        field["name"]
                    )
                )
        else:
            if len(pure_string) == 0:
                raise ValueError(
                    "the introduced data does not contain any alphanumeric character in alphanumeric field {}.".format(
                        field["name"]
                    )
                )
            if not pure_string.isalnum():
                raise ValueError(
                    "non-admitted character introduced in alphanumeric field {}.".format(
                        field["name"]
                    )
                )
        ## Check if the required characters have been included into the input data
        try:
            self.__check_required(field["required"], alphanum_string)
        except KeyError:
            pass
        try:
            alphanum_string = field["style"](alphanum_string)
        except KeyError:
            pass
        try:
            if len(alphanum_string) not in range(
                field["length_range"][0], field["length_range"][1] + 1
            ):
                raise ValueError("{} length out of range.".format(field["name"]))
        except KeyError:
            pass
        return alphanum_string

    ## This private method gives format to the introduced data if none of the other private formatters is applied.
    def __default_formatter(self, field, string: str):
        if (
            string.__class__ != str
        ):  ## Check that the introduced string is actually a string
            raise ValueError("data to format must be a string.")
        string = self.__string_cleaner(string)  ## Cleaning the string....
        ## Apply the specific format and check the data fits it.
        try:
            string = field["style"](string)
        except KeyError:
            pass
        ## Check if the required characters have been included into the input data
        try:
            self.__check_required(field["required"], string)
        except KeyError:
            pass
        try:
            if len(string) not in range(
                field["length_range"][0], field["length_range"][1] + 1
            ):
                raise ValueError("{} length out of range.".format(field["name"]))
        except KeyError:
            pass
        return string

    ## This private method removes admitted characters from the introduced data in order to check that the rest of the string fits the requirements. Also it ensures that the data does not exceed the amount of these admitted characters
    def __remove_admitted(self, admitted: dict, data: str):
        for admitted_character in admitted.keys():
            if (
                admitted[admitted_character].__class__ == int
                and data.count(admitted_character) > admitted[admitted_character]
            ):
                raise ValueError(
                    "the introduced data {} may contain at most {} {}, but it contains {}.".format(
                        data,
                        admitted[admitted_character],
                        admitted_character,
                        data.count(admitted_character),
                    )
                )
            data = "".join(data.split(admitted_character))
        return data

    ## This private method checks that the introduced data contains all the required characters.
    def __check_required(self, required: dict, data: str):
        required_switch = Switch({str: self.__check_string, tuple: self.__check_tuple})
        for required_key in required.keys():
            required_switch.exec(required_key.__class__)(
                required_key, required[required_key], data
            )

    ## Submethod of __check_required to use when the key is a string
    def __check_string(self, required_key: str, required_value: int, data: str):
        if len(required_key) == 1 and data.count(required_key) < required_value:
            raise ValueError(
                "the introduced data {} must contain the character {} at least {} times.".format(
                    data, required_key, required_value
                )
            )
        elif (
            len(required_key) == 2
            and [
                True if required_key[0] <= character <= required_key[1] else False
                for character in data
            ].count(True)
            < required_value
        ):
            raise ValueError(
                "the introduced data {} must contain characters in the range {}-{} at least {} times.".format(
                    data, required_key[0], required_key[1], required_value
                )
            )

    ## Submethod of __check_required to use when the key is a tuple
    def __check_tuple(self, required_key: tuple, required_value: int, data: str):
        if sum([data.count(character) for character in required_key]) < required_value:
            raise ValueError(
                "the introduced data {} must contain characters from the set {} at least {} times.".format(
                    data, required_key, required_value
                )
            )

    ## This private method "cleans" a string, deleting unnecessary spaces that must have been included by error.
    def __string_cleaner(self, string):
        return " ".join(string.split())
