def data_type(var):
  if type(var)is str:
    return len(var)
  elif var is None:
    return 'no value'
  elif type(var) is bool:
    return var
  elif isinstance(var,(int,long))==True:
    if var<100:
      return 'less than 100'
    elif var>100:
      return 'more than 100'
    else:
      return 'equal to 100'
      
  elif type(var) is list:
    if len(var)>2:
      return var[2]
    else :
      return None

  else:
    return "variable not int, str,None,list"
      
