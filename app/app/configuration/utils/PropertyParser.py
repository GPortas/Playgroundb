import ast
import configparser
import re


class PropertyParser:
    PROPERTY_STRING = 'string'
    PROPERTY_BOOLEAN = 'boolean'
    PROPERTY_ARRAY = 'array'
    PROPERTY_OBJECT = 'object'

    __instance = None

    def __init__(self, path, conf=None):
        if conf:
            self.__configParser = conf
        else:
            self.__configParser = configparser.RawConfigParser()
            self.__configParser.read(path)

    @staticmethod
    def getInstance(path):
        if PropertyParser.__instance is None:
            PropertyParser.__instance = PropertyParser(path)
        return PropertyParser.__instance

    def getStringProperty(self, section, property):
        return self.__innerGet(section, property, self.__configParser.get)

    def getArrayProperty(self, section, property):
        return self.__getPythonStructuredProperty(section, property, '[', ']', self.PROPERTY_ARRAY)

    def getBooleanProperty(self, section, property):
        try:
            value = self.__innerGet(section, property, self.__configParser.getboolean)
            return value
        except:
            self.__raiseInvalidPropertyFormatException(section=section, property=property, type=self.PROPERTY_BOOLEAN)

    def getObjectProperty(self, section, property):
        return self.__getPythonStructuredProperty(section, property, '{', '}', self.PROPERTY_OBJECT)

    def __innerGet(self, section, property, callback):
        try:
            return callback(section, property)
        except configparser.NoOptionError as noe:
            self.__raiseNotExistPropertyException(property, section)
        except configparser.NoSectionError as nse:
            raise ValueError('Section "' + section + '" doesn\'t exist')

    def __getPythonStructuredProperty(self, section, property, startswithstr, endswithstr, property_type):
        try:
            innerResult = self.__innerGet(section, property, self.__configParser.get)
            innerResult = self.__removeStringWhitespaces(innerResult)
            self.__validateStringStartAndEnd(innerResult, startswithstr, endswithstr)
            result = self.__parseStringPythonExpression(expression=innerResult)
        except ValueError:
            self.__raiseInvalidPropertyFormatException(section=section, property=property, type=property_type)
        return result

    def __removeStringWhitespaces(self, string):
        self.__validateStringValue(string)
        return re.sub('[\s+]', '', string)

    def __validateStringValue(self, str_to_test):
        if str_to_test is None or not isinstance(str_to_test, str):
            raise ValueError('Value ' + str(str_to_test) + ' is not a valid string')

    def __validateStringStartAndEnd(self, string, startswithstr, endswithstr):
        self.__validateStringValue(string)
        if string is None or not string.startswith(startswithstr) or not string.endswith(endswithstr):
            raise ValueError(
                'String ' + string + ' doesn\'t start with ' + startswithstr + ' and doesn\'t end with ' + endswithstr)

    def __parseStringPythonExpression(self, expression):
        try:
            self.__validateStringValue(expression)
            # We're using 'literal_eval' because 'eval' also evaluates the Python expression and that may be a security risk
            result = ast.literal_eval(expression)
        except SyntaxError:
            self.__raiseInvalidPythonExpressionException(expression=expression)
        except ValueError:
            self.__raiseInvalidPythonExpressionException(expression=expression)
        return result

    def __raiseInvalidPythonExpressionException(self, expression):
        raise ValueError('Value "' + expression + '" is not a valid Python expression')

    def __raiseInvalidPropertyFormatException(self, section, property, type):
        raise ValueError('Value "' + property + '" from section "' + section + '" is not in ' + type + ' format')

    def __raiseNotExistPropertyException(self, property, section):
        raise ValueError('Property "' + property + '" from section "' + section + '" doesn\'t exist')
