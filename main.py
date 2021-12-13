def check_samenum(total_num, num_str):
  num=0
  res = 0
  for i in num_str:
    new_str = num_str[num:]
    num+=1
    for j in range(total_num):
      l_num = total_num-j
      if l_num<=len(new_str):
        main_num = new_str[0:l_num]
        if main_num[0]!=main_num[len(main_num)-1]:
          res+=1
  print(res)

if __name__=="__main__":
  tot_num = int(input("Total num"))
  num_str = input("The Num: ")
  check_samenum(tot_num, num_str)

# Five loops 
# 1. 1 0 2 0 1
# 2. 10 02 20 01
# 3. 102 020 201
# 4. 1020 0201
# 5. 10201 