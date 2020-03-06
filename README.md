# TravisCI Windows Builds with PyBind

This is an attempt to create a minimal reproducer for an issue I
encountered testing
[peakingduck](https://github.com/thomasms/peakingduck) in the TravisCI
Windows environment. Python encounters trouble when trying to load an
extension library written in C++ and compiled with PyBind. At first I
thought it couldn't find the file, but now I think there may be a
dependency DLL which can not be found. See [this
discussion](https://travis-ci.community/t/failing-to-run-compiled-python-extension/7456)
on the problem.
