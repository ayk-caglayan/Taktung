#written by Aykut Caglayan 2021

# a range which runs on floating steps
def my_range(a,b,step):
    ruler=[a]
    start=a
    stop=b
    while a<=b:
        a+=step
        ruler.append(round(a, 3))
    return ruler

#replaces x with y in the list a
def replace(a, x, y): 
    for ind, ele in enumerate(a):
        if ele==x:
            a[ind]=y
    return a
        

# quantizes a number to a step
def quantize(x, step):
    board=my_range(int(x), int(x)+1, step)
    return min(board, key=lambda y: abs(y-x))

#quantize list 
def quantize_list(liste, step_size=0.25):
    out=[]
    for i in liste:
        out.append(quantize(i, step_size))
    out=replace(out, 0, step_size) #prohibits 0 as dur value, rather puts the smallest step value 
    return out
    


# flattens sub-arrays, depth 1.
def concatenate(list_of_lists):
    out=[]
    for l in list_of_lists:
        for r in l:
            out.append(r)
    return out


#repack a list of numbers(durations) into sub-arrays of given sum
def reframe(a, summe=3):
    main_out=[]
    out=[]
    counter=0
    for i in a:
        out.append(i)
        if sum(out)>=summe:
            main_out.append(out)
            if not counter==len(a)-1: #when it's last element, keep it to append
                out=[]
            else:
                pass
        if counter==len(a)-1: #this to append the uncompleted rest into the array
            if sum(out)<2 and sum(main_out[len(main_out)-1])<=4: #if shorter than two beats append it to the last frame
                out=concatenate([main_out[len(main_out)-1], out])
                main_out[len(main_out)-1]=out
            else: #if longer than 2 beats pack it as a seperate frame
                main_out.append(out)
        counter+=1
    return main_out
            
#interprets and returns given sub-arrays as time signatures
def sechszehntelORachtelORviertel(ref_out):
    out=[]
    for bar in ref_out:
        print(bar, sum(bar))
        if sum(bar)%1==0:
            out.append(str(int(sum(bar)*1))+'/'+str(4))
        elif sum(bar)%0.5==0:
            out.append(str(int(sum(bar)*2))+'/'+str(8))
        elif sum(bar)%0.25==0:
            out.append(str(int(sum(bar)*4))+'/'+str(16))
    return out

# run this to quantize numbers, pack them into bars and get time signatures
def Taktung(numbers, quantize=0.25):
    return sechszehntelORachtelORviertel(reframe(quantize_list(numbers)))

Taktung([1,2,0.5,0.5, 0.7, 0.2, 0.5,1])