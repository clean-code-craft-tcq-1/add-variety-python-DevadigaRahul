individual_temperature_range={
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
  temperature_range=individual_temperature_range[coolingType]
  return infer_breach(temperatureInC, temperature_range['lowerLimit'], temperature_range['upperLimit'])

def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  message_target[alertTarget](breachType)

def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')
  
   
def send_to_email(breachType):
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

message_target={
  'to_console':send_to_controller,
  'to_email':send_to_email
  }
