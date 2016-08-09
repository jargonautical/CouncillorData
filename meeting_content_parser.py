import sys
import csv

import base_parser

class MeetingContentParser(base_parser.BaseParser):

    def parse(self):
        all_data = []
        for mtg in self.soup.findAll('meeting'):
            meetingid = mtg.findParent('meetingid')
            items = meetingid.find('agendaitems').text
            all_data.append(meetingid)
        print all_data




#if __name__ == "__main__":

#    import fnmatch
#    import os

#    matches = []
#    for root, dirnames, filenames in os.walk('data'):
#        for filename in fnmatch.filter(filenames, 'CouncillorsByWard.xml'):
#            matches.append(os.path.join(root, filename))

#    all_urls = []
#    out_file = csv.writer(sys.stdout)
#    for match in matches:
#        data = MeetingContentParser(match).parse()
#        if data:
#            out_file.writerows(data)
#    data = MeetingContentParser()
#    print(data)
