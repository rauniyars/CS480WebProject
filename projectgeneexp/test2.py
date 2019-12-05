import csv


with open('mycsv1.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow(['Name', 'Value1', 'Value2', 'Value3', 'Value4'])
    thewriter.writerow(['A', '21', '22', '23', '24'])
    thewriter.writerow(['B', '31', '32', '33', '34'])
    thewriter.writerow(['C', '25', '26', '27', '28'])
    thewriter.writerow(['D', '35', '36', '37', '38'])
