import jenkins
import matplotlib.pyplot as plt
import matplotlib
import time
import sys, getopt
from datetime import datetime



class DurationMetrics:
    username = ''
    password = ''
    totalBuildDuration = 0.0
    numberOfBuilds = 0.0
    buildDurations = []
    buildTimestamps = []
    server = None

    def __init__(self,username,password):
        self.username = "jatinkumar"
        self.password = "jatinkumar"

    def calculateAverageDuration(self):
        #TODO: calculate average duration
        averageDuration = (self.totalBuildDuration / self.numberOfBuilds) / 1000
        return averageDuration

    def getJobDuration(self):
        # TODO: get job duration
        jenkinsJobs = self.server.get_all_jobs()
        print(jenkinsJobs)
        myJob = self.server.get_job_info('Test', 0, True)
        # print("aaaaaaaaaaaa")
        # print(myJob)
        
        #print(myJob)
        #myJobBuilds = myJob.get('builds')
        myJobBuilds = []
        for job in jenkinsJobs:
            print("@@@@@@@@@@")
            jobInfo = job.get_job_info()
            myJobBuilds.append(jobInfo.get('builds'))
        print("###############################################################")
        print(myJobBuilds)

        # for build in myJobBuilds:
        #     buildNumber = build.get('number')
        #     buildInfo = self.server.get_build_info('Test', buildNumber)
        #     #print(buildInfo)
        #     buildDuration = buildInfo.get('duration')
        #     self.buildDurations.append((buildDuration / 1000))
        #     self.totalBuildDuration += buildDuration
        #     self.numberOfBuilds += 1.0
        #     buildTimestamp = buildInfo.get('timestamp')
        #     self.buildTimestamps.append(buildTimestamp)

    def connectToJenkins(self):

        # TODO: connect to Jenkins server
        self.server = jenkins.Jenkins('http://localhost:8080', username=self.username, password=self.password)
        user = self.server.get_whoami()
        version = self.server.get_version()
        print('Hello %s from Jenkins %s' % (user['fullName'], version))

    def convertTimestamps(self):
        dates = []
        for timestamp in self.buildTimestamps:
            dateTimeObj = datetime.fromtimestamp((timestamp / 1000))
            dates.append(dateTimeObj)
        return dates


def main(argv):

    username = ''
    password = ''

    try:
        opts, args = getopt.getopt(argv, "hu:p:", ["username=", "password="])
    except getopt.GetoptError:
        print
        'python Job-Duration-Metrics.py -u <username> -p <password>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print
            'python Job-Duration-Metrics.py -u <username> -p <password>'
            sys.exit()
        elif opt in ("-u", "--username"):
            username = arg
        elif opt in ("-p", "--password"):
            password = arg

    durationMetrics = DurationMetrics(username,password)
    durationMetrics.connectToJenkins()
    durationMetrics.getJobDuration()
   # print("Build Average Duration: %.2f seconds" % durationMetrics.calculateAverageDuration())
    # function to show GUI representation of job durations
    #durationMetrics.plotJobDuration()



if __name__ == "__main__":
   main(sys.argv[1:])