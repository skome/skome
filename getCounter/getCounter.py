import pycounter.sushi
import datetime
weekdays = {1:"Mon",2:"Tue",3:"Wed",4:"Thu",5:"Fri",6:"Sat",7:"Sun"}
START = datetime.date(2015,1,1)
END = datetime.date(2015,4,15)
RID = "b29daa24-cc02-4760-8694-3084f90445a7"
CR = "X054213"
REP = "JR1"
REL = 4
COUNTERREP = pycounter.sushi.get_report(wsdl_url="http://sushi4.scholarlyiq.com/SushiService.svc", 
start_date=START, 
end_date=END, 
requestor_id=RID,
customer_reference=CR,
report=REP,release=REL)

for row in COUNTERREP:
    for metric in row:
        print row.title, row.eissn, row.publisher, metric[0].year, metric[0].month,metric[0].day,weekdays[metric[0].weekday()],metric[2]
