
# coding: utf-8

# This is the script we need to run to grade students' submissions.

# In[6]:

import urllib
import json
import urllib2
import re


# In[7]:

REPO = "sahuguet/travis-python"
GIT_PULLS = "https://api.github.com/repos/%s/pulls" % REPO
GIT_STATUSES_FROM_SHA = "https://api.github.com/repos/sahuguet/travis-python/commits/%s/statuses"
GIT_COMMIT_FROM_SHA   = "https://api.github.com/repos/sahuguet/travis-python/commits/%s"
TRAVIS_LOG_FROM_ID    = "https://api.travis-ci.org/jobs/%d/logs"
TRAVIS_BUILDS_URL     = "https://api.travis-ci.org/repos/%s/builds" % REPO
TRAVIS_LOG_S3         = "https://s3.amazonaws.com/archive.travis-ci.org/jobs/%d/log.txt"

print GIT_PULLS
pull_requests = json.loads(urllib.urlopen(GIT_PULLS).read())


# In[8]:

def get_travis_url_from_git(sha):
    """Grabs the Travis URL from the git commit data."""
    url = GIT_STATUSES_FROM_SHA % sha
    statuses = json.loads(urllib.urlopen(url).read())
    return statuses[0]['target_url']

def get_modified_files_from_git(sha):
    """Grabs the set of modified files from the git commit data."""
    url = GIT_COMMIT_FROM_SHA % sha
    print url
    commit = json.loads(urllib.urlopen(url).read())
    return map(lambda x:x['filename'], commit['files'])



# In[9]:

def get_pytest_report_from_s3(id):
    """Retrieves the raw log data from S3, based on job id."""
    url = TRAVIS_LOG_S3 % int(id)
    print id
    log_data = urllib.urlopen(url).read()
    slices = re.split("<MQkrXV>", log_data)
    if len(slices)>1:
        pytest_report = json.loads(slices[3].strip())
    else:
        pytest_report = {}
    return pytest_report

def get_travis_builds():
    """Retrieves the Travis build for a given repository."""
    url = TRAVIS_BUILDS_URL
    headers = { 'User-Agent': 'MyClient/1.0.0', 'Accept': 'application/vnd.travis-ci.2+json'}
    req = urllib2.Request(url, headers = headers)
    travis_data = json.loads(urllib2.urlopen(req).read())
    return travis_data['builds']

def get_travis_jobid(builds, build_id):
    for build in builds:
        if build['id'] == build_id:
            return int(build['job_ids'][0])


# In[10]:

print "%d submission(s)." % len(pull_requests)
TRAVIS_BUILDS = get_travis_builds()
SUBMISSIONS = []

for r in pull_requests:
    user = r['user']['login']
    timestamp = r['updated_at']
    sha = r['head']['sha']
    travis_data = get_travis_url_from_git(sha)
    modified_files = get_modified_files_from_git(sha)
    build_id = int(travis_data.split('/')[-1])
    job_id = get_travis_jobid(TRAVIS_BUILDS, build_id)
    SUBMISSIONS.append( {'user': user, 'sha': sha, 'timestamp': timestamp,
                         'modified_files': modified_files,
                         'travis': travis_data,
                         'travis_job_id': job_id,
                         'pytest_report': get_pytest_report_from_s3(job_id)
                        })
print json.dumps(SUBMISSIONS, sort_keys=True, indent=2,)


# In[11]:

get_pytest_report_from_s3(153338568)


# In[12]:

def get_pytest_report_from_s3_(id):
    """Retrieves the raw log data from S3, based on job id."""
    url = TRAVIS_LOG_S3 % int(id)
    print id
    log_data = urllib.urlopen(url).read()
    return log_data


# In[13]:

a = get_pytest_report_from_s3_(153338568)


# In[14]:

slices = re.split("<~~~~>", a)
print len(slices)


# In[ ]:



