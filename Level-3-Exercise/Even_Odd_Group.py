# group the even and odd integer from group

nums = [1,2,3,4,5,6,7,8]
even_odd = {
    "even": [],
    "odd": []
}
for x in nums:
    if(x % 2 == 0):
        even_odd["even"].append(x)
    else:
        even_odd["odd"].append(x)
print("The even and odd group: ",even_odd)
