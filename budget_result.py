import os
import csv

# Define PyBank's variables
Month = []
Change_Profit_Loss = []

MonthCount = 0
Profit_Loss_Net = 0
PrevMonth_Profit_Loss = 0
CrntMonth_Profit_loss = 0
Profit_loss_change = 0

LoadPath = os.path.join("budget_data.csv")

with open(LoadPath, newline="") as csvfile:

    Reader = csv.reader(csvfile, delimiter=",")
    Header = next(csvfile)

    for row in Reader:

        MonthCount += 1
        CrntMonth_Profit_loss = int(row[1])
        Profit_Loss_Net += CrntMonth_Profit_loss

        if (MonthCount == 1):
            PrevMonth_Profit_Loss = CrntMonth_Profit_loss
            continue

        else:

            Profit_loss_change = CrntMonth_Profit_loss - PrevMonth_Profit_Loss
            Month.append(row[0])
            Change_Profit_Loss.append(Profit_loss_change)
            PrevMonth_Profit_Loss = CrntMonth_Profit_loss

    sum_Profit_loss = sum(Change_Profit_Loss)
    average_Profit_loss = round(sum_Profit_loss/(MonthCount - 1), 2)
    highest_change = max(Change_Profit_Loss)
    lowest_change = min(Change_Profit_Loss)
    highest_Month_index = Change_Profit_Loss.index(highest_change)
    lowest_Month_index = Change_Profit_Loss.index(lowest_change)
    best_Month = Month[highest_Month_index]
    worst_Month = Month[lowest_Month_index]
print("Financial Analysis")
print("----------------------------")
print(f"Total Month:  {MonthCount}")
print(f"Total:  ${Profit_Loss_Net}")
print(f"Average Change:  ${average_Profit_loss}")
print(f"Greatest Increase in Profits:  {best_Month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_Month} (${lowest_change})")

tosave_path = os.path.join("budget_data.txt")
with open(tosave_path, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Month:  {MonthCount}\n")
    outfile.write(f"Total:  ${Profit_Loss_Net}\n")
    outfile.write(f"Average Change:  ${average_Profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_Month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_Month} (${lowest_change})\n")