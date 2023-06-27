#python3

from records.studentrecords import StudentRecords
import sys
import io
import logging
logging.basicConfig(level=logging.INFO)

if __name__=='__main__':

    SR = StudentRecords()

    # print('GPA: ', SR.get_GPA(1))
    SR.report_card(1, sys.stdout, False)
    SR.report_card(2, sys.stdout, False)

    SR.report_file(io.StringIO())
