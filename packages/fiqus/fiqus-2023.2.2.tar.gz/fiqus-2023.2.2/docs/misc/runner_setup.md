# Gitlab Runner setup 

## Prerequisites

Python prerequisites are found in `requirements.txt`. 
Furthermore, the runner needs to have the `CERNGetDP` binary available (and callable from command line?) --> this step needs some thinking on how we do it. 

## Runner setup

If we can also ship `CERNGetDP` as a python package, no particular runner would be needed but the docker python image could be used (to be tested). Should this not be possible, we need to setup runners ourselves (preferably one UNIX, one Windows) as desribed in [the Gitlab documentation](https://docs.gitlab.com/runner/install/). 
