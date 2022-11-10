# POC howto add comment to Jira issue
#
# 7.9.2020,3.2.2022,10.11.2022 mika.nokka1@gmail.com 
# 
# python3


import sys,argparse
from Authorization import Authenticate  # no need to use as external command
from Authorization import DoJIRAStuff

from jira import JIRA, JIRAError

__version__ = u"0.73300"



def main(argv):
    
    JIRASERVICE=u""
    JIRAPROJECT=u""
    PSWD=u''
    USER=u''
    SUMMARY=u''
    DESCRIPTION=u''
  


    parser = argparse.ArgumentParser(description="Get given Jira instance,credentials and comment data",
    
    
    epilog="""
    
    EXAMPLE:
    
    AddComment.py  -u MYUSERNAME -w MYPASSWORD -s JIRASERVICE -c COMMENT -d JIRAISSUEID"""  
    )

    parser.add_argument('-v', help='Show version&author and exit', action='version',version="Version:{0}   mika.nokka1@gmail.com ,  MIT licenced ".format(__version__) )
    
    parser.add_argument("-w",help='<JIRA Password>',metavar="password")
    parser.add_argument('-u', help='<JIRA user account>',metavar="user")
    parser.add_argument('-s', help='<JIRA service>',metavar="server_address")
    parser.add_argument('-i', help='<JIRA Issue ID>',metavar="IssueID")
    parser.add_argument('-c', help='<Commment>',metavar="IssueComment")
    parser.add_argument('-r', help='<DryRun - do nothing but emulate. Off by default>',metavar="on|off",default="off")
    parser.add_argument('-d', help='<JIRA issueID>',metavar="IssueID")


    args = parser.parse_args()
       
    JIRASERVICE = args.s or ''
    PSWD= args.w or ''
    USER= args.u or ''
    COMMENT=args.c or ''
    ISSUEID=args.i or ''
    if (args.r=="on"):
        SKIP=1
    else:
        SKIP=0    

    
    # quick old-school way to check needed parameters
    if (JIRASERVICE=='' or  PSWD=='' or USER=='' or  COMMENT=='' or  ISSUEID=='' ):
        print("\n---> MISSING ARGUMENTS!!\n ")
        parser.print_help()
        sys.exit(2)
        
     
    Authenticate(JIRASERVICE,PSWD,USER)
    jira=DoJIRAStuff(USER,PSWD,JIRASERVICE)

    AddcComment(JIRASERVICE,PSWD,USER,jira,SKIP,COMMENT,ISSUEID)
 
    
####################################################################################
def AddcComment(JIRASERVICE,PSWD,USER,jira,SKIP,COMMENT,ISSUEID):
    jiraobj=jira

    try:
        if (SKIP==1):
            print ("DRYRUN: Would have added-> issue:{0} comment:{1}".format(ISSUEID,COMMENT))
        
        else:    
            print( "Adding comment:{0} for issue: {1}".format(ISSUEID,COMMENT))
            jira.add_comment(ISSUEID, COMMENT)
    

    except Exception as e:
        print(("Failed to add comment, error: %s" % e))
        sys.exit(1)
        
        
        

if __name__ == "__main__":
        main(sys.argv[1:])



