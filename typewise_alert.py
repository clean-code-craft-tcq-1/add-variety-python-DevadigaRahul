coolingType_temperature_range={
  'PASSIVE_COOLING':{'lowerLimit':0, 'upperLimit':35},
  'MED_ACTIVE_COOLING':{'lowerLimit':0, 'upperLimit':40},
  'HI_ACTIVE_COOLING':{'lowerLimit':0, 'upperLimit':45}
  }

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'

def classify_temperature_breach(coolingType, temperatureInC):
  temperature_range=coolingType_temperature_range.get(coolingType)
  if(temperature_range!=None):
    return infer_breach(temperatureInC, temperature_range['lowerLimit'], temperature_range['upperLimit'])


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  if(breachType!=None):
    #message_to_target[alertTarget](breachType)
    return message_to_target[alertTarget](breachType) #Mocking and validation purpose

def send_to_console(breachType):#mocking console and verify Input received to console
  header = 'Console:'
  print(f'{header}, {breachType}')
  return breachType

def send_to_controller(breachType):#mocking console and verify Input received to controller
  header = 0xfeed
  print(f'{header}, {breachType}')
  return breachType

def send_to_email(breachType):#mocking console and verify Input received to email
  frame_mail_to_print(breachType)
  return breachType

def frame_mail_to_print(breachType):
  recepient = "a.b@c.com"
  text_msg={
    'TOO_LOW':'too low',
    'TOO_HIGH':'too high'
    }
  def print_mail(message):
    if(message!=None):
      print(f'To: {recepient}')
      print(f'Hi, the temperature is {message}')
  return print_mail(text_msg.get(breachType))

message_to_target={
  'to_console':send_to_console,
  'to_controller':send_to_controller,
  'to_email':send_to_email
  }
