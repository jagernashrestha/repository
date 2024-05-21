num = [10, 20, 30, 40,50,80]
for i in num:
    if i == 50:
        print(f'The loop has been break with value{i}')
        break
    else:
        print("running loop.")
    print('Outside the for loop.')
