def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
    return getOrgInfo(topManager, reportOne, reportTwo).lowCommManager

# DFS


def getOrgInfo(manager, reportOne, reportTwo):
    numImpReport = 0
    for report in manager.directReports:
        orgInfo = getOrgInfo(report, reportOne, reportTwo)
        if orgInfo.lowCommManager is not None:
            return orgInfo
        numImpReport += orgInfo.numReport
    if manager == reportOne or manager == reportTwo:
        numImpReport += 1
    if numImpReport == 2:
        return OrgInfo(manager, numImpReport)
    else:
        return OrgInfo(None, numImpReport)
# This is an input class. Do not edit.


class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []


# Interface
class OrgInfo:
    def __init__(self, lowCommManager, numReport):
        self.lowCommManager = lowCommManager
        self.numReport = numReport
