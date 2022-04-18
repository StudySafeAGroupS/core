# Study Safe Group S

## Vision Statement
For the COVID Task Force team who needs to identify HKU close contacts of any member testing positive for the SARS-CoV-2 virus, the StudySafe System is an application that records entries and exits of HKU members and outputs a list of members or venues who have been in close contacts with tested-positive members.

Unlike the current Attendance@HKU application, members attending the venues, using the
StudySafe System, would not need to download the application as attendances are recorded by devices placed at the venues’ entry/exit points. HKU students registered in a class are not automatically flagged as an attendee as in the existing application, thus increasing the accuracy. Furthermore, task forces members can quickly query the venues/members who have close contact with tested-positive members through StudySafe Trace.


## Code Standards for Commits
### Environment
1. The minimum Python version supported is 3.10
2. Your code is expected to be executable in Windows, MacOS and Linux

### Name Conventions
1. Always use snake_case for variable, and use CamelCase for class names.
2. Try at all costs to give a proper, clear name to your classes, functions, arguments, and variables, from which the user can directly understand their purposes.
3. Class initialization and function calls should use named arguments.

### Code Commits
1. Create a branch for each functionality that you are working on. Submit a Pull Request to master branch to merge.
## GitHub
```sh
gh repo clone StudySafeAGroupS/core
```

## Heroku
```sh
mkdir heroku
cd heroku
heroku login
heroku create
heroku config:set DISABLE_COLLECTSTATIC=1 -a {Heroku_app_name}
git init
heroku git:remote -a {Heroku_app_name}
git fetch --all
```