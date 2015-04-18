import pycounter.sushi
import datetime

report = pycounter.sushi.get_report(wsdl_url="http://sushi4.scholarlyiq.com/SushiService.svc", start_date=datetime.date(2015,1,1), enddate=datetime.date(2015,4,15), requestor_id="b29daa24-cc02-4760-8694-3084f90445a7",customer_reference="X054213",report="JR1",release=4)

for row in report:
    for metric in row:
        print row.title, row.eissn, row.publisher, metric[0],metric[2]
