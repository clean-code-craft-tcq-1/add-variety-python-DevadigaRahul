import unittest
import typewise_alert

class TypewiseTest(unittest.TestCase):
  
  def test_infers_breach_for_TOO_LOW_min_minus_one(self):#(min-1)<(min)
    self.assertTrue(typewise_alert.infer_breach(19, 20, 30) == 'TOO_LOW')
    
  def test_infers_breach_for_TOO_HIGH_max_plus_one(self):#(max)<(max+1)
    self.assertTrue(typewise_alert.infer_breach(31, 20, 30) == 'TOO_HIGH')
    
  def test_infers_breach_for_NORMAL_min_plus_one(self):#(min+1)>(min)
    self.assertTrue(typewise_alert.infer_breach(21, 20, 30) == 'NORMAL')
    
  def test_infers_breach_for_NORMAL_max_minus_one(self):#(max-1)<(max)
    self.assertTrue(typewise_alert.infer_breach(29, 20, 30) == 'NORMAL')
  
  def test_check_and_alert_to_controller(self):
    batteryChar1={
    'coolingType':'PASSIVE_COOLING'
    }
    self.assertEqual(typewise_alert.check_and_alert('to_console', batteryChar1, 1),None)

  def test_check_and_alert_to_email_if_too_high(self):#Positive case:Not none
    batteryChar2={
    'coolingType':'MED_ACTIVE_COOLING'
    }
    self.assertEqual(typewise_alert.check_and_alert('to_email', batteryChar2, 41),None)
    
  def test_check_and_alert_to_email_if_too_low(self):#Positive case:Not none
    batteryChar2={
    'coolingType':'MED_ACTIVE_COOLING'
    }
    self.assertEqual(typewise_alert.check_and_alert('to_email', batteryChar2, -1),None)
    
  def test_check_and_alert_not_to_email_if_normal(self):#Positive case:Not none
    batteryChar3={
    'coolingType':'HI_ACTIVE_COOLING'
    }
    self.assertEqual(typewise_alert.check_and_alert('to_email', batteryChar3, 44),None)

if __name__ == '__main__':
  unittest.main()
