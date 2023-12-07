for _ in range(int(input())):
  s = input()
  ans = "CODETOWN"

  vowel = 'AEIOU'
  
  if s == ans:
    print("YES")
  elif s[0] in vowel or s[2] in vowel or s[4] in vowel or s[6] in vowel or s[7] in vowel:
    print("NO")
  elif s[1] in vowel and s[3] in vowel and s[5] in vowel:
    if s[0] is not vowel and s[2] is not vowel and s[4] is not vowel and s[6] is not vowel and s[7] is not vowel:
      print("YES")
    else:
      print("NO")
  else:
    print("NO")
 
      
      
    
    
    