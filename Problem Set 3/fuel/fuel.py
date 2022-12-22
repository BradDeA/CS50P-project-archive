def main():
  x = percent()
  print(x)


def percent():
  while True:
    try:
      #prompt for fraction
      f = input('Fraction: ')
      s = f.split('/')
      #convert fraction to percent value & round number
      p = round(int(s[0]) / int(s[1]) * 100)
      if p > 100:
        pass
      #if 1% or less remains output E
      elif p == 0 or p == 1:
        return 'E'
      #if there is 99% or more output F
      elif p == 99 or p == 100:
        return 'F'
      #else output % left
      else:
        return f'{p}%'
      #ValueError & ZeroDivisionError catch
    except ValueError:
      print('Not a fraction')
    except ZeroDivisionError:
      print('Invalid fraction')

main()
