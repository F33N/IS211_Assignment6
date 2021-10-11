def convertCelsiusToKelvin(data):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    return (data + 273.15)

def convertCelsiusToFarenheit(data):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Farenheit"""
    result=round((data * 9/5) + 32,2)
    return(result)

def convertFarenheitToCelsius(data):
    """Takes in a float representing a Farenheit measurement, and returns that temperature converted into Celsius"""
    return round((data - 32) * 5/9,2)

def convertFarenheitToKelvin(data):
    """Takes in a float representing a Farenheit measurement, and returns that temperature converted into Kelvin"""
    return round((data + 459.67)  * 5/9,2)

def convertKelvinToCelsius(data):
    """Takes in a float representing a Farenheit measurement, and returns that temperature converted into Celsius"""
    return round((data - 273.15),2)

def convertKelvinToFarenheit(data):
    """Takes in a float representing a Farenheit measurement, and returns that temperature converted into Kelvin"""
    return round((data * 9/5) - 459.67,2)