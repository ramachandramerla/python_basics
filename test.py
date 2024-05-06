def avg_marks(marks):
    sum_marks=sum(marks)
    print(sum_marks)
    total_marks=len(marks)
    print(total_marks)
    avg= sum_marks / total_marks
    return avg

marks=[10,20,30,40,50]

result=avg_marks(marks)

print(result)