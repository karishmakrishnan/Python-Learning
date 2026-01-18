# shallow copy and deepcopy
import copy

original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copied_list = copy.copy(original_list)
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)
# Modify the original list
original_list[0][0] = 'X'
print("After Modification:")
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)

original_list=[[1,2,3],[4,5,6]]
deep_copied_list=copy.deepcopy(original_list)
print("OriginalList:",original_list)
print("DeepCopiedList:",deep_copied_list)
#Modifytheoriginallist
original_list[0][0]='X'
print("AfterModification:")
print("OriginalList:",original_list)
print("DeepCopiedList:",deep_copied_list)