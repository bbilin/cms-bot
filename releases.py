from milestones import *

#Default development branch
# Changes from master branch will be merge in to it
# Any PR open against this will be automatically closed by cms-bot (Pr should be made for master branch)
# For new release cycle just change this and make sure to add its milestone and production branches
CMSSW_DEVEL_BRANCH = "CMSSW_10_2_X"

RELEASE_BRANCH_MILESTONE["master"]=RELEASE_BRANCH_MILESTONE[CMSSW_DEVEL_BRANCH]
RELEASE_BRANCH_PRODUCTION.append("master")
USERS_TO_TRIGGER_HOOKS = set(SPECIAL_RELEASE_MANAGERS + [ m for rel in RELEASE_MANAGERS for m in rel ])

